# Lovable Prompt — Rebuild /fiesta-box (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-28
**Scope:** Build the `/fiesta-box` page using approved product copy from Ramsey 2026-05-28. Revenue driver — page is the entry point to Toast online ordering.

---

## PASTE BELOW THIS LINE INTO LOVABLE

Build the `/fiesta-box` page. This is the to-go meal kit page — Uno Más customers order online via Toast for pickup. Existing on Squarespace at https://www.unomastacoshop.com/fiesta-box. Real revenue driver, conversion-focused.

Use the same lighter visual treatment as the rest of the site: cream `#fafaf7` body, near-black `#1a1a1a` text, brand pink `#E22690` accents, warm-dark hero band. Antonio (or Impact fallback) Bold for headlines, Montserrat (or system sans) for body. Use **Tabler outline icons** (`<i class="ti ti-*"></i>`) — no emojis.

### Page route + metadata

- Route: `/fiesta-box`
- `<title>`: "10 Street Taco Fiesta Box — Order Online | Uno Más Spokane"
- meta description: "Our 10 Street Taco Fiesta Box. Fresh tortillas, your choice of protein, rice + beans, all the fixings. Order online for pickup at Uno Más on Monroe in Spokane."
- og:title: "10 Street Taco Fiesta Box — Uno Más"
- og:description: same as meta description
- og:image: Cloudinary URL of asset tagged `role:hero-fiesta-box` with fallback chain → `role:menu-tacos` → `category:tacos` → `role:hero-lunch`

### Toast online ordering URL (use in every CTA)

```
https://order.toasttab.com/online/uno-mas-taco-shop-2020-n-monroe-st-suite-c
```

**Every CTA opens in a new tab** (`target="_blank"` + `rel="noopener noreferrer"`).

---

### Page structure

#### 1. Hero band (warm-dark gradient on Cloudinary image)
- Background: tag-query image (see fallback chain above)
- Overlay: `linear-gradient(180deg, rgba(0,0,0,0.30), rgba(0,0,0,0.65))`
- Kicker (small caps, Pink-100 `#f4c0d1`): "To-Go · Take It Home"
- Headline (Antonio Bold, white, ~52px desktop / ~36px mobile, all caps): **"10 STREET TACO FIESTA BOX."**
- Subhead (white, ~95% opacity): "Perfect for date night, a cozy dinner, or when you just want Uno Más at home."
- Primary CTA button (pink `#E22690`, white text, all caps, letter-spaced 1.5px): "Order A Fiesta Box" → Toast URL (new tab)

#### 2. "How It Works" — cream background, 5-step process
Section header: **"HOW IT WORKS"** (Antonio Bold, all caps) with 60px-wide × 3px-tall pink rule below.

Render as a **5-column numbered process** on desktop (or stacked on mobile). Each step is:
- A circular pink badge `#E22690` with white number (1-5)
- Step text below, 13-14px, line-height 1.5

The 5 steps:

| # | Step text |
|---|---|
| 1 | Order online for pickup. *(Allow 1 hour of prep time.)* |
| 2 | We prep everything fresh. |
| 3 | Pick up at Uno Más — 2020 N Monroe Suite C *(off Knox, behind Indaba Coffee)*. |
| 4 | Heat following our easy instructions. |
| 5 | Build your tacos and enjoy. |

Below the steps, a centered CTA: "Order A Fiesta Box" → Toast URL.

#### 3. "What You Get" — white background band
Section header: **"WHAT YOU GET"** + pink rule.

Sub-header line directly under the rule: **"Taco Kit for Two — 10 Street Tacos"** (Antonio Bold ~22px, all caps).

Then a 2-column grid (1 col on mobile) of 5 items. Each item is a flex row with:
- 38px pink-tinted icon circle (`rgba(226,38,144,0.10)` background)
- Tabler outline icon centered, color `#E22690`, font-size 18px
- Title only (no subtitle this round — kept tight)

The 5 items:

| # | Icon | Title |
|---|---|---|
| 1 | `ti ti-bowl-spoon` | Fresh 4" corn tortillas |
| 2 | `ti ti-flame` | Your choice of protein |
| 3 | `ti ti-leaf` | Cilantro, onion & lime |
| 4 | `ti ti-pepper` | House salsa |
| 5 | `ti ti-soup` | Rice & beans |

#### 4. "Level Up With Add-Ons" — cream background band
Section header: **"LEVEL UP WITH ADD-ONS"** + pink rule.

3-up card grid on desktop (1-col mobile). Each card:
- White background, 0.5px border `#e8e4d8`, padding 24px, border-radius `var(--border-radius-md)`
- Large Tabler icon at top (~32px, pink `#E22690`)
- Card title in Antonio Bold, all caps, ~16-18px

The 3 add-ons:

| # | Icon | Title |
|---|---|---|
| 1 | `ti ti-glass-cocktail` | Marg To-Go |
| 2 | `ti ti-bowl` | Chip & Dip Trio |
| 3 | `ti ti-candy` | Churro 3-Pack |

Below the 3 cards, small italic note (gray `#6b6b6b`, 12px): *"Must be 21+ with valid ID for alcohol orders."*

#### 5. Bottom CTA band — dark `#1a1a1a`, white text, centered
- Padding: 60px+ vertical, 28px horizontal
- Headline (Antonio Bold, ~44px desktop / ~32px mobile, all caps): **"WE'VE GOT YOU."**
- Subhead (white at 85% opacity, ~14px, max-width ~400px): "Order online via Toast. Pickup in an hour. Tacos at home tonight."
- CTA button (pink `#E22690`): "Order A Fiesta Box" → Toast URL (new tab)

#### 6. Fine print (very small text below bottom CTA band)
Cream background, padding 20px, centered italic gray (~11px, `#6b6b6b`, max-width 600px):

*"Reheating instructions included with every order. Best enjoyed day of pickup. Must be 21+ with valid ID for alcohol add-ons."*

### Brand voice for any UI microcopy

- Confident, fragments welcome
- Banned: "amazing," "delicious," "mouthwatering," "perfect for any occasion" *(note: "perfect for date night" is OK because it's specific, not generic)*
- Use exactly the copy provided above for the steps + items + add-ons — these are approved by the operator

### Acceptance criteria

After this build:
- `/fiesta-box` route renders cleanly on desktop + mobile (375px viewport passes)
- Hero shows kicker → "10 STREET TACO FIESTA BOX." → subhead → CTA on the warm-dark gradient
- "How It Works" section shows 5 numbered steps with pink number badges, plus a mid-page CTA
- "What You Get" section shows "Taco Kit for Two — 10 Street Tacos" subheader and the 5-item grid
- "Level Up With Add-Ons" section shows 3 cards (Marg, Chip & Dip, Churro) + 21+ note
- Dark bottom CTA band reads "WE'VE GOT YOU." with the order CTA
- Fine print appears below the bottom CTA in small italic gray
- All 3+ CTAs link to the Toast URL with `target="_blank"` + `rel="noopener noreferrer"`
- `<title>`, meta description, og:image all set
- No horizontal scroll on mobile
- Numbered process steps wrap to 2 rows or stack on mobile

### Out of scope (do NOT touch)

- Any other page
- Header / nav structure
- Footer structure (use existing component)
- Any other Lovable component beyond what's needed for this single route
