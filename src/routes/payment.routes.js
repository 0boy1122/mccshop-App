const express = require("express");
const crypto = require("crypto");
const prisma = require("../lib/prisma");
const { authenticate } = require("../middleware/auth.middleware");
const { notifyOrderStatus } = require("../lib/notify");
const { refundPaystackCharge } = require("../lib/refund");

const router = express.Router();

const MOMO_PROVIDERS = ["mtn", "vodafone", "atl"];

// Normalize a Ghana phone number to the local 0XXXXXXXXX format Paystack expects
function normalizeGhanaPhone(raw) {
  const digits = String(raw || "").replace(/\D/g, "");
  if (digits.startsWith("233") && digits.length === 12) return `0${digits.slice(3)}`;
  if (digits.length === 9) return `0${digits}`;
  return digits; // already 0XXXXXXXXX, or let Paystack reject an invalid one
}

// POST /api/payments/initiate
router.post("/initiate", authenticate, async (req, res, next) => {
  try {
    const { orderId, method, momoPhone, momoProvider } = req.body;

    if (!orderId || !method) {
      return res.status(400).json({ error: "orderId and method are required" });
    }

    const order = await prisma.order.findUnique({ where: { id: orderId } });
    if (!order) return res.status(404).json({ error: "Order not found" });
    if (order.userId !== req.user.id) return res.status(403).json({ error: "Access denied" });

    const existingPayment = await prisma.payment.findUnique({ where: { orderId } });
    if (existingPayment && existingPayment.status === "SUCCESS") {
      return res.status(409).json({ error: "Order already paid" });
    }

    let paymentData = {};

    if (method === "MOMO") {
      const provider = MOMO_PROVIDERS.includes(momoProvider) ? momoProvider : "mtn";
      const phone = normalizeGhanaPhone(momoPhone || req.user.phone);

      const paystackRes = await fetch("https://api.paystack.co/charge", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.PAYSTACK_SECRET_KEY}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: req.user.email || `${req.user.phone}@mccshop.com`,
          amount: Math.round(order.total * 100),
          currency: "GHS",
          mobile_money: { phone, provider },
        }),
      });
      const paystackData = await paystackRes.json();
      if (!paystackRes.ok || paystackData.status === false) {
        return res.status(502).json({ error: paystackData.message || "MoMo charge could not be started" });
      }
      paymentData = { reference: paystackData.data?.reference, checkoutUrl: null, provider: "paystack" };
    } else if (method === "CARD") {
      const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
      const session = await stripe.checkout.sessions.create({
        payment_method_types: ["card"],
        line_items: [{
          price_data: {
            currency: "ghs",
            product_data: { name: `MCC Shop Order #${orderId.slice(0, 8)}` },
            unit_amount: Math.round(order.total * 100),
          },
          quantity: 1,
        }],
        mode: "payment",
        success_url: `${process.env.CLIENT_URL}/orders/${orderId}?paid=true`,
        cancel_url: `${process.env.CLIENT_URL}/orders/${orderId}?paid=false`,
        metadata: { orderId },
      });
      paymentData = { reference: session.id, checkoutUrl: session.url, provider: "stripe" };
    } else {
      return res.status(400).json({ error: "Invalid payment method. Use MOMO or CARD" });
    }

    const payment = await prisma.payment.upsert({
      where: { orderId },
      update: { method, reference: paymentData.reference, momoPhone },
      create: { orderId, method, status: "PENDING", amount: order.total, reference: paymentData.reference, momoPhone },
    });

    res.json({ payment, ...paymentData });
  } catch (err) {
    next(err);
  }
});

