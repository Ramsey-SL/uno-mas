# Lovable Prompt — Mezzanine page cleanup (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-28
**Scope:** Three small fixes on the /mezzanine page + render the new "kicker" field that's now in Supabase site_content.

---

## PASTE BELOW THIS LINE INTO LOVABLE

Three targeted fixes on the `/mezzanine` page only. No other pages should change.

### Fix 1: Remove duplicate logo from the /mezzanine hero

The site header already renders the Uno Más logo at the top of every page. The /mezzanine hero band currently ALSO renders a logo (added in an earlier prompt as a "Mezzanine wordmark / logo at top of the hero"). It's redundant — the header logo above the hero is doing the work.

**Remove the logo overlay from inside the /mezzanine hero band component.** The header logo stays. The hero should now contain only:
- Kicker text (new — see Fix 2)
- Headline
- Subhead
- Primary CTA button

### Fix 2: Render the new `kicker` field on hero + teaser blocks

The `site_content` table now includes a `kicker` field on two blocks:
- `page_slug='/'` + `block_key='mezzanine-teaser'`
- `page_slug='/mezzanine'` + `block_key='hero'`

Both blocks now have content shaped like:
```json
{
  "kicker": "The Mezzanine on Monroe",
  "headline": "...",
  "subhead": "..." (or "body" for the teaser),
  "cta_primary_label": "..." (or "cta_label" for the teaser),
  "cta_primary_url": "..." (or "cta_url" for the teaser),
  "image_tag": "role:hero-mezzanine"
}
```

Update the hero band component and the homepage mezzanine teaser component to render the `kicker` field. Style:

- Position: above the headline
- Font: DIN Condensed VF (or Oswald fallback) — same family as headline, just much smaller
- Size: 11-13px desktop, 10-11px mobile
- Color: Electric Pink `#E22790` (NOT Uno Más main brand pink `#E22690` — this is the sub-brand variant — slight hex difference is intentional)
- Letter-spacing: 2.5-3px (small caps feel)
- Transform: uppercase
- Margin-bottom: 14-16px (separating from the headline)
- Weight: 500

If the `kicker` field is missing or empty, the component should NOT render an empty space — the kicker is optional.

### Fix 3: Update /mezzanine page metadata to reflect "The Mezzanine on Monroe"

Update the page-level metadata for `/mezzanine`:

- `<title>` tag → `"The Mezzanine on Monroe — Spokane's Speakeasy & Private Event Venue"`
- `meta description` → `"The escape you didn't know existed, until you did. The Mezzanine on Monroe — speakeasy and private event venue above Uno Más in Spokane. Private dinners, cocktail receptions, watch parties, full buyouts."`
- `<meta property="og:title">` → `"The Mezzanine on Monroe"`
- `<meta property="og:description">` → same as meta description above

If the page already has these set, replace them. Don't touch any other page's metadata.

### Out of scope (do NOT change)

- Hero image / background gradient on the /mezzanine page — that's correct as-is
- Other content blocks on /mezzanine (event-type cards, etc.) — only the hero block changes
- Any other page (`/`, `/menu/*`, `/about`, `/contact`, `/private-events`) — except the homepage mezzanine teaser block which now also has the new kicker field to render

### Acceptance criteria

After this build:
- `/mezzanine` hero band shows: small pink kicker "The Mezzanine on Monroe" → big headline "UPSTAIRS AT UNO MÁS, A QUIETER STORY." → subhead → "Email Karissa" CTA. **NO logo inside the hero band.** Site header logo is the only logo visible above the fold.
- Homepage mezzanine-teaser section shows the new kicker + headline + body + "Find the stairs" CTA.
- `/mezzanine` page source has the new `<title>` and meta tags.
- No other pages changed.
