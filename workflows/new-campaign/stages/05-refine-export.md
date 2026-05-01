# Stage 5 — Refine & Export

## Goal

Take the picked concept, apply user-requested edits, produce a `final/` folder with a finalized recipe ready for the eventual app render or for a designer to execute.

## What to load before this stage

- `campaigns/{slug}/brief.md`
- `campaigns/{slug}/decisions.md`
- `campaigns/{slug}/concepts/concept-{N}.md` (the picked concept)
- `brand-intelligence-center/system-prompt.md`
- `marketing-knowledge/knowledge-center/UnoMas_CopyBank_April2026.md` (for refinement reference)

## Steps

1. Confirm which concept the user picked.
2. Ask: "What would you like to refine?"
   - Copy edits (most common)
   - Asset swap
   - Tone adjustment
   - Color/style nudge
3. Apply requested changes to a new file `campaigns/{slug}/final/final.md`.
4. If a Nano Banana visual was used, optionally regenerate `final/final.png` with refined inputs.
5. Document what changed in `final/notes.md`.
6. Update `decisions.md` with Stage 5 entry.
7. Ask: "Done. Want to run a retro on this campaign?"

## Schema for `final/final.md`

```markdown
# Final — {Campaign Name}

**Source concept:** concept-{N}
**Refined at:** {YYYY-MM-DD HH:MM}

## Locked recipe

This is what gets handed to a designer or rendered by the V1 app.

### Parameter set

- **Tone:** {final value}
- **Layout:** {final value}
- **Primary asset:** {asset reference}
- **Logo:** {logo reference}
- **Sections included:** {final list}
- **Accent color:** {final brand token}
- **Canva Kit ID:** {kAFqKpAzOh0 for Uno Más, kAGze1MPDmA for Mezzanine}

### Copy (final)

- **Headline:** {final ≤50 chars}
- **Subheadline:** {final ≤80 chars}
- **CTA:** {final ≤25 chars}
- **Caption:** {final, if Instagram}
- **Disclaimer:** {final, if applicable}

### Output target

- **Template:** `_templates/{template-slug}.md`
- **Format:** PNG / JPG / PDF / HTML / SMS-text
- **Dimensions:** {as defined by the template}
- **Platform:** {Instagram / flyer / email / SMS / etc}
- **Channel-specific notes:** {e.g., "Send via Klaviyo," "Schedule via Vista Social," "Print to table tent"}
```

## Schema for `final/notes.md`

```markdown
# Refinement notes — {Campaign Name}

## What changed from concept-{N}

- **Headline:** "{old}" → "{new}" — {1-line reason}
- **CTA:** "{old}" → "{new}" — {reason}
- **Asset:** {old} → {new} — {reason}
- ...

## What stayed

- {item} — kept as-is from concept

## Final approval

- {Approver name (if specified)}
- {YYYY-MM-DD}
```

## Schema for `decisions.md` (Stage 5 entry — append)

```markdown
## Stage 5: Refine & Export

- **Picked concept:** concept-{N}
- **Refinements applied:** {brief list}
- **Final saved to:** `final/final.md`
- **Decided at:** {YYYY-MM-DD HH:MM}
```

## What this stage does NOT do

- Does NOT produce final-print-ready PNG (V1 app does that via locked-template render). Phase 0 produces the **recipe**, not the **render**.
- Does NOT publish to Klaviyo / Vista Social / Resy. The recipe gets handed off.
- Does NOT save to a database. Files only.

## Retro prompt (after Stage 5)

If user agrees to a retro, ask these questions one at a time and save to `campaigns/{slug}/retro.md`:

1. Did the brief stage ask the right questions? (1-5, plus what was missing)
2. Did the style suggestion fit? (yes/no, plus why)
3. Did the asset suggestions fit? (yes/no, plus why) — this one matters a lot for Phase 0 since asset selection is manual
4. Were the concepts on-brand? Which concept was picked? Why? (free text)
5. What was refined and why? (free text)
6. What did you want that the workflow didn't support? (free text)
7. Did the workflow correctly use Ramsey's brand docs (system-prompt, voice, menu)? Or did it drift? (yes/no, examples)
8. Would you use this campaign output as-is? (yes / yes with edits / no)

Schema for `retro.md`:

```markdown
# Retro — {Campaign Name}

**Date:** {YYYY-MM-DD}
**Run by:** {user name or "Ramsey"}

## Brief stage
{answers}

## Style stage
{answers}

## Assets stage
{answers}

## Concepts stage
{answers}

## Refine stage
{answers}

## Brand context fidelity
{answers — did the workflow respect Ramsey's docs?}

## Friction / asks
{answers — what did you want that wasn't there?}

## Would post as-is?
{answer}
```
