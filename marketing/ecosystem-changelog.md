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

## 2026-08-25 — Cloudinary operating guide · daily-special banner set · week-wide Meta ads  [F7, F9]
Three deliverables in one pass.

**1 · `marketing/cloudinary-operating-guide.md`** — consolidated the DAM rules that were spread across the registry, `dam-workflow.md`, `dam-asset-manifest.md` and the design skill into one reference: structure, naming (`YYYYMMDD_UM_<CAT>_<Subject>_v#`), the tag layer, the **print gate**, standard transforms, upload procedure, credit budget, MediaFlows build order.
🔴 **Recorded honestly that I cannot audit the DAM** — no local credentials, connector unauthorized. Listed what to authorize and the four things I'd check first, including the dangerous case: **a low-res asset *missing* the `needs-hires-swap` tag.**

**2 · Daily-special banner set** (`campaigns/daily-special-banners/`, served at `:8791`) — Wed, Thu, Fri/Sat and Sun tiles built in the **exact structure of the live Taco Tuesday tile**, all reusing `useIsSpokaneDay(day)`. Built as a **series on purpose**: a guest who learns the shape once reads any day at a glance, and the specials feel like a programme rather than five unrelated promos.
**Two decisions raised rather than assumed:** (a) **Late Night is 8–10pm** — recommended extending the hook to take an hour range so the Fri/Sat tile appears from ~4pm, since a "tonight" promise at lunchtime is weaker than the same promise at 5pm; (b) **Sunday may be redundant** — the homepage already has a `SundayBrunchFeature` band, and one strong block beats two competing ones.

**3 · `campaigns/meta-ads-day-of-week.md`** — ads for the whole week, 11 variants, all counts verified with **zero failures**. Stayed in the ritual/clean-stack lane Ramsey picked; no price-contrast hooks.
**The governing rule, stated once and applied per day:** *the hook must be true at the moment it's seen.* Tue/Wed/Thu run all-day copy in one ad set; **Fri/Sat and Sunday must be dayparted**, because an 8–10pm offer and a 10–4 brunch are the two cases where copy genuinely cannot save the schedule.
**Flagged:** T-B ("new tequila cocktails every single Thursday") is the sleeper — **the only offer all week that gives a reason to come *back* rather than just come once.** Also that Thursday has **no BFQ hero photo** in the DAM, and that budget should favour **Wednesday and Sunday** — softest demand, biggest upside.

## 2026-08-25 — Gift card: offer stays Wednesday, marketing launch moves to Thursday  [F7]
**Ramsey wanted the launch pushed to Thursday. Flagged a timing conflict first:** the Tuesday SMS had **already gone out at 11am** saying the drop *"starts tomorrow"* — so a straight move to Thursday would have made a live message untrue. Gave three options rather than silently repointing dates.

**His resolution — and it's the cleanest one:** the team gets what it needs to **execute from Wednesday**, while the **big pushes and announcements happen Thursday.** So the campaign now has **two dates, not one:**
- **Offer live: Wed Aug 26 → Sun Aug 30** (unchanged — the SMS stays accurate)
- **Marketing launch: Thu Aug 27**

**Restructured accordingly:**
- **Wednesday = soft open, no consumer send.** Offer works for walk-ins; table tents out; team briefed; cards pre-loaded. Recorded *why* no send: doubling the announcement across two days splits attention and makes Thursday feel like a repeat.
- **Thursday = the anchor day**, carrying both the email (10–11am, explains) and the SMS (3–4pm, drives that night).
- **The email's "tonight" section changed from Beer & Bites to Big F'N Thursday** — a "tonight" block must always name the day it actually lands on. That's the kind of thing that survives a date move unnoticed and then reads as sloppy.
- Added a note not to write "starts today" in Thursday's email, since the offer will have been running since Wednesday.

**Risk recorded prominently:** a soft open only works if **staff are briefed before Wednesday service.** Anyone who saw Tuesday's SMS may ask, and a blank look is worse than no announcement.
**Pattern captured** in `campaign-architecture.md` §4c — an offer window and a launch day can be separated deliberately, on the condition that staff are ready first.
**Propagated:** brief · send plan · executions log · campaign-architecture · HQ README and SMS file.

