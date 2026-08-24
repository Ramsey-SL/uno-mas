# Uno Más Ecosystem Changelog

> Append-only. Every propagated information change gets one entry, newest at the top.
> Written by the Ecosystem Steward at the end of each `/unomas-update` run.
>
> **Format:**
> ```
> ## YYYY-MM-DD — <short title>  [F#]
> **Change:** what changed, old → new.
> **Owner updated:** <canonical surface>
> **Mirrors updated:** <surface> · <surface> · …
> **Manual pending:** <surface: what Ramsey still needs to click>  (or "none")
> **Commit:** <sha>  ·  **Deploy verified:** <evidence, or n/a>
> **Notes:** drift found, rulings made, follow-ups.
> ```

---

## 2026-08-23 — Gift card promo LOCKED: Wed Aug 26 → Sun Aug 30, physical card at checkout  [F7]
**Ruling:** Ramsey locked **Wed 2026-08-26 → Sun 2026-08-30**, fulfilled as a **physical gift card handed over at checkout.**
**Caught before print:** the mockups still read **"This week only · Tue–Sun"** — factually wrong once the start moved to Wednesday. All three artboards now read **"Wed–Sun · Aug 26–30"** and were re-rendered, re-inspected, and re-exported to the HQ exports folder.
**Overlap accepted (Ramsey's call).** Late Night launches Fri Aug 28, so Fri/Sat run both offers and **they stack.** Defensible: the gift card is deferred credit, not a discount, so the Fri/Sat check still closes at full margin and the cost moves to a future visit. **Consequence recorded:** this promo *is* the Aug 28–30 weekend test (test 4) — do not schedule a separate weekend offer on top, since three offers on one ticket is where margin actually breaks.
**Staff script extended** for the overlap: staff must not imply the gift card replaces late-night pricing, must not invent a restriction, and if asked whether the offers stack the answer is **yes**.

**✅ Inventory resolved: 200 cards on hand** (confirmed by Ramsey) — comfortably above the 75–125 sizing; would need ~40 qualifying checks/day to exhaust. Recorded the liability math (200 issued at a 70/30 $10/$20 split ≈ **$2,600 future liability against ≥$13,000 of qualifying revenue — ~20%, deferred, minus breakage**, which is precisely why it beats an immediate 20% discount), a **Friday-morning tripwire** (under 60 = normal; 80+ = prep the IOU fallback; 120+ = reorder), and a note separating the two wins: issuing all 200 proves the *threshold* worked, cards coming back proves the *bounce-back* worked — **judge the promo on return rate, not sellout.**

**Original risk framing (now resolved) — physical inventory.** Physical fulfillment introduces the one failure mode that embarrasses you: running out mid-promo, which turns a generosity play into a broken promise. Added to the brief: count stock now; rough sizing of **75–125 cards** if 15–25 checks/day clear $50 over five days; prepare a written-IOU fallback; decide whether servers or only managers can activate (manager-only is a service bottleneck on a Friday night); and **record issued card numbers** so return rate is measurable — that's the entire metric for this test.

**Mirrors updated:** gift-card brief (status, dates, physical fulfillment, overlap, inventory section, staff script) · all three mockup artboards · `campaigns/weekend-promos/executions-log.md` test-4 row.

## 2026-08-23 — Weekend offers reframed as a rotating test · gift card starts Wed  [F7]
**Corrections from Ramsey:** (1) the **$10-off-$60 offer is OVER** — it was the *first* of a series, not a standing offer; (2) test 2 was **2 House Margs + Chip & Dip Trio $30**; (3) test 3 is **Full Send $45/$65, running this weekend Aug 22–24**; (4) the **gift-card promo starts Wednesday Aug 26.**

**The reframe that matters:** weekend offers are a **rotating weekly TEST**, not standing offers. The repo had `weekend-campaigns-and-flows.md` describing $10-off-$60 as a **"locked offer"** — that framing was wrong and has been retired with a banner; its subject lines, SMS copy and brunch nudges are now marked retired creative. Its always-on nurture flows (welcome, win-back, birthday, post-visit) remain valid.

**Pattern named in `campaigns/weekend-promos/executions-log.md`:** the four tests move **deliberately away from discounting** — straight discount ($10 off) → fixed bundle ($30 margs+trio) → bundle ladder ($45/$65 tiers) → **deferred credit (gift card)**. Each step protects more margin than the last while still reading as generous. Test 4 is the strongest structure and is the natural default to beat.
**Measurement gap flagged:** four experiments are running with no recorded results. Added what to measure — check average vs. a control weekday, redemption rate, attach rate on bundles, and for the gift card the **return rate and second-check average**. Recommended logging the three completed tests before Wednesday. ⚠️ The Toast dashboard is the tool but **its API credentials currently fail auth** (registry §4).

**Mirrors updated:** `weekend-campaigns-and-flows.md` (retired banner) · `cantina-club-RESUME-HERE.md` (stale "locked offer" pointer) · `handoff-2026-08-20-integration.md` item 4 resolved · `campaign-architecture.md` Fri–Sun row · `ecosystem-registry.md` §4 item 15 rewritten · gift-card brief conflict 1 closed.

**Gift card promo: starts Wed 2026-08-26. End date still open** — flagged that running past Thursday collides with both the Aug 28–30 weekend test slot and the **Late Night launch on Fri Aug 28**, where a guest could hit $50 on discounted Late Night items and still earn a gift card. Three options given; **recommended Wed–Thu only** — clean, protects the Late Night launch, and lifts the two genuinely slow nights.

## 2026-08-23 — Late Night ruled FRI + SAT only  [F3]
**Ruling:** Ramsey confirmed **Late Night runs Friday and Saturday only, 8–10pm.** This resolves the blocker raised in the same-day brief — Tue–Thu close at 8pm, so a weekday late-night program would have required an hours change.
**Consequence: no hours change needed**, so nothing propagates to Supabase `business_hours`, the site's JSON-LD, GBP, Apple, Yelp, or Resy. That's the cheap path, and it launches on existing labor.
**Owner updated:** `CLAUDE.md` "Always Get Right" now carries Late Night as a named daypart with its full offer, the Fri–Sat constraint and the reason for it, and the two copy guards.
**Mirrors updated:** `marketing/master-reference.md` (weekly specials + the `site_events` seeding list) · `marketing/knowledge-center/venue-and-operations.md` · `marketing/knowledge-center/menu-and-offers.md` (menu table + v2.5 changelog) · `marketing/campaign-architecture.md` (new Fri+Sat row in the per-day program table, framed as a **new occasion** rather than a discount on an existing one) · **`marketing/brand-context-pack.md`** — the ChatGPT/Gemini bridge, so the new daypart reaches those assistants instead of being re-seeded stale · `AI-PLATFORM-ACCESS.md` current-facts block.
**Copy guards recorded everywhere the offer appears:** always **"Two Street Tacos — $10"**, never "$10 tacos" (Big A** tacos are already $10 each) · **tacos only, no side** (the 2-tacos-plus-side combo stays $16.50).
**Launch date assumed 2026-08-28** (the first Fri of "next week"). Flagged — correct it if the intent was 2026-09-04.
**Still open:** confirm the **$7 paloma** against the current cocktail price · gift-card promo dates · whether the locked $10-off-$60 weekend offer pauses.
**Not yet done:** add Late Night to the site as a menu daypart (`menu_sections`/`menu_items` already support dayparts), Toast email, GBP post.

## 2026-08-23 — Late Night menu + Gift Card bounce-back: briefs & mockups built  [F2, F3, F7]
**Built two campaigns from Ramsey's brief.**

**Late Night menu** (`marketing/campaigns/late-night-menu/`) — 8–10pm: $6 margs, $30 pitchers, $7 palomas, pick any two street tacos $10. Taco list pulled from the **lunch** menu per instruction, minus Camaron (shrimp): Carne Asada, Al Pastor Chicken, Carnitas, Barbacoa, Batata, Hongos.
🔴 **BLOCKER surfaced: 8–10pm does not fit current hours.** Tue–Thu close at **8pm** (Supabase `business_hours`, matching live JSON-LD); Sun closes 4pm; Mon closed. **The menu can only run Fri–Sat as written.** Mockup built Fri–Sat; three options documented with a recommendation (launch Fri–Sat, then test 7–9pm midweek rather than extending hours on a hypothesis).
**Pricing conflicts flagged:** two tacos à la carte is $13 so $10 is a 23% discount, but the *2 tacos + side* combo is $16.50 — staff need the "tacos only, no side" line · **$10 already means "one Big A** taco"** on the menu, so always write "Two Street Tacos — $10" · **$6 margs is Taco Tuesday's price**, recommend accepting it since one memorable price beats two competing ones · confirm the $7 paloma against current menu price.

**Gift Card bounce-back** (`marketing/campaigns/gift-card-bounceback-aug2026/`) — spend $50 → $10 gift card, spend $100 → $20. Flat 20% at both tiers. Full brief: why the mechanic beats a discount (first visit at full margin, buys the second visit, breakage favors the house, cards walk out as gifts, reads generous not desperate), mechanics, staff script, channels, copy.
**Conflicts flagged:** the **$10-off-$60 weekend offer is a locked standing offer** in `weekend-campaigns-and-flows.md` and overlaps — a $60 check could take $10 off *and* a $10 gift card (33% off). Recommend pausing it this week. Also recommend **not** overlapping with the Late Night launch. Per-check guard needed or tables will split checks. **No printed expiry** — WA restricts gift-card expiration. Alcohol-threshold legality flagged for Ramsey to confirm, not advised on.

**Collateral:** `late-night-menu-mockup.html` (1080×1350) · `gift-card-promo-mockups.html` (three artboards: 1080×1350 feed, 1080×1920 story, 750×1050 table tent @150dpi). Both use verified Cloudinary transforms — real wordmark, real DAM taco line-art, house icon-pattern texture — and **no photography**, which sidesteps the `needs-hires-swap` print gate entirely. Illustrated promo-card system for the offer creative, per `campaign-architecture.md` §4b; the menu uses the navy/dark treatment.
**Rendered PNGs → `~/Documents/Uno-mas-hq-2026/exports/2026-08-23-latenight-and-giftcard/`** per the design skill's export rule.
**Design QA:** first render had colliding headline lines (Antonio at `line-height:.84` over three lines), ungridded tiers, and ~400px of dead space. Fixed leading to `.92`, moved tiers to a CSS grid so the arrows and cards align on a column axis, and redistributed vertical rhythm. Re-rendered and inspected.

**Needs a ruling:** Late Night days (Fri–Sat vs extend hours) · gift-card promo dates (Tue Aug 25 – Sun Aug 30?) · whether the $10-off-$60 pauses · per-check guard · alcohol-threshold legality.

## 2026-08-21 — Schema.org logo + entity graph fixed · HQ library registered · agent snapshot  [F9, infra]
**SEO fix (Lovable `e62848eb` + `1738f4f6`):** the Organization `logo` pointed at **`VenueInterior_FINAL_11` — a dining-room photo**, which Google uses for knowledge-panel branding.
- Now `UM_Logo_-_T_T-Pink_g7pvjz` (the real primary wordmark, pink-on-transparent, 3077×1577) delivered as `b_white,c_pad,w_1200,h_615,q_auto,f_jpg` — aspect matches native **1.951** exactly, flattened onto white so it renders wherever Google composites it.
- **Entity-graph cleanup found in review:** the homepage `Restaurant` node had **no `@id`**, so it and the new `Organization` node read as two unlinked businesses with the same name. Added `@id: #restaurant`, a `logo`, and `parentOrganization → #org`; added the same `parentOrganization` link on `/about`, which had both `@id`s but no relationship between them.
- **Verified live:** both `/` and `/about` now emit `#restaurant` → `parentOrganization` → `#org` with the wordmark as `logo`. `og:image`/`twitter:image` deliberately left as photos — a logo would look wrong on a share card. `VenueInterior_FINAL_11` retained in its three legitimate photo uses.

**Local HQ library registered (tier 4):** `/Users/ramseypruchnic/Documents/Uno-mas-hq-2026` is now a formal agent **destination and reference library** — `listings/ menus/ promos/ photos-video/ reference/ exports/`, each with a README stating the rules. Registered in registry §2, wired into `unomas-find` (search it, and write gathered files there) and `unomas-design` (rendered exports go there since the repo `.gitignore` blocks binaries). `scripts/build-listings-kit.sh` now defaults its output to `listings/`. The 2026-08-21 listings kit was moved into it.
**Rules recorded:** it is **not** a source of truth — facts go to the repo, web-ready assets go to Cloudinary with proper naming, masters go to the LaCie Drive, nothing is deleted without asking.

**Agent snapshot:** `um-marketing-agent/` in the HQ folder — a portable copy of the three skills, the steward, `AGENT-ACCESS.md`, the bootstrap script, the ChatGPT context pack, and brand-brain/registry snapshots, plus a `refresh.sh` so it can be re-synced instead of silently drifting. Clearly marked as a snapshot; the repo `.claude/` remains canonical.

**Second fix NOT done — asset renaming.** The 31 non-conforming public_ids (registry §4 item 19) need **Cloudinary write access, which is not authorized in this environment** and no local Master API key exists. See Notes for the recommended approach.
**Notes:** ⚠️ **Recommendation: tag rather than rename.** Renaming a Cloudinary public_id changes its delivery URL, which would break every live-site reference until a coordinated redeploy — real downtime risk for a cosmetic gain. **Adding `category-*` and campaign tags to those 31 assets achieves the actual goal (findability) with zero breakage.** Awaiting Ramsey's call + Cloudinary authorization.

## 2026-08-21 — Critical dependency vulnerability fixed · local-listings asset kit built  [infra, F9]
**Security fix (Lovable commit `f2778912`, deploy `cc22a9bb`):** cleared **GHSA-mv8w-475r-vwqw** — a `seroval` `fromJSON()` Promise-resolver type-confusion, vulnerable ≤1.5.2.
- **Diagnosis correction:** the TanStack packages already declared `seroval: "^1.5.0"`, so their ranges permitted the patch — bumping TanStack would have changed nothing. **The lockfile was pinning 1.5.2 in four nested trees.**
- Fix: `overrides` in `package.json` pinning `seroval` + `seroval-plugins` to **1.6.2**; stale nested `node_modules` copies removed; `bun.lock` regenerated as text. **TanStack versions untouched** (`react-router` 1.168.25, `react-start` 1.167.50, `router-plugin` 1.167.28).
- Verified: typecheck exit 0, production build exit 0, dependency scan clean (no high/critical), finding marked fixed. Dependency-only change → rolls back cleanly.
- **Post-deploy SSR health check** (a dep change can break SSR): all 8 routes HTTP 200 with full byte counts and JSON-LD intact; homepage dynamic sections (Big F'N Thursday, Taco Tuesday, hours, Cantina Club band) all rendering.

**Local listings kit (new):** `marketing/local-listings-asset-kit.md` + `scripts/build-listings-kit.sh`.
- Copy-paste NAP / hours / 750-char description / attributes / categories for GBP, Apple Business Connect, Yelp, Bing, TripAdvisor, Resy, socials.
- Photo shortlist **sourced by scraping the live site's own Cloudinary references** — 62 images + 8 videos, all already approved and in production use, and all clear of `needs-hires-swap`.
- Script downloads a dated folder with **7 per-platform crop profiles generated server-side by Cloudinary** (Google cover/additional, Apple hero, Yelp wide, social 4:5 and 9:16, square) plus the house grade — no manual resizing. Ships an UPLOAD-CHECKLIST and keeps Mezzanine assets in a separate folder so the sub-brands never mix.
- Menu/promo pointers: Canva dinner `DAHDBfNpwpg`, brunch `DAHPnEFIfAU`, and the live `uno-mas/website/promos/pick-your-full-send-aug2026` card.

**New findings logged:** (18) the site's schema.org Organization `logo` points at an **interior photo**, not a logo — Google uses it for knowledge-panel branding; (19) **31 live assets violate the naming convention** and are unsearchable.
**Manual pending:** unchanged — rename the loyalty program in Toast, rename the Toast organization, rename TripAdvisor.

## 2026-08-21 — Loyalty naming propagated to the live site  [F8]
**Change:** Removed the deprecated **"Uno Más Rewards"** program name from the live site, per the 2026-08-20 ruling (one program, The Cantina Club, free).
**Surfaces updated** (Lovable commits `9952ec2d` + `ec088f84`, deploy `375fa9f9`):
- `src/components/CantinaClubBand.tsx` — homepage eyebrow "Free to join · Uno Más Rewards" → "Free to join" (the "The Cantina Club" H2 sits directly below, so re-stating the name would duplicate it).
- `src/routes/about.tsx` — body copy → "Cantina Club members spend 107% more…". FAQ JSON-LD verified already correct.
- **`src/routes/cantina-club.tsx`** — meta description → "Join The Cantina Club free…"; eyebrow → "Free to join". *(An entire `/cantina-club` page the registry did not know about — found by the codebase grep, now added to the registry route list.)*
- `src/components/CantinaClubPopup.tsx` — label → "Free to join".
- `public/llms.txt` — → "The Cantina Club (free loyalty program)."
**Deliberately NOT changed:** the two mock phone/SMS previews (`CantinaClubBand.tsx:187`, `cantina-club.tsx:601`) quote the **real Toast message verbatim** — "Welcome to Uno Más Rewards: The Cantina Club, Powered by Toast!". Editing them would make the site misrepresent what guests actually receive. **The real fix is renaming the program inside Toast Loyalty** — see Manual pending.
**Verified:** live audit — `/about` 0 hits; `/` and `/cantina-club` 1 hit each, both the Toast quote.
**Paid-tier audit:** grepped the site for paid/membership/subscription/tier/Cantina Member/Cantina OG/La Familia. **No public copy implies the Club is paid or tiered.** Two pages actively *deny* it ("no subscription, no tiers to climb", "no tier you have to climb") — keep that language, it's on-message.
**Manual pending:** rename the loyalty program inside **Toast** (drops the "Uno Más Rewards:" prefix from the guest SMS, which then makes the site's quote accurate) · rename the Toast **organization** to "Uno Más Tacos & Tequila" (registry §4 item 14).
**Notes:** ⚠️ Lovable's security scan flagged a **pre-existing critical supply-chain vulnerability** — `seroval` deserialization via `@tanstack/react-router` / `react-start` / `router-plugin`, scan stale. Deployed anyway: those packages were already live, and this was a text-only change, so holding it would not have reduced exposure. **Logged as real work — see registry §4 item 17.**

## 2026-08-20 — Loyalty ruled: ONE free program (The Cantina Club) · 3 weekend promos logged  [F8, F4]
**Change:**
1. **RULING — there is ONE loyalty program: The Cantina Club, and it is FREE.** Paid tiers (Cantina Member / Cantina OG / La Familia) are a **future-state idea, not live**, and must never be marketed or publicly referenced. This closes a naming muddle across four sources and overrides the Aug 2026 handoff's "The Guest List."
2. **Three real weekend promo executions captured** from Toast email PDFs — offers the repo did not have.
**Owner updated:** `CLAUDE.md` loyalty line is now canonical: The Cantina Club, free, paid tiers future-state, "Uno Más Rewards:" prefix deprecated.
**Mirrors updated:** `marketing/campaign-architecture.md` §2/§6/§7 · `marketing/mas-rewards-loyalty-playbook.md` (banner rewritten) · `marketing/cantina-club-program-spec.md` (paid/two-tier framing marked FUTURE-STATE, not a description of what exists) · `.claude/skills/unomas-design` · registry §4 items 11–12 closed.
**Added:** `marketing/campaigns/weekend-promos/executions-log.md` — the MICKEY code-word $60/$10 offer, the $30 two-margs + Chip & Dip Trio special, and the $45/$65 "Pick Your Full Send" bundle ladder, with menu items verified against the repo.
**Also captured:** `campaign-architecture.md` §4b now documents **two creative systems** (photographic for experience, illustrated promo-card for offers) with the illustrated system's full token recipe, and `/unomas-design` routes between them.
**New conflicts logged:** (14) Toast org name is "Uno Mas Taco Shop" — no accent, uses a banned phrase, and it's in **every** Toast email footer; (15) the weekend redemption phrase is a rotating variable — "Mickey" vs "Mas Please" vs `WEEKEND10`; (16) "Full Send" is used three ways.
**Manual pending:** rename the Toast organization to "Uno Más Tacos & Tequila."
**Notes:** ⚠️ The **Cantina Connect app** was built around paid tiers, Stripe billing, and monthly credits — that build is **ahead of the business**. Flagged in registry §4 as future-state infrastructure rather than a live program. Ramsey offered to upload recent promo SMS/emails — more executions welcome.

## 2026-08-20 — Big F’N Thursday: pricing scope + BFQ naming convention ruled  [F2, F4]
**Change:** Two rulings from Ramsey closing the open questions on the new Thursday promo.
1. **$10 is the BASE BFQ price.** Protein add-ons are charged on top at normal menu prices (Skirt Steak +$9 · Carnitas +$7 · Grilled Chicken +$6). A Thursday BFQ with carnitas is $17.
2. **The two BFQ renderings are intentional, not drift.** Menu keeps `The Big F*** Quesadilla (BFQ)`; marketing uses `Big F’N Quesadilla`. Menu language stays exactly as it is.
**Owner updated:** `CLAUDE.md` §Brand Name Rule now carries both the BFQ rendering convention and the pricing rule, so neither gets "corrected" by a future pass.
**Mirrors updated:** `marketing/campaigns/daily-specials/big-fn-thursday-creative-spec.md` · `marketing/ecosystem-registry.md` (conflicts 9 and 10 closed; 9 reclassified as a convention).
**Manual pending:** unchanged from the previous entries — GBP attributes + specials post, social Thursday graphic, Klaviyo Thursday flow.
**Notes:** Photography deferred by Ramsey — no BFQ hero shot needed yet; poster and AI-prompt set still to build. **Recommend** adding a `Proteins additional` qualifier to the live homepage Thursday tile (currently just "$10 Big F’N Quesadilla"), since the base-price framing isn't obvious to a first-time guest — not changed, awaiting Ramsey's call.

## 2026-08-20 — Mezzanine 21+ stripped from the live site (follow-up ruling)  [policy]
**Change:** Ramsey ruled **no 21+ anywhere, The Mezzanine included**, and confirmed **Tue–Thu close at 8pm**.
**Owner updated:** `CLAUDE.md` — the policy line now states the ruling *and* names the only two surviving exceptions, so it can't be quietly re-added.
**Live site updated + deployed** (Lovable commit `d17dd26f`, deploy `ff1424c1`):
- `src/routes/mezzanine.tsx` — "Is the Mezzanine 21+?" → "Can we bring kids to the Mezzanine?" in BOTH the visible FAQ and the FAQPage JSON-LD; hero subtitle "Private 21+ dining & event space" → "Private dining & event space".
- `src/routes/about.tsx` — removed the `21+ / After 9pm, by design` stat badge; Mezzanine card copy now ends "The room for the nights that matter."
- `src/routes/index.tsx` — cocktails card eyebrow "21+ · All Service Hours" → "All Service Hours".
- `src/components/MenuCollection.tsx` — cocktails eyebrow "Cocktails & Tequila · 21+" → "Cocktails & Tequila" *(a mirror I hadn't found in the repo — the Lovable agent caught it on the codebase grep)*.
**Verified:** `/`, `/about`, `/mezzanine`, `/fiesta-box`, `/catering`, `/private-events`, `/now-hiring` audited on the live domain. `/about`, `/catering`, `/private-events`, `/now-hiring` clean. The only 21+ strings left site-wide are the Love Island event (copy + `typicalAgeRange`), the Fiesta Box alcohol notes, and the negating phrase "there's no 21+ window" in the new Mezzanine FAQ answer.
**Hours:** 8pm confirmed — no further action; Supabase and the site were already correct.
**Manual pending:** GBP still needs the Family-friendly / Good-for-kids attributes set to all hours, and any "21+ after 9pm" removed from the GBP description and Q&A.
**Notes:** Repo needed no further edits — remaining 21+ references there are all Love Island, Fiesta Box alcohol, or Cantina Club age verification, all correctly retained.

## 2026-08-20 — Taco Tuesday $6 ruling · no 21+ window · Big F’N Thursday replaces Burrito Thursday  [F3, F1, policy]
**Change:**
1. **Taco Tuesday = $6 margs / $30 pitchers** (ruling). Repo and live site already agreed at $6; the stray "$9" existed only in a session memory note. No repo edit needed — conflict closed.
2. **Kid-friendly at all times — NO 21+ window** (ruling). Removed the house-wide "21+ after 9pm" claim everywhere it appeared.
3. **Thursday promo replaced.** Burrito Thursday ($15 House Burrito or Bowl) → **Big F’N Thursday** ($10 Big F’N Quesadilla "BFQ" · $10 menu tequila cocktail fresh sheet, new cocktails every Thursday). Source: the live site, which was already running it — the repo was 27 files behind.
4. **Hours corrected** Tue–Thu 11am–9pm → **8pm** in `CLAUDE.md`, to match canonical Supabase `business_hours` + live JSON-LD.

**Owner updated:** F3 specials → `CLAUDE.md`. F1 hours → already correct in Supabase `business_hours` (no DB write needed; the mirror was wrong).
**Mirrors updated (27 files):** `CLAUDE.md` · `marketing/master-reference.md` · `marketing/brand-context-pack.md` · `marketing/website-homepage-v2.md` · `marketing/seo-page-briefs.md` · `marketing/paid-search-and-seo-keyword-plan.md` · `marketing/local-seo-gbp-reviews-playbook.md` · `marketing/quick-reference/{EMAIL_SMS,SOCIAL_MEDIA}_PLAYBOOK.md` · `marketing/knowledge-center/{menu-and-offers,venue-and-operations,audience-personas,brand-voice}.md` · `marketing/brand-guidelines/{04-voice-and-tone,08-social-copy-examples,09-menu-product-context}.md` · `brand-intelligence-center/{customer,differentiation,messaging-framework,system-prompt}.md` · `website/SITE-STATUS.md` · `marketing/campaigns/daily-specials/{creative-copy,campaign-brief,web-package,creative-brief,chatgpt-prompts}.md` + `{table-tent,poster-midweek-lineup,specials-page-preview}.html`
**Retired:** `poster-burrito-thursday.html` → `_RETIRED-2026-08-poster-burrito-thursday.html`. `_gallery.html` is generated — regenerate to pick up the new copy.
**Also fixed in passing:** Masa Coated Fries $7 → $8 (pre-existing uncommitted edit, now committed) · `SITE-STATUS.md` pixel + day-deal-icon staleness · production domain `unomastacoshop.com` confirmed CONNECTED (registry said otherwise).

**Manual pending:**
- **Google Business Profile** — set Crowd/Planning → *Family-friendly (all hours)*, Children → *Good for kids (all hours)*; remove any "21+ after 9pm" from the description/Q&A; update the specials Post to Big F’N Thursday.
- **Instagram / TikTok / Facebook** (via Vista Social) — Thursday specials graphic + any pinned midweek-lineup post still says Burrito Thursday.
- **Klaviyo** — Thursday flow/campaign copy still references $15 burritos & bowls.
- **New Thursday creative needed** — poster (4:5), table-tent art, and an AI-image prompt set for Big F’N Thursday (hero: big griddled quesadilla, cut, cheese pulling, beside a tequila cocktail; accent Blue `#18BCDC`).

**Commit:** see below  ·  **Deploy verified:** n/a — **no Lovable change made.** The live site was already correct on both Thursday and $6 margs.
**Notes / needs a ruling:**
- **Mezzanine 21+ scope** — every remaining 21+ reference on the live site is Mezzanine- or event-scoped (`/about` card, `/mezzanine` copy + FAQ JSON-LD, homepage card, Love Island event, Fiesta Box alcohol). Is the Mezzanine 21+ always, after 9pm, or not at all? No site change made pending the answer.
- **Confirm Tue–Thu close at 8pm** (not 9pm) — I trusted Supabase + live JSON-LD over `CLAUDE.md`.
- **`site_events` is empty** and the homepage hardcodes specials/hours — so this propagation could not be done via the DB. Seeding `site_events` + wiring the homepage to read it remains the structural fix for F1/F3/F7 drift.

## 2026-08-20 — Ecosystem Steward agent created  [infra]
**Change:** Stood up the Uno Más Ecosystem Steward — a registry-driven agent that propagates
information changes across every surface and locates files anywhere in the ecosystem.
**Added:** `marketing/ecosystem-registry.md` (surface inventory, F1–F12 propagation matrix, gotchas,
known conflicts) · `.claude/skills/unomas-update/` · `.claude/skills/unomas-find/` ·
`.claude/agents/unomas-steward.md` · this changelog · `CLAUDE.md` pointer.
**Manual pending:** none.
**Notes:** Registry §4 logged 6 live conflicts found during the build — Taco Tuesday marg price
($6 vs $9), the 21+ policy contradiction between `CLAUDE.md` and `master-reference.md`, a stale
`SITE-STATUS.md` pixel note, the unrotated Gemini key, the trailing-space Drive folders, and
uncommitted work in `menu-and-offers.md`. All await a ruling from Ramsey.
