# Lovable Prompt — Fact Corrections (paste AFTER current builds finish)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Two fact corrections that affect multiple pages. Paste this AFTER the in-flight builds (/about, /private-events, /contact, /mezzanine) complete — these corrections will overwrite any wrong numbers in those pages.

---

## PASTE BELOW THIS LINE INTO LOVABLE

Two facts were wrong in earlier prompts. Apply these corrections across every page that references them.

### Correction 1: Uno Más is kid-friendly at ALL times — no 21+ window

Earlier brand intel said "21+ after 9pm Fri/Sat" — that's incorrect. Uno Más is kid-friendly at all times, full stop.

Find and remove any reference to:
- "21+ after 9pm"
- "21+ Fri/Sat"
- "Until 9pm" (in the context of "kid-friendly until 9pm")
- Anything implying an age restriction

Replace with simpler accurate phrasing where the concept appears:
- "Kid-friendly at all times."
- "All ages welcome."

Check these pages specifically: `/`, `/about`, `/contact`, `/menu/dinner`, `/menu/lunch`, `/menu/cocktails`, `/private-events`, `/mezzanine`, any FAQ section.

### Correction 2: Mezzanine capacity is higher than previously documented

**Old (wrong) numbers:**
- 20-32 seated dinner
- Up to 60 cocktail reception
- "32 seated · 60 standing"

**Correct numbers:**
- **35-40 seated dinner**
- **65-75 cocktail reception (standing)**

Update everywhere the Mezzanine capacity is referenced:

**On `/mezzanine`:**
- 3-stat callout band: "35-40 seated · 65-75 standing" (was "32 seated · 60 standing")
- Private Dinners card: "35-40 seated. Custom menus, full bar, dedicated server."
- Cocktail Receptions card: "Up to 75 standing. Open bar, light bites, and an upstairs that doesn't feel like a banquet hall."

**On `/private-events`:**
- Mezzanine Dinners event card capacity: "35-40 seated · 65-75 standing" (was "20-32 seated · 60 standing")

**On `/about`** (if it mentions Mezzanine capacity at all):
- Any range like "20-60" → "35-75"

**Any JSON-LD schema** on `/mezzanine` or `/private-events`:
- `maximumAttendeeCapacity` should be 75 (was 60)
- Update any other capacity-related fields

### Acceptance criteria

After this update:
- Zero references to "21+" anywhere on the site
- Zero references to "kid-friendly until 9pm" (replaced with "kid-friendly at all times")
- All Mezzanine seated capacity values are "35-40" (or just "35" or "40")
- All Mezzanine standing/cocktail-reception values are "65-75" (or "75 max")
- Schema markup `maximumAttendeeCapacity` reflects 75, not 60
- No layout or visual changes — just text edits
