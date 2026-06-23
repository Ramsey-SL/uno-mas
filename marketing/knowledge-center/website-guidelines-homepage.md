# Uno Más Tacos & Tequila — Website Redesign Guidelines (Homepage)

*Last updated: April 23, 2026 — aligned to Uno Más Brand Guide 2024*
*Source of truth: `Brand_Guidelines/UnoMas/Uno_Mas_Brand_Guide_2024_CURRENT.pdf`*

## Project Overview

Full redesign of unomastacoshop.com. The current site needs a modern overhaul that matches the energy of the brand — bold, confident, community-rooted, and self-aware. This document defines the homepage structure, visual direction, and content guidelines to generate an accurate mockup.

---

## Brand Identity Summary

**Brand Name:** Uno Más Tacos & Tequila (commonly "Uno Más")
**Primary Tagline:** "Get a little lost at Uno Más."
**Brand Personality:** Confident, playful, self-aware, community-driven, just a little chaotic. Not corporate. Not chain. The friend who always knows where to go.
**Location:** 2020 N Monroe St, Suite C, Spokane WA 99201

### Sub-Brand
**The Mezzanine** — Speakeasy and private event venue upstairs at Monroe. Separate visual identity (dark, electric pink/magenta/ultra violet palette) but connected to Uno Más.

---

## Color Palette

> **Source of truth:** `Brand_Guidelines/UnoMas/Uno_Mas_Brand_Guide_2024_CURRENT.pdf`

### Uno Más — Primary Colors

| Role | Color Name | Hex | Usage |
|------|-----------|-----|-------|
| Primary Ink / Dark BG | Navy | `#003366` | Headers, nav, footer, primary text, dark backgrounds |
| Primary CTA / Headline | Blue | `#18BCDC` | CTAs, links, headline accents |
| Bright Accent | Teal | `#27F3DE` | Agave icon highlight, logo typography accent |
| Secondary Digital Accent | Green | `#25E9B9` | Complementary digital accents |
| Hero / Brand Color | Pink | `#E22690` | Primary brand color — logo, hero highlights, key CTAs |
| Energy / Callout | Yellow | `#FFEC00` | Badges, energy moments, pops |

### Uno Más — Neutrals

| Role | Color Name | Hex | Usage |
|------|-----------|-----|-------|
| Body Text | Dark Grey | `#212121` | Body copy on light backgrounds |
| Dividers / Muted | Light Grey | `#BFBFBF` | Dividers, secondary info, disabled states |
| Warm Background | Sand / Tan | `#E8DECE` | Section alternating backgrounds, menu feel |
| Page Background | White | `#FFFFFF` | Primary page background |
| Absolute Dark | Black | `#000000` | Print, absolute dark UI |

### The Mezzanine — Sub-Brand Colors (use ONLY for Mezzanine content)

| Role | Color Name | Hex | Usage |
|------|-----------|-----|-------|
| Primary Brand | Electric Pink | `#E22790` | Primary Mezzanine color, key CTAs |
| Secondary Accent | Magenta | `#BF28BF` | Secondary accents |
| Deep Accent | Ultra Violet | `#93009B` | Dark accent, moody depth |
| Dark Background | Charcoal | `#333333` | Dark UI elements |
| Primary Background | Black | `#000000` | Primary Mezzanine background |

> ⚠️ **NEVER mix Uno Más and Mezzanine brand colors in the same design.** Never use Uno Más Pink (`#E22690`) with Mezzanine typography, or vice versa.

---

## Typography

> **Source of truth:** `Brand_Guidelines/UnoMas/Uno_Mas_Brand_Guide_2024_CURRENT.pdf`, Section 07 — Fonts

### Uno Más

| Role | Font | Fallback | Weight / Notes |
|------|------|----------|--------|
| Decorative / Accent | Thirsty Rough | cursive | Sparingly — never near the logo, never as the primary headline |
| Headlines / Display | Antonio | Impact, sans-serif | Bold for hero; Regular for section headers |
| Body / UI / Nav | Montserrat | -apple-system, sans-serif | Thin through Extra-Bold — use weight range for hierarchy |

### The Mezzanine

| Role | Font | Notes |
|------|------|-------|
| Titles / Display | DIN Condensed VF | All Mezzanine headlines |
| Body / UI | Poppins | Descriptions, labels |
| Decorative Callouts | Baka Too | Signature accent moments |

