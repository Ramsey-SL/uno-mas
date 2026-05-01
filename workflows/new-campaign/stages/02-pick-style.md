# Stage 2 — Pick a Style

## Goal

Recommend 2 style boards that fit the brief. User picks one. Save the choice.

## What to load before this stage

- `campaigns/{slug}/brief.md` (from Stage 1)
- `brand-intelligence-center/system-prompt.md`
- All five `_styles/*.md` files

## Steps

1. Read the brief.
2. Read every `_styles/*.md` file.
3. Recommend 2 styles. For each:
   - Name the style
   - Quote the 1-line description
   - Explain in 1-2 sentences why it fits this brief
4. Ask the user to pick one (or override with a different style).
5. Save the choice to `campaigns/{slug}/decisions.md` (create the file if it doesn't exist).
6. Ask: "Style locked in. Ready for Stage 3 (pick assets)?"

## Recommendation logic

Match brief signals to style "Example use cases":

| If brief signals... | Lean toward |
|---|---|
| Mezzanine venue / late night / 21+ / cocktail / tequila tasting | Premium Cocktail Lounge |
| Sunday Brunch / Mother's Day / family / patio daytime | Family Fiesta |
| Dinner program / new menu / press / editorial / travelers | Modern Mexican Minimal |
| Cinco de Mayo / weekend party / specials / happy hour / Cantina | Bold Cantina Energy |
| Birria / single-item drop / late-night / Chef's Pick | Street Taco Grit |

Cross-check against the style's "When NOT to use this style" sections — if the brief is clearly excluded, drop that style from recommendations.

If the **venue is Mezzanine**, default to Premium Cocktail Lounge (it's the only style using the Mezzanine sub-brand palette per Ramsey's brand separation rules).

If the **daypart is Dinner** AND venue is The Cantina, lean Modern Mexican Minimal (per Ramsey's "elevated, considered, reservation CTA" register).

If two styles are close, present both with explicit tradeoffs:

> "Bold Cantina Energy fits because it's our default party style and the brief is about a Cinco de Mayo weekend. Family Fiesta also fits because the brief mentions families. The difference: Bold Cantina is louder and night-feeling; Family Fiesta is warmer and day-feeling. Which day part matters more?"

## Schema for `decisions.md` after this stage

If `decisions.md` doesn't exist yet, create it with:

```markdown
# Decisions — {Campaign Name}

**Slug:** {YYYY-MM}-{slug}
**Created:** {YYYY-MM-DD}

---

## Stage 2: Style

- **Chosen style:** {style-name}
- **File:** `_styles/{style-slug}.md`
- **Why:** {1-2 sentences from the recommendation, plus user's reasoning}
- **Alternatives considered:** {other style if it was a close call}
- **Decided at:** {YYYY-MM-DD HH:MM}
```

If `decisions.md` already exists, append the Stage 2 section.

## Common issues

- **User picks a style that conflicts with the brief.** Flag it: "Premium Cocktail Lounge uses the Mezzanine sub-brand palette. The brief is about The Cantina lunch. Are you sure?" Don't override silently.
- **User wants a style not in `_styles/`.** Phase 0 is locked to the 5 existing styles. Note the request in `decisions.md` notes for the V1 spec input.
- **None of the styles fit.** Flag it: "None of the existing styles match this brief well. Closest is {X}, but {reason}. Want to add a new style board first, or proceed with the closest fit?"
- **User picks Premium Cocktail Lounge for Cantina content.** This violates Ramsey's brand separation rules. Flag and explain — Mezzanine palette/typography is sub-brand only.
