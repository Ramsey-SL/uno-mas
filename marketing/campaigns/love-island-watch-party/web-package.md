# Web Design Package — Love Island Watch Party

**Placement:** standalone page `/events/love-island` + homepage event callout that links to it.
**Brand:** The Mezzanine (electric pink `#E22790` / black `#000` / ultra-violet `#93009B` / off-white `#F5F5F5`).
**Fonts:** Anton/Bebas/DIN-condensed headlines · Poppins body. **CTA:** Reserve → `https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila` (Resy — standard venue reservations).

## Page wireframe (top → bottom)
1. **Hero** — full-bleed Mezzanine watch-party photo, dark gradient scrim, pink accent.
   - Eyebrow: THE MEZZANINE AT UNO MÁS
   - H1: LOVE ISLAND WATCH PARTY
   - Sub: All tacos. All tequila. All drama.
   - Primary button: **Reserve Your Spot** → https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila · secondary: See Dates
   - Hero img: `https://res.cloudinary.com/drxrfyq9i/image/upload/v1781646674/20251028_MEZZ_VENUE_MezzWatchParty_v5.jpg`
2. **Dates & times band** (pink) — EVERY THURSDAY · Jun 25 · Jul 2 · Jul 9 · Doors 5PM / Show 6PM · Reservations recommended · ❤ Season Finale: Sun Jul 12.
3. **"It's a night out, not just a watch party"** — 3 cards: 🍸 Signature Cocktails · 🌮 Tacos & Shareables · 💗 Bring Your Villa Crew. Body: "Cocktails, a little friendly competition, and your people — Spokane's Love Island HQ is upstairs."
   - Img: `…/v1781646685/20251028_MEZZ_VENUE_MezzBar_v2.jpg` (bar) + `…/v1781646594/20251028_MEZZ_VENUE_MezzTV_RAW.jpg` (big screen)
4. **The room** — gallery strip of the Mezzanine: `MezzLounge_RAW`, `MezzSeatingAndBar_RAW`, `MezzWatchParty_v4`.
5. **Reserve CTA band** — "Grab your villa crew." → Reserve button (`https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila`). 21+. Mezzanine.
6. **FAQ (optional):** 21+, walk-ins vs reservations, finale note.

## Homepage section (BUILT — `homepage-section.html`)
Drop-in homepage block in the neon-graphic style (pink LOVE ISLAND + teal *Watch Party* script, info chips, **Reserve on Resy** + **See Details →** to `/events/love-island`). Responsive; preview in `homepage-section.html`.

## Homepage callout (links to the page)
Card: pink, "LOVE ISLAND — Thursdays upstairs" · "All tacos. All tequila. All drama." · button "See Dates →" → `/events/love-island`.

## Lovable build prompt (paste into the project)
```
Add a new standalone page at /events/love-island for our recurring "Love Island Watch Party" at
The Mezzanine. Use the MEZZANINE brand identity: electric pink #E22790, black, ultra-violet #93009B
accents, off-white text; condensed bold headline font (Anton/Bebas), Poppins body. Sections:

1) Full-bleed hero with this background image:
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1781646674/20251028_MEZZ_VENUE_MezzWatchParty_v5.jpg
   dark gradient scrim; eyebrow "THE MEZZANINE AT UNO MÁS"; H1 "LOVE ISLAND WATCH PARTY";
   subhead "All tacos. All tequila. All drama."; primary pink button "Reserve Your Spot" (link https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila);
   secondary ghost button "See Dates".
2) Pink dates band: "EVERY THURSDAY · JUNE 25 · JULY 2 · JULY 9 · DOORS 5PM / SHOW 6PM ·
   RESERVATIONS RECOMMENDED" and a highlighted "SEASON FINALE — SUNDAY, JULY 12".
3) Three feature cards with icons: Signature Cocktails / Tacos & Shareables / Bring Your Villa Crew,
   with intro copy "It's not just watching — it's a night out." Use images:
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1781646685/20251028_MEZZ_VENUE_MezzBar_v2.jpg
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1781646594/20251028_MEZZ_VENUE_MezzTV_RAW.jpg
4) A photo gallery strip of The Mezzanine using:
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1781646691/20251028_MEZZ_VENUE_MezzLounge_RAW.jpg
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1781630844/20251028_MEZZ_VENUE_MezzSeatingAndBar_RAW.jpg
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1781646650/20251028_MEZZ_VENUE_MezzWatchParty_v4.jpg
5) Closing reserve band: headline "Grab your villa crew." + pink "Reserve" button (link https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila); note 21+.
Mobile-first, scroll-reveal, fast. Add a homepage event callout card (pink) linking to /events/love-island.
SEO: title "Love Island Watch Party — The Mezzanine at Uno Más | Spokane"; meta about Thursdays, cocktails,
21+, reservations. Keep "Uno Más" spelled with the accent everywhere.
```

## To finalize
- ✅ Reservations = **Resy** (https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila) — wires every button (same as all Uno Más reservations).
- Confirm Mezzanine indoor vs rooftop framing for the imagery (use real DAM shots either way).
