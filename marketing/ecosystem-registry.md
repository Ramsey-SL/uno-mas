# Uno Más Ecosystem Registry

> **This is the machine-readable map of every surface that carries Uno Más information.**
> The Ecosystem Steward agent (`.claude/skills/unomas-update`, `unomas-find`, `unomas-design`)
> reads this file first on every task. When a surface is added, changed, retired, or a
> credential/ID changes — update this file in the same commit.
>
> **Last verified:** 2026-08-20 (specials/policy propagation run) · Maintained by Ramsey Pruchnic / Strategy Labs

---

## 1. Ownership principle

Every fact has exactly **one canonical owner**. Every other place that fact appears is a
**mirror**. Mirrors are always overwritten from the owner — never the reverse. If a mirror
disagrees with its owner, the mirror is wrong by definition, even if the mirror looks newer.

If you discover a fact with no owner assigned, assign one in §3 before propagating it.

---

## 2. Surface inventory

### Tier 1 — GitHub `Ramsey-SL/uno-mas` (the brain)
Local: `~/projects/uno-mas-brand` · Remote: `git@github.com:Ramsey-SL/uno-mas.git` · branch `main`

| Path | Holds | Access |
|---|---|---|
| `CLAUDE.md` | Orientation, brand name rule, voice quick rules, "Always Get Right" facts, hours, specials | read/write local, commit + push |
| `marketing/master-reference.md` | Operational cheat sheet — NAP, IDs, keys, menu, SEO, stack | read/write |
| `brand-intelligence-center/*.md` | Deep strategy: business, customer, differentiation, financial, proof-goals, voice-identity, messaging-framework | read/write |
| `marketing/knowledge-center/` | Personas, copy bank, campaign templates, `menu-and-offers.md`, performance | read/write |
| `marketing/brand-guidelines/`, `design-system/` | Color, type, logo, layout, photography rules | read/write |
| `marketing/quick-reference/` | Email/SMS, social, AI-marketing playbooks | read/write |
| `marketing/campaigns/` | Campaign briefs, copy, creative notes | read/write |
| `website/` + `marketing/website-*.md` | Lovable prompts, rebuild plan, site messaging, backlog, `SITE-STATUS.md` | read/write |
| `marketing/ecosystem-registry.md` | **This file** | read/write |
| `marketing/ecosystem-changelog.md` | Append-only log of every propagated update | append only |

**Gotcha:** `.gitignore` blocks all binaries (`*.jpg *.png *.mp4 *.pdf *.xlsx *.docx`) and
anything matching `*SBA*`, `*financial*`, `*credentials*`, `*.env*`, `*.key`. Never try to commit
assets here — they belong in Cloudinary or Drive.

### Tier 2 — Cloudinary (the DAM, curated web-ready subset)
Cloud name `drxrfyq9i` · **FREE plan: 25 credits/mo, images ≤10 MB, videos ≤100 MB**

- Root trees: `uno-mas/approved-assets/{photos/<cat>,videos/<cat>,logos,icons,graphics}` (~805–1350 assets), plus `uno-mas/{website,menu,venue,generated,submissions,inspiration,team-uploads}` and a separate root `mezzanine/venue`.
- Naming: bare `public_id` = `YYYYMMDD_UM_<CAT>_<Name>`, `asset_folder` set explicitly, tags `website,uno-mas,approved-assets,category-<cat>,import-<date>`.
- **Selection convention:** Ramsey marks a Drive asset for the DAM by putting `website` in the filename. Strip `-website` to match the Drive master.
- Transform grade in use site-wide: `e_saturation:18,e_contrast:10,e_brightness:4`; videos `c_fill,g_center`, images `c_fill,g_auto`.
- **Gotcha:** the Cloudinary MCP runs remotely and CANNOT read local files (`file://` fails). Upload via signed REST API with curl from a local script using a **Master/full-access** key — a restricted key returns `missing permissions actions=[create]`.
- **Gotcha:** always set `asset_folder` on upload or the asset lands in Home as a path-in-public_id orphan. To relocate an existing one: `POST resources/<type>/upload/<public_id>` with `asset_folder=` (non-breaking, URL unchanged).
- **⚠️ PRINT GATE — `needs-hires-swap`.** A large August 2026 batch came from an **iCloud shared album at 2048px** and is tagged `shared-album-2048` + `needs-hires-swap`. **~141 assets in the library carry it.** These are fine for social/digital working creative and **must NOT be used for print, large-format, or archival production** without swapping in the original capture. `/unomas-design` checks this tag before any print piece.
  - Known high-res exceptions (safe for print): `20260814_UM_PROMO_WeekendSpecial_Portrait` (3506×4381) · `20260814_UM_PROMO_WeekendSpecial_Wide` (6000×2000).
