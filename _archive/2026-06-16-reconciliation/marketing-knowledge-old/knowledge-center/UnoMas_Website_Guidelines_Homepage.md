# Uno Mas Taco Shop — Website Redesign Guidelines (Homepage)

## Project Overview

Full redesign of unomastacos.com. The current site needs a modern overhaul that matches the energy of the brand — bold, fun, community-rooted, and unapologetically vibrant. This document defines the homepage structure, visual direction, and content guidelines to generate an accurate mockup.

---

## Brand Identity Summary

**Brand Name:** Uno Mas Tacos & Tequila (commonly "Uno Mas" or "Uno Más")
**Tagline Options:** "One More" | "Always Room for One More" | "Spokane's Taco Shop"
**Brand Personality:** Fun, bold, community-driven, locally rooted, unpretentious, vibrant. Not corporate. Not chain. The friend who always knows where to eat.
**Locations:** Wonder Building (Downtown Spokane), South Valley, Monroe Street

### Sub-Brand
**The Mezzanine** — Private event venue located above the Wonder Building location. Separate visual identity (watercolor aesthetic, electric pink/magenta palette) but connected to Uno Mas.

---

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary Dark | Deep Navy / Dark Blue | #1B2A4A | Headers, nav, footer, primary text |
| Primary Accent | Vibrant Teal | #00B4D8 | CTAs, links, highlights |
| Secondary Accent | Warm Orange | #F77F00 | Badges, specials callouts, hover states |
| Tertiary Accent | Magenta/Hot Pink | #E91E8C | Mezzanine references, event callouts |
| Background | Off-White / Warm Cream | #FAF8F5 | Page background |
| Background Alt | Light Sand | #F0EDE6 | Section alternating backgrounds |
| Text Primary | Near Black | #1A1A1A | Body copy |
| Text Secondary | Warm Gray | #6B6B6B | Captions, secondary info |
| Success/Fresh | Avocado Green | #4CAF50 | Fresh indicators, confirmation states |

> **Note:** These are approximations based on brand materials. Verify against the official brand guide PDF in `Brand-Intelligence-Claude/brand-intelligence-center/Uno-Mas-Brand-Guide-2024.pdf`.

---

## Typography

| Role | Font | Fallback | Weight |
|------|------|----------|--------|
| Display / Hero | Martellas Caps | Impact, sans-serif | Regular |
| Headlines (H1-H3) | Palmer Lake Print | Georgia, serif | Regular |
| Sub-headlines | Narrabeen | Helvetica, sans-serif | Regular |
| Body Copy | Cordoba Sans | -apple-system, sans-serif | Regular / Bold |
| Accent / Callouts | Santos | cursive | Regular |
| UI / Navigation | Nersans Two | Inter, sans-serif | Regular |

Font files located in: `01_Brand_Assets/Fonts/`

---

## Homepage Structure (Top to Bottom)

### 1. Navigation Bar
- **Style:** Sticky, transparent on hero → solid dark navy on scroll
- **Logo:** Left-aligned Uno Mas logo (horizontal variant, taco shop tagline)
- **Nav Items:** Menu | Locations | Catering | Events | The Mezzanine | About
- **CTA Button:** "Order Now" (teal background, white text, slight rounded corners)
- **Mobile:** Hamburger menu with full-screen overlay

### 2. Hero Section
- **Layout:** Full-width, full-viewport-height image/video background
- **Content:** Bold headline in Martellas Caps, subheadline in Narrabeen, two CTA buttons
- **Headline Example:** "ALWAYS ROOM FOR ONE MORE"
- **Sub-headline:** "Spokane's favorite tacos, tequila, and good times — three locations strong."
- **Primary CTA:** "View Our Menu" (teal button)
- **Secondary CTA:** "Order Online" (outlined/ghost button, white border)
- **Background:** High-energy photo — patio scene, food close-up, or crowd shot. Slight dark overlay (40-50% opacity) for text readability.
- **Motion:** Subtle parallax scroll or slow Ken Burns effect on the background image

### 3. Quick-Hit Value Strip
- **Layout:** Horizontal strip with 3-4 icons + short text
- **Items:** "Scratch-Made Daily" | "3 Locations" | "Catering Available" | "Private Events"
- **Style:** Dark navy background, white text, teal icons (line-art style using existing UM icon set)

### 4. Menu Highlights / Featured Items
- **Layout:** 3-4 card grid with food photography
- **Content:** Top menu items with photo, name, brief description, price
- **Categories to Feature:** Signature Tacos, Margaritas/Tequila, Fiesta Packs (catering)
- **CTA:** "See Full Menu" button below the grid
- **Style:** Cards with subtle shadow, warm cream background, slight hover lift animation
- **Photography:** Use professional food shots from `02_PHOTO_LIBRARY/UnoMas_Brand/food/`

### 5. Location Finder
- **Layout:** Three-column layout (one per location) or interactive map
- **Each Location Card:**
  - Location name (Wonder Building, South Valley, Monroe)
  - Address
  - Hours
  - Phone
  - "Get Directions" link
  - "Order from Here" CTA
  - Location-specific photo
- **Style:** Clean cards on alternating sand background section
- **Map Option:** Embedded map with custom Uno Mas pins (use location icons from `01_Brand_Assets/Logos/Icons/`)