## 2026-08-25 — Chef doc final: sign-off block removed  [F2]
**Ramsey:** *"remove the sign-off section, everything else is good."* Removed. The doc is now purely **offer → six tacos → excluded item → add-ons → drinks**, with no sign-off, no questions, no commentary. Still 2 pages.
**Retargeted the top ask** so it doesn't reference a block that's gone — now *"Anything that's off, tell me and I'll fix it before this goes anywhere."*
**Cleaned 2,319 characters of dead CSS** left behind by three rounds of removals — the `.signoff`, `.sigrow`, `.checks`, `.cbox`, `ol.q` and `strong.hl` rules, in both the screen and print blocks. Worth doing because this file is committed source that gets regenerated: orphaned selectors are how a stylesheet quietly rots into something nobody can safely edit.
Verified by rendering both pages.

## 2026-08-25 — Chef doc trimmed to a pure content sheet · now 2 pages  [F2]
**Three trims from Ramsey, all removing *my* reasoning rather than his content:**
1. The **$16.50 explainer** under the offer line — internal rationale, not a chef verification item.
2. The Camaron **"Confirm that's right — and tell me the reason…"** sentence → now just **"Not on Late Night."**
3. The entire **Four Questions** section.

**Removing the questions loses nothing**, because the sign-off tick-boxes already capture the same four points in actionable form — protein hold times, the shrimp reason (with a blank for it), description accuracy, and the drink prices. Questions asked; tick-boxes get answered.
**Also rewrote the top ask** so it no longer points at a section that doesn't exist — it now directs her to the sign-off block, and corrects "won't hold at 9pm" to "won't hold to 10pm" to match the actual service window.
**Result: 3 pages → 2.** Verified by rendering both. The doc is now offer → six tacos → excluded item → add-ons → drinks → sign-off, with no commentary.

## 2026-08-25 — Chef doc: dropped the $16.50 explainer  [F2]
**Ramsey:** *"you can remove this from the doc we are aligned."* Removed the *"Tacos only — no side. The regular 2-tacos-plus-side plate stays $16.50…"* line from the chef content-check sheet — that was internal reasoning for Ramsey, not something the kitchen needs to verify. The offer line is now simply *"Any two street tacos from the six below."*
**Scoped to this doc only.** The "tacos only, no side" fact **remains** on the customer-facing print menu, the social cards, and in `CLAUDE.md` as a copy guard — it's a real table-side distinction for staff, just not a chef sign-off item.
PDF regenerated, still 3 pages, verified by rendering page 1.

## 2026-08-25 — Paloma repriced $7 → $8; propagated across 20 surfaces  [F2]
**Ruling:** Ramsey set the Late Night paloma at **$8** (was drafted at $7). Regular price $14.50, so a **$6.50 cut (45%)**.

**Consequence worth noting:** the **margarita is now the steepest Late Night discount** at $12.50 → $6 (52%), not the paloma. Every place that framed the paloma as "the steepest cut on the menu" had to be rewritten, not just renumbered — including the chef sign-off question, which now asks about the drink prices as a set and names the margarita as the deepest.

**Propagated to 20 files:** `CLAUDE.md` · `AI-PLATFORM-ACCESS.md` · `master-reference.md` · **`brand-context-pack.md`** (the ChatGPT/Gemini bridge) · `venue-and-operations.md` · `menu-and-offers.md` (Late Night row + new v2.6 changelog entry) · the Late Night campaign brief (its "confirm the paloma price" open item now closed) · `chef-content-check.html` · `late-night-menu-mockup.html` · `late-night-social.html` · `email-graphics.html` · `send-plan.md` · `review-index.html` · the registry · plus the HQ folder's SMS file, README and review page.
**Re-rendered 4 PNGs** (menu 1080×1350, social feed, social story, Late Night email banner) and **regenerated the 3-page chef PDF**.
**Verified:** Friday launch SMS still **130/160, one segment**. Spot-checked `$8` in the rendered menu art rather than trusting the source edit.

**Caught by rendering and looking:** the first regenerated PDF had the table correct at $8 but **question 4 still read "going out at $7"** — my replacement pattern matched "paloma at $7" and missed "going out at $7". Fixed and re-verified. A reminder that a price appears in prose as well as in tables, and prose doesn't follow a pattern.

