# Cloudinary — Operating Guide

**The single place for how the DAM works.** Consolidated 2026-08-25 from rules previously scattered
across `ecosystem-registry.md`, `dam-workflow.md`, `dam-asset-manifest.md` and the design skill.
Supersedes those as the reference; they remain for history.

**Cloud name:** `drxrfyq9i` · **Plan:** FREE — 25 credits/month, images ≤10 MB, videos ≤100 MB

---

## 1. What Cloudinary is *for* here

Three-tier model (`CLAUDE.md`): **GitHub = text/context brain · Cloudinary = curated web-ready
delivery · LaCie Drive = 129 GB master archive.**

> **Cloudinary holds a curated SUBSET, not a mirror.** The Drive library is ~13,300 images and 1,750
> videos; the free plan cannot hold it and shouldn't. Every asset in Cloudinary should be there
> because something ships it.

## 2. Folder structure

```
uno-mas/
  approved-assets/
    photos/{food,brunch,cocktails,venue,team,building,promo,events}
    videos/{food,brunch,cocktails,venue,team,promo,events}
    logos/            icons/            graphics/
  website/
    icons/            promos/           cantina/     events/love-island-finale
  menu/   venue/   generated/   submissions/   inspiration/   team-uploads/
mezzanine/
  venue/
```

**Rule:** `approved-assets/` is the curated core. `website/` holds site-specific derivatives and
UI art. Anything in `submissions/`, `inspiration/` or `team-uploads/` is **not** approved for use.

## 3. Naming

**Current convention:** `YYYYMMDD_UM_<CATEGORY>_<Subject>_v#`
e.g. `20260125_UM_FOOD_TacoCloseUpV10_FINAL`, `20260814_UM_PROMO_WeekendSpecial_Wide`

- The `_v#` suffix was adopted in the July/August 2026 batch — keep it.
- `<CATEGORY>` matches the folder: `FOOD`, `BRUNCH`, `DRINK`, `COCKTAIL`, `VENUE`, `TEAM`, `PROMO`, `PATIO`, `MEZZ`.
- **Always set `asset_folder` on upload** with a bare `public_id`. Skip it and the asset lands in Home as a path-in-public_id orphan.
- To relocate an existing asset without breaking its URL: `POST resources/<type>/upload/<public_id>` with `asset_folder=`. Non-breaking — public_id and URL unchanged.

⚠️ **31 live-site assets violate this** (`IMG_0245`, `2R7A8526`, `carne-asada-knife-hero`, …).
**Resolution: tag them, don't rename them.** Renaming changes the delivery URL and the site
references them by public_id, so a rename needs a coordinated redeploy for a cosmetic gain.

## 4. Tags — the layer that's missing

Tags in use today: `website`, `uno-mas`, `approved-assets`, `category-<cat>`, `import-<date>`,
`shared-album-2048`, `needs-hires-swap`.

**Three tags that don't exist yet and should:**

| Tag | Means | Why it matters |
|---|---|---|
| **`hero-approved`** | Good enough to lead a piece | ~1,350 assets and nothing marks which are hero-quality, so design work keeps reusing the same 3–4 hand-verified ones. **25–40 assets, ~30 minutes, highest-leverage change available.** |
| **`print-ok`** | Verified ≥2000px long edge | Makes the print gate positive rather than relying on the absence of `needs-hires-swap` |
| **`campaign-<slug>`** | Belongs to one campaign | Lets a finished promo's assets be found and retired together (e.g. `campaign-fullsend-aug2026`) |
| **`retired-YYYY-MM`** | Expired creative | Excluded from search by default |

## 5. 🚫 The print gate — the one rule that prevents a real mistake

**~141 assets are 2048px iCloud shared-album derivatives**, tagged `shared-album-2048` +
`needs-hires-swap`. They are **digital/social only.**

**Before any print piece:** check the tag. If present → swap in the original from Drive, or say it
needs a hi-res replacement. **Never silently upscale.**

Known print-safe: `20260814_UM_PROMO_WeekendSpecial_Portrait` (3506×4381) · `..._Wide` (6000×2000) ·
`20260125_UM_FOOD_TacoCloseUpV10_FINAL` (2560×2135) · `20260125_UM_FOOD_FoodOnTable_FINAL` (2541×2560).

**Verify resolution rather than assuming** — `curl` the asset and check dimensions. Several 2026-06
assets that *look* like finals are 1536×2048.