- **Asset count:** ~805 (2026-06-21 curation) + 548 (2026-06-23 sort) + **143 new uploads July 7 – Aug 20 2026** (the July/August shoot batches: Baja fish tacos, margarita flights, French toast prep, burrito builds, carne asada grill, staff/bar service, guest/venue content).
- **Naming, current convention:** `YYYYMMDD_UM_CATEGORY_Subject_v#` — note the **`_v#` version suffix** adopted in the July/August batch (the older convention was `YYYYMMDD_UM_<CAT>_<Name>` with no version). Preserve `_v#` going forward.
- **Named promo assets** (July–Aug 2026): `20260721_UM_PROMO_TacoTuesday_v1` · `20260721_UM_PROMO_MargsAllDay_v1` · `20260722_UM_PROMO_FiveDollarDrafts_v1` · `20260723_UM_PROMO_BurritoThursdays_v1` *(retired promo — see Thursday change)* · `20260725_UM_PROMO_SundayBrunchCollage_v1` · `20260726_UM_PROMO_SundayBrunch_v1` · `20260727_UM_PROMO_SpicyMargsStory_v1` (video) · `20260729_UM_PROMO_LoadedNachos_v1` · `20260730_UM_PROMO_BurritoThursdays_v2` *(retired)* · `20260814_UM_PROMO_WeekendSpecial_{Wide,Portrait}`.
- **Additional folder:** `uno-mas/website/events/love-island-finale`.
- **Search by campaign term** as well as category — `tacotuesday`, `burritothursdays`, `sundaybrunch`, `weekendspecial`.
- **Never mirror Drive here.** Curated subset only. Never overwrite a master — create derivatives.

### Tier 3 — LaCie Drive (the warehouse / master archive)
`/Volumes/lacie-exter/Google Drive/Uno_Mas_HQ /Uno Mas Marketing HQ ` — **note the trailing
spaces on BOTH the parent and the folder.** Always quote paths exactly.

- ~13,314 images + 1,754 videos ≈ 129 GB, folders `00`–`12`, plus `_CHANNEL_READY` (curated, 6.4 GB) and `_ARCHIVE` (42 GB).
- `02_PHOTO_LIBRARY` / `03_VIDEO_LIBRARY` hold ONLY approved assets; everything else was moved to `_ARCHIVE/…-2026-06-21/`.
- **Rule: archive, never delete.** Non-approved files move to `_ARCHIVE/<purpose>-<date>/` with a reversal log. See the `feedback_drive_archive_not_delete` memory.
- **Gotcha:** the GDrive-on-LaCie mount lags `find` enumeration of just-written files and has dropped a file mid-`mv`. Verify per-file with `os.path.isfile`, never `find | wc`.
- Code apps live separately at `Ramsey-HQ/Plugins-and-Apps/`.

### Tier 4 — Local HQ working library (registered 2026-08-21)
`/Users/ramseypruchnic/Documents/Uno-mas-hq-2026`

**Both a destination and a reference library.** The agent writes gathered/built files here and
reads from it. **Not a source of truth** — a staging area and a reference shelf.

