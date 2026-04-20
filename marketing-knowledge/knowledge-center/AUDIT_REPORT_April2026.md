# UNO MÁS — KNOWLEDGE CENTER AUDIT REPORT
**Date:** April 9, 2026 · **Issues Resolved:** April 20, 2026
**Auditor:** Claude / Cowork
**Scope:** All Knowledge Center MD files + 14 website templates + `_CHANNEL_READY/Website/` photo library
**Status:** ✅ Issues 1–4 resolved by Ramsey on 2026-04-20. Photo library reference below retained for ongoing use.

---

## SUMMARY

All 4 factual discrepancies identified in the original audit have been resolved. Canonical values below under "KEY FACTS LOCKED IN." The Knowledge Center is now internally consistent on hours, address, ZIP, menu offerings, and reservation phrasing.

---

## RESOLUTION RECORD (2026-04-20)

| Issue | Resolution |
|---|---|
| **1. Opening time** | Open 11am Tue–Sat. Lunch 11am–5pm, Dinner 5pm–9pm Tue–Thu / 5pm–10pm Fri–Sat. |
| **2. Sunday hours** | Currently closed Sun & Mon. Sunday Brunch launches Mother's Day 2026, Sundays 10am–4pm going forward. |
| **3. ZIP code** | Confirmed **99205**. Fixed across `business.md`, `digital-ecosystem.md`, `system-prompt.md`, `CLAUDE_DESIGN_SYSTEM_BRIEF.md`, `README.md`. |
| **4. Reservation phrasing** | Canonical copy: "Reservations not required but recommended. Walk-ins welcomed." |
| **Bonus: Lunch Special** | Removed. Lunch and Dinner now operate as separate menus — there is no $12 2-taco deal. `MENU_AND_OFFERS.md` section removed and sections renumbered. |
| **Bonus: Address landmark** | Added to `VENUE_AND_OPERATIONS.md` Business Essentials: "Behind Indaba Coffee, corner of Knox Ave & N Monroe." |

---

## ORIGINAL ISSUES (for historical reference)

### 🔴 ISSUE 1 — Opening Hours Conflict (Critical) — ✅ RESOLVED

Three documents disagree on what time the restaurant opens Tuesday–Saturday:

| Document | Opening Time |
|---|---|
| `VENUE_AND_OPERATIONS.md` | 12pm (Tue–Thu, Fri–Sat) |
| `UnoMas_CopyBank_April2026.md` (header) | 11am (Tue–Thu, Fri–Sat) |
| `MENU_AND_OFFERS.md` | Lunch Special runs 11am–5pm (implies 11am open) |
| Current homepage template | 12pm (uses VENUE_AND_OPERATIONS version) |

**Likely answer:** Open at 11am for lunch service (consistent with Lunch Special). If so, VENUE_AND_OPERATIONS.md needs correcting.

> **⚡ ACTION NEEDED:** Confirm — does the restaurant open at 11am or 12pm, Tuesday–Saturday?

---

### 🔴 ISSUE 2 — Sunday Hours Missing in CopyBank (Critical) — ✅ RESOLVED

The `UnoMas_CopyBank_April2026.md` header lists:
> "Hours: Tue–Thu 11am–9pm | Fri–Sat 11am–10pm | **Sun–Mon Closed**"

But `VENUE_AND_OPERATIONS.md` clearly shows:
- Sunday: 12pm – 8pm (with Brunch 9am–2pm)
- **Only Monday is closed**

The homepage template correctly shows Sunday open. The CopyBank header is wrong and will cause errors in any AI-generated content that references it.

> **⚡ ACTION NEEDED:** Confirm Sunday hours, then CopyBank header will be updated to match.

---

### 🟡 ISSUE 3 — ZIP Code (Minor) — ✅ RESOLVED

`VENUE_AND_OPERATIONS.md` lists the address as:
> 2020 N Monroe St, Suite C, Spokane, WA **99201**

All other documents and the homepage template use **99205**, which is the correct ZIP for North Monroe.

> **⚡ ACTION NEEDED:** Confirm correct ZIP (almost certainly 99205) — will update VENUE_AND_OPERATIONS after confirmation.

---

### 🟡 ISSUE 4 — Homepage Template Copy Phrasing (Minor) — ✅ RESOLVED

The current `web_page_homepage_v1.html` has this in the info section:
> "No reservations for main floor walk-ins welcome."

This is grammatically awkward. Suggested replacement (in brand voice):
> "No reservations needed for the main floor. Walk right in."

Or even more on-brand:
> "Main floor is first come, first served. Walk-ins always welcome."

> **⚡ ACTION NEEDED:** Confirm preferred phrasing, will update across all 14 templates.

