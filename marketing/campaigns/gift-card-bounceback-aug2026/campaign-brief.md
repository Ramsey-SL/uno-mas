# Gift Card Bounce-Back — Campaign Brief

**Type:** promotion (limited window) · **Status:** 🟢 **LOCKED — Wed 2026-08-26 → Sun 2026-08-30** · physical gift card at checkout
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
3. ✅ **Dates LOCKED: Wed Aug 26 → Sun Aug 30.** Five days, ending Sunday so it captures brunch.

   **Overlap with Late Night accepted (Ramsey's call).** Late Night launches Fri Aug 28, so Fri/Sat
   run both. A guest can hit $50 on discounted Late Night items and still earn a $10 gift card.
   That's a real double-up on the same ticket — but the gift card is **deferred credit, not a
   discount**, so the Fri/Sat check still lands at full margin today. The cost moves to a future
   visit, which is the point.
   **Consequence:** this promo IS the weekend test for Aug 28–30 (test 4 in
   `campaigns/weekend-promos/executions-log.md`). Don't schedule a separate weekend offer on top —
   three offers on one ticket is where margin actually breaks.
4. **Per-check or per-visit?** One gift card per check is the standard guard. Without it, a table can
   split checks to farm the reward. **Recommend: one per check, pre-tax subtotal, dine-in and takeout.**
5. **Alcohol-only checks.** WA rules around promotions tied to alcohol purchases are worth a
   sanity-check with your distributor rep or attorney before promoting a spend threshold that could
   be met entirely with drinks. **Flagging, not advising** — confirm before launch.

## Mechanics — the details staff and Toast need

- **Threshold:** pre-tax subtotal, before any other discount.
- **Issued:** at checkout — **a physical gift card, handed over with the receipt.** Confirmed fulfillment method.
- **Redeemable:** on a **future** visit — not the same check. This is the whole point.
- **Expiry:** none. WA law restricts gift-card expiration; **do not print an expiry date.**
- **Stacking:** not combinable with other offers (see conflict 1).
- **One per check.**

**Toast setup:** this is not a discount — do **not** build it as one. It's a **physical gift-card
activation at checkout**, triggered by the check total. Staff load $10 or $20 onto a physical card
using the existing gift-card SKU/flow. Confirm with whoever manages Toast config; the Aug 2026 work
on the Toast discount/promo redemption flow is relevant prior art.

### 🔴 Physical inventory — check this before Wednesday

Physical fulfillment introduces the one failure mode that will actually embarrass you: **running out
of cards mid-promo.**

- **Count your physical gift card stock today.** Five days including a weekend and a Late Night
  launch is your highest-traffic window of the month.
- **Rough sizing:** if 15–25 checks/day clear $50 across five days, that's **75–125 cards.** If you
  hold fewer than that, reorder now or set expectations with the team.
- **Have a fallback ready** for running out — a written IOU redeemable on the next visit is far
  better than "sorry, we're out," which turns a generosity play into a broken promise.
- **Decide who activates.** If only managers can load cards, every qualifying check needs a manager
  at the terminal. That's a service bottleneck on a Friday night. Push activation to servers if Toast
  permissions allow.
- **Track the card numbers issued** so return rate is measurable — that's the whole metric for this test.

**Tracking:** tag the activations so you can measure the thing that matters — **how many of those
gift cards come back, and what the return check averages.** Opens and redemptions are the metric;
not sends. Review at 30 days (`toast-lifecycle-automation-playbook.md`).

## Staff script

> "Your total's $52 — that hits our gift card deal, so here's a $10 gift card for next time.
> No expiration, just bring it back."

**Fri + Sat — Late Night overlap.** Both offers run. Staff should treat them as unrelated and not
apologize for either:

> "Late night pricing's already on your tab, and you still cleared $50 — so here's a $10 gift card too."

Do **not** let staff imply the gift card is *instead of* late-night pricing, and don't let them
invent a restriction that doesn't exist. If a guest asks whether the offers stack: **yes, they do.**

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
