# Uno Más — Storage Consolidation & Migration Plan

**Owner:** Ramsey Pruchnic · **Started:** 2026-06-16 · **Status:** in progress (Phases 0–2 done)

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
| 3 | Move code apps → `Ramsey-HQ/Plugins-and-Apps/` (plain files, no git) | ⬜ pending |
| 4 | Migrate marketing/ops/financial **text** (.md) into repo; assets stay on Drive | ⬜ pending |
| 5 | Drive cleanup: `_TO_BE_DELETED`, cleanup HTMLs, `._`/AppleDouble junk, trailing-space folder renames | ⬜ pending |
| — | Cloudinary DAM: Ramsey-driven, curated subset, resume at `mezzanine/venue` | 🔄 ongoing (separate sessions) |

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

1. **Zip code conflict** — brand-intel `99205` vs old instructions `99201`. Confirm and fix everywhere.
2. **Rotate the Gemini API key** that was exposed in the old `HANDOFF-PROMPT.md`.
3. **`credentials.json` + `email_mcp_setup.py`** sit loose in `~/` — keep out of any repo (gitignore now covers them).
4. **Trailing-space folder names** on Drive — rename in Phase 5.
5. **Baked-in "UNO MAS" (no accent)** text in some merch PNGs — needs regeneration before print (from old handoff open threads).
