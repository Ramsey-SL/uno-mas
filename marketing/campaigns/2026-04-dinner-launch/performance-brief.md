# Performance Brief — Uno Más Dinner Launch

> From: Campaign Strategist
> To: Performance Marketing Agent
> Campaign: 2026-04-dinner-launch
> Date: April 9, 2026
> **Campaign live: April 14 (soft) → April 15 (full)**

---

## Campaign Overview

| Field | Value |
|-------|-------|
| **Goal** | Drive dinner covers — establish Uno Más as Spokane's dinner destination |
| **Dates** | April 14 (soft) → May 21, 2026 |
| **Total Paid Budget** | $1,500 (Meta only) |
| **Daily budget** | ~$71/day at full deployment |
| **Platform** | Meta Ads Manager (Facebook + Instagram) |

---

## Channel Plan

| Channel | Role | Budget | Start Date |
|---------|------|--------|-----------|
| Meta — Prospecting | New audience discovery — Spokane locals who don't know about dinner menu | $900 (60%) | Apr 14 |
| Meta — Retargeting | Re-engage website visitors + social engagers who haven't converted | $600 (40%) | Apr 15 |
| Email / SMS | Conversion + retention — owned, no paid budget | $0 | Apr 15 |

---

## Audience Targeting

### Meta — Prospecting Campaign

**Geography**: Spokane, WA metro area — 15-mile radius from 2020 N Monroe St

**Primary audience (interest-based)**:
- Interests: Restaurants, Dining, Mexican food, Cocktail bars, Date night, Spokane WA
- Behaviors: Frequent restaurant visitors, Frequent travelers (dining-oriented)
- Age: 25–45
- Exclude: Current Uno Más Rewards: The Cantina Club loyalty list (they get the email/SMS — don't double-pay for them)

**Lookalike audience**:
- Source: Upload Klaviyo Uno Más Rewards: The Cantina Club email list as custom audience → build 1% lookalike
- This is your highest-intent prospecting audience — budget 60% of prospecting here

**Broad audience (test)**:
- Age 22–50, Spokane metro, no interest filters
- Budget: 20% of prospecting — let Meta's algorithm find converters
- Only scale if CTR and CPA are competitive with interest/lookalike

### Meta — Retargeting Campaign

**Website visitors**: All visitors to unomastacoshop.com in last 60 days — exclude anyone who visited the dinner menu page 3+ times (already highly aware)

**Social engagers**: Anyone who engaged with Uno Más Instagram or Facebook in last 90 days — video views, profile visits, saves, comments

**Email non-converters**: Upload Klaviyo list of subscribers who opened the dinner launch email but didn't click through (high intent, didn't act)

**Exclusion**: Anyone who has already visited the restaurant in the last 30 days (loyal regulars handled by email/SMS)

---

## Campaign Structure (Meta Ads Manager)

```
Campaign: Uno Más Dinner Launch
├── Ad Set 1: Prospecting — Lookalike (1%)
│   ├── Budget: $540 (36% of $1,500)
│   ├── Objective: Conversions (menu page view or click-to-call)
│   ├── Creative: Variant A (Surf & Turf) + Variant B (Feast)
│   └── Bid: Lowest cost
│
├── Ad Set 2: Prospecting — Interest/Behavior
│   ├── Budget: $360 (24% of $1,500)
│   ├── Objective: Conversions
│   ├── Creative: Variant C (Raw Bar) + Variant A (Surf & Turf)
│   └── Bid: Lowest cost
│
├── Ad Set 3: Retargeting — Website Visitors + Social Engagers
│   ├── Budget: $450 (30% of $1,500)
│   ├── Objective: Conversions
│   ├── Creative: Story variants (shorter, more direct CTA)
│   └── Bid: Lowest cost
│
└── Ad Set 4: Retargeting — Email Non-Converters
    ├── Budget: $150 (10% of $1,500)
    ├── Objective: Conversions
    ├── Creative: Most direct CTA variant ("you saw the email — now come see the menu")
    └── Bid: Lowest cost
```

