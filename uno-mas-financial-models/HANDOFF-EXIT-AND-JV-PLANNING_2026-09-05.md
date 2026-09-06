# HANDOFF — Exit & JV Planning — start here (2026-09-05)

This captures several weeks of scenario work done in a single Claude conversation that
was never written to disk until now. If you're picking this up in a new session, read
this file first, then pull the five artifacts listed at the bottom (they're the only
part of this work that already survives independently).

## The situation driving this work

Ramsey had a cardiac event and can no longer operate the business day to day. Two paths
have been under active analysis:

- **Plan A — sell the business** to a third-party buyer, structured around debt
  assumption + a seller note.
- **Plan B — don't sell yet.** Consolidate all debt into one SBA loan collateralized by
  the landlord's real estate, bring the landlord in as a 50/50 JV partner, activate the
  vacant unit next door as an event space run by Uno Más staff, and target a sale in
  12–24 months once the business is de-levered and diversified.

Both paths assume a broker relationship already exists (prior LOI history) providing a
standing floor exit at any time, independent of either plan's progress.

---

## THE DEBT PICTURE (source of truth — cross-check against `Debt/Uno Mas - DEBT SCHEDULE.csv`)

| Facility | Balance | Rate | Monthly | Notes |
|---|---:|---:|---:|---|
| MoFi 202407502 (larger) | 257,662.58 | 11.0% | 2,800.00 | SBA-guaranteed 75% (confirmed via SBA FOIA data — see below). Modified July 2026, payment cut from $4,995.46. **Executed modification agreement never received — resolve before any transaction.** Personal guaranty attached. |
| MoFi 202507954 (smaller) | 65,419.20 | 9.5% | 1,244.21 | Also SBA-guaranteed 75%. Personal guaranty attached. |
| ARF Financial (revolving LOC) | 43,627.90 | fee-based | 3,743.22 | Revolving period ends 03/02/2027 — terms after that date unconfirmed. Cannot be assumed by a buyer; must be cash-cleared. |
| Amex Plum — 0% workout | 45,995.50 | 0% | 1,021.00 | Card member is Ramsey personally — will NOT novate to a buyer or new entity regardless of deal structure. Treat as permanently personal unless Amex agrees otherwise. |
| Chase Ink — 0% workout | 53,646.86 | 0% | 882.00 | Business card, LLC's name — CAN travel with an entity/equity sale. |
| Tenant improvement loan | 69,506.22 | 11.0% | 2,174.00 | Billed inside the landlord's rent invoice. **Payoff disputed**: landlord's schedule shows $69,506.22; Ramsey contends $74,033.55 (principal frozen by a 05/22/2026 agreement) plus $5,735.85 of separately disputed charges. Steps off Oct 2029 (−$26,088/yr permanently, whoever holds it). |
| Misc — Toast Capital + Scott + other | ~100,000 | — | — | **Not yet precisely quantified — get exact Toast balance and Scott's exact figure before finalizing any structure.** A $20K miss moves Plan B's net-to-Ramsey by ~$2,900/yr. |
| **Third-party total, ex-owner-loan** | **535,858.26** (+ ~100K misc = **635,858.26** if consolidating everything) | | | |
| Owner loan (Ramsey → Uno Más, related party) | 539,370.14 | 0% | discretionary | Subordinated, no fixed schedule. Does NOT get repaid in full under any scenario modeled — recovery ranges from ~14% to ~26% depending on structure. |

**SBA FOIA lookup performed** (data.sba.gov, 7(a) FY2020-Present file): both MoFi loans
confirmed SBA-guaranteed at 75%, Preferred Lenders Program, 84-month term (matures ~March
2032 — this resolves an earlier internal conflict between the loan docs' stated maturity
and the July 2026 modification's 204-month re-amortization, which implies a large balloon
at the true 2032 maturity if the modification didn't also extend it — **confirm this with
MoFi directly**). MoFi's own unguaranteed exposure is only ~25% of each note (~$80,770
combined) — this is why MoFi has limited economic incentive to compromise principal while
the loans are current, but real incentive to grant rate/term relief since that costs them
nothing.

**MoFi ask, in priority order** (from cheapest-for-them to hardest):
1. Consent to any ownership change **at the modified $2,800 payment** — reversion to
   $4,995.46 breaks every buyer-financeability case modeled.
2. **Written release of Ramsey's personal guaranty** on both notes — non-negotiable, this
   is what makes any of Plan A actually an exit rather than a transfer of operations while
   keeping the liability.
3. Rate/term relief (e.g., 6% over 15–20 years) on any residual Ramsey retains personally
   — costs MoFi nothing, worth $40–75K to Ramsey depending on structure.
4. Partial principal forgiveness — the hard ask, needs documented hardship (physician
   letter + SBA personal financial statement), realistically 10–25%, not 40%+, while
   Strategy Labs income exists. Confirm insolvency-exclusion tax treatment with a CPA
   before agreeing to any forgiveness (1099-C exposure).

---

