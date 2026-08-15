const express = require("express");
const { calculateDeliveryFee } = require("../lib/deliveryFee");

const router = express.Router();

// POST /api/delivery/estimate — live fee preview for checkout, before the order exists.
router.post("/estimate", (req, res) => {
  const { vehicleType, deliveryLat, deliveryLng } = req.body;
  const result = calculateDeliveryFee({
    vehicleType,
    deliveryLat: typeof deliveryLat === "number" ? deliveryLat : undefined,
    deliveryLng: typeof deliveryLng === "number" ? deliveryLng : undefined,
  });
  res.json(result);
});

module.exports = router;
