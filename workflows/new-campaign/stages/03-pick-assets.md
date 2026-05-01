# Stage 3 — Pick Assets

## Goal

Recommend 3-5 photos and 1 logo variant that fit the brief and chosen style. User confirms or overrides. Save picks.

## What to load before this stage

- `campaigns/{slug}/brief.md`
- `campaigns/{slug}/decisions.md` (to know the chosen style)
- The chosen `_styles/{style-slug}.md` only — not all styles
- `marketing-knowledge/brand-assets/BRAND_ASSETS.md` (asset rules and Canva kit IDs)
- `brand-intelligence-center/system-prompt.md` (brand visual identity quick ref)

## Steps

1. Read brief, decisions (chosen style), brand assets doc.
2. Phase 0 caveat: assets currently live in Ramsey's Canva and Drive folders, not catalogued in this repo. **Ask the user for the actual image URLs or Canva references** they want used. Save those URLs/refs into the campaign decisions.
3. Recommend logo variant per chosen style (see logic below).
4. Save the asset references to `decisions.md`.
5. Ask: "Assets locked in. Ready for Stage 4 (generate concepts)?"

## Logo recommendation logic

| Chosen style | Default logo | Rationale |
|---|---|---|
| Bold Cantina Energy | Uno Más wordmark, Pink-on-White | Default, energetic |
| Family Fiesta | Uno Más wordmark, Pink-on-White | Default, warm |
| Modern Mexican Minimal | Uno Más wordmark, Pink-on-White | Default, restrained accent |
| Premium Cocktail Lounge | Mezzanine wordmark (NOT Uno Más) | Mezzanine sub-brand uses its own logo per Ramsey's separation rules |
| Street Taco Grit | Uno Más wordmark, Pink-on-Black | Two-color palette fits this style |

Reverse / Mezzanine variants per Ramsey's `voice-identity.md`. Canva Kit IDs: Uno Más `kAFqKpAzOh0`, Mezzanine `kAGze1MPDmA`.

## Photo guidance

In Phase 0, photo selection is manual — staff identifies the right Drive/Canva asset themselves. The workflow should:

- Suggest the type of photo needed based on brief + style ("a top-down margarita shot," "a duotoned carne asada plate," "a moody Mezzanine interior")
- Ask the user to provide URLs or Drive links for the photos they want to use
- Note photo specs the user should aim for (orientation: square / portrait / landscape; treatment: full-color / duotone / B&W)
- Cross-reference Ramsey's photography rules from `voice-identity.md` if needed

This is intentional — Phase 0 validates whether staff can find the right assets in their existing Drive/Canva. Track C of the V1 app builds the integrated asset library.

## Schema for `decisions.md` (Stage 3 section)

```markdown
## Stage 3: Assets

- **Logo:** {logo-name} ({Pink-on-White / White-on-Navy / etc.})
  - Canva Kit: `{kAFqKpAzOh0 or kAGze1MPDmA}`
  - Reasoning: {if non-default}
- **Photos picked:**
  - {photo description or display name} — {Drive URL or Canva ref} — {1-line reasoning}
  - {photo 2} — {ref} — {reasoning}
  - ...
- **Photo specs requested but not yet sourced:**
  - {description of needed photo} — {what type, orientation, treatment}
- **Decided at:** {YYYY-MM-DD HH:MM}
```

## Common issues

- **No matching asset exists.** Flag and ask: "We need a {description} photo for this concept. Do you have one in Drive/Canva, or should we plan to shoot/source one before this campaign launches?" Note the gap in the campaign retro.
- **User picks a Mezzanine asset for Cantina content (or vice versa).** Flag per Ramsey's brand separation rules.
- **User wants a stock photo.** Phase 0 rule: only Uno Más / Mezzanine approved assets. Flag and ask Ramsey if needed.
- **User wants AI-generated imagery as the final.** Phase 0 = template-bounded only. AI image gen is OK at Stage 4 as concept *exploration*, not as the final asset.
