# Decision Log Schema

The shared format for `campaigns/{slug}/decisions.md`. Each stage appends one section.

## Initial creation (Stage 2 creates this file if absent)

```markdown
# Decisions — {Campaign Name}

**Slug:** {YYYY-MM}-{slug}
**Created:** {YYYY-MM-DD}

---
```

## Stage 2 entry (Style)

```markdown
## Stage 2: Style

- **Chosen style:** {style-name}
- **File:** `_styles/{style-slug}.md`
- **Why:** {reasoning}
- **Alternatives considered:** {other styles, if any close calls}
- **Decided at:** {YYYY-MM-DD HH:MM}
```

## Stage 3 entry (Assets)

```markdown
## Stage 3: Assets

- **Logo:** {logo-name} ({color variant})
  - Canva Kit: `{kAFqKpAzOh0 or kAGze1MPDmA}`
  - Reasoning: {if non-default}
- **Photos picked:**
  - {description} — {Drive URL or Canva ref} — {1-line reasoning}
  - ...
- **Photo specs requested but not yet sourced:**
  - {description} — {orientation, treatment}
- **Decided at:** {YYYY-MM-DD HH:MM}
```

## Stage 4: NO entry in decisions.md

(Stage 4 creates `concepts/concept-N.md` files. The picked concept is logged in Stage 5's entry.)

## Stage 5 entry (Refine & Export)

```markdown
## Stage 5: Refine & Export

- **Picked concept:** concept-{N}
- **Refinements applied:** {brief list}
- **Final saved to:** `final/final.md`
- **Decided at:** {YYYY-MM-DD HH:MM}
```

## Append rule

Always append. Never rewrite previous sections.

If the user wants to change an earlier decision, add an OVERRIDE section noting it:

```markdown
## Stage 2 OVERRIDE (after Stage 4)

- **Original:** Bold Cantina Energy
- **New:** Family Fiesta
- **Why:** User decided after seeing concepts that the Family Fiesta direction matched the audience better
- **Decided at:** {YYYY-MM-DD HH:MM}
- **Cascading effect:** Stages 3 and 4 may need re-running.
```
