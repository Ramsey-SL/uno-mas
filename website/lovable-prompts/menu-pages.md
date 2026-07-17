# Lovable Prompt — Menu Pages (paste this into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Build /menu (hub) + /menu/dinner + /menu/lunch + /menu/cocktails in one pass. *(Update July 2026: Brunch is now LIVE as a tab at /menu?tab=brunch — Sundays 10am–4pm.)*

---

## PASTE BELOW THIS LINE INTO LOVABLE

Build four menu pages on this site, all powered by Supabase data already populated in the `menu_sections` and `menu_items` tables. Follow our existing brand system. Be production-ready, mobile-first, and SEO-optimized.

### Routes to build

1. `/menu` — Menu hub page (4 cards linking to dayparts)
2. `/menu/dinner` — Dinner menu (active campaign focus)
3. `/menu/lunch` — Lunch menu
4. `/menu/cocktails` — Cocktails + beer + non-alcoholic

### Data model — what's already in Supabase

```
menu_sections (18 published)
  - id, slug, name, daypart, description, display_order, is_published
  - daypart ∈ {'lunch','dinner','brunch','cocktails','raw-bar','sides','desserts','beverages','shareables'}

menu_items (69 published)
  - id, section_id, slug, name, description, price, is_signature, is_published, display_order
  - cloudinary_id (optional — most items don't have photos yet; handle gracefully)
  - dietary_tags (text array, optional)

assets
  - Query by tags to fetch images. Use existing helpers if `resolveImageByTags()` exists.
  - Hero tags: role:hero-dinner (5 photos), role:hero-lunch (4), role:hero-cocktails (1)
  - Future menu item photos will be tagged with the dish slug (e.g., `carne-asada`)
```

### Daypart query logic per page

| Page | Sections to include (by daypart) |
|---|---|
| `/menu/dinner` | `dinner`, `raw-bar`, `shareables`, `sides`, `desserts` |
| `/menu/lunch` | `lunch`, `shareables`, `sides`, `desserts` |
| `/menu/cocktails` | `cocktails`, `beverages` |

Sort sections by `display_order`. Within each section, sort items by `display_order`.

**Important:** Cocktails are NOT included on the dinner or lunch pages — they live on their own `/menu/cocktails` page (this mirrors the printed menus). Cross-link with a "See full cocktail menu" CTA on dinner + lunch pages.

### Brand visual rules (CRITICAL — pull from existing site)

- **Primary color (Uno Más Pink):** `#E22690` — use for accents, CTAs, signature item badges
- **Headlines / display:** Antonio Bold, all uppercase, tight letter-spacing
- **Body:** Montserrat, sentence case
- **Background:** White (Mezzanine sub-brand is separate, not used here)
- **Style ref:** raw textures, atmospheric lighting feel (already established in homepage hero)
- DO NOT use Mezzanine fonts (DIN Condensed, Poppins) or Mezzanine palette (electric pink, magenta, ultra violet) on these pages

### Page structure — /menu (hub)

Above the fold:
- Hero band: full-bleed background image (fallback: `role:hero-cantina`)
- Headline: **"GET A LITTLE LOST."** (Antonio Bold, white text over dark overlay)
- Subhead: "Four menus. One Uno Más." (Montserrat)

4-card grid (responsive: 2x2 on desktop, stacked on mobile):
- **Lunch** card — image: `role:hero-lunch`, headline "LUNCH", subhead "Burritos. Bowls. Tacos.", CTA → `/menu/lunch`
- **Dinner** card — image: `role:hero-dinner`, headline "DINNER", subhead "Plates that surprise people.", CTA → `/menu/dinner`
- **Brunch** card — LIVE (July 2026): headline "BRUNCH", subhead "Sundays · 10am–4pm", CTA → `/menu?tab=brunch`. *(Photos not yet shot — tab launched text-first.)*
- **Cocktails** card — image: `role:hero-cocktails`, headline "COCKTAILS", subhead "Modern margaritas. Serious tequila.", CTA → `/menu/cocktails`

Below cards:
- "Reserve a table" CTA band (Resy widget, button color `#E22690`, label "RESERVE A TABLE")
- Visit/contact strip (pulled from existing component or homepage)

### Page structure — /menu/dinner