## 2026-08-25 — Late Night content-check sheet for Chef Maraya (PDF + shareable page)  [F2]
**Need:** the chef leaves for a few days today and has to sign off that the Late Night menu content is accurate before anything prints.

**Built a verification sheet, not a menu mockup** — the job is catching errors, not admiring layout. The ask sits at the top, all six taco descriptions are quoted **verbatim from `menu-and-offers.md`** (so a wrong line means the menu doc is wrong too), drinks show regular price beside late-night price, and **four kitchen-only questions** sit at the bottom for a two-minute read.
**The four questions are the actual value:** do all six proteins hold to 10pm · why no shrimp (staff need a real answer, not "we're out") · do the descriptions still match the build, **especially Hongos with seven components** · is a $14.50 paloma at $7 workable.
**Excluded item shown deliberately** — Camaron struck through with its description intact, so she confirms the exclusion rather than wondering whether it was forgotten.

**Delivered two ways:** a shareable Artifact page (phone-friendly, light/dark aware) and — on Ramsey's request, since it's the easiest path to sign-off — a **3-page letter PDF at `~/Documents/Uno-mas-hq-2026/menus/Late-Night-Menu-CONTENT-CHECK-2026-08-25.pdf`** with a real **sign-off block**: four tick-boxes, a corrections field, and signature + date lines.
**Print QA caught a real defect:** the first PDF ran to **4 pages with an orphaned footer alone on the last one** — sloppy on a document going out for signature. Tightened the print CSS (type scale, card padding, section rhythm) and added `break-before:avoid` on the footer so it stays with the sign-off. Now 3 pages, verified by rendering every page.
**Source committed** at `marketing/campaigns/late-night-menu/chef-content-check.html` so corrections can be folded in and the PDF regenerated.

## 2026-08-25 — Meta ads v3: three more in the ritual/clean-stack lane  [F7]
**Ramsey picked C (ritual) and E (clean offer stack)** from v2 — both avoid selling the discount. Read that as the preference and stayed in the lane: **no price-contrast hooks, no "normally $50"** in the new ones.
- **F · "Tuesdays are handled."** — removes a decision rather than offering a deal. *"Nothing to remember, nothing to claim"* kills the friction people expect from a promo.
- **G · "The regulars already know what day it is."** — insider register, the same one his **MICKEY weekend promo** ran on (*"if you know, you know"*), which his list actually responded to. Best for **cold** audiences: implies a full room rather than a restaurant asking for business.
- **H · E's stack in feed format** — no hook at all, per-line windows, more lines than a Story allows.

**Recommended a two-variant split that actually teaches something:** **C for warm** (retargeting, customer list) and **G for cold** (Spokane targeting) — same idea, different audience temperature. Flagged that two variants of the same idea aimed at the same audience tells you nothing, and offered **H as a plain-facts control** to isolate whether the ritual framing beats a bare offer.
All counts verified; every hook lands inside the ~125 visible characters and every variant stays all-day-true.

## 2026-08-25 — Meta ad copy v2: rewritten to run all day  [F7]
**Ramsey: the content is relevant all day, so the copy should be too.** Rewrote all five variants so each **reads correctly at 11am and at 8pm** — which means **one ad set running all day Tuesday** instead of the two dayparted sets v1 proposed.

**The craft rule that makes it work:** the **hook is always an all-day-true statement** ($6 margs, $30 pitchers, open to close), and **BOGO appears only as a secondary line, never without "till 5pm" attached.** Read any variant at 8pm and nothing is false — the margs are still $6 and the BOGO line carries its own cutoff.

**This is simpler and better than v1.** Writing the copy correctly removed the need for dayparting: fewer moving parts, one schedule, and **Meta gets a single audience to learn on instead of two half-budgets.** Kept the lunch-specific ad set documented as optional but explicitly not the recommended start.
**Story variant now carries per-line windows** (`$6 margs · all day` / `BOGO street tacos · till 5pm`) so it stays accurate whenever it's seen.
All counts re-verified against Meta's 27/30 limits; every hook lands inside the ~125 visible characters.
**Also fixed:** the `CLAUDE.md` pointer added in v1 had the wrong path (`marketing/` instead of `marketing/campaigns/`).

