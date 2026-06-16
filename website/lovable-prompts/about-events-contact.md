# Lovable Prompt — /about + /private-events + /contact (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Build out three stub pages in one pass + fix wrong email domains. Use the same lighter visual treatment we're applying to the menu pages (cream `#fafaf7` body, near-black text, brand pink `#E22690` accents, warm-dark heroes).

---

## PASTE BELOW THIS LINE INTO LOVABLE

Build out three currently-stubbed pages: `/about`, `/private-events`, `/contact`. Also fix two wrong email addresses found on the site (see Bug Fix section at the bottom).

Use the same lighter visual treatment as the menu pages: cream body background `#fafaf7`, near-black text `#1a1a1a`, brand pink `#E22690` for accents and CTAs, warm-dark hero bands. Antonio Bold for headlines (all caps, tight letter-spacing), Montserrat for body. Generous whitespace.

---

## PAGE 1: /about

### Hero band
- Image: `role:hero-about` (fallback to `role:hero-cantina`)
- Kicker: "Our Story"
- Headline: **"BUILT IN SPOKANE. FED BY MEXICO."** (Antonio Bold, white over dark gradient overlay)
- Subhead: "A modern Mexican kitchen and tequila bar in a converted garage on Monroe. Three venues. One address. Get a little lost."

### Section 1 — Brand narrative
Two-column on desktop, single column on mobile. Left side body copy, right side a single photo (use any asset tagged `role:hero-cantina` or `role:venue-cantina`).

**Headline:** "We started as a taco shop. We grew into something more."