> ⚠️ **Never use Antonio or Thirsty Rough on Mezzanine content. Never use DIN Condensed, Poppins, or Baka Too on Uno Más content.**

Font files located in: `01_Brand_Assets/Fonts/`

---

## Homepage Structure (Top to Bottom)

### 1. Navigation Bar
- **Style:** Sticky, transparent on hero → solid dark navy on scroll
- **Logo:** Left-aligned Uno Más logo (horizontal variant, taco shop tagline)
- **Nav Items:** Menu | Locations | Catering | Events | The Mezzanine | About
- **CTA Button:** "Order Now" (teal background, white text, slight rounded corners)
- **Mobile:** Hamburger menu with full-screen overlay

### 2. Hero Section
- **Layout:** Full-width, full-viewport-height image/video background
- **Content:** Bold headline in Antonio Bold, body in Montserrat, two CTA buttons
- **Headline Example:** "GET A LITTLE LOST."
- **Sub-headline:** "Modern Mexican. Craft cocktails. A speakeasy upstairs. 2020 N Monroe, Spokane."
- **Primary CTA:** "Make a Reservation" (Pink `#E22690` button)
- **Secondary CTA:** "See the Menu" (ghost/outlined button, white border)
- **Background:** High-energy photo — patio scene, food close-up, or crowd shot. Slight dark overlay (40-50% opacity) for text readability.
- **Motion:** Subtle parallax scroll or slow Ken Burns effect on the background image

### 3. Quick-Hit Value Strip
- **Layout:** Horizontal strip with 3-4 icons + short text
- **Items:** "Quarter-Pound Tacos" | "House-Smoked Meats" | "Craft Cocktails" | "Private Events"
- **Style:** Navy `#003366` background, white text, Blue `#18BCDC` or Teal `#27F3DE` icons (line-art style using existing UM icon set)

### 4. Menu Highlights / Featured Items
- **Layout:** 3-4 card grid with food photography
- **Content:** Top menu items with photo, name, brief description, price
- **Categories to Feature:** Signature Tacos, Margaritas/Tequila, Fiesta Packs (catering)
- **CTA:** "See Full Menu" button below the grid
- **Style:** Cards with subtle shadow, warm cream background, slight hover lift animation
- **Photography:** Use professional food shots from `02_PHOTO_LIBRARY/UnoMas_Brand/food/`

### 5. Location / Hours
- **Layout:** Single location card or split layout with map
- **Card content:**
  - 2020 N Monroe St, Suite C, Spokane WA 99201
  - Hours: Tue–Thu 11am–9pm · Fri–Sat 11am–10pm · Sun Closed (brunch ON HOLD — relaunch TBD)
  - Phone: (509) 960-7989
  - "Get Directions" link
  - "Make a Reservation" CTA → Resy
- **Style:** Clean card on Sand `#E8DECE` background section
- **Map Option:** Embedded map with custom Uno Más pin (use agave icon from `01_Brand_Assets/Logos/Icons/`)

### 6. The Mezzanine Callout
- **Layout:** Split section — large atmospheric dark photo on one side, text on the other
- **Headline:** "THE MEZZANINE" in DIN Condensed VF (Mezzanine brand font)
- **Body:** Brief description — speakeasy upstairs, leather lounges, fireplace, private events, 28 seated capacity
- **CTA:** "Inquire About Your Event" → karissa@unomastacoshop.com (Electric Pink `#E22790` button)
- **Style:** Dark section using Mezzanine palette — Black/Charcoal backgrounds, Electric Pink accents. Watercolor textures are an approved design element for Mezzanine content. Never mix Uno Más main brand colors in this section.
- **Photo:** Mezzanine interior shot from `02_PHOTO_LIBRARY/Mezzanine_Brand/`

### 7. Social Proof / Community Section
- **Layout:** Instagram feed embed or curated photo grid + testimonial quotes
- **Content:** Pull from real Google/Yelp reviews + Instagram content
- **Style:** Masonry-style photo grid with overlay quotes
- **CTA:** "Follow Us @unomastacoshop" linking to Instagram

