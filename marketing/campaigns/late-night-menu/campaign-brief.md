# Late Night Menu — Brief

**Type:** new recurring daypart · **Status:** 🟢 **RULED FRI + SAT ONLY (2026-08-23)** — mockup matches, ready to produce
**Owner:** Ramsey · **Target launch:** week of 2026-08-24 · **Created:** 2026-08-23

---

## ✅ RESOLVED 2026-08-23 — FRI + SAT ONLY

**Ramsey ruled Friday and Saturday only.** No hours change, no propagation to GBP/Apple/Yelp/Resy needed.
The mockup was already built for Fri–Sat, so it ships as-is. Option 1 below was taken.

### Why the constraint existed

Canonical hours (Supabase `business_hours`, matching the live site's JSON-LD):

| Day | Close | Does 8–10pm fit? |
|---|---|---|
| Mon | closed | ✗ |
| **Tue** | **8:00pm** | ✗ — closes exactly when late night starts |
| **Wed** | **8:00pm** | ✗ |
| **Thu** | **8:00pm** | ✗ |
| **Fri** | 10:00pm | ✅ |
| **Sat** | 10:00pm | ✅ |
| Sun | 4:00pm | ✗ |

**As written, this menu can only run Friday and Saturday.** Three options:

1. **Fri–Sat only** — launch as-is, no operational change. Fastest. Also the two nights with the most late traffic to convert.
2. **Extend Tue–Thu to 10pm** — makes it a five-night program, but it's a labor and staffing decision, and it changes hours on Supabase, the site, GBP, Apple, Yelp, and Resy. The agent can propagate that in one pass once you decide.
3. **Shift the window to 7–9pm Tue–Thu** and 8–10pm Fri–Sat — captures the slow midweek hour without extending close. More complex to communicate.

**✅ Option 1 chosen.** Prove late-night demand on Fri/Sat first, where the traffic already exists. Option 3 (7–9pm midweek) remains the natural follow-up test once there's data.

## The offer

| Item | Price |
|---|---|
| House Margarita | **$6** |
| Margarita Pitcher | **$30** |
| Paloma | **$8** |
| **Pick any two street tacos** | **$10** |

**Taco proteins — all street tacos except Camaron (shrimp), per Ramsey:**

| Protein | Description |
|---|---|
| Carne Asada | Marinated steak + salsa roja + white onion + cilantro + queso fresco |
| Al Pastor Chicken | Grilled chicken + pineapple + salsa verde + cilantro |
| Carnitas | House smoked pork + Monterey Jack + pickled onion + cilantro + salsa verde |
| Barbacoa | Braised chuck + salsa verde + cilantro + pickled red onion |
| Batata *(vegan-able)* | Grilled sweet potato + Monterey Jack + pickled onion + cilantro + salsa aguacate |
| Hongos *(vegan-able)* | Chile roasted portabella + Monterey Jack + spicy roja + cilantro + pickled daikon + tomatillo + shaved radish |

⚠️ **Camaron (shrimp) excluded** — confirm with the kitchen that it's excluded for cost/holding reasons and that staff know to say so plainly rather than "we're out."

## Pricing conflicts to resolve before launch

1. **$10 for two street tacos vs. $6.50 each.** Two tacos à la carte is $13, so this is a **$3 discount (23%)**. Fine — but note the existing *2 Street Tacos + Side* combo is **$16.50**. A guest could reasonably ask why two tacos are $10 late and $16.50 with a side. Make sure staff can answer: *the late-night price is tacos only, no side.*
2. **$10 already means "one Big A** taco."** Big A** ¼lb tacos are $10 each. Two price points at $10 for different things on the same menu invites confusion at the table. Consider calling the late-night item **"Two Street Tacos — $10"** explicitly, never just "$10 tacos."
3. **$6 margs is Taco Tuesday's price.** If margs are $6 every Fri–Sat late night, Taco Tuesday's marg deal stops being special. Either accept that ($6 becomes the recognizable "deal price" across programs — arguably good, it's memorable), or move late night to $7 to protect Tuesday. **Recommend accepting it** — one memorable price beats two competing ones, and Tuesday's real hook is BOGO tacos, not the marg.
4. **Paloma at $7** — confirm against the current cocktail menu price so the discount is real and staff can state it.

## Strategic role

Per `campaign-architecture.md`: this is a **visit-frequency** play on the **Get a Little Lost**
platform — the whole point of that platform is "came in for tacos, stayed longer than planned," and a
late-night menu is the literal mechanism. It also creates a **new occasion** (after-dinner, post-event,
industry crowd) rather than discounting an existing one, which is the right kind of program.

**Ladder position:** rung 3 — a reason to return for a *different* occasion. Capture the guest in
Toast so it can feed a late-night segment later.

## Copy

**Menu header:** LATE NIGHT · FRI + SAT · 8–10PM
**Tagline line:** The kitchen's still going. So are we.
**Social/SMS:** `Late night is on. Fri + Sat, 8–10pm. Two street tacos $10, margs $6, palomas $8, pitchers $30. Get a little lost.`
**Table tent:** *Not done yet? Good. Late night starts at 8.*

Voice check: short, price-confident, no "perfect for any occasion," no apology for the deal.

## Collateral

- ✅ `late-night-menu-mockup.html` — print/table-tent mockup, 1080×1350
- ⬜ Social 4:5 + story 9:16 (illustrated promo-card system)
- ⬜ Add to the site's menu system as a daypart (`menu_sections`/`menu_items` support dayparts already)
- ⬜ GBP post + Klaviyo/Toast send once dates are locked