| Folder | Holds |
|---|---|
| `listings/` | Local-listing upload kits (dated) — built by `scripts/build-listings-kit.sh` |
| `menus/` | Current menu exports (dinner, brunch, lunch, print PDFs) |
| `promos/` | Sent promos — emails, SMS screenshots, offer cards, poster exports |
| `photos-video/` | Working pulls and shoot batches, pre-DAM |
| `reference/` | Docs, playbooks, guides, handoffs the agent should read |
| `exports/` | One-off generated packages |
| `um-marketing-agent/` | **Portable SNAPSHOT of the agent** — skills, steward, access doc, bootstrap, ChatGPT context pack, brand-brain + registry copies. **Not the source of truth** (the repo `.claude/` is). Re-sync with its `refresh.sh` or it goes stale. |

**Rules:**
- Anything here that becomes a **decision or fact** must be written into the repo — this folder is never the only record of a fact.
- **Web-ready assets** get uploaded to Cloudinary with `YYYYMMDD_UM_CATEGORY_Subject_v#` naming + tags.
- **Master originals** belong on the LaCie Drive.
- **Never delete from here without asking.** Binaries stay here, not in the repo (`.gitignore` blocks them by design).
- Default output target for generated kits and packages. `scripts/build-listings-kit.sh` writes here.
- Its own `README.md` restates these rules for anyone opening the folder directly.

### Marketing website — Lovable + Supabase
- **Lovable project** `78c4ac75-6325-4f38-a44b-278bb2194cf2`, slug `uno-mas-site-builder`, workspace `h7z1Qf3pORsTwkJiC3ie` ("Ramsey's Lovable"). TanStack Start + Tailwind + shadcn/ui.
- Live: https://uno-mas-site-builder.lovable.app · Editor: https://lovable.dev/projects/78c4ac75-6325-4f38-a44b-278bb2194cf2
- Public domain `unomastacoshop.com` — **CONNECTED** (verified 2026-08-20; the lovable.app URL 301s to it).
- Routes: `/`, `/about`, `/fiesta-box`, `/catering`, `/now-hiring`, `/mezzanine`, `/private-events`, **`/cantina-club`**, `/#menu`; `/menu`→`/#menu`; `/reservations` 301→Resy. Admin: `/admin`, `/admin/dashboard`, `/admin/events`, `/admin/content`.
- Key components: `CantinaClubBand.tsx` (homepage loyalty band + Toast SMS mock), `CantinaClubPopup.tsx`, `MenuCollection.tsx` (homepage menu — **hardcoded menu** + Cloudinary rail), `WhatsOnThisWeek.tsx` (specials tiles), `SectionTransition.tsx` (5 approved dividers), `site-header.tsx`, `page-shell.tsx`, `__root.tsx` (pixel loader), `src/lib/queries.functions.ts` (server-fn read layer).
- **Gotcha:** every `send_message` must say *"typecheck only (`bunx tsgo --noEmit`), do NOT run Playwright/browser/screenshots"* — browser runs blow the 300s idle timeout.
- **Gotcha:** verify a deploy via `get_project` `commit_sha` + `curl --compressed … | grep -a` on a NEW unique marker. Raw curl is gzipped; headless Chrome will not paint the SSR mid/lower sections.
- Deploy with `deploy_project`; propagation 15–40s.

- **Supabase project `coandmppuqqzcbbhcien` is SHARED** across the marketing site, food-cost app, DAM/brand tool, and SL Opportunity Engine. **Inspect before every migration — never assume a table is ours.**
  - Ours: `site_content` (page_slug/block_key/block_type/content jsonb/is_published), `site_events` (**the promo/featured-campaign table** — date-windowed), `business_hours` + `hours_overrides`, `menu_sections`/`menu_items`, `event_inquiries`, `user_roles` (+ `has_role(text)` RPC), `brand_guidelines` (chunked ≤2000 chars for AI retrieval).
  - ⚠️ `campaigns` in this DB is an **unrelated SL copy-builder** — do NOT use it for site banners. Use `site_events`.
  - Admins: ramsey@strategylabs.us, scott@strategylabs.us. Karissa not yet added.
  - **Gotcha:** a new table/column needs BOTH an RLS policy AND Postgres `GRANT` to `authenticated`. Missing grants caused a silent 403 "0 members" bug.
