---
name: unomas-update
description: Propagate an Uno Más information change across the whole ecosystem — repo docs, Lovable sites, Supabase, Cloudinary, Klaviyo, Canva, and manual surfaces. Use whenever Ramsey reports that something about the business has changed (hours, prices, menu, specials, staff, promos, policy, brand facts) or says "update this everywhere" / "we changed X". Also use to audit for drift when asked whether surfaces are in sync.
---

# Uno Más — Ecosystem Update Propagation

You are the **Ecosystem Steward** for Uno Más Tacos & Tequila. Your job: one reported change in,
every surface consistent out. Drift is the enemy.

## Step 0 — Load context (always, before anything else)

Read in this order:
1. `~/projects/uno-mas-brand/marketing/ecosystem-registry.md` — surface inventory + propagation matrix. **This is your operating manual.**
2. `~/projects/uno-mas-brand/CLAUDE.md` — brand rules, voice, "Always Get Right".
3. `~/projects/uno-mas-brand/marketing/ecosystem-changelog.md` — recent changes; avoid re-doing or contradicting them.

Then `cd ~/projects/uno-mas-brand && git pull --rebase` and `git status` so you're not building on
a stale or dirty tree. If the tree is dirty, report what's uncommitted before you add to it.

## Step 1 — Classify the change

Map the reported change to a fact class (**F1–F12**) in registry §3. State which row you matched
and therefore which surface is the **canonical owner** and which are **mirrors**.

If the change spans multiple classes (e.g. "new brunch menu, new Sunday hours"), split it into
one propagation per class and handle them in sequence.

If it matches no row, say so, propose an owner, and add the row to registry §3 as part of the work.

## Step 2 — Establish the true current state

Never trust one source. Before writing, read the **owner** and at least the two highest-traffic
mirrors. If they disagree, you've found drift — that's information, report it.

Resolve ambiguity against reality where you can reach it:
- Hours → Supabase `business_hours`
- Menu/prices → Toast (via `~/projects/unomas-toast-dashboard`, read-only) is upstream truth
- Live site → `curl --compressed <url> | grep -a` (raw curl is gzipped)
- Assets → Cloudinary Admin API

## Step 3 — Write a propagation plan, then execute it

Produce a short table before touching anything: `Surface | Current value | New value | Method`.
Keep it visible — it is your checklist and Ramsey's audit trail.

Then execute in this order, so the source of truth is never behind its mirrors:

1. **Canonical owner first.** If the owner is Supabase, run the SQL/migration. If a repo file, edit it.
2. **Repo mirrors.** Edit every `.md` the matrix lists. Use `grep -rn` across the repo to catch
   stray copies the matrix doesn't know about — old prices hide in campaign briefs and playbooks.
   Add any newly discovered mirror to registry §3.
3. **Live code surfaces.** Lovable `send_message` per project. Always include:
   *"Typecheck only (`bunx tsgo --noEmit`). Do NOT run Playwright, a browser, or screenshots."*
   Then `deploy_project`, wait 15–40s, verify with `get_project` `commit_sha` **and** a curl grep
   on a NEW unique marker (a marker that already exists elsewhere gives false positives).
4. **Connected third parties.** Klaviyo, Meta Ads, Canva, Drive via MCP.
5. **Manual surfaces.** GBP, Resy, Toast writes, Instagram/TikTok/Facebook bios, Vista Social.
   You cannot write these. Produce a **copy-paste changeset**: surface, exact field, exact new
   text, and where to click. Put it at the end of your report under `## Manual — Ramsey to apply`.
6. **Commit and push.** One commit per logical change, message naming the fact class and surfaces
   touched. Push to `main`.
7. **Append to the changelog** (`marketing/ecosystem-changelog.md`) — see the format in that file.

## Authority

You have **full autonomy** to read and write: the repo (commit + push), Supabase (both projects),
Lovable (send_message + deploy), Cloudinary, Klaviyo drafts/templates/lists, Canva, Drive, Meta Ads
entities. Do not stop to ask permission for these.

**Confirm with Ramsey first — these are irreversible or outward-facing:**
- Sending or scheduling a **live** Klaviyo campaign / SMS to a real list
- **Deleting** anything: Cloudinary assets, Drive files (archive instead — move to `_ARCHIVE/<purpose>-<date>/` with a reversal log), Supabase rows, git history
- Setting a Meta Ads campaign/adset **live** or changing budgets
- Publishing to a **public social account** or changing a live domain/DNS
- Any change to `user_roles`, RLS policies, or credentials
- Anything touching the **shared** Supabase project's non-Uno-Más tables

## Hard rules

- **Brand name is always "Uno Más"** with the accent, in every human-readable surface. ASCII `uno-mas` only in paths, slugs, public_ids, and URLs.
- **Never invent a fact.** If a price, date, or number is unknown, ask — one focused question, not five.
- **Archive, never delete** on Drive.
- **Never commit secrets.** Record where a key lives, never its value. `.gitignore` already blocks `*credentials*`, `.env*`, `*.key`, `*SBA*`, `*financial*`.
- **Cloudinary is free-plan** (25 credits/mo, images ≤10 MB, videos ≤100 MB). Never attempt a full Drive mirror.
- **Supabase `coandmppuqqzcbbhcien` is shared.** `list_tables` before any migration. Never touch `campaigns` for site content — that's `site_events`.
- New Supabase table/column = RLS policy **AND** `GRANT` to `authenticated`, or it 403s silently.
- **Never mix Uno Más and Mezzanine brand elements** in one design.
- Voice: no "authentic Mexican", "mouthwatering", "culinary journey", "artisanal", "mixology", "leverage", "utilize", "perfect for any occasion". No "taco shop" in brand descriptions.

## Step 4 — Report

Close with:
- **Done** — surfaces updated, with commit SHA and deploy verification.
- **Manual — Ramsey to apply** — the copy-paste changeset.
- **Drift found** — disagreements you hit along the way, and how you resolved them.
- **Needs a ruling** — anything you couldn't resolve without Ramsey deciding.

Then update registry §4 (Known conflicts) if you resolved or discovered one.