1. **Hero band** (16:9 image, `role:hero-dinner`)
   - Kicker: "Dinner Service · 5pm – Close"
   - Headline: **"DINNER"** (Antonio Bold, white over dark gradient)
   - Subhead: "Modern Mexican. Plates that surprise people."
   - Primary CTA: "RESERVE A TABLE" → Resy (venue ID 87582, button widget OR link to https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila)

2. **Feast callout** (full-width band above the menu)
   - Headline: "THE UNO MÁS FEAST · $129"
   - Body: "A spread of signature dishes. Feeds 2–3. Carne Asada, Achiote Cilantro Shrimp, Al Pastor Chicken, cilantro lime rice, house-made black beans, salsa and tortillas."
   - CTA: "RESERVE A TABLE" → Resy

3. **Menu sections** (rendered in this order):
   - For The Table (shareables daypart, slug=`shareables`)
   - Chips & Dips (shareables daypart, slug=`chips-dips`)
   - Dinner Plates (dinner daypart, slug=`dinner-plates`)
   - Raw Bar (raw-bar daypart, slug=`dinner-raw-bar`)
   - Dinner Tacos (dinner daypart, slug=`dinner-tacos`)
   - Birria Tacos (dinner daypart, slug=`dinner-birria`)
   - Sides (sides daypart, slug=`sides`)
   - Dessert (desserts daypart, slug=`dessert`)

4. **Cross-link to cocktails**: small band at the bottom — "Pair it with a cocktail" → `/menu/cocktails`

5. **Visit/contact strip** (footer pattern from homepage)

### Page structure — /menu/lunch

1. **Hero band** (`role:hero-lunch`)
   - Kicker: "Lunch Service · 11am – 5pm · Tue–Sat"
   - Headline: **"LUNCH"**
   - Subhead: "Bowls. Burritos. Tacos. The 509."
   - Primary CTA: "RESERVE A TABLE" → Resy

2. **Menu sections** (in this order):
   - For The Table (shareables, slug=`shareables`)
   - Chips & Dips (shareables, slug=`chips-dips`)
   - Burritos (lunch, slug=`lunch-burritos`)
   - Bowls (lunch, slug=`lunch-bowls`)
   - Taco Plates (lunch, slug=`lunch-taco-plates`) — section description: "Choice of rice & beans or masa-coated waffle fries."
   - Tacos (lunch, slug=`lunch-tacos`) — section description: "Street Taco $6.50 · Big A** ¼ lb Taco $10"
   - Birria Tacos (lunch, slug=`lunch-birria`)
   - Sides (sides, slug=`sides`)
   - Dessert (desserts, slug=`dessert`)

3. **Cross-link**: "Hungrier? See the dinner menu" → `/menu/dinner`

4. **Visit/contact strip**

### Page structure — /menu/cocktails

1. **Hero band** (`role:hero-cocktails`)
   - Kicker: "Craft Cocktails · Serious Tequila"
   - Headline: **"COCKTAILS"**
   - Subhead: "Modern margaritas. Indaba Coffee collab. The cleanest tequila program in Spokane."
   - Primary CTA: "RESERVE A TABLE" → Resy

2. **Signature Cocktail callout** (above the menu)
   - Item: Espresso Margarita
   - Image: `role:hero-cocktails` (or any asset tagged `espresso-margarita`)
   - Body: "Tequila blanco + Indaba cold brew + Baileys + agave. The Indaba collab — uniquely Spokane. $15."

3. **Menu sections** (in this order):
   - Cocktails (cocktails, slug=`cocktails`)
   - Pitchers (cocktails, slug=`pitchers`)
   - Beer (beverages, slug=`beer`)
   - Non-Alcoholic (beverages, slug=`non-alcoholic`)

4. **Visit/contact strip**

### Menu item card design

For each menu_item, render a card with:
- **Name** (Antonio Bold, ~24px desktop, all caps)
- **Price** right-aligned next to name (Antonio Regular, same size — use price as `$XX` if integer, `$X.XX` if has cents)
- **Description** below (Montserrat Regular, ~16px)
- **Signature badge** if `is_signature = true` — small pink dot or "★" in `#E22690` next to name
- **Image** (if `cloudinary_id` exists OR an asset is tagged with the item's slug): thumbnail to the left of text. If no image, render text-only (don't reserve empty space — let the text fill the card width).
- **MP** for market price items (Oysters, Ceviche): render "MP" instead of dollar amount

