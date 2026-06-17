# Uno Mas Asset Library — Full Organization Report

**Generated:** March 01, 2026
**Organizer:** Claude AI (uno-mas-asset-organizer skill)
**Scope:** Complete — Photos (Phase 1) + Videos (Phase 2)

---

## Executive Summary

| Metric | Photos | Videos | Total |
|--------|--------|--------|-------|
| Total files found | 616 | 379 | 995 |
| Unique files organized | 597 | 270 | 867 |
| Duplicates detected | 19 | 38 | 57 |
| Skipped (cloud lock) | 0 | 109 | 109 |
| Processing errors | 1 | 0 | 1 |

All original files have been **preserved** in their source locations. Organized copies were placed in the `brand_assets/` folder structure with standardized naming.

109 video files could not be copied due to Google Drive FUSE mount resource locks — they are fully classified in the JSON log and can be copied when the lock releases.

---

## Naming Convention

All files follow this format:

```
YYYYMMDD_BRAND_CATEGORY_Subject_VERSION.ext
```

**Photo examples:**
| Before | After |
|--------|-------|
| `DSC03841.jpg` | `20251217_UM_VENUE_VenueInterior_FINAL.jpg` |
| `IMG_3639.jpeg` | `20251027_UM_EVENT_BloodyMaryBash_FINAL.jpeg` |
| `DSC02149.jpeg` | `20251028_MEZZ_VENUE_MezzanineInterior_FINAL.jpeg` |

**Video examples:**
| Before | After |
|--------|-------|
| `UNO MAS 31.mp4` | `20251217_UM_FOOD_MomentumShoot31_RAW.mp4` |
| `Epic Quesadilla Making_ The Ultimate Foodie Hook!.mp4` | `20251230_UM_FOOD_EpicQuesadillaMaking_FINAL.mp4` |
| `Pouring a Marg-1.mp4` | `20260207_UM_DRINK_PouringAMarg_RAW.mp4` |
| `Adulting is a scam - v3.mp4` | `20260208_UM_PROMO_AdultingIsAScam_v3.mp4` |
| `gemini_generated_video_D5C2DDB5.mov` | `20260212_UM_FOOD_GeminiGenD5C2DDB5_v1.mov` |

---

## Photo Organization (Phase 1)

| Destination Folder | Count | Content |
|---|---|---|
| `uno_mas/food/` | 431 | Tacos, tortas, sopes, birria ramen, nachos, sides, desserts, food spreads |
| `uno_mas/drinks/` | 60 | Margaritas, palomas, bloody marys, beer, cocktails |
| `uno_mas/venue/` | 29 | Interior shots, bar, seating, exterior |
| `uno_mas/events/` | 20 | Bloody Mary Bash 2025 event photos |
| `uno_mas/promo/` | 1 | Cinco de Mayo promotional content |
| `mezzanine/venue/` | 23 | Dark/moody venue shots with purple lighting |
| `_unsorted/` | 33 | Creative inspiration screenshots, graphics, AI content |
| `_unsorted/duplicates/` | 19 photo dupes | Same content with "(1)" suffix confirmed by size |

---

## Video Organization (Phase 2)

Videos were organized into subcategories within `video/uno_mas/` for better usability:

| Destination Folder | Copied | Skipped | Total | Content |
|---|---|---|---|---|
| `video/uno_mas/raw_clips/` | 69 | 26 | 95 | Momentum Studios pro shoot footage, GIGIM raw masters, food prep clips |
| `video/uno_mas/edited/` | 71 | 24 | 95 | GIGIM produced content, CapCut exports, campaign edits, end cards |
| `video/uno_mas/social_reels/` | 87 | 53 | 140 | Jaden content creator clips, IG Story videos |
| `video/uno_mas/ai_generated/` | 11 | 0 | 11 | Gemini AI-generated food videos |
| `_unsorted/duplicates/` | 32 | 6 | 38 | Video duplicates (by filename pattern + size matching) |

### Video Source Mapping

| Source Folder | Files | Destination |
|---|---|---|
| Momentum Studios / Video Files | 75 | raw_clips (pro shoot RAW footage) |
| UM Content - GIGIM / Video Clips | 87 | edited (produced food content) |
| UM Content - GIGIM (root masters) | 3 | raw_clips (6.8 GB raw masters) |
| Jaden - UM Content | 111 | social_reels (mixed creator content) |
| UM IG Stories | 49 | social_reels (IG story clips) |
| Tacos are our love language | 14 | edited (campaign video variations) |
| Uno Mas Video Clips | 6 | raw_clips (food prep footage) |
| Margs-Palomas-Cocktails | 12 | raw_clips + edited (cocktail making) |
| Gemini Content | 12 | ai_generated (AI food videos) |
| Cap Cut Exports | 5 | edited (social media exports) |
| UM- Video End Cards | 4 | edited (end card graphics) |

---

## Complete Folder Structure

```
brand_assets/
├── uno_mas/
│   ├── food/              (431 photos)
│   ├── drinks/            (60 photos)
│   ├── venue/             (29 photos)
│   ├── events/            (20 photos)
│   ├── patio/             (empty — patio shots currently in food/)
│   ├── team/              (empty — team shots currently in food/)
│   └── promo/             (1 photo)
├── mezzanine/
│   ├── venue/             (23 photos)
│   ├── events/            (empty)
│   └── bar/               (empty)
├── logos/
│   ├── uno_mas/           (existing logos in separate folder)
│   └── mezzanine/
├── video/
│   ├── uno_mas/
│   │   ├── raw_clips/     (69 videos — 95 total when cloud unlocks)
│   │   ├── edited/        (71 videos — 95 total when cloud unlocks)
│   │   ├── social_reels/  (87 videos — 140 total when cloud unlocks)
│   │   └── ai_generated/  (11 videos)
│   └── mezzanine/         (empty — no Mezzanine-specific video found)
└── _unsorted/
    ├── (33 photos)
    └── duplicates/        (19 photo dupes + 32 video dupes = 51)
```

---

## Known Limitations & Recommendations

### Items Needing Manual Review

1. **Jaden Photo Classification** — ~15-20 photos from the Jaden folder are in `uno_mas/food/` but are actually team, venue, drink, or patio content. A quick manual pass can reclassify them.

2. **Jaden Video Classification** — All 111 Jaden videos are tagged as FOOD, but the content is mixed (food, drinks, venue shots). Same as photos — a manual pass would improve accuracy.

3. **IG Stories** — 73 photos + 49 videos have social media text overlays. Usable for social but not ideal for website/print.

4. **109 Skipped Videos** — These files are fully classified in `organize_videos_log.json` with their intended destinations and standardized names. When the Google Drive sync lock releases, the script can be re-run to copy them.

5. **Unsorted Items** (33 photos) — Creative inspiration screenshots, line art, AI-generated content — not original UM photography.

### Future Improvements

- Logo files (23 UM + 15 MEZZ) could be renamed and sorted into `brand_assets/logos/`
- Empty folders (`patio/`, `team/`, `mezzanine/events/`, `mezzanine/bar/`) are ready for future content
- Consider separate `promo/` subfolder under `video/uno_mas/` for campaign-specific edits

---

*Operation logs:*
- *Photos: `organize_photos_log.json`*
- *Videos: `organize_videos_log.json`*
