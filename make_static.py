#!/usr/bin/env python3
"""Convert index.html to a fully static site — no backend required."""

HTML = r"c:\Users\dell\OneDrive\Desktop\mcc shop\backend\mcc-shop-backend\public\index.html"

with open(HTML, encoding="utf-8") as f:
    content = f.read()

# ── 1. Replace FALLBACK_PRODUCTS ─────────────────────────────────────────────
OLD_FB_START = "FALLBACK_PRODUCTS = ["
OLD_FB_END   = "\n    ];"

fb_start = content.find(OLD_FB_START)
fb_end   = content.find(OLD_FB_END, fb_start) + len(OLD_FB_END)

NEW_FALLBACK = r"""FALLBACK_PRODUCTS = [
      // ── Paints ──────────────────────────────────────────────────────
      { skuCode:"PNT-EMU-001",  name:"MCC Standard Emulsion Paint",          category:"Paints",    unitSize:"20 Litres",  sellingPrice:300,   bulkThreshold:5,  bulkPrice:280,   dispatchMode:"VAN",  images:"/mcc_emulsion_paint.jpeg", notes:"colours:White,Magnolia,Ivory,Grey,Broken White", mvpPriority:true  },
      { skuCode:"PNT-ACR-001",  name:"MCC Acrylic Premium Emulsion Paint",    category:"Paints",    unitSize:"20 Litres",  sellingPrice:650,   bulkThreshold:3,  bulkPrice:620,   dispatchMode:"VAN",  images:"/acrylic_paint.jpg",       notes:"colours:White,Magnolia,Ivory,Grey,Broken White", mvpPriority:true  },
      { skuCode:"PNT-OIL-001",  name:"Oil Paint",                             category:"Paints",    unitSize:"4 Litres",   sellingPrice:200,   bulkThreshold:10, bulkPrice:185,   dispatchMode:"BIKE", images:"/oil_paint.png",            notes:"colours:White,Dark Brown,Dark Grey",             mvpPriority:true  },
      { skuCode:"PNT-THIN-001", name:"Paint Thinner",                         category:"Paints",    unitSize:"4 Litres",   sellingPrice:150,   bulkThreshold:10, bulkPrice:135,   dispatchMode:"BIKE", images:"/paint_thinner.jpg",        mvpPriority:false },
      // ── Boards ──────────────────────────────────────────────────────
      { skuCode:"PLB-9MM-001",  name:"Plasterboard 9mm",                      category:"Boards",    unitSize:"Sheet",      sellingPrice:150,   bulkThreshold:20, bulkPrice:135,   dispatchMode:"VAN",  images:"/plasterboard_9mm.jpg",     mvpPriority:true  },
      { skuCode:"PLB-12MM-001", name:"Plasterboard 12mm",                     category:"Boards",    unitSize:"Sheet",      sellingPrice:200,   bulkThreshold:20, bulkPrice:180,   dispatchMode:"VAN",  images:"/plasterboard_12mm.jpg",    mvpPriority:true  },
      { skuCode:"JNT-CMP-001",  name:"Joint Compound",                        category:"Boards",    unitSize:"20 Litres",  sellingPrice:350,   bulkThreshold:5,  bulkPrice:320,   dispatchMode:"VAN",  images:"/joint_compound.jpg",       mvpPriority:true  },
      { skuCode:"JNT-PWD-001",  name:"Joint Powder",                          category:"Boards",    unitSize:"25kg Bag",   sellingPrice:350,   bulkThreshold:5,  bulkPrice:320,   dispatchMode:"VAN",  images:"/skimming_powder.jpg",      mvpPriority:true  },
      // ── Panels ──────────────────────────────────────────────────────
      { skuCode:"PVC-PNL-001",  name:"PVC Ceiling Panels",                    category:"Panels",    unitSize:"Per Piece",  sellingPrice:60,    bulkThreshold:50, bulkPrice:55,    dispatchMode:"VAN",  images:"/ceiling_panel.jpeg",       notes:"colours:White,Brown",                           mvpPriority:true  },
      { skuCode:"PVC-BD-001",   name:"PVC Ceiling Boards",                    category:"Panels",    unitSize:"Per Sheet",  sellingPrice:40,    bulkThreshold:50, bulkPrice:36,    dispatchMode:"VAN",  images:"/pvc_ceiling_board.jpg",    mvpPriority:false },
      { skuCode:"WCL-001",      name:"Wall Cladding",                         category:"Panels",    unitSize:"Per m²",     sellingPrice:150,   bulkThreshold:20, bulkPrice:135,   dispatchMode:"VAN",  images:"/wall_cladding.jpg",        mvpPriority:false },
      // ── Furniture — Sofas ───────────────────────────────────────────
      { skuCode:"SFA-FAB-3S",   name:"3-Seater Fabric Sofa",                  category:"Furniture", unitSize:"Unit",       sellingPrice:2500,  bulkThreshold:2,  bulkPrice:2400,  dispatchMode:"VAN",  images:"/sofa_fabric_3s.jpg",       mvpPriority:true  },
      { skuCode:"SFA-FAB-LS",   name:"L-Shaped Fabric Sofa",                  category:"Furniture", unitSize:"Unit",       sellingPrice:4600,  bulkThreshold:2,  bulkPrice:4400,  dispatchMode:"VAN",  images:"/sofa_fabric_ls.jpg",       mvpPriority:true  },
      { skuCode:"SFA-LEA-LS",   name:"L-Shaped Half Leather Sofa",            category:"Furniture", unitSize:"Unit",       sellingPrice:7000,  bulkThreshold:2,  bulkPrice:6700,  dispatchMode:"VAN",  images:"/sofa_leather_ls.jpg",      mvpPriority:true  },
      { skuCode:"SFA-LEA-LUX",  name:"Full Leather Luxury Sofa",              category:"Furniture", unitSize:"Unit",       sellingPrice:15000, bulkThreshold:2,  bulkPrice:14500, dispatchMode:"VAN",  images:"/sofa_leather_lux.jpg",     mvpPriority:true  },
      // ── Furniture — Beds & Mattresses ───────────────────────────────
      { skuCode:"BED-UPH-QN",   name:"Queen Size Upholstered Bed",            category:"Furniture", unitSize:"Unit",       sellingPrice:2000,  bulkThreshold:2,  bulkPrice:1900,  dispatchMode:"VAN",  images:"/bed_queen.jpg",            mvpPriority:true  },
      { skuCode:"MAT-QN-001",   name:"Queen Size Mattress",                   category:"Furniture", unitSize:"Unit",       sellingPrice:1400,  bulkThreshold:2,  bulkPrice:1350,  dispatchMode:"VAN",  images:"/mattress.jpg",             mvpPriority:true  },
      { skuCode:"BED-UPH-KG",   name:"King Size Upholstered Bed",             category:"Furniture", unitSize:"Unit",       sellingPrice:4000,  bulkThreshold:2,  bulkPrice:3800,  dispatchMode:"VAN",  images:"/bed_king.jpg",             mvpPriority:true  },
      { skuCode:"MAT-KG-001",   name:"King Size Mattress",                    category:"Furniture", unitSize:"Unit",       sellingPrice:2000,  bulkThreshold:2,  bulkPrice:1900,  dispatchMode:"VAN",  images:"/mattress.jpg",             mvpPriority:true  },
      // ── Furniture — Dining ──────────────────────────────────────────
      { skuCode:"DIN-4ST-001",  name:"4-Seater Dining Set",                   category:"Furniture", unitSize:"Set",        sellingPrice:4500,  bulkThreshold:2,  bulkPrice:4300,  dispatchMode:"VAN",  images:"/dining_4s.jpg",            mvpPriority:true  },
      { skuCode:"DIN-6ST-001",  name:"6-Seater Dining Set",                   category:"Furniture", unitSize:"Set",        sellingPrice:6000,  bulkThreshold:2,  bulkPrice:5700,  dispatchMode:"VAN",  images:"/dining_6s.jpg",            mvpPriority:true  },
      { skuCode:"DIN-LUX-001",  name:"Marble / Ceramic Luxury Dining Set",   category:"Furniture", unitSize:"Set",        sellingPrice:8000,  bulkThreshold:2,  bulkPrice:7600,  dispatchMode:"VAN",  images:"/dining_luxury.jpg",        mvpPriority:true  },
    ];"""

