const express = require("express");
const { GoogleGenerativeAI } = require("@google/generative-ai");

const router = express.Router();

// Initialize Gemini API
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || "YOUR_GEMINI_API_KEY");

const PRODUCT_CONTEXT = `You are the MCC Shop AI assistant — a helpful, knowledgeable, and friendly shopping guide for The MCC Shop, Ghana's premier building materials, decor, home & office furniture, tools and equipment delivery service in Accra.

ABOUT MCC SHOP:
- Delivers to all of Accra (home, office, construction sites)
- Delivery modes: Bike (small items), Van (medium/bulky), Pickup (collect from the showroom, free)
- All prices are VAT inclusive, in GHS
- Bulk discounts available above per-product threshold quantities

CATEGORIES CARRIED: Paints, Boards, Panels, Furniture (including the premium GECHI showroom line — sofas, beds, dining sets, mattresses), Office furniture, Tools, Electrical, Plumbing, Hardware, Safety equipment, Adhesives.

IMPORTANT — you do not have live access to exact current prices, stock levels, or the full product list. Never state a specific price or say an item is in/out of stock — always direct the person to the Shop tab to search and see live pricing and availability, or ask what they're looking for so you can point them to the right category.

ORDERING: This is a full shopping app — customers browse, add to cart, and pay directly in-app via Mobile Money (MTN, Vodafone Cash, or AirtelTigo Money) at checkout. There is no need to order via WhatsApp; only mention WhatsApp if someone asks for human support or something outside what the app can do.

PERSONALITY: Be warm, helpful, concise. Speak like a knowledgeable Ghanaian shop assistant. Use GHS for currency. Keep responses short (2-4 sentences max). If asked about something not carried, say the team may be able to source it and suggest contacting support.`;

// POST /api/ai/chat
router.post("/chat", async (req, res, next) => {
  try {
    const { messages } = req.body;
    if (!messages || !Array.isArray(messages)) {
      return res.status(400).json({ error: "Invalid messages format" });
    }
    if (messages.length > 20) {
      return res.status(400).json({ error: "Too many messages in conversation" });
    }
    for (const msg of messages) {
      if (typeof msg.content !== "string" || msg.content.length > 2000) {
        return res.status(400).json({ error: "Message too long (max 2000 characters)" });
      }
    }

    // Configure the model. Use the "-latest" alias, not a pinned version —
    // pinned model names get retired by Google over time (this is exactly
    // what broke here: gemini-1.5-flash no longer exists) and the alias
    // is what Google maintains to keep pointing at a current fast model.
    const model = genAI.getGenerativeModel({
      model: "gemini-flash-latest",
      systemInstruction: PRODUCT_CONTEXT
    });

    // Format history for Gemini (gemini uses role: "user" | "model").
    // Gemini rejects history that doesn't start with "user" — drop any
    // leading assistant/model turns (e.g. a client-side canned greeting)
    // rather than 500ing on a shape mismatch.
    const priorTurns = messages.slice(0, -1);
    const firstUserIndex = priorTurns.findIndex(msg => msg.role !== "assistant" && msg.role !== "model");
    const history = (firstUserIndex === -1 ? [] : priorTurns.slice(firstUserIndex)).map(msg => ({
      role: msg.role === "assistant" ? "model" : "user",
      parts: [{ text: msg.content }]
    }));

    const latestMessage = messages[messages.length - 1].content;

    // Start a chat session
    const chat = model.startChat({ history });
    
    // Send the latest message
    const result = await chat.sendMessage(latestMessage);
    const reply = result.response.text();
    
    res.json({ reply });
  } catch (err) {
    console.error("AI Error:", err);
    res.status(500).json({ error: "Failed to generate AI response. Please try again." });
  }
});

module.exports = router;
