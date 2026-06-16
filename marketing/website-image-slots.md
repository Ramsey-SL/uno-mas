# Uno Más Website — Image Slots & Tag Reference

**Last updated:** 2026-05-17
**Use:** Reference for tagging photos so they auto-populate the right places on the website.
**Convention:** Each photo can have multiple tags. The website queries by tag and returns the most recent approved match. If multiple photos match a slot, the most recently approved wins.

---

## How tagging works

The website renders images via `resolveImageByTags(primaryTag, fallbackTags[])`:

1. Query 1: any asset with `primaryTag` AND `status='approved'` AND not archived
2. If 0 results → Query 2 with first fallback tag
3. Continue through fallbacks until something matches
4. If nothing matches → render placeholder background

**This means:** if you tag a photo correctly, it just shows up where it needs to. No code change.

**Tag format:** `role:[slot-name]` for website roles, lowercase, hyphens-not-underscores. Existing assets also use `category:*` and `orientation:*` prefixes — those are fine to keep.

---

## P1 — Critical for v1 launch

These slots are currently rendering placeholder (logo / generic fallback) and need real photography ASAP.

### Hero shots (full-bleed, landscape, high-resolution)

| Slot | Primary tag | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **Homepage hero** | `role:hero-cantina` | `role:venue-cantina`, `interior`, `vibe-night` | Wide cantina interior shot. Should capture the converted-garage feel — exposed beams, warm lighting, neon accents, energy of the room | 16:9 minimum, 1920px wide |
| **Dinner page + homepage dinner feature** | `role:hero-dinner` | `category:food`, `menu`, `dinner` | Wide hero-ish shot of an elevated dinner plate (Carne Asada or Surf & Turf preferred) OR a moody dinner-time table spread | 16:9, 1920px wide |
| **Mezzanine page + homepage teaser** | `role:hero-mezzanine` | `role:venue-mezzanine`, `mezzanine`, `vibe-night` | Dark, atmospheric Mezzanine shot — leather lounges, fireplace, low light, electric pink accent if possible. Should feel distinctly different from cantina | 16:9, 1920px wide |
| **About page hero** | `role:hero-about` | `role:hero-cantina`, `team` | Either a team shot in the cantina, exterior of building on Monroe, or a wide environmental shot showing all three spaces if possible | 16:9, 1920px wide |
| **Reservations page hero** | `role:hero-cantina` | (uses same hero-cantina) | Same shot can serve both — could also be a "table set, awaiting guests" shot | 16:9, 1920px wide |

### Venue cards (homepage "Three Venues" grid)

| Slot | Primary tag | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **The Cantina card** | `role:venue-cantina` | `interior`, `category:general_vibe` | Tight, energy-forward shot of the cantina floor — people, food, drinks all in one frame ideal. Should pair with the hero but be its own composition | 4:5 portrait or 1:1 square |
| **The Mezzanine card** | `role:venue-mezzanine` | `mezzanine`, `vibe-night` | Distinct Mezzanine mood shot. Different from Mezzanine hero — should show the space at a different angle/moment | 4:5 portrait or 1:1 square |
| **The Patio card** | `role:venue-patio` | `patio`, `outdoor`, `vibe-day` | Outdoor patio shot — daytime energy, the outdoor bar/kitchen visible if possible. Seasonal — sunny shots win | 4:5 portrait or 1:1 square |

### Menu item photos (for /menu/dinner and homepage dinner feature)

Tag each photo with the menu item's slug AS the tag — that's how the menu page auto-binds photos to dishes.

