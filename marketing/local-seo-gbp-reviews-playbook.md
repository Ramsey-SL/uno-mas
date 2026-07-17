# Uno Más — Local SEO: Google Business Profile + Reviews Engine Playbook

**Date:** 2026-06-29 · **Owner:** Ramsey · Managed by Strategy Labs
**Why this matters:** the on-page SEO is done (see [seo-page-briefs.md](seo-page-briefs.md) + [paid-search-and-seo-keyword-plan.md](paid-search-and-seo-keyword-plan.md)), but the **highest-demand local terms — "best restaurants in spokane," "mexican restaurant spokane," "restaurants near me" — are won in the Google Map Pack, not on the website.** The Map Pack is driven by **Google Business Profile (GBP) completeness + review volume/velocity/recency + NAP consistency.** This is that program. Most steps happen in the GBP dashboard and your review pipeline, not in code.

---

## 0. Current state (diagnosis, 2026-06-29)

| Signal | State | Action |
|---|---|---|
| GBP for 2020 N Monroe | Exists (aggregators like Wanderlog pull it) but **Place ID unconfirmed + likely unclaimed/unoptimized** | **Claim + verify + optimize (Part A/B)** |
| Old Spokane Valley listings | **Stale "Uno Más Taco Shop — CLOSED"** at 835 N Post St & 11205 E Dishman Mica Rd (Yelp; likely GBP too) | **Mark permanently closed / merge — duplicates dilute ranking** |
| Yelp (Monroe) | Live, ~16 reviews | Claim + maintain (Part D) |
| TripAdvisor | Under old name **"Uno Mas Taco Shop," unclaimed** | Claim + rename + fix NAP (Part D) |
| AggregateRating schema | **Intentionally absent on site** (no verified count) | Add ONLY after a real, stable Google rating exists — never fabricate |

> **Canonical NAP — must be byte-identical everywhere (matches the live JSON-LD I deployed):**
> **Name:** Uno Más Tacos & Tequila · **Address:** 2020 N Monroe St, Suite C, Spokane, WA 99205 · **Phone:** (509) 960-7989 · **Web:** https://unomastacoshop.com · **Hours:** Tue–Thu 11am–9pm, Fri–Sat 11am–10pm, Sun 10am–4pm (Sunday Brunch + lunch), Mon closed.

---

## Part A — Claim, verify & de-duplicate the GBP (do first)