### 8. Catering / Fiesta Packs
- **Layout:** Full-width banner or split section
- **Headline:** "BRING UNO MÁS TO YOUR NEXT EVENT"
- **Body:** Quick pitch for catering — fiesta packs, office lunches, party trays [VERIFY: confirm current catering offerings are active]
- **CTA:** "Get In Touch" → karissa@unomastacoshop.com (Pink `#E22690` button)
- **Background:** Photo of fiesta pack or catering spread

### 9. Email / Loyalty Signup — The Cantina Club
- **Layout:** Centered section with email input field
- **Headline:** "JOIN THE CANTINA CLUB"
- **Body:** "Get exclusive deals, early access, and earn rewards. Cantina Club members spend 107% more — because they know better."
- **Input:** Email/phone field + "Sign Up" button
- **Style:** Navy `#003366` background section, Pink `#E22690` CTA button
- **Integration:** Klaviyo email + SMS capture (connected to Toast loyalty data)
- **Loyalty program name:** Uno Más Rewards: The Cantina Club

### 10. Footer
- **Layout:** Four-column layout
- **Column 1:** Logo + brief brand description
- **Column 2:** Quick links (Menu, Locations, Catering, Events, About, Careers)
- **Column 3:** Contact info (phone, email, general inquiries)
- **Column 4:** Social media icons (Instagram, Facebook, TikTok) + hours summary
- **Bottom Bar:** Copyright, privacy policy, accessibility statement
- **Style:** Navy `#003366` background, white/light text, Blue `#18BCDC` link accents

---

## Visual Design Principles

1. **Bold, Not Busy** — Big type, strong color blocks, generous whitespace. Let the food and venue photography do the heavy lifting.

2. **Photography-Forward** — Every section should have real Uno Más photography. No stock photos. The brand asset library has thousands of shots organized by category.

3. **Mobile-First** — Over 70% of restaurant traffic is mobile. The design must be exceptional on phone screens — large tap targets, easy-to-read menus, one-thumb ordering.

4. **Speed Over Flash** — Restaurant sites need to load fast. Optimize images, minimize animations, prioritize Core Web Vitals. No heavy JavaScript frameworks that slow first paint.

5. **Clear Conversion Paths** — Every section should funnel toward one of three actions: View Menu, Order Online, or Book an Event. CTAs should be obvious and persistent.

6. **Authenticity** — The site should feel like walking into Uno Más. Warm, fun, a little loud (visually), unpretentious. Avoid anything that feels corporate, templated, or generic.

---

## Technical Notes

- **Current Domain:** unomastacoshop.com
- **Platform:** Squarespace (migrating — in progress)
- **Reservations:** Resy — resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila
- **POS / Ordering:** Toast [VERIFY: confirm current online ordering status]
- **Email/SMS Platform:** Klaviyo — signup forms should integrate directly
- **Social Scheduling:** Vista Social — embed Instagram feed if possible
- **Loyalty Program:** Uno Más Rewards: The Cantina Club (via Toast + Klaviyo) — surface in nav or hero
- **Instagram:** @unomastacoshop | **TikTok:** @unomastacosandtequila
- **Events Contact:** karissa@unomastacoshop.com | **General:** tacos@unomastacoshop.com
- **Phone:** (509) 960-7989
- **SEO Priority:** "taco restaurant spokane", "taco bar spokane", "taco tuesday spokane", "private event venue spokane", "speakeasy spokane"
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
| Brand Guidelines PDF | `01_Brand_Assets/Brand_Guidelines/UnoMas/Uno_Mas_Brand_Guide_2024_CURRENT.pdf` |
| Current Menus | `Operations/Menu/` |

---

## Competitive Reference

The site should outclass typical local restaurant websites (which are usually template Squarespace/Wix sites) while feeling distinctly Spokane — not trying to be an LA or NYC brand. Think the energy of a Torchy's Tacos or Velvet Taco web presence but with Pacific Northwest warmth and Uno Más's specific community-rooted personality.

---

*Last updated: April 23, 2026 — aligned to Uno Más Brand Guide 2024*
*For mockup generation — pair this document with brand photography and `01_Brand_Assets/Brand_Guidelines/UnoMas/Uno_Mas_Brand_Guide_2024_CURRENT.pdf`.*
*Full design system brief: `01_Brand_Assets/CLAUDE_DESIGN_SYSTEM_BRIEF.md`*
