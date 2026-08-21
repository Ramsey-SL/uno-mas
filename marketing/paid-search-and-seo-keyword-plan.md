# Uno Más — Integrated Paid Search + SEO Keyword Plan

**Date:** 2026-06-28
**Owner:** Ramsey · Managed by Strategy Labs
**Purpose:** A single keyword universe that runs **two channels off one map** — Google Ads (capture now) and SEO/GBP (earn the position over time) — with geo-tiered bidding and an explicit rule to *bid on high-volume terms until the website ranks top-3 organically for them, then pull paid back.*

> **Confirmed decisions (2026-06-28):** Primary goal = **balanced** (dinner covers + event/catering inquiries, track both). **Coeur d'Alene, ID is IN** the Events + Catering catchment. **Wedding terms = small capped test only** (we're better positioned for rehearsal dinners + reception after-parties). Monthly budget TBD → 3 scenarios modeled in §6a.

> **Estimates disclaimer:** Search volume, competition, and CPC below are **directional estimates for the Spokane DMA**, not pulled from a live Keyword Planner. Treat them as a prioritization framework. Validate exact numbers in Google Ads Keyword Planner before locking bids (see *Next Steps*). Demand = relative monthly search volume in the Spokane metro (H/M/L). Comp = Google Ads auction competition. CPC = estimated cost-per-click range. SEO Diff = how hard to rank organically.

---

## 1. The operating model — "Bid until we rank"

Every high-value term lives in **both** channels. The governance rule:

| Current organic position | Paid posture |
|---|---|
| Not in top 10 (page 2+) | **Bid aggressively.** Paid is the only way you show today. |
| Top 4–10 (page 1, below fold) | **Keep bidding**, slightly lower budget. Paid + organic both visible = more SERP real estate. |
| Top 3 organic / Map Pack | **Throttle paid down** to a defensive minimum. Don't pay for clicks you'd win free. Keep a small bid only if a *competitor is bidding on the term* (defend the top of page). |
| #1 organic **and** Map Pack #1, no competitor bidding | **Pause paid.** Reallocate budget to terms you don't yet own. |

**Implication:** This plan is also a **SEO roadmap**. The clusters below double as the page/content architecture for the new Lovable site. Build the page → rank the page → retire the ad spend → recycle budget into the next cluster. Track each term's live organic rank (Search Console + manual SERP checks) in a shared sheet so the throttle rule can actually be applied monthly.

⚠️ **Audit needed:** I haven't pulled your current organic rankings (no Search Console access here). Every "SEO play" below assumes a from-scratch position. First action in *Next Steps* is a ranking baseline so we know which terms are already partly won.

---

## 2. Geo architecture — nested radius + per-business-line catchment

You're right that a casual taco run is hyper-local while a wedding-venue or catering search is worth paying for from much farther out. So radius is **not one setting — it varies by what's being sold.**

### 2a. The three concentric tiers (default casual/dining campaigns)

| Tier | Ring | Who's here | Bid posture |
|---|---|---|---|
| **T1 — Core** | 0–2 mi | North Monroe, Emerson-Garfield, West Central, Kendall Yards, downtown-adjacent | **Highest bids** (baseline, or +15–20%). Your everyday catchment. |
| **T2 — Near** | 2–5 mi | Downtown Spokane, South Hill north edge, Logan, Audubon | **Baseline / slight discount** (−10% to 0%). |
| **T3 — Metro** | 5–10 mi | Spokane Valley, North Side, Cheney edge, Mead | **Discounted** (−25% to −40%). Worth less per click for casual dining. |

**Mechanics (two ways to build it):**
- **Simplest — one campaign, location bid adjustments:** Target a 10-mi radius, then add 5-mi and 2-mi radius targets *inside the same campaign* and set descending bid adjustments (e.g. 2 mi +20%, 5 mi 0%, 10 mi −30%). Google applies the tightest matching ring's adjustment. Low management overhead. **Recommended for v1.**
- **Truest "nested campaigns" — separate campaigns per ring:** One campaign per ring with the inner ring(s) *excluded* from the outer campaign, each with its own daily budget and max-CPC cap. Maximum control over "how much I'll pay the further out they are," but 3× the management. Worth it once spend scales or for the high-value lines below.

### 2b. Catchment overrides by business line

| Campaign | Recommended max radius | Why |
|---|---|---|
| Taco Tuesday / weekly specials / lunch | **2–3 mi** | Impulse, midweek, hyper-local. Don't pay for far clicks. |
| Mexican / tacos / casual dinner | **5–10 mi** (tiered as above) | Standard dining catchment. |
| Date night / destination dinner | **10–15 mi** | People *travel* for a "worth it" night out. |
| Private events / venue rental | **15–25 mi + Spokane Valley + Coeur d'Alene, ID** | Event planners shop the whole region; one booking >> dozens of covers. |
| Off-site catering | **20–30 mi** | Catering travels; corporate/Valley offices are prime. |
| "Best / must-try / visiting Spokane" | **Metro + visitor layer** | Tourists & relocators research before they arrive — see 2c. |

### 2c. The visitor / "destination" layer
Your customer doc flags travelers as a real segment ("best Mexican I've had in a long time"). Run a small, separate ad group targeting **"people regularly in or who searched for" Spokane** (not "presence only") for terms like *best restaurants in spokane*, *where to eat spokane*, *must try spokane*. Cap it low — it's discovery, not bottom-funnel — but it captures the trip-planner before arrival.

> Set base location targeting to **"Presence: people in or regularly in your targeted locations"** for all dining/specials campaigns to avoid burning budget on out-of-market researchers. Only the visitor layer uses the broader "presence or interest" setting.

---

## 3. The keyword universe

Organized by cluster. Each cluster = a Google Ads ad group **and** a target page/content theme for SEO. Priority ★ = funding/effort order within the channel.

> **Match-type strategy (paid):** Lead with **Phrase** match for control on a local budget. Use **Exact** for your highest-converting head terms once data proves them. Use **Broad** *only* paired with Smart Bidding + a strong negative list, and only on a few discovery terms. Brand stays Phrase/Exact.

---

### Cluster A — Reputation & "best / must-try / staple" (BEYOND the food vertical) ★ NEW EMPHASIS
*The positioning lane you asked for. High volume, high competition, mixes locals + visitors. This is where SEO + Google Business Profile matter most — these queries are won in the Map Pack and "best of" listicles as much as in ads.*

| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| best restaurants in spokane | Phrase | H | High | $2.00–4.00 | ★★★ | High | Bid now; long game is GBP reviews + getting onto Inlander/Visit Spokane "best of" lists + a strong on-site "Why Uno Más" page. |
| best restaurant spokane | Phrase | H | High | $2.00–4.00 | ★★★ | High | Same as above. Volume head term. |
| top restaurants spokane | Phrase | M–H | High | $1.75–3.50 | ★★ | High | SEO via listicles + reviews; paid to bridge. |
| must try restaurants spokane | Phrase | L–M | Med | $1.50–3.00 | ★★ | Med | Lower comp, great fit ("you *have* to go"). Content: "must-try" page + signature-dish schema. |
| best locally owned restaurant spokane | Phrase | L | Low–Med | $1.25–2.75 | ★★ | Med | **Owner-operated is a true differentiator vs chains (Matador/Borracho).** Own this in copy + GBP "locally owned" attribute. |
| best new restaurants spokane | Phrase | M | Med | $1.75–3.25 | ★ | Med | Monroe flagship opened Dec 2024 — still "new-ish." Time-boxed opportunity. |
| best mexican restaurant spokane | Phrase | H | High | $2.00–3.50 | ★★★ | High | Bridges A and C. Map Pack + reviews are the organic win. |
| best taco spokane / best tacos spokane | Phrase | M | Med | $1.25–2.75 | ★★ | Med | Signature-strength; rank via taco-specific content + reviews. |
| best margarita spokane | Phrase | L–M | Low–Med | $1.00–2.25 | ★★ | Low–Med | Tequila-bar identity; low comp, winnable organically. |
| best happy hour spokane | Phrase | M | Med | $1.50–3.00 | ⚠️ | — | **Caution: Happy Hour is retired.** Don't bid — landing page can't honestly promise it. Revisit only if a HH-style offer returns. |
| spokane staple restaurant / iconic spokane restaurant | Phrase | L | Low | $1.00–2.00 | ★ | Low | More PR/brand than search volume. Use in content + earned media, light paid. |

**SEO build for Cluster A:** Reviews engine (ask-for-review flow via Toast/Klaviyo → GBP + Yelp), claim & optimize Google Business Profile (the single biggest lever for "best…spokane"), pitch to *Inlander* "Best Of" + *Visit Spokane*, and a site page that earns the "best/must-try" framing with proof points (107% loyalty spend, 76K-view post, signature dishes).

---

### Cluster B — Discovery / "where to eat" (broad intent, beyond vertical)
| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| restaurants in spokane | Phrase | H | High | $1.50–3.00 | ★ | High | High volume but broad; run lean with tight negatives. |
| places to eat in spokane | Phrase | M–H | Med | $1.50–2.75 | ★★ | Med | Good discovery; landing on a strong home/about page. |
| where to eat in spokane | Phrase | M | Med | $1.50–2.75 | ★★ | Med | Visitor-heavy — pairs with 2c visitor layer. |
| restaurants near me | Broad+loc | H | High | $1.50–3.00 | ★ | n/a | Tight 2–3 mi radius only; Smart Bidding. Organic = GBP/Maps. |
| restaurants on monroe spokane / north monroe restaurants | Phrase | L | Low | $1.00–2.25 | ★★ | Low | **Hyper-local, low comp, easy SEO win.** Own "North Monroe" corridor. |
| fun restaurants spokane / unique restaurants spokane | Phrase | L–M | Low–Med | $1.25–2.75 | ★★ | Med | "Get a little lost" / three-venue story fits perfectly. |
| good restaurants spokane | Phrase | M | Med | $1.50–2.75 | ★ | Med | Generic; supportive, not primary. |
| spokane restaurants open now | Phrase | M | Med | $1.25–2.50 | ★ | Low | GBP hours + dayparting ads (only when open). |

---

### Cluster C — Mexican / tacos core (the vertical — kept, not relied on alone)
| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| mexican restaurant spokane | Phrase | H | High | $1.50–3.00 | ★★★ | High | Core. Map Pack + Mexican-cuisine schema. |
| mexican food spokane / mexican food near me | Phrase / Broad+loc | H | High | $1.50–3.00 | ★★ | High | Near-me = tight radius. |
| tacos spokane / best tacos spokane | Phrase | M | Med | $1.25–2.50 | ★★ | Med | Signature strength; taco menu page. |
| taco bar spokane | Phrase | L–M | Low–Med | $1.00–2.25 | ★★ | Low | Closer to identity, lower comp. |
| birria tacos spokane | Phrase | L–M | Low | $1.00–2.00 | ★★★ | Low | Trending + on-menu ($14). Easy organic win. |
| taco shop spokane | Phrase | L–M | Low | $1.00–2.00 | ★ | Low | Brand origin term; note brand voice avoids "taco shop" in *descriptions* but it's fine as a search target. |
| mexican restaurant north spokane | Phrase | M | Med | $1.25–2.50 | ★★ | Low | Geo-niche, winnable. |

---

### Cluster D — Dinner / date night / destination (★ PRIMARY MARGIN)
| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| date night restaurant spokane | Phrase | M | Med–High | $1.75–3.25 | ★★★ | Med | Wider radius (10–15 mi). Dinner page + Resy CTA. |
| romantic restaurant spokane | Phrase | L–M | Med | $1.50–3.00 | ★★ | Med | The Mezzanine angle. |
| nice restaurants spokane / upscale restaurant spokane | Phrase | M | Med–High | $1.75–3.25 | ★★★ | Med | Reframe "elevated dinner program" without "fine dining." |
| dinner spokane | Broad+loc | M | Med | $1.25–2.75 | ★★ | Med | Pair "dinner spokane monroe" for geo-niche. |
| group dinner spokane / large group restaurant spokane | Phrase | L | Low–Med | $1.25–2.50 | ★★ | Low | Bridges into events. The Feast / shareables. |
| best dinner spokane | Phrase | M | Med | $1.50–3.00 | ★★ | Med | Overlaps Cluster A reputation play. |
| carne asada spokane / surf and turf spokane | Phrase | L | Low | $1.00–2.25 | ★ | Low | Signature-dish high-intent; cheap, easy organic. |

---

