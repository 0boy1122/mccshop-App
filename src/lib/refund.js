async function refundPaystackCharge(reference) {
  const res = await fetch("https://api.paystack.co/refund", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.PAYSTACK_SECRET_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ transaction: reference }),
  });
  const data = await res.json();
  if (!res.ok || data.status === false) {
    throw new Error(data.message || "Refund could not be processed");
  }
  return data;
}

async function refundStripeCharge(sessionId) {
  const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
  const session = await stripe.checkout.sessions.retrieve(sessionId);
  if (!session.payment_intent) throw new Error("No payment found to refund");
  return stripe.refunds.create({ payment_intent: session.payment_intent });
}

module.exports = { refundPaystackCharge, refundStripeCharge };
