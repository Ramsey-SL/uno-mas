# Cantina Club — Platform Evaluation

**Status:** Leaning toward building our own Toast integration (see Option 3) · **Created:** 2026-07-10 · **Owner:** Ramsey

Deciding what platform to run **The Cantina Club** membership program on, given our
stack: **Toast POS** + **Klaviyo** (email/SMS, tied to Toast loyalty data). Two
candidates under review: **WineView** and **Table22**.

Related: the existing loyalty program is "Uno Más Rewards: The Cantina Club" (Toast →
Klaviyo). See `marketing/master-reference.md` (LOYALTY section) and
`brand-intelligence-center/differentiation.md`.

---

## The core distinction

These two tools solve different problems. Which fits depends on whether the Cantina
Club is primarily an **in-venue membership** (perks applied at the table on Toast) or a
**recurring D2C revenue channel** (subscription boxes, drops, shipped/pickup goods).

| | **WineView** | **Table22** |
|---|---|---|
| What it is | Membership/club layer that runs **inside Toast** | Subscription **commerce/growth platform** running *alongside* Toast |
| Native Toast integration | **Yes** — official Toast partner, real-time two-way API sync | **No true POS integration** — parallel branded storefront |
| Best for | In-restaurant tiered membership; members recognized at POS, perks auto-applied to the check | Recurring revenue: subscription boxes, "drops," pre-orders, shipped/pickup goods |
| Who runs it | You, on your Toast hardware | Table22 largely runs it *for* you (payments, fulfillment, support) |
| Pricing (public) | No monthly/signup fees stated (confirm processing/per-transaction) | ~10% + payment processing on subscription revenue |
| Marketing tools | Member mgmt, tier perks, redemption tracking, "built-in marketing" | Automated marketing + CRM, branded storefront, white-glove fulfillment |

**Working recommendation:** the Cantina Club is described in our brand docs as an
**in-restaurant** rewards/membership program (signup at POS; perks like free drinks,
birthday rewards, Mezzanine first-access). That maps to **WineView's** model — it does
the one thing Table22 can't: recognize members and apply perks live on the Toast check.
Reach for **Table22** only if the vision shifts toward paid subscriptions / drops /
shipped goods. **Confirm with the questions below before committing.**

---

## Vendor questions & demo checklists

### Shared context (paste at top of both emails)

> We run **Uno Más Tacos & Tequila** (Spokane, WA) on **Toast POS**, with **Klaviyo**
> for email/SMS tied to our Toast loyalty data. We're building a membership program —
> "The Cantina Club" — where members are recognized in-restaurant and receive tiered
> perks (e.g., free drinks, birthday rewards, first-access to our Mezzanine event
> space). We have two venues in play (main dining room + The Mezzanine). We're
> evaluating platforms to run this on and want to understand fit, integration depth,
> costs, and marketing capabilities before deciding.

---

### WineView

**Program fit**
1. We're a Mexican restaurant / tequila bar, not a winery — can WineView run a **general food + cocktail membership** (not a wine club)? Do you have restaurant customers doing this today, and can you share a reference?
2. Can we build **multiple tiers** with different perks per tier (free drinks, birthday rewards, event first-access, member pricing)?
3. Can perks be **non-product** (e.g., "1 free house margarita/month," "skip the line," "Mezzanine early access") rather than bottle allocations?

**Toast integration**
4. Confirm the integration is **live two-way sync** on our existing Toast hardware (terminals + Toast Go 2/Go 3 handhelds). Anything we need to add or license on the Toast side?
5. When a member is at the table, how exactly does staff **pull them up and apply perks to the check**? Walk us through the server workflow.
6. Do **tier discounts auto-apply**, or does staff apply them manually? How are redemptions tracked and reset each cycle?
7. Does it sync **member/customer data and order history** back to Toast (and therefore to our Klaviyo integration)?
8. How does signup work — **at the POS**, on a web link, or both?

