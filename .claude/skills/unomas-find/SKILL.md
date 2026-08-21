---
name: unomas-find
description: Locate any Uno Más file, asset, document, doc, photo, video, logo, menu, campaign brief, spreadsheet, or piece of information across the entire ecosystem — GitHub repo, Cloudinary DAM, LaCie/Google Drive warehouse, Lovable projects, Supabase, Canva, Klaviyo, Slack, ClickUp, Fireflies. Use whenever Ramsey asks "where is...", "find me the...", "do we have a...", or needs a file, asset URL, or number retrieved.
---

# Uno Más — Ecosystem Finder

Ramsey asks for a thing. You find it, tell him exactly where it is, and hand him what he can
actually use — a path, a delivery URL, a value, or the file itself.

## Step 0 — Load the map

Read `~/projects/uno-mas-brand/marketing/ecosystem-registry.md` §2 (surface inventory) and §3
(what fact lives where). It tells you which surfaces are even plausible before you start searching.

## Step 1 — Route by what's being asked for

| Asked for | Search here first | Then |
|---|---|---|
| Brand fact, voice rule, strategy, playbook, campaign brief | `~/projects/uno-mas-brand` — `grep -rni` across `marketing/`, `brand-intelligence-center/`, `website/` | Supabase `brand_guidelines`; Drive docs |
| Photo / video / logo / icon (web-ready) | **Cloudinary** `drxrfyq9i` — Admin API search by tag/prefix/public_id | Drive `_CHANNEL_READY`, then `02_PHOTO_LIBRARY`/`03_VIDEO_LIBRARY` |
| Photo / video (original, high-res, or not in the DAM) | **Drive/LaCie** warehouse (129 GB) | `_ARCHIVE/` — non-approved assets were moved there, not deleted |
| Menu, prices | `marketing/knowledge-center/menu-and-offers.md`, `website/content-studio/menus/` | Supabase `menu_items`; Toast (upstream truth); Canva print menus |
| Hours, closures | Supabase `business_hours` / `hours_overrides` | `CLAUDE.md`, `master-reference.md` |
| Promo / event / featured campaign | Supabase `site_events` | `marketing/campaigns/` |
| Site code, component, copy on a page | Lovable `list_files` / `read_file` on project `78c4ac75-…` | `curl --compressed` the live page |
| Loyalty rules, tiers, credits | `~/projects/cantina-club/schema.sql`, `marketing/cantina-club-program-spec.md` | Cantina Connect Supabase |
| Design file, menu layout, print piece, social template | **Canva** `search_designs` / `search_folders` (brand kits `kAFqKpAzOh0`, Mezzanine `kAGze1MPDmA`) | Drive |
| Email/SMS template, list, flow, campaign performance | **Klaviyo** (company `UjAfaJ`) | `marketing/quick-reference/` playbooks |
| Ad creative, campaign, audience, pixel data | **Meta Ads** | `marketing/campaigns/` |
| Sales / labor / traffic numbers | `~/projects/unomas-toast-dashboard`; Financials Knowledge Center | QuickBooks MCP |
| Spreadsheet, doc, PDF, contract | **Google Drive** `search_files` | LaCie mount |
| Recent menu export, sent promo, listing kit, handoff doc | **Local HQ** `/Users/ramseypruchnic/Documents/Uno-mas-hq-2026` (`menus/ promos/ listings/ reference/`) | then Drive / Cloudinary |
| "We discussed it in a meeting / someone sent it" | **Fireflies** transcripts, **Slack** search, **ClickUp** tasks | Gmail (needs auth) |

## Step 2 — Search technique

- **Go wide before deep.** Search 3–4 plausible surfaces in parallel rather than exhausting one.
  For a broad sweep across many local files, delegate to `Explore` subagents in parallel.
- **Vary the query.** Try the brand spelling both ways (`Uno Más` and `uno-mas`), the DAM naming
  convention (`YYYYMMDD_UM_<CAT>_<Name>`), the `website` filename marker, category tags
  (`category-food`, `category-brunch`), and plain keywords. One phrasing rarely finds everything.
- **Quote Drive paths exactly** — `Uno_Mas_HQ ` and `Uno Mas Marketing HQ ` have literal trailing
  spaces. Unquoted paths silently fail.
- **Check `_ARCHIVE/`** before concluding something is gone. Nothing was deleted on Drive — 3,053
  media files and old duplicate trees were moved to `_ARCHIVE/…-2026-06-21/` and
  `_archive/2026-06-16-reconciliation/` in the repo.
- **Cloudinary** is the fast path for any asset that's already web-ready. Search by tag first
  (`approved-assets`, `category-<cat>`), then by prefix, then by public_id fragment.
- The Cloudinary MCP requires authorization; if it isn't connected, use the signed REST Admin API
  via curl, or say plainly that it needs authorizing in claude.ai connector settings.

**Always check the local HQ library** (`~/Documents/Uno-mas-hq-2026`) — Ramsey stages menus, sent
promos, listing kits, and reference docs there. It is often the freshest copy of a *sent* or
*exported* artifact even when the repo has the underlying facts.

**When you gather files at Ramsey's request, write them into the HQ folder** in the matching
subfolder (`listings/ menus/ promos/ photos-video/ reference/ exports/`) rather than a temp dir, so
they persist and stay findable. Say where you put them.

## Step 3 — Deliver something usable

Don't just report a location. Give Ramsey the thing:

- **Cloudinary asset** → the full delivery URL, with the house grade applied
  (`e_saturation:18,e_contrast:10,e_brightness:4`; images `c_fill,g_auto`, videos `c_fill,g_center`),
  plus the public_id and which folder it's in.
- **Repo file** → clickable relative path and line number, plus the relevant excerpt quoted.
- **Drive file** → exact quoted absolute path, size, and modified date. Offer to copy it somewhere useful.
- **A number or fact** → the value, its canonical owner per registry §3, and whether the mirrors agree.
- **Multiple matches** → rank them, say which one you'd use and why. Don't dump a list and leave it.

## Step 4 — Report drift and gaps

If you find the same fact with two different values, **say so explicitly** and name the canonical
owner from registry §3. Offer to run `/unomas-update` to reconcile.

If it genuinely doesn't exist anywhere, say that plainly, list the surfaces you checked, and note
whether an unauthorized connector (Cloudinary, Gmail, Notion, Square) might be hiding it.
