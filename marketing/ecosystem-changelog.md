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
