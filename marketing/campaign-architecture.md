# Campaign Architecture — Platforms, Ladder, Channel Roles

> **Source:** integrated 2026-08-20 from the ChatGPT marketing handoff covering July 7 – Aug 20 2026
> (`UNO_MAS_MARKETING_AGENT_CONTEXT.md`, `AGENT_OPERATING_RULES.md`, `PROMO_PROGRAMS.md`).
> This is the **strategic layer** the repo was missing: it explains *why* a campaign exists and
> which platform it belongs to. Facts (prices, dates, offers) still come from their canonical
> owners in `ecosystem-registry.md` §3 — never from this file.

---

## 1. Two platforms, two jobs

| Platform | Job | Core idea |
|---|---|---|
| **Get a Little Lost** | **Acquisition / experience.** Discovery, first visit, the feeling of coming in for tacos and staying longer than planned. | The tagline is also the campaign platform. Use it to frame discovery and experience work — not offers. |
| **The Cantina Club** | **Retention / belonging.** Recognition, access, membership identity, visit frequency. | **Belonging beats bargains.** Recognition and identity matter as much as discount economics. |

Uno Más should feel like **a place people make their regular spot — not a transactional discount
restaurant.** Every recurring program exists to create another reason to return *and* another
chance to identify the guest in Toast.

## 2. The guest ladder (six steps)

The marketing calendar is not a sequence of disconnected specials. It moves guests along this ladder:

1. **Discover** Uno Más
2. **Visit once**
3. **Return** for a 2nd/3rd occasion via recurring programming
4. **Join The Cantina Club** (free)
5. **Become a recognizable regular**
6. **Convert qualified regulars into paid Cantina Club members**

**Design test for any campaign:** which rung does this move a guest to, and how will we know it
happened in Toast? A campaign that can't answer both is a coupon, not a program.

## 3. Recurring demand drivers — and their strategic role

| Day | Program | Role |
|---|---|---|
| **Tuesday** | Taco Tuesday | Habit driver. Pair food with the social experience and margarita messaging. Not a discount blast. |
| **Wednesday** | Beer & Bites Wednesday | Lift a slow midweek night **without turning the brand into a discount proposition.** Keep it experience-led. |
| **Thursday** | Big F’N Thursday *(replaced Burrito Thursday, 2026-08)* | Food offer. **Watch for collision with Mezzanine entertainment programming** — Love Island watch parties also ran Thursdays. Decide campaign hierarchy when they overlap. |
| **Sunday** | Sunday Brunch 10am–4pm | **Major growth priority.** Still new — needs repetition, menu education, food-forward creative, and retention follow-up. |
| **Fri + Sat** | **Late Night Happy Hour 8–10pm** *(new, launches 2026-08-28)* | Creates a **new occasion** — after-dinner, post-event, industry crowd — rather than discounting an existing one. The literal mechanism behind *Get a Little Lost*: came in for tacos, stayed longer than planned. **Fri–Sat only: Tue–Thu close at 8pm.** |
| **Wed–Sun** | **The Weekly Promo Drop** *(named 2026-08-25)* — the recurring slot the rotating offer lands in | Announced Tuesday, revealed Wednesday. **Naming the franchise means each week inherits the equity of the last** instead of launching cold, and it turns "what's the offer this week?" into a slot to fill rather than a decision to remake. First drop: the gift-card bounce-back, Wed Aug 26. |
| **Fri–Sun** | Weekend traffic promos — **a rotating weekly TEST, not a standing offer** | Each weekend runs a different structure, and the sequence has moved deliberately **away from discounting**: straight discount → fixed bundle → bundle ladder → deferred credit (gift card). Current status + the full test history and what to measure: `campaigns/weekend-promos/executions-log.md`. |

## 4. Channel roles

- **Email** — richer storytelling, menu/program education, events, multi-section weekly messaging, lifecycle automation. Use **modular sections** with meaningful click targets. Always: preview text, compliant unsubscribe footer, **one clear primary action** with secondary sections supporting it. Module system: Canva `DAHINHHZJng` (11 pages) + `uno-mas-klaviyo-email-clickable-sections.html`.
- **SMS** — concise, high-intent reminders, flash offers, same-week traffic, utility. **Put the reason to act early.** One promotion per message. **Keep it short: segment count drives cost.**
- **Social** — real food, cocktails, venue, staff, guest energy. Prefer **vertical**. Show the experience; don't just restate the offer card.
- **Website** — campaign landings, brunch/menu discovery, recurring specials, event details, visit intent, loyalty education.
- **In-restaurant** — table talkers, menu inserts, gift cards, staff scripting, and Toast check-in/check-out behavior must reinforce whatever is running digitally.

## 4b. Two creative systems — pick deliberately

Uno Más runs **two distinct visual systems.** Don't blend them in one piece.