**Costs**
9. You state no monthly/signup fees — what are the **actual costs**? Per-transaction %, payment processing rate, setup, hardware, or add-ons?
10. Any **minimums, contract length, or volume tiers**?

**Marketing**
11. What **built-in marketing** exists (email, SMS, automated messaging, member portal/app)?
12. **How does WineView coexist with Klaviyo?** Can member status/tier/redemption events flow into Klaviyo segments and flows, or would WineView replace part of what Klaviyo does for us?
13. Is there a **member-facing portal or app** (update payment, see perks/rewards, manage membership)?

**Ops & support**
14. Onboarding time, who does the setup, and what training do staff get?
15. What does **reporting** show (member LTV, redemption rates, churn, revenue)?
16. What happens to member/billing data if we **leave** — is it exportable?

**Live-demo checklist**
- [ ] Create a multi-tier Cantina Club with non-wine perks in the admin
- [ ] Ring up a check on a **Toast Go handheld** and show a member being recognized + perk auto-applied
- [ ] Show a redemption being tracked and the cycle resetting
- [ ] Show the member signup flow (at POS and via link)
- [ ] Show member data landing somewhere Klaviyo can read it
- [ ] Show the reporting dashboard (LTV, redemptions, revenue)
- [ ] Show the member-facing portal/app

---

### Table22

**Program fit**
1. Our Cantina Club is primarily an **in-restaurant** membership (perks applied at the table on Toast), with possible add-ons like a monthly member box or pre-paid dining credit. Which of these does Table22 support well, and which not at all?
2. Can you support **tiered memberships with recurring billing**, and what perk types (discounts, credits, exclusive events, shipped/pickup goods)?
3. Do you have **restaurant references** running an in-venue membership (vs. a shipped subscription box)? Can we talk to one?

**Toast integration (biggest question)**
4. **Is there any Toast POS integration?** Specifically: can a Table22 member be **recognized at our Toast terminal** and have perks/discounts **applied to their in-house check**?
5. If not, how do members redeem in-restaurant perks — manual lookup, a code, a separate app? Walk us through the server workflow.
6. Does member/order data sync to Toast and/or **Klaviyo**?
7. If Table22 runs its own storefront/checkout, how do we **reconcile that revenue** against Toast for accounting?

**Costs**
8. Confirm the **exact fee structure** — we've seen ~10% + processing cited publicly. What's the real number, plus payment processing, setup, and any add-ons?
9. Any **minimums, contract, or commitment**?
10. If you handle **fulfillment/shipping**, how is that cost structured?

**Marketing & service**
11. Detail the **automated marketing + CRM** tools. What's included vs. what still needs Klaviyo?
12. **How does Table22 coexist with our existing Klaviyo?** Can events/segments flow between them?
13. You mention white-glove fulfillment and consumer support — what exactly do **you handle vs. us** (payments, customer service, refunds, shipping)?
14. Is there a **branded member storefront/portal** and how much can we brand it (Uno Más look/feel)?

**Ops & exit**
15. Onboarding timeline and what you need from us.
16. Reporting: what metrics do we get (MRR, churn, LTV)?
17. If we leave, is **member + billing data exportable**?

**Live-demo checklist**
- [ ] Set up a tiered Cantina Club membership with recurring billing
- [ ] Show the **branded member storefront** and how it's customized to our brand
- [ ] Demonstrate exactly how an **in-restaurant perk is redeemed** (and whether Toast is involved at all)
- [ ] Show the automated marketing/CRM in action and how it hands off to (or overlaps) Klaviyo
- [ ] Show the fulfillment flow if we add a member box/pickup
- [ ] Show the revenue/churn/LTV reporting
- [ ] Show how their revenue reconciles against Toast

**Framing tip for both calls:** lead with *"a member walks into the restaurant, sits
down, orders — show me exactly what the server sees and does."* That single scenario is
where WineView and Table22 diverge most.

---

## Option 3 — Build our own Toast integration (leading direction)

