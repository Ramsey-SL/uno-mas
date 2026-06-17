# Uno Más — AI Image Generation Playbook

How to generate brand visuals by testing **Gemini** and **ChatGPT** against each other, with
**Claude as art director + judge**. Manual workflow (no API setup). Entry point: `/CLAUDE.md`.

---

## The roles (important)

- **Gemini** — generates. *Imagen 4* (`imagen-4.0-generate-001`) for polished mockups; *Gemini 2.5
  Flash Image / "Nano Banana"* for fast iteration + image **editing** + decent in-image text.
- **ChatGPT** — generates. *GPT-Image-1* — best at following detailed instructions and rendering
  **legible text** in-image.
- **Claude** — does **not** make raster images. It writes the brand-locked prompt, holds the
  brand rules, and **scores the outputs** (it can see images). It can also produce **SVG/HTML/CSS**
  designs directly when you want vector/code, not a photo.

**Frame it as:** same prompt → Gemini vs GPT-Image → Claude judges which nails the brand.

---

## The workflow

1. Tell Claude the asset (type, subject, brand = Uno Más **or** Mezzanine, where it'll be used).
2. Claude returns **one brand-locked prompt** + the aspect ratio.
3. Paste the *same* prompt into ChatGPT and Gemini (3–4 variants each).
4. Paste outputs back to Claude → it scores against the rubric and suggests prompt tweaks.
5. Iterate the **prompt**, not the tool. Lock the model+prompt combo that wins per asset type.

---

## ⚠️ Hard brand guardrails (bake into every prompt)

- **Never mix Uno Más and Mezzanine** looks/palettes in one image.
- **AI can't be trusted with the logo or exact hex.** Generate the *imagery/style* with AI, then
  composite the **real logo** and retype **"Uno Más"** (with the accent!) in Canva/Illustrator.
  This is how we avoid repeating the baked-in "UNO MAS" (no-accent) merch problem.
- **Uno Más look:** warm, candid, natural light. Subject fills ≥60% of frame. Clean wood/slate/
  neutral background. **No cool/blue color cast. No posed stock-photo energy. No empty-restaurant
  shots.** Leave negative space on one side for caption overlay.
- **Mezzanine look:** dark, dramatic, intimate. Fireplace/lamp/bar light, deep shadows, slightly
  desaturated. Electric Pink pops against cool darks. No flat/bright/overhead light, no daylight.
- **Palettes (for reference — don't rely on AI to hit them exactly):**
  Uno Más = Hot Pink `#E22690`, Electric Blue `#18BCDC`, Navy `#003366`, Yellow `#FFEC00`.
  Mezzanine = Electric Pink `#E22790`, Ultra Violet `#93009B`, Black, Off-White `#F5F5F5`.

---

## Master prompt template (shared base)

```
Subject: [what — e.g. "Carne Asada plate, hands lifting one taco, cheese pull"]
Brand: Uno Más — modern Mexican restaurant & tequila bar, Spokane; converted mechanic's-garage
  space; warm, candid, alive, a little chaotic. [or: The Mezzanine — dark speakeasy upstairs]
Style: [photography style block per asset type below]
Lighting: warm natural window light; no blue/cool cast; texture preserved (no harsh flash)
Composition: subject fills 60%+ of frame; clean [wood/slate] background; negative space on [side]
Mood: makes you hungry/curious/envious; real, not styled-to-death
Color feel: warm Latin palette with a hot-pink accent moment [Mezzanine: dark with electric-pink pop]
Do NOT include: text, logos, watermarks [unless asset needs text — then specify exact words]
Aspect ratio: [per asset type]
```

---

## Per-asset-type scaffolds + which model to favor

### 🌐 Website imagery — *favor Gemini Imagen 4*
- Photoreal hero/section images; warm natural light; aspect **16:9** (hero) or **4:5** (section).
- Imagen 4 tends to win on natural-light realism. GPT-Image as challenger.
- **Reality check:** for a real venue, your own Cloudinary photography usually beats AI. Use AI for
  concepts, backgrounds, textures, and gaps — not as a substitute for real venue/food shots.

### 📱 Social content — *Gemini Flash for speed, GPT-Image for text posts*
- Aspect **4:5** (feed) / **9:16** (stories/reels covers). Action shots (cheese pull, pour) outperform static.
- Use Gemini 2.5 Flash Image to iterate fast and **edit** an existing shot. Use GPT-Image when the
  post needs legible on-image text — then still verify the "Más" accent.

### 👕 Merch designs — *favor ChatGPT GPT-Image (text), but composite the logo yourself*
- GPT-Image renders in-image text best. Aspect **1:1**.
- Generate the **artwork/illustration only**; add the real Uno Más logo + any "Uno Más" wordmark in
  Canva/Illustrator afterward. Never ship AI-rendered brand text to print.
- For screen print you need vector — run the chosen raster through Illustrator Image Trace, or have
  Claude produce an SVG version.

### 🍽️ Menu / print — *don't AI-generate the layout*
- AI image models are weak at multi-line legible text + precise layout. Build the menu/print piece
  in Canva (brand kit `kAFqKpAzOh0`) or a template. Use AI only for **decorative illustrations,
  backgrounds, or spot art** that you place into the real layout.

---

## Scoring rubric (Claude applies this to pasted outputs)

Rate each image 1–5 per dimension:

| Dimension | What "5" looks like |
|---|---|
| **Brand vibe** | Warm/candid/alive (Uno Más) or dark/dramatic (Mezzanine) — instantly on-brand |
| **Color** | Reads as the brand palette; warm tone, no blue cast (Uno Más) |
| **Composition** | Subject ≥60% frame, clean background, usable negative space |
| **Realism / craft** | Natural light, real texture; not plastic/over-rendered/stock |
| **Text & logo** | Any in-image text legible AND correct ("Uno Más" accent) — or cleanly text-free |
| **Usability** | Right aspect ratio, high-res, easy to crop/composite |

**Gut check:** "Does this look like *Uno Más*, or like a generic Mexican-restaurant stock photo?"
If generic → reject and tighten the prompt's specificity (the garage space, the neon TACOS sign,
house-smoked char, real hands).

---

## Quick model cheat-sheet

| Need | Best first try |
|---|---|
| Photoreal food/venue/website hero | Gemini Imagen 4 |
| Fast variations / edit an existing image | Gemini 2.5 Flash Image (Nano Banana) |
| Legible in-image text / instruction-heavy comps | ChatGPT GPT-Image-1 |
| Vector / code-based layout / SVG | Claude (direct) |
| Production layout with real type + brand kit | Canva (not raw AI) |

---

## Test findings (June 2026)

Ran two head-to-head rounds (Gemini vs ChatGPT, same prompt, same 6 base images).

**Round 1 — photoreal hero (food/venue):**
- **Gemini Imagen 4** wins *atmosphere & sense of place* — pulled in the TACOS neon, brick-garage,
  papel picado, real people. Best for website hero / About / brand storytelling.
- **ChatGPT GPT-Image** wins *clean food-hero* — tighter, more product-forward, added the drink.
  Best for menu & social product shots.

**Round 2 — text + graphics + icon overlay (Happy Hour promo):**
- **ChatGPT GPT-Image is the clear winner.** Best at integrated, *designed-poster* compositions:
  strong hierarchy, characterful display type, hand-drawn icon, on-brand playful energy. Both
  models got the "Más" accent right this round.
- **⚠️ Caveats that still require finishing in Canva:** the "Uno Más" wordmark GPT renders is an
  *invented script*, NOT the real logo; the display font is not Antonio; output is baked pixels
  (not editable). Looks on-brand but isn't brand-*system* exact.

**Working rule:** ChatGPT = fast concept + designed social posters → **finish by compositing the
real logo + (ideally) retyping the headline in Antonio in Canva** before brand-critical use.
Use Claude/SVG for editable, exactly-repeatable templates (e.g. a weekly Happy Hour post where
only the text changes). Use Gemini for photoreal atmosphere/website imagery.