- Pixels installed in `__root.tsx` (deferred, fires on interaction/6s): Meta Pixel `1737601003250529`, GA4 `G-YXKMDL0KF2`, Klaviyo onsite company `UjAfaJ`.
- Transactional email: Resend (`RESEND_API_KEY` live) → inquiries to Karissa. Sending-domain verification unconfirmed (open item).

### Cantina Connect — loyalty app (separate from the marketing site)
- Lovable project `9e76084a-a5cc-4ca3-8a3f-82ec78aa3f10`, same workspace. Preview: https://id-preview--9e76084a-a5cc-4ca3-8a3f-82ec78aa3f10.lovable.app
- Own Supabase backend. Schema source of truth: `~/projects/cantina-club/schema.sql`.
- Staff console + member portal `/portal` in one role-based app. Demo staff: demo@unomas.com.
- Program name is **"Uno Más Rewards: The Cantina Club"** — never just "loyalty program".
- Toast is NOT integrated; discounts/purchases stay in Toast. Stripe is BYOK.
- **Gotcha:** same RLS + GRANT rule as above.

### External / third-party surfaces
| Surface | Holds | Access path |
|---|---|---|
| **Toast** (POS) | Live menu + prices + loyalty transactions — *upstream truth for menu* | No MCP. Read via `~/projects/unomas-toast-dashboard` (Standard API, read-only). Menu edits are manual in Toast. |
| **Google Business Profile** | Hours, NAP, photos, posts, reviews | No MCP connected. Manual — agent produces a copy/paste changeset. |
| **Resy** | Reservations, venue hours | Venue ID `87582`, widget key `g47nf19Sg6grqO50HcS2HDIUIO8PjEGM`. Manual. |
| **Klaviyo** | Email/SMS, lists, flows, templates, campaigns | MCP connected. Account/company `UjAfaJ`. Connected to Toast, Square, Meta Ads. |
| **Meta Ads** | Campaigns, creatives, catalog, pixel | MCP connected. Pixel `1737601003250529`. |
| **Canva** | Menus, print, social templates, the email module system | MCP connected. Brand kits: Uno Más `kAFqKpAzOh0`, Mezzanine `kAGze1MPDmA`. **Design IDs + edit/view links: `marketing/canva-design-manifest.md`.** Key masters: Menu MASTER TEMPLATE `DAHIOMHMSp0` · Email Module System `DAHINHHZJng` (11 pages) · Line Art Icons `DAHCAbfY8gU`. ⚠️ The connector exposes discovery/edit/copy but **no downloadable editable-source export** — open the edit link to export. |
| **Google Drive** | Docs, sheets, the asset warehouse | MCP connected (also mounted on LaCie). |
| **Netlify** | Hosting for other SL/Uno Más apps (food-cost dashboard etc.) | MCP connected. |
| **Instagram** @unomastacoshop (primary) · **TikTok** @unomastacosandtequila · **Facebook** | Bio, links, captions | No MCP. Scheduling via **Vista Social**. Manual changeset. |
| **QuickBooks** | Financials | MCP connected. Out of marketing scope — read only for proof points. |
| **Fireflies / Slack / ClickUp** | Meeting notes, comms, tasks | MCP connected. Sources of *incoming* updates, not marketing surfaces. |

**Needs authorization before use** (claude.ai connector settings): Cloudinary, Gmail, Google
Calendar, Notion, Square, Rube, Zapier, Adobe, Microsoft 365, Apollo, Mem, Fulcrum. If a task
needs one of these, say so up front rather than routing around it.

---

## 3. Fact → owner → mirrors (the propagation matrix)

When Ramsey reports a change, find its row, update the **owner** first, then every mirror listed.