## PLAN A — SALE TO A THIRD-PARTY BUYER

### Core structure settled on
Buyer assumes the lease (with TI inside it, treated as rent) + assumes MoFi (both notes,
at the $2,800/$1,244 payments) + clears ARF in cash at closing. Ramsey carries a seller
note for the balance, retains the two cards + Scott personally.

### The pricing ladder (price → what's retained → payoff timeline)
This is the master table — regenerate it if any input changes (misc debt figure, broker
split, rate):

| Price | Cash to MoFi | MoFi residual to Ramsey | Retained debt (cards+Scott+misc) |
|---:|---:|---:|---:|
| 300,000 | 38,730 | 284,352 | 149,642–193,270 depending on cards |
| 350,000 | 85,730 | 237,352 | " |
| 375,000 | 109,230 | 213,852 | " |
| 400,000 | 132,730 | 190,352 | " |
| 450,000 | 179,730 | 143,352 | " |

Break-even price to clear **all** debt including MoFi in cash: **~$549,311** (cards
assumed by buyer) or **~$602,502** (nothing assumed). $600K listed cash-only nets
approximately zero to Ramsey — that's the practical "fully clean" cash number.

### Seller note terms modeled (best version found)
**$183,290 at 10%, stepped 3%/4%/5% of gross sales (years 1/2/3-5), 5-year balloon,
prepayable at par.** Buyer's DSCR at the $75,071/mo sales forecast: 1.33x in year 1 rising
to comfortable by year 3. This was the best-tested structure — flat percentages either
starve the buyer in year 1 or leave Ramsey under-collected.

Ramsey's retained-debt sweep (cards + Scott's $50K, servicing them from note receipts):
clears in ~46–67 months depending on whether Chase is retained or goes with the buyer
(**Chase should go with the buyer** — worth ~$60,000 to Ramsey vs. keeping it).

MoFi residual, if any is left with Ramsey personally, should be refinanced onto an
**interest-only LOC at ~7.75%** rather than serviced at MoFi's 11% — this alone is worth
20–40 months off any payoff timeline. $1,500/mo of Ramsey's own money on top of the LOC
minimum is the identified sweet spot (below that, the payoff timeline stretches past 9
years and costs MORE in total interest, not less — this is counterintuitive and worth
re-deriving if it comes up again).

### The Amex/Chase distinction — remember this
Amex is personally Ramsey's card and will not novate under ANY structure without Amex's
explicit release. Chase is a business card and travels with an equity/entity sale. This
single fact is worth tens of thousands of dollars across every structure modeled — always
route Chase to the buyer, always plan for Amex staying personal.

### Successor liability / deal structure
An **asset sale** exposes a buyer to WA excise-tax successor liability unless they get a
DOR tax clearance certificate (adds 2–4 weeks). An **equity sale** (membership interests)
avoids this and lets MoFi/lease/cards travel without individual assignment — recommended
structure given the timeline pressure Ramsey is under.

---

## PLAN B — LANDLORD JV + DEBT CONSOLIDATION (the more recently developed plan)

### The structure
- Bank has verbally offered to consolidate **all** Uno Más debt into a single 10-year SBA
  loan at 8%, CONDITIONAL on the landlord co-signing/collateralizing with real estate.
- Consolidated amount: **$635,858.26** (all third-party debt including the misc ~$100K —
  confirm exact misc figure before finalizing). Payment: **$7,714.72/mo, $92,577/yr.**
- Landlord and Ramsey become **50/50 partners** in the combined entity (restaurant +
  event space) — 50/50 justified specifically because the landlord is pledging real
  estate (not cash) and likely signing a personal guaranty per SBA's 20%+-owner
  requirement, a genuinely comparable risk to what Ramsey has carried.
- The event space (vacant adjoining unit) is operated by existing Uno Más staff —
  kitchen, licenses, wholesale accounts, marketing already in place, no new hire needed.

### Restaurant standalone economics (60% prime, INCLUDING the chef fully loaded inside
the 60% rather than as a separate fixed line — this was a specific modeling correction
requested and should be preserved in any re-derivation)
Annual restaurant contribution before debt/management comp: **$190,043** on the 2026
reforecast of $900,854 sales. November is the seasonal low point (~$4,637/mo) — five
months of the year run cash-negative on a standalone basis before JV income offsets it.

### Event space economics (50% prime = 30% food + 20% labor)
Modeled at a **$360,000/year** revenue case (the planning target, NOT a booked
calendar — flagged clearly in the landlord pitch as an assumption to revisit). At that
level: event contribution $180,000/yr. A $3,000/mo management fee to Karissa & Thomas
was modeled as an offset to their base restaurant comp, not a separate revenue line —
i.e., total K&T comp stays $88,400/yr combined regardless of whether it's sourced from
the restaurant or the event fee.

