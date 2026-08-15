const express = require("express");
const { validateCoupon } = require("../lib/coupon");

const router = express.Router();

// POST /api/coupons/validate — live preview at checkout, before placing the order
router.post("/validate", async (req, res, next) => {
  try {
    const { code, subtotal } = req.body;
    if (typeof subtotal !== "number" || subtotal < 0) {
      return res.status(400).json({ error: "subtotal is required" });
    }
    const result = await validateCoupon(code, subtotal);
    res.json(result);
  } catch (err) {
    next(err);
  }
});

module.exports = router;