| # | Fact class | Canonical owner | Mirrors that MUST be updated |
|---|---|---|---|
| F1 | **Hours of operation** | Supabase `business_hours` (+ `hours_overrides` for dated closures) | `CLAUDE.md` "Always Get Right"; `master-reference.md`; Lovable site hours block; Google Business Profile; Resy; Yelp/Apple Maps; IG/FB bio if stated |
| F2 | **Menu items & prices** | Toast POS → recorded in `marketing/knowledge-center/menu-and-offers.md` | `MenuCollection.tsx` (hardcoded — must edit in Lovable); Supabase `menu_items`/`menu_sections`; `website/content-studio/menus/*.md`; `master-reference.md` menu section; Canva print menus; GBP menu link |
| F3 | **Weekly specials / dayparts** | `CLAUDE.md` "Always Get Right" specials line | `WhatsOnThisWeek.tsx`; Supabase `site_events`; `master-reference.md`; Klaviyo campaigns/flows; social captions; day-deal cards on site |
| F4 | **Brand name, tagline, voice rules** | `CLAUDE.md` + `brand-intelligence-center/voice-identity.md` | `brand-intelligence-center/system-prompt.md`; Supabase `brand_guidelines`; Lovable **project knowledge** on BOTH Lovable projects; Canva brand kits; every playbook in `marketing/quick-reference/` |
| F5 | **NAP** (address, phone, emails) | `master-reference.md` QUICK REFERENCE table | `CLAUDE.md`; site JSON-LD + footer; GBP; Resy; Klaviyo footer; social bios; Canva templates |
| F6 | **Palette / typography / logo** | `design-system/` | `marketing/brand-guidelines/`; Lovable project knowledge (both projects) + Tailwind theme; Canva brand kits; Cloudinary `logos`/`icons` |
| F7 | **Promos / events / campaigns** | Supabase `site_events` | Site featured band + announcement bar; Klaviyo campaign; Meta Ads; social; `marketing/campaigns/<slug>/` brief |
| F8 | **Loyalty program rules** | `~/projects/cantina-club/schema.sql` + `marketing/cantina-club-program-spec.md` | Cantina Connect app; `brand-intelligence-center/cantina-club-messaging-framework.md`; site loyalty section; Klaviyo flows; Toast (manual) |
| F9 | **Assets** (photo/video/logo) | Drive `_CHANNEL_READY` / `02_`/`03_` libraries (master) | Cloudinary curated subset → site, Canva, Meta Ads. `marketing/dam-asset-manifest.md` |
| F10 | **Proof points / performance numbers** | `brand-intelligence-center/proof-goals.md` | `CLAUDE.md` proof points; `master-reference.md`; ad copy; SBA/investor docs (out of repo — gitignored) |
| F11 | **Team / roles** | `CLAUDE.md` team line | `master-reference.md`; `/about` page; GBP; `now-hiring` page |
| F12 | **Digital ecosystem IDs / keys** | `master-reference.md` + this registry | Wherever configured. **Never commit secrets** — record the location, not the value. |
| F13 | **Lifecycle / retention automations** | `marketing/toast-lifecycle-automation-playbook.md` | Toast automation config (manual) · Klaviyo flows · `marketing/cantina-club-program-spec.md` · staff quick guide |
| F14 | **Campaign platform & strategy framing** | `marketing/campaign-architecture.md` | Campaign briefs · ad copy · `brand-intelligence-center/messaging-framework.md` · Klaviyo/social copy |

---

## 4. Known conflicts — resolve on next touch

These are live disagreements found on 2026-08-20. The Steward should surface them and ask
Ramsey to rule, then propagate the ruling.

1. ~~**Taco Tuesday margarita price.**~~ **RESOLVED 2026-08-20 — $6 margs / $30 pitchers.** Ruled by Ramsey; live site already showed $6. The stray "$9" existed only in a session memory note, not in the repo. Memory corrected.
2. ~~**21+ policy (house-wide).**~~ **RESOLVED 2026-08-20 — kid-friendly at all times, NO 21+ window.** Ruled by Ramsey. Propagated to `CLAUDE.md`, `master-reference.md`, all four `brand-intelligence-center/` docs, `brand-context-pack.md`, `local-seo-gbp-reviews-playbook.md` (incl. GBP attributes), `audience-personas.md`, `brand-voice.md`.
   **Mezzanine scope RESOLVED 2026-08-20 — no 21+ anywhere, The Mezzanine included.** Live site updated + deployed (Lovable commit `d17dd26f`): `/mezzanine` hero subtitle + FAQ (visible **and** FAQPage JSON-LD) rewritten to a "can we bring kids" Q&A, `/about` Mezzanine stat badge and card copy stripped, homepage + `MenuCollection.tsx` cocktails eyebrows de-aged. **Surviving 21+ (correct, keep):** Love Island Watch Party event copy + `typicalAgeRange`, Fiesta Box alcohol notes, Cantina Club paid-tier age verification.
