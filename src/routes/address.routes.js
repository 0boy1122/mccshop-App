const express = require("express");
const prisma = require("../lib/prisma");
const { authenticate } = require("../middleware/auth.middleware");

const router = express.Router();

// All address routes require a logged-in customer
router.use(authenticate);

// GET /api/addresses — my saved delivery addresses, default first
router.get("/", async (req, res, next) => {
  try {
    const addresses = await prisma.savedAddress.findMany({
      where: { userId: req.user.id },
      orderBy: [{ isDefault: "desc" }, { createdAt: "desc" }],
    });
    res.json({ addresses });
  } catch (err) {
    next(err);
  }
});

// POST /api/addresses — save a new delivery address
router.post("/", async (req, res, next) => {
  try {
    const { label, address, landmark, lat, lng, isDefault } = req.body;
    if (!label || typeof label !== "string" || !label.trim()) {
      return res.status(400).json({ error: "A label is required (e.g. Home, Site office)" });
    }
    if (!address || typeof address !== "string" || !address.trim()) {
      return res.status(400).json({ error: "Address is required" });
    }

    const saved = await prisma.$transaction(async (tx) => {
      if (isDefault) {
        await tx.savedAddress.updateMany({ where: { userId: req.user.id }, data: { isDefault: false } });
      }
      return tx.savedAddress.create({
        data: {
          userId: req.user.id,
          label: label.trim().slice(0, 40),
          address: address.trim().slice(0, 300),
          landmark: landmark ? String(landmark).trim().slice(0, 200) : null,
          lat: typeof lat === "number" ? lat : null,
          lng: typeof lng === "number" ? lng : null,
          isDefault: !!isDefault,
        },
      });
    });

    res.status(201).json({ address: saved });
  } catch (err) {
    next(err);
  }
});

// PATCH /api/addresses/:id/default — make this the default address
router.patch("/:id/default", async (req, res, next) => {
  try {
    const existing = await prisma.savedAddress.findUnique({ where: { id: req.params.id } });
    if (!existing || existing.userId !== req.user.id) {
      return res.status(404).json({ error: "Address not found" });
    }

    await prisma.$transaction([
      prisma.savedAddress.updateMany({ where: { userId: req.user.id }, data: { isDefault: false } }),
      prisma.savedAddress.update({ where: { id: req.params.id }, data: { isDefault: true } }),
    ]);

    res.json({ ok: true });
  } catch (err) {
    next(err);
  }
});

// DELETE /api/addresses/:id
router.delete("/:id", async (req, res, next) => {
  try {
    await prisma.savedAddress.deleteMany({ where: { id: req.params.id, userId: req.user.id } });
    res.json({ ok: true });
  } catch (err) {
    next(err);
  }
});

module.exports = router;
