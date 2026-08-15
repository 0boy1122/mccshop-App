import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HTML = r"c:\Users\dell\OneDrive\Desktop\mcc shop\backend\mcc-shop-backend\public\index.html"

with open(HTML, encoding='utf-8') as f:
    content = f.read()

# ── 1. Update CI object ──────────────────────────────────────────
OLD_CI = "const CI={All:'\U0001f3ea',Paints:'\U0001f3a8',Boards:'\U0001fab5',Panels:'\U0001f3d7️',Furniture:'\U0001f6cb️',Imported:'\U0001f6a2',Adhesives:'\U0001f527',Safety:'⛑️',Tools:'\U0001f528',Electrical:'\U0001f4a1',Plumbing:'\U0001f6bf',Hardware:'\U0001f529',Office:'\U0001fa91'};"
NEW_CI = "const CI={All:'\U0001f3ea',Paints:'\U0001f3a8',Boards:'\U0001fab5',Panels:'\U0001f3d7️',Furniture:'\U0001f6cb️',Imported:'\U0001f6a2',Office:'\U0001f5a5️',Kitchens:'\U0001f373',Wardrobes:'\U0001f5c4️',Doors:'\U0001f6aa',Windows:'\U0001fa9f',Flooring:'\U0001f3e1',Adhesives:'\U0001f527',Safety:'⛑️',Tools:'\U0001f528',Electrical:'\U0001f4a1',Plumbing:'\U0001f6bf',Hardware:'\U0001f529'};"

if OLD_CI in content:
    content = content.replace(OLD_CI, NEW_CI)
    print("[1] CI updated")
else:
    # Try to find it dynamically
    import re
    m = re.search(r"const CI=\{[^}]+\};", content)
    if m:
        content = content[:m.start()] + NEW_CI + content[m.end():]
        print("[1] CI updated (regex)")
    else:
        print("[1] ERROR: CI not found")

# ── 2. Append new products ───────────────────────────────────────
MARKER = '{ skuCode:"GCH-CHR-PRE"'
idx = content.find(MARKER)
if idx == -1:
    print("[2] ERROR: marker not found")
