# Lovable Prompt — /mezzanine Sub-brand Page (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Flesh out /mezzanine page as a distinct SUB-BRAND. Dark visual treatment IS correct here (it's the speakeasy — moody is the point). Different fonts, different palette, different voice register from the rest of the site.

---

## PASTE BELOW THIS LINE INTO LOVABLE

The Mezzanine is Uno Más's upstairs speakeasy + private event venue. It's a distinct **sub-brand** — different fonts, different colors, different voice. The dark visual treatment IS correct here, in contrast to the cream-base menu pages. Moody is the point.

The current /mezzanine page has a hero and 3 stat callouts but needs to be fleshed out. Build out the rest while preserving the sub-brand visual rules below.

### Visual rules (do NOT cross-contaminate with Uno Más main brand)

**Palette:**
- Primary background: Deep Black `#000000`
- Card / section backgrounds: Charcoal `#333333`
- Primary accent: Electric Pink `#E22790` *(note: this is a SLIGHTLY different pink than Uno Más main brand `#E22690` — keep the distinction)*
- Secondary accent: Magenta `#BF28BF`
- Deep accent: Ultra Violet `#93009B`
- Text on dark: White `#FFFFFF` for body, white at 65-80% opacity for secondary text
- Gradient for moody backgrounds: `linear-gradient(135deg, #000000 0%, #1a1a1a 40%, #4a1d4a 80%, #762a4f 100%)`

**Typography:**
- Headlines / display: DIN Condensed VF (Demi Bold, Regular). If not loaded in the project, load it via Google Fonts CDN: `Oswald` is an acceptable web-safe fallback. All caps. Tight letter-spacing (~1-2px).
- Body: Poppins (Regular, Medium for emphasis). If not loaded, system sans-serif fallback.
- Accent callouts: Baka Too (if loaded), otherwise the same DIN Condensed at smaller size.

**Voice register (different from Uno Más):**
- Cool, minimal, atmosphere-forward. 0-1 emojis max.
- Lead with the room, not the food.
- Examples of correct voice:
  - "Upstairs, it gets quieter. Better."
  - "Private. Moody. The kind of room where whatever you're celebrating actually feels celebrated."
  - "An unforgettable evening — with tacos and tequila."
- Banned: anything chatty, casual, group-chat-energy. That's Uno Más main brand voice — different room.

### Page structure

#### Hero band (keep / refine existing)
- Full-bleed image: `role:hero-mezzanine` (we already have 1 photo tagged correctly)
- Overlay: deep gradient — `linear-gradient(180deg, rgba(0,0,0,0.2), rgba(0,0,0,0.8))` so headlines are crisp
- Mezzanine wordmark / logo at top (use any asset tagged `role:logo-white` or `role:logo` with mezzanine variant — fallback to "THE MEZZANINE" text in DIN Condensed)
- Headline (DIN Condensed, ~70px desktop / 48px mobile, all caps, white):
  **"UPSTAIRS, IT GETS QUIETER. BETTER."**
- Subhead (Poppins Light, ~16px, white at 85% opacity):
  "A speakeasy and private event space above Uno Más."
- Primary CTA: "INQUIRE" button — Electric Pink `#E22790` background, white text, DIN Condensed letter-spaced 2px — links to mailto:karissa@unomastacoshop.com?subject=Mezzanine Inquiry

#### Section 1 — The Room (keep existing 3-stat callout, refine)
3-column stat band on dark/charcoal background. Each stat:
- Number / value in DIN Condensed, large (~60px), Electric Pink
- Label below in Poppins, white at 80% opacity, small caps
- Stats:
  - **35-40 seated · 65-75 standing** — Capacity
  - **Private entrance** — Discreet access from the alley
  - **Thu–Sat 7pm – late** — When the room comes alive (or "By appointment for private events")

#### Section 2 — Three ways to use the room (3-up event-type grid)
Each card has a moody image, title, and 1-2 line description. Card background: `#333333` with subtle border `rgba(255,255,255,0.08)`.