### Cluster E — Tequila / cocktails / bar (differentiator, low comp)
| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| tequila bar spokane | Phrase | L | Low | $1.00–2.25 | ★★ | Low | Own it — direct vs Table 13 / De Leon's. |
| cocktail bar spokane | Phrase | M | Med | $1.25–2.75 | ★★ | Med | Craft cocktail page. |
| margaritas spokane / best margarita spokane | Phrase | L–M | Low–Med | $1.00–2.25 | ★★ | Low | Espresso Margarita (Indaba) is unique hook. |
| espresso martini / espresso margarita spokane | Phrase | L | Low | $1.00–2.00 | ★★ | Low | Near-zero comp, distinctive. Content + GBP post. |
| tequila flight spokane | Phrase | L | Low | $1.00–2.00 | ★ | Low | Niche, high-intent, cheap. |
| bars in spokane / fun bars spokane | Phrase | M–H | Med | $1.25–2.75 | ★ | Med | Broad; run lean. |

---

### Cluster F — Weekly specials / Taco Tuesday (★ tight radius, cheap, high frequency)
*You asked specifically to win "best Taco Tuesday specials." High intent, recurring, hyper-local. Dayparting matters — heavy on the day-of.*

| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| taco tuesday spokane | Phrase | M | Low–Med | $1.00–2.25 | ★★★ | Low | **Dayparting: bid hard Mon eve–Tue, throttle rest of week.** 2–3 mi radius. Dedicated /specials page + weekly GBP post. |
| best taco tuesday spokane | Phrase | L–M | Low | $1.00–2.00 | ★★★ | Low | Low comp, exact fit (BOGO street tacos + $6 margs). Easy to own organically. |
| taco tuesday deals / taco tuesday near me | Phrase / Broad+loc | M | Low–Med | $1.00–2.25 | ★★ | Low | Near-me = 2 mi cap. |
| drink specials spokane / food specials spokane | Phrase | L–M | Low | $1.00–2.00 | ★ | Low | Map weekly specials (Beer & Bites Wed, Burrito Thu) onto these. |
| margarita deals spokane / cheap margaritas spokane | Phrase | L | Low | $1.00–1.75 | ★ | Low | $6 marg / $30 pitcher hook. Note "cheap" usually a negative elsewhere — allow only in this ad group. |
| big f’n thursday spokane | Phrase | L | Low | $1.00–1.75 | ★ | Low | Niche brand-specific; trivial to own. *(Replaced `burrito thursday spokane` — Burrito Thursday retired 2026-08.)* |

---

### Cluster G — Private events / venue rental (★ HIGH MARGIN — expand) 
*Wide catchment (15–25 mi + CdA). Event/venue CPCs run higher, but one booking dwarfs a cover. Worth a dedicated campaign with its own budget.*

| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| private event venue spokane | Phrase | L–M | Med–High | $2.50–5.00 | ★★★ | Med | Dedicated /private-events page → karissa@ inquiry as conversion. |
| event venue spokane / event space spokane | Phrase | M | High | $2.50–5.50 | ★★★ | High | Map Pack + venue directories matter; bid while ranking. |
| private dining spokane / private dining room spokane | Phrase | L–M | Med | $2.00–4.50 | ★★★ | Med | The Mezzanine = exact answer (28 seated). |
| party venue spokane / party room spokane | Phrase | L–M | Med | $1.75–4.00 | ★★ | Med | Birthday/celebration intent. |
| birthday party venue spokane | Phrase | L–M | Med | $2.00–4.00 | ★★ | Med | High-frequency event type. |
| rehearsal dinner venue spokane | Phrase | L | Med | $2.00–4.00 | ★★★ | Med | High-value, low-comp; Mezzanine fit. |
| corporate event venue spokane / meeting space spokane | Phrase | L | Med–High | $2.50–5.00 | ★★ | Med | Valley/downtown offices; weekday catchment. |
| bachelorette party spokane / graduation party venue spokane | Phrase | L | Med | $1.75–3.50 | ★ | Med | Seasonal spikes (spring/summer grad). |
| holiday party venue spokane | Phrase | seasonal | Med–High | $2.50–5.00 | seasonal | Med | **Spin up Oct–Dec.** High-value, high-intent window. |
| wedding venue spokane / wedding reception venue spokane | Phrase | M–H | **High** | $3.00–8.00 | ★ (test) | High | Expensive & competitive vs dedicated wedding venues. Test small; you're better positioned for *rehearsal dinners* + *reception after-parties* than full weddings. |

**SEO build for Cluster G:** A real `/private-events` hub with each space (Mezzanine/Patio/Buyout), capacities, the three packages (Essentials $750 / Fiesta $1,200 / Full Send $1,800), photos, an inquiry form (conversion event), Event + Service + FAQ schema. List on The Knot/WeddingWire/Eventective + Visit Spokane for backlinks.

---

### Cluster H — Off-site catering (★ HIGH MARGIN — expand)
*Catering travels — radius 20–30 mi. $55K+ in 2025 with zero sales effort = big runway.*

| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | SEO Diff | Integrated play |
|---|---|---|---|---|---|---|---|
| catering spokane | Broad+loc | M | High | $2.50–5.00 | ★★ | High | Broad; pair with Smart Bidding + negatives. |
| taco catering spokane / taco bar catering spokane | Phrase | L | Low–Med | $1.75–3.50 | ★★★ | Low | **Exact fit, low comp — best catering entry point.** Own it. |
| mexican catering spokane | Phrase | L | Low–Med | $2.00–4.00 | ★★★ | Low | Distinctive cuisine + low comp. |
| corporate catering spokane / office catering spokane | Phrase | L | Med–High | $2.50–5.00 | ★★ | Med | Weekday, Valley/downtown offices; high LTV. |
| party catering spokane / event catering spokane | Phrase | L–M | Med | $2.00–4.50 | ★★ | Med | Bridges to events cluster. |
| wedding catering spokane | Phrase | L–M | Med–High | $2.50–5.50 | ★ | Med | Test; seasonal. |
| food truck catering spokane | Phrase | L | Low | $1.50–3.00 | — | — | **Skip unless a truck exists** — don't bid on a service you don't offer. |

**SEO build for Cluster H:** A `/catering` page (menus, min headcount, lead time, service area map, quote form → conversion), Service + FAQ schema, and a Google "catering" service attribute on GBP.

---

### Cluster I — Brand (always-on, cheapest, defensive)
| Keyword | Match | Demand | Comp | Est. CPC | Paid ★ | Notes |
|---|---|---|---|---|---|---|
| uno más / uno mas spokane | Phrase | M | Low | $0.50–1.50 | ★★★ | Cheap, high CTR; defend against competitor poaching. |
| uno mas tacos / uno más tacos and tequila | Phrase | M | Low | $0.50–1.50 | ★★★ | Pair with sitelinks (Menu/Reservations/Events). |
| uno mas monroe / uno mas mezzanine | Phrase | L | Low | $0.50–1.25 | ★★ | Captures venue-specific intent. |