| Dish | Tag with slug | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **Carne Asada ($37)** | `carne-asada` | `category:food`, `dinner`, `signature`, `category:menu` | Skirt steak, charred onion, cilantro lime rice, black beans. Plated. Top-down or 3/4 angle | 1:1 square or 4:5 |
| **Surf & Turf ($47)** | `surf-turf` | `category:food`, `dinner`, `signature`, `category:menu` | Skirt steak + tiger prawns. Should look indulgent | 1:1 square or 4:5 |
| **Achiote Cilantro Shrimp ($30)** | `achiote-shrimp` | `category:food`, `dinner`, `signature`, `category:menu` | Wild prawns, citrus achiote glaze, charred lime | 1:1 square or 4:5 |
| **Al Pastor Chicken ($28)** | `al-pastor` | `category:food`, `dinner`, `category:menu` | House-marinated chicken, pineapple, cilantro, lime | 1:1 square or 4:5 |
| **Birria Tacos ($18)** | `birria-tacos` | `category:food`, `category:tacos`, `signature`, `category:menu` | Slow-braised beef tacos with consommé on the side | 1:1 square or 4:5 |
| **The Uno Más Feast ($129)** | `uno-mas-feast` | `category:food`, `dinner`, `signature`, `category:menu`, `hero` | Large family-style spread. The wow shot. Multiple plates on the table, drinks, sides | 16:9 landscape or 4:5 |

### Team photos (for /about team grid)

| Person | Primary tag | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **Ramsey Pruchnic (Owner)** | `role:team-ramsey` | `team`, `headshot` | Headshot or environmental portrait in the cantina | 1:1 square |
| **Karissa Schulke (GM / Events)** | `role:team-karissa` | `team`, `headshot` | Same style as Ramsey's. Both should match in lighting/treatment | 1:1 square |
| **Thomas Schulke (Ops)** | `role:team-thomas` | `team`, `headshot` | Same style | 1:1 square |
| **Maraya Lindo (Executive Chef)** | `role:team-maraya` | `team`, `headshot`, `chef` | Could include kitchen environment if it fits | 1:1 square |

---

## P2 — Important, can launch without

### Cocktails

| Slot | Primary tag | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **Cocktails hero (when /menu/cocktails is built)** | `role:hero-cocktails` | `category:cocktails`, `signature`, `drinks` | Wide bar shot or moody cocktail close-up. Espresso Margarita is the signature — would make a great hero | 16:9 |
| **Espresso Margarita** | `espresso-margarita` | `category:cocktails`, `signature`, `indaba` | Tight, beautifully lit shot. The Indaba collab is uniquely Spokane | 1:1 or 4:5 |

### Lunch and Brunch

| Slot | Primary tag | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **Lunch hero** | `role:hero-lunch` | `category:food`, `lunch`, `vibe-day` | Bright, daytime lunch energy. People at the bar, plates being served | 16:9 |
| **Brunch hero** | `role:hero-brunch` | `category:food`, `brunch`, `vibe-day` | When brunch launches. Sundays vibe. Mimosa or bloody mary forward | 16:9 |

### Mezzanine event cards (3-up grid on /mezzanine page)

| Slot | Primary tag | Also tag with | Description | Aspect ratio |
|---|---|---|---|---|
| **Private dinners card** | `role:mezzanine-private-dinner` | `mezzanine`, `event`, `dinner` | Intimate dinner setup in Mezzanine — small table set for 6-10 | 4:5 portrait |
| **Buyouts card** | `role:mezzanine-buyout` | `mezzanine`, `event` | Larger group, full Mezzanine floor activated | 4:5 portrait |
| **Cocktail receptions card** | `role:mezzanine-cocktails` | `mezzanine`, `event`, `cocktails` | Standing reception, people with drinks | 4:5 portrait |

### Patio detail shots (if you build out /patio later)

| Slot | Primary tag | Description |
|---|---|---|
| **Patio bar** | `role:patio-bar` | The outdoor bar setup |
| **Patio food** | `role:patio-food` | Street food coming out of the outdoor kitchen |
| **Patio crowd** | `role:patio-crowd` | People at the patio, watch party energy |

---

## P3 — Nice-to-have, future content

### Lifestyle / atmosphere (rotating use across pages)

