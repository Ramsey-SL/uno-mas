# UNO MÁS · MERCH & MENU PROJECT · START HERE
**Last updated:** April 22, 2026  

> **Session 7 Consolidation (April 24, 2026):** Two Netlify sites (asset-hub + template-hub) previously served identical content. They were consolidated into a single Brand Hub at https://uno-mas-asset-hub.netlify.app. The `uno-mas-template-hub` site is deprecated. See `Template-Hub/CONSOLIDATION.md` for details.

**Session:** Cowork / Strategy Labs  
**Status:** Active — multiple design directions in review

---

## LIVE SITE
**Template Hub:** https://uno-mas-template-hub.netlify.app  
**Netlify Site ID:** `ed4907ff-b429-4b0f-83f5-1b33eace1ada`  
**Netlify Admin:** https://app.netlify.com/projects/uno-mas-template-hub  
**Team:** Fulcrum (ramsey-o7de640)

### Key Pages Live Now
| URL | What It Is |
|-----|------------|
| `/` (index.html) | Hub — tabs for Web, Cards, Merch, Illustration, Social, Brand |
| `/merch-2026.html` | **Main merch concepts page** — all 3 directions, 22 mockups |
| `/menus.html` | **Menu preview page** — all 6 layouts with live iframe previews |
| `/2026-collection.html` | Original 2026 collection + Comedy Series + Style Showdown |
| `/menus/brunch-menu-layouts.html` | Standard menu layouts A & B (full interactive) |
| `/menus/brunch-menu-illustrated.html` | Illustrated C1–C4 (tabbed, full interactive) |
| `/sticker-collection-dashboard.html` | Sticker collection dashboard |

---

## WHAT WAS BUILT THIS SESSION

### 1. Merch Concept System — 3 Design Directions

#### Direction A: Comfort Colors / Feminine (the approved direction)
- **Style:** Trendy Etsy-core, Comfort Colors neutral shirts, thin-line illustrations, script + condensed serif type combos, warm inks (navy, terracotta, mauve)
- **Reference:** Margarita Cocktail Club ESTD style shirts on Pinterest
- **V5–V8 are the locked style** (V1–V4 were earlier attempts, archived)

#### Direction B: Illustrated / Engraving (heritage/collectible)
- **Style:** Fine-line engraving on cream shirts, navy & gold ink, western americana
- **Reference:** Sendero Provisions, Fieldschool Brand
- **Status:** Cinco & Summer series complete

#### Direction C: Western Americana (original, superseded by A+B)
- Original mockups still saved in `01_Comedy-Series-V1-Western/`

---

## APPROVED PHRASES — FINAL LIST

### Existing Comedy Series (needs regeneration in Comfort Colors style where not done)
| # | Main Phrase | Tagline | Supporting Text | Status |
|---|---|---|---|---|
| 1 | TACOS | *Before Vows* | Est. 2022 · Uno Más | ✅ Generated V2 |
| 2 | *will work for birria* | — | — | ✅ Generated V2 |
| 3 | MÁS TACOS MENOS PROBLEMAS | — | Est. 2022 · Uno Más · Spokane, WA | ✅ Generated V2 |
| 4 | BORN TO | *Brunch* | Brunch Club · Est. 2022 | ✅ Generated V2 |
| 5 | SPOKANE'S | *Hottest Mess* | Est. 2022 · Spokane, WA | ✅ Generated V2 |
| 6 | *feed me tacos* | and tell me I'm pretty | — | ✅ Generated V2 |
| 7 | LONG LIVE | *Tacos* | Uno Más · Spokane | ✅ Generated V2 |

### Marg Season
| # | Main Phrase | Tagline | Supporting Text | Status |
|---|---|---|---|---|
| M1 | MARGARITA | *Cocktail Club* | ESTD · Est. 2022 · Uno Más | ✅ V5 |
| M2 | *in my marg era* | — | — | ✅ V6 |
| M3 | UNO MÁS MARGARITA SOCIAL CLUB | — | SPOKANE, WA | ✅ V7 |
| M4 | *just here for the margs* | — | — | ✅ V8 |

