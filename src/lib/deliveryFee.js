const { haversineKm } = require("./geo");
const { SHOP_ORIGIN } = require("./shopLocation");

// Used when we have no delivery coordinates at all (customer denied location
// permission, or typed an address with no pin) — better than nothing, but
// distance-based pricing below is the real fee whenever we have a pin.
const FLAT_FALLBACK_FEES = {
  BIKE: 20,
  VAN: 60,
  PICKUP: 0,
};

// Base covers the trip to the nearest customers; per-km covers everyone further out.
// Bike is cheaper but only realistic for shorter/lighter runs; van costs more
// per trip but is the only option once distance or bulk makes a bike impractical.
const DISTANCE_PRICING = {
  BIKE: { base: 10, perKm: 2.5, maxKm: 20 },
  VAN: { base: 25, perKm: 4, maxKm: 60 },
};

function calculateDeliveryFee({ vehicleType, deliveryLat, deliveryLng } = {}) {
  const safeType = ["BIKE", "VAN", "PICKUP"].includes(vehicleType) ? vehicleType : "BIKE";
  if (safeType === "PICKUP") return { fee: 0, distanceKm: null, method: "PICKUP" };

  const hasPin = typeof deliveryLat === "number" && typeof deliveryLng === "number" && !Number.isNaN(deliveryLat) && !Number.isNaN(deliveryLng);
  if (!hasPin) {
    return { fee: FLAT_FALLBACK_FEES[safeType], distanceKm: null, method: "FLAT_FALLBACK" };
  }

  const distanceKm = haversineKm(SHOP_ORIGIN, { lat: deliveryLat, lng: deliveryLng });
  const pricing = DISTANCE_PRICING[safeType];
  if (distanceKm > pricing.maxKm) {
    // Out of realistic range for this vehicle — caller should nudge the customer toward VAN, or we just charge for the max tier.
    return { fee: Math.round(pricing.base + pricing.perKm * pricing.maxKm), distanceKm, method: "DISTANCE", outOfRange: true };
  }

  const fee = Math.round(pricing.base + pricing.perKm * distanceKm);
  return { fee, distanceKm: Math.round(distanceKm * 10) / 10, method: "DISTANCE" };
}

module.exports = { calculateDeliveryFee };