### 6. The Mezzanine Callout
- **Layout:** Split section — large atmospheric photo on one side, text on the other
- **Headline:** "THE MEZZANINE" (in Mezzanine brand font/style)
- **Body:** Brief description of the private event space — rooftop vibes, capacity, what makes it unique
- **CTA:** "Book Your Event" (magenta/hot pink button to differentiate from Uno Mas teal CTAs)
- **Style:** This section should feel slightly elevated — the Mezzanine brand leans more sophisticated (watercolor textures, magenta palette) while still connected to Uno Mas
- **Photo:** Mezzanine interior/rooftop shot from `02_PHOTO_LIBRARY/Mezzanine_Brand/`

### 7. Social Proof / Community Section
- **Layout:** Instagram feed embed or curated photo grid + testimonial quotes
- **Content:** Pull from real Google/Yelp reviews + Instagram content
- **Style:** Masonry-style photo grid with overlay quotes
- **CTA:** "Follow Us @unomastacos" linking to Instagram

### 8. Catering / Fiesta Packs
- **Layout:** Full-width banner or split section
- **Headline:** "BRING UNO MAS TO YOUR NEXT EVENT"
- **Body:** Quick pitch for catering — fiesta packs, office lunches, party trays
- **CTA:** "View Catering Menu" (orange accent button)
- **Background:** Photo of fiesta pack or catering spread

### 9. Email / Loyalty Signup
- **Layout:** Centered section with email input field
- **Headline:** "JOIN THE FAMILIA"
- **Body:** "Get exclusive deals, be the first to know about events, and earn rewards."
- **Input:** Email field + "Sign Up" button
- **Style:** Dark navy background section, teal CTA button
- **Integration:** Klaviyo email capture

### 10. Footer
- **Layout:** Four-column layout
- **Column 1:** Logo + brief brand description
- **Column 2:** Quick links (Menu, Locations, Catering, Events, About, Careers)
- **Column 3:** Contact info (phone, email, general inquiries)
- **Column 4:** Social media icons (Instagram, Facebook, TikTok) + hours summary
- **Bottom Bar:** Copyright, privacy policy, accessibility statement
- **Style:** Deep navy background, white/light text, teal link accents

---

## Visual Design Principles

1. **Bold, Not Busy** — Big type, strong color blocks, generous whitespace. Let the food and venue photography do the heavy lifting.

2. **Photography-Forward** — Every section should have real Uno Mas photography. No stock photos. The brand asset library has thousands of shots organized by category.

3. **Mobile-First** — Over 70% of restaurant traffic is mobile. The design must be exceptional on phone screens — large tap targets, easy-to-read menus, one-thumb ordering.

4. **Speed Over Flash** — Restaurant sites need to load fast. Optimize images, minimize animations, prioritize Core Web Vitals. No heavy JavaScript frameworks that slow first paint.

5. **Clear Conversion Paths** — Every section should funnel toward one of three actions: View Menu, Order Online, or Book an Event. CTAs should be obvious and persistent.

6. **Authenticity** — The site should feel like walking into Uno Mas. Warm, fun, a little loud (visually), unpretentious. Avoid anything that feels corporate, templated, or generic.

---

## Technical Notes

- **Current Domain:** unomastacos.com
- **Ordering Integration:** Square Online (current) — needs seamless embed or redirect
- **Email Platform:** Klaviyo — signup forms should integrate directly
- **Social Scheduling:** Vista Social — embed Instagram feed if possible
- **Loyalty Program:** Square Loyalty — surface rewards/signup in nav or hero
- **SEO Priority:** "tacos spokane", "best tacos spokane", "taco catering spokane", "private event venue spokane"
- **Accessibility:** WCAG 2.1 AA compliance minimum

---

## Asset References

| Asset Type | Location |
|-----------|----------|
| Logos (PNG/SVG/AI) | `01_Brand_Assets/Logos/UnoMas/` |
| Mezzanine Logos | `01_Brand_Assets/Logos/Mezzanine/` |
| Icons (Agave, Location, UI) | `01_Brand_Assets/Logos/Icons/` |
| Fonts | `01_Brand_Assets/Fonts/` |
| Food Photography | `02_PHOTO_LIBRARY/UnoMas_Brand/food/` |
| Venue/Patio Photography | `02_PHOTO_LIBRARY/UnoMas_Brand/venue/` |
| Drinks Photography | `02_PHOTO_LIBRARY/UnoMas_Brand/drinks/` |
| Team Photography | `02_PHOTO_LIBRARY/UnoMas_Brand/team/` |
| Event Photography | `02_PHOTO_LIBRARY/UnoMas_Brand/events/` |
| Mezzanine Photography | `02_PHOTO_LIBRARY/Mezzanine_Brand/` |
| Brand Guidelines PDF | `Brand-Intelligence-Claude/brand-intelligence-center/Uno-Mas-Brand-Guide-2024.pdf` |
| Current Menus | `Operations/Menu/` |

---

## Competitive Reference

The site should outclass typical local restaurant websites (which are usually template Squarespace/Wix sites) while feeling distinctly Spokane — not trying to be an LA or NYC brand. Think the energy of a Torchy's Tacos or Velvet Taco web presence but with Pacific Northwest warmth and Uno Mas's specific community-rooted personality.

---

*Last updated: April 6, 2026*
*For mockup generation — pair this document with brand photography and the official brand guide PDF.*
