# The Cantina Club — Program & Platform Spec

**Status:** Planning → build · **Created:** 2026-07-20 · **Owner:** Ramsey · Managed by Strategy Labs

Companion to `marketing/cantina-club-platform-evaluation.md` (why we're building vs. buying)
and the Toast API access guide. This doc defines **what** we're building: the program
structure, member benefits, technology architecture, comms, and a phased build plan.

> 🔴 **SUPERSEDED IN PART — 2026-08-20 ruling.** **The Cantina Club is live TODAY as a single FREE program.**
> Everything in this doc describing **paid membership, subscription revenue, and the three paid tiers
> is FUTURE-STATE design work — not live, not to be marketed.** Read it as the build plan for a
> possible paid program, not a description of what exists. The free program's live mechanics are in
> `marketing/mas-rewards-loyalty-playbook.md`.

**Locked decisions (2026-07-20) — *see the superseding note above*:**
- ~~**Two tiers:** free **Uno Más Rewards** (open to all) + **paid The Cantina Club** (premium).~~ → **2026-08-20: ONE program, The Cantina Club, free. Paid tiers deferred.**
- ~~**Cantina Club = paid membership**~~ → **The Cantina Club IS the free program.** A paid layer may sit on top later.
- **Build the full platform** (organized as parallel workstreams with a "launchable" line).
- **Reviews handled compliantly** — no review gating, no incentivized public reviews.
- **Productization path = Prove single-tenant, resale-friendly (Option ②).** Build cleanly for
  Uno Más now; keep the design modular (tenant-scoped IDs, config-driven perks) so going
  multi-tenant later is a refactor, not a rewrite. Graduate to owned multi-tenant SaaS
  (Option ①) once the concept + paid-membership economics are proven. Skip GoHighLevel.
- **Phase-1 comms = Klaviyo (bulk) + Resend (email) / Twilio (SMS) for triggered 1:1** —
  seeds the owned comms stack.
- **Reservations = build our own, Phase 2** (after loyalty core proves; run Resy in parallel
  until cutover). See WS-F.

---

## 1. Vision & guiding principle

Reward the **return, not the receipt.** Frequency is the currency; spend is a multiplier.
The program exists to **drive repeat visits** — getting people in the door is the goal,
and higher spend is a welcome bonus, not the basis for rewards.

Everyone can join free (top of funnel + marketing list). The Cantina Club is the paid,
aspirational upgrade: *Uno Más Rewards gets you in; the Cantina Club gets you treated like
family.*

## 2. Membership structure

*(⚠️ FUTURE-STATE table — as of 2026-08-20 The Cantina Club is the single FREE program and no paid tier exists.)*

| | ~~**Uno Más Rewards** (free)~~ → **The Cantina Club** (free, LIVE) | **Paid layer** (FUTURE — unnamed publicly) |
|---|---|---|
| Cost | Free | Recurring subscription (price TBD — see Open Decisions) |
| Join via | Checkout, QR, web page, text-to-join | Upgrade from Rewards; buy online or at POS |
| Earning | Visit stamps, base rate | Accelerated earning + exclusive perks |
| Purpose | Acquisition, list growth, base habit loop | Recurring revenue, superfans, premium experience |

**Naming:** reuses existing brand equity — "Uno Más Rewards: The Cantina Club" splits into
its two natural halves.

## 3. Earning & behavioral mechanics (visit-driven)

- **Visit stamp** per check-in (capped once/day) — the base unit.
- **Streaks & comeback windows** — return within N days to keep a streak / unlock the next
  perk. Loss aversion is the strongest repeat-visit lever.
- **Endowed progress** — new members start with 1–2 stamps pre-filled.
- **Slow-day multipliers** — 2× stamps Tue/Wed, aligned to Taco Tuesday + Beer & Bites
  Wednesday, to steer traffic to softer demand.
- **Surprise/variable drops** — occasional unexpected, time-boxed perks (best for habit
  formation).
- **Spend as a bonus** — cross $X in a visit → bonus stamp. Rewarded, never the base.
- Cantina Club members earn at an **accelerated rate** and unlock member-only ladders.

## 4. Benefits catalog (brainstorm — to finalize)

Flag: **POS-applied** perks reduce the check via the Toast loyalty response; **your-system**
perks live in our platform/comms (Toast doesn't apply them to a ticket).

**Uno Más Rewards (free):**
- Free item after N visits *(POS-applied)*
- Birthday treat *(POS-applied)*
- Member price on the daily special *(POS-applied)*
- Access to the member portal, Wallet pass, and comms *(your-system)*

**The Cantina Club (paid) — "loyalty on steroids":**
- Everything in Rewards, at an accelerated earn rate
- **Priority / premium reservations** *(your-system + Resy ops)*
- **Mezzanine event first-access & member comps** *(your-system)*
- Standing monthly perk (e.g. a free house margarita) *(POS-applied)*
- **Flash-perk eligibility** — time-boxed member-only deals *(POS-applied)*
- Surprise drops, early menu/event access *(mixed)*
- "Bring a friend" perks, skip-the-line *(mixed)*
- Exclusive member events

## 4.5 "Join & Save" calculator (in-the-moment conversion tool)

A server- or guest-facing tool that shows, at the table, exactly what a guest would save by
joining the Cantina Club **today** vs. paying full price — then converts them on the spot.

- **Input the current check** — pulled live from the Toast Orders API (by table/check), or
  quick-entered on the server tablet.
- **Simulate membership** — run the check through the rules engine in *hypothetical member*
  mode (same `INQUIRE` logic) to compute today's applicable perks + savings.
- **Show the math** — "Join today ($Y/mo), save $X on this check + [ongoing perks];
  pays for itself in N visits."
- **One-tap convert** — enroll → charge via Stripe → perks apply to *this* check in real time
  via the loyalty integration, so the savings are immediately real.

Spans WS-A + WS-B + WS-C + WS-D. Doubles as the **#1 sales demo** when selling to other
restaurants ("watch it convert a table live").

## 5. Paid-membership mechanics

- **Billing:** Stripe (subscriptions) — monthly and/or annual; free trial optional.
- **Lifecycle:** signup → active → dunning (failed payment retries) → cancel/win-back.
- **Value equation is critical** — a paid member must feel obvious ROI vs. free. Anchor the
  price below the value of the standing monthly perk + priority reservations.
- **Membership status flows into the rules engine** so Toast applies the right perks at POS
  and Klaviyo targets the right segment.

## 6. Technology architecture

```
   Your surfaces                Your brain (own it)            Toast (POS touchpoint)
 ┌────────────────┐        ┌────────────────────────┐        ┌──────────────────┐
 │ Web signup /PWA│──────▶ │  Supabase               │◀─────▶ │ Loyalty API      │
 │ QR · text-join │        │  members, visits,       │ SEARCH │ (recognize +     │
 │ Apple/Google   │◀────── │  tiers, perks, ledger,  │ INQUIRE│  perk on check)  │
 │ Wallet pass    │  push  │  rules engine, billing  │ ACCRUE │                  │
 │ Member portal  │        │                         │◀────── │ Orders webhook   │
 └───────┬────────┘        └───────────┬─────────────┘  spend │ (enrichment)     │
         │ web push                     │                      └──────────────────┘
         ▼                              ▼
   PWA notifications   Klaviyo (email+SMS) · Resy · Stripe · Google Business Profile
```

| Layer | Tool | Role |
|---|---|---|
| Customer DB + rules engine | **Supabase** (Postgres + Edge Functions) | System of record: members, visits, tiers, perks, ledger. Hosts the loyalty endpoint. |
| POS bridge (perk on check) | **Toast Loyalty API** (inbound: SEARCH/SIGNUP/INQUIRE/ACCRUE/REDEEM/REVERSE) | Recognize members + apply perks in real time |
| POS enrichment | **Toast Orders API + orders-updated webhook** (OAuth, `orders:read`, `guest.pi:read`) | Capture visits/spend, feed segments |
| Membership billing | **Stripe** | Recurring Cantina Club subscriptions |
| Digital card | **Apple Wallet + Google Wallet passes** (PassKit/Passcreator or self-hosted) | Lock-screen card + near-free push updates |
| Lightweight app | **PWA** (installable; iOS web push 16.4+) | App experience + push without App Store |
| Email + SMS | **Klaviyo** (already connected to Toast) | Automations + bulk + segments |
| Reservations | **Own build (WS-F)** → replaces Resy | Membership-aware booking on the same guest spine (see §9) |
| Reviews | **Google Business Profile** (Place ID + review link + QR already exist) | Public reviews (compliant flow) |

## 7. Data model (starting point)

```
members            (id, phone_e164, email, name, birthday, tier, status, created_at)
loyalty_tokens     (loyalty_identifier UUID PK, member_id FK)     -- opaque, no PII, for Toast
visits             (id, member_id, check_guid, visited_at, spend_cents, day_of_week)
perk_definitions   (ref, tier, type, value, applies_to, window_rule, active)
perk_grants        (id, member_id|segment, perk_ref, valid_from, valid_until, source)
redemptions        (id, member_id, perk_ref, check_guid, cycle_key, redeemed_at)
subscriptions      (id, member_id, stripe_sub_id, plan, status, current_period_end)
txn_log            (toast_transaction_guid PK, type, payload, result, created_at)  -- idempotency
consent            (member_id, sms_opt_in, email_opt_in, push_opt_in, source, ts)  -- TCPA/CTIA

-- Reservations (WS-F) — same guest spine
venues             (id, name)                                   -- Cantina, Mezzanine, Patio
res_tables         (id, venue_id, name, min_party, max_party, combinable_with[])
availability_rules (venue_id, daypart, slot_interval_min, pacing_covers, turn_time_min)
reservations       (id, member_id|guest_contact, venue_id, party_size, res_at, status,
                    source, deposit_intent_id, member_priority, notes, created_at)
member_priority    (venue_id, rule)                             -- held-back tables / early windows
waitlist           (id, venue_id, guest_contact, party_size, quoted_wait_min, status, created_at)
```

## 8. Communications plan

Match message to the cheapest channel that fits — push does the frequency lifting, SMS is
reserved for high-value/timely.

| Channel | Cost | Use for |
|---|---|---|
| Wallet + PWA push | ~free | Perk unlocked, flash deal today, streak reminder |
| Email (Klaviyo) | cheap | Weekly specials, events, newsletters, bulk |
| SMS (Klaviyo) | per-msg | Flash perks, reservation reminders, win-back |

**Automations:** welcome series · visit milestones · **comeback/win-back** (no visit in N
days — highest ROI) · birthday · perk-expiring · post-visit feedback · tier-up · Cantina Club
renewal/dunning.
**Bulk/planned:** weekly specials, event announcements, flash campaigns.

## 8.5 Comms: build vs. buy vs. white-label + productization

Goal: **prove on Uno Más → sell to other restaurants.** First principle: **don't build the
transport layer** (SMTP, IP warming, carrier/10DLC, deliverability). Decide at the app layer.

| Path | What | Resellable? | Effort |
|---|---|---|---|
| 1 · **Klaviyo (now)** | Keep it; feed loyalty events via API to trigger flows | ❌ each client needs own Klaviyo | lowest |
| 2 · **White-label platform** | Rebrand GoHighLevel (category king) / Vendasta / HubSpot Solutions Partner | ✅ built for resale | low–med |
| 3 · **Build app layer on infra APIs** | Rent pipes — email: SES (~$0.10/1k) / Postmark / Resend; SMS: Twilio/Telnyx/Plivo. Build composer, segmentation, automation builder, consent, analytics — multi-tenant, wired to the loyalty engine | ✅ own the IP | highest |

**Insight:** our differentiation is the **visit-driven loyalty engine**; comms that fire off
*our* events is the point — loosely served by per-client Klaviyo or generic white-label. If
this becomes a product, **Path 3 is the moat.**

**Recommended sequence:**
- **Phase 1 (prove):** Klaviyo for bulk + **triggered 1:1 on Resend (email) + Twilio (SMS)**
  from the loyalty engine — seeds the owned stack cheaply.
- **Phase 2 (productize):** build owned app-layer comms (SES/Postmark + Twilio, multi-tenant).
- **GoHighLevel** = legitimate fast bridge if selling to others *before* that engineering.

**Productization note:** selling to other Toast restaurants = **becoming a Toast integration
partner** and listing in the marketplace (Path B in the eval doc). Each client gets its own
Toast loyalty integration under our app → the SaaS path and the Toast-partner path are the
same road. Implies **multi-tenancy** from the start of any Phase-2 build.

## 9. Reservations — build our own (WS-F, Phase 2)

Replace Resy ($399/mo) with a **membership-aware booking system on the same guest spine**.
Reservations become another surface on the member record — not a separate silo — so
member-priority booking windows, held-back tables, and member-only access are native.

**Design:**
- **Venue/floor model** across Cantina / Mezzanine / Patio: table inventory, pacing
  (covers-per-slot), turn times, combinable tables, waitlist. (Data model in §7.)
- **Member priority** — held-back tables + early-access windows as a Cantina Club perk;
  the system already knows who's a member.
- **No-shows** — Stripe card-on-file / deposits, cancellation windows.
- **Comms** — SMS/email confirmations + reminders via the Phase-1 comms stack.
- **Host-stand UX** — staff must *prefer* it to Resy or they'll route around it.
- **Discovery:** GBP **"Reserve a table"** link → our booking page now (captures Google
  intent, no partner status); pursue **Reserve with Google end-to-end** partner later
  (sub-1s availability, 30+ days inventory, online cancel — gatekept).

**Sequencing & risk:** roughly as big as the loyalty engine; **Phase 2, after the loyalty
core proves out**. Reliability bar is higher than loyalty (a dropped/double booking = a bad
night) — **run Resy in parallel until the host stand trusts it, then cut over** (~$4,800/yr
saved). Design the guest DB now (done) so it slots in.

**Archetype — SevenRooms:** the commercial proof of this exact model (reservations + CRM +
loyalty + marketing on one guest spine). Acquired by **DoorDash for $1.2B (June 2025)**;
now powers "DoorDash Reservations." Priced ~$499–900/mo per venue. Study it for ideas (guest
tagging, spend-aware profiles) — but adopting it means higher cost across our 3 venues, lost
ownership/margin, and tying guest data to DoorDash (against our "no delivery apps" stance).
Building leaner + owning it is the differentiated, resale-friendly path.

## 10. Reviews & feedback (compliant design)

⚠️ **No review gating.** Routing negative reviews to private while pushing positive ones
public violates **Google's review policies** and the **FTC 2024 Consumer Review Rule**.
**Incentivizing public reviews** (perks for a Google review) also violates Google policy +
FTC rules. Penalties are real (review removal, GBP action, FTC enforcement).

**Compliant design that gets ~90% of the intent:**
- **One post-visit flow for all guests** — everyone is offered the public review option; we
  never hide it from unhappy guests.
- **Parallel private service-recovery channel** — a "how was it?" that flags low scores to
  the team to make it right (allowed — we solicit + resolve; we don't *block* the public path).
- **Reward the behavior of giving feedback / checking in** — never conditioned on sentiment
  or on posting a public review.
- Referrals and social tags may be incentivized (lower risk); public reviews may not.

## 11. Compliance & legal checklist

- **SMS (TCPA/CTIA):** explicit opt-in + documented consent; use Klaviyo double-opt-in;
  honor STOP. Store consent in the `consent` table.
- **Reviews (Google/FTC):** per §10 — no gating, no incentivized public reviews.
- **Payments (PCI):** Stripe handles card data; keep it out of our DB/logs.
- **Data privacy:** members own their data; `loyaltyIdentifier` holds no PII; export/delete on
  request.
- **Toast:** loyalty identifier no-PII rule; confirm we can replace Toast native loyalty with
  our integration (can't run both).

## 12. Build plan — parallel workstreams

"Everything at once" in scope, organized so it still ships. **Launchable line = WS-A + WS-B +
WS-C + basic WS-E.** Reservations/reviews (WS-F/G) can trail slightly without blocking launch.

- **WS-A · Loyalty engine (critical path):** Supabase schema + rules engine (visits, streaks,
  slow-day multipliers, tiers, perk grants/windows).
- **WS-B · Toast integration:** inbound loyalty endpoint (6 transaction types) + OAuth Orders
  webhook enrichment. *(Gated by Toast sandbox access — in progress.)*
- **WS-C · Enrollment + identity:** web signup page, QR, text-to-join; **multi-device
  signup** — any browser is a station: iPads/Android tablets in kiosk mode (guest
  self-serve) + server-carried tablets in staff-assisted mode with **staff PIN +
  attribution** (credit the server who signs a guest up); **offline queue** for Wi-Fi blips.
  Phone-E.164 normalization as the POS join key; consent capture. (No Toast dependency for
  signup — members are matched at POS later via `LOYALTY_SEARCH`.)
- **WS-D · Paid membership:** Stripe subscriptions, lifecycle, member status → rules engine.
- **WS-E · Member surfaces & comms:** Wallet passes (Apple/Google) + PWA w/ push; Klaviyo
  automations + bulk.
- **WS-F · Reservations (build our own, Phase 2):** replace Resy ($399/mo) with a
  membership-aware booking system on the same guest spine. Venue/floor model across Cantina /
  Mezzanine / Patio (table inventory, pacing/turn times, combining tables, waitlist);
  **member-priority slots + held-back tables** as a Cantina Club perk; no-show handling
  (Stripe card-on-file/deposits); host-stand UX; SMS/email confirmations + reminders.
  Discovery: **GBP "Reserve a table" link to our booking page now** (captures Google intent
  without partner status); pursue **Reserve with Google end-to-end** partner later (sub-1s
  availability, 30+ days inventory, online cancel — gatekept). **Run Resy in parallel until
  the replacement earns host-stand trust, then cut over** (~$4,800/yr saved). Archetype:
  SevenRooms (reservations + CRM + loyalty in one) — also strengthens the eventual SaaS.
  Reliability bar is higher than loyalty; do not rush the cutover.
- **WS-G · Reviews & feedback:** compliant post-visit flow + private recovery routing (reuse
  existing GBP link/QR).

## 13. Open decisions / inputs needed

1. **Cantina Club price & billing period** (monthly? annual? both? trial?) — anchors the whole
   value equation.
2. **Perk finalization** — pick the launch set for each tier from §4; set thresholds (N visits,
   comeback window days, slow-day rules).
3. **Wallet/pass provider** — managed (PassKit/Passcreator) vs. self-hosted PassKit.
4. **Where the app/infra code lives** — new repo vs. `Ramsey-HQ/Plugins-and-Apps/`.
5. **Free-tier name** — keep "Uno Más Rewards" for free + "The Cantina Club" for paid?
6. **Toast:** confirm we can run our loyalty integration in place of native Toast loyalty.
7. ~~Phase-1 comms path~~ — **RESOLVED:** Klaviyo (bulk) + Resend/Twilio (triggered).
8. ~~Productization intent~~ — **RESOLVED:** Option ② (prove single-tenant, resale-friendly).

## 14. Success metrics

- Repeat-visit rate & visit frequency (primary) · member acquisition (free + paid) · paid
  conversion & retention/churn · win-back reactivations · slow-day traffic lift · comms
  engagement (push/email/SMS) · review volume & rating trend.

## Decision log

- **2026-07-20** — Program shape locked: free Rewards + paid Cantina Club; full-platform build
  as parallel workstreams; compliant reviews (no gating). Spec created.
- **2026-07-20 (cont.)** — Added Join & Save calculator (§4.5), multi-device signup (WS-C),
  comms build/buy analysis (§8.5). **Resolved:** productization = Option ② (prove
  single-tenant, resale-friendly → graduate to owned multi-tenant SaaS; skip GoHighLevel);
  Phase-1 comms = Klaviyo bulk + Resend/Twilio triggered; **reservations = build our own in
  Phase 2** (WS-F, run Resy in parallel until cutover). Next: lock price + launch perk set,
  confirm Toast sandbox, choose pass provider + code home, then **start WS-A**.