else:
    end = content.find('];', idx)
    NEW_PRODUCTS = """,
      // -- Office Furniture (GECHi Italian Design) --
      { skuCode:"OFF-DSK-SM",  name:"Executive Desk Small (1.8m)",           category:"Office",    unitSize:"Unit",      sellingPrice:3100,   bulkThreshold:2,  bulkPrice:2900,  dispatchMode:"VAN",  images:"/office_exec_desk.jpg",   mvpPriority:true  },
      { skuCode:"OFF-DSK-MD",  name:"Executive Desk Medium (2.4m)",          category:"Office",    unitSize:"Unit",      sellingPrice:6100,   bulkThreshold:2,  bulkPrice:5800,  dispatchMode:"VAN",  images:"/office_exec_desk.jpg",   mvpPriority:true  },
      { skuCode:"OFF-DSK-LG",  name:"Executive Desk Large (3.2m + Cabinet)", category:"Office",    unitSize:"Unit",      sellingPrice:7900,   bulkThreshold:2,  bulkPrice:7500,  dispatchMode:"VAN",  images:"/office_exec_desk.jpg",   mvpPriority:true  },
      { skuCode:"OFF-CHR-VIS", name:"Visitor Chair",                         category:"Office",    unitSize:"Unit",      sellingPrice:700,    bulkThreshold:4,  bulkPrice:650,   dispatchMode:"VAN",  images:"/office_chair.jpg",       mvpPriority:true  },
      { skuCode:"OFF-CHR-MID", name:"Mid-level Swivel Chair",                category:"Office",    unitSize:"Unit",      sellingPrice:1200,   bulkThreshold:4,  bulkPrice:1100,  dispatchMode:"VAN",  images:"/office_chair.jpg",       mvpPriority:true  },
      { skuCode:"OFF-CHR-EXC", name:"Executive Leather Chair",               category:"Office",    unitSize:"Unit",      sellingPrice:2500,   bulkThreshold:2,  bulkPrice:2300,  dispatchMode:"VAN",  images:"/office_chair.jpg",       mvpPriority:true  },
      { skuCode:"OFF-WRK-2P",  name:"2-Person Workstation",                  category:"Office",    unitSize:"Set",       sellingPrice:2500,   bulkThreshold:2,  bulkPrice:2300,  dispatchMode:"VAN",  images:"/office_workstation.jpg", mvpPriority:true  },
      { skuCode:"OFF-WRK-4P",  name:"4-Person Workstation",                  category:"Office",    unitSize:"Set",       sellingPrice:4500,   bulkThreshold:2,  bulkPrice:4300,  dispatchMode:"VAN",  images:"/office_workstation.jpg", mvpPriority:true  },
      { skuCode:"OFF-WRK-6P",  name:"6-8 Person Workstation",                category:"Office",    unitSize:"Set",       sellingPrice:7000,   bulkThreshold:2,  bulkPrice:6700,  dispatchMode:"VAN",  images:"/office_workstation.jpg", mvpPriority:true  },
      // -- Kitchens (Custom Built) --
      { skuCode:"KIT-BUD-001", name:"Budget Kitchen (Custom Built)",         category:"Kitchens",  unitSize:"Full Set",  sellingPrice:45000,  bulkThreshold:1,  bulkPrice:43000, dispatchMode:"VAN",  images:"/kitchen_budget.jpg",     notes:"custom:true", mvpPriority:true  },
      { skuCode:"KIT-STD-001", name:"Standard Kitchen (Custom Built)",       category:"Kitchens",  unitSize:"Full Set",  sellingPrice:75000,  bulkThreshold:1,  bulkPrice:72000, dispatchMode:"VAN",  images:"/kitchen_standard.jpg",   notes:"custom:true", mvpPriority:true  },
      { skuCode:"KIT-PRE-001", name:"Premium Kitchen (Custom Built)",        category:"Kitchens",  unitSize:"Full Set",  sellingPrice:150000, bulkThreshold:1,  bulkPrice:145000,dispatchMode:"VAN",  images:"/kitchen_premium.jpg",    notes:"custom:true", mvpPriority:true  },
      // -- Wardrobes & Storage --
      { skuCode:"WRD-SLD-001", name:"Sliding Wardrobe",                      category:"Wardrobes", unitSize:"Per m2",    sellingPrice:900,    bulkThreshold:5,  bulkPrice:850,   dispatchMode:"VAN",  images:"/wardrobe_sliding.jpg",   mvpPriority:true  },
      { skuCode:"WRD-HNG-001", name:"Hinged Wardrobe",                       category:"Wardrobes", unitSize:"Per m2",    sellingPrice:800,    bulkThreshold:5,  bulkPrice:750,   dispatchMode:"VAN",  images:"/wardrobe_hinged.jpg",    mvpPriority:true  },
      { skuCode:"WRD-WLK-001", name:"Walk-in Closet (Custom)",               category:"Wardrobes", unitSize:"Custom",    sellingPrice:5000,   bulkThreshold:1,  bulkPrice:4800,  dispatchMode:"VAN",  images:"/wardrobe_walkin.jpg",    notes:"custom:true", mvpPriority:true  },
      { skuCode:"WRD-TVU-001", name:"TV Wall Unit",                          category:"Wardrobes", unitSize:"Unit",      sellingPrice:2500,   bulkThreshold:2,  bulkPrice:2300,  dispatchMode:"VAN",  images:"/tv_wall_unit.jpg",       mvpPriority:true  },
      // -- Doors --
      { skuCode:"DOR-WOD-001", name:"Wooden Door",                           category:"Doors",     unitSize:"Per Door",  sellingPrice:850,    bulkThreshold:5,  bulkPrice:800,   dispatchMode:"VAN",  images:"/door_wooden.jpg",        mvpPriority:true  },
      { skuCode:"DOR-SEC-001", name:"Security Door",                         category:"Doors",     unitSize:"Per Door",  sellingPrice:1200,   bulkThreshold:3,  bulkPrice:1100,  dispatchMode:"VAN",  images:"/door_security.jpg",      mvpPriority:true  },
      { skuCode:"DOR-WPC-001", name:"WPC Door",                              category:"Doors",     unitSize:"Per Door",  sellingPrice:900,    bulkThreshold:5,  bulkPrice:850,   dispatchMode:"VAN",  images:"/door_wpc.jpg",           mvpPriority:true  },
      { skuCode:"DOR-MDF-001", name:"MDF Door",                              category:"Doors",     unitSize:"Per Door",  sellingPrice:700,    bulkThreshold:5,  bulkPrice:650,   dispatchMode:"VAN",  images:"/door_mdf.jpg",           mvpPriority:false },
      { skuCode:"DOR-LAM-001", name:"Laminate Door",                         category:"Doors",     unitSize:"Per Door",  sellingPrice:750,    bulkThreshold:5,  bulkPrice:700,   dispatchMode:"VAN",  images:"/door_laminate.jpg",      mvpPriority:false },
      { skuCode:"DOR-GLS-001", name:"Glass Door",                            category:"Doors",     unitSize:"Per Door",  sellingPrice:950,    bulkThreshold:3,  bulkPrice:900,   dispatchMode:"VAN",  images:"/door_glass.jpg",         mvpPriority:true  },
      // -- Glazing Windows --
      { skuCode:"WIN-ALU-001", name:"Aluminium Sliding Window",              category:"Windows",   unitSize:"Per m2",    sellingPrice:650,    bulkThreshold:10, bulkPrice:600,   dispatchMode:"VAN",  images:"/window_sliding.jpg",     mvpPriority:true  },
      { skuCode:"WIN-CAS-001", name:"Casement Window",                       category:"Windows",   unitSize:"Per m2",    sellingPrice:700,    bulkThreshold:10, bulkPrice:650,   dispatchMode:"VAN",  images:"/window_casement.jpg",    mvpPriority:true  },
      { skuCode:"WIN-FIX-001", name:"Fixed Window",                          category:"Windows",   unitSize:"Per m2",    sellingPrice:600,    bulkThreshold:10, bulkPrice:550,   dispatchMode:"VAN",  images:"/window_fixed.jpg",       mvpPriority:false },
      { skuCode:"WIN-TMP-001", name:"Tempered Glass Window",                 category:"Windows",   unitSize:"Per m2",    sellingPrice:800,    bulkThreshold:5,  bulkPrice:750,   dispatchMode:"VAN",  images:"/window_tempered.jpg",    mvpPriority:true  },
      { skuCode:"WIN-TNT-001", name:"Tinted Glass Window",                   category:"Windows",   unitSize:"Per m2",    sellingPrice:750,    bulkThreshold:5,  bulkPrice:700,   dispatchMode:"VAN",  images:"/window_tinted.jpg",      mvpPriority:false },
      // -- Flooring --
      { skuCode:"FLR-POR-001", name:"Porcelain Tiles",                       category:"Flooring",  unitSize:"Per m2",    sellingPrice:50,     bulkThreshold:50, bulkPrice:45,    dispatchMode:"VAN",  images:"/flooring_porcelain.jpg", mvpPriority:true  },
      { skuCode:"FLR-GRN-001", name:"Granite Tiles",                         category:"Flooring",  unitSize:"Per m2",    sellingPrice:60,     bulkThreshold:50, bulkPrice:55,    dispatchMode:"VAN",  images:"/flooring_granite.jpg",   mvpPriority:true  },
      { skuCode:"FLR-SPC-001", name:"SPC / Vinyl Flooring",                  category:"Flooring",  unitSize:"Per m2",    sellingPrice:120,    bulkThreshold:30, bulkPrice:110,   dispatchMode:"VAN",  images:"/flooring_spc.jpg",       mvpPriority:true  },
      { skuCode:"FLR-LAM-001", name:"Laminate Flooring",                     category:"Flooring",  unitSize:"Per m2",    sellingPrice:100,    bulkThreshold:30, bulkPrice:90,    dispatchMode:"VAN",  images:"/flooring_laminate.jpg",  mvpPriority:true  }"""
    # Find the end of the GCH-CHR-PRE line
    eol = content.find('\n', idx)
    content = content[:eol] + NEW_PRODUCTS + content[eol:]
    print("[2] 34 new products inserted")

