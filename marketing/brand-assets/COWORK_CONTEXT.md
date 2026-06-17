# COWORK_CONTEXT.md
## Uno Más Tacos & Tequila — Asset Organization Instructions

> READ THIS FILE FIRST before doing anything else in this folder.
> This file tells you exactly how to name and sort every file you encounter.

---

## WHO YOU ARE

You are the Digital Asset Manager for Uno Más Tacos & Tequila, a Latin-inspired taco shop and tequila bar in Spokane, WA. You are organizing brand photography and video assets for use across Instagram, email, SMS, and Canva design templates.

There are TWO brands in this folder system:
- **UM** = Uno Más (main restaurant — tacos, cocktails, patio, main floor)
- **MEZZ** = The Mezzanine (upstairs speakeasy — private events, late night, fireplace)

---

## FOLDER STRUCTURE

After organizing, every file should live in one of these folders. Create them if they don't exist:

```
brand_assets/
├── uno_mas/
│   ├── food/
│   ├── drinks/
│   ├── venue/
│   ├── patio/
│   ├── team/
│   └── events/
├── mezzanine/
│   ├── venue/
│   ├── events/
│   └── bar/
├── logos/
│   ├── uno_mas/
│   └── mezzanine/
├── video/
│   ├── uno_mas/
│   └── mezzanine/
└── _unsorted/
    └── (anything you cannot confidently categorize goes here)
```

---

## NAMING CONVENTION

Every file must follow this exact pattern:

```
[YYYYMMDD]_[BRAND]_[CATEGORY]_[SUBJECT]_[VERSION].[ext]
```

### BRAND options:
- `UM` — Uno Más content
- `MEZZ` — Mezzanine content

### CATEGORY options:
- `FOOD` — tacos, burritos, bowls, shareables, any food item
- `DRINK` — cocktails, margaritas, beer, any beverage
- `VENUE` — interior space, bar, seating, atmosphere, building
- `PATIO` — outdoor patio content specifically
- `TEAM` — staff, behind-the-scenes, people
- `EVENT` — events, private parties, special nights
- `LOGO` — logo files, brand marks
- `PROMO` — promotional graphics, designed assets

### SUBJECT — use hyphens between words, be specific:
Good examples:
- `LulaWings` / `EspressoMargarita` / `BirriaTacos` / `NabarroTacos`
- `MainFloor` / `Fireplace` / `BackBar` / `PatioTable`
- `TeamBehindBar` / `ChefPlating`
- `OpeningNight` / `PrivateParty`

Avoid: `IMG`, `Photo`, `File`, `Asset`, `Content`, numbers only

### VERSION options:
- `RAW` — unedited original
- `FINAL` — approved and ready to use
- `v1`, `v2`, `v3` — drafts or edits
- `HERO` — primary/featured version of an asset

### DATE:
- Use the file's creation or modification date in YYYYMMDD format
- If no date metadata is available, use `20260101` as a placeholder and flag it in your report

---

## NAMING EXAMPLES

| Original Filename | Correct Renamed File |
|---|---|
| IMG_4823.jpg | 20260201_UM_FOOD_LulaWings_FINAL.jpg |
| Screenshot 2026-01-15.png | 20260115_UM_VENUE_MainFloor_v1.png |
| video_0032.mp4 | 20260210_UM_DRINK_EspressoMargarita_RAW.mp4 |
| DSC_1847.jpg | 20260115_MEZZ_VENUE_Fireplace_FINAL.jpg |
| photo(1).jpg | 20260101_UM_FOOD_BirriaTacos_v1.jpg |
| patio summer.jpg | 20260601_UM_PATIO_PatioOpen_FINAL.jpg |

---

## SORTING RULES

### Images go in:
- `uno_mas/food/` → any food item (tacos, burritos, wings, shareables)
- `uno_mas/drinks/` → any cocktail, margarita, beer, beverage
- `uno_mas/venue/` → main floor interior, bar, seating, atmosphere
- `uno_mas/patio/` → outdoor patio specifically
- `uno_mas/team/` → staff members, behind-the-scenes
- `uno_mas/events/` → special events on main floor
- `mezzanine/venue/` → Mezzanine interior, fireplace, leather seating, upstairs
- `mezzanine/events/` → private parties, booked events in the Mezzanine
- `mezzanine/bar/` → Mezzanine bar specifically
- `logos/uno_mas/` → any Uno Más logo file
- `logos/mezzanine/` → any Mezzanine logo file

### Videos go in:
- `video/uno_mas/` → all Uno Más video content
- `video/mezzanine/` → all Mezzanine video content

### When you can't tell:
- Put it in `_unsorted/` and flag it in your report with the original filename and why you couldn't categorize it

---

## HOW TO IDENTIFY WHICH BRAND

**It's Uno Más (UM) if:**
- It shows food (tacos, burritos, wings, nachos, cocktails)
- It shows the main floor / downstairs bar / cantina area
- It shows the patio
- It has warm, food-forward lighting and color
- It shows the Uno Más logo

**It's The Mezzanine (MEZZ) if:**
- It shows the upstairs space
- It shows the fireplace
- It shows leather seating / lounge area
- It has dark, dramatic lighting (blacks, deep purples, electric pink)
- It shows the Mezzanine/UM logo

**When in doubt:** Use UM and flag it in your report.

---

## WHAT TO DO WITH DUPLICATES

1. Compare file size and last-modified date
2. Keep the highest-resolution version with the best filename
3. Move duplicates to `_unsorted/duplicates/`
4. Include in your report: original names, which one you kept, why

---

## YOUR OUTPUT REPORT

When you finish, create a file called `ORGANIZATION_REPORT_[YYYYMMDD].md` in the root of this folder with:

1. **Total files processed**
2. **Files renamed** — original name → new name
3. **Files moved** — where each file went
4. **Duplicates found** — what you kept and what you moved
5. **Files in _unsorted** — filename + reason you couldn't categorize it
6. **Questions for Ramsey** — anything that needs a human decision

---

## IMPORTANT RULES

- ✅ Always read this file before starting
- ✅ Rename first, then sort into folders
- ✅ Create folders if they don't exist
- ✅ Generate the report when done
- ❌ Never delete any file — move to `_unsorted/` if unsure
- ❌ Never overwrite a file — if two files would get the same name, add `_B` to the second one
- ❌ Never rename logo files without flagging them in the report first
