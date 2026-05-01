# Flyer Portrait Vertical

Standard print/digital flyer template. Portrait, 4:5 aspect ratio.

## Format

- **Aspect ratio:** 4:5 (portrait)
- **Dimensions:** 1200×1500 px
- **Final export:** PNG or PDF
- **Platform:** Instagram story (vertical), printed flyer, table tent, email graphic

## Layout zones

```
┌─────────────────────────┐
│ [Logo top-left]         │
│ ┌─────────────────────┐ │
│ │  COLORED HEADER     │ │
│ │  HEADLINE           │ │
│ │  (auto-shrink)      │ │
│ └─────────────────────┘ │
│                         │
│  WHEN          HOW MUCH │
│  Date          $Price   │
│  Time                   │
│                         │
│      HERO IMAGE         │
│      (40% height)       │
│                         │
│  "Tagline / vibe line"  │
│                         │
│  CTA              footer│
└─────────────────────────┘
```

## Editable fields

- `headline` (text, max 50 chars, auto-shrinks)
- `date` (text, max 30 chars)
- `time` (text, max 20 chars)
- `price` (text, max 15 chars, auto-shrinks)
- `tagline` (text, max 80 chars): vibe line
- `cta` (text, max 25 chars)
- `heroAsset` (asset picker)
- `logoVariant` (asset picker)
- `accentColor` (brand color token, drives the colored header band)
- `disclaimer` (text, optional, auto-loaded from `_brand/disclaimers.md` or system-prompt when alcohol mentioned)

## Locked

- Typography: Antonio + Montserrat
- Color palette: brand tokens only
- Section structure (header band → when/how-much → hero → tagline → cta)

## Best for

- Cinco de Mayo flyer
- Holiday event flyers (Mother's Day Brunch, etc.)
- Specials of the week (printed table tent)
- Email header graphic
- Instagram story (use 9:16 variant when defined)

## Not great for

- Square Instagram feed → use instagram-square-bold
- Cocktail menu inserts → use a future menu-insert template
- Mezzanine event content → use a future Mezzanine-specific template

## Render reference

The auto-shrink behavior (`fitText` helper that computes font size from string length) is part of the locked template. A standalone POC demonstrates this rendering pipeline outside this repo — ask Scott for the link if you need to see it working.
