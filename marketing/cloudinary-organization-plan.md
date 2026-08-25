# Cloudinary — Organization Plan & MediaFlows Assessment

**Created 2026-08-25.** Answers two questions: how to keep the DAM organized as fresh assets land
and old ones get reused, and whether Cloudinary **MediaFlows** can automate it.

---

## 1. The actual problems (not hypothetical — all four are live)

| # | Problem | Evidence |
|---|---|---|
| 1 | **No way to tell good assets from merely present ones.** ~1,350 assets, but the agent keeps reaching for the same 3–4 because nothing marks which are *hero-quality*. | Every mockup this month used `TacoCloseUpV10_FINAL` or `PitcherAndMarg_FINAL` |
| 2 | **`needs-hires-swap` is applied manually and inconsistently.** ~141 assets carry it; the tag is the only thing standing between a 2048px derivative and a printed table tent. | Registry §2, print gate in `/unomas-design` |
| 3 | **31 live-site assets violate the naming convention** (`IMG_0245`, `2R7A8526`, `carne-asada-knife-hero`) — invisible to a convention-based search. | Registry §4 item 19 |
| 4 | **Expired campaign assets sit alongside live ones.** `pick-your-full-send-aug2026` is still in `website/promos/` with nothing marking it as finished. | Full Send ended Aug 24 |

## 2. The highest-value fix is not automation — it's a `hero` tag

**Problem 1 is the expensive one**, and it's a curation problem, not a tooling problem.

> **Proposal: tag 25–40 assets `hero-approved`.** The ones you'd actually put on a poster or the
> top of the homepage. Nothing else changes.

Why this matters more than it sounds: the agent currently picks assets by *searching and hoping*.
Given a `hero-approved` tag it picks from a curated shortlist you've blessed — which means less
repetition across pieces, and no more asking you to confirm whether a photo is good enough.
**This is a 30-minute pass through the library that pays back on every asset built after it.**

Suggested companion tags, all cheap and human-set:
- `hero-approved` — good enough to lead a piece
- `print-ok` — verified ≥2000px on the long edge *(see MediaFlows below — this can be automatic)*
- `campaign-<slug>` — e.g. `campaign-fullsend-aug2026`, so a finished promo's assets can be found and retired together
- `retired-YYYY-MM` — expired campaign creative, excluded from search by default

## 3. MediaFlows — where it genuinely helps

MediaFlows is Cloudinary's automation builder (upload triggers → actions). Judged against the four
problems above, **three are a real fit and two are the strongest ROI:**

### ⭐ Flow 1 — Auto-tag by resolution *(solves problem 2 outright)*
**Trigger:** on upload. **Condition:** `width < 2000 OR height < 2000`. **Action:** add tag `needs-hires-swap`. Else add `print-ok`.

This is the one to build first. The print gate currently depends on someone remembering to tag —
which is exactly the kind of thing that fails silently and ends with a soft table tent. Make it
mechanical and the gate becomes trustworthy.

### ⭐ Flow 2 — Smart Rename to the convention *(solves problem 3 going forward)*
**Trigger:** on upload. **Action:** rename to `YYYYMMDD_UM_<CATEGORY>_<Subject>_v#`, set `asset_folder`.

Fixes the *inflow*. It does **not** retroactively fix the existing 31 — and renaming those is still
the risky operation it always was, because the live site references them by public_id. **Recommend:
tag the existing 31 rather than rename them**, and let this flow stop the problem growing.

### Flow 3 — AI auto-tagging on upload
**Trigger:** on upload. **Action:** category tags (`category-food`, `category-cocktails`, `category-venue`, `category-team`).

Useful, lower stakes. Worth it mainly because it makes bulk uploads searchable without a manual pass.
**Verify the AI add-on's credit cost before enabling** — see the constraint below.

### Flow 4 — Auto-expire campaign assets
**Trigger:** scheduled. **Condition:** tag `campaign-*` older than N days. **Action:** add `retired-YYYY-MM`, optionally move to an archive folder.

Solves problem 4. Only worth building **after** the `campaign-<slug>` tagging convention is actually in use — automation over an inconsistent tag does nothing.

### Not worth it right now
- **Sync to 3rd party / Akeneo PIM** — no PIM in the stack.
- **Quality Check** — Flow 1 covers the failure mode that actually bites you.

## 4. ⚠️ The constraint that decides all of this

**You are on the Cloudinary FREE plan** — 25 credits/month, ~10% used (registry §2).

**Before enabling any flow, confirm:**
1. **Is MediaFlows available on the free plan at all**, or is it a paid-tier feature? The UI being visible does not mean it's included.
2. **Do flow executions consume credits?** If each upload triggers 2–3 flows, a 100-asset batch could become 200–300 executions. That math matters a lot at 25 credits.
3. **Does AI auto-tagging bill separately** from flow execution?

**If flows are metered, build Flow 1 only.** It's the one that prevents a real, expensive mistake
(printing a low-res asset), and it runs a trivial condition rather than an AI call.

## 5. Recommended order

1. **Tag `hero-approved` by hand** — 30 minutes, no tooling, biggest immediate payoff for every asset built from here on.
2. **Confirm MediaFlows plan availability and credit cost.**
3. **Build Flow 1** (resolution → `needs-hires-swap` / `print-ok`).
4. **Build Flow 2** (smart rename on upload) once naming is settled.
5. **Adopt `campaign-<slug>` tagging** on the next promo, then build Flow 4.
6. **Tag — don't rename — the existing 31 non-conforming assets.** Registry §4 item 19 updated accordingly.

## 6. What the agent needs from this

Once `hero-approved` and `print-ok` exist, `/unomas-design` changes from *"search, guess, verify
resolution, ask Ramsey"* to *"pull from `hero-approved`, filter `print-ok` if it's going to print."*
That removes a verification step from every single design task.