| System | Looks like | Use for |
|---|---|---|
| **Photographic** | Real DAM photo, dark scrim, huge Antonio headline over the image, minimal furniture. Built as 1080×1350 HTML — see `campaigns/daily-specials/poster-taco-tuesday.html`. | Day-of-week programs, brand/experience work, anything selling the room or the food itself. |
| **Illustrated promo card** | Textured cream/aged ground, script *Uno Más* wordmark, condensed heavy sans, pink money numbers, yellow highlight swash, teal starbursts, halftone-shadowed **illustrated** food & drinks, `UNO MÁS ★ TACOS + TEQUILA` footer. | **Offer communication** — bundles, thresholds, weekend specials, code-word promos. Where a price is the message. |

**⚠️ REVISED 2026-08-24 after Ramsey's review.** The clean split above was too rigid. His note on the
first round of Late Night Happy Hour assets: *"they just feel underwhelming and not bold, bright, and inline with
restaurant advertising best practices."*

**The corrected rule: food photography leads, brand furniture frames it.** Restaurant advertising
sells the food — a type-only offer card reads as a coupon, not an invitation. So:
- **Photo-led + a bold offer block** is the default for anything promoting *food or a daypart*
  (menus, dayparts, specials). Photo hero, dark scrim, huge Antonio headline, then a solid
  pink/yellow bar carrying the price.
- **Pure illustrated** is reserved for offers where **money is the message** and there's no dish to
  show — gift cards, spend thresholds, dollar-value promos.
- **Legibility is not optional.** White type over food needs a real scrim *and* a text-shadow;
  check it at full size, not thumbnail. A bright tortilla will eat a white headline.

*Get a Little Lost* still leans photographic. The difference is that offer creative now does too,
unless the offer has no food in it.

Live examples of the illustrated system: `campaigns/weekend-promos/executions-log.md`.

## 4c. The Weekly Promo Drop

**Named 2026-08-25.** The rotating weekly offer now has a name and a rhythm:

| | |
|---|---|
| **Tuesday** | Announce it — *"Our new weekly promo drop starts tomorrow."* No detail. |
| **Wednesday** | **Soft open.** Offer live, team briefed, table tents out. No consumer send. |
| **Thursday** | **Launch.** The email explains the offer; the SMS drives that night. |
| **Wed–Sun** | It runs |

**On splitting the offer window from the launch day** *(pattern set 2026-08-25)*: the offer can go
live before the marketing does. That keeps a promise already made to the list while giving the push
a single, uncrowded day. **The condition is that staff are briefed before the soft open** — a guest
who heard about it and gets a blank look is worse than no announcement at all.

**Why "drop" and not "flash":** a flash implies hours. These run five days, and a word that
overpromises stops meaning anything by week three. "Drop" carries the same recurring-anticipation
benefit without claiming urgency the window doesn't deliver.

**What this fixes:** the first four weekend offers each launched cold, with no connective tissue.
A named slot means guests start *checking* rather than being interrupted, and you get a container
to fill instead of a decision to remake every week.

**Rules:**
- **Announce the program on Tuesday, never the offer.** The reveal belongs to Wednesday's email — that's the channel that can explain it.
- **One drop per week.** Two competing offers in the same window is where margin breaks.
- **Log every drop** in `campaigns/weekend-promos/executions-log.md` with its result, so the series compounds into knowledge instead of four unmeasured experiments.

## 5. Campaign cadence principle

> Create **predictable reasons to visit multiple times** — do not train guests to wait for random
> coupons. Build weekly rituals; use loyalty to recognize the behavior.

## 6. Loyalty naming — ✅ RESOLVED 2026-08-20

**There is ONE loyalty program: The Cantina Club. It is FREE.**

- Call it **The Cantina Club**. Never "loyalty program," never "rewards program."
- There is **no free-vs-paid split to name** — the program is free, full stop. Do not invent a
  separate free-tier name.
- **Paid tiers (Cantina Member / Cantina OG / La Familia) are a FUTURE-STATE idea. Not live.
  Never market or publicly reference them.**
- Retired naming, do not use: **"The Guest List"** (Aug 2026 handoff's term — never adopted),
  **"Más Rewards"** / **"Uno Más Rewards"** as a standalone program name (legacy prefix, deprecated).

This closes the open decision logged in `cantina-club-program-spec.md` and overrides the handoff.

## 7. Cantina Club copy guardrails (from the handoff — adopt these)

- **The Cantina Club is free.** Don't imply a purchase, a tier, or a paywall.
- Paid tiers (**Cantina Member · Cantina OG · La Familia**) are **future-state — never referenced publicly.**
- **Reward visit frequency first.** Spend may be a signal but must not define belonging.
- When selling paid membership, use **specific economics**, not vague "exclusive savings."
- **Never call La Familia "VIP," "elite," "boss-level,"** or frame members as above other guests.
- **Never reward or gate on positive public reviews.** No review gating, ever.

## 8. Pre-flight checklist before producing any campaign

1. Confirm the actual current offer, date, daypart, price, and **operational availability**.
2. Check the canonical owner for every fact on the piece (`ecosystem-registry.md` §3).
3. **Search approved Cloudinary assets before sourcing or generating anything.**
4. Search Canva for the closest reusable component (`canva-design-manifest.md`).
5. Name the campaign's role: acquisition · visit-frequency · event traffic · brunch awareness · loyalty signup · paid conversion.