### New Approved Phrases (generated, on merch-2026.html)
| # | Main Phrase | Tagline | Supporting Text | Status |
|---|---|---|---|---|
| A | TACOS | *are a Lifestyle* | Uno Más · Est. 2022 | ✅ Generated |
| D | SUNDAY MOOD | *Tacos & Margs* | Uno Más · Spokane | ✅ Generated |
| E | THE TACO CLUB | — | Est. 2022 · Spokane, WA | ✅ Generated |
| H | *brunch is my* | LOVE LANGUAGE | Est. 2022 · Uno Más | ✅ Generated |
| J | CERTIFIED | *Margarita Enthusiast* | Uno Más · Est. 2022 · Spokane, WA | ✅ Generated |
| N | BAD DECISIONS | *Good Tacos* | Uno Más · Est. 2022 | ✅ Generated |
| L | TEQUILA IS CHEAPER | *than Therapy* | Uno Más · Spokane | ✅ Generated |

### Notes on Phrases
- **EST. standard:** Always "Est. 2022" (not ESTD, not Est. alone)
- **Brand text standard:** "Uno Más · Spokane, WA" or "Uno Más · Est. 2022" — pick one per design
- **Lowercase phrases** (V8/V6 style) are intentional — part of the Comfort Colors aesthetic

---

## FILE STRUCTURE

```
Uno Más Marketing HQ/
├── START-HERE.md                          ← YOU ARE HERE
├── SESSION-5-HANDOFF.md                   ← Previous session notes
│
├── Template-Hub/                          ← NETLIFY SOURCE OF TRUTH
│   ├── index.html                         ← Hub homepage (updated)
│   ├── merch-2026.html                    ← NEW: All merch concepts (22 designs)
│   ├── menus.html                         ← NEW: Menu preview page (iframe previews)
│   ├── 2026-collection.html               ← Updated: Style Showdown + Comedy Series
│   ├── sticker-collection-dashboard.html
│   ├── assets/
│   │   ├── merch-2026/                    ← NEW: All 22 merch mockup images
│   │   └── *.png                          ← Original merch/sticker assets (44)
│   ├── menus/
│   │   ├── brunch-menu-layouts.html       ← Standard menus A & B
│   │   ├── brunch-menu-illustrated.html   ← Illustrated C1–C4 (tabbed)
│   │   └── images/                        ← 24 Gemini illustration PNGs
│   ├── illustration/
│   │   └── engraving-series-master-library.html  ← Optimized engraving library
│   └── NETLIFY.txt                        ← Deploy instructions
│
├── AI-Generated/
│   └── 2026-Merch-Mockups/
│       ├── 01_Comedy-Series-V1-Western/   ← Original western style (12 images)
│       ├── 02_Comedy-Series-V2-Comfort-Colors/  ← APPROVED direction (7 images)
│       ├── 03_Cinco-Summer-Illustrated/   ← Direction B + Direction A (8 images)
│       ├── 04_Marg-Season-Iterations/     ← V1–V8 iterations (8 images)
│       └── 05_New-Phrases-Approved/       ← 7 new approved phrases
│
├── 07_MENU_ASSETS/                        ← Original menu source files
├── 09_PRINT_MERCH/                        ← Original print/merch files
└── Template-Hub/previews/                 ← Local HTML preview files
    ├── cinco-summer-style-showdown.html
    ├── comedy-series-v2-comfort-colors.html
    ├── margs-all-iterations.html
    └── margs-direction-a-iterations.html
```

---

## HOW TO REDEPLOY TO NETLIFY

**Option A — Netlify MCP (from Cowork):**
The Netlify MCP is connected. Use the `netlify-deploy-services-updater` tool with site ID `ed4907ff-b429-4b0f-83f5-1b33eace1ada`. It will generate a proxy command — run that from the `Template-Hub/` folder (copy to local session space first to avoid resource deadlock).

