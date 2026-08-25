# Uno Más — Master Brand & Operations Reference

> **Entry point is `/CLAUDE.md` at the repo root.** This is the operational cheat sheet it points
> to — facts, configs, voice rules. Read CLAUDE.md first for orientation and repo structure.

**Owner:** Ramsey Pruchnic
**Last updated:** 2026-08-04
**Purpose:** Single source of truth for the brand. House info, menu, social, technical stack, SEO, voice. Reference this file in any new Claude session, brief, or vendor handoff — it's the canonical doc.

**How this file relates to others:**
- This file = **the cheat sheet**. Quick reference for facts, configs, voice rules.
- `uno-mas-website-backlog.md` = active project todos, INBOX, what's in flight.
- `brand-intelligence-center/*.md` (in `uno-mas` GitHub repo) = deep brand intelligence (customer psychology, financials, full competitor analysis). Feed those to Claude when doing campaign strategy / creative direction.
- Supabase `brand_guidelines` table = same content as `brand-intelligence-center/` but chunked ≤2000 chars for AI retrieval inside the Creative Studio app.

---

## QUICK REFERENCE — the one-screen cheat sheet

| Field | Value |
|---|---|
| **Brand** | Uno Más Tacos & Tequila |
| **Tagline** | Get a little lost. |
| **Address** | 2020 N Monroe St, Suite C, Spokane, WA 99205 |
| **Lat / Long** | 47.6764702, -117.4263699 *(for schema markup `geo` field)* |
| **Locator detail** | Behind Indaba Coffee, corner of Knox Ave & N Monroe (between W Knox Ave & W Shannon Ave) |
| **Phone** | (509) 960-7989 |
| **General email** | tacos@unomastacoshop.com |
| **Events / catering email** | karissa@unomastacoshop.com |
| **Website** | unomastacoshop.com |
| **Resy** | [Book here](https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila) · Venue ID `87582` · Public widget key `g47nf19Sg6grqO50HcS2HDIUIO8PjEGM` |
| **Instagram** | [@unomastacoshop](https://www.instagram.com/unomastacoshop) — primary |
| **TikTok** | [@unomastacosandtequila](https://www.tiktok.com/@unomastacosandtequila) |
| **Facebook** | Uno Más Tacos & Tequila |
| **POS** | Toast |
| **Loyalty** | Uno Mas Rewards: The Cantina Club (via Toast → Klaviyo segments) |
| **Email/SMS** | Klaviyo |
| **Reservations** | Resy (dinner + brunch); walk-ins always welcome |
| **Delivery** | Dine-in + takeout only. No DoorDash / Uber Eats. |
| **Family policy** | Kid-friendly at all times. **No 21+ window.** Event-specific 21+ (Mezzanine watch parties) and alcohol purchase 21+ still apply. |
| **Founded** | 2022 |
| **Ownership** | Ramsey Pruchnic, 100% |

---

## IDENTITY & CONCEPT

**One sentence (long-form / press):** Uno Más is a modern Mexican restaurant and tequila bar in Spokane where the food is serious, the atmosphere is alive, and the only thing we take lightly is ourselves.

**One sentence (social / discovery):** Inside. Feels like outside. Feels like somewhere else. Modern Mexican and tequila bar at 2020 N Monroe.

**One sentence (occasion / dinner):** The kind of dinner you'll still be talking about Sunday. Modern Mexican, craft cocktails, a speakeasy upstairs. Get a little lost.

**One sentence (short-form / ad):** Modern Mexican. Craft cocktails. A speakeasy upstairs. The food is serious. The vibe is not. Get a little lost.

**Mission:** To be the place Spokane comes back to — not because it's the obvious choice, but because it's the one they found themselves.

**Concept summary:** We started as a taco shop. We grew into something more. Three venues at one address: The Cantina (ground floor, converted garage), The Mezzanine (upstairs speakeasy + private events), The Patio (outdoor bar + street-food kitchen). Full lunch + dinner program, craft cocktails, serious tequila program, Uno Más Feast ($129 family-style), house-smoked meats, Espresso Margarita collab with Indaba Coffee.

---

## THE THREE VENUES

### The Cantina
- Ground floor, converted mechanic's garage at 2020 N Monroe.
- Full lunch + dinner + craft cocktails + full bar.
- Inside feels like outside — courtyard-off-a-side-street-in-Mexico energy. Raw textures, warm lighting, neon accents.
- Kid-friendly at all times. No 21+ restriction.

### The Mezzanine *(sub-brand: "The Mezzanine on Monroe")*

**Sub-brand name locked 2026-05-28:** Use **"The Mezzanine on Monroe"** as the formal/marketing name. Use **"The Mezzanine"** as short reference. Never use just "Mezzanine" without an article.

- Upstairs speakeasy + private event venue.
- Leather lounges. Fireplace. Full bar. Moody, atmospheric, private.
- Buyouts: intimate dinners (35-40 seated) → cocktail receptions (65-75 standing).
- Events contact: karissa@unomastacoshop.com.
- Sub-brand has its own visual identity — see Visual Identity section below.

### The Patio
- Outdoor bar + street-food-style outdoor kitchen.
- Casual dining, watch parties, patio season programming, large groups.
- Same address — third distinct experience.

---

## TEAM

| Name | Role | Email |
|---|---|---|
| Ramsey Pruchnic | Owner (100%) | ramsey@strategylabs.us |
| Karissa Schulke | GM / Events | karissa@unomastacoshop.com |
| Thomas Schulke | Operations Manager | [TODO: email] |
| Maraya Lindo | Executive Chef | [TODO: email] |

---

## HOURS

*Source: Supabase `business_hours` table. Update there for live website.*

*Source of truth: Supabase `business_hours` table, synced with the live Squarespace site and Google Business Profile listing as of 2026-05-25.*

### Cantina

| Day | Hours |
|---|---|
| Sunday | **10am – 4pm** *(Sunday Brunch + lunch — launched July 2026)* |
| Monday | **CLOSED** |
| Tuesday | 11am – 9pm |
| Wednesday | 11am – 9pm |
| Thursday | 11am – 9pm |
| Friday | 11am – 10pm |
| Saturday | 11am – 10pm |

**Service blocks:** Lunch 11am–5pm (Tue–Sat) · Dinner 5pm–close (Tue–Sat) · Sunday Brunch + lunch 10am–4pm

### Brunch
LIVE — every Sunday 10am–4pm (launched July 2026). Full fresh sheet in `website/content-studio/menus/brunch-menu.md`; live on the site at `/menu?tab=brunch`.

### The Mezzanine
By appointment / private event bookings only. Contact karissa@unomastacoshop.com.

---

## MENU

*Source of truth: PDFs `UM Menu Lunch & Cocktails — July 2026.pdf` (lunch/cocktails) + `Uno Mas Dinner Menu — July 2026.pdf` (dinner) + Sunday Brunch menu (July 2026). Supabase `menu_sections` + `menu_items` tables should mirror these. POS-side menu lives in Toast.*

*Last reconciled: 2026-08-04 — Supabase synced ✅ against the July 2026 printed menus. Price updates + Oysters removal + Brunch second-page expansion applied.*

> ⚠️ **Print-menu inconsistency (flagged 2026-08-04, still open):** The Lunch & Cocktails PDF prices Chip & Dip Trio at $16; the Dinner PDF prices the identical item at $15. Ramsey has directed we use **$16** everywhere on the website/DB as the interim fix, but the two printed menus disagree and should be reconciled with the printer/menu designer.

### Shareables / For The Table *(available all day)*

| Item | Price | Description |
|---|---|---|
| **Starter Trio** | $45 | Chip & Dip Trio, Lula Wings, and Loaded Masa Fries. Start here. End happy. |
| **Lula Wings** | $18 | 1 lb of wings tossed in housemade Lula sauce, topped with lime zest, cotija cheese & fresh cilantro. Crunchy, bright, & hitting every flavor note. |
| Masa Coated Fries | $8 | Crispy masa-coated fries. Choice of dip: Chipotle Crema, Jalapeño Ranch, or Ketchup (if you must). |
| Loaded Masa Coated Fries | $15 | Loaded with queso blanco, black beans, guacamole, salsa, sour cream & fresh cilantro. *Add: Skirt Steak $9 / Carnitas $7 / Grilled Chicken $6* |
| The Big F*** Quesadilla (BFQ) | $15 | Size of a medium pizza. Loaded with melted cheese — it's exactly what it sounds like. *Add: Skirt Steak $9 / Carnitas $7 / Grilled Chicken $6* |

### Chips & Dips *(available all day)*

| Item | Price | Description |
|---|---|---|
| Chips & Salsa | $4 | |
| Chips & Guacamole | $6 | |
| Chips & Queso Blanco | $8 | |
| **Chip & Dip Trio** | $16 | Salsa, guacamole & queso blanco — three dips, one massive pile of chips. The move for the table. *(See print-menu inconsistency note above.)* |
| Nachos | $15 | Loaded with queso blanco, black beans, guacamole, salsa, sour cream & fresh cilantro. *Add: Skirt Steak $9 / Carnitas $7 / Grilled Chicken $6* |

### Dinner Plates *(elevated dinner program — served with cilantro lime rice + house-made black beans)*

| Item | Price | Description | Slug |
|---|---|---|---|
| **Carne Asada** ⭐ | $39 | Skirt steak, grilled hot and fast. Salsa roja, fresh pico, charred onion & jalapeño. Corn tortillas. The one people come back for. | `carne-asada` |
| **Surf & Turf** ⭐ | $49 | Grilled skirt steak meets achiote cilantro tiger prawns. Everything included. Nothing held back. This is the move. | `surf-turf` |
| **Achiote Cilantro Shrimp** ⭐ | $30 | Tiger prawns in achiote, cilantro & lime — bright, a little smoky, deeply good. Cabbage slaw, pineapple salsa, corn tortillas. | `achiote-shrimp` |
| Al Pastor Chicken | **$24** | Marinated chicken thighs and pineapple, skewered and grilled over open flame. Salsa verde, corn tortillas. Old school technique. Serious results. | `al-pastor` |
| **Birria Tacos** (dinner) ⭐ | $18.50 | Two braised chuck tacos on corn tortillas with melted Monterey Jack, served alongside rich consommé for dipping. Order these first. Thank us later. | `birria-tacos-dinner` |

### Raw Bar

| Item | Price | Description |
|---|---|---|
| ~~Oysters~~ | — | **Removed from the menu (July 2026).** *(Tostilocos also confirmed removed this round — see `brand-guidelines/09-menu-product-context.md`; it was already absent from the current printed menus/Supabase, so no DB change was needed.)* |
| Ceviche | MP | Fresh, bold, and bright. Ask your server for today's preparation. |

### The Feast

| Item | Price | Description | Slug |
|---|---|---|---|
| **The Uno Más Feast** ⭐ | $129 | A spread of signature dishes. Feeds 2–3. Includes: Carne Asada, Achiote Cilantro Shrimp, Al Pastor Chicken, cilantro lime rice, house-made black beans, salsa and tortillas. | `uno-mas-feast` |

### Dinner Tacos *(separate from Dinner Plates)*

| Item | Price | Description |
|---|---|---|
| **Street Tacos** (3 per order) | $18.50 | Mix & match proteins. Corn tortillas, cilantro, onion & salsa. Options: Carnitas, Barbacoa, Hongos (vegan), Batata (vegetarian/can be vegan). |
| **Chef's Pick** (2 tacos) | $15 | Changes weekly. Always worth ordering. |

### Lunch — Burritos

| Item | Price | Description |
|---|---|---|
| **The 509** ⭐ | $23 | Marinated skirt steak + fries + Monterey Jack cheese + salsa verde + pico de gallo + cilantro + guacamole + crema. |
| Thicc Chic | $17 | Al pastor chicken + rice + beans + Monterey Jack cheese + cilantro + pickled red onion + aguacate + guacamole. |
| The Notorious P.I.G | $18 | House smoked pork + rice + beans + Monterey Jack cheese + pickled red onion + cilantro + salsa verde + guacamole. |

### Lunch — Bowls

| Item | Price | Description |
|---|---|---|
| **The Zag** | $20 | Marinated steak + rice + beans + salsa roja + white onion + cilantro + cotija cheese. |
| Monroe | $17 | Grilled shrimp + rice + beans + tajín slaw + pineapple salsa + chipotle mayo. |
| El Camino | $16 | Al pastor chicken + rice + beans + pineapple + salsa verde + cilantro. |
| Batata Bowl | $13 | Grilled sweet potato + rice + beans + pickled red onion + salsa aguacate + cilantro. |

### Lunch — Taco Plates *(comes with choice of rice & beans OR masa-coated waffle fries)*

| Item | Price |
|---|---|
| 2 Street Tacos + side | $16.50 |
| 2 Big A** ¼ lb Tacos + side | $23 |

### Lunch — Individual Tacos

**Street Taco $6.50 · Big A** ¼ lb Taco $10**

| Taco | Composition |
|---|---|
| **Carne Asada** | Marinated steak + salsa roja + white onion + cilantro + queso fresco |
| **Al Pastor Chicken** | Grilled chicken + pineapple + salsa verde + cilantro |
| **Carnitas** | House smoked pork + melted Monterey Jack cheese + pickled onion + cilantro + salsa verde |
| **Barbacoa** | Braised chuck + salsa verde + cilantro + pickled red onion |
| **Camaron** | Grilled shrimp + tajín slaw + pineapple salsa + chipotle mayo |
| **Batata** *(can be vegan)* | Grilled sweet potato + melted Monterey Jack cheese + pickled onion + cilantro + salsa aguacate |
| **Hongos** *(can be vegan)* | Chile roasted portabella + melted Monterey Jack cheese + spicy roja + cilantro + pickled daikon & tomatillo + shaved radish |

*Add guacamole or crema +$1.50 · Additional sauces $1.50*

### Lunch — Birria Tacos *(standalone callout — NOT included with taco plates)*

| Item | Price | Description | Slug |
|---|---|---|---|
| **Birria Tacos** (lunch) ⭐ | $14 | Braised chuck + melted Monterey Jack cheese + cilantro + white onion + consommé. | `birria-tacos-lunch` |

> ⚠️ **Birria pricing note:** $14 on lunch menu, $18.50 on dinner menu (gap widened with the July 2026 dinner price update). Confirm intent — same item or different portion?

### Sides *(available all day)*

| Item | Price |
|---|---|
| Cilantro Lime Rice | $6 |
| Black Beans | $7 |
| Street Corn | $9 |
| Escabeche | $3 |

### Dessert

| Item | Price | Description |
|---|---|---|
| Churros | $7 | Three churros dusted in cinnamon sugar, served with house whipped cream, fresh strawberries, and chocolate dipping sauce. |

### Cocktails

| Cocktail | Price | Description | Slug |
|---|---|---|---|
| House Margarita | $12.50 | Tequila blanco + agave + Meyer lemon juice + salt rim + lemon wheel garnish. *Spicy available. Sub mezcal / Cadillac +$2* | `house-margarita` |
| **Espresso Margarita** ⭐ | $15.50 | Tequila blanco + Indaba cold brew + Baileys + agave. *(Indaba Coffee collab — uniquely Spokane)* | `espresso-margarita` |
| Frozen Margarita | $11 | Rotating flavors. Ask your server. | `frozen-margarita` |
| Paloma | $14.50 | Tequila + grapefruit juice + lime juice + agave + grapefruit soda water + garnish grapefruit wedge. | `paloma` |
| Tepache Bevvy | $12.50 | Choice of tequila / mezcal / rum + lemon juice + tepache. | `tepache-bevvy` |
| Latin Candy Shot | $8.50 | Tequila + lime juice + agave + pineapple juice + watermelon pucker + serranos. | `latin-candy-shot` |
| POM 75 | $14.50 | Gin + lemon juice + agave + pomegranate liqueur + champagne. | `pom-75` |
| Jamica Spritz | $14 | Tequila + jamica syrup + lime juice + St. Germain + agave. Top with champagne. | `jamica-spritz` |
| Dirty Horchata | $12.50 | Rum + house-made horchata. | `dirty-horchata` |

### Pitchers

| Item | Price |
|---|---|
| House Margarita Pitcher | $50 |
| Beer Pitcher | $25 |

### Beer

| Item | Price |
|---|---|
| Michelada (housemade mix + choice of beer + chamoy + tajín rim + lime wedge) | $8 |
| Cheleda (salted rim + lime juice + choice of beer) | $7 |
| Bucket of Bud Light / Michelob Ultra / Coors Light | $15 |
| Bucket of Modelo / Pacifico / Corona / Modelo Negra | $25 |
| Draft 16oz | $7 |
| Draft 20oz | $8 |
| Domestic | $5 |
| Imports | $6 |
| N/A Beer | $6 |

### Non-Alcoholic

| Item | Price |
|---|---|
| Agua Frescas *(ask about flavors)* | $5 |
| House-made Tepache | $6 |
| Red Bull | $3 |
| Soda | $2 |
| Jarritos | $3 |
| Bottled Soda | $3 |
| N/A Beer | $6 |
| Mocktails available | — |

### Flights

Tequila flights available — ask your server.

### Brunch *(Sundays 10am–4pm — LIVE, launched July 2026)*

*Two-sided print menu (July 2026). Front = Breakfast + Brunch Drinks. Back = Apps + Street Tacos + House Favorites (added to the live site's Brunch tab 2026-08-04). Full doc: `website/content-studio/menus/brunch-menu.md`. Live at `/menu?tab=brunch`.*

**Breakfast:** Steak & Eggs $32 (**new item**) · Breakfast Burrito $14 + protein · Chilaquiles $14 · Breakfast Potato Hash $15 + protein · Hair of the Hog $14 · Horchata French Toast $14. Protein add-ons (Burrito & Potato Hash): Carne Asada +$9, Carnitas +$7, Chorizo +$5, Bacon +$3.

**Brunch Drinks:** Mimosa $8 · Bloody Mary $9 · Coffee $3 · Orange Juice $2 · Apple Juice $2 · Cranberry Juice $2.

**Apps:** Lula Wings $18 · Chip & Dip Trio $16 · Masa-Coated Waffle Fries $8.

**Street Tacos** *(2-taco minimum, street size only)*: Carne Asada, Batata (vegetarian), Carnitas, Barbacoa — $6.50 each ($13 for 2).

**House Favorites:** BFQ $14 + protein · Loaded Waffle Fries or Nachos $15 + protein · The Notorious P.I.G. (burrito or bowl) $18 · Churros $7. Protein add-ons: Carne Asada +$9, Carnitas +$7.

**Sides** *(shared with the lunch/dinner Sides section above)*: Cilantro Lime Rice $6 · Black Beans $7 · Street Corn $9 · Escabeche $3.

⭐ = signature item (lead in copy, photography, ads)

---

## SPECIALS & RECURRING EVENTS

*Source: Supabase `site_events` table (currently empty — `is_recurring` flag distinguishes weekly vs. one-off).*

### Recurring (weekly / standing offers)
- Weekly specials (ongoing): Taco Tuesday (BOGO lunch tacos, $6 margs, $30 pitchers), Beer & Bites Wednesday ($5 pints, $10 loaded nachos, $10 loaded masa fries), **Big F’N Thursday ($10 Big F’N Quesadilla, $10 menu cocktails (fresh sheet, new pours weekly) — new cocktails weekly)**. Happy Hour + $12 lunch special RETIRED. **Burrito Thursday RETIRED 2026-08.**
- **Late Night Happy Hour (Fri + Sat only, 8–10pm — launches 2026-08-28):** $6 margs, $30 marg pitchers, $8 palomas, pick any two street tacos $10 (all street proteins except Camaron/shrimp; tacos only, no side). Fri–Sat only because Tue–Thu close at 8pm.
- [TODO: any standing dinner-night programming, Sunday brunch promo, etc.]

### Upcoming one-offs
- [TODO: list with dates, descriptions, CTA links]

**When adding events to Supabase:**
```sql
INSERT INTO site_events (slug, name, description, starts_at, ends_at, venue, is_recurring, is_published, cta_label, cta_url)
VALUES ('taco-tuesday', 'Taco Tuesday', '$X tacos all night.', '2026-XX-XX 17:00', '2026-XX-XX 22:00', 'cantina', true, true, 'See menu', '/menu/dinner');
```

---

## LOYALTY — UNO MÁS REWARDS: THE CANTINA CLUB

- Toast-based loyalty program, integrated with Klaviyo for email/SMS segments.
- **Performance:** members spend 107% more ($66.99 avg vs. $32.44), visit 2x as often.
- 10% value return on spend.
- 200+ rewards redeemed (to date).
- Signup happens **at POS in-restaurant**, not on the website. Website CTA = "Join the Cantina Club" → Klaviyo form → tagged `loyalty interest` → flow explains in-restaurant signup.

---

## BRAND VOICE

### Personality
Confident · playful · self-aware · community-driven · just a little chaotic.

### Persona
The friend who starts every story with "so we did a thing…" and somehow always knows where the party is. Jester + Everyman with a dash of Rebel. Confident without being cocky. Honest about the chaos.

**Comedian references:**
- **Tom Segura** — default register. Dry, precise, earns the laugh. Use for dinner, Mezzanine, brand-level copy.
- **Bert Kreischer** — lunch / casual / social register. High energy, self-aware, story-driven, never mean.

### Tone by context

| Context | Tone | Emojis |
|---|---|---|
| Lunch / casual | Energetic, playful | 3–5 |
| Dinner / elevated plates | Confident, considered | 1–2 max |
| Cocktails / weekly specials | Flirty, self-aware | 2–3 |
| Patio / outdoor | Casual, inviting | 3–5 |
| **The Mezzanine** | Cool, minimal, moody | 0–1 |
| Paid ads | Hook-driven, clarity first | 1–2 |
| Email / SMS | Friend texting good news | 1–3 |
| Social organic | Full personality | 3–5 |
| Review responses | Warm, direct, never corporate | 0 — sign "The Uno Más Team," under 100 words |
| Private events | Confident, easy-breezy | 1–2 |

### ALWAYS
- Feel like a real person, not a corporation
- Reflect Spokane pride and local community identity
- Lead with the experience, prove it with the food
- Sound like you're in on the joke
- Short sentences. Fragments welcome. Parenthetical asides.
- Dinner copy: slightly more elevated tone — grown up for the occasion
- Price confidence: never apologize, explain, or justify costs

### NEVER (banned words & phrases)
- taco shop *(in brand descriptions)*
- authentic Mexican
- street tacos *(brand-level — fine in direct menu refs)*
- mouthwatering
- culinary journey
- leverage / utilize
- artisanal
- mixology
- amazing *(generic)*
- "We apologize for…"
- vibrant
- "perfect for any occasion"
- Stacked adjectives ("fresh, delicious, flavorful, hearty")
- Trying too hard to sound cool

### Vocabulary swaps
| Use | Instead of |
|---|---|
| Modern Mexican | Authentic Mexican / taco shop |
| House-smoked | Slow-cooked / artisanal |
| Get a little lost | Discover / explore |
| Craft cocktails | Mixology / handcrafted |
| Latin-inspired | Authentic Mexican |
| The Mezzanine | Upstairs / event space |
| Speakeasy | Lounge / bar area |
| Uno Mas Rewards: The Cantina Club | Loyalty program / rewards |
| So we did a thing… | We're excited to announce |
| Hit different | Unique / special |
| Your move | Book now / make a reservation |
| Make good choices | Choose wisely / decide carefully |
| Birria | Braised beef tacos |
| 2020 N Monroe | Our location / the restaurant |

---

## VISUAL IDENTITY

### Uno Más

**Colors**
| Name | Hex | Use |
|---|---|---|
| **Pink** ⭐ | `#E22690` | Primary — logo, hero moments, key highlights |
| Blue | `#18BCDC` | Headlines, accents, CTAs |
| Navy | `#003366` | Dark backgrounds, text on light |
| Yellow | `#FFEC00` | Accents, energy moments |
| White | `#FFFFFF` | Backgrounds, reversed text |
| Black | `#000000` | Body text, dark UI |

**Pink is the hero. Don't let Navy or Blue dominate.**

**Typography**
| Role | Font | Weights |
|---|---|---|
| Headlines / Display | **Antonio** | Bold, Regular |
| Body / UI | **Montserrat** | Light, Regular, Medium, Bold |

**Logo**
- Primary mark: "Uno Más" script + agave icon + "TACOS & TEQUILA" bar
- Icon-only: pink agave plant (favicon / watermark)
- Default treatment: full color (pink on white)
- Reversed: white on dark/navy
- **Canva Brand Kit ID:** `kAFqKpAzOh0`

**Aesthetic note:** Converted mechanic's garage meets Latin cantina. Raw textures, warm atmospheric lighting, neon accents. The room does most of the work. Dinner and Mezzanine content leans darker, more atmospheric — still unmistakably Uno Más.

### The Mezzanine *(sub-brand — never mix with Uno Más design)*

**Colors**
| Name | Hex | Use |
|---|---|---|
| **Electric Pink** ⭐ | `#E22790` | Primary — bold, electric |
| Magenta | `#BF28BF` | Secondary accent |
| Ultra Violet | `#93009B` | Deep accent, dark UI |
| Charcoal | `#333333` | Dark backgrounds, text |
| Deep Black | `#000000` | Primary dark background |
| White | `#FFFFFF` | Reversed text |

**Typography**
| Role | Font | Weights |
|---|---|---|
| Titles / Display | **DIN Condensed VF** | Demi Bold, Regular, Light |
| Body / UI | **Poppins** | Black, Bold, Regular, Medium, Light, Thin |
| Accent Callouts | **Baka Too** | Regular |

**Logo**
- Primary mark: "UM" tribal/geometric + "MEZZANINE" wordmark
- Default: white on black
- Bold: Electric Pink on black
- Premium: gradient (Pink → Magenta → Ultra Violet) on black
- **Canva Brand Kit ID:** `kAGze1MPDmA`

### Brand separation rules
| Content | Uno Más | Mezzanine |
|---|---|---|
| Food, cocktails, main floor | ✅ | — |
| Patio | ✅ | — |
| Sunday Brunch (LIVE · Sundays 10am–4pm) | ✅ | — |
| Mezzanine atmosphere / late night | — | ✅ |
| Private events in Mezzanine | — | ✅ |
| Mezzanine event packages | — | ✅ |

**Never mix:** Uno Más Pink with Mezzanine typography. Never use Antonio in Mezzanine. Never use DIN Condensed in Uno Más.

---

## TECH STACK

### Website (rebuild in flight)
- **Builder:** Lovable (project: `uno-mas-site-builder`)
- **Framework:** TanStack Start v1 (full-stack React, SSR)
- **Styling:** Tailwind v4 (@theme tokens, no `tailwind.config.js`) + shadcn/ui (New York style)
- **Backend:** Supabase project `coandmppuqqzcbbhcien` ("Ramsey Uno Mas Database") — **shared with Creative Studio**
- **Supabase publishable key:** `sb_publishable_lMz5J6zflCQd_1gXmKYvQA_aqApWb2l` *(public — safe to commit)*
- **Image CDN:** Cloudinary, cloud name `drxrfyq9i` (free plan)
- **Hosting:** Netlify (target — DNS cutover from Squarespace pending)
- **Domain:** unomastacoshop.com (currently on Squarespace; cutover at launch)

### Creative Studio (sibling app)
- **Project:** `uno-m-s-creator` Lovable app
- **Repo:** github.com/Ramsey-SL/uno-m-s-creator
- Same Supabase as website. Generates campaign content, manages brand_guidelines, uploads to Cloudinary via `/app/bulk-upload`.

### Integrations
| Service | Use | Notes |
|---|---|---|
| **Resy** | Reservations (dinner + brunch) | Venue ID `87582`, public widget key `g47nf19Sg6grqO50HcS2HDIUIO8PjEGM` |
| **Klaviyo** | Email + SMS marketing | Account/Public API Key `UjAfaJ`. Connected to Toast AND Square. 6 lists, 4 segments (all Square-based), 0 flows. Onsite pixel snippet in EMAIL / SMS — KLAVIYO section. |
| **Toast** | POS + loyalty backend | **Sole POS as of 2026-05-26.** Source of truth for menu pricing in-restaurant, loyalty member data. Square was decommissioned. |
| **Vista Social** | Social scheduling | Instagram + Facebook |
| **Meta Ads Manager** | Paid social | Managed in-house |
| **Google Ads** | Paid search | Managed in-house |
| **GTM** | Tag wrapper — recommended approach for rebuild | Container `GTM-T6L25CLD` (re-use on new site). Account ID `6338296309`. Internal container ID `243011905`. See TAG MANAGER section. |
| **GA4** | Web analytics | Measurement ID `G-YXKMDL0KF2` · Property ID `523092931` · Account ID `383242412` · Stream ID `13410595932` · Stream name: "Uno Mas Taco Shop" · Enhanced measurement ON · Data flowing confirmed |
| **Google Business Profile** | Local SEO | [TODO: confirm verified + photo upload cadence] |
| **Apple Business Connect** | Local SEO | [TODO: confirm claimed] |

### Security note
- **Public keys** (Resy widget, Supabase publishable, GA4 measurement ID): safe to commit + paste in chat.
- **Service role keys / database passwords / private API tokens / OAuth secrets: NEVER paste in chat. NEVER commit. NEVER share with Claude.**

---

## ASSET LIBRARY & TAG CONVENTIONS

### Current state (as of 2026-05-25)
- **201** total assets in Supabase `assets` table
- **172** synced from Cloudinary with full role tagging
- **29** legacy Supabase Storage uploads (pre-Cloudinary unification)
- **All 201** flagged `status='approved'` and not archived → visible to website

### Tag prefixes
| Prefix | Use | Example |
|---|---|---|
| `role:` | Maps asset to a specific website slot | `role:hero-cantina`, `role:venue-mezzanine`, `role:team-ramsey` |
| `category:` | Broad content type | `category:food`, `category:interior`, `category:cocktails`, `category:menu`, `category:tacos`, `category:general_vibe` |
| `orientation:` | Aspect/use hint | `orientation:landscape`, `orientation:portrait`, `orientation:square` |
| *menu slug* | Auto-binds photo to menu item | `carne-asada`, `surf-turf`, `birria-tacos` |
| *free-form descriptors* | Searchable filters | `mezzanine`, `patio`, `vibe-night`, `vibe-day`, `interior`, `signature`, `team`, `dinner`, `lunch`, `brunch` |

### Role tags reference (canonical list)

| Role tag | Where it renders | Aspect | Priority |
|---|---|---|---|
| `role:hero-cantina` | Homepage hero, /reservations hero | 16:9 wide | P1 |
| `role:hero-dinner` | /menu/dinner hero, homepage dinner feature | 16:9 wide | P1 |
| `role:hero-mezzanine` | /mezzanine hero, homepage mezzanine teaser | 16:9 wide | P1 ✅ |
| `role:hero-about` | /about hero (falls back to hero-cantina) | 16:9 wide | P1 |
| `role:hero-cocktails` | /menu/cocktails hero (future) | 16:9 wide | P2 |
| `role:hero-lunch` | /menu/lunch hero (future) | 16:9 wide | P2 |
| `role:hero-brunch` | /menu/brunch hero (future) | 16:9 wide | P2 |
| `role:venue-cantina` | Homepage venues card | 4:5 / 1:1 | P1 |
| `role:venue-mezzanine` | Homepage venues card | 4:5 / 1:1 | P1 ✅ |
| `role:venue-patio` | Homepage venues card | 4:5 / 1:1 | P1 |
| `role:team-ramsey` | /about team grid | 1:1 | P1 |
| `role:team-karissa` | /about team grid | 1:1 | P1 |
| `role:team-thomas` | /about team grid | 1:1 | P1 |
| `role:team-maraya` | /about team grid | 1:1 | P1 |
| `role:mezzanine-private-dinner` | /mezzanine 3-up grid | 4:5 | P2 |
| `role:mezzanine-buyout` | /mezzanine 3-up grid | 4:5 | P2 |
| `role:mezzanine-cocktails` | /mezzanine 3-up grid | 4:5 | P2 |
| `role:patio-bar` | /patio future detail | — | P3 |
| `role:patio-food` | /patio future detail | — | P3 |
| `role:patio-crowd` | /patio future detail | — | P3 |
| `role:logo` (+ color variants `-pink`, `-white`, `-black`, `-navy`, `-blue`, `-gradient`) | Header, footer, OG images, fallbacks | varies | P1 ✅ (21 logos already) |

**Tag format rules:**
- All lowercase
- Hyphens, not underscores
- `role:` is the routing tag — the one the website queries for
- Add 2–4 fallback tags so the asset still surfaces in browse views

**How website resolves a slot:**
`resolveImageByTags(primaryTag, fallbackTags[])` → finds first approved, non-archived asset matching primary tag → if 0 results, walks fallback tags in order → if still nothing, renders placeholder.

### Full image slot reference
See **`uno-mas-website-image-slots.md`** in this workspace for per-page slot specs, aspect ratios, and shoot lists.

### Asset upload workflow
1. **Cloudinary is the canonical source.** Upload via Creative Studio `/app/bulk-upload` (routes correctly to Cloudinary).
2. Tag in Cloudinary with role + descriptors.
3. Trigger sync (or weekly auto-sync — Phase 3 not yet built) → creates/updates row in Supabase `assets`.
4. Website queries by tag → photo appears live. No code change.

**Known gap:** `/upload` (public) and `/app/submit-asset` in Creative Studio currently bypass Cloudinary and write to Supabase Storage directly. Unify these paths or document the bulk-upload-only rule. Logged in backlog INBOX.

---

## SEO & AI SEARCH

### Target keywords (local SEO)

> **Strategic shift 2026-05-26:** "Modern Mexican" is being called out in industry as vague/generic. Keep it in brand voice/copy but don't chase it for SEO. Higher-leverage targets below.

**Primary (chase these):**
1. tacos and tequila Spokane *(brand-aligned, exact match to our name, low competition)*
2. Spokane Mexican brunch *(🚀 OPEN LANE — own before competitors notice)*
3. Spokane speakeasy *(Mezzanine winnable — thin competitor field)*
4. private event venue Spokane *(direct intent → catering revenue)*
5. dinner Spokane Monroe / Monroe Street Mexican *(geo-specific niche)*

**Win via Google Business Profile + schema (not on-page SEO):**
1. best Mexican restaurant Spokane
2. Mexican restaurants Spokane
3. tacos Spokane

**Secondary keywords:**
1. modern Mexican Spokane *(legacy guess —
2. dinner Spokane
3. speakeasy Spokane
4. private event venue Spokane
5. brunch Spokane *(LIVE — Sundays 10am–4pm)*
6. date night Spokane
7. best restaurants Spokane
8. Monroe Street restaurant Spokane
9. Latin restaurant Spokane
10. taco bar Spokane
11. tequila bar Spokane

### Schema markup (JSON-LD — required on all pages)

**`Restaurant` schema** — on `/` and `/about`. Should include:
- `@type`: Restaurant
- `name`, `image`, `url`
- `address` (PostalAddress with all fields)
- `geo` (GeoCoordinates — [TODO: confirm lat/long])
- `telephone`
- `servesCuisine`: ["Mexican", "Latin", "Modern Mexican"]
- `priceRange`: "$$" (or "$$$" for dinner pages)
- `openingHoursSpecification` (array — one per day)
- `acceptsReservations`: true
- `hasMenu`: URL to /menu
- `sameAs`: array of social URLs

**`Menu` + `MenuSection` + `MenuItem`** — on `/menu`, `/menu/dinner`.

**`LocalBusiness`** with `OpeningHoursSpecification`.

**`Event`** — for `site_events` rows when populated.

### llms.txt
Static file at root with:
- Brand summary (2–3 sentences from voice-identity.md)
- Address, hours summary, reservation URL
- Links to key pages: /menu/dinner, /mezzanine, /about
- "We are NOT a taco shop" disambiguation paragraph (prevents AI crawlers from miscategorizing)

### sitemap.xml
Dynamically generated from routes. Update whenever a new route is added.

### robots.txt
Allow all. Point to sitemap.

### Per-page meta tags template

```
<title>{Page-Specific Title} | Uno Más Tacos & Tequila — Spokane</title>
<meta name="description" content="{≤155 chars, includes target keyword, ends with CTA}">
<meta property="og:title" content="{Page title, no '| Uno Más...' suffix}">
<meta property="og:description" content="{Same as meta description}">
<meta property="og:image" content="{Cloudinary URL of role:hero-{page} asset}">
<meta property="og:url" content="https://unomastacoshop.com/{path}">
<meta property="og:type" content="restaurant.menu">
<meta name="twitter:card" content="summary_large_image">
```

**Page-by-page title patterns:**
| Page | Title pattern |
|---|---|
| `/` | Modern Mexican & Tequila Bar in Spokane \| Uno Más Tacos & Tequila |
| `/menu/dinner` | Dinner Menu — Carne Asada, Surf & Turf, The Feast \| Uno Más Spokane |
| `/menu/lunch` | Lunch Menu — Tacos, Plates, Cocktails \| Uno Más Spokane |
| `/menu/brunch` | Sunday Brunch in Spokane \| Uno Más Tacos & Tequila |
| `/menu/cocktails` | Craft Cocktails & Tequila Bar in Spokane \| Uno Más |
| `/mezzanine` | The Mezzanine — Spokane's Speakeasy & Private Event Venue |
| `/about` | About Uno Más — Three Venues on Monroe in Spokane |
| `/reservations` | Reservations \| Uno Más Tacos & Tequila — Spokane |

---

## ANALYTICS & TRACKING

| System | ID / Endpoint | Purpose |
|---|---|---|
| GA4 | Measurement ID: `G-YXKMDL0KF2` · Property ID: `523092931` · Account ID: `383242412` | Site analytics, conversion tracking |
| Google Tag Manager | `GTM-T6L25CLD` *(currently on Squarespace)* | Wrapper firing GA4 + any other configured tags. For the rebuild, decide: re-use this container, or wire GA4 directly with `gtag.js`. |
| Meta Pixel | `1737601003250529` | Retargeting, conversion API |
| Google Ads conversion tag | `[TODO: AW-XXXXX]` | Paid search conversions |
| Klaviyo | Public site tracking key: `[TODO: paste]` | Onsite tracking → flow triggers |
| Toast | n/a (POS-side only) | Loyalty + revenue source-of-truth |

### Events to track in GA4
| Event | Trigger | Page |
|---|---|---|
| `reserve_table_click` | Resy button clicked | header, hero, /reservations |
| `menu_pdf_download` | Lead-gen menu download | /menu, /menu/dinner |
| `event_inquiry_submit` | Mezzanine inquiry form | /mezzanine |
| `cantina_club_signup` | Klaviyo loyalty form submit | / , /about, footer |
| `phone_click` | Click-to-call tap | mobile contact strip |
| `directions_click` | Map / address tap | contact strip |

---

## CONVERSION GOALS (priority order)

1. **Walk in and dine** — primary; no reservation required.
2. **Dinner reservation via Resy** — active campaign focus.
3. **Cantina Club loyalty signup** — at POS via Toast / Klaviyo segment.
4. **Private event or catering inquiry** → karissa@unomastacoshop.com.
5. **Sunday brunch visit** — LIVE — Sundays 10am–4pm.

---

## PROOF POINTS (use in copy / ads / press)

- 2022 founded — 3+ years on Monroe Street
- Loyalty members spend **107% more** ($66.99 avg vs. $32.44)
- Loyalty members visit **twice as often**
- 200+ rewards redeemed
- Top organic post: 1,400+ likes, 76K views
- Brunch announcement post: 785 likes, 41K views
- Top-reviewed Latin restaurant in Spokane (Google + Yelp)

---

## COMPETITOR LANDSCAPE (quick reference)

Full analysis in `brand-intelligence-center/differentiation.md`. Quick refs:

| Competitor | Their angle | Our counter |
|---|---|---|
| **Table 13 Tacos & Tequila** *(added 2026-05-26)* | Davenport Grand Hotel downtown, largest tequila list in Spokane | Three-venue concept + room/experience + brunch lane + non-chain identity |
| Borracho Tacos & Tequila | Large patio, tequila list | Three distinct venues + full dinner program |
| Cochinito Taqueria | Chef-driven taqueria | Match food, exceed on experience + occasion range |
| Purgatory Agave | Tacos + tequila cocktails | Deeper roots, more venue flexibility |
| Matador (chain) | Brand recognition | We're the anti-chain |
| Indicana | India-Mexico fusion, "Best New Restaurant 2025" | Broader menu, three venues, stronger loyalty base |

---

## CURRENT BUSINESS FOCUS

- **Dinner menu rollout** *(active, primary campaign)* — elevated pricing, premium-tone copy
- Scaling social content volume with AI-assisted production (Creative Studio)
- Positioning The Mezzanine as Spokane's premier private event + speakeasy venue
- Website migration off Squarespace → Lovable/Netlify with local + AI SEO
- Klaviyo email/SMS campaigns tied to Toast loyalty data
- Expanding brand awareness beyond current loyal regulars
- **Catering target:** $8K/month (currently $55K+ annual with no dedicated sales effort)

---



## EXTERNAL LISTINGS & REVIEWS

*Last reviewed: 2026-05-25*

### Public listing data confirmed

| Source | Listed details | Notes |
|---|---|---|
| **Visit Spokane** | 2020 N Monroe St, Spokane, **99201** ⚠️ (their data has wrong zip), phone (509) 960-7989, "Bars & Grills / Mexican" categories, lat/long 47.6764702/-117.4263699 | Has stale description: "redefining comfort food with a witty twist." Worth updating their listing to match current "Modern Mexican" positioning. [Listing](https://www.visitspokane.com/directory/uno-mas-tacos-tequila/) |
| **Yahoo Local / Yelp aggregate** | 3.5 stars, ~13–16 reviews, hours match live site (Sun-Mon closed, Tue-Thu 11–9, Fri-Sat 11–10) | [Listing](https://local.yahoo.com/info-238062511-uno-ms-spokane-spokane/) |
| **Yelp** | 20 photos, 13 reviews as of Feb 2026 | [Listing](https://www.yelp.com/biz/uno-más-spokane-spokane) |

### Recent review themes (from Yahoo/Yelp aggregate, last 12 months)
- 🟢 **Positive:** "bold flavor," Lula Wings called out specifically, Tostilocos mentioned *(historical review quote — item since removed from the menu, confirmed 2026-08-04)*, brunch launch ("first day Uno Más offered brunch — Boozy Barista drink"), space praised ("pretty spacious with a private event room"), location callout ("tucked behind the new Indaba on Knox")
- 🟡 **Mixed:** "white rice in the bowl" feedback (Camino/Monroe bowls), "so/so" portions
- 🔴 **Negative:** One review noting decline vs. original Wonder Building location ("now established, and it has only degraded")

### Google Business Profile (not directly accessible to Claude)

Claude cannot pull live data **from your Google Business Profile dashboard or the official Google reviews feed without one of these:**

1. **Google Places API key** — gives access to up to 5 most recent reviews per business + review count + average rating. Costs ~$17/1000 calls but free tier covers small usage. Best for live review embed on website.
2. **Google Business Profile API access** — full review management (read all reviews, write responses programmatically). Requires OAuth to the GBP account itself, harder to wire up.
3. **Manual sync** — copy/paste from the dashboard into a Supabase `reviews` table on a cadence (weekly or monthly).

**Recommendation:** Use the Places API for the website's "Reviews" section + JSON-LD `aggregateRating` schema. It's the fastest path and the rating + 5 most-recent reviews is what AI search (Google AI Overviews, Perplexity) actually surfaces. Logging this as a backlog item.

### Action items for ongoing listing hygiene

- [ ] **Fix Visit Spokane zip code** — they have 99201, should be 99205. Email their directory team via [directory@visitspokane.com](mailto:directory@visitspokane.com) or use their "is this your business?" claim flow.
- [ ] **Update Visit Spokane description** — current copy is outdated ("comfort food with a witty twist"). Should match current voice — pull from one of the four pre-written brand sentences in this doc.
- [ ] **Claim/verify all listings** — Yelp, Yahoo Local, Restaurantji, Apple Business Connect, Bing Places. Anywhere you're listed without claiming it, you can't respond to reviews.
- [ ] **Set up Places API for live reviews on website** — adds rating + 5 most recent reviews to /, /about, schema markup. Cost is minimal at our traffic.
- [ ] **Standing review response cadence** — use the `local-business-marketing-os:review-responses` skill to draft replies to new Google + Yelp reviews weekly.

---



## EMAIL / SMS — KLAVIYO

*Pulled live from Klaviyo API on 2026-05-26.*

### Account
| Field | Value |
|---|---|
| **Public API Key / Account ID** | `UjAfaJ` *(used in onsite tracking pixel + signup forms)* |
| **Organization name** | Uno Mas Taco Shop |
| **Default sender email** | Tacos@unomastacoshop.com |
| **Default sender name** | Uno Más Taco Shop |
| **Industry** | Restaurants |
| **Timezone** | America/Los_Angeles |
| **Currency** | USD |
| **Address on file** | 2020 N Monroe St Suite C, Spokane, WA 99205 *(matches)* |

### Klaviyo Onsite Tracking Pixel

Install this in `<head>` on every page of the new Lovable site:

```html
<!-- Klaviyo Onsite Tracking -->
<script async type="text/javascript"
  src="https://static.klaviyo.com/onsite/js/UjAfaJ/klaviyo.js">
</script>
```

Once installed, you can fire events client-side:
```javascript
// Identify a known user (e.g., after email signup)
_learnq.push(['identify', { '$email': 'guest@example.com', '$first_name': 'Pat' }]);

// Track a custom event (e.g., "Viewed Menu Item")
_learnq.push(['track', 'Viewed Menu Item', {
  ItemName: 'Surf & Turf', ItemPrice: 47, Daypart: 'dinner'
}]);
```

### Lists (6 total)

| List ID | Name | Opt-in |
|---|---|---|
| `SA8BS3` | Text Messaging List | Double opt-in |
| `T8wq9g` | Preview List | Single opt-in |
| `TcwW8y` | **Uno Mas - Marketing Opt In** | Single opt-in *(primary marketing list)* |
| `V3fFSV` | Full Customer List - Square | Single opt-in |
| `XXqgpu` | Email List | Single opt-in |
| `XrvckP` | SMS Import | Double opt-in |

### Segments (4 total)

| Segment ID | Name | Active |
|---|---|---|
| `TTJ8xD` | Repeat Buyers (Square) | ✅ |
| `VUmxAF` | All SMS Subscribers | ✅ |
| `Wjb4EK` | Potential Purchasers (Square) | ✅ |
| `XY6eZD` | All Profiles Export | ✅ |

> ⚠️ **Note on segmentation:** Active segments still use legacy **Square** data, but Square POS is decommissioned (Toast is now sole POS as of 2026-05-26). All new segments + flows must be built off Toast metrics. Square integration in Klaviyo is historical-only — pending decision to disconnect.

### Flows

**Zero flows currently active.** No welcome series, no post-purchase, no abandoned cart, no win-back, no birthday flow. The brand intel previously suggested flows were live — they are not.

**Recommendation P1:** Build out the core flow stack:
- Welcome series (triggered by `Subscribed to List → Uno Mas - Marketing Opt In`)
- Post-purchase nurture (triggered by `Placed Order` via Toast)
- Abandoned checkout (triggered by `Abandoned Checkout` via Square — or wait until Toast equivalent exists)
- Win-back / re-engagement (90/180/365 day variants)
- Birthday flow (if collecting DOB at signup)
- Reservation confirmation companion (triggered by Resy webhook or a "Reservation Made" custom event)

### Active integrations + their metrics

| Integration | Metrics fed into Klaviyo |
|---|---|
| **Toast** *(Restaurants)* | Placed Order · Ordered Product · Fulfilled Order · Prepared Order |
| **Square** *(eCommerce)* | Placed Order · Abandoned Checkout · Cancelled Order · Fulfilled Order · Ordered Product · Refunded Order |
| **Meta Ads** *(Advertising)* | Filled Out Lead Ad |
| **API** *(Custom/server-side)* | Viewed Product · Active on Site |
| **Klaviyo internal** | Email + SMS engagement events (opens, clicks, subscribes, unsubscribes, bounces, etc.) |

### Useful metric IDs (for flow triggers + segment conditions)

| Metric ID | Name | Source |
|---|---|---|
| `XyK4sq` | Placed Order | Toast |
| `Vd6SAT` | Ordered Product | Toast |
| `RyUsKV` | Placed Order | Square |
| `SBrM8r` | Abandoned Checkout | Square |
| `VHdQXa` | Active on Site | API *(client-side onsite tracking)* |
| `UwKbag` | Viewed Product | API *(client-side custom event)* |
| `UF5EmK` | Subscribed to List | Klaviyo |
| `YvN4EH` | Subscribed to SMS Marketing | Klaviyo |
| `YfVrnH` | Subscribed to Email Marketing | Klaviyo |
| `W7xwB6` | Filled Out Lead Ad | Meta Ads |

### Segment-building ideas (post-launch)

Once the onsite pixel is firing on the new website, build segments off:
- "Engaged + Hasn't ordered recently" → win-back targets
- "Viewed dinner menu in last 30 days but no order" → dinner conversion targets
- "Cantina Club opted in but never claimed a reward" → activation push
- "SMS subscriber + ordered ≥3 times" → VIP tier
- "Brunch interest (subscribed via brunch landing page)" → ready-list for when brunch relaunches

---

## TAG MANAGER — GOOGLE TAG MANAGER (GTM)

*Live on Squarespace site as of 2026-05-26. Tag config detail is in the GTM admin UI; container JS is fetchable at `https://www.googletagmanager.com/gtm.js?id=GTM-T6L25CLD` if needed.*

### Container details

| Field | Value |
|---|---|
| **Container ID** | `GTM-T6L25CLD` |
| **GTM Account ID** | `6338296309` |
| **GTM Container internal ID** | `243011905` |
| **Workspace** | Default Workspace |
| **Live Version** | Version 2 (published 4 months ago by ramsey@unomastacoshop.com) |
| **Container quality** | Good (per GTM dashboard) |

### Installation snippets (currently on Squarespace)

**Head (loads GTM):**
```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-T6L25CLD');</script>
<!-- End Google Tag Manager -->
```

**Body (noscript fallback):**
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T6L25CLD"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

### Decision: GTM container vs. direct gtag for the rebuild

**Recommendation: Re-use the existing `GTM-T6L25CLD` container** on the Lovable rebuild. Reasons:
1. **Consistency:** preserves the historical attribution model (GA4 + Meta Pixel + any other tags already configured fire identically before and after the cutover)
2. **Flexibility:** future tag additions (TikTok Pixel, Pinterest Tag, conversion API endpoints, etc.) require only a GTM admin change — no code deploy
3. **Centralized triggering:** events like "reserve_table_click," "view_menu_item," "cantina_club_signup" can fire in GTM and propagate to GA4 + Meta + Klaviyo in one place

**The alternative — direct gtag.js + direct Meta Pixel — gets us:**
- Slightly faster page load (no GTM wrapper)
- Slightly cleaner code
- But every new tag is a code change. Painful for a marketing-led product.

### Tags / triggers / variables (TODO: capture from GTM admin)

[TODO: paste GTM container JS so we can extract the full tag list, or screenshot the Tags / Triggers / Variables sections of GTM admin. Current assumption: at minimum the GA4 config tag firing `G-YXKMDL0KF2` is in there, since we confirmed data is flowing to GA4. Probably also Meta Pixel `1737601003250529` firing on All Pages. Anything else — Klaviyo onsite, Google Ads conversion tags, custom events — unconfirmed until we read the container.]

### Tags we want on the rebuild (recommended target state)

| Tag | Purpose | Trigger |
|---|---|---|
| **GA4 Config** (`G-YXKMDL0KF2`) | Base GA4 install + enhanced measurement | All Pages |
| **GA4 Event — reserve_table_click** | Track Resy button clicks | Custom event: button class/ID match |
| **GA4 Event — view_menu_item** | Track engagement with menu items | Custom event from React |
| **GA4 Event — cantina_club_signup** | Loyalty form submissions | Form submit on `.klaviyo-form-*` |
| **GA4 Event — phone_click** | Click-to-call on mobile | Click on `tel:` link |
| **GA4 Event — directions_click** | Address / map clicks | Click on map link |
| **Meta Pixel Base** (`1737601003250529`) | PageView on all pages | All Pages |
| **Meta Pixel Lead** | Klaviyo form submission | Same trigger as cantina_club_signup |
| **Meta Pixel ViewContent** | Menu item views | Same trigger as view_menu_item |
| **Klaviyo onsite tracking** (`UjAfaJ`) | Active on Site / Viewed Product tracking | All Pages — or load directly in `<head>`, bypassing GTM |
| **Google Ads conversion tag** | Tie Google Ads campaigns to conversions | Reserve / signup events |

### Security note

The GTM container ID, GA4 Measurement ID, Meta Pixel ID, and Klaviyo Public API Key are all **public values** — they're designed to be exposed in client-side code. Safe to commit + paste in chat. Service-level credentials (GTM admin, Klaviyo private API key, Meta Business Manager access tokens) are NOT in this doc.

---

## DOCUMENT INDEX — where to find more depth

| Topic | File |
|---|---|
| Active project todos + INBOX | `uno-mas-website-backlog.md` (this workspace) |
| Per-page image slot specs + shoot lists | `uno-mas-website-image-slots.md` (this workspace) |
| Weekend sprint guide | `uno-mas-weekend-sprint-v2.md` (this workspace) |
| Brand: business identity, address, team | `brand-intelligence-center/business.md` (uno-mas repo) |
| Brand: digital ecosystem, integrations | `brand-intelligence-center/digital-ecosystem.md` |
| Brand: voice, vocabulary, banned words, visual identity | `brand-intelligence-center/voice-identity.md` |
| Brand: competitive position + differentiation | `brand-intelligence-center/differentiation.md` |
| Brand: customer personas | `brand-intelligence-center/customer.md` |
| Brand: proof points + goals | `brand-intelligence-center/proof-goals.md` |
| Brand: financial context | `brand-intelligence-center/financial.md` |
| Brand: Claude system prompt | `brand-intelligence-center/system-prompt.md` |
| Creative Studio roadmap | `docs/uno-mas-creative-studio-roadmap.md` (uno-mas repo) |

---

## TODO — gaps to fill

1. ~~**Primary phone number**~~ ✅ (509) 960-7989
2. ~~**GA4 Measurement ID**~~ ✅ `G-YXKMDL0KF2`
2a. **Decide: re-use GTM container `GTM-T6L25CLD` on the new site, or wire GA4 + Meta Pixel directly?** GTM is more flexible for future tag additions; direct is simpler and faster.
3. ~~**Meta Pixel ID**~~ ✅ 1737601003250529
4. **Google Ads conversion tag** (paste `AW-XXXXX`)
5. ~~**Klaviyo public site tracking key**~~ ✅ `UjAfaJ` (also see EMAIL / SMS — KLAVIYO section)
6. ~~**Exact lat/long**~~ ✅ 47.6764702, -117.4263699
7. **Email addresses** for Thomas Schulke + Maraya Lindo
8. ~~**Lunch menu items**~~ ✅ documented in master MD (per April 2026 menu PDF). Still needs Supabase reconciliation — see `MENU-RECONCILIATION-SQL.md` once generated.
9. **Brunch menu items** — finalized & live (Sundays 10am–4pm); see `website/content-studio/menus/brunch-menu.md`
10. ~~**Cocktail items**~~ ✅ documented in master MD (9 cocktails + pitchers + beer + non-alc). Needs Supabase reconciliation.
11. **Recurring specials** (Taco Tuesday, Beer & Bites Wednesday, Big F’N Thursday, Late Night Happy Hour Fri+Sat, etc.) — seed into `site_events`
12. **Upcoming one-off events** — seed into `site_events`
13. **Google Business Profile + Apple Business Connect** — confirm verified, photo upload cadence
14. **Award / press list** — finalize what's quotable

---

*Update this file as facts change. It's the canonical brand reference. Don't rely on chat sessions to remember.*