3. ~~**Pixels installed.**~~ **RESOLVED** — `SITE-STATUS.md` corrected; pixels are live (Meta `1737601003250529`, GA4 `G-YXKMDL0KF2`, Klaviyo `UjAfaJ`).
9. ~~**BFQ naming inconsistency.**~~ **NOT A CONFLICT — ruled 2026-08-20.** Two renderings are intentional: the **menu keeps "Big F\*\*\* Quesadilla"**, **marketing uses "Big F’N Quesadilla"**. Recorded as a convention in `CLAUDE.md` §Brand Name Rule. Do not "reconcile" these.
10. ~~**Big F’N Thursday price scope.**~~ **RESOLVED 2026-08-20 — $10 is the BASE price**; protein add-ons are charged on top at normal prices (Skirt Steak +$9 · Carnitas +$7 · Grilled Chicken +$6). Never write "$10 with choice of protein."

11. ~~**Loyalty free-tier name — three names in circulation.**~~ **RESOLVED 2026-08-20 (Ramsey):** **ONE program — "The Cantina Club" — and it is FREE.** No free-tier name needed. Retired: "The Guest List" (handoff term, never adopted), "Más Rewards"/"Uno Más Rewards" as a standalone program name. Propagated to `CLAUDE.md`, `campaign-architecture.md` §6/§7, `mas-rewards-loyalty-playbook.md`, `cantina-club-program-spec.md`.
12. ~~**Paid Cantina Club launch status.**~~ **RESOLVED 2026-08-20: paid tiers are NOT live — future-state idea only.** Never market or publicly reference Cantina Member / Cantina OG / La Familia. ⚠️ **Note:** the **Cantina Connect app** (`9e76084a-…`) was BUILT around paid tiers, Stripe billing, and monthly credits. That build is ahead of the business — treat it as future-state infrastructure, not a live program.
13. **Missing binaries from the Aug 2026 handoff** — 8 files referenced but not exported (Toast Automation Playbook + Tracker `.docx`, Loyalty Staff Quick Guide `.pdf`, Cantina-Club-Brand-Messaging-Book `.md`, Klaviyo clickable-sections `.html`, Love Island Bingo 60-card `.pdf`, Festive Sunday brunch menu `.png`, Gift Card Series Mockup `.png`). They sit in the ChatGPT File Library. See `marketing/handoff-2026-08-20-integration.md`.

14. **⚠️ Toast org name lacks the accent and says "Taco Shop."** Every Toast marketing email footer reads **"Uno Mas Taco Shop"** — violating the brand-name rule on a live sending surface, in a phrase `CLAUDE.md` bans for brand descriptions. Rename the Toast organization to **"Uno Más Tacos & Tequila."** (Same fix already queued for TripAdvisor per `local-seo-gbp-reviews-playbook.md`.)
15. **Weekend offers are a rotating weekly TEST — treat every weekend offer as a variable, not a fact.** Confirmed 2026-08-23: $10-off-$60 (code word `MICKEY`) was test 1 and is **over**; the $30 margs+trio bundle was test 2 and is over; **Full Send $45/$65 ran Aug 22–24**; the gift-card bounce-back starts **Wed Aug 26**. The redemption phrase also rotates ("Mickey", "Mas Please", `WEEKEND10`). **Never write weekend copy without checking `marketing/campaigns/weekend-promos/executions-log.md` first.** `weekend-campaigns-and-flows.md` carried a stale "locked offer" — corrected.
16. **"Full Send" is used three ways** — the $45/$65 weekend drink+shareable bundle, the private-events package tier, and adjacent to the menu's "Starter Trio" $45. Needs a naming decision before it's used in more creative.