### Combined JV profit pool
```
Restaurant contribution (60% prime, incl. chef)      190,043
+ Event space contribution ($360K rev, 50% prime)    180,000
- Karissa + Thomas combined compensation             (88,400)
- Consolidated SBA debt service                      (92,577)
= COMBINED JV PROFIT POOL                             189,066
  → Ramsey's 50%                                       94,533/yr
  → Landlord's 50%                                     94,533/yr
```

### 24-month sale targets
Enterprise value target range agreed for the pitch: **$800,000–$1,200,000**, based on a
2.5x–3.5x multiple against combined debt-free EBITDA of $281,643/yr (restaurant + event
contribution, less K&T comp, no debt service since the premise is the loan is retired or
being retired from proceeds at sale). Buyer DSCR at these prices, 90% SBA-financed at 8%,
ranges 1.79x–2.69x — comfortably bankable; max financeable price before hitting a 1.25x
floor is roughly **$1.72M**, so financeability is not the constraint — achievable multiple
is.

**No-sweep** (100% of the $189,066 pool distributed, loan serviced at scheduled minimum
only) was the version recommended to LEAD the pitch with — it delivers nearly identical
total 24-month outcomes to a 50%-principal-sweep version but gets both partners
~2x more cash during the hold. The sweep only matters if optimizing for a lower loan
balance at sale (helps a buyer's financing) or a "debt-free" narrative.

**24-month landlord total return** (no-sweep): $385,711–$585,711 across the $800K–$1.2M
range, made up of: $69,506 TI payoff in cash at closing (this is unique to the landlord —
resolves the disputed TI billing immediately) + $189,066 of distributions over 24 months
+ 50% of sale equity (sale price minus ~$545,723 loan balance at month 24).

**24-month Ramsey total return** (no-sweep): $316,204–$516,204 across the same range —
identical structure minus the TI windfall, which is the landlord's alone since resolving
that obligation is specifically theirs to capture.

### Open items specific to Plan B
- Exact split of "misc $100K" (Toast + Scott + other) needs real figures, not a round
  number, before this goes to the bank.
- Whether Scott is willing to be rolled into a joint SBA facility behind a landlord's
  collateral (this changes his position materially from a personal note to a subordinate
  creditor position) — has not been asked yet.
- Whether the landlord's collateral is the whole building or a specific parcel — changes
  their downside meaningfully (their tenant relationship is also their collateral in the
  whole-building case).
- SBA generally requires personal guaranties from 20%+ owners — Ramsey should expect to
  still personally guarantee the NEW consolidated loan even after this restructuring;
  it's a much cleaner single-facility guaranty rather than six scattered ones, not a full
  release.

---

## ARTIFACTS PRODUCED (these persist independently of any session)

| Artifact | Purpose | URL |
|---|---|---|
| Monroe Street Operating Summary | Broker-facing P&L, asset value, FY2025 sales, 2026 reforecast | https://claude.ai/code/artifact/29ff401c-6248-4261-b95e-2c2569c9f463 |
| Monroe Street Deal Terms | One-pager for the broker on the Plan A structure Ramsey will consider | https://claude.ai/code/artifact/1545a5c6-065a-4ec3-bd53-39af5e268f01 |
| Monroe Street Partnership | Earlier investor/partner memo (Karissa+Thomas+outside investor version, capital-for-equity) — **note the near-duplicate title with the item below; rename one to avoid confusion** | https://claude.ai/code/artifact/4b774157-1391-4142-848d-3c32c40ef1b0 |
| June 2026 Cash Activity | Management-prepared consolidated bank statement, 3 accounts, for a potential lender | https://claude.ai/code/artifact/eb3aeb60-3718-46d5-9f02-eef602c12bb9 |
| **The Monroe Street Partnership** | **Plan B landlord pitch — the most current, most complete deliverable of this whole thread** | https://claude.ai/code/artifact/446fcb69-aac7-4e01-9abb-6edcd7aaf25a |

## Reference tools available for re-running any of this
- SBA FOIA loan-level data: `https://data.sba.gov/sites/default/files/uploaded_resources/FOIA_7a_FY2020_Present_asof_260630.csv` (173MB CSV — grep by borrower name, do not load whole file into a script's memory casually)
- `~/projects/unomas-toast-dashboard` — Toast API dashboard, credentials need refreshing (last check returned 401 — client secret likely rotated, or Standard API access revoked; regenerate at Toast Web → Integrations → API access)
- The Uno Más brand system (`~/projects/uno-mas-brand/design-system/tokens.css`) was used for every artifact above — Antonio + Montserrat, pink `#E22690` / navy `#003366`

## Immediate next actions, in order
1. Get exact figures for the "misc $100K" (Toast balance, Scott's precise number)
2. Call MoFi — ask the four things listed above, in that order
3. Decide Plan A vs. Plan B (or run both in parallel — the broker relationship supports
   this since Plan A's floor exit doesn't require abandoning Plan B)
4. If Plan B: present the landlord pitch artifact, gauge their interest in the real estate
   collateral ask before spending more time refining the model
5. Confirm the true 2032 MoFi maturity/balloon question directly with MoFi — resolve
   before any transaction of either kind closes
