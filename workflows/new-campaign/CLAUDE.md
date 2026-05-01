# Workflow: New Campaign

The Phase 0 campaign generation workflow. Run by Ramsey + 1-2 staff via Claude Code to validate the campaign workflow before V1 app build.

## When to use this

The user typed something like:
- "I want to start a new campaign"
- "Help me make a Cinco de Mayo flyer"
- "Build a campaign for Sunday Brunch"
- "Create a Mezzanine event promo"

If the user is asking about brand voice, asset rules, or styles in isolation, you do NOT start this workflow — answer using the relevant Ramsey doc directly (`brand-intelligence-center/system-prompt.md` is the master entry point).

## Stages

| # | Stage | File | What happens |
|---|---|---|---|
| 1 | Brief | `stages/01-brief.md` | Ask intake questions, save `brief.md` |
| 2 | Style | `stages/02-pick-style.md` | Recommend 2 styles, user picks |
| 3 | Assets | `stages/03-pick-assets.md` | Recommend assets, user confirms |
| 4 | Concepts | `stages/04-generate-concepts.md` | Generate 3-4 concept variations |
| 5 | Refine & Export | `stages/05-refine-export.md` | Pick + tweak, save final |

Run them in order. After each stage, ask the user to confirm before moving to the next.

## Always-load brand context

Every stage that produces or references brand decisions should load:

- `brand-intelligence-center/system-prompt.md` — Ramsey's master brand brief

For specific stages, additionally load:

| Stage | Also load |
|---|---|
| 1 (Brief) | `marketing-knowledge/knowledge-center/AUDIENCE_PERSONAS.md` (if user is unsure of audience) |
| 2 (Style) | All `_styles/*.md` files |
| 3 (Assets) | `marketing-knowledge/brand-assets/BRAND_ASSETS.md` |
| 4 (Concepts) | `marketing-knowledge/knowledge-center/MENU_AND_OFFERS.md` (when food/drink mentioned), `marketing-knowledge/knowledge-center/UnoMas_CopyBank_April2026.md` (for example lines), `marketing-knowledge/brand-assets/CLAUDE_DESIGN_SYSTEM_BRIEF.md` (for visual decisions), the chosen `_styles/{style-slug}.md` |
| 5 (Refine) | Same as Stage 4 |

DO NOT load all brand docs at once. Match information to step scope.

## Campaign folder convention

When Stage 1 starts, create:

```
campaigns/{YYYY-MM}-{kebab-case-slug}/
```

Per Ramsey's existing repo convention (he already uses `campaigns/YYYY-MM-campaign-slug/` per the README). Inside this folder, each stage saves outputs:

```
campaigns/2026-05-cinco-de-mayo/
├── brief.md           ← Stage 1
├── decisions.md       ← Stages 2, 3, 5 append
├── concepts/
│   ├── concept-1.md   ← Stage 4
│   ├── concept-1.png  ← Stage 4 optional via Nano Banana
│   ├── concept-2.md
│   └── ...
├── final/
│   ├── final.md       ← Stage 5
│   ├── final.png      ← Stage 5 optional
│   └── notes.md       ← Stage 5
└── retro.md           ← After Stage 5, optional
```

Per Ramsey's convention, Stage 5's final output also gets surfaced into existing `campaigns/{slug}/copy/` and `campaigns/{slug}/briefs/` subfolders if Ramsey wants channel-specific copy split out — but Phase 0 default is everything inside the campaign folder using the schema above.

## Shared prompt fragments

Common snippets (voice rules, fabrication rules, output schema templates) live in `shared/prompt-fragments.md`. Each stage references them — load on demand.

## What this workflow does NOT produce

- Final-print-ready PNGs (concepts are descriptions + optional Nano Banana visuals; the locked-template render is V1 app territory)
- Database records (everything is files for Phase 0)
- Multi-channel deployment (this produces a recipe; Klaviyo/Vista Social/Resy integration happens in V1+)

## After the workflow

Optionally run `retro the last campaign` to capture what worked. Retros aggregate into the V1 app spec input.

## Smoke test reference

A working example campaign lives at `campaigns/2026-04-30-smoke-test-cinco-de-mayo/` (created during Phase 0 setup). Reference it when teaching someone the workflow.