// POST /api/payments/webhook
router.post("/webhook", express.raw({ type: "application/json" }), async (req, res, next) => {
  try {
    // ── Paystack Webhook ─────────────────────────────────
    if (req.headers["x-paystack-signature"]) {
      const secret = process.env.PAYSTACK_SECRET_KEY;
      if (!secret) return res.sendStatus(500);

      // Verify HMAC-SHA512 signature — prevents anyone faking a payment confirmation
      const expected = crypto
        .createHmac("sha512", secret)
        .update(req.body)
        .digest("hex");

      if (req.headers["x-paystack-signature"] !== expected) {
        return res.status(401).send("Invalid signature");
      }

      const event = JSON.parse(req.body);
      if (event.event === "charge.success") {
        const reference = event.data?.reference;
        if (!reference) return res.sendStatus(400);
        const payment = await prisma.payment.findUnique({ where: { reference } });
        if (payment) {
          const order = await prisma.order.findUnique({ where: { id: payment.orderId } });
          if (order?.status === "CANCELLED") {
            // The customer self-cancelled while this MoMo approval was still in
            // flight — the charge went through anyway. Refund it immediately
            // instead of silently re-confirming an order they already walked away from.
            await prisma.payment.update({ where: { reference }, data: { status: "SUCCESS" } });
            try {
              await refundPaystackCharge(reference);
              await prisma.payment.update({ where: { reference }, data: { status: "REFUNDED" } });
            } catch (e) {
              console.error("Auto-refund of late charge on a cancelled order failed:", e.message);
            }
            return res.sendStatus(200);
          }
          await prisma.payment.update({ where: { reference }, data: { status: "SUCCESS" } });
          const updatedOrder = await prisma.order.update({ where: { id: payment.orderId }, data: { status: "CONFIRMED" } });
          const io = req.app.get("io");
          if (io) io.to(`order:${payment.orderId}`).emit("order:status", { orderId: payment.orderId, status: "CONFIRMED" });
          await notifyOrderStatus(io, updatedOrder);
        }
      } else if (event.event === "charge.failed") {
        // MoMo declined/expired — release the stock reserved when the order was placed
        const reference = event.data?.reference;
        if (!reference) return res.sendStatus(400);
        const payment = await prisma.payment.findUnique({ where: { reference } });
        if (payment && payment.status !== "SUCCESS") {
          const order = await prisma.order.findUnique({ where: { id: payment.orderId }, include: { items: true } });
          if (order && order.status === "PENDING") {
            await prisma.$transaction(async (tx) => {
              await tx.payment.update({ where: { reference }, data: { status: "FAILED" } });
              await tx.order.update({ where: { id: order.id }, data: { status: "CANCELLED" } });
              for (const item of order.items) {
                await tx.product.update({ where: { id: item.productId }, data: { stockQty: { increment: item.quantity } } });
              }
            });
            const io = req.app.get("io");
            if (io) io.to(`order:${order.id}`).emit("order:status", { orderId: order.id, status: "CANCELLED" });
            await notifyOrderStatus(io, { ...order, status: "CANCELLED" });
          } else {
            await prisma.payment.update({ where: { reference }, data: { status: "FAILED" } });
          }
        }
      }
      return res.sendStatus(200);
    }

    // ── Stripe Webhook ───────────────────────────────────
    if (req.headers["stripe-signature"]) {
      const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
      const event = stripe.webhooks.constructEvent(
        req.body,
        req.headers["stripe-signature"],
        process.env.STRIPE_WEBHOOK_SECRET
      );
      if (event.type === "checkout.session.completed") {
        const session = event.data.object;
        const orderId = session.metadata.orderId;
        await prisma.payment.update({ where: { reference: session.id }, data: { status: "SUCCESS" } });
        await prisma.order.update({ where: { id: orderId }, data: { status: "CONFIRMED" } });
      }
      return res.sendStatus(200);
    }

    res.sendStatus(400);
  } catch (err) {
    next(err);
  }
});

// GET /api/payments/:orderId  — owner or admin only
router.get("/:orderId", authenticate, async (req, res, next) => {
  try {
    const payment = await prisma.payment.findUnique({
      where: { orderId: req.params.orderId },
      include: { order: { select: { userId: true } } },
    });
    if (!payment) return res.status(404).json({ error: "Payment not found" });

    if (req.user.role === "CUSTOMER" && payment.order.userId !== req.user.id) {
      return res.status(403).json({ error: "Access denied" });
    }

    const { order: _, ...safePayment } = payment;
    res.json({ payment: safePayment });
  } catch (err) {
    next(err);
  }
});

module.exports = router;