1. **Find/confirm the listing & Place ID.** Go to [business.google.com](https://business.google.com) signed in as the owner account. Search "Uno Más Tacos & Tequila, 2020 N Monroe." Also get the **Place ID** via the [Place ID Finder](https://developers.google.com/maps/documentation/places/web-service/place-id) (search the business, copy the ID) — record it in SITE-STATUS.md and the website memory (it's still listed as unconfirmed).
2. **Claim it.** If "Own this business?" appears → claim. **Verify** (video call is now most common for restaurants — have signage, the storefront, and the kitchen ready; postcard/phone are fallbacks). This unlocks everything below.
3. **Kill the duplicates.** Find the old Spokane Valley entries (835 N Post St; 11205 E Dishman Mica Rd). Mark each **"Permanently closed"** (or request merge if any duplicates the *Monroe* address). Two live "Uno Más" pins in one metro split your reviews and ranking signal — this is a real, fixable drag.
4. **Set the opening date** to **December 27, 2024** (Monroe flagship) so Google models tenure correctly.

---

## Part B — Optimize the GBP (the ranking surface)

### Categories (biggest single ranking lever after claiming)
- **Primary:** `Mexican restaurant`
- **Secondary** (add all that GBP offers): `Taco restaurant` · `Cocktail bar` · `Bar` · `Caterer` · `Event venue` · `Restaurant`
  *(`Caterer` unlocks "catering spokane"; `Event venue` unlocks "event venue/space spokane" — Map-Pack terms the website can only support.)*

### Business description (paste verbatim — ≤750 chars, no phone/URL per Google rules)
> Uno Más is a modern Mexican restaurant and tequila bar on North Monroe in Spokane, five minutes north of downtown and behind Indaba Coffee. We started as a taco shop in 2022 and opened our Monroe flagship in 2024 — a converted mechanic's garage with three spaces under one roof: the Cantina on the main floor, the Mezzanine speakeasy upstairs, and a seasonal patio. Quarter-pound tacos, birria, house-smoked carnitas, burritos and bowls, plus a full craft cocktail and tequila program — try the Espresso Margarita with Indaba cold brew. Lunch and dinner Tuesday through Saturday. Private events, off-site catering, and a full bar. Walk-ins welcome; reservations on Resy. Get a little lost.

### Attributes (check these on)
- **From the business:** Identifies as locally owned (if offered) · Owner-operated
- **Service options:** Dine-in ✓ · Takeout ✓ · **Delivery ✗** (you don't deliver — leave OFF) · No-contact ✗
- **Offerings:** Cocktails · Beer · Wine · Hard liquor · Coffee · Vegetarian options · Vegan options · Late-night food (Fri/Sat) · Small plates · Quick bite (lunch)
- **Dining options:** Lunch · Dinner · Dessert · Seating · Catering
- **Amenities:** Bar onsite · Gender-neutral restroom (if true) · Wi-Fi (if offered) · Dogs allowed (patio, if true)
- **Crowd/Planning:** Family-friendly (until 9pm) · Groups · Accepts reservations · Accepts walk-ins
- **Parking:** Free parking lot / Free street parking
- **Children:** Good for kids (until 9pm) · High chairs (if available)
- **Payments:** Credit cards · Debit · NFC mobile payments

### Products (add with photos + prices — these show in the listing)
Carne Asada $37 · Surf & Turf $47 · Birria Tacos $14 · The Uno Más Feast $129 (feeds 2–3) · The 509 burrito $23 · Espresso Margarita $15 (Indaba cold brew). *House-smoked carnitas. Vegan: Batata & Hongos.*

### Services
- **Catering** — "Off-site taco & Mexican catering across Spokane, Spokane Valley, Liberty Lake, and Coeur d'Alene."
- **Private events** — "The Mezzanine speakeasy (up to 28 seated), patio takeovers, and full cantina buyouts."

### Links
- **Website:** https://unomastacoshop.com  · **Menu:** https://unomastacoshop.com/menu  · **Reservations:** the Resy link  · **Catering/Events:** https://unomastacoshop.com/private-events
- Turn on **Messaging** only if someone monitors it (slow replies hurt ranking).

### Photos (Google weights fresh photos heavily — aim for a steady drip, not a dump)
Cover: the converted-garage cantina interior. Logo: agave-on-navy. Then categories: **Food** (tacos, birria, Surf & Turf, the Feast), **Drink** (Espresso Margarita, margs), **Interior** (Cantina, the Mezzanine), **Exterior** (storefront/signage behind Indaba), **Team**. Add ~3–5 new photos/week from the DAM. Geotag-fresh owner photos > stock.

### Seed the Q&A (post these as the owner, then answer from the business account)
- "Where is Uno Más?" → "2020 N Monroe St, Suite C — five minutes north of downtown, behind Indaba Coffee. Parking on site."
- "Do you take reservations?" → "Yes, on Resy — especially Fri/Sat, the Mezzanine, and larger groups. Walk-ins always welcome."
- "Do you cater?" → "Yes — taco & Mexican catering across Spokane, the Valley, Liberty Lake, and Coeur d'Alene. Email karissa@unomastacoshop.com."
- "Is there a private event space?" → "The Mezzanine speakeasy seats 28, plus patio takeovers and full buyouts. karissa@unomastacoshop.com."
- "Are there vegan options?" → "Yes — the Batata (sweet potato) and Hongos (portabella) tacos can be made vegan."
- "Is it kid-friendly?" → "Yes until 9pm. After 9pm the room is 21+ by design."

### GBP Posts (publish weekly — keeps the profile 'active', a ranking signal). First batch:
1. **Taco Tuesday** (recurring, post Mondays): "Taco Tuesday on North Monroe — BOGO lunch street tacos, $6 margs, $30 marg pitchers. Every Tuesday at 2020 N Monroe." → button **Order/Reserve**.
2. **Espresso Margarita:** "Tequila blanco, Indaba cold brew, Baileys, agave. The Espresso Margarita — $15, made with the roaster behind the building." → **Learn more** → /mezzanine.
3. **Private events:** "Your group deserves its own room. The Mezzanine speakeasy seats 28 — rehearsal dinners, birthdays, corporate nights." → **Learn more** → /private-events.
4. **Catering:** "We bring the taco bar to you — across Spokane, the Valley, and Coeur d'Alene." → **Learn more** → /catering.
5. **Dinner:** "Dinner worth the table — Carne Asada, Surf & Turf, the $129 Feast. Tue–Sat." → **Reserve** → Resy.

---

## Part C — The reviews engine (what actually wins "best…spokane")

Map-Pack ranking for reputation terms = **review count + velocity + recency + your responses.** Build a repeatable ask; never buy or fake reviews; never add AggregateRating schema until a real rating is stable.

### 1. Get the Google review short-link
After claiming: GBP dashboard → **"Ask for reviews"** / "Get more reviews" gives a short link like `https://g.page/r/XXXX/review`. (Or build `https://search.google.com/local/writereview?placeid=PLACE_ID` with the Place ID from Part A.) **This link is the destination for every ask below.** Make a QR code of it for table tents/receipts.

### 2. Automate the ask (you have the tools)
- **Toast** (POS, ties to Cantina Club): trigger a **post-visit** email/SMS to checked-in loyalty guests.
- **Klaviyo** (connected): a **post-dine flow** — 2–24 hrs after a visit/loyalty event → send the ask → route to the Google link. *(I can draft/stage the Klaviyo email + SMS templates for you — say the word.)*
- **In-person:** QR table tents + "Loved it? A Google review makes our day — [QR]" on receipts. Staff ask at the check drop for tables that were clearly happy.

### 3. Ask copy (drafted, brand voice)
- **SMS (≤160):** "Glad you came by Uno Más 🌮 If we did it right, a quick Google review means the world to a locally owned spot: [link]"
- **Email subject:** "One more thing… 🌮"  **Body:** "Thanks for hanging with us at Uno Más. We're locally owned on North Monroe, and Google reviews are how Spokane finds us. If you had a good time, 30 seconds here goes a long way: [Review on Google]. See you for the next round. — The Uno Más Team"
- **Targeting:** route *happy* guests (loyalty repeat visit, high check, or a thumbs-up micro-survey) to Google; route any *unhappy* signal to a private "tell us what happened → karissa@" path first. (Don't gate reviews, but don't aim a bad night at your public profile.)

### 4. Respond to every review (responses are a ranking + trust signal) — templates, <100 words, signed "The Uno Más Team"
- **5-star:** "This is the stuff. Thank you for hanging with us — come find the Mezzanine upstairs next time. See you soon. — The Uno Más Team"
- **4-star:** "Appreciate you, and the honest read. We want the next one to be a 5 — come back and let us prove it. — The Uno Más Team"
- **1–3 star:** "Thank you for telling us — this isn't the night we want anyone to have. We'd genuinely like to make it right: karissa@unomastacoshop.com. — The Uno Más Team" *(warm, specific, never defensive)*

### 5. Cadence & goal
Steady beats spiky (Google flags review bursts). Target **~10–20 new Google reviews/month**, responded to within 48 hrs. Watch the count/velocity in GBP Insights.

---

## Part D — Citations & NAP consistency (stop diluting the signal)

Build/claim and make **byte-identical to the canonical NAP** above:
- **Yelp** (Monroe) — claim, complete, add menu + photos; respond to reviews.
- **TripAdvisor** — claim and **rename from "Uno Mas Taco Shop" → "Uno Más Tacos & Tequila,"** fix NAP.
- **Apple Business Connect** (Apple Maps), **Bing Places** — claim + complete (Siri/Apple Maps + Bing/ChatGPT pull these).
- **Data aggregators** (Data Axle, Foursquare) + **Restaurantji/Wanderlog** — correct NAP where editable.
- **Wedding/event directories** (The Knot, WeddingWire, Eventective, Peerspace) + **Visit Spokane** — backlinks + referral for the events/catering terms.
- **Kill stale Valley citations** that still show old addresses/the "Taco Shop" name.

---

## Part E — Measurement & the payoff loop
- **GBP Insights:** track searches (discovery vs direct), calls, direction requests, website clicks, review count/rating monthly.
- **Tie-back to the master plan:** as the GBP climbs the Map Pack for "best/mexican restaurant spokane," apply the **§1 "bid-until-we-rank" throttle** — pull the matching Google Ads spend down as you start winning the local pack organically.
- **Then, and only then,** add `AggregateRating` JSON-LD to the site (home/about) using the *real* Google count+value — this lights up star ratings in search.

---

## ⚡ First 48 hours (do these in order)
1. Claim + start verification of the Monroe GBP; record the **Place ID**.
2. Mark the **old Valley listings permanently closed**.
3. Set **primary + secondary categories** and paste the **business description**.
4. Grab the **Google review short-link** + make a QR.
5. Turn on the **Klaviyo/Toast review-ask** (I can stage the templates).
6. Post **GBP Post #1 (Taco Tuesday)** and add 5 fresh food photos.

*Companion docs: [seo-page-briefs.md](seo-page-briefs.md) · [paid-search-and-seo-keyword-plan.md](paid-search-and-seo-keyword-plan.md). On-page SEO deployed & verified live 2026-06-29; this off-page layer is what wins the reputation/Map-Pack terms the pages can only support.*
