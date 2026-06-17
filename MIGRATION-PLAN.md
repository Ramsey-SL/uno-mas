# Uno Más — Storage Consolidation & Migration Plan

**Owner:** Ramsey Pruchnic · **Started:** 2026-06-16 · **Status:** ✅ COMPLETE (Phases 0–5; Cloudinary DAM ongoing, Ramsey-driven)

The durable record of how Uno Más files are being reorganized. Replaces the role of the old
`HANDOFF-PROMPT.md` / `_INDEX.md`. Update the status table as phases complete.

---

## Goal

Stop the "scattered context layers" problem. Establish one clear home for each kind of thing.

## The 3-tier model

| Tier | Role | Location |
|---|---|---|
| **GitHub** `Ramsey-SL/uno-mas` | Brain — all text/context/brand intel, `CLAUDE.md` | `~/projects/uno-mas-brand` |
| **Cloudinary** (free) | DAM — curated web-ready assets only (not a mirror) | `uno-mas/…`, `mezzanine/…` |
| **LaCie Drive** | Warehouse — 129 GB master archive + non-asset binaries + code apps | `/Volumes/lacie-exter/Google Drive/` |

---

## Phase status

| Phase | What | Status |
|---|---|---|
| 0 | Safety: pushed backup branch `pre-consolidation-backup-2026-06-16`; gitignore hardened; secrets flagged | ✅ done |
| 1 | Merge 4 competing master docs → one `CLAUDE.md`; archive originals | ✅ done |
| 2 | Collapse 3 brand-intelligence-center copies → 1 canonical (repo) | ✅ done |
| 2.5 | **Reconcile parallel migration:** a separate session pushed 18k+ lines (marketing/, claude-project/, website/). Deduped overlapping trees → canonical `marketing/`; archived `claude-project/` + old `marketing-knowledge/`; rescued unique playbooks/brand-assets; CLAUDE.md = entry point | ✅ done (branch `reconcile-content-trees-2026-06-16`) |
| 3 | Move code apps → `Ramsey-HQ/Plugins-and-Apps/` (plain files, no git) | ✅ done — `food-cost-analysis/` (31M, same-vol move) + `the-great-pnw/` (from ~, md5-verified); home cleaned |
| 4 | Migrate marketing/ops/financial **text** into repo | ✅ done — marketing text migrated by parallel session; **ops/financial had no migratable text** (Operations = 3 text files: 1 PII-excluded resume + 2 menu data-dumps left with assets; SOPs/training/process all live as Google Docs/PDFs that stay on Drive; 11 Financials `.md` excluded as sensitive per policy) |
| 5 | Drive cleanup (safe): removed `_TO_BE_DELETED/` (verified no real content; canonical SBA intact), 2 stale cleanup HTMLs, 4,197 AppleDouble `._` files | ✅ done — **trailing-space renames intentionally SKIPPED** (plugins/apps/memories depend on those exact paths; leave as-is) |
| — | Cloudinary DAM: Ramsey-driven, curated subset, resume at `mezzanine/venue` | 🔄 ongoing (separate sessions) |

### Canonical repo structure (after reconciliation)

```
CLAUDE.md              ← entry point / orientation
MIGRATION-PLAN.md      ← this file
marketing/             ← CANONICAL marketing content
  master-reference.md  ← operational cheat sheet
  knowledge-center/    ← personas, copy bank, campaign templates, performance, menu, venue
  brand-guidelines/    ← colors, type, logo, layout, photography
  quick-reference/     ← email/SMS, social, AI-marketing playbooks, cheatsheets
  brand-assets/        ← brand asset reference, design system brief
  campaigns/           ← dinner-launch, cinco-weekend
  website-*.md         ← rebuild plan, messaging, backlog, image slots, status
brand-intelligence-center/  ← deep brand strategy (business/customer/differentiation/voice/messaging)
website/               ← Lovable prompts, content-studio
docs/                  ← roadmaps
_archive/2026-06-16-reconciliation/  ← retired duplicate trees (claude-project, old marketing-knowledge)
```

---

## App moves (Phase 3) — plain files, no git per decision

| App | From | To |
|---|---|---|
| Food Cost Analysis | `Uno_Mas_HQ /Uno Mas - Food Cost Analysis App ` | `Ramsey-HQ/Plugins-and-Apps/food-cost-analysis/` |
| The Great PNW tool | `~/pnw_investigator.py` + `~/pnw_data.json` (+ existing `Ramsey-HQ/the-great-pnw-claude/`) | `Ramsey-HQ/Plugins-and-Apps/the-great-pnw/` |

---

## Drive warehouse map — `Uno_Mas_HQ ` (note trailing space)

Preserved from the old `_INDEX.md`. These heavy/binary folders stay on Drive.

- **Operations/** — Business-Documents, Training-and-SOPs, Menu, Recipes, Human-Resources, Logins, Leadership_Meetings (`YYYY-MM/`)
- **Legal/** — Operating-Agreements, Letters-of-Intent, Contracts, SBA-Refinance
- **Locations/** — Monroe (ACTIVE), The-Mezzanine, Wonder-Building (CLOSED)
- **Equity-and-Ownership/** — ownership structure, buy-in, VP equity
- **Uno Más Financials Knowledge Center/** ⚡ plugin-managed, DO NOT reorganize — 00_Reference_Documents → 06_Dashboards_and_Tools
- **Uno Más Marketing HQ /** ⚡ plugin-managed — numbered `00_KNOWLEDGE_CENTER` → `12_VENDOR_ASSETS`, Template-Hub, Website Builder, `_CHANNEL_READY` (curated, 6.4 GB), `_ARCHIVE` (42 GB), `_INBOX`
- **Uno Más Customer Database/** — Klaviyo, Loyalty, Square transactions
- **US Foods Invoices/** — monthly archives 2025-11 → 2026-05 + analysis
- **Archive/** — historical (leave untouched per decision)

## Drive — `Ramsey-HQ/` (personal/company, separate from restaurant)

Plugins-and-Apps, Finance, Strategy Labs, Investment Fund, R&M HQ, the-great-pnw-claude, etc.

---

## Live infrastructure (verify before relying — may have drifted)

- **Asset Hub (canonical):** https://uno-mas-asset-hub.netlify.app — siteId `91594b30-2857-483c-8dcd-5ed8cbb048b2`
- Deprecated `uno-mas-template-hub` (301s to canonical) — Ramsey to delete manually in Netlify admin
- Other Netlify: `uno-mas-hq-internal`, `uno-mas-hq-folders`
- Canva Brand Kits: Uno Más `kAFqKpAzOh0` · Mezzanine `kAGze1MPDmA`

---

## Known issues to resolve

1. ~~Zip code conflict~~ — **RESOLVED 2026-06-16: 99205 confirmed correct** (2020 N Monroe St, Suite C).
2. **Rotate the Gemini API key** that was exposed in the old `HANDOFF-PROMPT.md`.
3. **`credentials.json` + `email_mcp_setup.py`** sit loose in `~/` — keep out of any repo (gitignore now covers them).
4. **Trailing-space folder names** on Drive — rename in Phase 5.
5. **Baked-in "UNO MAS" (no accent)** text in some merch PNGs — needs regeneration before print (from old handoff open threads).