## 6. Standard transforms

| Use | Transform |
|---|---|
| **House grade — every delivery** | `e_saturation:18,e_contrast:10,e_brightness:4` |
| Images | `c_fill,g_auto` |
| Videos | `c_fill,g_center` |
| Line-art recolor | `e_make_transparent:45/e_colorize,co_rgb:<HEX>/e_trim/c_fit,h_160,f_auto,q_auto` |
| Logo on white (schema/email) | `b_white,c_pad,w_1200,h_615,q_auto,f_jpg` |
| Background texture | `uno-mas/website/icons/icons-pattern-forramsey-02-1.png` at ~5% opacity |

⚠️ **CSS gotcha when a photo background and a logo are both `<img>` in one container:**
`.hero img{width:100%;height:100%}` beats `.logo{height:64px}` and blows the wordmark to full-bleed.
Scope the background rule (`.hero > img.bgimg`).

## 7. Upload procedure

**The MCP connector runs remotely and cannot read local files** — `file://` fails. Upload via
**signed REST API with curl from a local script**, using a **Master/full-access** key. A restricted
key returns `missing permissions actions=[create]`.

1. Web-optimize first: images with `sips` (≤2560px, q82); videos with `ffmpeg` (1080p) for the 10/100 MB caps.
2. Upload with a **bare `public_id`** + explicit **`asset_folder`** + tags.
3. Tag on upload: `approved-assets`, `category-<cat>`, `import-<date>`, plus `print-ok` or `needs-hires-swap` by resolution.
4. **Never overwrite a master.** Create a derivative or a campaign-specific export.

**Drive-side gotcha:** the GDrive-on-LaCie mount lags `find` enumeration of just-written files and
has dropped a file mid-`mv`. Verify per-file with `os.path.isfile`, never `find | wc`.

**Selection convention:** Ramsey marks a Drive asset for the DAM by putting **`website`** in the
filename. Strip `-website` to match the Drive master.

## 8. Credit budget

25/month, historically ~10% used. Transformations and storage both count.
- Don't generate speculative derivative sets.
- Prefer on-the-fly transform URLs over uploading new renditions.
- Before enabling any MediaFlows automation, **confirm whether flow executions bill against credits** — a 100-asset batch triggering 2–3 flows becomes 200–300 executions.

## 9. MediaFlows — recommended build order

**⚠️ Unverified: is MediaFlows even included on the FREE plan?** Seeing the UI is not proof. Confirm
availability *and* metering before building anything.

1. **⭐ Auto-tag by resolution.** On upload: `width < 2000 OR height < 2000` → tag `needs-hires-swap`, else `print-ok`. **Build this first** — it converts the print gate from "someone remembered" to mechanical, which is the failure mode that actually costs money.
2. **Smart Rename** to `YYYYMMDD_UM_<CATEGORY>_<Subject>_v#` on upload. Fixes the inflow; does **not** retroactively fix the existing 31.
3. **AI auto-tagging** → `category-*`. Useful, lower stakes. **Verify the add-on's credit cost.**
4. **Auto-expire campaign assets** → `retired-YYYY-MM`. Only worth building once `campaign-<slug>` tagging is actually in use.

**Not worth it:** Akeneo/PIM sync (no PIM in the stack) · Quality Check (flow 1 covers the real risk).

## 10. 🔴 Access — what's blocked right now

**I cannot audit the DAM.** No Cloudinary credentials exist locally, and the claude.ai Cloudinary
connector is **not authorized**. So I can't enumerate assets, read tags, verify the `needs-hires-swap`
count, or confirm folder contents. Everything above is from repo documentation plus what I could
verify by fetching delivery URLs.

**To unblock, either:**
- **Authorize the Cloudinary connector** in claude.ai connector settings *(easiest — then I can search and audit directly)*, or
- Tell me where a **Master API key** lives locally and I'll drive the Admin API by curl.

**What I'd do first once unblocked:**
1. Full inventory — count, folders, total bytes, credit usage.
2. Audit `needs-hires-swap` against actual dimensions — confirm the ~141 figure and find any low-res asset *missing* the tag. **That's the dangerous case.**
3. List candidates for `hero-approved` so the tagging pass is a review rather than a hunt.
4. Find orphans: assets in Home, in `submissions/`/`inspiration/`, or referenced nowhere.
