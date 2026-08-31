# Weekend Promos — Executions Log

> **Weekend offers are a rotating WEEKLY TEST, not standing offers.** Each one runs a weekend, then
> is replaced. Confirm what's live here before writing any weekend copy — and never resurrect a
> retired offer's creative without checking.
>
> Captured from the Toast email PDFs Ramsey provided 2026-08-20, plus his verbal history 2026-08-23.
>
> **Channel reality:** these go out through **Toast email** (footer reads "powered by Toast"), not
> Klaviyo. Klaviyo carries the site-connected onsite/flow work.

---

## 🏷 The franchise: **The Weekly Promo Drop** (named 2026-08-25)

Tests 1–3 each launched cold with no connective tissue. From test 4 on, the rotating offer lands in
a **named recurring slot**: announced Tuesday (program only, no detail), revealed Wednesday, runs
Wed–Sun. See `campaign-architecture.md` §4c. **"Drop" not "flash"** — a flash implies hours, these
run five days, and an overpromising word stops meaning anything by week three.

## Test sequence — chronological

| # | Offer | Window | Status |
|---|---|---|---|
| 1 | **Spend $60, get $10 off** — code word `MICKEY` | ~Aug 14–17 | 🔴 **OVER** — the first test |
| 2 | **2 House Margs + Chip & Dip Trio — $30** | mid-Aug weekend | 🔴 **OVER** |
| 3 | **Pick Your Full Send — $45 / $65** | **Aug 22–24** | 🟡 **RUNNING** (this weekend) |
| 4 | **Gift card bounce-back** — $50→$10, $100→$20 (physical card at checkout) | **offer Wed Aug 26 → Sun Aug 30 · marketing launch Thu Aug 27** | 🔴 **OVER — reported SUCCESSFUL by Ramsey 2026-08-31.** Spans the weekend, so it **is** the Aug 28–30 weekend test. Overlaps the Late Night launch (Fri Aug 28); offers stack. See `campaigns/gift-card-bounceback-aug2026/` |

## 📈 The pattern — each test moves further from discounting

This is the most useful thing in this log. Read the sequence as a deliberate progression:

| # | Structure | What it costs you |
| 5 | **Two Margs + A Dip — $25** (2 house margs + chips & guac or queso) | **Wed 2 Sep → Sun 6 Sep** | 🔵 **PROPOSED** — review package in `campaigns/marg-dip-drop-sep2026/`. Carries a hard Late Night carve-out: margs are $6 Fri/Sat 8–10pm, which makes a $25 bundle cost the guest $5 *more* than the menu in that window. |
|---|---|---|
| 1 | **Straight discount** — $10 off a $60 check | Full margin hit, immediately, on a visit that was already happening |
| 2 | **Fixed bundle** — 2 margs + a shareable at $30 | Discounted, but it *builds a bigger check* and pushes a specific high-margin pairing |
| 3 | **Bundle ladder** — $45 / $65 tiers | Same, plus a reason to trade **up** rather than stop at the first tier |
| 4 | **Deferred credit** — gift card, not a discount | **First visit at full margin.** Cost only lands on a return visit, and breakage works in your favor |

**Each step protects more margin than the last while still reading as generous.** Test 4 is the
strongest structure of the four and is the natural default to beat going forward.

**What to measure** (per `toast-lifecycle-automation-playbook.md` — incremental visits, not opens):
- **Average check** on the offer vs. the same weekday without it
- **Redemption rate** — how many actually hit the threshold
- **For #4 specifically: return rate.** How many gift cards come back, and what the *second* check averages. That's the number that decides whether bounce-backs become the standing weekend structure.
- **Attach rate** on bundles (#2, #3) — did they add the shareable, or swap it for something they'd have ordered anyway?

Without this, you're running four experiments and learning nothing from any of them. **Recommend
logging check-average and redemption for the three completed tests before test 4 starts Wednesday**
— the Toast dashboard at `~/projects/unomas-toast-dashboard` is the tool, though note its API
credentials currently fail auth (registry §4).

---

## Execution detail

### 1. "Code Word: MICKEY" — spend-threshold weekend offer 🔴 OVER (first test)

| Field | Value |
|---|---|
| Offer | **Spend $60 this weekend, get $10 off your tab** |
| Window | **Fri–Sun** |
| Applies to | Tacos, margs, dinner, Sunday brunch — "you know the drill." |
| **Redemption** | **Tell your server the code word "MICKEY."** |
| Hook copy | *"Psst. We probably shouldn't be telling you this."* / *"If you know, you know."* |
| Footer lockup | UNO MÁS ★ TACOS + TEQUILA · *Get a little lost.* |
| CTA | MAKE A RESERVATION |

**Confirmed over as of 2026-08-23.** This **supersedes "Mas Please"** (the phrase the Aug 2026 handoff recorded) and the
`WEEKEND10` Toast promo code in `weekend-campaigns-and-flows.md`. The verbal code word appears to
**rotate per execution** — treat the phrase as a campaign variable, not a fixed fact. Confirm the
current word before printing or sending anything that names it.

The "code word / if you know, you know" mechanic is strong: it's an insider signal rather than a
discount announcement, which fits **belonging over bargains** far better than a coupon does.

### 2. "Weekend Special" — Two House Margs + Chip & Dip Trio 🔴 OVER

| Field | Value |
|---|---|
| Offer | **2 House Margs + Chip & Dip Trio — $30** |
| Window | **All day Fri–Sun** |
| Redemption | *"Ask your server."* |
| Copy | *"Start with the good stuff."* · *"Our fan-favorite Chip & Dip Trio"* |
| Footer | Tacos. Margs. Brunch. Get a little lost. |
| Secondary module | **Brunch — Every Sunday 10am–4pm, new brunch menu** |

### 3. "Pick Your Full Send" — bundle ladder 🟡 RUNNING (Aug 22–24)

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