*Brand SEO should already be #1 — if it isn't, that's a quick technical fix, not an ad spend.* Tight negatives essential (see below — "uno más" = "one more" in Spanish triggers junk).

---

### Cluster J — Brunch ▶ LIVE (brunch launched July 2026 — Sundays 10am–4pm; activate this cluster)
`mexican brunch spokane`, `brunch spokane`, `sunday brunch spokane`, `best brunch spokane`, `bottomless mimosas spokane`. Your SEO brief flags this as an **open lane** — no Mexican brunch competitor in Spokane. Build the `/menu/brunch` page + ad group now (SEO takes months to mature), keep ads paused, flip on the day brunch returns to capture the lane first.

---

## 4. Negative keywords (master list — expanded)

Apply at **account or shared-library** level so every campaign inherits them.

**Brand-protection / disambiguation:**
`recipe`, `recipes`, `how to make`, `homemade`, `card game`, `uno rules`, `uno app`, `uno online`, `song`, `lyrics`, `meaning`, `translation`, `in english`

**Wrong intent / non-buyers:**
`jobs`, `job`, `hiring`, `careers`, `application`, `salary`, `menu pdf`, `nutrition`, `calories`, `gift card balance`, `coupon` (except in the specials ad group), `free`, `$1`

**Chains / competitors you don't want to pay to match:**
`taco bell`, `del taco`, `jack in the box`, `chipotle`, `qdoba`, `moe's`

