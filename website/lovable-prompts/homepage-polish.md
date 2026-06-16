# Lovable Prompt — Homepage Polish + Site-Wide Resy Fix (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Small targeted fixes on the homepage + a site-wide Resy link fix that affects every page. No design overhaul — the cream/pink direction is already correct.

---

## PASTE BELOW THIS LINE INTO LOVABLE

The homepage is already on the right visual direction (cream body, pink accents). Just need a handful of focused fixes. None of these should change the page's existing layout or visual style.

### Fix 1: Duplicate Resy button in homepage "Book a table" strip

On the homepage bottom strip (the row with "Hours today / Find us / Book a table"), the "Book a table" column currently renders the Resy reservation button **twice**, stacked. Markup currently looks like:

```
Book a table
[Reserve a table → Resy]
[Reserve at Resy → Resy]
```

Both buttons point to the same Resy URL. Remove the duplicate — keep only **one** Resy button in that column. Whichever component is rendering the Resy widget once is fine; just don't render it twice.

### Fix 2: Site-wide Resy link behavior — open in new tab + back path

This is a persistent UX bug on mobile. When a user taps any Resy link on the site, it currently navigates the same tab to resy.com — once they're there, they have no way back to unomastacoshop.com short of using the browser back button (which on iOS Safari often closes the page entirely if it was opened via app link).

Apply this to **every Resy link site-wide** (header, hero, mezzanine teaser, reservations page, /menu/dinner CTA, every "Book a table" / "Reserve a table" / "Reserve at Resy" instance):

```html
<a href="https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila"
   target="_blank"
   rel="noopener noreferrer">
   Reserve a table
</a>
```

Add `target="_blank"` + `rel="noopener noreferrer"` to all of them. This opens Resy in a new tab so the user's session on our site is preserved — they can close the Resy tab and they're right back where they started.

If you're using a component for the Resy button (e.g., `<ResyButton />`), update the component itself so this propagates everywhere.

### Fix 3: Homepage hero — add a light pink kicker above the headline

Currently the hero shows just the headline "GET A LITTLE LOST." and the subhead. Add a small kicker line ABOVE the headline:

- Text: "Modern Mexican · Spokane"
- Style: All caps, letter-spacing 2px, font-size 11-12px, color `#f4c0d1` (light brand pink — the Pink-100 stop from the palette)
- Spacing: 14-16px below the kicker, then the headline

This is a small accent that telegraphs the brand category before the headline lands. Match the same kicker pattern used on the menu pages.

### Fix 4: Homepage hero — fallback CTA label consistency

Currently the secondary CTA on the homepage hero says "See the menu" — change to "See The Menu" (title case, capital T) so it matches the formatting of other CTAs on the site like "Reserve A Table." Consistency thing.

### Fix 5: Testimonials section — tighten the visual treatment

The "Spokane is talking." section currently shows two testimonials as plain blockquotes. Style them slightly better:
- Move the testimonials into a 2-column grid on desktop, 1 column on mobile
- Each testimonial card: subtle cream background `#fafaf7` with a 0.5px border `#e8e4d8`, padding 24px, border-radius var(--border-radius-lg)
- Add a large pink quote mark (the `"` character or Tabler icon `ti-quote`) in `#E22690` at the top-left of each card, ~32px, positioned absolutely or as a decorative element
- Attribution line ("— Top organic post (1,449 likes, 76K views)") in Montserrat italic, gray `#6b6b6b`, ~12-13px

### Fix 6: Cantina Club teaser band (NEW — add this section)

Add a new band between the testimonials section and the Mezzanine teaser. Cream `#fafaf7` background, centered content, generous padding (~60px vertical).

- Kicker (light pink `#E22690`, small caps): "The Cantina Club"
- Headline (Antonio Bold, ~36px, `#1a1a1a`, all caps): "JOIN THE CLUB. EAT BETTER, MORE OFTEN."
- Subhead (Montserrat, ~15px, `#4a4a4a`, max-width 540px centered): "Members spend 107% more than non-members because they get it. Loyalty rewards, exclusive drops, first dibs on Mezzanine events. Sign up at the bar — or get on the list."
- Inline email signup form: email input + "Get On The List" button (pink `#E22690` background, white text). Submit goes to Klaviyo list ID `TcwW8y` (Uno Mas - Marketing Opt In) if Klaviyo is wired up; otherwise mailto fallback.

If Klaviyo onsite tracking pixel isn't installed yet on this site, also include it in the `<head>`:

```html
<script async type="text/javascript"
  src="https://static.klaviyo.com/onsite/js/UjAfaJ/klaviyo.js">
</script>
```

This enables future Klaviyo features (forms, segments, abandonment tracking).

### Out of scope (do NOT change)

- The hero photo, headline, or subhead copy
- The three-venues section (it's good)
- The dinner feature section (it's good)
- The Mezzanine teaser section (it's good)
- The footer (it's good)
- The header / nav (it's good)
- Any other pages — this prompt is homepage-only except for the site-wide Resy `target="_blank"` change

### Acceptance criteria

After this build:
- Homepage "Book a table" column shows exactly ONE Resy button, not two
- Every Resy link on every page opens in a new tab (target="_blank") with rel="noopener noreferrer"
- Homepage hero has a small pink kicker "Modern Mexican · Spokane" above the headline
- Homepage hero secondary CTA says "See The Menu" (title case)
- Testimonials are in 2-column card grid with pink quote marks (or 1-column on mobile)
- New Cantina Club teaser band appears between testimonials and Mezzanine teaser, with Klaviyo signup form
- Klaviyo onsite tracking pixel loads in `<head>` site-wide
- No other layout or copy changes

If anything is ambiguous, default to the lighter / less-busy option. The homepage should feel like a confident invitation, not a sales pitch.
