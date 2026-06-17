# BRAND_ASSETS.md
## Uno Más Tacos & Tequila — Brand Assets Reference

**Version:** 1.0
**Last Updated:** 2026-02-28
**Owner:** Ramsey
**Status:** Active

> **AI AGENT NOTE:** This file documents all brand assets for both Uno Más and The Mezzanine. When generating Canva designs, always apply the correct brand kit using the IDs below. Never mix Uno Más and Mezzanine brand elements in the same design.

---

## TABLE OF CONTENTS

1. Canva Brand Kit IDs (Quick Reference)
2. Uno Más Taco Shop — Full Brand System
3. The Mezzanine @ Uno Más — Full Brand System
4. Logo Usage Rules
5. Asset Folder Structure
6. File Naming Convention
7. Asset Status Tracker

---

## 1. CANVA BRAND KIT IDs (QUICK REFERENCE)

| Brand | Canva Kit Name | Kit ID | When to Use |
|---|---|---|---|
| **Uno Más** | Uno Más Taco Shop | `kAFqKpAzOh0` | All main restaurant content |
| **The Mezzanine** | The Mezzanine @ Uno Más | `kAGze1MPDmA` | Mezzanine and speakeasy content only |

> When generating any Canva design, pass the appropriate `brand_kit_id` to ensure fonts, colors, and logos are applied automatically.

---

## 2. UNO MÁS TACO SHOP — FULL BRAND SYSTEM

### Color Palette

| Name | Hex | RGB | Use For |
|---|---|---|---|
| **Navy** | `#003366` | 0, 51, 102 | Dark backgrounds, text on light |
| **Blue** | `#18BCDC` | 24, 188, 220 | Headlines, accents, CTAs |
| **Pink** | `#E22690` | 226, 38, 144 | Primary brand color, logo, key highlights |
| **Yellow** | `#FFEC00` | 255, 236, 0 | Accents, callouts, energy moments |
| **White** | `#FFFFFF` | 255, 255, 255 | Backgrounds, reversed text |
| **Black** | `#000000` | 0, 0, 0 | Body text, dark UI |

**CSS Variables (for web use):**
```css
:root {
  --unomas-navy:  #003366;
  --unomas-blue:  #18BCDC;
  --unomas-pink:  #E22690;
  --unomas-yellow:#FFEC00;
  --unomas-white: #FFFFFF;
  --unomas-black: #000000;
}
```

### Typography

| Role | Font | Weights | Use For |
|---|---|---|---|
| **Headlines** | Antonio | Regular, Bold | All primary headlines and display text |
| **Body / UI** | Montserrat | Light, Regular, Medium, Bold | Body copy, captions, UI labels |

**Typography Hierarchy:**
- H1 Display: Antonio Bold — large, high-impact headlines
- H2 Section: Antonio Regular — section headers, menu category titles
- Body: Montserrat Regular — descriptions, captions, body copy
- Labels / Callouts: Montserrat Bold or Medium — prices, tags, emphasis

### Brand Marks & Logos

| Asset | Description | Use Case |
|---|---|---|
| **Primary Logo** | "Uno Más" script + agave icon + "TACOS & TEQUILA" bar | Default — all primary brand placements |
| **Wordmark Only** | "Uno Más" script without tagline bar | Space-constrained placements |
| **Agave Icon** | Pink agave plant icon standalone | Icon-only contexts, watermarks, favicons |

**Logo Color Versions:**
- Full color (Pink on white) — default
- Reversed (White on dark/Navy background)
- Single color Black — print, embossing
- Single color White — dark backgrounds

**Logo Spacing Rule:**
Empty space equal to the size of the agave icon must surround the logo on all sides. No competing elements within that boundary.

**Logo Restrictions:**
- Never place on high-contrast or visually competing patterns
- Drop shadow permitted at max 60% opacity if needed
- Never distort or stretch the logo
- Never recreate the logo in a different font

### Brand Voice Reminder (Uno Más)
Playful, confident, community-first. Antonio headlines hit hard. Pink is the hero color — don't let Navy or Blue dominate.

---

## 3. THE MEZZANINE @ UNO MÁS — FULL BRAND SYSTEM

> The Mezzanine has its own complete brand identity — separate colors, separate fonts, separate logo. It lives under the Uno Más umbrella but has its own visual world. Do not mix these assets with the main Uno Más brand.

### Color Palette

| Name | Hex | RGB | Use For |
|---|---|---|---|
| **Electric Pink** | `#E22790` | 226, 39, 144 | Primary brand color — bold, electric |
| **Magenta** | `#BF28BF` | 191, 40, 191 | Secondary accent |
| **Ultra Violet** | `#93009B` | 147, 0, 155 | Deep accent, dark UI |
| **Charcoal** | `#333333` | 51, 51, 51 | Dark backgrounds, text |
| **Deep Black** | `#000000` | 0, 0, 0 | Primary dark background |
| **White** | `#FFFFFF` | 255, 255, 255 | Reversed text, light elements |

