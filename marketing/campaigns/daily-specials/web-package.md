# Web Design Package — Daily Specials (Tue / Wed / Thu)

**Placement:** standalone page `/specials` + homepage banner (rotates the day's special) + a callout on `/menu`.
**Brand:** Uno Más warm — Hot Pink `#E22690`, Navy `#003366`, Yellow `#FFEC00`, Blue `#18BCDC`; Antonio headlines / Montserrat body.
**CTA:** Directions · Reserve (Resy) · See Menu. *(Open: time windows + dine-in/takeout — see brief.)*

## The offers
| Day | Special |
|---|---|
| **Taco Tuesday** | BOGO Lunch Street Tacos · $6 Margs · $30 Marg Pitchers |
| **$5 Wednesday** | $5 Pints · $5 Street Tacos |
| **Burrito Thursday** | $15 House Burrito or Bowl |

## Page wireframe (top → bottom)
1. **Hero** — "THREE REASONS TO GET A LITTLE LOST MIDWEEK." Warm food/marg image, pink accent.
   - Img: `https://res.cloudinary.com/drxrfyq9i/image/upload/v1782019435/20260207_UM_DRINK_PitcherAndMarg_FINAL.jpg`
2. **Three special cards** (one per day) — big day label, the offer, a hero photo:
   - **Taco Tuesday** — "BOGO street tacos. $6 margs. $30 marg pitchers." → imgs `…/v1782019842/20260125_UM_FOOD_TacoCloseUpV10_FINAL.jpg` + `…/v1782019423/20260207_UM_DRINK_MargWithLime_FINAL.jpg`
   - **$5 Wednesday** — "$5 pints. $5 street tacos. Math we can get behind." → `…/v1782019842/20260125_UM_FOOD_TacoCloseUpV10_FINAL.jpg` *(pull a pint/beer shot — see gap)*
   - **Burrito Thursday** — "$15 House Burrito or Bowl. Your Thursday just got a plan." → `…/v1781926386/uno-mas/photos/food/20260619_UM_FOOD_BurritoBeanRiceCloseup.png`
3. **Hours strip** — Specials run Tue / Wed / Thu (+ time windows once confirmed).
4. **CTA band** — "Midweek just got better." → Reserve / Directions / See Menu.

## Homepage banner (rotates by day)
Pink banner: "[TODAY]: [offer]" e.g. "TACO TUESDAY · BOGO street tacos, $6 margs" → links to `/specials`.

## Lovable build prompt (paste into the project)
```
Add a standalone page at /specials for our weekly day-of specials, plus a homepage banner that shows
the current day's special and links to it. Use the UNO MÁS warm brand: Hot Pink #E22690, Navy #003366,
Yellow #FFEC00; Antonio headlines, Montserrat body. Sections:

1) Hero: headline "THREE REASONS TO GET A LITTLE LOST MIDWEEK", warm background image
   https://res.cloudinary.com/drxrfyq9i/image/upload/v1782019435/20260207_UM_DRINK_PitcherAndMarg_FINAL.jpg
2) Three large special cards (Tue/Wed/Thu), each with the day, the offer, and a photo:
   • TACO TUESDAY — "BOGO Lunch Street Tacos · $6 Margs · $30 Marg Pitchers"
     imgs: …/v1782019842/20260125_UM_FOOD_TacoCloseUpV10_FINAL.jpg and …/v1782019423/20260207_UM_DRINK_MargWithLime_FINAL.jpg
   • $5 WEDNESDAY — "$5 Pints · $5 Street Tacos"
     img: …/v1782019842/20260125_UM_FOOD_TacoCloseUpV10_FINAL.jpg
   • BURRITO THURSDAY — "$15 House Burrito or Bowl"
     img: https://res.cloudinary.com/drxrfyq9i/image/upload/v1781926386/uno-mas/photos/food/20260619_UM_FOOD_BurritoBeanRiceCloseup.png
3) Hours strip: "Specials run Tue / Wed / Thu."
4) Closing CTA band "Midweek just got better." with buttons Reserve (Resy), Get Directions, See Menu.
Mobile-first, scroll-reveal. Homepage: add a pink banner that displays today's special and links to /specials.
SEO title "Weekly Specials — Taco Tuesday, $5 Wednesday, Burrito Thursday | Uno Más Spokane".
Spell "Uno Más" with the accent.
```

## To finalize
- **Time windows** per day + dine-in/takeout (brief §9).
- **Pint/beer photo** — no strong beer shot in the DAM yet; add one for the $5 Wednesday card (shoot-list item).
- Reserve link (shared with other campaigns).
