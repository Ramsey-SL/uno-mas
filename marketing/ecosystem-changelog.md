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
