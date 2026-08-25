# Gift Card Bounce-Back — Campaign Brief

**Type:** promotion (limited window) · **Status:** 🟢 **OFFER LIVE Wed 2026-08-26 → Sun 2026-08-30** · **MARKETING LAUNCH Thu 2026-08-27** · physical gift card at checkout
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
3. ✅ **Two dates, not one (set 2026-08-25):**
   - **Offer live: Wed Aug 26 → Sun Aug 30.** Unchanged. Any guest who hits the threshold Wednesday gets their card.
   - **Marketing launch: Thu Aug 27.** The anchor email and the push happen Thursday, not Wednesday.

   **Why this works:** the Tuesday SMS already told the list the drop "starts tomorrow," and it does —
   so nothing said to a guest becomes untrue. Wednesday is a **soft open**: the offer is live and the
   team can execute it, but no consumer announcement goes out. Thursday carries the volume.

   **The cost of a soft open is real, though:** anyone who saw Tuesday's SMS and comes in Wednesday
   expects something. **Staff must be briefed before Wednesday service** — "we don't know what you're
   talking about" is the one outcome that damages the promo.

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
- **Issued:** at checkout — a **pre-loaded physical gift card** ($10 or $20 already on it) handed over with the receipt. **No terminal activation needed.** Confirmed 2026-08-23.
- **Redeemable:** on a **future** visit — not the same check. This is the whole point.
- **Expiry:** none. WA law restricts gift-card expiration; **do not print an expiry date.**
- **Stacking:** not combinable with other offers (see conflict 1).
- **One per check.**

**Toast setup: minimal — cards are PRE-LOADED.** This is not a discount and it is not a checkout
activation. Cards are loaded with $10 and $20 **in advance**, so at the table it's just: check clears
the threshold → hand over the right card. No terminal steps, no manager override, no discount object
in Toast.

**This resolves the activation bottleneck.** The earlier concern — that manager-only activation would
jam Friday service during the Late Night launch — **no longer applies.** Any server can hand over a
pre-loaded card.

### ✅ Physical inventory — 200 cards on hand (confirmed 2026-08-23)

**You're covered.** Sizing at 15–25 qualifying checks/day over five days is 75–125 cards. You'd need
to average **40/day** to exhaust 200 — roughly double the strong case. No reorder needed.

**What 200 issued would actually mean.** Assume a 70/30 split of $10 to $20 cards:

| | |
|---|---|
| Cards issued | 140 × $10 + 60 × $20 |
| **Future liability created** | **~$2,600** |
| **Qualifying revenue required to issue them** | **≥$13,000** (140 checks ≥$50 + 60 ≥$100) |
| Liability as % of that revenue | **~20%** — and only realized when cards come back |

Breakage cuts the real cost further: a meaningful share of gift cards are never fully redeemed. So
the honest framing is *~20% of incremental revenue, deferred, minus breakage* — which is why this
beats a straight 20% discount that costs the full amount immediately.

**Mid-promo tripwire.** Count issued cards **Friday morning.**
- **Under 60** — normal pace, 200 is plenty.
- **80+** — you're tracking toward exhausting 200 across the weekend. Prep the IOU fallback Friday
  afternoon rather than discovering it at 9pm Saturday.
- **120+** — reorder, and consider whether to keep promoting it Sunday.

**Still to decide:** who activates cards. If only managers can load them, every qualifying check
needs a manager at the terminal — a real service bottleneck on the Late Night launch night. Push
activation to servers if Toast permissions allow.

**Track the card numbers issued.** Return rate is the entire metric for this test. Pre-loading makes this easier — record the number range you load, then reconcile what's left on Monday.

### On "hoping we sell out"

Worth separating two different wins:

- **Issuing all 200** means the *threshold worked* — people spent to hit $50/$100. That's a check-average win, and it shows up this week.
- **Cards coming back** means the *bounce-back worked*. That's the actual point, and it shows up over the following weeks.

Issuing 120 with 70 returning is better business than issuing 200 with 30 returning. So measure both,
but **judge the promo on return rate** — and don't let a full-sellout week talk you into repeating it
if the cards never come home.

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