**Card 1 — Private Dinners**
- Image: `role:mezzanine-private-dinner` (fallback: `role:venue-mezzanine`)
- Title: "PRIVATE DINNERS"
- Body: "35-40 seated. Custom menus, full bar, dedicated server. Rehearsals, milestones, intimate corporate."

**Card 2 — Cocktail Receptions**
- Image: `role:mezzanine-cocktails` (fallback: `role:venue-mezzanine`)
- Title: "COCKTAIL RECEPTIONS"
- Body: "Up to 75 standing. Open bar, light bites, and an upstairs that doesn't feel like a banquet hall."

**Card 3 — Buyouts**
- Image: `role:mezzanine-buyout` (fallback: `role:venue-mezzanine`)
- Title: "FULL BUYOUTS"
- Body: "Take the whole floor. Mezzanine + downstairs combo available for larger events. We'll build it around you."

#### Section 3 — What you get
4-up icon row (use Tabler outline icons in Electric Pink):
- ti-music — Curated playlist / live DJ option
- ti-glass-cocktail — Full craft bar + bartender
- ti-flame — Fireplace + leather lounges
- ti-user-check — Dedicated event lead

Below the icons, a short paragraph in Poppins:
"Sound system. Lighting controls. A fireplace that's actually lit. Leather lounges. A private bar. A team that handles everything so you can just show up and be a guest at your own night."

#### Section 4 — Brand quote moment
Full-width band with a single quote treatment. Center-aligned, generous padding, dark gradient background.

Quote (DIN Condensed, large, Electric Pink):
**"What happens when a speakeasy and a rooftop bar decide to share a space."**

#### Section 5 — Inquire / contact band
Dark band at the bottom. Two-column on desktop:

Left column:
- Headline: "PLAN YOUR EVENING."
- Body: "Karissa runs Mezzanine events. The fastest way to lock something in is to email her with your date and guest count."
- CTA: "EMAIL KARISSA" — Electric Pink button → mailto:karissa@unomastacoshop.com

Right column:
- Address: 2020 N Monroe St, Suite C · Spokane, WA 99205
- Phone: (509) 960-7989
- Hours: "Open to the public Thu-Sat 7pm-late · Private events any night"

### Cross-link back to main brand
Small link at the very bottom, low-key:
"Looking for the dinner menu? → unomastacoshop.com/menu/dinner"

### SEO
- `<title>`: "The Mezzanine — Spokane's Speakeasy & Private Event Venue"
- meta description: "Upstairs at Uno Más on Monroe. Speakeasy. Private events. Capacity 20-60. Leather lounges, a fireplace, a private bar. Spokane's most distinctive event space."
- og:image: `role:hero-mezzanine` Cloudinary URL
- JSON-LD: Place schema (since it's a venue, not just a restaurant page) with parent organization = Uno Más

### Don't touch
- Header / nav — leave as-is
- Footer chrome — can stay the standard Uno Más footer for cross-site consistency, OR if it's already a custom Mezzanine-styled footer, keep that. Don't replace.
- Other pages — this prompt is /mezzanine only

### Acceptance criteria

After this build:
- `/mezzanine` background is solid black `#000000` or near-black gradients — NOT cream
- All headlines use DIN Condensed (or Oswald fallback) — NOT Antonio
- All body uses Poppins (or system fallback) — NOT Montserrat
- All accents use Electric Pink `#E22790` — NOT Uno Más Pink `#E22690`
- Page reads moody / atmospheric / cool — NOT chatty / casual
- Sections render: hero, 3-stat callout, 3-up event types, what-you-get icons, brand quote moment, inquire band, cross-link
- Mobile responsive — DevTools 375px width passes visual review
- "INQUIRE" CTA in hero links to karissa@unomastacoshop.com with subject pre-filled

If anything is ambiguous, default to the more atmospheric / less-busy option. The vibe: high-end speakeasy in a city you visit once a year. Not nightclub. Not lounge bar. The room you found behind the bookshelf.
