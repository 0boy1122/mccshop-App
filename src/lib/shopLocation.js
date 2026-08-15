// Dispatch origin for delivery-fee distance calculations.
// Set SHOP_LAT / SHOP_LNG in .env to the real showroom/warehouse coordinates
// once known — until then this falls back to Accra's city-center coordinate,
// which is directionally fine but will under/overstate distance depending on
// which part of Accra the showroom is actually in.
const SHOP_ORIGIN = {
  lat: process.env.SHOP_LAT ? Number(process.env.SHOP_LAT) : 5.6037,
  lng: process.env.SHOP_LNG ? Number(process.env.SHOP_LNG) : -0.187,
};

module.exports = { SHOP_ORIGIN };
