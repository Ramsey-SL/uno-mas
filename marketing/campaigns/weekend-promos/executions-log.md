# Weekend Promos — Executions Log

> Real sent campaigns, captured from the Toast email PDFs Ramsey provided 2026-08-20.
> **These are executions, not standing offers** — per the handoff's own rule, treat recent
> executions as examples, not permanent rules. Verify with Toast before re-running any of them.
>
> **Channel reality:** these went out through **Toast email** (footer reads "powered by Toast"),
> not Klaviyo. `weekend-campaigns-and-flows.md` already documents Toast as the platform for the
> weekend push. Klaviyo carries the site-connected onsite/flow work.

---

## 1. "Code Word: MICKEY" — spend-threshold weekend offer

| Field | Value |
|---|---|
| Offer | **Spend $60 this weekend, get $10 off your tab** |
| Window | **Fri–Sun** |
| Applies to | Tacos, margs, dinner, Sunday brunch — "you know the drill." |
| **Redemption** | **Tell your server the code word "MICKEY."** |
| Hook copy | *"Psst. We probably shouldn't be telling you this."* / *"If you know, you know."* |
| Footer lockup | UNO MÁS ★ TACOS + TEQUILA · *Get a little lost.* |
| CTA | MAKE A RESERVATION |

**Important:** this **supersedes "Mas Please"** (the phrase the Aug 2026 handoff recorded) and the
`WEEKEND10` Toast promo code in `weekend-campaigns-and-flows.md`. The verbal code word appears to
**rotate per execution** — treat the phrase as a campaign variable, not a fixed fact. Confirm the
current word before printing or sending anything that names it.

The "code word / if you know, you know" mechanic is strong: it's an insider signal rather than a
discount announcement, which fits **belonging over bargains** far better than a coupon does.

## 2. "Weekend Special" — Two House Margs + Chip & Dip Trio

| Field | Value |
|---|---|
| Offer | **2 House Margs + Chip & Dip Trio — $30** |
| Window | **All day Fri–Sun** |
| Redemption | *"Ask your server."* |
| Copy | *"Start with the good stuff."* · *"Our fan-favorite Chip & Dip Trio"* |
| Footer | Tacos. Margs. Brunch. Get a little lost. |
| Secondary module | **Brunch — Every Sunday 10am–4pm, new brunch menu** |

## 3. "Pick Your Full Send" — bundle ladder

| Field | Value |
|---|---|
| Tier 1 | **$45 — 2 margs/palomas + any 2 shareables** |
| Tier 2 | **$65 — 4 margs/palomas + any 2 shareables** |
| Shareable choices | Chip & Dip Trio · Lula Wings · Loaded Masa Fries · Nachos |
| Fine print | **Protein add-ons extra.** |
| Window | **This weekend only** |
| Secondary module | **Brunch — Horchata French Toast, "fan-favorite brunch plate," Every Sunday 10am–4pm** |

**Note the naming collision:** the menu already has a **"Starter Trio" at $45** (Chip & Dip Trio +
Lula Wings + Loaded Masa Fries — `master-reference.md`). "Full Send" at $45 is a *different*
construct (2 drinks + choice of 2 shareables). Don't conflate them. Also note "The Full Send" is
already an **event package** name in the private-events system — a third use of the phrase. Worth
deciding whether "Full Send" belongs to the bundle or the event package.

---

## Menu items referenced — all verified present in the repo

- **Lula Wings** $18 — 1 lb, housemade Lula sauce, lime zest, cotija, fresh herbs
- **Chip & Dip Trio** — shareable
- **Loaded Masa Fries** $8 (corrected from $7, 2026-08-20)
- **Nachos** / loaded nachos
- **Horchata French Toast** $14 — brioche soaked in horchata batter, whipped cinnamon butter
- **Starter Trio** $45 — the three shareables together

## Creative system used (see `marketing/campaign-architecture.md`)

These use the **illustrated promo-card system**, not the photographic poster pattern:
- Textured cream/off-white or aged-paper ground
- Script **Uno Más** wordmark at top, often flanked by agave or starburst marks
- Condensed heavy sans headlines in navy, with the money number in **pink `#E22690`**
- **Yellow `#FFEC00`** highlight swash behind a key phrase
- **Teal `#18BCDC`** starbursts / accent rays; halftone dot shadows under illustrated food & drinks
- Illustrated (not photographed) food and cocktails — vintage letterpress/riso feel
- Footer lockup: `UNO MÁS ★ TACOS + TEQUILA` + script *Get a little lost.*

## ⚠️ Brand-name issue on a live sending surface

The Toast email footer reads **"Uno Mas Taco Shop"** — no accent, and it uses "Taco Shop," which
`CLAUDE.md` bans in brand descriptions. This is the Toast account/organization name
(`master-reference.md` §Organization name). It appears in **every marketing email Toast sends.**
Recommend renaming the Toast organization to **"Uno Más Tacos & Tequila."** Same fix already queued
for TripAdvisor. Logged in `ecosystem-registry.md` §4.