---

## ITEMS TO ARCHIVE / DEPRECATE

### 🗂 ARCHIVE — Website Guidelines Doc (Outdated)

`UnoMas_Website_Guidelines_Homepage.md` was clearly written for an earlier phase of the brand and contains several outdated references that will cause problems if used as a source:

| Outdated Element | What It Says | Reality |
|---|---|---|
| Locations | "Three locations: Wonder Building, South Valley, Monroe" | Monroe only |
| Fonts | Martellas Caps, Palmer Lake Print, Narrabeen, Santos | Antonio + Montserrat |
| Ordering CTA | "Order Now" / "Order Online" | No online ordering, dine-in only |
| Ordering platform | "Square Online" | No online ordering |
| Domain | unomastacos.com | unomastacoshop.com |
| Mezzanine location | "Above the Wonder Building" | Above Monroe flagship |

**Recommendation:** Move to `_ARCHIVE/` subfolder so it's not accidentally referenced by AI agents. It served its purpose but will produce wrong output now.

---

## WHAT'S IN GOOD SHAPE ✅

| Document | Status | Notes |
|---|---|---|
| `UnoMas_BrandVoice_April2026.md` | ✅ Authoritative | Minor encoding issue near the end of file (binary characters) — content is readable but file may need to be resaved cleanly |
| `UnoMas_CopyBank_April2026.md` | ✅ Strong | Fix the hours header (Issues 1 & 2 above) — rest is excellent |
| `MENU_AND_OFFERS.md` | ✅ Accurate | Good source of truth for menu items and prices |
| `VENUE_AND_OPERATIONS.md` | ✅ Mostly Accurate | Fix ZIP (Issue 3), fix hours if Issue 1 resolves |
| All 14 HTML templates | ✅ On-brand | No external images, correct fonts and colors — see copy note above |

---

## KEY FACTS LOCKED IN (CONFIRMED ACROSS MULTIPLE FILES)

These are consistent and correct — use with confidence:

