# Uno Más Content Studio

HTML templates and design assets for Uno Más — organized for GitHub and [Lovable](https://lovable.dev) integration.

## What's in here

| Folder | Contents |
|--------|----------|
| `menus/` | Editable HTML menus (full, lunch, cocktail, brunch, editor) |
| `menus/print/` | Print-ready bifold/trifold layouts |
| `merch/` | Retail & merchandise designs (engraving library, line art) |
| `merch/previews/` | Campaign-specific merch previews |
| `website/templates/` | Full homepage themes (luz del día, día y noche, noche eléctrica) |
| `website/pages/` | Individual page components (Mezzanine, menu pages, reservations) |
| `email/` | Klaviyo email design system |
| `email/campaigns/` | Campaign emails (deal drop, loyalty, Mezzanine events, new item) |
| `email/flows/` | Automation flow emails (welcome series) |
| `campaigns/` | Dated campaign asset sets |
| `assets/logos/svg/` | SVG logos — all brand colors + stacked/horizontal variants |
| `assets/logos/flat/` | Flat logo variants |

## Approved templates (12)

All templates in the root folder structure are **approved for production use**.

See `manifest.json` for the full machine-readable index with metadata, tags, and Lovable integration hints.

## Needs revision (36 files)

These files exist in the source Marketing HQ folder but need updates before they're production-ready. See `manifest.json` → `needs_revision` for the full list.

## Lovable Integration

```js
// Fetch the manifest at build time
const manifest = await fetch(
  'https://raw.githubusercontent.com/[org]/uno-mas-content-studio/main/manifest.json'
).then(r => r.json());

// Load a specific template
const template = manifest.templates.find(t => t.id === 'menus/editor');
const html = await fetch(
  `https://raw.githubusercontent.com/[org]/uno-mas-content-studio/main/${template.path}`
).then(r => r.text());
```

Each template is a **self-contained HTML file** — all styles and scripts are inline. No external dependencies beyond Google Fonts.

## Brand

- **Primary green:** `#1a5c3a`
- **Magenta:** `#c0185c`
- **Orange:** `#d4550a`
- **Teal:** `#0e6b7c`
- **Yellow:** `#c49a00`
- **Fonts:** Antonio (headings), Montserrat (body), Dancing Script (accent)

## Source

All files sourced from `Uno Mas Marketing HQ / ` in Google Drive. Original files remain there; this repo contains approved/finalized copies.

Last reviewed: April 30, 2026