**Color Character:**
The Mezzanine palette is dark, electric, and dramatic. Black and Charcoal are the foundation. Electric Pink through Ultra Violet create a gradient of intensity. This is not a warm, food-forward palette — it's a nightlife palette.

**CSS Variables:**
```css
:root {
  --mezz-electric-pink: #E22790;
  --mezz-magenta:       #BF28BF;
  --mezz-ultraviolet:   #93009B;
  --mezz-charcoal:      #333333;
  --mezz-black:         #000000;
  --mezz-white:         #FFFFFF;
}
```

### Typography

| Role | Font | Weights | Use For |
|---|---|---|---|
| **Titles / Display** | DIN Condensed VF | Demi Bold, Regular, Light | All headlines and display text |
| **Body / UI** | Poppins | Black, Bold, Regular, Medium, Light, Thin | Body copy, descriptions, labels |
| **Accent Callouts** | Baka Too | Regular | Decorative callouts, signature moments |

**Typography Hierarchy:**
- Display: DIN Condensed VF Demi Bold — event titles, big announcements
- Subheads: DIN Condensed VF Regular — section labels, venue info
- Body: Poppins Regular or Light — descriptions, copy
- Callouts: Baka Too — accent moments, taglines, special callouts

### Brand Marks & Logos

| Asset | Description | Use Case |
|---|---|---|
| **Primary Logo** | "UM" tribal/geometric mark + "MEZZANINE" wordmark | Default — all Mezzanine placements |
| **Mark Only** | "UM" tribal icon standalone | Icon contexts, small placements |
| **Wordmark Only** | "MEZZANINE" in DIN Condensed | Text-only placements |

**Logo Color Versions:**
- White on Black (primary — default)
- Electric Pink on Black (event/bold use)
- Gradient (Pink → Magenta → Ultra Violet) on Black — premium use
- Black on White — light background contexts
- White on Charcoal — mid-tone backgrounds

**The Mezzanine Logo Grid:**
The UM mark has multiple approved iterations across color combinations — all documented in the Mezzanine Branding Cheatsheet. Always use an approved combination, never improvise a new color pairing.

### Brand Voice Reminder (Mezzanine)
Darker, more mysterious, elevated. DIN Condensed is authoritative but not stiff. Lead with atmosphere over information. Electric Pink is the only warm element in a predominantly dark palette — use it intentionally.

---

## 4. LOGO USAGE RULES

### When to Use Which Brand

| Content Type | Brand to Use |
|---|---|
| Tacos, burritos, bowls, street food | Uno Más |
| Cocktails / happy hour (main floor) | Uno Más |
| Sunday Brunch | Uno Más |
| Patio content | Uno Más |
| General restaurant/community content | Uno Más |
| Mezzanine atmosphere / late night | The Mezzanine |
| Private events in The Mezzanine | The Mezzanine |
| Mezzanine event packages | The Mezzanine |
| Content explicitly about the upstairs speakeasy | The Mezzanine |

### Never Do
- ❌ Mix Uno Más Pink (`#E22690`) with Mezzanine typography in the same design
- ❌ Use Mezzanine's dark palette for food-forward content
- ❌ Use Antonio font in Mezzanine designs
- ❌ Use DIN Condensed in main Uno Más designs
- ❌ Place either logo on a competing visual pattern
- ❌ Recreate logos — always use approved files

---

## 5. ASSET FOLDER STRUCTURE

Recommended local folder structure inside `UNO_MAS_AI_HQ/`:

```
📁 UNO_MAS_AI_HQ/
├── 📁 knowledge/               ← All .md files (complete)
├── 📁 brand_assets/
│   ├── 📁 uno_mas/
│   │   ├── 📁 logos/
│   │   │   ├── primary/        ← Full color logo files
│   │   │   ├── reversed/       ← White versions
│   │   │   ├── black/          ← Single color black
│   │   │   └── icon_only/      ← Agave icon standalone
│   │   ├── 📁 fonts/
│   │   │   ├── Antonio/        ← .ttf or .otf files
│   │   │   └── Montserrat/     ← .ttf or .otf files
│   │   └── 📁 colors/
│   │       ├── UnoMas_Colors.ase    ← Adobe swatch file
│   │       └── UnoMas_Colors.css   ← CSS variables
│   ├── 📁 mezzanine/
│   │   ├── 📁 logos/
│   │   │   ├── primary/        ← UM mark + wordmark
│   │   │   ├── mark_only/      ← UM icon
│   │   │   ├── wordmark_only/  ← MEZZANINE text
│   │   │   └── gradient/       ← Gradient versions
│   │   ├── 📁 fonts/
│   │   │   ├── DIN_Condensed/
│   │   │   ├── Poppins/
│   │   │   └── Baka_Too/
│   │   └── 📁 colors/
│   │       ├── Mezzanine_Colors.ase
│   │       └── Mezzanine_Colors.css
│   └── 📁 shared/
│       └── 📁 photography/     ← Venue, food, cocktail photos
├── 📁 active_campaigns/
├── 📁 outputs/
└── 📁 agents/
```