content = content[:fb_start] + NEW_FALLBACK + content[fb_end:]
print(f"[1] FALLBACK_PRODUCTS replaced — {len(NEW_FALLBACK)} chars")

# ── 2. Remove the API fetch block, use static data directly ──────────────────
OLD_FETCH = """    // Show skeleton placeholders while loading
    showSkeletons();

    // Load live products from the API
    try {
      const res = await fetch('/api/products?limit=100');
      if (!res.ok) throw new Error(`API ${res.status}`);
      const data = await res.json();
      if (data.products && data.products.length > 0) {
        P = data.products.map(mapProduct);
        console.log(`Loaded ${P.length} products from API`);
      } else {
        throw new Error('Empty product list');
      }
    } catch(err) {
      console.warn('API unavailable, using fallback products:', err.message);
      P = FALLBACK_PRODUCTS.map(mapProduct);
    }"""

NEW_FETCH = """    // Static product catalogue — served without a backend
    showSkeletons();
    P = FALLBACK_PRODUCTS.map(mapProduct);"""

if OLD_FETCH in content:
    content = content.replace(OLD_FETCH, NEW_FETCH)
    print("[2] API fetch block replaced with static load")
else:
    print("[2] WARNING: fetch block not found — check manually")

# ── 3. Replace callClaude with a smart static responder ─────────────────────
OLD_CLAUDE = """async function callClaude(userMsg){
  const messages = [
    ...aiHistory.filter(m=>m.role!=='assistant'||aiHistory.indexOf(m)>aiHistory.length-10).slice(-16),
    {role:'user', content: userMsg}
  ];
  const res = await fetch('/api/ai/chat',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({
      system: buildProductContext(),
      messages: messages
    })
  });
  const data = await res.json();
  return data.reply || 'Sorry, I couldn\'t process that. Please try again or contact us on WhatsApp at +233 303 978 485.';
}"""