**Body** (use exactly this copy — it's brand-approved):
> Uno Más is a modern Mexican restaurant and tequila bar at 2020 N Monroe in Spokane. We run a lunch program and an elevated dinner program. We have a full craft cocktail menu. We have The Mezzanine — a speakeasy and private event space upstairs. We are a gathering place. We are a destination.
>
> The ground floor cantina operates out of a converted mechanic's garage. Inside, it feels like outside. Feels like somewhere else entirely. The room does most of the work.
>
> Tacos are something we do exceptionally well — they are not the entirety of what we are.

### Section 2 — Three venues, one address
3-column grid on desktop, single column on mobile. Each card:
- Image (`role:venue-cantina`, `role:venue-mezzanine`, `role:venue-patio`)
- Title (Antonio Bold): The Cantina · The Mezzanine · The Patio
- Body (1-2 sentences each):
  - **The Cantina:** Ground floor. Converted garage. Lunch + elevated dinner + full bar. The room does the work.
  - **The Mezzanine:** Upstairs. Speakeasy + private events. Leather, fireplace, low light. The kind of room where whatever you're celebrating actually feels celebrated.
  - **The Patio:** Outdoor bar + street-food kitchen. Watch parties, big groups, sunny afternoons that turn into nights.
- Link: each card links to the relevant page (Cantina → /menu/dinner, Mezzanine → /mezzanine, Patio → /menu/lunch for now)

### Section 3 — Meet the team
Headline: "WHO YOU'RE TRUSTING WITH YOUR NIGHT."

4-card grid (or 2x2 on mobile). Each card:
- Headshot image (use `role:team-{firstname}` tag — fallback to a styled monogram circle in `#E22690` with white initials if no photo yet)
- Name (Antonio Bold)
- Title (Montserrat italic, gray)
- One-line bio in body copy

Team data:
- **Ramsey Pruchnic** — Owner. "Built it. Runs it. Knows every regular by name."
- **Karissa Schulke** — GM / Events. "If you're booking the Mezzanine, you're talking to Karissa. karissa@unomastacoshop.com"
- **Thomas Schulke** — Operations Manager. "Keeps the lights on, the kitchen moving, the floor sharp."
- **Maraya Lindo** — Executive Chef. "Runs the kitchen. Carne Asada is hers. So is the Feast."

### Section 4 — Proof points / why people come back
4-up stat band on cream background, with each stat in its own block. Numbers in Antonio Bold ~48px, brand pink `#E22690`. Caption underneath in Montserrat, gray.

- **2022** — Founded. 3+ years on Monroe.
- **107%** — How much more loyalty members spend vs. non-members.
- **2×** — How often loyalty members visit.
- **3** — Venues at one address.

### Section 5 — Visit strip / contact band
At the bottom, a dark band `#1a1a1a` with white text:
- Headline: "FIND US."
- Address: 2020 N Monroe St, Suite C · Spokane, WA 99205 (link to Google Maps)
- Phone: (509) 960-7989 (tel: link)
- Hours summary (pull from Supabase `business_hours`)
- Email: tacos@unomastacoshop.com
- CTA: "Reserve a Table" button → Resy

### SEO
- `<title>`: "About Uno Más — Three Venues on Monroe in Spokane"
- meta description: "Modern Mexican on Monroe. Built in a converted garage. A cantina, a speakeasy, and a patio at 2020 N Monroe in Spokane. Get a little lost."
- og:image: `role:hero-about` Cloudinary URL
- JSON-LD: AboutPage schema linked to the Restaurant entity

---

## PAGE 2: /private-events

### Hero band
- Image: `role:hero-mezzanine` (or any asset tagged `mezzanine` + `event`)
- Kicker: "Private Events · Catering · Buyouts"
- Headline: **"WHATEVER YOU'RE CELEBRATING DESERVES THE ROOM."**
- Subhead: "Three venues. Twenty guests to two hundred. Mezzanine dinners, patio takeovers, full buyouts, off-site catering."
- Primary CTA: "Inquire" → mailto:karissa@unomastacoshop.com with subject pre-filled "Private Event Inquiry — [Venue]"

### Section 1 — Event types (4-up grid)
4 cards. Each card has image, title, capacity, ideal-for, link to inquiry.

**Card 1 — The Mezzanine**
- Image: `role:mezzanine-private-dinner` (fallback: `role:venue-mezzanine`)
- Title: Mezzanine Dinners
- Capacity: 35-40 seated · 65-75 standing
- Ideal for: Rehearsal dinners, milestone birthdays, intimate corporate events.
- Body: "Upstairs. Private entrance. Full bar. Leather lounges and a fireplace. The kind of room where whatever you're celebrating actually feels celebrated."

**Card 2 — The Patio**
- Image: `role:venue-patio` (fallback: `role:patio-crowd`)
- Title: Patio Takeovers
- Capacity: 40-80 standing
- Ideal for: Watch parties, summer happy hours, casual group celebrations.
- Body: "Outdoor bar. Street-food kitchen. Daytime energy that runs into the night."

**Card 3 — Full Restaurant Buyout**
- Image: `role:venue-cantina` (fallback: `role:hero-cantina`)
- Title: Full Buyouts
- Capacity: 150-200+
- Ideal for: Weddings, large corporate events, big-format celebrations.
- Body: "All three spaces. Custom menu options. We handle the room, you handle the toast."

**Card 4 — Off-Site Catering**
- Image: `role:hero-dinner` (placeholder until we have a proper catering shot)
- Title: Off-Site Catering
- Capacity: 25-500+
- Ideal for: Office lunches, corporate events, big-house weddings.
- Body: "We bring it to you. Tacos, plates, full setups. Quote within 24 hours."

### Section 2 — What's included
3-up icon row (use Tabler outline icons via `<i class="ti ti-*"></i>`):
- 🍽 Custom menus tailored to your group (ti-tools-kitchen)
- 🍸 Full bar + craft cocktails (ti-glass-cocktail)
- 👥 Dedicated event coordinator (Karissa) (ti-user-check)

### Section 3 — How it works
3-step horizontal flow:
1. **Tell us about your event** → fill the inquiry form OR email karissa@unomastacoshop.com
2. **We build a proposal** → menu, pricing, layout, timing — usually back to you within 24-48 hours
3. **You show up. We handle the rest.** → from setup to cleanup, you're a guest at your own event.

### Section 4 — Inquiry form / contact band
Embedded form (use Klaviyo form if possible, otherwise simple mailto) with these fields:
- Name
- Email
- Phone
- Event type (dropdown: Mezzanine Dinner / Patio Takeover / Full Buyout / Off-Site Catering / Other)
- Estimated guest count
- Date(s) you're considering
- Tell us about your event (textarea)
- CTA: "Send Inquiry"

On submit, route to karissa@unomastacoshop.com. Also fire a Klaviyo `Filled Out Lead Ad` style event if Klaviyo onsite pixel is loaded (it should be in the future — for now mailto fallback is fine).

Below the form, a dark band:
- "Talking with Karissa is the fastest path. karissa@unomastacoshop.com · (509) 960-7989"

### SEO
- `<title>`: "Private Events & Catering in Spokane | Uno Más Tacos & Tequila"
- meta description: "Private dinners, full buyouts, off-site catering. Three venues at 2020 N Monroe. Rehearsals, weddings, corporate events. Inquire with Karissa."
- og:image: `role:hero-mezzanine`
- JSON-LD: Service schema for the catering offering

---

## PAGE 3: /contact

### Hero (tight, not full-bleed)
- Kicker: "Say Hello"
- Headline: **"CONTACT US."** (Antonio Bold, near-black on cream)
- Subhead: "Reservations, private events, press, or just to say you loved the Birria."

### Section 1 — Two-column primary info
Left column (60% width on desktop, full width on mobile):

**Find us:**
- Address: 2020 N Monroe St, Suite C, Spokane, WA 99205
  - Subline: "Behind Indaba Coffee. Corner of Knox Ave & N Monroe."
  - "Get directions" link → Google Maps URL
- Phone: (509) 960-7989 (tel: link, big and clickable)
- General email: tacos@unomastacoshop.com
- Private events: karissa@unomastacoshop.com

**Hours** (pull from Supabase `business_hours`, venue=cantina):
- Sunday — Closed
- Monday — Closed
- Tuesday — 11am – 9pm
- Wednesday — 11am – 9pm
- Thursday — 11am – 9pm
- Friday — 11am – 10pm
- Saturday — 11am – 10pm

Below hours: "Lunch service 11am–5pm · Dinner service 5pm–close"

Right column (40% width on desktop): embedded Google Map iframe centered on the Uno Más address (or static map image with link-through if simpler).

### Section 2 — Quick action cards (3-up)
- **Reserve a table** → Resy link
- **Plan an event** → karissa@unomastacoshop.com mailto
- **Press / partnerships** → tacos@unomastacoshop.com mailto

### Section 3 — Follow us
Three social icons in `#E22690` (Tabler outline):
- Instagram (ti-brand-instagram) → https://www.instagram.com/unomastacoshop
- TikTok (ti-brand-tiktok) → https://www.tiktok.com/@unomastacosandtequila
- Facebook (ti-brand-facebook) → https://www.facebook.com/UnoMasTacoShop/

### SEO
- `<title>`: "Contact Uno Más — 2020 N Monroe, Spokane | (509) 960-7989"
- meta description: "Find us, call us, or book a private event at Uno Más on Monroe in Spokane. Modern Mexican. Get a little lost."
- og:image: `role:hero-cantina`
- JSON-LD: ContactPage schema with full address, phone, geo, openingHoursSpecification

---

## BUG FIXES (do these alongside)

### Bug 1: Wrong email domain on /private-events
Currently shows `events@unomasspokane.com` — **this is not a valid domain**. Replace ALL instances on the site with the correct email: `karissa@unomastacoshop.com`

### Bug 2: Wrong email domain on /contact
Currently shows `hello@unomasspokane.com` — also not valid. Replace with: `tacos@unomastacoshop.com`

### Bug 3: Search the codebase for any remaining references to `unomasspokane.com` and replace with `unomastacoshop.com`. There may be other instances Lovable made up.

---

## ACCEPTANCE CRITERIA

After this build:
- `/about` has hero + 5 content sections + visit strip — no more "coming soon" placeholders
- `/private-events` has hero + 4 event-type cards + 3-up included + 3-step process + inquiry form/band
- `/contact` has full address, phone, both emails, embedded map, hours from Supabase, 3 social icons
- All emails use `@unomastacoshop.com` domain — zero references to `unomasspokane.com` anywhere in the codebase
- All pages use cream `#fafaf7` body, near-black text, brand pink `#E22690` for accents — matches the menu page treatment
- Mobile responsive — DevTools 375px wide passes visual review on each page
- All Cloudinary images pull via `role:*` tag queries (with fallbacks defined)
- View source on each page → proper `<title>`, meta description, og:image, JSON-LD all present

If something is ambiguous, default to the lighter / cleaner / more-pink option. Same editorial direction as the menu pages: printed brochure at a great modern restaurant, not a nightclub poster.
