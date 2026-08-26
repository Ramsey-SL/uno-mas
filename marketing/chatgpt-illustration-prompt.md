# ChatGPT Prompt — Uno Más Illustrated Promo Art

**Purpose:** generate the illustrated food/drink artwork that Claude cannot produce, in a form that
becomes a **reusable asset library** rather than another flat poster.

---

## The one thing to change from last time

The Weekend Special and Full Send toppers were generated as **finished composites** — headline, prices,
ribbon and art baked into a single flat PNG. That's why, when we audited the DAM, there were only
**3 illustration-tagged assets in 1,486**: the individual margarita glasses and chip-and-dip platter
don't exist as art. They exist only inside one 3506×4381 poster we now have to crop them out of.

> **Ask for isolated elements on a plain ground, with no text.** Then the same margarita can appear on a
> table topper, a Meta ad, an email header and a site tile — and the price can change without regenerating art.

---

## Step 1 — Give ChatGPT the brand context

Both repos are private, so ChatGPT needs explicit access. Easiest path first:

**A. GitHub connector (recommended)**
ChatGPT → Settings → Connectors → GitHub → authorize → grant `Ramsey-SL/uno-mas` and
`Ramsey-SL/uno-mas-marketing-agent`. Then in a Project, tell it which files to read (below).

**B. Make the agent repo public**
`uno-mas-marketing-agent` holds behavior only — skills, protocol, session logs. **No secrets, no
financials.** Making it public means any AI platform can fetch it by raw URL with zero auth, which is
the whole point of it being portable. The brand repo stays private. *Your call — but this is the
friction you keep hitting.*

**C. Upload the files** to a ChatGPT Project if you'd rather not connect anything.

### Files to load, in this order

| File | Repo | Why |
|---|---|---|
| `CLAUDE.md` | uno-mas | The brand brain — voice, the "Always Get Right" facts, current specials |
| `marketing/cloudinary-operating-guide.md` | uno-mas | Naming, folders, the print gate, standard transforms |
| `marketing/cloudinary-folder-structure.md` | uno-mas | Where art actually lives (public_id ≠ folder) |
| `marketing/brand/visual-identity.md` *(if present)* | uno-mas | Palette and type |
| `START-HERE.md` | agent repo | Session protocol |

---

## Step 2 — Paste this as the Project instruction

```
You are the Uno Más Art Director. Uno Más Tacos & Tequila is a taco and tequila restaurant in
Spokane, WA. Read CLAUDE.md and marketing/cloudinary-operating-guide.md in the Ramsey-SL/uno-mas
repo before your first response and follow them.

YOUR JOB: generate illustrated promo ELEMENTS — single food or drink subjects, isolated, no text.
You do not generate finished posters. Layout, headlines and pricing are assembled elsewhere.

HOUSE ILLUSTRATION STYLE (match this exactly — it is established, not up for reinterpretation):
- Editorial/comic-book food illustration. Confident near-black outlines, warm rather than pure black.
- Rich cel-style shading with visible highlight facets. Slightly retro, poster-like. Not photoreal,
  not cartoon-cute, not watercolor, not 3D render.
- Saturated, appetite-forward colour. Food reads glossy and fresh.
- Ground: FLAT off-white paper, #FCFBFB. Nothing else in the frame.
- CAST SHADOW: a halftone dot shadow in deep royal blue #012D79, sitting under and slightly
  left-to-right behind the subject, dots getting sparser as they move away. This is the single most
  recognizable part of the style — never a soft grey drop shadow.
- Subtle paper grain over the whole image.
- Three-quarter view, subject centered, generous margin, nothing cropped by the frame edge.

BRAND PALETTE (exact, sampled from live artwork):
  paper #FCFBFB · navy #011332 · pink #DC1548 · yellow #FBC001 · blue #00A6EF
  halftone shadow #012D79

HARD RULES:
- NO TEXT of any kind in the image. No prices, no logos, no labels, no signage, no menu boards.
  Text is added in layout. Any text you bake in makes the asset single-use and it gets rejected.
- NO starbursts, ribbons, banners, brush blocks or badges. Those are layout furniture.
- ONE subject per image.
- Output the LONGEST EDGE AT 2400px MINIMUM. Anything at or under 2048px fails our print gate and
  cannot be used on printed material. State the pixel dimensions with every image you deliver.
- Square (1:1) unless I ask for portrait. Portrait is 4:5.
- Never invent menu items, prices, or specials. If you need a menu fact, ask or read the repo.

DELIVERY: for each image give me
  1. the image
  2. a filename in our convention: YYYYMMDD_UM_<CATEGORY>_<Subject>_v#
     CATEGORY is one of FOOD, DRINK, COCKTAIL, BRUNCH, VENUE, PROMO
     e.g. 20260826_UM_COCKTAIL_HouseMargaritaPair_v1
  3. the pixel dimensions
  4. suggested tags: category:<cat>, type:illustration, line art, style:halftone-shadow
Target folder in Cloudinary: uno-mas/approved-assets/illustrations/<category>
```