- **Name:** Uno Más Tacos & Tequila
- **Address:** 2020 N Monroe St, Suite C, Spokane, WA 99205
- **Phone:** (509) 960-7989
- **Website:** unomastacoshop.com
- **Email:** tacos@unomastacoshop.com | Events: karissa@unomastacoshop.com
- **Instagram:** @unomastacoshop
- **Hours:** Mon & Sun closed. Tue–Thu 11am–9pm (Lunch 11am–5pm / Dinner 5pm–9pm). Fri–Sat 11am–10pm (Lunch 11am–5pm / Dinner 5pm–10pm). *(Sunday Brunch launching Mother's Day 2026, Sundays 10am–4pm — do not reference publicly until launch week)*
- **Lunch Special:** ❌ REMOVED (2026-04-20). No $12 2-taco deal. Lunch and dinner are separate menus now.
- **Taco Tuesday:** ❌ NOT ACTIVE — do not reference
- **No delivery. Dine-in only.**
- **Loyalty Program:** Uno Mas Rewards: The Cantina Club
- **Primary Tagline:** "Get a little lost at Uno Más."
- **Brand Fonts:** Antonio (headlines) + Montserrat (body)
- **Brand Colors:** Navy #003366 | Teal #18BCDC | Pink #E22690 | Yellow #FFEC00

---

## WEBSITE PHOTO LIBRARY — APPROVED ASSETS CATALOG

All photos below are in `_CHANNEL_READY/Website/` — these are cleared for website use.

### 🏠 Main Floor Interior (56 photos)
`Hero_Lifestyle/Monroe_Interior/UM - Photos - Monroe - Interior - Downstairs /`

**Hero/Full-Bleed Recommended:**
- `2R7A3339.JPG` — currently used as homepage hero ✅
- `2R7A3619.JPG` — currently used as room background ✅
- `2R7A3616.JPG`, `2R7A3621.JPG` — strong wide-angle interior shots
- `2R7A7176.JPG`, `2R7A7194.JPG` — newer interior shots, excellent quality

**Detail/Feature Shots:**
- `2R7A3178.JPG` — currently used as intro feature ✅
- `2R7A3171.JPG`, `2R7A3172.JPG`, `2R7A3174.JPG` — interior detail shots
- `IMG_4070.JPG` – `IMG_4110-1.jpg` — additional interior variety

**Bar Shots:**
- `D8057198-E562-47EA-82AE-0D0F3B733D1E.jpeg` — bar area
- `IMG_0521.jpeg`, `IMG_1101.jpeg` — service moments

---

### 🎭 The Mezzanine (42 photos)
`Hero_Lifestyle/Monroe_Interior/UM - Photos - Monroe - Interior - Mezz/`

**Hero/Full-Bleed Recommended:**
- `DSC02008.jpeg` — currently used as Mezzanine feature ✅
- `DSC02043.jpeg`, `DSC02049.jpeg` — lounge shots
- `DSC02051.jpeg`, `DSC02066.jpeg`, `DSC02070.jpeg` — fireplace + leather scenes
- `DSC02080.jpeg`, `DSC02084.jpeg` — bar detail
- `2R7A7731.jpg` — wide-angle Mezzanine

**Additional Mezzanine:**
- `DSC02014.jpeg`, `DSC02022.jpeg`, `DSC02035.jpeg` — various atmosphere shots
- `IMG_1072.jpeg`, `IMG_1086.jpeg`, `IMG_1089.jpeg` — smaller detail shots
- `IMG_9857.jpg`, `IMG_9857-1.jpg`, `IMG_9857-2.jpg` — Mezzanine varied angles

---

### 🌿 Patio (1 photo)
`Hero_Lifestyle/Monroe_Interior/UM - Photos - Monroe - Interior - Patio/`
- `IMG_1982.jpeg` — only patio shot available. Seasonal content should note more photography is needed when patio opens.

---

### 🏗 Exterior / Building
`Hero_Lifestyle/Monroe_Exterior/`
- `IMG_0890.jpeg`, `IMG_0891.jpeg` — exterior of building
- `IMG_1996.jpg` — street view
- `Soft Open Hours - 3.jpeg` — soft open reference (do not use in current templates)

---

### 🌮 Food Photography (80+ photos)
`Food_Gallery/UM - Website - Photos /`

**Currently used in templates:**
- `Taco Close Up V11.png` — Birria card ✅
- `Lula Wings - V1.png` — Wings card ✅
- `Marg.jpeg` — Margarita card ✅

**Additional strong food shots for email/social:**
- `Chip Dip Trio v6.png` — chip & dip trio (best version)
- `Tijuana Flatbread.png`, `Tijuana Flatbread no background V2.png` — WTF menu feature
- `Waffle Fries.png` — sides feature
- `Street vs Quarter Pound Taco v5.png` — great for taco tier messaging
- `Fiesta Pack - V12.png` — event/catering feature
- `Food on Table v3.png` — table spread, good for social proof sections
- `Uno Mas - Tacos and Corn on Table.jpeg` — lifestyle food shot

**Caution — avoid these filenames:**
- Files numbered 1.png through 8.png (unnamed, unclear subject)
- `Soft Open` references
- Multiple `.psd` files (source only, not web-ready)

---

### 🖼 Logos (Approved Web Versions)
`Logos_Icons/UnoMas_Logos/`

**For dark backgrounds (nav, dark sections):**
- `UnoMas-TacosTequila-DARK-WhiteLettering-NoFrame@4x.png` ✅ (currently used)

**For light backgrounds:**
- `UnoMas-TacosTequila-DARK-BlueLettering-NoFrame@4x.png`

**For color/pink treatments:**
- `UnoMas-TacosTequila-PinkLettering-NoFrame@4x.png`
- `Uno Mas - Pink .png`

**Do NOT use:**
- Any `TacoShop` logo variants (outdated name/brand)
- `.psd` or `AI_Source` files (source files, not web-ready)

---

### 👥 Team Photos
`Team/UM - Photos - Monroe - Preopening - Team Beer Tasting /`
- Pre-opening team photos — authentic, human, good for "About" sections
- Note: These are pre-opening shots; consider updating with current team photos for web use

---

## COPY ACCURACY CHECK — ALL 14 TEMPLATES

| Template | Address | Phone | Hours | Tagline | Issues |
|---|---|---|---|---|---|
| homepage_v1 | ✅ 99205 | ✅ | ✅ 12pm | ✅ | Awkward "walk-ins" phrasing |
| homepage_luz-del-dia | — | — | — | — | Hours/contact likely in footer |
| homepage_dia-y-noche | — | — | — | — | " |
| homepage_noche-electrica | — | — | — | — | " |
| homepage_dinevo | — | — | — | — | " |
| mezzanine_* (5 templates) | — | — | — | — | Event package prices should match MENU_AND_OFFERS |
| menu_* (4 templates) | — | — | — | — | Menu items/prices should match MENU_AND_OFFERS |

**Recommendation:** Run a final pass on all non-v1 templates to verify address, phone, and hours once Issues 1–3 above are resolved by Ramsey.

---

*AUDIT_REPORT_April2026.md — Uno Más Tacos & Tequila*
*Generated: April 9, 2026 | Claude / Cowork*
*Next steps: Ramsey resolves Issues 1–4, then proceed to Klaviyo email template generation.*
