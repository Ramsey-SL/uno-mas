# Meta Ads — Taco Tuesday

**Created 2026-08-25** · Format follows `campaigns/2026-04-dinner-launch/creative/copy/ad-copy.md`
**Voice rule applied:** paid ads are *hook-driven, clarity first — 60% clever max* (`CLAUDE.md`).
All character counts verified.

---

## 🔴 Read this before launching: two offers, two dayparts

Taco Tuesday is really **two offers with different windows**, and running them as one ad wastes money:

| Offer | Window | Implication |
|---|---|---|
| **BOGO street tacos** | **till 5pm** — lunch only | Ads must **stop delivering at 5pm**, or you're paying to advertise an expired offer |
| **$6 margs · $30 pitchers** | **all day** | Can run to close |

**Set up two ad sets, not one.** Use Meta's **dayparting** (Ad Set → Budget & Schedule → Run ads on a schedule):
- **Ad set 1 — BOGO:** Tuesdays only, roughly **9am–4pm**. Cut at 4 so you're not paying for clicks that arrive after the offer ends.
- **Ad set 2 — Margs/pitchers:** Tuesdays only, **11am–9pm**.

A single always-on ad saying "BOGO till 5pm" delivered at 8pm is the most common way small restaurant budgets get wasted.

**Targeting:** Spokane + ~8–10 mi radius. Don't go broader — this is a walk-in lunch offer and you have one location.
**Pixel:** `1737601003250529` is installed. Optimize for **landing page views** to start; you have no purchase event on-site, so conversion optimization has nothing to learn from.
**Destination:** `unomastacoshop.com` — the Taco Tuesday tile is live on the homepage every Tuesday, so the ad and the landing page now match. *(That matters: sending offer traffic to a page that doesn't mention the offer is the other common waste.)*

---

## Feed — 1080×1080 or 1080×1350

### Variant A — The BOGO math *(lead with this for the lunch ad set)*
**Hook angle:** the offer is the hook; no cleverness needed in front of it.

**Primary text**
```
Two tacos. One price. Every Tuesday.

BOGO street tacos till 5pm. Carne asada, al pastor chicken, carnitas, barbacoa. Corn tortillas, cilantro, onion, salsa.

2020 N Monroe. Walk right in.
```
*(188 chars · first line 36 — lands well inside the ~125 visible before "See more")*

**Headline:** `Two tacos. One price.` *(21/27 ✓)*
**Description:** `BOGO till 5pm. Every Tuesday.` *(29/30 ✓)*
**CTA:** `Learn More`

---

### Variant B — The price contrast *(strongest for the all-day ad set)*
**Hook angle:** the number people don't expect. A $12.50 marg at $6 is a 52% cut — that's genuinely notable, so state it plainly rather than dressing it up.

**Primary text**
```
The $12.50 margarita is $6 today.

So is every other Tuesday. House marg, on the rocks, salt, lime. Pitchers $30 instead of $50.

All day. 2020 N Monroe, Spokane.
```
*(162 chars · first line 33)*

**Headline:** `Margs are $6 today.` *(19/27 ✓)*
**Description:** `Every Tuesday. All day.` *(23/30 ✓)*
**CTA:** `Learn More`

---

### Variant C — The ritual *(best for retargeting people who've already visited)*
**Hook angle:** habit, not discount. Fits *belonging beats bargains* — this is the one to show people who already know you.

**Primary text**
```
Your Tuesday already has a plan.

BOGO street tacos till 5pm. $6 house margs and $30 pitchers all day. Every single Tuesday, no catch, no code.

2020 N Monroe.
```
*(159 chars · first line 32)*

**Headline:** `Tuesday has a plan.` *(19/27 ✓)*
**Description:** `BOGO tacos. $6 margs.` *(21/30 ✓)*
**CTA:** `Learn More`

---

### Variant D — The group play *(run this against larger-party / group interests)*
**Hook angle:** pitchers are the highest-ticket item in the offer and the one that brings four people instead of one.

**Primary text**
```
$30 for a pitcher of margaritas.

Normally $50. Every Tuesday, all day. Bring four people or don't - we're not counting.

Uno Más, 2020 N Monroe. Behind Indaba.
```
*(160 chars · first line 32)*

**Headline:** `$30 marg pitchers.` *(18/27 ✓)*
**Description:** `Every Tuesday, all day.` *(23/30 ✓)*
**CTA:** `Learn More`

---

## Story / Reels — 1080×1920

**Variant E — stacked offer, no cleverness.** Stories get a second of attention; the offer has to be the whole message.

**Primary text**
```
BOGO street tacos till 5pm
$6 margs all day
$30 pitchers all day

Every Tuesday.
```
**Headline:** `Taco Tuesday.` *(13/27 ✓)*
**CTA:** `Learn More`

Use the **1080×1920 Late Night-style photo treatment** — taco photo, dark scrim, offer stacked over it. Asset: `20260125_UM_FOOD_TacoCloseUpV10_FINAL` with the house grade.

---

## Creative to pair with these

Per `campaign-architecture.md` §4b, **photo-led** — these promote food, so lead with the food.
- **Approved, print-safe hero:** `20260125_UM_FOOD_TacoCloseUpV10_FINAL` (2560px native, not `needs-hires-swap`)
- Alternates: `20260125_UM_FOOD_FoodOnTable_FINAL` · `20260207_UM_DRINK_PitcherAndMarg_FINAL` (for D)
- House grade: `e_saturation:18,e_contrast:10,e_brightness:4`, `c_fill,g_auto`

⚠️ **Meta strips most text overlays from consideration in some placements and penalizes heavy text.** Keep in-image text to the offer only — the copy above does the explaining.

---

## Copy checks applied

- Hook-driven, clarity first, ≤60% clever ✓
- No banned words (`authentic Mexican`, `mouthwatering`, `culinary journey`, `artisanal`, `mixology`, `perfect for any occasion`) ✓
- "Uno Más" with the accent in all human-readable copy ✓
- **"till", not "til"** ✓
- Exact prices and the exact cutoff stated in every variant ✓
- No "BOGO" without "till 5pm" attached — the two must never be separated, or the ad promises an all-day offer that isn't

## What to measure

Not clicks. **Tuesday covers versus the prior three Tuesdays**, and Tuesday's average check. Per
`toast-lifecycle-automation-playbook.md`, judge on incremental visits. Set a modest budget, run four
Tuesdays, then compare — one Tuesday tells you nothing.

## Open

- **Which ad account?** The Meta Ads connector is authorized; say the word and I'll pull the account, existing campaigns, and past creative performance so these can be built against what's already worked rather than from scratch.
- **Budget and duration** — needs a number before I can size ad sets.
