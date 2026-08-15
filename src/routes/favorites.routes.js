const express = require("express");
const prisma = require("../lib/prisma");
const { authenticate } = require("../middleware/auth.middleware");

const router = express.Router();

// All favorites routes require a logged-in customer
router.use(authenticate);

// GET /api/favorites — my favorited products
router.get("/", async (req, res, next) => {
  try {
    const favorites = await prisma.favorite.findMany({
      where: { userId: req.user.id },
      include: { product: true },
      orderBy: { createdAt: "desc" },
    });
    const products = favorites
      .filter((f) => f.product.isPublished)
      .map(({ product }) => {
        const { costPrice: _, ...safe } = product;
        return safe;
      });
    res.json({ products });
  } catch (err) {
    next(err);
  }
});

// POST /api/favorites/:productId — add to favorites
router.post("/:productId", async (req, res, next) => {
  try {
    const product = await prisma.product.findUnique({ where: { id: req.params.productId } });
    if (!product) return res.status(404).json({ error: "Product not found" });

    await prisma.favorite.upsert({
      where: { userId_productId: { userId: req.user.id, productId: req.params.productId } },
      update: {},
      create: { userId: req.user.id, productId: req.params.productId },
    });
    res.status(201).json({ favorited: true });
  } catch (err) {
    next(err);
  }
});

// DELETE /api/favorites/:productId — remove from favorites
router.delete("/:productId", async (req, res, next) => {
  try {
    await prisma.favorite.deleteMany({
      where: { userId: req.user.id, productId: req.params.productId },
    });
    res.json({ favorited: false });
  } catch (err) {
    next(err);
  }
});

module.exports = router;