**Context:** We've already built the Cantina Club program layer (members, tiers, perks)
and have outgrown what WineView/Table22 offer *except* WineView's Toast integration. So
the real question is building that integration ourselves.

**Good news:** this is a first-class, documented Toast capability — the **Loyalty
Integration API** — and it's the same mechanism WineView uses. We'd build the same
bridge, wired into our own stack.

### How the flow works (matches our requirement exactly)

1. Server taps **Rewards** on the Toast terminal/handheld and looks up the guest (phone,
   scannable card, or guest-facing entry).
2. Toast sends an **`inquire`** request to *our* hosted endpoint with the guest identifier
   + current check contents.
3. Our service checks the Cantina Club DB, sees member + tier, and responds
   **synchronously** with the perks/discounts to apply.
4. Toast applies them to the ticket in real time; on payment it sends **`accrue`**
   (plus `redeem`/`reverse` as needed).

Toast supports loyalty discounts at **check-level and item-level** via this API — unlike
the general Orders API, which *cannot* apply discounts to a live check. Loyalty is the
sanctioned path.

### What we'd build

- **One HTTPS endpoint** handling `inquire` / `accrue` / `redeem` / `reverse` (returns
  `200` + `"transactionStatus":"ACCEPT"`).
- **Mapping layer** from our member records to Toast's `loyaltyIdentifier` (which
  **cannot contain PII** — use a UUID/token).
- **Auth + safety:** verify requests are from Toast, maintain a restaurant-GUID
  allowlist, idempotent handling via `Toast-Transaction-GUID`.
- **Low-latency** synchronous responses (a server is waiting at the table).
- **(item-level perks only)** push discount/menu mapping via the **Menus API**.

The code is a contained backend service. The long pole is Toast **access + certification**,
not the code.

### Two paths to access

| | **Path A — Standard API (private)** | **Path B — Marketplace partner app** |
|---|---|---|
| For | Our own locations only | A commercial app other restaurants adopt (Strategy Labs product play) |
| Prereqs | RMS Essentials+, Manage Integrations permission | Full vetting, legal/security/privacy review, signed partner agreement |
| Wrapper | Light | Heavy: certification, alpha, beta, GA listing |
| Note | **Loyalty is email-setup, not self-service** — confirm access model | Toast declines many applicants |

**Important:** Toast docs state **gift-card/loyalty integrations require direct email
setup**, not the self-service marketplace flow — so either path starts with a direct
conversation with Toast's integrations team.

### Path B roadmap (marketplace listing, 8 stages)

1. Apply & get vetted → 2. Discovery & approvals (compliance/privacy/security/legal) →
3. Partner agreement → 4. Dev kickoff (sandbox creds) → 5. Certification (~1-hr demo
review) → 6. Alpha (1 restaurant, ~1 wk) → 7. Beta (3–5 locations, several wks +
co-marketing) → 8. General Availability (public marketplace listing).

Economics context: restaurants pay Toast **$25/mo per location** for unlimited partner
integrations; partner revenue-share terms are negotiated in the agreement (not public).

### Recommended sequence

1. **Email Toast's integrations team** to open the loyalty conversation + confirm the
   access model (self vs. partner) — the binary that gates everything.
2. **Build the loyalty endpoint in sandbox** (same code either path).
3. **Decide A vs. B once it works** — launch privately for Uno Más first, then decide
   whether to pursue the marketplace listing as a Strategy Labs product.

### Open questions for Toast (before writing code)

- Access model: Standard API vs. partner enrollment for a self-use loyalty integration?
- Setup process & timeline for an email-initiated loyalty integration?
- Subscription tier / permissions sufficient (RMS Essentials/Pro)?
- Sandbox credentials — how to get them?
- Latency/SLA for the synchronous `inquire` response; idempotency expectations?
- Does **check-level** discounting alone cover our perks, or do we need item-level (Menus API)?
- How are members identified at the table (phone / scannable / guest entry)?
- Certification requirements & timeline?
- (Path B) revenue share, exclusivity, regional agreement scope?

