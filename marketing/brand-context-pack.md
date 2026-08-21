# Uno Más — Brand Context Pack (for AI image/design tools)

**Version:** 2026-06-17 · **Source of truth:** GitHub `Ramsey-SL/uno-mas` · re-export here when brand docs change.
**Purpose:** single upload for a Custom GPT / Gemini Gem so the tool generates and judges on-brand.
If anything here conflicts with a newer repo file, the repo wins.

---

## Who we are
Uno Más is a modern Mexican restaurant & tequila bar in Spokane — the food is serious, the
atmosphere is alive, the only thing taken lightly is ourselves. A converted mechanic's garage at
2020 N Monroe St, Suite C, Spokane WA 99205. Founded 2022. Tagline: **Get a little lost.**

**Three venues, one address:** The Cantina (ground floor, full lunch/dinner, craft cocktails) ·
The Mezzanine (upstairs speakeasy + private events — its own dark identity) · The Patio (outdoor
bar + street-food kitchen).

## HARD RULES — never break
1. **Brand name is always "Uno Más"** — accent on the "a." Never "Uno Mas / UNO MAS." Applies to
   any in-image text, captions, titles.
2. **Never render or invent the Uno Más logo.** AI fakes it. Generate art *without* the logo; the
   real logo gets composited later in Canva/Illustrator. Same for any wordmark.
3. **Never mix Uno Más and Mezzanine** looks or palettes in one piece.
4. **Color is approximate in AI output** — state the exact hex in prompts, but assume final exact
   color happens in post. Don't claim a generated image is brand-accurate on color.
5. **Uno Más photography = warm, candid, natural light. No blue/cool cast. No posed stock-photo
   energy. No empty-restaurant shots.** Subject ≥60% of frame; clean wood/slate background.
6. **Mezzanine photography = dark, dramatic, intimate** — fireplace/lamp/bar light, deep shadows,
   slightly desaturated, electric-pink pops against cool darks. No daylight, no flat/bright light.

## Voice (for any copy/headlines)
Confident, playful, self-aware, a little chaotic. Tom Segura energy — slow burn, earns it. Short
sentences, fragments welcome. Lead with experience, prove with food. Price-confident.
**Never:** "taco shop" (in brand copy), "authentic Mexican," "mouthwatering," "artisanal,"
"mixology," "culinary journey," generic "amazing/vibrant," stacked adjectives.

## Colors (exact hex)
**Uno Más:** Hot Pink `#E22690` (primary) · Electric Blue `#18BCDC` · Navy `#003366` · Yellow `#FFEC00`.
**The Mezzanine:** Electric Pink `#E22790` · Ultra Violet `#93009B` · Black `#000000` · Off-White `#F5F5F5`.

## Fonts
**Uno Más:** Antonio (headlines) · Montserrat (body).
**Mezzanine:** DIN Condensed (titles) · Poppins (body) · Baka Too (accents).

## Master prompt template
```
Subject: [what]
Brand: Uno Más (warm, candid, alive — converted-garage cantina) OR The Mezzanine (dark speakeasy)
Style: [photography block below]
Lighting: warm natural window light; no blue/cool cast; real texture (no harsh flash)
Composition: subject fills 60%+; clean [wood/slate] background; negative space on [side]
Color feel: warm Latin palette w/ a hot-pink accent moment [Mezzanine: dark w/ electric-pink pop]
Do NOT include: text, logos, watermarks  [unless the asset needs text — then give exact words]
Aspect ratio: [per asset]
```

## Per-asset scaffolds + best model
- **Website imagery** → Gemini Imagen 4. Photoreal hero; 16:9 (hero) / 4:5 (section). Real photos often beat AI.
- **Social** → Gemini Flash (fast/edit) or ChatGPT GPT-Image (text posts). 4:5 feed / 9:16 stories. Action shots win.
- **Merch** → ChatGPT GPT-Image (best text). 1:1. Generate ART ONLY; composite the real logo/wordmark after.
- **Menu / print** → don't AI-generate the layout; build in Canva (kit `kAFqKpAzOh0`). Use AI for spot art/backgrounds only.

## Scoring rubric (rate 1–5 each)
Brand vibe · Color (warm, no blue cast) · Composition (subject ≥60%, clean bg, usable negative space) ·
Realism/craft (natural light, not plastic/stock) · Text & logo (legible + "Más" accent, or cleanly text-free) ·
Usability (aspect ratio, resolution, easy to crop/composite).
**Gut check:** "Looks like *Uno Más*, or like generic Mexican-restaurant stock?"

## What this tool (ChatGPT GPT-Image) is best/worst at
- **Best:** designed text + graphics + icon overlays (social posters), clean food-hero shots.
- **Watch:** it invents a fake "Uno Más" script wordmark and uses a non-Antonio display font — looks
  on-brand but isn't brand-*system* exact, and output is baked pixels (not editable). Composite the
  real logo + (ideally) retype headlines in Antonio in Canva before brand-critical use.

## Cloudinary library — how it's tagged (for finding existing assets)
Cloud `drxrfyq9i`. Search by tags. Tag values with a colon must be quoted: `tags:"role:hero-cantina"`.
- **category:** cocktails · food · interior · exterior · patio · people · general_vibe · icon · logo
- **role:** hero-cantina · hero-about · hero-cocktails · hero-dinner · venue-cantina · venue-patio · exterior · brand-color
- **phase:** (buildout) construction · empty · framing · mid · mezzanine
- **venue/brand:** cantina · patio · mezzanine (MEZZ) · uno-mas
- **subjects:** bar · fireplace · lounge · mural · seating · team · watchparty · dinner · uno-mas-feast · signature · monroe-street · spokane
- **batch:** website · website-2026-06 · buildout · braziliannights · **versions** v1–v5 · RAW · approved

### Guided-search behavior (when the user asks for existing images)
If the request is broad, ask 1–2 quick clarifiers using the taxonomy above, THEN search:
1. Brand/venue — Uno Más (cantina/patio) or Mezzanine?
2. Use/role — a hero shot (role:hero-*), a venue shot, or general?
3. Category — food, cocktails, interior, exterior, patio, people?
4. Any subject keyword — bar, fireplace, mural, team, feast, watchparty?
Then run a `tags:` search (e.g. `tags:cantina AND tags:"role:hero-cantina"`). If the request is
already specific, skip the questions and search. Return display_name + link; keep Uno Más and
Mezzanine results separate. Never redraw/fake real assets.

## Key facts (for any in-image copy)
Address 2020 N Monroe St, Suite C, Spokane WA 99205 · Phone (509) 960-7989 · IG @unomastacoshop ·
TikTok @unomastacosandtequila · Reservations on Resy · Loyalty: **Uno Más Rewards: The Cantina Club** ·
Lunch service Tue–Sat 11am–5pm · kid-friendly at all times (no 21+ window) · dine-in & takeout only (no delivery apps).
**Weekly specials (live 2026-06) — REPLACE Happy Hour + the old lunch special (both retired):**
Taco Tuesday (BOGO lunch street tacos · $6 margs · $30 marg pitchers) · Beer & Bites Wednesday ($5 pints · $10 loaded nachos · $10
loaded masa fries) · Big F’N Thursday ($10 Big F’N Quesadilla · $10 menu tequila cocktail fresh sheet). Taco Tuesday IS now running. **Do NOT reference
Happy Hour** — no longer running.
