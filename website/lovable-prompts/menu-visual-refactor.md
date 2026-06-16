# Lovable Prompt — Menu Visual Refactor + Bug Fixes (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Lighten the visual treatment on all four menu pages and fix three bugs in one pass.

---

## PASTE BELOW THIS LINE INTO LOVABLE

The current menu pages render too dark — the brand pink reads desaturated and the menu items feel like a nightclub poster instead of a printed menu. I want to lighten the body sections while keeping the warm/dark cantina feel on the hero bands.

Apply the following changes to **all four menu pages**: `/menu`, `/menu/dinner`, `/menu/lunch`, `/menu/cocktails`.

### 1. Visual treatment — body sections

**Background:** Switch the page background and section backgrounds from black/charcoal to a warm cream: `#fafaf7`. Card backgrounds (where used) should be pure white `#ffffff` with a 0.5px border in `#e8e4d8` (light warm gray).

**Menu text color:** Switch from muted gray to near-black:
- Item names (the dish names in the menu list): `#1a1a1a`
- Item prices: `#1a1a1a`
- Item descriptions: `#4a4a4a` (slightly muted but still high-contrast)
- Section titles ("Dinner Plates", "Cocktails", etc.): `#1a1a1a`

**Brand pink:** Restore the full Uno Más brand pink `#E22690` everywhere pink is used:
- Section underline rules (the short bar under section titles)
- Signature item star icons (★)
- "Reserve a Table" CTA button background
- Any kicker / eyebrow text above headlines
- Hover states on links

Do NOT use any of these darker / desaturated pink values currently rendering: `#6e1f47`, `#993556`, or any maroon. Always full `#E22690`.

### 2. Hero bands — keep dark, refine

Keep the existing warm-dark hero treatment, but tighten:
- Dinner hero gradient: `linear-gradient(135deg, #2a1810 0%, #5a2f1d 45%, #8b4423 100%)` overlaid on the existing hero image with a subtle `rgba(0,0,0,0.30)` to `rgba(0,0,0,0.65)` top-to-bottom gradient for text legibility. Currently the gradient feels too crushed — lighten the upper end.
- Lunch hero: warmer / lighter — `linear-gradient(135deg, #4a2c0c 0%, #8b5a2b 45%, #d4a574 100%)`. The lunch energy should feel daytime, not late-night.
- Cocktails hero: keep the dark/jewel-tone treatment — `linear-gradient(135deg, #1a0a1a 0%, #4a1d3d 50%, #762a4f 100%)`. This is the only place where the moody dark feel is exactly right.
- Hub `/menu` hero: warm-dark — `linear-gradient(135deg, #1a1a1a 0%, #3a2418 50%, #5e2e1a 100%)`.

Hero headlines stay white (`#ffffff`). Subheads stay white at 92% opacity. Kicker text (small caps above the headline) should be `#f4c0d1` (light brand pink) — currently rendering at low opacity gray.

### 3. Typography

Don't change fonts, but tighten:
- Section headlines (e.g., "Dinner Plates") should use Antonio Bold or the existing display font at ~30px desktop / 24px mobile, all caps, letter-spacing 1px
- The pink rule underneath should be 70px wide, 3px tall, `#E22690`
- Item names should be Antonio Bold or the existing display font at ~18px, all caps, letter-spacing 0.5px
- Item descriptions should be the body font (Montserrat or equivalent), 13-14px, line-height 1.5, color `#4a4a4a`
- Generous vertical spacing between items (10-12px padding + 0.5px bottom border in `#e8e4d8`)

### 4. Spacing / breathing room

The current pages feel tight. Add more whitespace:
- Section margins: 36-40px between sections (currently ~20-24px)
- Page padding: 32px desktop / 20px mobile (currently feels closer to 16px)
- Items in two columns on desktop (grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px 28px), one column on mobile

### 5. The Feast callout band (dinner page only)

On `/menu/dinner`, add a black callout band above the menu sections (between the hero and the first section). Black background, full-bleed within the content container:
- Kicker: "The Move" in `#E22690`, small caps
- Headline: "THE UNO MÁS FEAST · $129" in white, Antonio Bold ~38px
- Body: "A spread of signature dishes. Feeds 2–3. Carne Asada, Achiote Cilantro Shrimp, Al Pastor Chicken, cilantro lime rice, house-made black beans, salsa and tortillas." in white at 92% opacity
- CTA: "RESERVE A TABLE" button in `#E22690`