### Draft outreach to Toast

> **Subject:** Loyalty integration inquiry — Uno Más Tacos & Tequila (existing Toast customer)
>
> Hi Toast Integrations team,
>
> We're an existing Toast restaurant customer (Uno Más Tacos & Tequila, Spokane WA) and
> we've built our own membership program ("The Cantina Club"). We want to connect it to
> Toast via your **Loyalty Integration API** so a member is recognized at the POS and
> their tier perks/discounts apply to their check at dine-in.
>
> Questions to point us to the right path:
> 1. For a loyalty integration serving our **own locations only**, do we use **Standard
>    API access**, or does loyalty require enrolling as a full **integration partner**?
> 2. What's the **setup process and timeline** (we understand loyalty is email-initiated)?
> 3. Prerequisites — confirming our subscription tier (RMS Essentials/Pro) and permissions.
> 4. **Sandbox access** — how do we get credentials to start building/testing?
> 5. **Latency/SLA** for the synchronous inquire response, and certification steps.
> 6. Separately: we may later want to **list this as a marketplace integration** for other
>    restaurants — can you outline that partner track and any revenue-share terms?
>
> Happy to hop on a call. Thanks!

### Toast developer references

- Building a loyalty integration (cookbook): https://doc.toasttab.com/doc/cookbook/apiHowToLoyalty.html
- Loyalty integration overview: https://doc.toasttab.com/doc/devguide/apiLoyaltyIntegrationOverview.html
- Working with order discounts: https://doc.toasttab.com/doc/devguide/apiDiscountingOrders.html
- Reward offers processing: https://doc.toasttab.com/doc/devguide/apiLoyaltyDiscountProcessing.html
- Standard API access requirements: https://doc.toasttab.com/doc/devguide/devApiAccessRequirements.html
- Integration partnership process: https://doc.toasttab.com/doc/devguide/integrationDevProcess.html
- Integration partner application: https://pos.toasttab.com/partners/integration-partner-application

---

## Vendor responses (fill in as they come back)

| Question area | WineView | Table22 |
|---|---|---|
| Restaurant/non-wine fit | | |
| Toast POS recognition + perk-on-check | | |
| Tiers & perk types supported | | |
| Signup flow (POS / web) | | |
| Syncs to Klaviyo | | |
| Actual fees (%, processing, setup) | | |
| Minimums / contract | | |
| Built-in marketing tools | | |
| Member portal/app | | |
| Fulfillment (if member box/drops) | | |
| Reporting (LTV, churn, redemptions) | | |
| Data export on exit | | |
| Reference customer provided | | |

---

## Decision log

- **2026-07-10** — Doc created; both vendors to be contacted. Working lean: WineView for
  in-venue membership fit. Pending demos.
- **2026-07-20** — Table22 ruled out (no real Toast integration; wrong stack for our
  needs). WineView demo held — only compelling piece is the Toast integration; we've
  already surpassed the rest of their offering. **New direction: build our own Toast
  Loyalty Integration** (see Option 3). Next: email Toast integrations team to confirm
  access model, then build the loyalty endpoint in sandbox.

## Sources

- WineView — Toast integration: https://wineview.com/toast/
- WineView: https://wineview.com/
- Toast × WineView listing: https://pos.toasttab.com/integrations/wineview
- Toast Support — WineView setup: https://support.toasttab.com/en/article/Getting-Started-with-the-WineView-Integration
- Richmond BizSense — WineView raise: https://richmondbizsense.com/2026/05/18/wine-club-software-startup-wineview-raises-765k-from-investors-amid-relocation-to-richmond/
- Table22: https://www.table22.com/
- Table22 pricing: https://www.table22.com/pricing
- Table22 for restaurants: https://www.table22.com/category/restaurants
- Austin Chronicle — Table22 fees/margins: https://www.austinchronicle.com/food/table22s-subscriptions-are-helping-restaurants-do-more-than-survive-12102821/
