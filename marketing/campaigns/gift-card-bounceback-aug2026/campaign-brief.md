# Gift Card Bounce-Back — Campaign Brief

**Type:** promotion (limited window) · **Status:** 🟢 **STARTS WED 2026-08-26** — outline + mockups built, Toast setup to confirm
**Owner:** Ramsey · **Created:** 2026-08-23

---

## The offer

| Spend | Get | Effective value |
|---|---|---|
| **$50** | **$10 gift card** | 20% back |
| **$100** | **$20 gift card** | 20% back |

Flat 20% at both tiers, which keeps the math easy to explain at the table and easy for staff to
remember. The $100 tier gives a reason to add a shareable or a pitcher rather than stopping at $50.

## Why this mechanic is better than a discount

Worth saying plainly, because it changes how you should talk about it:

1. **The first visit is at full margin.** Nothing is discounted. You're issuing future credit, not
   giving money back today.
2. **It buys a second visit.** The reward is only realized when they come back — which is exactly
   the ladder rung the whole system is built around (`campaign-architecture.md` §2, rung 3).
3. **Breakage works for you.** A meaningful share of gift cards never get fully redeemed. A $10-off
   coupon has 100% cost; a $10 gift card does not.
4. **Gift cards walk out the door as gifts.** Some get handed to someone who has never been in. That
   is acquisition you don't pay for twice.
5. **It reads as generous, not desperate.** "Here's $20" lands better than "20% off," and it fits
   *belonging beats bargains* far better than a discount blast.

**So the copy should say "we're giving you $10," never "save $10."**

## ⚠️ Conflicts to resolve before launch

1. ~~**The $10-off-$60 weekend offer conflict.**~~ ✅ **RESOLVED 2026-08-23 — that offer is OVER.**
   It was the first of a rotating weekly weekend test. No stacking risk. The **Full Send $45/$65**
   test is running the weekend of Aug 22–24 and ends before this starts.
2. **Late Night launches next week** with $6 margs / $10 two-taco. Overlapping a spend-threshold
   promo with a discounted daypart compresses margin on the same ticket.
   **Recommend:** run the gift card promo **this week**, launch Late Night **next week**, don't overlap.
3. ✅ **Dates: starts Wednesday 2026-08-26.** End date still needed — see the open question below.

   ⚠️ **Overlap to decide.** Starting Wednesday means this is the first offer that is **not**
   weekend-scoped, and if it runs past Thursday it lands on top of two things:
   - the **weekend of Aug 28–30**, where a new rotating weekend test would normally run
   - **Late Night launching Fri Aug 28** ($6 margs, two tacos $10)

   A guest could hit the $50 threshold on discounted Late Night items and still take a $10 gift
   card. That's not fatal — the gift card is deferred credit, not a discount — but it does compress
   margin on the same ticket. **Three options:**
   1. **Wed–Thu only** (Aug 26–27). Clean, protects the Late Night launch, and lifts the two
      genuinely slow nights. **Recommended.**
   2. **Wed–Sun** (Aug 26–30). More volume, but it doubles up on the Late Night launch weekend and
      displaces this week's weekend test.
   3. **Wed–Sun, excluding Late Night items.** Cleanest on margin, worst to explain at the table.
      Avoid — a threshold offer with carve-outs invites arguments.
4. **Per-check or per-visit?** One gift card per check is the standard guard. Without it, a table can
   split checks to farm the reward. **Recommend: one per check, pre-tax subtotal, dine-in and takeout.**
5. **Alcohol-only checks.** WA rules around promotions tied to alcohol purchases are worth a
   sanity-check with your distributor rep or attorney before promoting a spend threshold that could
   be met entirely with drinks. **Flagging, not advising** — confirm before launch.

## Mechanics — the details staff and Toast need

- **Threshold:** pre-tax subtotal, before any other discount.
- **Issued:** at checkout, physical gift card handed over with the receipt.
- **Redeemable:** on a **future** visit — not the same check. This is the whole point.
- **Expiry:** none. WA law restricts gift-card expiration; **do not print an expiry date.**
- **Stacking:** not combinable with other offers (see conflict 1).
- **One per check.**

**Toast setup:** this is not a discount, so don't build it as one. It's a manual gift-card
activation at checkout triggered by the check total. The cleanest path is a staff-facing rule plus
an existing physical gift-card SKU. Confirm the flow with whoever manages Toast config — the
Aug 2026 work on Toast discount/promo redemption flow is relevant prior art.

**Tracking:** tag the activations so you can measure the thing that matters — **how many of those
gift cards come back, and what the return check averages.** Opens and redemptions are the metric;
not sends. Review at 30 days (`toast-lifecycle-automation-playbook.md`).

## Staff script

> "Your total's $52 — that hits our gift card deal, so here's a $10 gift card for next time.
> No expiration, just bring it back."

Rules for the floor:
- Say **"here's $10"** — not "you saved."
- Mention it at **greet** for tables likely to land near $50: *"heads up, spend $50 tonight and we'll
  hand you a $10 gift card."* That's what moves an add-on order.
- At **$40–49**, offer the nudge once, lightly: *"you're $8 from a $10 gift card if you want a
  shareable."* Once. Never pushy.
- Do **not** tie it to reviews. Ever.

## Channels

| Channel | Asset | Note |
|---|---|---|
| **Toast email** | 4:5 promo card | Primary — this is how the Aug weekend promos went out |
| **SMS** | text only | Keep to one segment. Lead with the offer. |
| **Instagram / Facebook feed** | 4:5 promo card | |
| **Stories** | 9:16 | |
| **In-restaurant** | table tent | Highest-converting surface for a threshold offer — the decision happens at the table |
| **GBP** | Post using the 4:5 | |

## Copy

**Email subject A:** `Spend $50, we'll hand you $10.`
**Email subject B:** `Here's $20 for next time.`
**Preview text:** `Gift card on us, this week only. No expiration, no catch.`

**SMS (one segment):**
`Uno Más: Spend $50 this week, get a $10 gift card. Spend $100, get $20. On us, for next time. Tue-Sun.`

**Social caption:**
> We're not discounting anything. We're just giving you money for next time. 💸
> Spend $50 → **$10 gift card.** Spend $100 → **$20 gift card.**
> This week only, Tue–Sun. No expiration. Bring it back whenever.
> Get a little lost.

**Table tent:** *Spend $50 tonight. Take $10 with you.*

## Collateral

- ✅ `gift-card-promo-mockups.html` — 4:5 feed card, 9:16 story, and table tent, all three artboards
- ⬜ Toast email build (use Canva Email Module System `DAHINHHZJng`)
- ⬜ Confirm dates, then GBP post + Toast send