# ── 3. Update announcement ticker ───────────────────────────────
ANN_MARKER = 'Home &amp; office delivery</span><span class="ann-sep">❖</span>\n  </div>\n</div>'
ANN_NEW = '''Home &amp; office delivery</span><span class="ann-sep">❖</span>
    <span class="ann-item">Kitchen cabinets &amp; installation</span><span class="ann-sep">❖</span>
    <span class="ann-item">Office furniture by GECHi</span><span class="ann-sep">❖</span>
    <span class="ann-item">Doors &amp; glazing windows</span><span class="ann-sep">❖</span>
    <span class="ann-item">Flooring &amp; wall cladding</span><span class="ann-sep">❖</span>
    <span class="ann-item">Wardrobes &amp; storage solutions</span><span class="ann-sep">❖</span>
    <span class="ann-item">Home &amp; office delivery</span><span class="ann-sep">❖</span>
    <span class="ann-item">Kitchen cabinets &amp; installation</span><span class="ann-sep">❖</span>
    <span class="ann-item">Office furniture by GECHi</span><span class="ann-sep">❖</span>
    <span class="ann-item">Doors &amp; glazing windows</span><span class="ann-sep">❖</span>
    <span class="ann-item">Flooring &amp; wall cladding</span><span class="ann-sep">❖</span>
    <span class="ann-item">Wardrobes &amp; storage solutions</span><span class="ann-sep">❖</span>
  </div>
</div>'''
if ANN_MARKER in content:
    content = content.replace(ANN_MARKER, ANN_NEW)
    print("[3] Ticker updated")