---

## 6. FILE NAMING CONVENTION

### Logos
```
[BRAND]_LOGO_[VERSION]_[COLORMODE].[ext]

Examples:
UNOMAS_LOGO_PRIMARY_FULLCOLOR.png
UNOMAS_LOGO_PRIMARY_REVERSED.svg
UNOMAS_LOGO_ICON_FULLCOLOR.png
MEZZ_LOGO_PRIMARY_WHITE-ON-BLACK.png
MEZZ_LOGO_MARK_ELECTRICPINK.svg
MEZZ_LOGO_WORDMARK_WHITE.png
```

### Fonts
```
[FONTFAMILY]_[WEIGHT].[ext]

Examples:
Antonio_Bold.ttf
Antonio_Regular.ttf
Montserrat_Regular.ttf
Montserrat_Bold.ttf
DINCondensed_DemiBold.otf
Poppins_Regular.ttf
BakaToo_Regular.otf
```

### Photography / Video
```
[YYYYMMDD]_[BRAND]_[CATEGORY]_[SUBJECT]_[VERSION].[ext]

CATEGORY options: FOOD, DRINK, VENUE, TEAM, EVENT, PATIO, MEZZ
BRAND options: UM (Uno Más), MEZZ (Mezzanine)

Examples:
20260201_UM_FOOD_LulaWings_v1.jpg
20260215_MEZZ_VENUE_Fireplace_RAW.jpg
20260220_UM_DRINK_EspressoMargarita_FINAL.jpg
20260228_UM_PATIO_OpeningDay_v1.jpg
```

### Canva Templates
```
[BRAND]_[CATEGORY]_[TYPE]_[SUBJECT]_TEMPLATE

Examples:
UM_SOCIAL_POST_FoodFeature_TEMPLATE
UM_SOCIAL_STORY_HappyHour_TEMPLATE
MEZZ_EVENT_FLYER_PrivateEvent_TEMPLATE
UM_EMAIL_HEADER_Promotional_TEMPLATE
```

---

## 7. ASSET STATUS TRACKER

Use this to track what's been organized, what's missing, and what needs attention.

| Asset | Brand | Status | Location | Notes |
|---|---|---|---|---|
| Primary logo (full color) | Uno Más | ✅ In Canva | Brand Kit `kAFqKpAzOh0` | Export SVG + PNG needed |
| Primary logo (reversed) | Uno Más | ⚠️ Confirm | Brand Kit `kAFqKpAzOh0` | Verify white version exists |
| Agave icon standalone | Uno Más | ⚠️ Confirm | Brand Kit `kAFqKpAzOh0` | Needed for favicon/icon use |
| Antonio font files | Uno Más | ❓ Unknown | — | Pull from Canva or Google Fonts |
| Montserrat font files | Uno Más | ❓ Unknown | — | Available on Google Fonts |
| Color swatch file (.ase) | Uno Más | ❌ Not created | — | Create from hex values above |
| Primary logo (white on black) | Mezzanine | ✅ In Canva | Brand Kit `kAGze1MPDmA` | Export needed |
| UM mark standalone | Mezzanine | ⚠️ Confirm | Brand Kit `kAGze1MPDmA` | Verify standalone exists |
| DIN Condensed VF font | Mezzanine | ❓ Unknown | — | May need license check |
| Poppins font files | Mezzanine | ❓ Unknown | — | Available on Google Fonts |
| Baka Too font files | Mezzanine | ❓ Unknown | — | May need purchase/license |
| Color swatch file (.ase) | Mezzanine | ❌ Not created | — | Create from hex values above |
| Food photography | Both | ❓ Unorganized | Local folder | Needs naming + organizing |
| Venue photography | Both | ❓ Unorganized | Local folder | Needs naming + organizing |

---

*BRAND_ASSETS.md — Uno Más Tacos & Tequila*
*Version 1.0 | Updated: 2026-02-28 | Owner: Ramsey*
*Canva Brand Kits: Uno Más (`kAFqKpAzOh0`) | The Mezzanine (`kAGze1MPDmA`)*
*Companion files: BRAND_VOICE_MASTER.md | VENUE_AND_OPERATIONS.md*
