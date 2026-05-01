# Shared Prompt Fragments

Reusable snippets referenced by multiple stages. Load on demand.

## Voice fragment (used in Stages 4, 5)

```
You are writing for Uno Más Tacos & Tequila. Voice rules per
brand-intelligence-center/system-prompt.md:

- Confident, playful, self-aware, just a little chaotic. Tom Segura
  default register; Bert Kreischer for lunch/casual content only.
- Headlines max 50 chars, subheadlines max 80, CTAs max 25.
- No emojis in headlines. Per-channel emoji limits:
  Lunch/casual: 3-5
  Dinner: 1-2 max
  Mezzanine: 0-1
  Paid ads: 1-2
  Social organic: 3-5
- Never say: "authentic Mexican," "taco shop" (in brand descriptions),
  "mouthwatering," "culinary journey," "artisanal," "mixology,"
  "vibrant," "amazing" (generic), "perfect for any occasion,"
  "leverage," "utilize."
- Always say: "Modern Mexican," "house-smoked," "craft cocktails,"
  "Get a little lost," "Modern Latin-inspired."
- Never invent menu items — verify against MENU_AND_OFFERS.md.
- Never apologize for or explain pricing.
```

## Fabrication-rules fragment (used in Stage 4)

```
HARD RULES on fabrication:
- Do not invent menu items not in marketing-knowledge/knowledge-center/MENU_AND_OFFERS.md
- Do not invent prices, dates, times, URLs, phone numbers, social handles
- If a brief contains placeholders like [ADD PRICE] or [ADD DATE], preserve them
- If the user mentioned an item that's not in MENU_AND_OFFERS.md, ask before generating
- Approved URLs (use only when relevant and explicit):
  - unomastacoshop.com
  - resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila
  - karissa@unomastacoshop.com (private events)
- Approved social handles:
  - @unomastacoshop (Instagram, primary)
  - @unomastacosandtequila (TikTok)
- Address: 2020 N Monroe St, Suite C, Spokane WA 99205
- Phone: (509) 960-7989
```

## Brand-separation fragment (used in Stages 2, 3, 4)

```
Uno Más and The Mezzanine are SEPARATE visual identities. NEVER mix.

Uno Más main brand:
- Palette: Hot Pink #E22690, Electric Blue #18BCDC, Navy #003366, Yellow #FFEC00
- Typography: Antonio (headlines), Montserrat (body)
- Canva Kit: kAFqKpAzOh0
- Use for: Cantina floor, patio, lunch, dinner, brunch, Sunday Brunch,
  general restaurant content

The Mezzanine sub-brand:
- Palette: Electric Pink #E22790, Magenta #BF28BF, Ultra Violet #93009B,
  Black foundation
- Typography: DIN Condensed VF (titles), Poppins (body), Baka Too (accents)
- Canva Kit: kAGze1MPDmA
- Use for: Mezzanine atmosphere/late night, Mezzanine private events,
  speakeasy content

NEVER use Antonio in Mezzanine designs. NEVER use DIN Condensed in
Uno Más designs. NEVER use Hot Pink #E22690 with Mezzanine typography.
```

## Output-schema reminder (used in Stages 1, 4, 5)

```
Save outputs to the campaign folder:
campaigns/{YYYY-MM}-{slug}/
├── brief.md (Stage 1)
├── decisions.md (Stages 2, 3, 5 append; Stage 1 creates)
├── concepts/
│   ├── concept-N.md (Stage 4 per concept)
│   └── concept-N.png (Stage 4 optional via Nano Banana)
├── final/
│   ├── final.md (Stage 5)
│   ├── final.png (Stage 5 optional)
│   └── notes.md (Stage 5)
└── retro.md (after Stage 5, optional)

Do not write outside this folder during a campaign run, except to
update files in `_styles/`, `_templates/`, or Ramsey's brand docs
if the user explicitly asks (and only with their confirmation —
those are the source of truth, not workflow scratch).
```

## Nano-Banana-prompt template (used in Stage 4)

```
{style hidden prompt}

Brand context (Uno Más main / Mezzanine — pick per venue):
- Palette: {hex codes from chosen style}
- Typography reference: {Antonio + Montserrat OR DIN Condensed + Poppins}
- Tagline: Get a little lost.

Campaign context:
- Name: {campaign_name}
- Audience: {target_audience}
- Daypart: {daypart_register}
- Key message: {key_offer}

Concept-specific direction:
- Tone: {tone_variant}
- Layout: {layout_direction}
- Primary asset description: {asset_description}

Required text (render EXACTLY, do not paraphrase):
- Headline: "{headline}"
- Subheadline: "{subheadline}"
- CTA: "{cta}"

Hard rules:
- No fabricated URLs, social handles, phone numbers, prices, dates
- No logos other than space for {logo_description} (will be composited later)
- Aspect ratio: {ratio}
- Brand separation: {Uno Más main palette OR Mezzanine sub-brand} ONLY
```

## When to load these fragments

- Stages 1-3: load `output-schema reminder` only
- Stage 4: load `voice fragment` + `fabrication-rules fragment` + `brand-separation fragment` + `nano-banana-prompt template` (if generating visuals)
- Stage 5: load `voice fragment` + `fabrication-rules fragment`
