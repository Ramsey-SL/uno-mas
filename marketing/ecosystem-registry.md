# Uno Más Ecosystem Registry

> **This is the machine-readable map of every surface that carries Uno Más information.**
> The Ecosystem Steward agent (`.claude/skills/unomas-update`, `.claude/skills/unomas-find`)
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
- **Never mirror Drive here.** Curated subset only.

### Tier 3 — LaCie Drive (the warehouse / master archive)
`/Volumes/lacie-exter/Google Drive/Uno_Mas_HQ /Uno Mas Marketing HQ ` — **note the trailing
spaces on BOTH the parent and the folder.** Always quote paths exactly.

- ~13,314 images + 1,754 videos ≈ 129 GB, folders `00`–`12`, plus `_CHANNEL_READY` (curated, 6.4 GB) and `_ARCHIVE` (42 GB).
- `02_PHOTO_LIBRARY` / `03_VIDEO_LIBRARY` hold ONLY approved assets; everything else was moved to `_ARCHIVE/…-2026-06-21/`.
- **Rule: archive, never delete.** Non-approved files move to `_ARCHIVE/<purpose>-<date>/` with a reversal log. See the `feedback_drive_archive_not_delete` memory.
- **Gotcha:** the GDrive-on-LaCie mount lags `find` enumeration of just-written files and has dropped a file mid-`mv`. Verify per-file with `os.path.isfile`, never `find | wc`.
- Code apps live separately at `Ramsey-HQ/Plugins-and-Apps/`.

### Marketing website — Lovable + Supabase
- **Lovable project** `78c4ac75-6325-4f38-a44b-278bb2194cf2`, slug `uno-mas-site-builder`, workspace `h7z1Qf3pORsTwkJiC3ie` ("Ramsey's Lovable"). TanStack Start + Tailwind + shadcn/ui.
- Live: https://uno-mas-site-builder.lovable.app · Editor: https://lovable.dev/projects/78c4ac75-6325-4f38-a44b-278bb2194cf2
- Public domain `unomastacoshop.com` — **CONNECTED** (verified 2026-08-20; the lovable.app URL 301s to it).
- Routes: `/`, `/about`, `/fiesta-box`, `/catering`, `/now-hiring`, `/mezzanine`, `/private-events`, `/#menu`; `/menu`→`/#menu`; `/reservations` 301→Resy. Admin: `/admin`, `/admin/dashboard`, `/admin/events`, `/admin/content`.
- Key components: `MenuCollection.tsx` (homepage menu — **hardcoded menu** + Cloudinary rail), `WhatsOnThisWeek.tsx` (specials tiles), `SectionTransition.tsx` (5 approved dividers), `site-header.tsx`, `page-shell.tsx`, `__root.tsx` (pixel loader), `src/lib/queries.functions.ts` (server-fn read layer).
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
| **Canva** | Menus, print, social templates | MCP connected. Brand kits: Uno Más `kAFqKpAzOh0`, Mezzanine `kAGze1MPDmA`. |
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

---

## 4. Known conflicts — resolve on next touch

These are live disagreements found on 2026-08-20. The Steward should surface them and ask
Ramsey to rule, then propagate the ruling.

1. ~~**Taco Tuesday margarita price.**~~ **RESOLVED 2026-08-20 — $6 margs / $30 pitchers.** Ruled by Ramsey; live site already showed $6. The stray "$9" existed only in a session memory note, not in the repo. Memory corrected.
2. ~~**21+ policy (house-wide).**~~ **RESOLVED 2026-08-20 — kid-friendly at all times, NO 21+ window.** Ruled by Ramsey. Propagated to `CLAUDE.md`, `master-reference.md`, all four `brand-intelligence-center/` docs, `brand-context-pack.md`, `local-seo-gbp-reviews-playbook.md` (incl. GBP attributes), `audience-personas.md`, `brand-voice.md`.
   **Mezzanine scope RESOLVED 2026-08-20 — no 21+ anywhere, The Mezzanine included.** Live site updated + deployed (Lovable commit `d17dd26f`): `/mezzanine` hero subtitle + FAQ (visible **and** FAQPage JSON-LD) rewritten to a "can we bring kids" Q&A, `/about` Mezzanine stat badge and card copy stripped, homepage + `MenuCollection.tsx` cocktails eyebrows de-aged. **Surviving 21+ (correct, keep):** Love Island Watch Party event copy + `typicalAgeRange`, Fiesta Box alcohol notes, Cantina Club paid-tier age verification.
3. ~~**Pixels installed.**~~ **RESOLVED** — `SITE-STATUS.md` corrected; pixels are live (Meta `1737601003250529`, GA4 `G-YXKMDL0KF2`, Klaviyo `UjAfaJ`).
9. **BFQ naming inconsistency.** Menu docs write "Big F*** Quesadilla" (asterisks); the live site writes "Big F’N Quesadilla". `Big F’N` is the print-safe public rendering and should be canonical in all consumer-facing copy. Needs a ruling on whether to standardize the menu docs too.
10. **Big F’N Thursday price scope unconfirmed** — is the $10 BFQ the cheese base (protein add-ons still $6–9), or protein included? Blocks printing a price. See `marketing/campaigns/daily-specials/big-fn-thursday-creative-spec.md`.

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
