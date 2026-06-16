# Lovable Prompt — Menu Page Bug Fixes (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Three targeted bug fixes on existing menu pages. No design overhaul yet — visual refactor comes in a separate pass.

---

## PASTE BELOW THIS LINE INTO LOVABLE

I found three bugs on the live menu pages. Please fix them without changing the visual design or layout — just clean up these specific issues.

### Bug 1: "Build Your Own Taco" component renders 3 times on /menu/lunch

On the /menu/lunch page, the "Build Your Own Taco" / taco proteins component currently appears three times:
- Once after the "Taco Plates" section
- Once after the "Tacos" section
- Once after the "Birria Tacos" section

Remove the duplicates. The component should appear **only once**, placed immediately under the "Tacos" section header (it serves as the protein-options legend for that section). Or — if you'd prefer — move it just above the Tacos section as a callout band. Either placement is fine, but **only one instance** of the component on the page.

### Bug 2: /menu/lunch hours footer is wrong

At the bottom of the /menu/lunch page there's a line that reads something like "Lunch available Tue–Fri 11am–2pm" — that's incorrect. Replace it with:

```
Lunch service · Tue–Sat · 11am–5pm
```

This should match the canonical hours data in Supabase `business_hours` (cantina is open Tue–Sat, with lunch service 11am–5pm per the `note` field). If possible, pull this dynamically from `business_hours` rather than hardcoding — query for `venue = 'cantina'` rows and read the lunch-service window from the note. If dynamic feels like over-engineering for one string, just hardcode "Tue–Sat · 11am–5pm" for now.

### Bug 3 (low-priority polish): Resy CTA on /menu/dinner

Currently there's a "Reserve a Table" CTA at the bottom of /menu/dinner under "Ready to sit down?". Add an additional Resy CTA in the **hero band at the top** of the page (next to or below the "Dinner" headline), so users don't have to scroll to the bottom to reserve.

Resy URL (already known to the project): `https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila`

Style the top hero CTA to match the existing site button system (whatever the current pink/brand button is using).

### Acceptance criteria

After this fix:
- View /menu/lunch — "Build Your Own Taco" component appears exactly once on the page
- View /menu/lunch — bottom footer says "Lunch service · Tue–Sat · 11am–5pm" (or pulls dynamically from Supabase)
- View /menu/dinner — there's a Reserve a Table CTA both in the hero AND at the bottom
- No other visual or layout changes
