# Stage 4 — Generate Concepts

## Goal

Produce 3-4 distinct concept variations grounded in the brief, chosen style, and selected assets. Each concept = a parameter set (copy + layout + asset choices) plus optionally a Nano Banana visual.

## What to load before this stage

- `campaigns/{slug}/brief.md`
- `campaigns/{slug}/decisions.md`
- The chosen `_styles/{style-slug}.md`
- `brand-intelligence-center/system-prompt.md` (master brand context)
- `marketing-knowledge/knowledge-center/UnoMas_CopyBank_April2026.md` (example lines by channel — STRONG reference for tone)
- `marketing-knowledge/knowledge-center/MENU_AND_OFFERS.md` (when food/drink mentioned)
- `marketing-knowledge/brand-assets/CLAUDE_DESIGN_SYSTEM_BRIEF.md` (visual rules — if generating Nano Banana visuals)
- The chosen template if specified: `_templates/{template-slug}.md`
- `workflows/new-campaign/shared/prompt-fragments.md`

## Steps

1. Generate 3-4 concept parameter sets with these axes of variation:
   - **Tone variant:** vary among {bold/loud, refined/premium, playful/casual, clean/minimal} — pick which 3-4 fit the chosen style
   - **Copy:** unique headline, subheadline, CTA, caption per concept (consult `UnoMas_CopyBank_April2026.md` for tone reference)
   - **Asset choice:** assign each concept a different primary photo from the picked pool
   - **Layout direction:** hero-dominant / headline-dominant / split / minimal — pick 3-4 different per concept
   - **Section toggles:** does this concept include the disclaimer? menu items? RSVP CTA?
2. For each concept, save `campaigns/{slug}/concepts/concept-{N}.md` with the parameter set.
3. Optionally call Nano Banana via MCP to generate `concept-{N}.png` for visual reference.
4. Present all concepts to the user with side-by-side summary.
5. Ask: "Which concept feels closest? (Or do you want to regenerate any?)"
6. Save the user's pick to `decisions.md`.
7. Ask: "Ready for Stage 5 (refine and export)?"

## Concept parameter schema

```markdown
# Concept {N} — {Tone Variant Name}

## Parameter set

- **Tone:** {bold / refined / playful / clean}
- **Layout:** {hero-dominant / headline-dominant / split / minimal}
- **Primary asset:** {asset description / URL from decisions}
- **Logo:** {logo from decisions}
- **Sections included:** {comma-separated: headline, subheadline, price, date, time, cta, disclaimer, menu-items}
- **Accent color:** {brand color hex}

## Copy

- **Headline:** {≤50 chars}
- **Subheadline:** {≤80 chars, often price + date or daypart}
- **CTA:** {≤25 chars, action verb — examples from CopyBank: "Reserve a table" / "Walk in" / "Your move" / "RSVP" / "Book the night"}
- **Caption** (Instagram only): {≤200 chars, emoji rules per chosen style/daypart from system-prompt}
- **Disclaimer:** {if alcohol mentioned: "21+ to consume alcohol." if happy hour: "Happy hour: dine-in only."}

## Reasoning

{1-2 sentences explaining why this combination of choices fits the brief and chosen style. Reference Ramsey's voice register if relevant.}

## Visual reference

> Generated via Nano Banana for direction-finding only. NOT a final render. Final render happens in V1 app via locked-template pipeline.

`concept-{N}.png`
```

## Nano Banana invocation

When generating visual references, compose the prompt as:

1. Style hidden prompt (from `_styles/{style-slug}.md`)
2. Brand context: pull from `system-prompt.md` — colors (per chosen style), typography (Antonio + Montserrat for main brand, DIN Condensed + Poppins for Mezzanine), tagline ("Get a little lost.")
3. Brief context: campaign name, key offer, audience, daypart
4. Concept-specific direction: tone, layout, asset description
5. Hard rules: render headline EXACTLY as `{headline}`, render subheadline EXACTLY as `{subheadline}`, no fabricated URLs, no fabricated prices

Call:

```
mcp__nano-banana-2__generate_image with:
  prompt: <composed prompt>
  aspectRatio: matched to template (1:1 / 4:5 / 9:16)
  resolution: "2K"
  thinking: "high"
```

Save the returned PNG to `campaigns/{slug}/concepts/concept-{N}.png`.

## Hard rules (per Ramsey's docs)

- Every concept must respect the never-say list from `system-prompt.md`. NO "authentic," "mouthwatering," "artisanal," "mixology," "vibrant," "amazing," "leverage," "utilize," "perfect for any occasion."
- Every concept must use only menu items from `MENU_AND_OFFERS.md`. If asked about a non-menu item, escalate to user.
- If brief uses `[ADD PRICE]` or `[ADD DATE]`, leave them as placeholders. Do not guess.
- No concept may include URLs unless explicitly given in the brief. Common Uno Más URLs (use only when relevant and explicit):
  - `unomastacoshop.com`
  - `resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila`
  - `karissa@unomastacoshop.com` (private events / catering)
- Logo placement is per template spec; do not move it.
- Color choices are limited to the palette from the chosen style's color notes.
- Mezzanine content uses Mezzanine palette + typography ONLY. Never mix.
- Use vocabulary substitutions per `system-prompt.md`:
  - "Modern Mexican" not "authentic Mexican"
  - "House-smoked" not "artisanal"
  - "Get a little lost" not "discover/explore"
  - "Craft cocktails" not "mixology"
  - "Your move" / "Make good choices" instead of generic CTAs

## Common issues

- **Nano Banana fabricates a URL or invents text.** Re-run with explicit "no URLs, no logos other than {logo description}, no fabricated text" in prompt. If persists, fall back to text-only concept.
- **Concepts are too similar.** Force more variation across the 4 axes. Each concept should be visibly different in tone OR layout OR asset.
- **User wants to skip Nano Banana visuals.** Fine. Concepts are still parameter sets in markdown.
- **Concept includes off-menu items or banned phrases.** Re-generate with explicit constraint reminder.
- **Concept uses Uno Más palette for Mezzanine venue (or vice versa).** Brand separation violation per Ramsey's rules. Re-generate.