**Service mismatch (you don't offer these):**
`delivery`, `doordash`, `uber eats`, `grubhub`, `drive thru`, `food truck` (until/unless one exists)

**Geo bleed (out of market):**
`seattle`, `tacoma`, `portland`, `boise`, `coeur d'alene` *(remove CdA from the negatives ONLY for the Events/Catering campaigns where you want it)*

**Ad-group-specific note:** "cheap," "deals," "$6," "bogo" are **negatives everywhere except Cluster F (specials)** — there they're the whole point.

---

## 5. SEO action layer (mapped to clusters — the roadmap)

Priority order, because organic is the long-term cost-killer behind every "bid until we rank" line:

1. **Google Business Profile** — claim/optimize (Place ID still unconfirmed per venue ops doc). Categories, hours, attributes ("locally owned," "private dining," "catering"), photos, weekly GBP posts (Taco Tuesday!), Q&A. *Single biggest lever for Clusters A, B, C "near me," and Map Pack.*
2. **Reviews engine** — automated ask-for-review via Toast/Klaviyo → Google + Yelp. Volume + recency of reviews is what wins "best…spokane."
3. **Schema/JSON-LD** on the new site — Restaurant, LocalBusiness (hours), Menu/MenuItem, Event, Service (catering), FAQPage, AggregateRating. (Detailed in [seo-keyword-research.md](seo-keyword-research.md).)
4. **Cluster landing pages** — `/private-events`, `/catering`, `/menu/dinner`, `/specials`, `/mezzanine`, `/menu/brunch` (pre-built, paused). Each owns its cluster's head term in H1 + title + body.
5. **Reputation content** — "Why Uno Más" / "must-try" page with proof points; pitch *Inlander* Best Of + *Visit Spokane*; venue/catering directory listings for backlinks.
6. **Local corridor content** — "North Monroe / Monroe Street" geo pages (low comp, easy wins).
7. **`llms.txt`** + sitemap (per existing SEO brief) for AI Overviews / Perplexity citations.

> **The handoff:** as each page matures to top-3 organic for its head term, apply the §1 throttle rule and move that ad budget to the next un-won cluster.

---

## 6. Budget, bidding & rollout

**Recommended v1 campaign structure (REVISED to match real volume — §7).** Weights moved *toward* the cheap/high-volume lanes (Reputation, Dinner, Mexican core) and *away* from exact-match Private Events (which the data showed is near-zero paid volume):

| Campaign | Radius | Starting bid strategy | Budget weight | Δ vs prior |
|---|---|---|---|---|
| Reputation / Best-of (A) | metro + visitor | Max Clicks, capped | **17%** | +4 🔺 cheap, 1K–10K, on-brand |
| Mexican / Tacos core (C) | tiered 2/5/10 mi | Max Clicks → CPA | **17%** | +2 🔺 cheap engine |
| Dinner (D) | 10–15 mi | Max Clicks → CPA | **17%** | re-anchored on `dinner spokane` (1K–10K) |
| Catering (H) | 20–30 mi + CdA | Max Clicks → CPA | **12%** | ~ workhorse = `catering spokane` |
| Discovery (B) | tiered 2–5 mi | Max Clicks, lean | **8%** | split out; huge vol, sliver capture |
| Private Events (G) | 15–25 mi + CdA | Max Clicks → CPA | **8%** | −12 🔻 only `event venue/space` have volume |
| Taco Tuesday / Specials (F) | 2–3 mi, dayparted | Max Clicks, capped | **8%** | ~ |
| Tequila / Bar (E) | tiered | Max Clicks, lean | **7%** | split out |
| Brand (I) | metro | Max Clicks, low cap | **6%** | +1 🔺 index 0 — own cheap |
| Brunch (J) | — | **Paused** | **0%** | — |

> **Honoring the "balanced" goal under thin event demand:** paid weight on Events+Catering is only 20% *not* because events matter less, but because their **search demand can't absorb more spend efficiently** (§7 finding #1). To keep the covers↔inquiries balance you asked for, events/catering get **disproportionate non-paid support**: the `/private-events` + `/catering` SEO pages, GBP attributes, Meta Ads (your connected channel), and referral/directory listings carry the load paid search can't. Revisit the paid weight up only if Keyword Planner volume grows or broad-match mines new event queries.

*\*Weights are relative — apply to whatever daily total you set. Real top-of-page bids (§7) are low ($0.12–2.13 on most money terms), so clicks are cheaper than first modeled — see revised scenarios below.*

### 6a. Budget scenarios (since the number isn't locked)

**Planning assumptions (REVISED with real bids):** blended CPC ≈ **$1.75** (lower than the first $2.25 estimate — §7 top-of-page bids on the money terms are mostly $0.12–2.13; note new accounts often pay *above* this early, settling down as Quality Score builds); click split ≈ **72% dining-side** (Reputation/Mexican/Dinner/Discovery/Tequila/Specials/Brand) / **16% events+catering** / **12% brand+discovery overflow**; dining click→conversion (Resy/call) ≈ **4–8%**; event/catering click→inquiry ≈ **3–5%**.

| | **A — Lean** | **B — Moderate** | **C — Aggressive** |
|---|---|---|---|
| Daily / Monthly | $30 / ~$900 | $50 / ~$1,500 | $100 / ~$3,000 |
| Est. clicks/mo (@ ~$1.75 CPC) | ~515 | ~855 | ~1,715 |
| Dining clicks → **conversions/mo** (Resy/call) | ~370 → **15–30** | ~615 → **25–49** | ~1,235 → **49–99** |
| Event+catering clicks → **inquiries/mo** | ~82 → **2–4** | ~137 → **4–7** | ~275 → **8–14** |
| What it funds | Brand + Reputation + Dinner + Mexican core | + Catering, Specials, Discovery; enough data for Target CPA in ~3 wks | All clusters; fastest learning + competitive reputation headroom |
| Best for | Testing the waters | **Recommended starting point** | Scaling once CPA is proven |

> Read these as *order-of-magnitude ranges*, not promises — "conversions" = tracked Resy clicks/calls, not guaranteed covers, and the low/high spread is why we gather 3 weeks before switching to Target CPA. **The margin lever still holds:** even Scenario A should surface ~2–4 event/catering inquiries/month, and a single Mezzanine buyout ($750–$2,000) or catering job covers the whole month's spend.

**Recommendation:** start at **Scenario B (~$50/day)** — smallest budget that generates enough conversions for Target CPA to work within ~3 weeks. The campaign build in §9 is sized to Scenario B by default.

**Bidding sequence:**
1. **Weeks 1–3:** Maximize Clicks with a max-CPC cap (~$3 dining, ~$5 events/catering) to gather data.
2. **Once conversions have volume:** switch D/G/H/C to **Maximize Conversions → Target CPA**.
3. **Geo bid adjustments** layered on per §2.
4. **Dayparting:** Specials heavy day-of; all campaigns respect open hours (Tue–Thu 11a–9p, Fri–Sat 11a–10p, Sun 10a–4p; Mon closed → pause).

**Conversion tracking — do this BEFORE spending:** Resy reservation click/complete, `karissa@` events inquiry (form + mailto + the events page), catering quote form, phone calls (call extensions + call-from-ads), Fiesta Pack Toast order, loyalty signup. Without it, the margin-weighted budgeting and the CPA switch are blind.

**Ad extensions day one:** Location, Call, Sitelinks (Dinner / Private Events / Catering / Reservations / The Mezzanine), Callout (Locally owned · Walk-ins welcome · Three venues · Free parking), Price (Feast $129, packages from $750), Promotion (Taco Tuesday).

---

## 7. Per-keyword search volume (REAL — Google Keyword Planner, Spokane + Spokane Valley)

> ✅ **REAL DATA — Google Keyword Planner, pulled 2026-06-28, localized to Spokane + Spokane Valley** (last 12 months, Jun 2025–May 2026). This replaces the earlier modeled estimates.
> **Caveat:** with no active campaign yet, Google reports **coarse rounded buckets** (`10–100` / `100–1K` / `1K–10K` / `10K–100K` / `100K–1M`), not exact counts — these sharpen once spend starts. **"Top-of-page bid"** is Google's real bid range (best available CPC proxy). **`<10`** = too little volume for Google to report → treat as **SEO/organic-only, not a paid target.** Competition shows Google's label + indexed value (0–100).

### 🔍 Reality-check: what the real data changed (read this first)

1. **⚠️ The events/private-dining PAID lane is far thinner than assumed.** Every exact-match venue term I'd starred — `private event venue spokane`, `rehearsal dinner venue spokane`, `party venue spokane`, `corporate event venue spokane`, `birthday party venue spokane` — returns **`<10` searches/mo (no data).** Only **`event venue spokane`** and **`event space spokane`** (both 100–1K, Medium) carry real paid volume. **Implication:** you cannot drive events through exact-match paid search — bid the two broad workhorse terms + use broad match, and lean on **SEO / GBP / Meta / referrals** for the rest. Events stay high-margin but are a **low-search-demand** channel; budget accordingly.
2. **`date night restaurant spokane` = `<10`.** Dinner demand is real but lives in **`dinner spokane` (1K–10K!)**, `nice restaurants spokane`, `romantic restaurant spokane`, `best dinner spokane` (all 100–1K). Re-pointed the Dinner cluster to those.
3. **🏆 The Reputation cluster is the sleeper win.** `best restaurants in spokane`, `top restaurants spokane`, `good restaurants spokane` are all **1K–10K, Low competition, $0.12–1.12 bids** — cheap, high-volume, and exactly your "best in Spokane" goal. Fund this *harder* than originally weighted.
4. **Mexican core confirmed cheap & strong:** `mexican restaurant spokane` / `mexican food spokane` both **1K–10K, Low (idx ~10)**, bids as low as **$0.03**. Reliable volume engine.
5. **Brand is wide open:** competition index **0** on every brand term (nobody bidding against you), and `uno mas tacos` is **+900%** 3-month. Capture it cheaply.
6. **Catering > Events for paid:** `catering spokane` (100–1K) plus own-able `taco catering` / `mexican catering`. Better paid prospect than the venue terms.
7. **Biggest raw volume:** `restaurants near me` (**100K–1M**) and `restaurants in spokane` (**10K–100K**) — capture only a sliver via tight radius; supplemental, not core.
8. **Brunch latent demand is large:** `brunch spokane` = **1K–10K** — strengthens the relaunch case, and `mexican brunch spokane` (`<10`) confirms the open lane (own it via SEO before anyone searches it).

> **Net effect on §6 budget weights:** shift dollars **toward Reputation + Dinner (`dinner spokane`) + Mexican core + Catering**, and **down on exact-match Private-Events paid** (move that effort to SEO/GBP + the two broad event terms). Revised ★ ratings are baked into the tables below.

**Columns:** Avg searches/mo = Spokane + Spokane Valley combined. 🔺 = upgraded vs prior plan · 🔻 = downgraded · "SEO" in the ★ column = no paid volume, win it organically.

### A — Reputation & "best / must-try"
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| best restaurants in spokane | **1K–10K** | Low (28) | $0.12–1.12 | ★★★ 🔺 | Cheap + high vol + on-brand. The flagship reputation buy. |
| top restaurants spokane | **1K–10K** | Low (28) | $0.12–1.12 | ★★★ 🔺 | Same cheap/high-vol profile. |
| best dinner spokane | 100–1K | Med (34) | $0.30–1.72 | ★★ | Rising (3-mo +900%). |
| best mexican restaurant spokane | 10–100 | Low (13) | — | ★★ | Low vol but **+900% YoY**; cheap. |
| best new restaurants spokane | 10–100 | Low (23) | $0.18–2.22 | ★ | "New-ish" window (opened Dec 2024). |
| best tacos spokane | 10–100 | Low (11) | — | ★ | Cheap own. |
| must try restaurants spokane | 10–100 | Med (38) | — | ★ | Visitor intent. |
| best locally owned restaurant spokane | `<10` | — | — | SEO 🔻 | No paid volume — own via GBP "locally owned" attribute + content. |
| best margarita spokane | `<10` | — | — | SEO 🔻 | No volume — content only. |
| spokane staple / iconic restaurant | `<10` | — | — | SEO/PR 🔻 | Positioning phrase, not a search term. |
| best happy hour spokane | 100–1K | Med (33) | $0.29–1.38 | ⚠️ skip | Real demand exists — but HH is retired, don't bid. |

### B — Discovery / "where to eat"
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| restaurants near me | **100K–1M** | Med (41) | $0.45–1.74 | ★ | Massive; tight 2–3 mi radius only + heavy negatives. |
| restaurants in spokane | **10K–100K** | Low (26) | $0.33–1.54 | ★★ | Huge + cheap; broad — tight negatives. |
| places to eat in spokane | **1K–10K** | Low (26) | $0.18–1.42 | ★★ | Cheap discovery. |
| good restaurants spokane | **1K–10K** | Low (28) | $0.12–1.12 | ★★ | High vol, cheap. |
| where to eat in spokane | 100–1K | Low (24) | $0.08–0.80 | ★★ | **Cheapest clicks in the whole plan.** |
| fun restaurants spokane | 100–1K | Low (24) | $0.24–1.82 | ★★ | "Get a little lost" fit. |
| north monroe restaurants / restaurants on monroe spokane | 10–100 | Low (7–18) | — | ★★ | Hyperlocal, dirt-cheap own. |
| unique restaurants spokane | 10–100 | Low (16) | — | ★ | Declining (-90%). |
| spokane restaurants open now | 10–100 | Med (36) | — | ★ | Daypart to open hours only. |

### C — Mexican / tacos core
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| mexican restaurant spokane | **1K–10K** | Low (10) | — | ★★★ | Core engine, cheap. |
| mexican food spokane | **1K–10K** | Low (11) | $0.03–3.75 | ★★★ | Cheap, high vol. |
| mexican food near me | **1K–10K** | Low (12) | $0.54–4.33 | ★★ | Tight radius. |
| tacos spokane | 100–1K | Low (14) | — | ★★ | Solid. |
| birria tacos spokane | 100–1K | Low (15) | — | ★★ | Still 100–1K despite a -90% dip. |
| mexican restaurant north spokane | 10–100 | Low (10) | — | ★★ | Hyperlocal own. |
| taco bar spokane | 10–100 | Low (23) | — | ★ | Niche. |
| taco shop spokane / carne asada / surf and turf spokane | `<10` | — | — | SEO 🔻 | No paid volume — menu/SEO pages. |

### D — Dinner / date night
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| dinner spokane | **1K–10K** | Low (26) | $0.54–2.13 | ★★★ 🔺 | The dinner-cluster volume winner — fund it. |
| nice restaurants spokane | 100–1K | Med (39) | $0.39–1.68 | ★★ | Elevated-intent. |
| romantic restaurant spokane | 100–1K | Med (41) | $0.31–2.42 | ★★ | Date/occasion intent (since "date night" has none). |
| best dinner spokane | 100–1K | Med (34) | $0.30–1.72 | ★★ | Rising (+900%). |
| date night restaurant spokane | `<10` | — | — | SEO 🔻 | **No paid volume — was ★★★.** Capture via dinner/romantic/nice instead. |
| group / large group dinner · upscale restaurant · carne asada · surf and turf spokane | `<10` | — | — | SEO 🔻 | No volume — dinner-menu SEO. |

### E — Tequila / cocktails / bar
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| bars in spokane | **1K–10K** | Low (16) | $1.34–4.51 | ★★ | Big vol, pricier clicks. |
| cocktail bar spokane | 100–1K | Low (7) | — | ★★ | Cheap. |
| tequila bar spokane | 10–100 | Low (14) | — | ★★ | Own the identity (vs Table 13 / De Leon's). |
| margaritas spokane | 10–100 | Low (9) | — | ★ | Cheap. |
| espresso martini spokane | 10–100 | Low (1) | — | ★ | Near-zero competition. |
| fun bars spokane | 10–100 | Low (6) | — | ★ | Cheap. |
| espresso margarita / tequila flight spokane | `<10` | — | — | SEO 🔻 | Signature but no search — content/GBP posts. |

### F — Weekly specials / Taco Tuesday
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| taco tuesday spokane | 100–1K | Low (19) | — | ★★★ | **Daypart Mon eve–Tue**; tight radius. |
| taco tuesday near me | 100–1K | Low (17) | — | ★★ | **YoY +900%** rising; 2–3 mi radius. |
| best taco tuesday spokane | 10–100 | Low (7) | — | ★★ | Cheap own. |
| taco tuesday deals · drink/food specials · margarita deals · cheap margaritas · big f’n thursday spokane | `<10` | — | — | SEO/social 🔻 | No paid volume — push via GBP posts + social. |

### G — Private events / venue rental ⚠️ *(thin paid demand — see finding #1)*
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| event venue spokane | 100–1K | Med (63) | $0.38–2.06 | ★★★ | The events paid workhorse. |
| event space spokane | 100–1K | Med (52) | $1.01–2.40 | ★★★ | Second workhorse. |
| private dining spokane | 10–100 | Med (51) | — | ★★ | Mezzanine fit (28 seated). |
| meeting space spokane | 10–100 | High (86) | $2.54–6.13 | ★ | Pricey; weekday corporate. |
| bachelorette party spokane | 10–100 | Low (18) | — | ★ | Cheap. |
| wedding venue spokane | 10–100 | Med (52) | $0.30–2.18 | ★ test | Small capped test. |
| private event venue spokane | `<10` | — | — | SEO 🔻 | **No paid volume — was ★★★.** /private-events page + GBP. |
| party venue · party room · birthday party venue · rehearsal dinner venue · corporate event venue · graduation party venue · holiday party venue · wedding reception venue spokane | `<10` | — | — | SEO 🔻 | **No paid volume.** Win via /private-events SEO, directories (The Knot/Eventective), Meta, referrals. *(Watch `holiday party venue` for a Q4 bump.)* |

### H — Off-site catering
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| catering spokane | 100–1K | Med (53) | $0.99–3.06 | ★★★ | The catering paid workhorse. |
| taco catering spokane | 10–100 | Med (48) | $0.98–3.00 | ★★★ | Own it. |
| mexican catering spokane | 10–100 | Low (23) | $1.66–6.56 | ★★★ | Own it; distinctive cuisine. |
| event catering spokane | 10–100 | High (86) | $1.39–6.16 | ★ | Pricey clicks. |
| wedding catering spokane | 10–100 | Med (52) | $0.65–1.87 | ★ test | Seasonal test. |
| corporate · office · party · taco bar catering spokane | `<10` | — | — | SEO/broad 🔻 | No exact volume — catch via broad match on "catering spokane" + SEO. |

### I — Brand *(competition index 0 — nobody bidding against you)*
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | ★ | Play |
|---|---|---|---|---|---|
| uno mas spokane | 100–1K | Low (0) | — | ★★★ | Own cheap — no competitor bidding. |
| uno mas tacos | 10–100 | Low (0) | — | ★★★ | **+900%** 3-month — growing. |
| uno mas monroe | 10–100 | Low (0) | — | ★★ | Venue/location intent. |
| uno mas tacos and tequila | 10–100 | Low (0) | — | ★★ | Full brand name. |
| uno mas mezzanine | `<10` | — | — | SEO 🔻 | Too new — build awareness first. |

### J — Brunch ▶ LIVE (Sundays 10am–4pm — activate; real demand confirmed)
| Keyword | Avg searches/mo | Competition (idx) | Top-of-page bid | Note |
|---|---|---|---|---|
| brunch spokane | **1K–10K** | Low (22) | $0.33–1.11 | 🔺 Big latent demand — strong relaunch lever. |
| best brunch spokane | 100–1K | Low (20) | $0.02–0.85 | Cheap. |
| sunday brunch spokane | 10–100 | Low (25) | — | Flip on at relaunch. |
| bottomless mimosas spokane | 10–100 | Low (22) | — | Flip on at relaunch. |
| mexican brunch spokane | `<10` | — | — | **Open lane** — nobody searching it yet; own organically first. |

---

## 8. Next steps

1. ✅ **Done — real Keyword Planner numbers pulled (2026-06-28)** and tiered into §7. Google Ads connected via Composio (account 164-990-7395). *(Exact counts sharpen once a campaign is spending.)*
2. **Baseline organic rankings** — connect Search Console (or I run manual SERP checks) so the §1 throttle rule has data. *This is what makes "bid until we rank" operational.*
3. **🚦 GATE: confirm conversion tracking** is wired (Resy click/complete, calls, events+catering form, Fiesta Pack) **before any spend** — §9 is blind without it.
4. ✅ **v1 priority set by the data (§9 build):** Brand + Core Local Search (Reputation / Mexican / Dinner / Discovery / Tequila) + Events & Catering + Taco Tuesday. Exact-match private-events terms moved to SEO.
5. **Confirm GBP** — claim/optimize Google Business Profile (Place ID unconfirmed); biggest organic lever + powers "near me" / Map Pack.
6. **Push the §9 build via Composio** once tracking is live (I can create the campaigns/ad groups/keywords directly), then write the **RSAs per ad group** + SEO page briefs for `/private-events`, `/catering`, `/specials`.

---

## 9. Campaign build spec (v1 — ready to push via Composio)

**Sized to Scenario B (~$50/day · ~$1,500/mo). Account: Uno Más — 164-990-7395 (`customers/1649907395`).**

> ✅ **BUILT & PAUSED via Composio — 2026-06-29.** 4 campaigns · 9 ad groups · 48 keywords · 9 RSAs · 16 geo/schedule criteria · 42 negatives (2 shared lists). Geo rings, schedules, and alcohol-keyword exemptions all applied. **Nothing will spend until (a) conversion tracking is live and (b) campaigns are manually enabled.**
> **Still to add before enabling:** ad extensions/assets (sitelinks, callouts, call, location, price, promotion), real final URLs (all currently → homepage), and `restaurants near me` (held for wk 3).

### Architecture: 4 campaigns, not 10 (budget efficiency)
The §6 weights are real, but **10 separate campaigns would starve Smart Bidding** — each needs ~$10–20/day to learn. So clusters become **ad groups inside 4 campaigns**, split only where *settings* genuinely differ (radius, dayparting, bid cap). Weights are preserved at the ad-group level.

| # | Campaign | Daily budget | Radius (Presence) | Max-CPC cap | Bid strategy | Ad schedule |
|---|---|---|---|---|---|---|
| 1 | **UM \| Brand** | $3 | Spokane 10 mi | $1.00 | Max Clicks | Open hours |
| 2 | **UM \| Core Local Search** | $30 | Tiered 2 mi (+20%) / 5 mi (0%) / 10 mi (−30%) | $2.50 | Max Clicks → Target CPA | Open hours |
| 3 | **UM \| Events & Catering** | $10 | 25 mi + **Coeur d'Alene, ID** + Spokane Valley | $5.00 | Max Clicks → Target CPA | All week 8a–10p (capture leads even when closed) |
| 4 | **UM \| Taco Tuesday & Specials** | $7 | Tight 3 mi | $2.00 | Max Clicks | **Mon 4–10p + Tue 11a–9p heavy;** paused/min other days |

**Open hours** = Tue–Thu 11a–9p, Fri–Sat 11a–10p, Sun 10a–4p; **Mon −80% or paused** (closed). Total = **$50/day.**

### Global settings (all campaigns)
- **Networks:** Google Search only — **Search Partners OFF, Display OFF** for v1.
- **Location option:** "Presence: people in or regularly in" (not interest) — except a small **+interest** allowance on the Reputation/Discovery ad groups for the visitor/trip-planner layer.
- **Language:** English · **Devices:** all (review mobile bid +% after data).
- **Shared negative list "UM – Master Negatives"** (from §4) applied to all 4. ⚠️ **Exclude `cheap`/`deals`/`bogo`/`$6` from Campaign 4** (specials need them).
- **🚦 Conversions must be live first:** Resy click + complete, calls (call asset + on-site), events/catering form (→ karissa@), Fiesta Pack Toast order.

### Keywords by ad group (P = phrase · E = exact · B = broad)

**Campaign 1 — UM | Brand** · AG *Brand*
`[uno mas spokane]` E · `"uno mas spokane"` P · `"uno mas tacos"` P · `"uno mas tacos and tequila"` P · `"uno mas monroe"` P

**Campaign 2 — UM | Core Local Search**
- **AG Reputation/Best-of:** `"best restaurants in spokane"` P · `"top restaurants spokane"` P · `"best mexican restaurant spokane"` P · `"best dinner spokane"` P · `"best tacos spokane"` P · `"must try restaurants spokane"` P · `"best new restaurants spokane"` P
- **AG Mexican & Tacos:** `"mexican restaurant spokane"` P · `[mexican restaurant spokane]` E · `"mexican food spokane"` P · `"mexican food near me"` P · `"tacos spokane"` P · `"birria tacos spokane"` P · `"taco bar spokane"` P · `"mexican restaurant north spokane"` P
- **AG Dinner:** `"dinner spokane"` P · `"nice restaurants spokane"` P · `"romantic restaurant spokane"` P
- **AG Discovery:** `"places to eat in spokane"` P · `"where to eat in spokane"` P · `"good restaurants spokane"` P · `"fun restaurants spokane"` P · `"restaurants in spokane"` P · `"north monroe restaurants"` P · *(HOLD `"restaurants near me"` → add wk 3 at 2 mi only — it's 100K–1M and will eat budget)*
- **AG Tequila & Bar:** `"tequila bar spokane"` P · `"cocktail bar spokane"` P · `"bars in spokane"` P · `"margaritas spokane"` P

**Campaign 3 — UM | Events & Catering**
- **AG Event Venue:** `"event venue spokane"` P + B · `"event space spokane"` P + B · `"private dining spokane"` P · `"meeting space spokane"` P · `private event venue spokane` B *(broad to mine the long-tail event queries that show `<10` individually)*
- **AG Catering:** `"catering spokane"` P + B · `"taco catering spokane"` P · `"mexican catering spokane"` P · `"wedding catering spokane"` P *(test)*

**Campaign 4 — UM | Taco Tuesday & Specials** · AG *Taco Tuesday*
`"taco tuesday spokane"` P · `"taco tuesday near me"` P · `"best taco tuesday spokane"` P

> **Why broad match only in Campaign 3:** exact-match event/catering volume is too thin (§7) — broad + Smart Bidding lets Google surface adjacent queries ("banquet room spokane," "graduation dinner spokane," etc.) we can't see in Planner. Everywhere else, phrase keeps control on a small budget.

### Starter ad copy (one RSA per campaign — tailor per ad group later)
*Paid-ads voice: hook-driven, clarity first, ≤60% clever. **Always "Uno Más" with the accent.***

- **Brand** — H: *Uno Más Tacos & Tequila* · *Modern Mexican on Monroe* · *Tequila Bar + Speakeasy* · *Reserve on Resy* · *Get a Little Lost* · D: *Modern Mexican and a tequila bar at 2020 N Monroe. Walk-ins welcome.* / *Tacos, craft cocktails, a speakeasy upstairs. Come find it.*
- **Core/Reputation** — H: *One of Spokane's Best* · *Modern Mexican on Monroe* · *Tacos, Tequila & More* · *Locally Owned in Spokane* · *Reserve on Resy* · D: *Serious food, a room that does the work, cocktails worth staying for. 2020 N Monroe.* / *Lunch, dinner, and a speakeasy upstairs. Get a little lost.*
- **Events & Catering** — H: *Private Events in Spokane* · *Book The Mezzanine* · *Taco & Mexican Catering* · *Receptions to Full Buyouts* · *Your Group, Your Space* · D: *A speakeasy for 28, patio takeovers, buyouts to 200. Let's build your night.* / *Off-site Mexican + taco catering. Tell us the headcount — we handle the rest.*
- **Taco Tuesday** — H: *Taco Tuesday on Monroe* · *BOGO Street Tacos* · *$6 Margs, $30 Pitchers* · *Your Midweek Ritual* · D: *BOGO lunch street tacos, $6 margaritas, $30 pitchers. Every Tuesday at Uno Más.* / *2020 N Monroe. Taco Tuesday, the way it should be.*

**Final URLs** (⚠️ site mid-migration to Lovable — build/confirm these pages, fall back to homepage): Brand/Core → `unomastacoshop.com` (or `/menu`) · Events → `/private-events` · Catering → `/catering` · Specials → `/specials`.

### Ad extensions (assets) — all campaigns
Location · Call (509-960-7989) · Sitelinks (Menu / Reservations / Private Events / The Mezzanine) · Callouts (Locally owned · Walk-ins welcome · Three venues · Free parking) · Price (The Feast $129, Packages from $750) · Promotion (Taco Tuesday).

### Build sequence (what I'll do via Composio)
1. **You confirm conversion tracking is live** (the gate).
2. I create the **shared negative list** + the **4 campaigns** with settings above.
3. I add **ad groups + keywords** with match types.
4. I add **RSAs** (tailored per ad group) + **assets/extensions**.
5. Leave **paused for your review** → you approve → enable.
6. Add geo bid-adjustment rings on Campaign 2; set Campaign 4 dayparting.

> I can execute steps 2–4 now and leave everything **paused** so nothing spends before tracking + your sign-off. Just say go.

---

## Open questions for Ramsey
*(Resolved: goal = balanced · CdA = in · wedding = small test · build = consolidated campaigns + bid-adjustment rings.)*
1. **Monthly ad budget** — confirm the number. Build defaults to **Scenario B ($50/day)**; I'll rescale the per-campaign budgets to whatever you set.
2. **🚦 Is conversion tracking live?** Resy click/complete, calls, events+catering form, Fiesta Pack. **This gates spend** — but I can build everything *paused* before it's done.
3. **Landing pages** — are `/private-events`, `/catering`, `/specials` built on the new Lovable site yet, or should ads point to the homepage for now (and do I draft those page briefs)?
4. **Green light to push the §9 build via Composio (paused for your review)?**

---
*Companion: [seo-keyword-research.md](seo-keyword-research.md) (organic foundation) · [master-reference.md](master-reference.md) (operations). §7 volumes = real Keyword Planner data (2026-06-28, Spokane + Spokane Valley); exact counts sharpen after spend begins.*