Card layout:
- 1 column on mobile, 2 columns on tablet+, 3 columns optional on large desktop for shorter items
- Generous spacing — let the menu breathe
- No card borders or backgrounds — clean type-driven layout. Section breaks separate visually.

### Menu section header design

- Section name in Antonio Bold, all caps, ~36px
- Underline rule in pink (`#E22690`), 60–100px wide
- Section description (if any) below in Montserrat, italic, gray (~14px)

### SEO requirements per page

**`/menu` (hub):**
- `<title>` — "Menu | Uno Más Tacos & Tequila — Spokane"
- meta description — "Modern Mexican menu in Spokane. Lunch, dinner, brunch, and craft cocktails at 2020 N Monroe."
- og:image — hero from `role:hero-cantina` via Cloudinary
- JSON-LD: `Restaurant` schema with embedded `Menu` ref

**`/menu/dinner`:**
- `<title>` — "Dinner Menu — Carne Asada, Surf & Turf, The Feast | Uno Más Spokane"
- meta description — "Modern Mexican dinner in Spokane. Carne Asada $37, Surf & Turf $47, the $129 Uno Más Feast. Reserve a table."
- og:image — `role:hero-dinner`
- JSON-LD: `Menu` schema with `MenuSection` + `MenuItem` for each dinner plate. Include price.

**`/menu/lunch`:**
- `<title>` — "Lunch Menu — Tacos, Bowls, Burritos | Uno Más Spokane"
- meta description — "Lunch at Uno Más on Monroe. The 509 burrito, The Zag bowl, hand-pressed tacos. Open Tue-Sat 11am-5pm."
- og:image — `role:hero-lunch`
- JSON-LD: `Menu` schema

**`/menu/cocktails`:**
- `<title>` — "Craft Cocktails & Tequila Bar in Spokane | Uno Más"
- meta description — "Espresso Margarita with Indaba cold brew. Modern margaritas. Serious tequila. Spokane's most distinctive cocktail program."
- og:image — `role:hero-cocktails`
- JSON-LD: `Menu` schema, focus on cocktails section

### Header navigation

Replace any existing "Menu" link in the site header with a link to `/menu`. (We're using the hub page approach — easier SEO, one canonical menu URL.)

If the header already has dropdowns, the Menu item can be a single link (no dropdown). The hub page does the disambiguation.

### Brand voice for any UI microcopy

If you need to write button labels, empty states, or section intros, follow our voice:
- Confident, self-aware, group-chat energy
- Short sentences. Fragments welcome.
- Banned: "taco shop," "authentic Mexican," "mouthwatering," "mixology," "artisanal," "amazing," "vibrant"
- Use: "Modern Mexican," "house-smoked," "Get a little lost," "craft cocktails"

### Edge cases to handle

- **Item has no description**: render name + price only
- **Item has no price** (Oysters, Ceviche): render "MP"
- **No assets tagged for hero**: use `role:hero-cantina` as universal fallback
- **Section has no items** (e.g., empty cocktail sub-section): don't render the section header
- **Daypart query returns 0 results**: show a friendly "Menu temporarily unavailable. Call (509) 960-7989." (Should not happen — sanity check)

### Performance

- Lazy-load any images below the fold
- Use Cloudinary transformations for responsive sizing (`f_auto,q_auto,w_*`)
- Don't ship the full menu image set at full resolution — thumbnails for cards (400x400), heroes at 1920x1080 max

### Acceptance criteria

After this build:
- `/menu` shows 4 cards, brunch card has "Launching Soon" badge
- `/menu/dinner` shows 8 sections with real Supabase data, Resy button works, Feast callout renders above sections
- `/menu/lunch` shows 9 sections with real Supabase data
- `/menu/cocktails` shows 4 sections with real Supabase data, Espresso Margarita callout renders
- All hero images render from Supabase asset query by `role:hero-*` tag
- Mobile responsive — DevTools 375px width passes visual review
- Lighthouse Mobile Performance ≥ 80 on each page
- View source on each page → title, meta description, og:image, JSON-LD all present

