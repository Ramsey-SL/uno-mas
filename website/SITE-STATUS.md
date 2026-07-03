# Uno Más Website — Site Status & Session Handoff
_Last updated: 2026-07-03 · maintained by the build assistant_

Pick-up doc for resuming the Uno Más marketing-site build (Lovable) in a new session / another device. Read this first.

---

## 1. Where the site lives
- **Live (Lovable hosting):** https://uno-mas-site-builder.lovable.app  ·  **status: PUBLISHED**
- **Lovable project id:** `78c4ac75-6325-4f38-a44b-278bb2194cf2`  ·  slug `uno-mas-site-builder`
- **Editor:** https://lovable.dev/projects/78c4ac75-6325-4f38-a44b-278bb2194cf2
- **Latest published commit:** `af5edf3b` (Love Island Finale homepage section + holiday closure announcement bar).
- **Stack:** TanStack Start (SSR) + Tailwind + shadcn/ui. Backend = Lovable Cloud / Supabase.
- **Production domain: CONNECTED ✅** — https://unomastacoshop.com is live; the lovable.app URL 302-redirects to it.

## 2. Connected infrastructure
- **Supabase project:** `coandmppuqqzcbbhcien` — menu content (menu_sections/menu_items) + **`event_inquiries`** lead table.
- **Cloudinary (DAM):** cloud `drxrfyq9i`. Videos use `c_fill,g_center`; images `c_fill,g_auto`; uniform menu grade `e_saturation:18,e_contrast:10,e_brightness:4`. Day-card line-art icons recolored via `e_make_transparent:45/e_colorize,co_rgb:<hex>`.
- **Resend (email):** `RESEND_API_KEY` is set as a **project secret** and live. Inquiry emails go to **karissa@unomastacoshop.com**. (Confirm `unomastacoshop.com` domain verification in Resend so it can send from `events@…`; otherwise default sender has limited delivery.)

## 3. How to work with this project (conventions that save pain)
- Edits go through the **Lovable `send_message`** agent. Always instruct **"typecheck only (`bunx tsgo --noEmit`), do NOT run Playwright/browser/screenshots"** — browser runs hit the ~300s idle timeout. For big changes use `wait:false` + poll `get_message`/`list_edits`.
- After edits, **`deploy_project`** to publish. Propagation ~15–40s.
- **Verify via curl** of the live HTML with `--compressed` + `grep -a` (raw curl can be gzip → grep sees binary). Poll on a *new, unique* marker (avoid strings that already exist elsewhere — many false positives otherwise).
- **Headless Chrome will NOT reliably paint** the SSR-React mid/lower sections or dialog/Suspense content for screenshots — verify structurally via curl/`--dump-dom`, and have the owner eyeball the live site.
- Local design mockups: `python3 -m http.server` in a scratch dir, screenshot with headless Chrome, slice with PIL. Used for all the "show me options" rounds.