---

## KPIs & Targets

| Metric | Baseline | Target | Platform |
|--------|---------|--------|---------|
| Blended ROAS (paid only) | No prior data | 1.5x minimum (owned channels bridge to 3x) | Meta Ads Manager + GA4 |
| CTR | No prior data | >1.5% | Meta Ads Manager |
| CPC | No prior data | <$2.00 | Meta Ads Manager |
| Frequency | — | <3.0 per person | Meta Ads Manager |
| Menu page visits from paid | — | 300+ over 6 weeks | GA4 |

**Alert thresholds**:
- CTR below 0.8% after 3 days → swap creative immediately
- CPC above $3.00 after 5 days → review audience targeting, broaden or narrow
- Frequency above 4.0 → creative refresh required, flag to Creative Director
- Daily spend underpacing by >30% → check audience size, expand geo or age range

---

## Tracking Requirements

**Pixel events to verify before launch**:
- `PageView` — firing on all pages ✓ (verify)
- `ViewContent` — firing on dinner menu page (verify)
- `Contact` — firing when phone number is clicked (verify)
- `Lead` — firing on any reservation/inquiry form submit (verify)

**UTM structure (apply to all links)**:
```
Paid Meta ads:     utm_source=meta&utm_medium=paid&utm_campaign=dinner-launch&utm_content=[variant-a/b/c]
Email:             utm_source=klaviyo&utm_medium=email&utm_campaign=dinner-launch
SMS:               utm_source=klaviyo&utm_medium=sms&utm_campaign=dinner-launch
Organic social:    utm_source=instagram&utm_medium=organic&utm_campaign=dinner-launch
```

**Attribution model**: Last-click via GA4 (official). Meta platform ROAS for bid optimization only.

**Conversion destination**: Link all ads to the dinner menu page on unomastacoshop.com. If no dedicated dinner landing page exists — flag to Ramsey and use the main menu page with a dinner section anchor link.

---

## Creative Asset ETA

All creative assets from Creative Director due: **April 13, 2026**

**What you'll receive**:
- 3 × 1080×1080 static images (Feed variants A, B, C)
- 2 × 1080×1920 static images (Story variants)
- 2 × 1200×628 static images (Facebook Feed)
- Ad copy for each variant (from Ad Copy agent)
- UTM links for all destinations

**Build all campaigns in Ads Manager on April 13 (paused). Activate on April 14.**

---

## Soft Launch Protocol (April 14)

1. Activate Ad Set 1 (Lookalike Prospecting) only — at 25% daily budget ($18/day)
2. Run 2 creative variants (A + B)
3. Monitor for 24 hours: pixel firing, UTMs populating in GA4, CTR >0.8%
4. If all checks pass → scale to full budget April 15
5. If tracking issues → hold, flag immediately, do not scale until resolved

---

## Optimization Schedule

| When | Action |
|------|--------|
| Apr 14 (24hr) | Tracking QA — confirm pixel + UTMs firing |
| Apr 18 (Day 3) | First CTR/CPC check — flag any alert-threshold breaches |
| Apr 22 (Day 7) | Creative performance ranking — identify winning variant, pause losers |
| Apr 22 | Audience performance — is lookalike or interest/behavior performing better? Reallocate budget to winner |
| Apr 28 | Check frequency on all ad sets — creative refresh if >3.0 |
| May 5 | Mid-campaign review — adjust budget pacing for final 2 weeks |
| May 10 | Begin wind down — reduce to 50% daily budget |
| May 21 | Pause all campaigns |

---

## Competitive Notes

No competitive ad data on file yet. Based on brand intelligence, Spokane's taco/Mexican restaurant segment is not heavily saturated with paid social. Expect low CPC competition ($1.50–$2.50 range). The dinner positioning angle ("Surf & Turf at a taco shop") is currently uncontested in the local market — move fast to own this territory before competitors notice.