---

## Step 3 — Ask for the assets

### Immediate need (gift card promo, Thu–Sun Aug 27–30)

```
Generate these as separate images, house style, no text:

1. A pair of gift cards — two flat rectangular plastic cards, rounded corners, overlapping at
   slightly opposing angles as if tossed on a table. One card teal (#00A6EF), one card pink
   (#DC1548). Blank faces — no numbers, no logos, no text of any kind. Subtle sheen so they read
   as plastic, not paper. Halftone blue cast shadow beneath. Square, 2400px minimum.

2. A pair of house margaritas — rocks glasses, heavy cut-crystal faceting, chili-salt rim in
   pink-red crystals, filled with amber-gold margarita and large clear ice. Three-quarter view,
   one glass slightly behind the other. Halftone blue cast shadow. Square, 2400px minimum.
   (We have this baked into one old poster — I want it as a standalone asset.)

3. A hand offering a gift card across a table — just forearm and hand, sleeve cropped at the
   wrist, holding a single blank teal card. Warm skin tones, same outline weight. Square, 2400px.
```

### The backlog worth clearing while you're in there

Every one of these is currently trapped inside a flat composite or doesn't exist:

| Asset | Needed for |
|---|---|
| Chip & dip trio platter (guac / queso / salsa, chips around a black oval tray) | Full Send, Weekend Special, Beer & Bites |
| Loaded nachos tower | Beer & Bites Wednesday |
| Loaded masa fries | Beer & Bites Wednesday |
| Lula wings on a blue plate with crema cup | Full Send |
| **Big F'N Quesadilla, whole, cut into wedges — the size of a medium pizza** | **Big F'N Thursday has no hero art at all** |
| Street tacos, three in a row in paper holders | Taco Tuesday |
| Marg pitcher with two glasses | Taco Tuesday ($30 pitchers) |
| Draft beer pint, condensation | Beer & Bites ($5 pints) |
| Paloma with lime wheel | Late Night Happy Hour ($8 palomas) |
| Tequila cocktail, coupe or rocks | Big F'N Thursday ($10 tequila cocktails) |

**Priority: the Big F'N Quesadilla.** Thursday's tile currently borrows a skirt steak photo and a
Mexican hot dog because nothing better exists in the library.

---

## Step 4 — When the art comes back

1. Check the stated dimensions. **Long edge under 2400px → send it back.** This is the gate that
   stopped us using the June photos on the table topper.
2. Upload to `uno-mas/approved-assets/illustrations/<category>` with a **bare public_id** and an
   explicit `asset_folder` — skipping `asset_folder` is how 188 assets ended up addressable at a path
   they don't live in.
3. Tag on upload: `category:<cat>`, `type:illustration`, `line art`, `style:halftone-shadow`,
   `print-ok`, `approved:yes`.
4. Tell Claude the public_ids and the layouts get rebuilt on real elements instead of crops.

## Why this compounds

Right now every promo needs new artwork because nothing is reusable. Ten illustrated elements at
2400px+, tagged and isolated, means the next table topper, Meta ad, email header and site tile are
**layout work, not generation work** — which is the half Claude can do in minutes.
