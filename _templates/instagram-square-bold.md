# Instagram Square Bold

The default Uno Más Instagram feed post template. Square 1:1.

## Format

- **Aspect ratio:** 1:1 (square)
- **Dimensions:** 1080×1080 px
- **Final export:** PNG or JPG
- **Platform:** Instagram feed, Facebook feed, generic social

## Layout zones

```
┌─────────────────────────────────┐
│ [Logo top-left, 15% width]      │
│                                 │
│      HERO IMAGE                 │
│      (food or drink, 60% area)  │
│                                 │
│  ┌──────────────────────────┐   │
│  │ HEADLINE (auto-shrink)   │   │
│  │ Subheadline + price/date │   │
│  └──────────────────────────┘   │
│                                 │
│  CTA bottom-right               │
└─────────────────────────────────┘
```

## Editable fields

- `headline` (text, max 50 chars, auto-shrinks): the main line
- `subheadline` (text, max 80 chars): supporting line ($X price, date, day part)
- `cta` (text, max 25 chars): action ("Reserve a table", "Walk in", "RSVP", "Your move")
- `heroAsset` (asset picker, food or drink photo)
- `logoVariant` (asset picker, logo only)
- `accentColor` (brand color token)

## Locked

- Typography: Antonio (headlines), Montserrat (body) per Uno Más design system
- Color palette: brand tokens only — no off-palette hex
- Layout zones: logo top-left, hero center, headline block bottom
- Logo placement and clear space

## Best for

- Bold Cantina Energy (default)
- Family Fiesta
- Street Taco Grit (with photo treatment = duotone)

## Not great for

- Premium Cocktail Lounge → use a Mezzanine-specific template (not yet defined)
- Information-dense posters → use flyer-portrait-vertical
- Vertical Instagram stories → use a 9:16 variant (not yet defined)

## Render reference

In the V1 app, this template will be a React component using `@vercel/og` with auto-shrink (font size computed from string length) and brand-token enforcement (palette restricted to brand hex codes only). A standalone POC of this rendering pipeline lives outside this repo — ask Scott for the link if you need to see it working.