**Option B — CLI:**
```bash
# Copy Template-Hub to local session space first (avoids deadlock)
cp -r "Template-Hub/" /tmp/deploy-hub/
cd /tmp/deploy-hub
npx netlify-cli deploy --prod --dir=. --no-build --site=ed4907ff-b429-4b0f-83f5-1b33eace1ada
```

**Option C — Drag and drop:**
Go to https://app.netlify.com/projects/uno-mas-template-hub/deploys and drag the Template-Hub folder.

> ⚠️ **IMPORTANT:** Files >2MB on the mounted volume cause "resource deadlock -35" errors when read directly. Always `cp -r` to `/tmp/` or local session space first before running deploys or reading large files.

---

## GEMINI API
- **Key:** `AIzaSyCFHoqgLu5-rGMWpV_hp-WYbrdPEoysH9o`
- **Model:** `imagen-4.0-generate-001`
- **Endpoint:** `https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict`
- **Config file:** `~/.gemini-creative-config.json` (on session machine)

**Quick generate:**
```bash
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key=AIzaSyCFHoqgLu5-rGMWpV_hp-WYbrdPEoysH9o" \
  -H "Content-Type: application/json" \
  -d '{"instances": [{"prompt": "YOUR PROMPT"}], "parameters": {"sampleCount": 1, "aspectRatio": "1:1"}}' \
  | python3 -c "import sys,json,base64; d=json.load(sys.stdin); open('output.png','wb').write(base64.b64decode(d['predictions'][0]['bytesBase64Encoded']))"
```

---

## PENDING DECISIONS / NEXT STEPS

### 🔴 Needs Decision
1. **Phrase finals** — Review all phrases in merch-2026.html and confirm final wording before production
2. **Hat designs** — Flagged as high priority but not yet started. Same Comfort Colors aesthetic would apply
3. **Menu prices** — All menus show "—" placeholders throughout. Need actual pricing to finalize

### 🟡 In Progress / Needs Work
4. **Cinco & Summer Direction A** — Traditional (pink/cyan) versions exist but were not feeling right; Direction B (illustrated) is strong. May want to revisit Direction A with the Comfort Colors treatment
5. **Sticker series** — Only 3 sticker mockups exist (Property of Uno Más, Monroe Street's Finest, Certified Delicious) in V1 style. Could regenerate in V2 Comfort Colors style
6. **Production files** — All mockups are AI concept images, not production-ready vector files. When ready to produce, will need actual graphic design files

### 🟢 Complete / Approved
- ✅ Comfort Colors Direction A style locked (V5–V8)
- ✅ Illustrated Direction B style locked (cream/navy engraving)
- ✅ All 7 comedy phrases + 7 new approved phrases generated
- ✅ Marg Season 4 directions generated
- ✅ Cinco & Summer 4 themes both directions generated
- ✅ Brunch menus (6 layouts) with Gemini illustrations deployed
- ✅ Full Template Hub live at Netlify with all pages navigable

---

## BRAND REFERENCE

**Colors:**
- Pink: `#E22690`
- Cyan/Blue: `#18BCDC`
- Navy: `#003366`
- Cream: `#F5F1EA`
- Gold: `#C4973A`

**Comfort Colors Direction A palette:**
- Shirts: pebble, bone, ivory, cream, dusty rose, sand, butter
- Inks: navy, terracotta (#C4602A), mauve/dusty rose, warm rust

**Direction B palette:**
- Shirts: cream, natural
- Inks: navy, gold

**Voice:** Fun, irreverent, locally proud (Spokane), taco-tequila culture, feminine-leaning but inclusive

---

## SKILLS TO USE IN NEXT SESSION

- `gemini-creative:gemini-generate` — for new mockup images
- `uno-mas-weekly-content-brief` — for social content
- `uno-mas-email-sms-campaigns` — for Klaviyo campaigns
- `uno-mas-asset-organizer` — for organizing new images into the library
- `brand-content-os:brand-os` — for brand-aligned copy