## 2026-08-25 — Meta ad copy for Taco Tuesday  [F7]
**Built** `marketing/taco-tuesday-meta-ads.md` — 5 variants (4 feed + 1 story), matching the established format in `campaigns/2026-04-dinner-launch/creative/copy/ad-copy.md`. **Every character count programmatically verified** against Meta's headline (27) and description (30) limits; all pass.
**Voice rule applied:** *hook-driven, clarity first — 60% clever max* (`CLAUDE.md`). Variants are angled rather than reworded: A the BOGO math · B the $12.50→$6 price contrast · C the ritual (for retargeting warm audiences, fits *belonging beats bargains*) · D the $30 pitcher group play · E stacked-offer story.

**🔴 The important finding is structural, not copy.** Taco Tuesday is **two offers on two dayparts** — BOGO ends at 5pm, margs and pitchers run all day. Running them as one always-on ad means **paying to advertise an expired offer after 5pm**, which is one of the most common ways a small restaurant budget leaks. Documented two ad sets with dayparting (BOGO ~9am–4pm Tuesdays; drinks 11am–9pm Tuesdays), plus a hard copy rule: **never write "BOGO" without "till 5pm" attached.**
**Also noted:** the ad and the landing page now match, because the Taco Tuesday tile went live today — sending offer traffic to a page that doesn't mention the offer is the other common waste. Recommended optimizing for landing-page views rather than conversions, since there's no on-site purchase event for Meta to learn from.
**Measurement framing:** Tuesday covers vs. the prior three Tuesdays, not clicks — and run four Tuesdays before judging.
**Open:** ad account not yet pulled (connector is authorized — offered), and no budget figure yet.

## 2026-08-25 — Named the franchise: **The Weekly Promo Drop**  [F7, F14]
**Ramsey's reframe, and it's worth more than the SMS it came from.** Rather than teasing the gift card, the Tuesday SMS now announces the *program*: **"Our new weekly promo drop starts tomorrow."** (141/160, one segment, 19 chars spare.)

**Why this matters:** the first four weekend offers each launched cold with no connective tissue between them. A **named recurring slot** means week five inherits whatever equity weeks one to four built, guests start *checking* rather than being interrupted, and Ramsey gets a container to fill instead of a decision to remake every week.

**"Drop", not "flash" — deliberate.** A flash implies hours; these run **Wed–Sun**. A word that overpromises stops meaning anything by week three. Raised the mismatch, offered both fixes (shorten the promo, or change the word), and Ramsey took the word.

**The rhythm, now recorded:** announce Tuesday (program only, no detail) → reveal Wednesday (the email can actually explain it) → runs Wed–Sun.
**Documented in:** `campaign-architecture.md` §4c + the per-day table · `campaigns/weekend-promos/executions-log.md` header · `CLAUDE.md` "Always Get Right" · the send plan and the HQ SMS file.
**Rules attached:** announce the program never the offer on Tuesday · **one drop per week** (two competing offers in one window is where margin breaks) · log every drop's result so the series compounds into knowledge rather than four unmeasured experiments.
⚠️ **The Tuesday SMS is already queued in Toast — paste the new text there by hand.**

## 2026-08-25 — Taco Tuesday tile SHIPPED LIVE · SMS reframed as a tease  [F7, F3]
**🟢 The Taco Tuesday tile is live** (Lovable commit `7b32a95c`). Treatment D, running automatically all day every Tuesday.
- **Built a reusable weekday gate** rather than another hardcoded date check: `src/components/useIsSpokaneDay.ts` exposing `spokaneDayIndex()` and `useIsSpokaneDay(day)`. It initializes to the correct value so SSR renders it right (no flash), re-verifies on the client, and re-checks every 5 minutes so a tab left open across midnight self-corrects. **The duplicate `spokaneDayOfWeek()` in `index.tsx` was deleted and re-imported from the new file — one implementation, not two.**
- **Wednesday, Thursday and Late Night can all reuse this hook.** That was the point.
- Tile reuses the FullSendBanner flyer chrome (cream ground, torn clip-path, halftone, drop animation with reduced-motion guard, starbursts). Offer row is treatment D: pink lead box `BOGO / Street Tacos / Till 5PM`, then yellow `$6 / House Margs / All day` and `$30 / Marg Pitchers / All day` — **item names at 17px sentence case**, dayparts as 11px uppercase fine print.
- **Whole tile is a real `<a href="/menu">`** firing `trackEvent("nav_click", {location:"taco_tuesday_banner"})` — so the promo is actionable and measurable without a visible button.
- **`FullSendBanner` deliberately left in place**, still gated off, as a template for future promos.
- **Verified live:** tile present with all three boxes, real anchor to `/menu`, FullSendBanner correctly absent. Lovable tested the gate against fixed timestamps in Node (`2026-08-24T12:00Z` → Mon/hidden, `2026-08-25T12:00Z` → Tue/shown) rather than editing the component, so there was no test override to revert.

