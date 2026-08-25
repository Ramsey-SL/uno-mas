# Homepage v2 — Agreed Build Spec (2026-06-23)

Decisions from the page-by-page review (options lookbook: `marketing/campaigns/_site-preview/options.html`).
Live site: Lovable `uno-mas-site-builder` (uno-mas-site-builder.lovable.app).

## Section order & decisions
1. **Hero** — KEEP current design (video photo-cluster + "GET A LITTLE LOST." + CTAs).
   - Fix only: restyle the **"Reserve a table"** button → primary **solid pink `#E22690`**, white text, rounded-full, soft shadow + hover-lift. Make all reserve CTAs consistent; secondary = teal/navy outline; tertiary = text + arrow.
2. **Transitions (global)** — **T3 Overlap & parallax:** sections overlap slightly with rounded tops; subtle parallax on section background images.
3. **~~Dinner section~~** — **REMOVED** ("The dinner Spokane didn't see coming." deleted). Dinner lives inside the interactive menu now.
4. **Interactive Menu (M1)** — NEW section: segmented pill tabs **Lunch · Dinner · Cocktails**; content (items + photo) swaps in place, pulled from Supabase menu data; each tab has "See full [daypart] menu" → `/menu/[daypart]`. *(Brunch tab is now LIVE — Sundays 10am–4pm, links to /menu?tab=brunch.)*
5. **What's On This Week (C3)** — NEW: events ticker + day-special chips.
   - **Love Island Watch Party** — Thursdays at The Mezzanine, doors 5 / show 6, 21+. **No tickets — reservations via Resy.** CTA "Reserve on Resy" + links to `/events/love-island` and the FB event (https://www.facebook.com/events/990221547324452/).
   - **Daily specials chips** → `/specials`: Taco Tuesday (BOGO street tacos · $6 margs · $30 pitchers) · Beer & Bites Wednesday ($5 pints · $10 loaded nachos · $10 loaded masa fries) · Big F’N Thursday ($10 Big F’N Quesadilla · $10 menu cocktails, fresh sheet).
6. **"Spokane is talking" (IG feed) — BG4 light editorial:** off-white `#F5F5F5` background (flip from dark), photos pop, pink accents, keep @unomastacoshop follow CTA.
7. **The Mezzanine (E2 split reveal)** — image slides in from one side, copy from the other on scroll. **MUST follow Mezzanine brand** (`brand-guidelines/11-mezzanine-brand-identity.md`): dark/black foundation, Electric Pink `#E22790` / Magenta `#BF28BF` / Ultra Violet `#93009B` gradient, DIN-condensed substitute (Oswald) headline + Poppins, line-art desert accents, real Mezzanine DAM photos. CTA "Find the stairs."
8. **Cantina Club** — UNCHANGED this session (parked; revisit later).
9. **Footer** — NOT YET DECIDED. Options F1–F4 in the lookbook (F1 3-col + map ★). All include an embedded Google Map + Get Directions + Google Business listing link. **Pending Ramsey's pick.**

## Open / follow-ups
- Footer option selection (F1–F4).
- Upload the Mezzanine logo to the Cloudinary DAM so the site/AI tools can pull it.
- Confirm lunch menu data is seeded in Supabase for the M1 tab.
