# The Weekly Promo Drop — Two Margs + A Dip

**Status: PROPOSED. Nothing live, nothing printed.** Review package: `promo-overview.html`.
Test 5 in the Weekly Promo Drop sequence.

| Field | Value |
|---|---|
| Offer | **Two house margaritas plus your choice of a chips and dip shareable — $25** |
| Window | Wed 2 Sep – Sun 6 Sep 2026, all day |
| **Exclusion** | **Not valid 8–10pm Fri & Sat during Late Night Happy Hour** |
| Redemption | Ask your server. No code, no app. |
| Limit | **No limit** — order it as many times as you like, per visit *(decided 2026-08-31)* |
| Drinks | **House margaritas only** — no Cadillac, no flavored upgrades at the offer price *(decided 2026-08-31)* |

| Dips | **All three** — Chips & Salsa, Chips & Guacamole, or Chips & Queso Blanco. Guest's choice, no upcharge *(decided 2026-08-31)* |

## The pricing logic

House margarita is **$12.50**, so two are **$25 exactly**. The dip is the entire reason this reads
as an offer rather than a wash.

| Guest picks | Dip | À la carte | Bundle | Saves | % off |
|---|---|---|---|---|---|
| Chips & Guacamole | $6 | $31 | $25 | $6 | 19% |
| Chips & Queso Blanco | $8 | $33 | $25 | $8 | 24% |
| Chips & Salsa | $4 | $29 | $25 | $4 | 14% — **included per Ramsey 2026-08-31** |

**Ladder consistency:** Full Send was 20% off at both tiers; Test 2 (2 margs + the $16 Trio at $30)
was 27%. This lands at 19–24%, so guests are not being taught that waiting gets a better week.

**Note on the team-facing page:** all comparative pricing and savings language was removed from
`promo-overview.html` on Ramsey's direction — the only figure that appears there is $25. The math below is
retained here as the internal record only.

**Rejected: $25 with the Chip & Dip Trio.** That is 39% off and hands over the $16 Trio for free,
because two margs already total $25. Ramsey caught this himself and narrowed the offer to a single dip.

## The Late Night conflict — this is the one that matters

Late Night Happy Hour drops margs to **$6** Fri/Sat 8–10pm. In that window the bundle contents are
worth **$12 + $8 = $20 maximum**, so a $25 bundle would cost the guest **$5 more than ordering off
the menu**. Four of the five days in the Drop window contain this collision.

Without an explicit carve-out the floor either refuses the sale and looks inconsistent, or a guest
does the arithmetic and feels misled. **The line is not optional.**

## Decided 2026-08-31

- **House margaritas only.** Cadillac (+$2) and flavored margs are excluded at the offer price.
- **No limit per visit.** A table can run the bundle as many times as they want.
- **All three dips are in.** Salsa included on Ramsey's call 2026-08-31, overriding my recommendation to
  restrict it to guac and queso. His reasoning holds: a choice with no wrong answer is easier for the floor
  to state and removes a reason to say no to a guest.

> **What the no-limit call actually does:** it makes every additional dip effectively free as long as
> the guest buys two more margs. Guac and queso are low food-cost items, so this trades cheap food
> against drink volume — a good trade, and it turns the offer into an upsell the floor can push
> rather than a one-shot coupon. Worth briefing as *"two more margs and another dip is another $25."*

- **The "what it's worth" pricing table was removed from the team-facing doc** on Ramsey's call. The
  math is retained here as the internal record: guac saves $6 (19%), queso saves $8 (24%), against
  Full Send's 20% and Test 2's 27%.

## Open decisions

1. **Late Night carve-out** — confirm in.
2. **Verify the individual dip prices on both printed menus** — the "up to $33" claim depends on it, and
   the printed menus already disagree on the Trio ($16 lunch vs $15 dinner).
3. **Fourth bundle in five weeks** — tests 2, 3 and 5 are all bundles. The gift card was the one
   structurally different test and it worked. Not an objection, but worth deciding deliberately.

## The team-facing page

`promo-overview.html` — white ground, typographic, **real photography**. The illustrated system is not
used on this page; the artboard previews of the tile, poster and email were removed on Ramsey's
direction 2026-08-31, along with the Logistics, Before-we-build and Afterwards sections.

**Photos used, all verified by eye before selection — not chosen off filenames:**

| Asset | Why |
|---|---|
| `…/food/20260814_UM_FOOD_ChipsGuacTrio_v1` | **The offer in one frame** — two margaritas and chips with guacamole, shot in the dining room with the Uno Más sign visible. Hero band. |
| `20260125_UM_FOOD_ChipDipTrioV2_FINAL` | Clean overhead of all three dips beside a chip basket. Carries "any of the three". |
| `…/food/20260814_UM_FOOD_ChipsGuacTrio_v4` | Overhead on a patio table, three dips plus two margs. Closes the floor section. |
| `20260125_UM_DRINK_Marg_FINAL` | Single house marg, in venue, warm. |
| `…/food/20260730_UM_FOOD_ChipsSalsa_v2` | Tight chip-basket texture shot. |

All are 1536–2560px, fine for web. The print gate does not apply here.

**Headline leading was corrected** from `line-height:.83` to `1.02` — at 90px the two lines were
colliding, which is a real defect of the condensed display face at large sizes, not a preference.

## Assets

**No new artwork required.** Margaritas and the single dip bowl are cropped from
`20260814_UM_PROMO_WeekendSpecial_Portrait` (3506×4381) — the only print-resolution illustrated
asset in the library. The single-bowl crop yields 720×540, enough for a 2in element and no larger.

**Gap:** no standalone illustration of a single chips & dip exists. On the generation backlog in
`marketing/chatgpt-illustration-prompt.md`.

## Creative system note

**Promos are illustrated. Menus are clean type on white.** This split was set 2026-08-27 when Ramsey
stripped the Late Night menu to type on white. Both are correct — they are different jobs, and the
two should not be judged against each other.

## Print output

`promo-overview.html` prints to **exactly 3 pages** on US Letter at 0.42in margins:

| Page | Contains |
|---|---|
| 1 | Header, hero, the four photo tiles, the offer spec |
| 2 | How it works, For the floor, what has to land this week |
| 3 | The send plan, the two alternative allocations, footer |

**Verified by rendering, not estimated.** `printcount.sh` drives headless Chrome
`--print-to-pdf` and counts `/Type /Page` in the output. The count went 7 → 5 → 4 → 3 across
four passes, with each group measured in isolation to find which one was overflowing.

Two breaks are forced: `break-after` on `#offer`, and a `.pagebreak` marker before the first
send block — the break sits *inside* the week section so page 2 absorbs the priorities and
page 3 carries only the send plan. That rebalance is what got it from 4 to 3.

**Print-only suppressions** (screen keeps everything): the Save-as-PDF button, the nav, the
inline photo in the offer section, and the two paired photos under How It Works. Print still
carries the four tiles and the floor photo.