### 6. Espresso Margarita callout (cocktails page only)

On `/menu/cocktails`, add a featured callout between the hero and the first section. White background, 0.5px border `#e8e4d8`, padding 24px. Two-column grid (200px image + 1fr text):
- Image column: square ratio, placeholder for now (will populate from Cloudinary later — query `assets` for tag `espresso-margarita`)
- Text column:
  - Kicker: "Signature · Uniquely Spokane" in `#E22690`
  - Name: "Espresso Margarita · $15" in `#1a1a1a`, Antonio Bold ~26px
  - Description: "Tequila blanco + Indaba cold brew + Baileys + agave. The Indaba Coffee collab you can't get anywhere else."

### 7. Bug fixes (do these alongside the visual refactor)

**Bug A: "Build Your Own Taco" component renders 3 times on /menu/lunch.**
Currently appears after Taco Plates, after Tacos, AND after Birria Tacos. Remove the duplicates — leave it **once**, placed immediately below the "Tacos" section header (it's the protein-options legend for that section).

**Bug B: /menu/lunch hours footer is wrong.**
Currently says "Lunch available Tue–Fri 11am–2pm" — that's incorrect. Replace with: "Lunch service · Tue–Sat · 11am–5pm". This matches our Supabase `business_hours` data and is the canonical truth.

**Bug C: Add Resy CTA to top of /menu/dinner hero.**
Currently the only Reserve-a-Table CTA is at the bottom of the page. Add one in the hero band as well (under the subhead). Same Resy URL the rest of the site uses: `https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila`. Style it as the refactored pink `#E22690` CTA button.

### 8. /menu (hub) — refresh the 4 cards

The 4 daypart cards on the `/menu` hub page should:
- Use the existing hero images via `role:hero-{daypart}` tag lookup (already done — keep)
- Overlay: `linear-gradient(135deg, rgba(0,0,0,0.55), rgba(0,0,0,0.25))` so text stays legible without crushing the image
- Headline in white, Antonio Bold, 38px, all caps
- One-line subhead in white at 92% opacity
- "Brunch" card retains the "Launching Soon" badge in `#E22690` (top-right corner)
- Card click target = entire card (not just the headline)

### 9. Footer / contact strip

If pages have a contact strip / hours / "Find us" section, switch from dark to either:
- Cream background `#fafaf7` matching the body (cleanest), with `#1a1a1a` text, OR
- A single dark band `#1a1a1a` at the very bottom for footer chrome only, with `#b8b8b8` text and `#ffffff` for emphasis spans

Either works — pick the one that's easier given the current component structure.

### Out of scope (do NOT change)

- Site header / nav — leave as-is
- Homepage — leave as-is for now (we'll refactor in a separate pass)
- Mezzanine page — leave as-is (separate sub-brand, handled separately)
- About / Reservations pages — leave as-is
- Data layer / Supabase queries — no changes needed; just restyle the components that render the data

### Acceptance criteria

After this change:
- `/menu`, `/menu/dinner`, `/menu/lunch`, `/menu/cocktails` all have cream body backgrounds (`#fafaf7`)
- Menu item text is near-black on cream — high contrast, readable
- Brand pink renders as full `#E22690` everywhere (no maroon `#6e1f47` anywhere)
- Hero bands keep warm/dark treatment with refined gradients per page
- `/menu/lunch` has exactly ONE "Build Your Own Taco" component
- `/menu/lunch` footer reads "Lunch service · Tue–Sat · 11am–5pm"
- `/menu/dinner` has Reserve CTAs in both the hero AND the bottom
- `/menu/dinner` has a black Feast callout band between hero and sections
- `/menu/cocktails` has an Espresso Margarita callout between hero and sections
- Mobile responsive — DevTools 375px width still looks great
- No layout collapse on tablet (768-1024px) — items go to single column gracefully

---

If anything is ambiguous, default to the lighter / cleaner / more-pink option. The vibe we're going for: printed menu at a great modern restaurant, not a nightclub poster.