| Slot | Primary tag | Description |
|---|---|---|
| Cocktail close-ups | `category:cocktails`, `drinks` | Multiple. The bar's craft program shots. |
| Food close-ups beyond menu items | `category:food` | Sides, sauces, prep details. |
| Service / staff in action | `team`, `service` | Behind-the-bar, in-the-kitchen, on-the-floor moments. |
| Customer / vibe shots | `customers`, `vibe-night`, `vibe-day` | Real (consented) customer moments. Builds social proof. |
| Exterior / Monroe Street | `exterior`, `monroe-street`, `building` | The building from outside. Helpful for first-time visitors finding the place. |
| Signage and details | `signage`, `branding`, `details` | Logo on the wall, menu boards, anything brand-asset visible in the wild. |

### Events documentation

| Slot | Primary tag | Description |
|---|---|---|
| Recurring events | `event-[name]`, e.g., `event-tequila-tasting` | When the events table is populated. |
| One-off / past events | `event-archive` | Documentation for portfolio/social use. |

---

## Logo variants (already covered, 21 in DB)

You have plenty of logo variants already. Tag convention reminder:

- `role:logo` — any logo
- `role:logo-pink` — pink color variant (for light backgrounds)
- `role:logo-white` — white variant (for dark backgrounds)
- `role:logo-black` — black variant
- `role:logo-navy`, `role:logo-blue`, `role:logo-gradient`, etc.

The website header should pull `role:logo-pink` by default; the Mezzanine header pulls `role:logo-white` if you want a dark-bg variant.

---

## Total photo count needed for full v1

| Tier | Count | Estimated shoot time |
|---|---|---|
| **P1 absolute minimum** (5 heroes + 3 venue cards + 6 dinner dishes + 4 team) | ~18 photos | 1 half-day shoot |
| **P1 + P2** (above + cocktail hero + 2 lunch/brunch + 3 Mezzanine event setups) | ~24 photos | 1 full-day shoot |
| **P1 + P2 + P3** (lifestyle + atmosphere + exteriors) | 40-60 photos | 1.5–2 day shoot |

---

## Workflow recommendation

### If photographing fresh

1. Shoot to the shot list above (P1 first)
2. Upload via Creative Studio Asset Browser (`/app/assets`) — handles upload + approval + tagging in one flow
3. Apply tags from this doc during upload (or after)
4. Set `status = 'approved'` so the website can read them
5. Refresh website — photos auto-populate. No code change.

### If photos are already in Cloudinary

Two-step sync:
1. Tell me the Cloudinary cloud name + folder where the photos live
2. I write a one-time script that creates `assets` table rows for each Cloudinary asset with the right tags
3. Photos go live on website

### If photos are scattered (some local, some Cloudinary, some Drive)

1. Consolidate to one upload pipeline first — recommend Creative Studio Asset Browser as the canonical location
2. Apply tags from this doc
3. Sync once

---

## Quick reference card — for printing or pinning

**Homepage immediately needs:**
- `role:hero-cantina` (1 photo, 16:9, wide cantina interior)
- `role:venue-cantina`, `role:venue-mezzanine`, `role:venue-patio` (3 photos for the venue cards)
- `role:hero-dinner` (1 dinner plate, 16:9)
- `role:hero-mezzanine` (1 Mezzanine atmosphere, 16:9)

**Dinner page immediately needs:**
- `role:hero-dinner` (same as homepage)
- `carne-asada`, `surf-turf`, `achiote-shrimp`, `al-pastor`, `birria-tacos`, `uno-mas-feast` (6 dish photos)

**About page immediately needs:**
- `role:hero-about` (or reuses hero-cantina)
- `role:team-ramsey`, `role:team-karissa`, `role:team-thomas`, `role:team-maraya` (4 team headshots)

**That's 17 critical photos.** Get those tagged and the v1 website looks real.

---

*This file lives in workspace. Update it as new sections/pages get built — add new image slots as you go.*
