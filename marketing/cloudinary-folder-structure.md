# Cloudinary — Actual Folder Structure (verified 2026-08-26)

Read from the API, not from memory. **This supersedes the folder diagram in
`cloudinary-operating-guide.md`, which was partly fiction.**

## The one thing to understand first

Cloudinary has **two addressing systems that do not have to agree**:

- **`asset_folder`** — where the asset appears when you browse the Media Library UI
- **`public_id`** — the delivery URL, which may itself contain a path

**188 assets have a `public_id` path that points somewhere their `asset_folder` doesn't.**

| public_id says… | but it actually lives in… | count |
|---|---|---|
| `uno-mas/photos/food/…` | `uno-mas/approved-assets/photos/food` | 108 |
| `uno-mas/website/icons/…` | `uno-mas/approved-assets/icons` | 50 |
| `uno-mas/website/logos/…` | `uno-mas/approved-assets/logos` | 28 |
| `uno-mas/website/icons/…` | *(no folder at all)* | 1 |
| `uno-mas/website/promos/…` | *(no folder at all)* | 1 |

**`uno-mas/website/icons` and `uno-mas/website/promos` do not exist as folders.** You cannot browse
to them. They exist only as URL prefixes. That is why the guide listed them and why searching by
folder never found them.

**Consequences:**
- Browsing the UI and searching by folder give different answers.
- The GPT Action's scope expression (`asset_folder:uno-mas/*`) returns ~154 of 1,486 assets — it
  misses the **1,115 assets with a bare public_id**, which are the bulk of the library.
- Any search must match **both** fields or it silently under-reports.

## The real tree

```
uno-mas/                                  1,469 assets · 4.43 GB
├── approved-assets/                      1,440 · 4.35 GB      ← 97% of everything
│   ├── photos/                           1,123 · 2.91 GB   (7 loose at this level)
│   │   ├── food/          680 · 2.18 GB   ⚠ 559 low-res (82%)   ← 46% of the library
│   │   ├── brunch/         87 · 108 MB       13 low-res (15%)
│   │   ├── cocktails/      86 · 114 MB       39 low-res (45%)
│   │   ├── promo/          84 ·  94 MB       10 low-res (12%)
│   │   ├── building/       76 ·  98 MB        1 low-res  (1%)   ← healthiest folder
│   │   ├── venue/          70 · 179 MB       45 low-res (64%)
│   │   ├── team/           24 ·  87 MB   ⚠  22 low-res (92%)
│   │   └── events/          9 ·  17 MB        3 low-res (33%)
│   ├── videos/             162 · 1.39 GB
│   │   ├── food/  83 · 506 MB · team/ 30 · 353 MB · cocktails/ 15 · brunch/ 12
│   │   └── promo/  9 · mezzanine/ 6 · events/ 5 · venue/ 2
│   ├── icons/               76 ·  17 MB       45 low-res (59%)
│   ├── logos/               72 ·  10 MB        0 low-res  (0%)  ← all print-safe
│   └── graphics/             7 ·  29 MB        7 low-res (100%)
├── menu/                        11 ·  55 MB   all 11 low-res
│   └── dinner/ 6 · shareables/ 3 · raw-bar/ 2
├── website/                     11 ·  10 MB   all 11 low-res    ← only 11 REALLY live here
│   └── cantina/ 4 · events/love-island-finale/ 3 · cocktails/ 1 · dinner/ 1 · exterior/ 1 · patio/ 1
├── process/                      3        team-uploads/ 3        venue/patio/ 1
mezzanine/venue/                 14 ·  29 MB    7 low-res (50%)
<Home> (no folder)                3
```

**34 folders. Documented but nonexistent:** `website/icons`, `website/promos`, `menu` (as a
folder — only its children exist), `venue`, `generated`, `submissions`, `inspiration`.
**Exists but undocumented:** `uno-mas/process`, `approved-assets/videos/mezzanine`,
`website/{cocktails,dinner,exterior,patio}`, and 7 assets loose in `approved-assets/photos`.

The guide's rule *"anything in `submissions/`, `inspiration/` or `team-uploads/` is not approved"*
is mostly moot — two of those three folders don't exist and `team-uploads` holds 3 assets.

## 183 duplicate copies, 314 MB wasted

146 groups of byte-identical assets stored under different public_ids. The pattern is clear: the
**June 2026 import re-uploaded assets that already existed under descriptive slugs**, giving them
convention-compliant names without removing the originals.

| | |
|---|---|
| `20260623_UM_FOOD_SkirtSteakFlameGrill` | = `carne-asada-grilling-process` |
| `20260623_UM_FOOD_RawOystersOnIce` | = `oysters-overhead-square` |
| `20260623_UM_FOOD_SaucyWingsLimePlate` | = `lula-wings-overhead-hero` |
| `20260623_UM_FOOD_TortillaOverFlame` | = `tortilla-flame-process` |
| `20260623_UM_FOOD_GlazedWingsBlueBowl` | = `lula-wings-side-view` |

**This explains three separate mysteries at once:** why `photos/food` holds 680 assets (46% of the
library), why there are 466 naming violations, and why the same photo keeps surfacing under two
names in search. `SkirtSteakFlameGrill` is on the live Thursday tile right now — and it has a twin.

**Do not delete duplicates.** Both public_ids may be referenced somewhere. The safe move is to tag
the older copy `superseded-by-<new_id>` and exclude it from search by default.

## What this means for organization work

1. **`asset_folder` is the source of truth for browsing; `public_id` is the source of truth for
   delivery.** They will keep diverging unless uploads always set `asset_folder` explicitly.
2. **`photos/food` is 46% of the library and 82% low-res.** It is simultaneously the biggest and
   the least print-ready folder. Any curation pass starts here.
3. **`logos/` is the only folder that is 100% print-safe.** 72 assets, zero under 2048px.
4. **Folder structure is not the problem — tags are.** The tree is reasonable. What's broken is
   that 699 low-res assets are unmarked, 64 are wrongly marked printable, and two tag conventions
   are running at once.
