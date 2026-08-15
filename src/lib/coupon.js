const prisma = require("./prisma");

// Shared by the /coupons/validate preview endpoint and real order creation,
// so a coupon can never be "valid" in the UI but rejected/miscalculated
// when the order is actually placed.
async function validateCoupon(code, subtotal) {
  if (!code) return { valid: false, message: "No coupon code given" };

  const coupon = await prisma.coupon.findUnique({ where: { code: code.trim().toUpperCase() } });
  if (!coupon || !coupon.active) return { valid: false, message: "Coupon not found" };
  if (coupon.expiresAt && coupon.expiresAt < new Date()) return { valid: false, message: "Coupon has expired" };
  if (coupon.maxUses != null && coupon.usedCount >= coupon.maxUses) return { valid: false, message: "Coupon has been fully redeemed" };
  if (subtotal < coupon.minOrderValue) {
    return { valid: false, message: `Minimum order of GHS ${coupon.minOrderValue} required` };
  }

  const discount = coupon.discountType === "PERCENT"
    ? Math.round(subtotal * (coupon.discountValue / 100) * 100) / 100
    : Math.min(coupon.discountValue, subtotal);

  return { valid: true, discount, coupon };
}

module.exports = { validateCoupon };
