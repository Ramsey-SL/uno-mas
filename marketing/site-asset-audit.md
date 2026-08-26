# Live Site Asset Audit — 2026-08-25

Every Cloudinary asset the live site actually ships, with its **true** resolution measured by
fetching the original and reading the image header. **No Cloudinary credentials were used** — this
is the subset of the DAM that can be audited from the outside, and it happens to be the subset that
matters most, because it's what guests actually see.

Method: crawl all 11 routes in `sitemap.xml`, extract every `res.cloudinary.com/drxrfyq9i` public_id,
strip transform segments, fetch each original, parse dimensions from the JPEG/PNG/WebP header.
Raw data in `site-asset-audit.json` (includes which pages use each asset).
Reproduce with `scripts/cloudinary-audit.py` once credentials exist — that covers the whole library.

## Totals

| | |
|---|---|
| Images shipped | **66** (62 distinct — 4 ship under two URL forms) |
| Videos shipped | **10** — all resolve, none broken |
| **Long edge ≤ 2048px** | **20 — 30% of shipped images** |
| Long edge 2049–2399 (small format only) | 5 |
| **Naming-convention violations** | **44** |
| Broken references | **0** |

## Finding 1 — 30% of what the site ships is a 2048px derivative

Twenty images are at or under 2048px on the long edge, which is the iCloud shared-album signature
(see the 2048 trap in `cloudinary-operating-guide.md`). Almost the entire `20260623_*` June set is
in this group, and that set carries the venue, patio and food photography across the site.

**For web this is fine.** For any print piece it is not, and the tag is the only thing standing
between these files and a table tent.

## Finding 2 — a 244×481 image is on three pages

`UM_-_Daily_Specials_-_June_2026_wtgpaz` is **244×481** and appears on `/`, `/catering` and
`/now-hiring`. That is smaller than a phone thumbnail. If it renders at any real size it is visibly
soft, and it is also **June daily-specials creative on a site whose specials changed in August** —
so it is likely both low-quality *and* out of date. **Check this one first.**

## Finding 3 — the naming problem is 44, not 31

Registry §4 item 19 records 31 non-conforming assets. On the live site alone there are **44**:
the `IMG_*` set (15), the `2R7A*` set (4), the whole `MEZZ_*` set (which uses `_MEZZ_` where the
convention wants `_UM_`), the `uno-mas/website/icons/*` path-based ids, and the Cloudinary
auto-generated slugs (`evxpzyftmm2npufta3db`, `d72ajps8zp3jflmqynne`, `x6pr9oakrtxj5dgbzikn`).

**The resolution stands: tag, don't rename.** The site references these by public_id and a rename
breaks the URL. But the count in the registry is wrong and understates the problem.

## Finding 4 — 4 assets ship under two different URLs

`20251028_MEZZ_VENUE_MezzFireplace_RAW`, `20251028_MEZZ_VENUE_MezzSeatingAndBar_RAW`,
`20260125_UM_FOOD_TacoCloseUpV10_FINAL` and `20260207_UM_DRINK_PitcherAndMarg_FINAL` are each
referenced both bare and with a `v<version>/` prefix. Same bytes, two cache entries, two CDN
warm-ups. Harmless but wasteful, and it inflates any count taken from the markup.

## What this does NOT answer

**Library size.** The site ships 62 distinct images. That says nothing about whether the DAM holds
154 or ~1,350 — it only proves the site uses a small curated slice. That contradiction is still
open and still blocks planning the `hero-approved` pass.

## Recommended order once the connector is authorized

1. Run `scripts/cloudinary-audit.py --csv` — settle the library size, then everything else follows.
2. **Audit `needs-hires-swap` against real dimensions.** The dangerous case is a low-res asset
   *missing* the tag. The script reports exactly that.
3. Replace `UM_-_Daily_Specials_-_June_2026_wtgpaz` — wrong size and probably wrong content.
4. Tag `hero-approved` — scope it against the real count, not the disputed one.
5. Tag the 44 non-conforming assets rather than renaming them.