**Tuesday SMS reframed as a tease** (Ramsey's call): the closing line no longer states Wednesday's offer. Now *"Tomorrow we're giving something away. That's all we'll say."* — 158/160, still one segment, but **almost no headroom left; any edit needs a re-count.**
**Recorded as a durable rule** in `EMAIL_SMS_PLAYBOOK.md`: **tease the next thing, don't announce it** — curiosity outperforms announcement, and it protects the reveal for the channel that can actually explain the offer.
⚠️ **This SMS is already scheduled in Toast** — the text has to be updated there by hand; the repo change doesn't propagate to a queued send.

## 2026-08-25 — BOGO line: fixed a two-headline collision  [F7]
**Ramsey's critique:** *"the BOGO Street tacos looks like another headline, getting lost with the Taco Tuesday headline."* Correct — I'd set it in **Antonio uppercase directly under Antonio uppercase**, so the name and the offer competed instead of ranking.

**Diagnosed the principle rather than nudging the size.** The tile has three jobs — **name**, **offer**, **prices** — and each needs a visibly distinct treatment. The prices already own "yellow box," so the offer needed its own lane, not just a smaller font.

**Built `bogo-line-treatments.html`** — the same tile with 6 treatments of that one element, so the choice is visual instead of described: pink band · Montserrat wide-tracked subhead · rule-flanked · **BOGO as the lead price box (pink)** · yellow highlighter swipe · moved above the name as an eyebrow.

**Recommended 4, then 1.** Option 4 solves it by *reclassifying* the line — BOGO stops being type competing with a headline and becomes the first and biggest offer box, pink outranking the yellow supporting ones. It also adds **no new pattern** to the tile, reusing one already there.
**Predicted and confirmed a failure:** option 5 (yellow highlighter) puts the offer in the same colour family as the prices, recreating the same confusion one layer down. Called out on the page as the one to avoid.

## 2026-08-25 — Taco Tuesday tile v2: copy stripped to three facts  [F7]
**Ramsey's edits applied** to all six promo-tile mockups: **no protein list · no CTA button · no "Every Tuesday" kicker** (the name already says it) · **"BOGO Street Tacos till 5PM"** promoted to the hero offer line, with $6 margs and $30 pitchers as supporting price boxes.

**The simplification changed the recommendation.** With only three facts left — the name, BOGO till 5PM, and two prices — the compact strip (F) stops being a compromise and becomes the obvious weekly shape. B stays the version for weeks worth pushing harder.

**⚠️ Raised: removing the button removes the only way to act on the tile, and the only measurement.** The Full Send CTA fired `trackEvent("nav_click", {location:"full_send_banner"})`. Recommended making the **whole tile a link** to `/menu` so the promo stays actionable and still reports whether it works.
**Copy convention recorded:** **"till", not "til"** — Ramsey's spelling. Added to `CLAUDE.md`. The already-scheduled Tue Aug 25 SMS used "til"; left alone, fixed forward. Also caught the announcement-bar mockups still saying "TIL" while the tile said "TILL", and the option-A description still claiming a ribbon and CTA that had just been removed.

## 2026-08-25 — Taco Tuesday promo tile mockups · Cloudinary organization plan  [F7, F9]
**Corrected target surface mid-task.** Started building announcement-bar variants; Ramsey clarified the promo should live in **the promo tile used for Full Send**, with the announcement bar only *reinforcing* it. Researched the real component before designing: **`FullSendBanner`**, inline in `src/routes/index.tsx`, a full-bleed torn-paper flyer rendered **above the hero** in a custom `max-width:1200px` wrapper, all copy in real HTML, Cloudinary art used only as two decorative cutouts, gated by a hardcoded `Date.now() < new Date(...)`.
**Built 6 promo-tile mockups** in that exact idiom (torn clip-path, halftone, starbursts, yellow price boxes, teal ribbon, pink pill CTA), each shown with the announcement bar above and a hero marker below: A reuse-Full-Send · B photo band inside the flyer · C split photo/offer · D BOGO-as-hero · E navy variant · F compact strip. Served locally at `:8789`.
**Recommendation given:** B for impact, **F for weekly use** — this runs 52×/year and a tall tile above the hero every Tuesday is how banner blindness starts.
**🔴 Flagged a real engineering gap:** there is **no weekday-gating pattern in the codebase.** Existing promos use hardcoded date checks. A "Tuesdays only" tile needs `spokaneDayOfWeek()` (already present, timezone-safe) combined with the `WeekendSpecialBanner` hydration pattern, or SSR renders one day's answer and the client flips it. **Build it once and every future recurring daypart reuses it.**
**Also caught while mocking the announcement bar:** at 390px the desktop copy wraps and overflows the fixed 40px bar. Mobile copy has a hard ceiling of ~30 characters including the CTA.

**New: `marketing/cloudinary-organization-plan.md`** — answers the DAM organization question and assesses MediaFlows against four *live* problems. Key conclusions:
- **The highest-value fix isn't automation, it's curation.** No `hero-approved` tag exists, so with ~1,350 assets the agent keeps reusing the same 3–4 it has hand-verified. A 25–40 asset tagging pass removes a verification step from every future design task. Logged as registry §4 item 22.
- **Best MediaFlows use: auto-tag by resolution** → `needs-hires-swap` / `print-ok`. That makes the print gate mechanical instead of dependent on someone remembering, which is the failure mode that ends in a soft table tent.
- **Smart Rename fixes the inflow but not the existing 31** — and registry item 19's recommendation is now explicitly **tag, don't rename**, since renaming changes delivery URLs the live site depends on.
- ⚠️ **Blocking unknown: is MediaFlows even on the FREE plan, and do executions consume credits?** 25/month budget. If metered, build only the resolution flow. Logged as item 23.

## 2026-08-24 — Feedback round 2 (v3): assets rebuilt PHOTO-LED  [F7, F9]
**Read `FEEDBACK.md` from the review page** and applied all three items.

**A1 — Late Night menu.** Removed the "Good to know" box · headline simplified to **"Pick any 2 tacos $10"** · removed all "kids welcome any hour" copy · removed the per-item "Save $X" lines (**strikethrough kept**, as previously requested) · **added real food photography**.
**B1/B2 — Late Night social.** Same changes, and **rebuilt photo-led** rather than type-only.
**D2/D3 — email banners.** Also now photo-led (nachos on Beer & Bites, tacos on Late Night).
**E1 — Tuesday SMS.** Reframed as *"Friendly reminder: it's Taco Tuesday"* since it's been sent before, **BOGO clarified as ending at 5pm**, address dropped. 139/160, still one segment.

**The GENERAL note drove a doctrine change, not just a redesign.** Ramsey: *"can we add images and more graphics… they just feel underwhelming and not bold, bright, and inline with restaurant advertising best practices."* He was right — my §4b split (photographic = experience, illustrated = offers) was too rigid and produced type-only offer cards that read as coupons. **Revised the rule in `campaign-architecture.md` §4b and in the `unomas-design` skill: photo-led is the default for anything promoting food or a daypart; pure illustrated is reserved for offers where money is the message and there's no dish to show** (gift cards, spend thresholds).

**Photo chosen:** `20260125_UM_FOOD_TacoCloseUpV10_FINAL` — checked native resolution first (**2560×2135**), so it is print-safe and *not* one of the `needs-hires-swap` shared-album derivatives. Verified before use rather than assumed.

**Two build bugs caught by rendering and looking:**
1. **CSS specificity** — `.hero img{width:100%;height:100%}` beat `.logo{height:64px}`, blowing the wordmark to full-bleed and pushing the headline outside the clipped hero. Scoped the background rule to `.hero > img.bgimg`. **Recorded in the design skill** so it doesn't recur.
2. **White headline over a bright tortilla was illegible.** Added a second radial scrim plus a stronger text-shadow, then re-checked at full size.
Also switched exports to **rendering each artboard in isolation** at exact canvas size — crop-detection on photographic backgrounds produced silently misaligned exports twice. Recorded in the skill.

**Review page updated to v3** with a change summary, and the six reworked items reset to un-reviewed so they get a fresh look. **C1–C3 (gift card) left illustrated** — money is the message there — but flagged on the page in case Ramsey wants photos there too.

## 2026-08-24 — Review page made interactive: per-asset approve + comments that persist  [infra]
**Built** `review-server.py` + an interactive `index.html` in the promo folder. Ramsey can now approve or comment on **each asset individually, right on the page**, instead of relaying IDs back in chat.

**How it works:** every one of the **17 review targets** (9 graphics, 4 SMS/copy blocks, 3 open questions, plus a general notes box) has an **✓ Approve / ✎ Needs changes** toggle and a comment box. Input debounce-saves to `localStorage` **and** POSTs to the local server, which writes:
- `feedback.json` — machine-readable state
- **`FEEDBACK.md`** — human-readable, grouped into *Needs changes* → *Approved* → *Comments without a decision* → *Not yet reviewed*, with a header tally

**Why a custom server rather than `python -m http.server`:** the plain module can't accept POSTs, so feedback would have had to be copy-pasted back. Now **Claude reads `FEEDBACK.md` directly** — Ramsey types once and nothing gets retyped or lost.

**UI details:** cards border green/amber by status with a status pill, a live tally in the sticky header shows approved/changes/left, and a toast confirms each save (falling back to "Saved locally — server offline" if the server is down, so nothing is lost). State survives a refresh via localStorage.

**Verified:** all 17 control blocks injected; POST round-trip tested end to end; test data cleared before handing over.
**Copies committed to the repo** at `marketing/campaigns/week-2026-08-24-sends/` (`review-server.py`, `review-index.html`) so the pattern is reusable for future review rounds.
**Restart command:** `cd <promo folder> && python3 review-server.py 8787`

## 2026-08-23 — Feedback round 1: struck-through pricing · pre-loaded cards · Toast prepends name  [F2, F7]
**Three pieces of feedback from Ramsey, all applied.**

**1. Struck-through regular pricing on Late Night.** Pulled the real menu prices to make the discount visible: **margs $12.50 → $6** (save $6.50), **palomas $14.50 → $7** (save $7.50), **pitchers $50 → $30** (save $20). Applied to the menu piece (with per-item "Save $X" lines and a "regular price struck through" note), both social cards, and the Late Night email banner. Re-rendered and inspected all three.
⚠️ **Worth Ramsey knowing:** these are **~52% off** on margs and palomas. Deep, but $6 already matches Taco Tuesday so the marg price is established. Flagging the depth, not objecting.

**2. Gift cards are PRE-LOADED with $10/$20** — not activated at checkout. This is materially simpler and **resolves the activation bottleneck entirely**: no terminal step, no manager override, no discount object in Toast, and any server can hand one over. The earlier Friday-service concern is now moot. Replaced with two new operational notes: **pre-load before Wednesday, not mid-shift**, and **split the denominations 70/30 — ~140 × $10, 60 × $20** to match the liability model, since guessing the mix wrong means running out of one while sitting on the other.

**3. Toast prepends the restaurant name to every SMS**, so the body must never contain it — it would read "Uno Mas: Uno Mas: …". This **also retires the `á`/GSM-7 question for SMS bodies**, since the name never appears there. Registry §4 item 20 rewritten. Fixed the one Thursday alternate that still said "at Uno Mas". Recorded as a durable rule in `EMAIL_SMS_PLAYBOOK.md` so it applies to every future send.

**Review page updated to v2** and re-served at `http://127.0.0.1:8787` — change banner at the top, and three of the six open questions now closed (paloma price, who activates, Toast flow) with a new one added for the pre-load split.

## 2026-08-23 — Promo asset folder assembled (9 graphics + SMS + sources)  [F7, F9]
**Delivered** `~/Documents/Uno-mas-hq-2026/promos/2026-08-26_giftcard-and-latenight/` — one folder covering both campaigns, 2.9 MB, dimensions verified.

**Built new for this:**
- `late-night-social.html` — Late Night **feed 1080×1350** + **story 1080×1920** (story has bottom safe-area). Distinct from the menu piece: the menu lists proteins with descriptions, the social cards lead with the offer and list protein *names* only.
- `email-graphics.html` — three Wednesday-email banners at **1200px wide** (2× the 600px email content standard, for retina): gift-card hero 1200×630 (illustrated/cream system), Beer & Bites 1200×500 (navy), Late Night 1200×500 (dark navy).
- `05_sms/sms-messages.md` — ready-to-paste SMS with segment counts, plus email subject lines and preview text.

**Folder is numbered by use** (`01_late-night-menu` → `05_sms`) with a README mapping every file to its channel, print instructions, the pre-flight checklist, and a pointer back to the repo as source of truth. `_source-html/` carries all four editable sources so print goes through Cmd+P → PDF rather than a 1× PNG.

**Design QA:** the Late Night social card first rendered with a large dead zone between the price row and the footer. Filled it with the **protein list** — real information a promo card should carry — then fixed a CSS bug where `margin-top:auto` + `margin-bottom:auto` centered the block in the leftover space instead of seating it under the prices. Re-rendered and inspected both times.

**Notable:** **no photography in any of the nine graphics.** All real wordmark + DAM line-art + house icon-pattern texture, so the `needs-hires-swap` print gate does not apply and every piece is print-safe as-is.
**Email caution recorded:** the offer must also appear as **live text in the email body**, since many clients block images by default and an image-only offer is invisible to those readers.

## 2026-08-23 — Week-of-Aug-24 send plan built (Tue SMS · Wed email · Thu SMS)  [F7]
**Built** `marketing/campaigns/week-2026-08-24-sends/send-plan.md` to Ramsey's brief — Tuesday SMS, Wednesday email, Thursday SMS, aimed at lifting Wed/Thu (his stated soft days). Every draft is segment-validated, with send times and alternates.

**🔴 Discovery — "á" is not in the GSM-7 character set.** Writing **"Uno Más"** in an SMS body forces UCS-2 encoding, which cuts the single-segment limit from **160 characters to 70** — so a normal-length text becomes **2 segments at ~2× cost.** (`é à ö ñ ü` are in GSM-7; `á í ó ú` are not.) This is the concrete technical reason behind the Aug 2026 handoff's "watch SMS segment cost" rule, which the repo had recorded only as a preference. **Needs a brand-rule ruling** — `CLAUDE.md` mandates the accent on human-readable surfaces and permits ASCII only for "technical compatibility," and SMS encoding is arguably exactly that. All drafts use ASCII "Uno Mas" or omit the brand name pending Ramsey's call. Logged as registry §4 item 20; item 21 flags the unverified question of whether Toast auto-appends the opt-out (worth 25 characters).

**Gap raised:** **Late Night launches Fri Aug 28 with no send on the plan.** Thursday teases it, but a brand-new daypart launching without a launch-day message is a missed shot. Recommended one 4pm Friday SMS (drafted, single segment) and offered the trade — if four sends to one list is too many, move Thursday's to Friday, since Friday has genuinely new news and Thursday is a recurring special the list already knows.

**Judgement call flagged, not made:** Tuesday's recommended draft **bends the house one-offer-per-SMS rule** by teasing Wednesday's gift card. Called out as a deliberate exception — priming the soft day is the highest-leverage line in the week — so Ramsey can veto it knowingly.
**Also flagged:** "Big F'N" going to every phone on the list is a conscious choice worth confirming, and the Wednesday email footer must state the corrected **8pm** Tue–Thu close.
**Measurement:** judged on Wed/Thu covers vs. the prior three Weds/Thurs, cards issued per day, and Friday Late Night covers — not opens.

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