NEW_CLAUDE = r"""async function callClaude(userMsg){
  const q = userMsg.toLowerCase();
  const wa = '+233303978485';
  // Keyword-based static responses
  if(/price|cost|how much|ghs|cedis/.test(q)){
    return "Our prices are shown on each product card and are VAT inclusive. Browse the catalogue above, add items to your cart, then tap the WhatsApp button to get a final quote including delivery. Call/WhatsApp us on +233 303 978 485.";
  }
  if(/sofa|couch|leather|fabric|living/.test(q)){
    return "We carry fabric and leather sofas — 3-seater, L-shaped, and full luxury sets. Prices from GHS 2,500. All are delivered by van across Accra. Tap any sofa card to see details, or WhatsApp us on +233 303 978 485 to discuss options.";
  }
  if(/bed|mattress|bedroom|king|queen/.test(q)){
    return "We have Queen and King size upholstered beds (GHS 2,000–GHS 4,000) and matching mattresses. WhatsApp us on +233 303 978 485 to place an order or ask about bundles.";
  }
  if(/dining|table|chair|eat/.test(q)){
    return "Our dining sets come in 4-seater, 6-seater, and marble/ceramic luxury options — from GHS 4,500. WhatsApp +233 303 978 485 for availability and delivery.";
  }
  if(/paint|emulsion|acrylic|oil|colour|color|white|magnolia|ivory|grey/.test(q)){
    return "We stock MCC Standard Emulsion (GHS 300/20L), Acrylic Premium Emulsion (GHS 650/20L), and Oil Paint (GHS 200/4L) in multiple colours. Select your colour on the product card, add to cart, then order via WhatsApp +233 303 978 485.";
  }
  if(/board|plaster|drywall|ceiling|panel|pvc/.test(q)){
    return "We carry Plasterboard 9mm (GHS 150/sheet) and 12mm (GHS 200/sheet), plus PVC Ceiling Panels from GHS 60/piece. Bulk discounts available. WhatsApp +233 303 978 485 for site delivery quotes.";
  }
  if(/deliver|shipping|accra|location|area/.test(q)){
    return "We deliver to all areas in Accra — home, office, and construction sites. Small items by bike, medium by van, bulk/heavy by pickup truck. Delivery fee is discussed on WhatsApp. Contact us: +233 303 978 485.";
  }
  if(/bulk|discount|wholesale|many/.test(q)){
    return "Yes, we offer bulk discounts! Each product shows the minimum quantity for a bulk price. Add your quantity in the cart and WhatsApp us on +233 303 978 485 — we'll confirm the bulk rate and delivery cost.";
  }
  if(/order|buy|purchase|how to/.test(q)){
    return "Easy! Browse the catalogue, pick your products, choose quantity and colour, then click the WhatsApp button. Your cart will be sent directly to our team at +233 303 978 485 and they'll confirm the order and delivery.";
  }
  if(/payment|pay|mobile money|momo|cash/.test(q)){
    return "We accept Mobile Money and cash on delivery. Payment details are confirmed with our team on WhatsApp +233 303 978 485 when you place your order.";
  }
  if(/hello|hi|hey|good|morning|afternoon|evening/.test(q)){
    return "Hello! Welcome to The MCC Shop — Ghana's trusted construction and home delivery service in Accra. Browse our catalogue above or ask me about any product. For orders, reach us on WhatsApp: +233 303 978 485.";
  }
  // Default
  return "Thanks for your message! For the fastest help, WhatsApp our team directly on +233 303 978 485. We're available Monday–Saturday and can answer any question about products, delivery, or pricing.";
}"""

if OLD_CLAUDE in content:
    content = content.replace(OLD_CLAUDE, NEW_CLAUDE)
    print("[3] callClaude replaced with static keyword responder")
else:
    print("[3] WARNING: callClaude not found exactly — check manually")

# ── Write out ─────────────────────────────────────────────────────────────────
with open(HTML, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nDone. File length: {len(content)} chars")