## 4. What's built & live
**Homepage (`/`):** hero (tilted media tiles) → "What's on this week" (agave ticker, Love Island watch-party card, 3 day-deal cards) → Fiesta Box teaser → Venues intro → **VenueShowcase** (Cantina/Mezzanine/Patio, framed tiles, auto-rotate every 3s) → **MenuCollection** (`#menu`: Lunch/Dinner/Cocktails tabs, full Monroe menu, collection rail auto-rotates 3s) → social proof → MezzanineSplit → Visit/contact → footer. Section transitions (fade/slant/wave/hill/dissolve) between color-change seams.
- **Day-deal cards:** Big-day editorial; icons now use real DAM line-art — taco `TTAsset_2_4x_vv5mg9` (pink), pint `UM_-_Daily_Specials_-_June_2026_wtgpaz` (navy), burrito `Burrito_-_source_kn4mzk` (blue). Burrito icon enlarged to match the taco/pint icon sizing and mirrored horizontally. Deals: Taco Tuesday = **$6 margs** (matches CLAUDE.md), **Beer & Bites Wednesday** ($5 pints · $10 loaded nachos · $10 loaded masa fries), Burrito Thursday ($15 House Burrito or Bowl).
**Nav (`site-header.tsx`):** Menu (→`/#menu`) · Fiesta Boxes To Go · Catering · The Mezzanine · **Plan an Event** · About · Now Hiring + Reserve a table. Active link = pink. **Mobile = slide-in drawer** (shadcn Sheet, hamburger < 1100px).
**The Mezzanine (`/mezzanine`):** uses the main site chrome (PageShell), Scheme-D high-contrast (black + electric-pink), video hero + tilted tiles, RoomStats, EventTypes, WhatYouGet (6 items incl. TVs + karaoke), "Inside the Mezzanine" L4 feature+thumbnail rail, mezzanine-colored footer. Inquire buttons → form popup.
**Plan an Event (`/private-events`):** rebranded to navy/cream/pink + transitions; "Four Ways to Celebrate" = **Design A** (full-bleed photo + gradient + pink pill + Inquire popup).
**Fiesta Box (`/fiesta-box`), Catering (`/catering`, Toast lead form), Now Hiring (`/now-hiring`, Google form), About (`/about`).** `/reservations` 301→Resy (removed). `/menu` 301→`/#menu`.
**Inquiry system:** `InquireDialog` opens the form directly → saves to `event_inquiries` + emails Karissa via Resend. Used by Mezzanine + Plan-an-Event CTAs.
**SEO:** unique titles/descriptions/canonical/OG/Twitter on every page; 100% image alt-text; robots.txt + sitemap.xml (13 urls) + llms.txt; favicon (agave on navy) + theme-color; JSON-LD on `/` (Restaurant + Menu + Event), `/mezzanine` (Place), `/private-events` (Service), `/about` (Restaurant).
**Time-sensitive / event content (added 2026-07-03):**
- **Holiday closure announcement bar** — date-gated in `page-shell.tsx`: shows a navy "Closed July 3–4 for the holiday — back open Tuesday, July 7! 🎆" bar during Jul 3–6 2026 (Pacific, window end `2026-07-07T00:00:00-07:00`), auto-reverts to the pink hiring bar on Jul 7 (they're normally closed Sun–Mon, so reopen Tue Jul 7). No manual removal needed.
- **Love Island Finale section** — `LoveIslandSection` on the homepage (between What's-on-this-week and Fiesta teaser): dark watch-party band, framed MezzWatchParty photo, flyer copy ("All tacos. All tequila. All drama." · Sun July 12 · Doors 5PM · 21+ · full restaurant takeover, main dining room + Mezzanine · only 50 seats · $10 Villa Pass = $10 dining credit) + feature row (Big Screens · Signature Cocktails · Love Island Menu · Giveaways & Villa Prizes). CTA **"Get Your Villa Pass →"** is LIVE → `TICKETS_URL = https://www.tickettailor.com/events/unomasllc/2296397` (Ticket Tailor). Owner has event flyer graphics (banner + square) NOT yet in the DAM — upload to Cloudinary if we want them as the OG/social share image or a section visual.

## 5. REMAINING / OPEN WORK (prioritized)
1. **Marketing pixels — NOT installed (needs IDs from owner):** Meta Pixel ID, GA4 Measurement ID (`G-…`), Klaviyo public API key (6-char). Once provided: add to root head/tracking + wire events. (GA4 may already exist elsewhere — confirm.)
2. **3 JSON-LD schemas to add (no inputs needed):** `/fiesta-box` → Product, `/catering` → Service, `/now-hiring` → JobPosting.
3. **(Optional) Love Island Finale flyer graphics** — owner has a banner + square flyer (Ticket Tailor promo). Upload to the DAM to use as the homepage OG/social share image and/or a section visual. Ticket CTA is already live (Ticket Tailor). ~~Paste Eventbrite URL~~ ✅ done via Ticket Tailor.
4. **Resend domain verification** for `events@unomastacoshop.com` sender (confirm done).
5. **Nice-to-haves:** verify mobile drawer on a real device; optional tonal step on same-color section transitions.
   _(Done: production domain connected; margs confirmed $6; Wednesday = Beer & Bites Wednesday.)_

## 6. Quick resume prompt for the next session
> "Resume the Uno Más Lovable site (project 78c4ac75-6325-4f38-a44b-278bb2194cf2, live at uno-mas-site-builder.lovable.app, repo Ramsey-SL/uno-mas). Read website/SITE-STATUS.md. Next up: [pixels / 3 JSON-LD schemas / domain]. Use send_message with typecheck-only, deploy, verify via curl --compressed."