else:
    print("[3] WARNING: ticker marker not found — skipping")

# ── 4. Add chatbot responses ─────────────────────────────────────
OLD_DEFAULT = "  return 'For the fastest help, WhatsApp our team on +233 50 991 9161 — available Monday to Saturday for products, delivery, and pricing.';"
NEW_DEFAULT = """  if(/office|desk|executive|workstation|swivel/.test(q))
    return 'GECHi Italian Design office furniture: Executive Desks from GHS 3,100, Office Chairs from GHS 700, Workstations (2-8 people) from GHS 2,500. Browse the Office tab or WhatsApp +233 50 991 9161.';
  if(/kitchen|cabinet/.test(q))
    return 'We build custom kitchens with imported materials: Budget from GHS 45,000, Standard from GHS 75,000, Premium from GHS 150,000. Price depends on size. WhatsApp +233 50 991 9161 for a quote.';
  if(/wardrobe|closet|tv unit|wall unit/.test(q))
    return 'Sliding wardrobes from GHS 800/m2, walk-in closets (custom quote), TV wall units from GHS 2,500. WhatsApp +233 50 991 9161.';
  if(/door|wooden door|security door|glass door/.test(q))
    return 'We stock Wooden, Security, WPC, MDF, Laminate and Glass doors from GHS 700 per door. WhatsApp +233 50 991 9161.';
  if(/window|glazing|aluminium|casement|tempered/.test(q))
    return 'We supply Aluminium Sliding, Casement, Fixed, Tempered and Tinted Glass windows from GHS 600/m2. WhatsApp +233 50 991 9161.';
  if(/floor|tile|porcelain|granite|vinyl|laminate floor/.test(q))
    return 'Flooring: Porcelain GHS 50/m2, Granite GHS 60/m2, SPC Vinyl GHS 120/m2, Laminate GHS 100/m2. Bulk from 30m2+. WhatsApp +233 50 991 9161.';
  return 'For the fastest help, WhatsApp our team on +233 50 991 9161 — available Monday to Saturday for products, delivery, and pricing.';"""

if OLD_DEFAULT in content:
    content = content.replace(OLD_DEFAULT, NEW_DEFAULT)
    print("[4] Chatbot updated")
else:
    print("[4] WARNING: chatbot default not found")

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone. File: {len(content):,} chars")