17. **⚠️ Critical dependency vulnerability on the marketing site** — `seroval` deserialization issue reaching us via `@tanstack/react-router`, `@tanstack/react-start`, `@tanstack/router-plugin`. Flagged by Lovable's security scan 2026-08-21 (scan stale). Already present in the deployed app. **Needs a fresh scan + dependency bump.** Not blocking copy deploys, but real.

18. **🔴 Schema.org `logo` on the marketing site points at an interior photo**, not a logo — Organization JSON-LD uses `20251217_UM_VENUE_VenueInterior_FINAL_11`. Google uses this for knowledge-panel branding. Should reference a real logo from `uno-mas/approved-assets/logos`. **Fix on the site.**
19. **31 live-site assets violate the naming convention** (`IMG_0245`, `2R7A8526`, `carne-asada-knife-hero`, `uno-mas/website/cantina/d72ajps8zp3jflmqynne`, …). They work but are unsearchable by `YYYYMMDD_UM_CATEGORY_Subject_v#`. Worth a rename pass — Cloudinary renames are non-breaking if done via `asset_folder`/rename API with URL preservation, but the site references them by public_id, so **the site must be updated in the same change.**

20. **🔴 SMS ENCODING — "á" is not in GSM-7.** Writing **"Uno Más"** in an SMS body forces UCS-2, dropping the single-segment limit from **160 chars to 70** — roughly **2× cost per message.** (`é à ö ñ ü` are fine; `á í ó ú` are not.) **Needs a brand-rule ruling:** `CLAUDE.md` requires the accent on human-readable surfaces and allows ASCII only for "technical compatibility" — SMS encoding is arguably exactly that. Until ruled, SMS drafts use ASCII "Uno Mas" or omit the brand name. See `marketing/campaigns/week-2026-08-24-sends/send-plan.md`.
21. ~~**Does Toast auto-append the SMS opt-out line?**~~ ✅ **CONFIRMED 2026-08-23: YES, Toast auto-appends it.** **Never write `Reply STOP to opt out.` in an SMS body** — it doubles the disclaimer and wastes 25 characters. Recorded in the SMS playbook and the send plan.

4. **Gemini API key** was committed in plaintext in the old `HANDOFF-PROMPT.md` (April 2026). **Still needs rotating.**
5. **Trailing-space Drive folders** (`Uno_Mas_HQ `, `Uno Mas Marketing HQ `) — planned rename, not done.
6. ~~**Uncommitted work** in `menu-and-offers.md`~~ — **RESOLVED**: it was a Masa Coated Fries price fix ($7 → $8); committed 2026-08-20.
7. ~~**Hours discrepancy** (`CLAUDE.md` 9pm vs Supabase/JSON-LD 8pm).~~ **RESOLVED 2026-08-20 — 8pm confirmed by Ramsey.** `CLAUDE.md` corrected; Supabase and the live site were already right.
8. **Thursday promo changed 2026-08** — Burrito Thursday ($15 House Burrito or Bowl) retired, replaced by **Big F’N Thursday** ($10 Big F’N Quesadilla + $10 menu tequila cocktail fresh sheet). The live site was AHEAD of the repo; 27 repo files were behind. Thursday **poster/AI-image creative is still the retired burrito artwork** — new creative needed.

---

## 5. Open ecosystem items

- Confirm Resend sending-domain verification.
- Wire the public homepage (announcement bar, featured band, hero, specials, hours) to READ Supabase instead of hardcoded values — **this is the single highest-leverage fix for drift**, because it collapses F1/F3/F7 mirrors into one.
- Build the Site Content + Hours/closures admin editors.
- Add Karissa as a site admin (auth user + `user_roles` row).
- Add JSON-LD Product/Service/JobPosting to `/fiesta-box`, `/catering`, `/now-hiring`.
- No MCP for GBP, Toast writes, Resy, or social publishing — these stay manual changesets until a connector exists.
