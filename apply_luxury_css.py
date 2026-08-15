#!/usr/bin/env python3
"""Replace index.html style block with dark luxury CSS."""

with open(
    r"c:\Users\dell\OneDrive\Desktop\mcc shop\backend\mcc-shop-backend\public\index.html",
    encoding="utf-8",
) as f:
    content = f.read()

# ── Locate landmarks ──────────────────────────────────────────────────────────
old_font_link = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,700;0,9..144,900;1,9..144,300;1,9..144,700&family=DM+Sans:wght@300;400;500;600&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">'
new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600;1,700&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">'

style_open = "<style>"
style_close = "</style>"
style_start = content.find(style_open) + len(style_open)
style_end = content.find(style_close)

NEW_CSS = r"""
html{scroll-behavior:smooth;font-size:16px;overflow-x:hidden;width:100%;}
body{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--t1);overflow-x:hidden;width:100%;-webkit-text-size-adjust:100%;}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;max-width:100%;word-wrap:break-word;}

:root{
  --ink:#090909;
  --ink2:#0f0f0f;
  --ink3:#141414;
  --sage:#c9963f;
  --sage2:#b8832e;
  --sage3:#9d6f25;
  --sage4:#060606;
  --mist:#1c1812;
  --mist2:#2a2318;
  --amber:#c9963f;
  --amber2:#b8832e;
  --amberl:#1a1610;
  --cream:#090909;
  --cream2:#121212;
  --cream3:#1c1c1c;
  --wa:#25D366;
  --wa2:#1aa34a;
  --white:#111111;
  --t1:#f2ede6;
  --t2:#cec8c0;
  --t3:#7a7470;
  --t4:#4a4642;
  --border:rgba(201,150,63,.12);
  --border2:rgba(201,150,63,.22);
  --r:16px;
  --r2:24px;
  --r3:32px;
  --shadow-sm:0 2px 8px rgba(0,0,0,.5);
  --shadow-md:0 8px 32px rgba(0,0,0,.55);
  --shadow-lg:0 24px 64px rgba(0,0,0,.65);
  --shadow-xl:0 40px 100px rgba(0,0,0,.75);
  --transition:all .4s cubic-bezier(.16,1,.3,1);
  --gold:#c9963f;
  --gold-glow:rgba(201,150,63,.15);
}

body{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--t1);overflow-x:hidden;}
a{text-decoration:none;color:inherit;}
button{font-family:'DM Sans',sans-serif;}
*,a,button{cursor:none!important;}

/* ══ CURSOR ══ */
#dot{position:fixed;z-index:9999;pointer-events:none;width:6px;height:6px;border-radius:50%;background:var(--gold);transform:translate(-50%,-50%);transition:width .2s,height .2s,background .2s,opacity .2s;opacity:0;}
#ring{position:fixed;z-index:9998;pointer-events:none;width:32px;height:32px;border-radius:50%;border:1px solid rgba(201,150,63,.4);transform:translate(-50%,-50%);transition:width .45s cubic-bezier(.16,1,.3,1),height .45s cubic-bezier(.16,1,.3,1),opacity .3s,border-color .3s;opacity:0;}
body.cur #dot{opacity:1;}
body.cur #ring{opacity:1;}
body.hov #dot{width:10px;height:10px;background:var(--gold);}
body.hov #ring{width:48px;height:48px;border-color:rgba(201,150,63,.3);}
body.clicking #dot{width:5px;height:5px;}
body.clicking #ring{width:26px;height:26px;}
@media(hover:none){#dot,#ring{display:none;}*,a,button{cursor:auto!important;}}

/* ══ LOADER ══ */
#ldr{position:fixed;inset:0;z-index:9000;background:#040404;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0;transition:opacity .8s ease,visibility .8s ease;}
#ldr.out{opacity:0;visibility:hidden;}
.ldr-words{overflow:hidden;margin-bottom:2px;}
.ldr-word{font-family:'Cormorant Garamond',serif;font-size:clamp(48px,8vw,100px);font-weight:700;color:var(--t1);letter-spacing:-.03em;line-height:1;display:block;transform:translateY(110%);animation:wordIn .7s cubic-bezier(.16,1,.3,1) forwards;}
.ldr-word:nth-child(1){animation-delay:.1s;}
.ldr-word:nth-child(2){animation-delay:.25s;color:var(--gold);font-style:italic;}
.ldr-word:nth-child(3){animation-delay:.4s;font-size:clamp(12px,1.5vw,16px);font-weight:400;color:rgba(242,237,230,.3);letter-spacing:.3em;text-transform:uppercase;font-family:'DM Sans',sans-serif;}
@keyframes wordIn{to{transform:translateY(0);}}
.ldr-line{width:0;height:1px;background:linear-gradient(to right,transparent,var(--gold),transparent);margin-top:40px;animation:lw 1.2s .6s cubic-bezier(.4,0,.2,1) forwards;}
@keyframes lw{to{width:200px;}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}

/* ══ ANNOUNCE ══ */
.ann{background:#050505;padding:11px 0;overflow:hidden;position:relative;border-bottom:1px solid rgba(201,150,63,.06);}
.ann::before,.ann::after{content:'';position:absolute;top:0;bottom:0;width:80px;z-index:2;}
.ann::before{left:0;background:linear-gradient(to right,#050505,transparent);}
.ann::after{right:0;background:linear-gradient(to left,#050505,transparent);}
.ann-inner{display:flex;gap:56px;animation:scroll 35s linear infinite;width:max-content;}
.ann-item{display:flex;align-items:center;gap:10px;font-size:11px;color:rgba(242,237,230,.35);letter-spacing:.1em;white-space:nowrap;flex-shrink:0;text-transform:uppercase;}
.ann-sep{font-size:8px;color:var(--gold);opacity:.6;}
@keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ══ NAV ══ */
nav{position:sticky;top:0;z-index:500;height:72px;display:flex;align-items:center;padding:0 56px;gap:32px;transition:background .5s,border-color .5s,backdrop-filter .5s;}
nav.scrolled{background:rgba(9,9,9,.88);backdrop-filter:blur(40px) saturate(1.4);border-bottom:1px solid rgba(201,150,63,.08);}
.nl{display:flex;align-items:center;gap:12px;flex-shrink:0;}
.nl-icon{width:44px;height:44px;background:#111;border-radius:12px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;flex-shrink:0;border:1px solid rgba(201,150,63,.15);}
.nl-icon::after{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(201,150,63,.15) 0%,transparent 55%);}
.nl-icon svg{width:22px;height:22px;fill:var(--gold);position:relative;z-index:1;}
.nl-text{line-height:1.15;}
.nl-logo-img{height:46px;width:auto;display:block;object-fit:contain;}
.nl-pre{font-size:9px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:var(--t4);}
.nl-main{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600;color:var(--t1);letter-spacing:.02em;}
.nav-mid{flex:1;display:flex;justify-content:center;}
.nav-links{display:flex;align-items:center;gap:0;background:transparent;border:none;border-radius:0;padding:0;}
.nav-link{padding:8px 22px;border-radius:0;font-size:12px;font-weight:400;color:var(--t3);border:none;background:none;transition:color .25s;letter-spacing:.08em;text-transform:uppercase;position:relative;}
.nav-link::after{content:'';position:absolute;bottom:0;left:50%;right:50%;height:1px;background:var(--gold);transition:left .3s,right .3s;}
.nav-link:hover{color:var(--t1);}
.nav-link:hover::after{left:22px;right:22px;}
.nav-link.on{color:var(--t1);}
.nav-link.on::after{left:22px;right:22px;}
.nav-r{display:flex;align-items:center;gap:8px;flex-shrink:0;}
.srch{display:flex;align-items:center;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:10px;overflow:hidden;width:220px;transition:width .3s,box-shadow .25s,border-color .25s,background .25s;}
.srch:focus-within{width:260px;border-color:rgba(201,150,63,.35);box-shadow:0 0 0 3px rgba(201,150,63,.07);background:rgba(255,255,255,.06);}
.srch-ic{padding:0 12px;display:flex;align-items:center;flex-shrink:0;}
.srch-ic svg{width:13px;height:13px;stroke:var(--t4);fill:none;stroke-width:2;}
.srch input{flex:1;border:none;outline:none;background:transparent;font-family:'DM Sans',sans-serif;font-size:16px;color:var(--t1);padding:10px 0;min-width:0;}
.srch input::placeholder{color:var(--t4);}
.nwa{display:flex;align-items:center;gap:8px;background:var(--wa);color:white;border:none;border-radius:10px;padding:10px 18px;font-size:12px;font-weight:600;text-decoration:none;transition:all .25s;white-space:nowrap;letter-spacing:.04em;}
.nwa:hover{background:var(--wa2);transform:translateY(-1px);box-shadow:0 6px 20px rgba(37,211,102,.25);}
.nwa svg{width:14px;height:14px;fill:white;}
.ncrt{position:relative;background:transparent;border:1px solid rgba(255,255,255,.08);border-radius:10px;width:42px;height:42px;display:flex;align-items:center;justify-content:center;transition:all .25s;}
.ncrt:hover{background:rgba(255,255,255,.06);border-color:rgba(201,150,63,.3);}
.ncrt svg{width:17px;height:17px;stroke:var(--t2);fill:none;stroke-width:1.6;}
.cbdg{position:absolute;top:-6px;right:-6px;background:var(--gold);color:#090909;font-size:9px;font-weight:700;min-width:18px;height:18px;border-radius:100px;display:none;align-items:center;justify-content:center;padding:0 4px;border:2px solid var(--cream);z-index:10;}

/* ══ HERO BADGE ══ */
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(201,150,63,.08);border:1px solid rgba(201,150,63,.2);border-radius:100px;padding:7px 16px;margin-bottom:20px;font-size:10px;font-weight:500;color:rgba(201,150,63,.85);letter-spacing:.14em;text-transform:uppercase;}
.hero-badge-dot{width:5px;height:5px;border-radius:50%;background:var(--gold);display:inline-block;box-shadow:0 0 0 3px rgba(201,150,63,.2);animation:pulse 2.5s infinite;}

/* ══ HERO ══ */
.hero{min-height:100vh;background:#050505;position:relative;display:flex;flex-direction:column;overflow:hidden;}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% -10%,rgba(201,150,63,.04) 0%,transparent 70%);pointer-events:none;z-index:1;}
#heroCanvas{position:absolute;inset:0;z-index:0;opacity:.4;}
.hero-content{flex:1;display:grid;grid-template-columns:1fr 1fr;position:relative;z-index:2;}
.hero-l{padding:140px 72px 100px;display:flex;flex-direction:column;justify-content:center;}
.hero-tag{display:inline-flex;align-items:center;gap:10px;margin-bottom:40px;}
.hero-tag-dot{width:7px;height:7px;border-radius:50%;background:var(--wa);animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(201,150,63,.35);}50%{box-shadow:0 0 0 7px rgba(201,150,63,0);}}
.hero-tag-text{font-size:10px;font-weight:400;letter-spacing:.22em;text-transform:uppercase;color:rgba(242,237,230,.32);}
.hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(52px,7vw,96px);font-weight:600;color:var(--t1);line-height:.93;letter-spacing:-.02em;margin-bottom:36px;}
.hero h1 .line{display:block;overflow:hidden;}
.hero h1 .line span{display:block;transform:translateY(110%);animation:lineUp .9s cubic-bezier(.16,1,.3,1) both;}
.hero h1 .line:nth-child(1) span{animation-delay:.3s;}
.hero h1 .line:nth-child(2) span{animation-delay:.45s;}
.hero h1 .line:nth-child(3) span{animation-delay:.6s;}
.hero h1 .green{color:rgba(242,237,230,.55);font-style:italic;font-weight:300;}
.hero h1 .amber{color:var(--gold);font-style:italic;}
@keyframes lineUp{to{transform:translateY(0);}}
.hero-sub{font-size:17px;font-weight:300;color:rgba(242,237,230,.38);line-height:1.85;max-width:420px;margin-bottom:52px;opacity:0;animation:fadeIn .8s .9s ease both;letter-spacing:.01em;}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;opacity:0;animation:fadeIn .8s 1.1s ease both;}
.btn-solid{display:inline-flex;align-items:center;gap:10px;background:var(--gold);color:#090909;border:none;border-radius:3px;padding:16px 36px;font-size:13px;font-weight:600;text-decoration:none;transition:var(--transition);letter-spacing:.08em;text-transform:uppercase;}
.btn-solid:hover{background:#d4a34a;transform:translateY(-2px);box-shadow:0 12px 40px rgba(201,150,63,.3);}
.btn-solid svg{width:16px;height:16px;fill:#090909;transition:transform .25s;}
.btn-solid:hover svg{transform:translateX(3px);}
.btn-ghost{display:inline-flex;align-items:center;gap:10px;background:transparent;color:rgba(242,237,230,.6);border:1px solid rgba(242,237,230,.15);border-radius:3px;padding:16px 36px;font-size:13px;font-weight:400;text-decoration:none;transition:var(--transition);letter-spacing:.08em;text-transform:uppercase;}
.btn-ghost:hover{color:var(--t1);border-color:rgba(242,237,230,.35);}
.btn-ghost svg{width:16px;height:16px;fill:rgba(242,237,230,.5);}
.hero-scroll{position:absolute;bottom:40px;left:64px;display:flex;align-items:center;gap:14px;opacity:0;animation:fadeIn .8s 1.4s ease both;}
.hero-scroll-line{width:36px;height:1px;background:rgba(255,255,255,.12);position:relative;overflow:hidden;}
.hero-scroll-line::after{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:var(--gold);animation:scanLine 2.5s 2s ease-in-out infinite;}
@keyframes scanLine{0%{left:-100%;}100%{left:100%;}}
.hero-scroll-text{font-size:9px;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.22);}
.hero-r{display:flex;align-items:center;justify-content:center;padding:80px 48px;border-left:1px solid rgba(255,255,255,.04);opacity:0;animation:fadeIn .8s 1s ease both;}
.feat-stack{width:100%;max-width:360px;display:flex;flex-direction:column;gap:10px;}
.feat-hdr{font-size:9px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;color:rgba(255,255,255,.2);margin-bottom:6px;}
.fcard{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:20px;transition:all .35s cubic-bezier(.16,1,.3,1);display:flex;align-items:center;gap:16px;}
.fcard:hover{background:rgba(201,150,63,.05);border-color:rgba(201,150,63,.2);transform:translateX(4px);}
.fcard.top{background:linear-gradient(135deg,rgba(201,150,63,.08),rgba(201,150,63,.02));border-color:rgba(201,150,63,.18);flex-direction:column;align-items:flex-start;gap:10px;}
.fcard-em{font-size:38px;line-height:1;}
.fcard.top .fcard-em{font-size:48px;}
.fcard-cat{font-size:9px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);opacity:.7;margin-bottom:3px;}
.fcard-name{font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:600;color:var(--t1);letter-spacing:-.01em;}
.fcard.top .fcard-name{font-size:22px;}
.fcard-price{font-family:'Cormorant Garamond',serif;font-size:22px;font-weight:700;color:var(--t1);margin-top:8px;}
.fcard-price sup{font-size:12px;font-weight:400;font-family:'DM Sans',sans-serif;color:rgba(242,237,230,.35);}
.fcard-smalls{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.fcard-sm{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.05);border-radius:10px;padding:14px;}

/* ══ STATS BAR ══ */
.statsbar{background:#050505;border-top:1px solid rgba(255,255,255,.03);border-bottom:1px solid rgba(255,255,255,.03);}
.stats-inner{max-width:1280px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);}
.stat-item{padding:32px 40px;border-right:1px solid rgba(255,255,255,.04);display:flex;align-items:center;gap:18px;transition:background .25s;}
.stat-item:hover{background:rgba(201,150,63,.03);}
.stat-item:last-child{border-right:none;}
.stat-ic{width:44px;height:44px;border-radius:12px;background:rgba(201,150,63,.08);border:1px solid rgba(201,150,63,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.stat-ic svg{width:18px;height:18px;stroke:var(--gold);fill:none;stroke-width:1.6;}
.stat-num{font-family:'Cormorant Garamond',serif;font-size:36px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.04em;}
.stat-lbl{font-size:9px;color:rgba(242,237,230,.28);margin-top:5px;letter-spacing:.12em;text-transform:uppercase;}

/* ══ PRODUCTS SECTION ══ */
.products-section{padding:96px 0;max-width:1440px;margin:0 auto;padding-left:56px;padding-right:56px;}
.sec-lead{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:40px;gap:24px;padding-bottom:28px;border-bottom:1px solid rgba(255,255,255,.05);}
.sec-kicker{font-size:9px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:12px;display:block;opacity:.8;}
.sec-h{font-family:'Cormorant Garamond',serif;font-size:clamp(28px,3vw,48px);font-weight:600;color:var(--t1);letter-spacing:-.03em;line-height:.95;}
.sec-h em{font-style:italic;color:rgba(242,237,230,.45);}
.sec-desc{font-size:13px;color:var(--t3);margin-top:0;max-width:300px;line-height:1.7;text-align:right;letter-spacing:.02em;}

/* ══ FILTER BAR ══ */
.filter-bar{display:flex;align-items:center;gap:6px;margin-bottom:44px;overflow-x:auto;scrollbar-width:none;padding-bottom:0;}
.filter-bar::-webkit-scrollbar{display:none;}
.ftab{display:flex;align-items:center;gap:6px;padding:7px 18px;border-radius:2px;flex-shrink:0;font-size:11px;font-weight:500;color:var(--t3);background:transparent;border:1px solid rgba(255,255,255,.07);transition:all .25s;letter-spacing:.09em;text-transform:uppercase;}
.ftab:hover{background:rgba(255,255,255,.04);color:var(--t1);border-color:rgba(255,255,255,.14);}
.ftab.on{background:transparent;color:var(--gold);font-weight:600;border-color:var(--gold);}
.ftab-ic{display:none;}
.ftab-n{font-size:8px;font-weight:700;padding:2px 6px;border-radius:3px;margin-left:2px;letter-spacing:.05em;}
.ftab.on .ftab-n{background:rgba(201,150,63,.15);color:var(--gold);}
.ftab:not(.on) .ftab-n{background:rgba(255,255,255,.05);color:var(--t4);}

/* ══ PRODUCT GRID ══ */
.pgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(255,255,255,.05);}
@keyframes cardIn{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:none;}}

/* Card base */
.pcard{background:#101010;display:flex;flex-direction:column;transition:background .35s cubic-bezier(.16,1,.3,1),transform .35s cubic-bezier(.16,1,.3,1);animation:cardIn .6s ease both;position:relative;overflow:hidden;border-radius:0;}
.pcard:nth-child(1){animation-delay:.05s}.pcard:nth-child(2){animation-delay:.1s}.pcard:nth-child(3){animation-delay:.15s}.pcard:nth-child(4){animation-delay:.2s}.pcard:nth-child(5){animation-delay:.25s}.pcard:nth-child(6){animation-delay:.3s}.pcard:nth-child(7){animation-delay:.35s}.pcard:nth-child(8){animation-delay:.4s}
.pcard:hover{background:#151510;transform:none;box-shadow:inset 0 0 0 1px rgba(201,150,63,.3);}

/* Image */
.pcard-img{aspect-ratio:4/3;background:#0d0d0d;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;}
.pcard-img img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .7s cubic-bezier(.16,1,.3,1);}
.pcard:hover .pcard-img img{transform:scale(1.04);}
.pcard-img::after{content:'View';position:absolute;inset:0;background:rgba(5,5,5,.45);display:flex;align-items:center;justify-content:center;color:rgba(242,237,230,.85);font-size:11px;font-weight:500;letter-spacing:.2em;text-transform:uppercase;opacity:0;transition:opacity .35s;backdrop-filter:blur(4px);}
.pcard:hover .pcard-img::after{opacity:1;}

/* Placeholder */
.pcard-placeholder{width:100%;height:100%;background:linear-gradient(145deg,#111 0%,#0a0a0a 100%);display:flex;align-items:center;justify-content:center;position:relative;}
.pcard-placeholder::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 30%,rgba(201,150,63,.04) 0%,transparent 60%);}
.pcard-placeholder span{font-family:'Cormorant Garamond',serif;font-size:72px;font-weight:300;color:rgba(201,150,63,.15);line-height:1;text-transform:uppercase;position:relative;z-index:1;font-style:italic;}
.pcard-em{display:none;}

/* Badges */
.pcard-badges{position:absolute;top:12px;left:12px;right:12px;display:flex;justify-content:space-between;align-items:flex-start;pointer-events:none;z-index:2;}
.badge-vat{background:rgba(201,150,63,.12);color:var(--gold);font-size:8px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:3px 8px;border-radius:2px;border:1px solid rgba(201,150,63,.2);}
.badge-del{background:rgba(0,0,0,.7);color:rgba(242,237,230,.6);font-size:8px;padding:3px 8px;border-radius:2px;font-weight:400;letter-spacing:.06em;}

/* Card body */
.pcard-body{padding:20px 20px 12px;flex:1;display:flex;flex-direction:column;}
.pcard-top{margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;}
.pcard-cat{font-size:8px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);opacity:.7;}
.pcard-sku{display:none;}
.pcard-name{font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--t1);line-height:1.25;letter-spacing:-.01em;margin-bottom:10px;}
.pcard-unit{font-size:11px;color:var(--t4);margin-bottom:10px;display:flex;align-items:center;gap:4px;}
.pcard-price-area{margin-top:auto;padding-top:4px;}
.pcard-price{font-family:'Cormorant Garamond',serif;font-size:26px;font-weight:600;color:var(--t1);line-height:1;letter-spacing:-.03em;}
.pcard-price-unit{font-size:9px;color:var(--t4);margin-top:4px;letter-spacing:.06em;text-transform:uppercase;}
.pcard-bulk{display:inline-flex;align-items:center;gap:5px;background:rgba(201,150,63,.08);color:var(--gold);font-size:9px;font-weight:500;border-radius:2px;padding:3px 8px;margin-top:10px;letter-spacing:.06em;border:1px solid rgba(201,150,63,.15);}

/* Colour pills */
.pcard-colours{display:flex;flex-wrap:wrap;gap:4px;margin-bottom:10px;}
.clr-pill{padding:4px 10px;border-radius:2px;font-size:10px;font-weight:400;border:1px solid rgba(255,255,255,.1);background:transparent;color:var(--t3);transition:all .2s;line-height:1.4;}
.clr-pill.on{background:rgba(201,150,63,.12);border-color:var(--gold);color:var(--gold);}
.clr-pill:hover:not(.on){background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.2);color:var(--t1);}

/* Card footer */
.pcard-foot{padding:14px 20px 18px;border-top:1px solid rgba(255,255,255,.05);display:flex;gap:8px;align-items:center;}
.qty-ctrl{display:flex;align-items:center;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);border-radius:3px;overflow:hidden;flex-shrink:0;}
.qty-b{background:none;border:none;width:30px;height:36px;font-size:16px;color:var(--t2);display:flex;align-items:center;justify-content:center;transition:background .15s;font-weight:300;}
.qty-b:hover{background:rgba(201,150,63,.1);}
.qty-v{width:30px;text-align:center;font-size:13px;font-weight:600;color:var(--t1);border-left:1px solid rgba(255,255,255,.07);border-right:1px solid rgba(255,255,255,.07);line-height:36px;}
.order-btn{flex:1;display:flex;align-items:center;justify-content:center;gap:6px;background:rgba(201,150,63,.1);color:var(--gold);border:1px solid rgba(201,150,63,.25);border-radius:2px;padding:10px 12px;font-size:11px;font-weight:500;text-decoration:none;transition:all .25s;letter-spacing:.07em;text-transform:uppercase;}
.order-btn:hover{background:rgba(201,150,63,.18);border-color:rgba(201,150,63,.45);box-shadow:0 0 20px rgba(201,150,63,.08);}
.order-btn svg{width:12px;height:12px;fill:var(--gold);flex-shrink:0;}
.detail-btn{width:36px;height:36px;border-radius:2px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);display:flex;align-items:center;justify-content:center;transition:background .2s,border-color .2s;flex-shrink:0;}
.detail-btn:hover{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15);}
.detail-btn svg{width:13px;height:13px;stroke:var(--t3);fill:none;stroke-width:2;}

/* Empty state */
.empty-msg{grid-column:1/-1;padding:96px 0;text-align:center;background:#0d0d0d;}
.empty-msg .ei{font-size:48px;margin-bottom:20px;opacity:.3;}
.empty-msg h3{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:400;color:var(--t2);margin-bottom:8px;}
.empty-msg p{font-size:14px;color:var(--t4);}

/* ══ MARQUEE DIVIDER ══ */
.mqdiv{background:#040404;padding:22px 0;overflow:hidden;margin:0;border-top:1px solid rgba(255,255,255,.03);border-bottom:1px solid rgba(255,255,255,.03);}
.mqd-track{display:flex;gap:0;animation:scrl2 30s linear infinite;width:max-content;}
.mqd-item{display:flex;align-items:center;gap:0;font-family:'Cormorant Garamond',serif;font-size:clamp(32px,4.5vw,60px);font-weight:600;color:rgba(255,255,255,.04);letter-spacing:-.03em;white-space:nowrap;padding:0 40px;font-style:italic;}
.mqd-item span{color:rgba(201,150,63,.08);}
@keyframes scrl2{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ══ EDITORIAL STRIP ══ */
.editorial{background:#040404;padding:96px 48px;border-top:1px solid rgba(255,255,255,.03);}
.ed-inner{max-width:1280px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;}
.ed-text .sec-kicker{color:rgba(201,150,63,.7);}
.ed-text .sec-h{color:var(--t1);}
.ed-text .sec-h em{color:rgba(242,237,230,.38);font-style:italic;}
.ed-text p{font-size:15px;color:rgba(242,237,230,.38);line-height:1.9;margin-top:20px;}
.ed-text p+p{margin-top:14px;}
.ed-cta{display:flex;gap:12px;margin-top:36px;flex-wrap:wrap;}
.btn-wa-big{display:inline-flex;align-items:center;gap:10px;background:var(--wa);color:white;border:none;border-radius:2px;padding:14px 28px;font-size:13px;font-weight:500;text-decoration:none;transition:all .25s;letter-spacing:.06em;text-transform:uppercase;}
.btn-wa-big:hover{background:var(--wa2);transform:translateY(-2px);box-shadow:0 8px 28px rgba(37,211,102,.25);}
.btn-wa-big svg{width:18px;height:18px;fill:white;}
.ed-feats{display:flex;flex-direction:column;gap:2px;}
.ed-feat{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:0;padding:22px 24px;display:flex;align-items:center;gap:18px;transition:all .3s;}
.ed-feat:hover{background:rgba(201,150,63,.04);border-color:rgba(201,150,63,.15);}
.ed-feat-em{width:46px;height:46px;border-radius:0;background:rgba(201,150,63,.08);border:1px solid rgba(201,150,63,.12);display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;}
.ed-feat-t{font-size:14px;font-weight:500;color:var(--t1);}
.ed-feat-d{font-size:12px;color:var(--t4);margin-top:4px;line-height:1.6;}

/* ══ MODAL ══ */
.ovl{position:fixed;inset:0;z-index:700;background:rgba(4,4,4,.88);backdrop-filter:blur(16px);display:flex;align-items:center;justify-content:center;padding:20px;opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s;}
.ovl.open{opacity:1;visibility:visible;}
.mdl{background:#0e0e0e;border:1px solid rgba(255,255,255,.06);border-radius:2px;width:100%;max-width:600px;max-height:92vh;overflow-y:auto;transform:scale(.95) translateY(24px);transition:transform .5s cubic-bezier(.16,1,.3,1);position:relative;}
@media(max-width:480px){
  .mdl{max-height:100%;height:100%;border-radius:0;max-width:none;}
  .ovl{padding:0;}
}
.ovl.open .mdl{transform:none;}
.mdl-top{background:linear-gradient(135deg,#131310 0%,#0d0d0a 100%);height:240px;display:flex;align-items:center;justify-content:center;position:relative;border-bottom:1px solid rgba(255,255,255,.05);}
@media(max-width:480px){
  .mdl-top{height:180px;border-radius:0;}
  .mdl-body{padding-bottom:120px;}
}
.mdl-em{font-size:96px;line-height:1;opacity:.6;}
.mdl-x{position:absolute;top:18px;right:18px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:2px;width:36px;height:36px;display:flex;align-items:center;justify-content:center;font-size:16px;color:var(--t3);transition:all .2s;}
.mdl-x:hover{background:rgba(255,255,255,.1);color:var(--t1);}
.mdl-body{padding:32px;}
.mdl-cr{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;}
.mdl-cat{font-size:10px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);}
.mdl-sku{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);font-size:10px;color:var(--t4);padding:3px 10px;border-radius:2px;}
.mdl-name{font-family:'Cormorant Garamond',serif;font-size:36px;font-weight:400;color:var(--t1);letter-spacing:-.03em;margin-bottom:28px;line-height:.95;}
.mdl-specs{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:28px;}
.mdl-spec{background:rgba(255,255,255,.03);border-radius:2px;padding:14px 16px;border:1px solid rgba(255,255,255,.06);}
.mdl-spec-l{font-size:9px;color:var(--t4);text-transform:uppercase;letter-spacing:.12em;margin-bottom:5px;}
.mdl-spec-v{font-size:15px;font-weight:500;color:var(--t1);}
.mdl-pzone{display:flex;align-items:center;justify-content:space-between;padding:22px 0;border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06);margin-bottom:24px;}
.mdl-price{font-family:'Cormorant Garamond',serif;font-size:50px;font-weight:600;color:var(--t1);letter-spacing:-.04em;line-height:1;}
.mdl-pvat{font-size:12px;color:var(--t4);margin-top:6px;}
.mdl-blkbdg{background:rgba(201,150,63,.07);border:1px solid rgba(201,150,63,.15);border-radius:2px;padding:12px 18px;text-align:center;}
.mdl-blk-t{font-size:12px;font-weight:500;color:var(--gold);}
.mdl-blk-d{font-size:11px;color:rgba(201,150,63,.55);margin-top:3px;}
.mdl-qrow{display:flex;align-items:center;gap:16px;margin-bottom:22px;}
.mdl-qlbl{font-size:13px;font-weight:400;color:var(--t3);}
.mdl-qctrl{display:flex;align-items:center;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:2px;overflow:hidden;}
.mq-btn{background:none;border:none;width:44px;height:44px;font-size:20px;font-weight:300;color:var(--t3);display:flex;align-items:center;justify-content:center;transition:background .15s;}
.mq-btn:hover{background:rgba(201,150,63,.08);color:var(--gold);}
.mq-n{width:52px;text-align:center;font-size:18px;font-weight:600;color:var(--t1);line-height:44px;border-left:1px solid rgba(255,255,255,.07);border-right:1px solid rgba(255,255,255,.07);}
.mdl-tot{margin-left:auto;text-align:right;}
.mdl-tot-l{font-size:9px;text-transform:uppercase;letter-spacing:.12em;color:var(--t4);}
.mdl-tot-v{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:600;color:var(--t1);letter-spacing:-.02em;}
.mdl-wa{display:flex;align-items:center;justify-content:center;gap:12px;background:var(--wa);color:white;border:none;border-radius:2px;padding:18px;font-size:15px;font-weight:600;width:100%;text-decoration:none;transition:var(--transition);letter-spacing:.04em;}
.mdl-wa:hover{background:var(--wa2);transform:translateY(-2px);box-shadow:0 10px 32px rgba(37,211,102,.25);}
.mdl-wa svg{width:20px;height:20px;fill:white;}
.mdl-note{text-align:center;font-size:11px;color:var(--t4);margin-top:12px;line-height:1.7;}

/* ══ CART DRAWER ══ */
.cscrim{position:fixed;inset:0;z-index:600;background:rgba(4,4,4,.72);backdrop-filter:blur(8px);opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s;}
.cscrim.open{opacity:1;visibility:visible;}
.cdwr{position:fixed;top:0;right:0;bottom:0;z-index:610;width:420px;background:#0c0c0c;border-left:1px solid rgba(255,255,255,.06);box-shadow:-24px 0 80px rgba(0,0,0,.6);transform:translateX(110%);transition:transform .5s cubic-bezier(.16,1,.3,1);display:flex;flex-direction:column;}
.cdwr.open{transform:none;}
.cdwr-head{padding:28px 28px 22px;border-bottom:1px solid rgba(255,255,255,.06);display:flex;align-items:center;justify-content:space-between;}
.cdwr-head h3{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:400;letter-spacing:-.02em;color:var(--t1);}
.cdwr-x{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);border-radius:2px;width:36px;height:36px;display:flex;align-items:center;justify-content:center;font-size:16px;color:var(--t3);transition:all .2s;}
.cdwr-x:hover{background:rgba(255,255,255,.1);color:var(--t1);}
.cdwr-body{flex:1;overflow-y:auto;padding:22px 28px;}
.cart-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center;gap:14px;padding:48px 0;}
.cart-empty-i{font-size:48px;opacity:.2;}
.cart-empty-t{font-family:'Cormorant Garamond',serif;font-size:24px;font-weight:400;color:var(--t2);}
.cart-empty-d{font-size:13px;color:var(--t4);line-height:1.7;}
.citem{display:flex;align-items:center;gap:14px;padding:16px 0;border-bottom:1px solid rgba(255,255,255,.05);}
.citem-ic{width:58px;height:58px;border-radius:2px;background:#151515;overflow:hidden;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;}
.citem-ic img{width:100%;height:100%;object-fit:cover;display:block;}
.citem-info{flex:1;min-width:0;}
.citem-n{font-size:14px;font-weight:400;color:var(--t1);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.citem-d{font-size:11px;color:var(--t4);margin-top:3px;}
.citem-p{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600;color:var(--t1);white-space:nowrap;}
.citem-rm{background:none;border:none;color:var(--t4);font-size:20px;transition:color .15s;padding:4px;flex-shrink:0;}
.citem-rm:hover{color:rgba(255,100,100,.7);}
.cdwr-foot{padding:22px 28px;border-top:1px solid rgba(255,255,255,.06);}
.ctot-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;}
.ctot-l{font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:var(--t4);}
.ctot-v{font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:600;color:var(--t1);letter-spacing:-.03em;}
.csend{display:flex;align-items:center;justify-content:center;gap:10px;background:rgba(201,150,63,.12);color:var(--gold);border:1px solid rgba(201,150,63,.3);border-radius:2px;padding:16px;font-size:14px;font-weight:500;width:100%;text-decoration:none;transition:var(--transition);letter-spacing:.06em;text-transform:uppercase;}
.csend:hover{background:rgba(201,150,63,.2);border-color:rgba(201,150,63,.5);box-shadow:0 0 30px rgba(201,150,63,.08);}
.csend svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:2;}
.cdwr-note{font-size:10px;color:var(--t4);text-align:center;margin-top:10px;line-height:1.7;}

/* ══ FOOTER ══ */
footer{background:#040404;padding:80px 56px 0;border-top:1px solid rgba(255,255,255,.04);}
.foot-inner{max-width:1280px;margin:0 auto;}
.foot-top{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:64px;padding-bottom:64px;border-bottom:1px solid rgba(255,255,255,.04);}
.fbrand-name{font-family:'Cormorant Garamond',serif;font-size:36px;font-weight:400;color:var(--t1);letter-spacing:-.03em;margin-bottom:14px;line-height:.95;}
.fbrand-desc{font-size:13px;color:rgba(242,237,230,.28);line-height:1.9;max-width:260px;margin-bottom:32px;}
.fwa-btn{display:inline-flex;align-items:center;gap:9px;background:var(--wa);color:white;border:none;border-radius:2px;padding:12px 22px;font-size:12px;font-weight:500;text-decoration:none;transition:all .25s;letter-spacing:.05em;text-transform:uppercase;}
.fwa-btn:hover{background:var(--wa2);transform:translateY(-2px);box-shadow:0 6px 20px rgba(37,211,102,.2);}
.fwa-btn svg{width:15px;height:15px;fill:white;}
.fcol-t{font-size:8px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:rgba(255,255,255,.18);margin-bottom:22px;}
.fcol ul{list-style:none;display:flex;flex-direction:column;gap:14px;}
.fcol ul li a{font-size:13px;color:rgba(255,255,255,.32);text-decoration:none;transition:color .2s;display:flex;align-items:center;gap:8px;}
.fcol ul li a:hover{color:rgba(255,255,255,.75);}
.fcol ul li a::before{content:'';display:block;width:8px;height:1px;background:currentColor;opacity:.3;flex-shrink:0;transition:width .25s,opacity .25s;}
.fcol ul li a:hover::before{width:14px;opacity:.7;}
.foot-bottom{display:flex;align-items:center;justify-content:space-between;padding:22px 0;max-width:1280px;margin:0 auto;border-top:1px solid rgba(255,255,255,.04);}
.foot-bottom p{font-size:10px;color:rgba(255,255,255,.16);letter-spacing:.06em;}
.foot-wa-num a{color:rgba(255,255,255,.22);text-decoration:none;font-size:10px;letter-spacing:.04em;}
.foot-wa-num a:hover{color:rgba(255,255,255,.55);}

/* ══ REVEAL ══ */
.rv{opacity:0;transform:translateY(28px);transition:opacity .9s ease,transform .9s ease;}
.rv.in{opacity:1;transform:none;}

/* ══ BOTTOM NAV ══ */
.bnav{display:none;position:fixed;bottom:0;left:0;right:0;background:rgba(12,12,12,.97);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);height:64px;border-top:1px solid rgba(255,255,255,.06);z-index:450;align-items:center;justify-content:space-around;padding:0 4px;}
.bnav-btn{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:8px;font-weight:500;color:var(--t4);text-decoration:none;position:relative;padding:8px 14px;border-radius:0;letter-spacing:.06em;text-transform:uppercase;transition:color .15s;min-width:56px;}
.bnav-btn svg{width:19px;height:19px;stroke:currentColor;fill:none;stroke-width:1.6;}
.bnav-btn.on{color:var(--gold);}
.bnav-btn.on svg{stroke:var(--gold);}
.bnav-bdg{position:absolute;top:4px;right:8px;background:var(--gold);color:#090909;font-size:8px;height:15px;min-width:15px;border-radius:100px;display:flex;align-items:center;justify-content:center;padding:0 3px;font-weight:700;}

/* ══ MOBILE SEARCH OVERLAY ══ */
.srch-overlay{display:none;position:fixed;inset:0;z-index:600;background:rgba(4,4,4,.88);backdrop-filter:blur(12px);padding:20px 16px;}
.srch-overlay.open{display:flex;flex-direction:column;gap:12px;}
.srch-overlay-bar{display:flex;align-items:center;background:#151515;border:1px solid rgba(255,255,255,.08);border-radius:2px;overflow:hidden;}
.srch-overlay-bar svg{width:17px;height:17px;stroke:var(--t4);fill:none;stroke-width:2;flex-shrink:0;margin-left:16px;}
.srch-overlay-bar input{flex:1;border:none;outline:none;font-family:'DM Sans',sans-serif;font-size:17px;color:var(--t1);padding:16px 12px;background:transparent;}
.srch-overlay-close{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:2px;color:var(--t2);font-size:12px;font-weight:500;padding:12px 24px;align-self:flex-start;min-height:44px;letter-spacing:.06em;text-transform:uppercase;}

/* ══ RESPONSIVE BREAKPOINTS ══ */
@media(max-width:1200px){
  .pgrid{grid-template-columns:repeat(3,1fr);}
}

@media(max-width:960px){
  nav{padding:0 16px;gap:8px;}
  .nav-mid{display:none;}
  .srch{width:160px;}
  .nwa{display:none;}
  .hero-content{grid-template-columns:1fr;}
  .hero-l{padding:80px 24px 40px;}
  .hero-r{display:none;}
  .hero-scroll{left:24px;}
  .statsbar .stats-inner{grid-template-columns:repeat(2,1fr);}
  .stat-item{border-bottom:1px solid rgba(255,255,255,.04);}
  .products-section{padding:48px 20px;}
  .pgrid{grid-template-columns:repeat(2,1fr);}
  input,textarea,select{font-size:16px!important;}
  .ed-inner{grid-template-columns:1fr;}
  .editorial{padding:60px 20px;}
  .foot-top{grid-template-columns:1fr 1fr;gap:32px;}
  footer{padding:48px 20px 0;}
  .foot-bottom{flex-direction:column;gap:8px;text-align:center;padding:20px 0;}
  .cdwr{width:100%;}
  .cdwr-body{padding:16px 20px;}
  .cdwr-head{padding:20px 20px 16px;}
  .cdwr-foot{padding:16px 20px;}
  #dot,#ring{display:none;}
  .pcard:hover{transform:none;}
}

@media(max-width:640px){
  .pgrid{grid-template-columns:repeat(2,1fr);}
  .pcard-img{aspect-ratio:4/3;}
  .qty-ctrl{display:none;}
  .add-to-cart-btn{display:none;}
  .order-btn{flex:1;font-size:11px;padding:11px 8px;border-radius:2px;letter-spacing:.04em;}
  .detail-btn{display:none;}
  .pcard-foot{padding:10px 12px 12px;gap:8px;}
  .pcard-bulk{font-size:9px;padding:2px 7px;}
}

@media(max-width:480px){
  nav{padding:0 12px;gap:6px;height:58px;}
  .nl-logo-img{height:32px;}
  .nl-main,.nl-pre,.nwa{display:none!important;}
  .nav-r{gap:6px;}
  .srch{width:38px;height:38px;border-radius:2px;justify-content:center;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.04);}
  .srch input{display:none;}
  .srch-ic{padding:0;width:100%;justify-content:center;}
  .ncrt{width:38px;height:38px;border-radius:2px;}
  .ncrt svg{width:15px;height:15px;}
  .bnav{display:flex;}
  body{padding-bottom:72px;}
  .hero{min-height:auto;}
  .hero-l{padding:72px 20px 32px;}
  .hero h1{font-size:clamp(38px,10vw,56px);letter-spacing:-.025em;}
  .hero-sub{font-size:14px;margin-bottom:28px;}
  .hero-actions{gap:10px;}
  .btn-solid,.btn-ghost{padding:13px 24px;font-size:12px;border-radius:2px;}
  .hero-scroll{display:none;}
  .statsbar .stats-inner{grid-template-columns:repeat(2,1fr);}
  .stat-item{padding:18px 20px;}
  .stat-num{font-size:30px;}
  .stat-ic{width:40px;height:40px;}
  .products-section{padding:32px 14px 48px;}
  .sec-lead{flex-direction:column;align-items:flex-start;gap:8px;margin-bottom:20px;padding-bottom:16px;}
  .sec-h{font-size:28px;}
  .filter-bar{gap:5px;margin-bottom:24px;padding-bottom:12px;}
  .ftab{padding:7px 12px;font-size:10px;}
  .pgrid{grid-template-columns:repeat(2,1fr);gap:1px;padding:0;}
  .pcard-img{aspect-ratio:4/3;}
  .pcard-body{padding:10px 12px 6px;}
  .pcard-name{font-size:15px;margin-bottom:6px;}
  .pcard-cat{font-size:8px;}
  .pcard-price{font-size:20px;}
  .pcard-price-unit{font-size:9px;}
  .pcard-placeholder span{font-size:44px;}
  .clr-pill{font-size:9px;padding:2px 7px;}
  .pcard-foot{padding:8px 10px 10px;}
  .order-btn{font-size:10px;padding:10px 6px;border-radius:2px;gap:3px;}
  .order-btn svg{width:10px;height:10px;}
  .badge-vat{font-size:7px;padding:3px 6px;}
  .badge-del{font-size:7px;padding:3px 6px;}
  .mdl-body{padding:20px;}
  .mdl-name{font-size:26px;}
  .mdl-price{font-size:36px;}
  .mdl-specs{grid-template-columns:1fr 1fr;}
  .citem-ic{width:44px;height:44px;border-radius:2px;}
  .citem-n{font-size:13px;}
  .ctot-v{font-size:26px;}
  .editorial{padding:48px 16px;}
  .fbrand-name{font-size:26px;}
  .foot-top{grid-template-columns:1fr;gap:28px;}
  footer{padding:40px 16px 0;}
  #chkOvl{padding:0;align-items:flex-end;}
  #chkOvl .mdl{border-radius:0;max-height:90vh;max-width:100%;}
  .ann{padding:8px 0;}
  .ann-item{font-size:10px;}
}

/* ══ TOAST ══ */
.toast{position:fixed;bottom:88px;left:50%;transform:translateX(-50%) translateY(16px);background:#151515;color:var(--t1);padding:12px 24px;border-radius:2px;font-size:13px;font-weight:400;z-index:9000;opacity:0;transition:all .3s;pointer-events:none;border:1px solid rgba(255,255,255,.08);white-space:nowrap;max-width:90vw;text-align:center;letter-spacing:.04em;}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
.toast.success{border-color:rgba(201,150,63,.25);color:var(--gold);}
.toast.error{border-color:rgba(255,80,80,.2);color:rgba(255,150,150,.8);}

/* ══ FLOATING WHATSAPP (MOBILE) ══ */
.wa-fab{display:none;position:fixed;bottom:76px;right:16px;z-index:440;width:52px;height:52px;border-radius:50%;background:var(--wa);color:white;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(37,211,102,.3);border:none;text-decoration:none;transition:transform .2s,box-shadow .2s;}
.wa-fab svg{width:26px;height:26px;fill:white;}
.wa-fab:active{transform:scale(.92);}
@media(max-width:480px){.wa-fab{display:flex;}}

/* ══ SKELETON ══ */
.skeleton{background:linear-gradient(90deg,#131313 25%,#1a1a1a 50%,#131313 75%);background-size:200% 100%;animation:shimmer 1.5s infinite;border-radius:0;}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}
.skel-card{background:#0f0f0f;border:1px solid rgba(255,255,255,.04);border-radius:0;overflow:hidden;}
.skel-img{aspect-ratio:1;width:100%;}
.skel-body{padding:20px;display:flex;flex-direction:column;gap:12px;}
.skel-line{height:12px;border-radius:0;}
.skel-line.wide{width:75%;}
.skel-line.narrow{width:40%;}
.skel-line.price{height:18px;width:50%;}
"""

# ── Build new file ────────────────────────────────────────────────────────────
new_content = (
    content[:547]
    + new_font_link
    + "\n"
    + style_open
    + NEW_CSS
    + content[style_end:]
)

with open(
    r"c:\Users\dell\OneDrive\Desktop\mcc shop\backend\mcc-shop-backend\public\index.html",
    "w",
    encoding="utf-8",
) as f:
    f.write(new_content)

print("Done. File written.")
print(f"Old length: {len(content)}")
print(f"New length: {len(new_content)}")
