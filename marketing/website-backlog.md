# Uno Más Website — Backlog

**Owner:** Ramsey
**Last updated:** 2026-05-25
**Project:** `uno-mas-site-builder` (Lovable) → published to `unomastacoshop.com` (eventually)
**Stack:** TanStack Start + Tailwind v4 + shadcn/ui on Lovable Cloud, Supabase = `coandmppuqqzcbbhcien`, deploy target = Netlify, photos via Supabase Storage assets table with `role:*` tag routing

---

## 📥 INBOX — quick capture, triage later

Anything that comes to mind, drop here as a one-liner. Half-formed thoughts welcome. Claude (or you) sweeps these into proper NOW / NEXT UP / FUTURE sections with priority + effort tags during weekly triage.

- **Photo shot list — gaps to capture next shoot.** Missing photos that the website needs: (1) **The Uno Más Feast** ($129) — full table spread, ideally with people enjoying it. Currently NO photo of the signature feast. (2) **Off-site catering setups** — buffet line at an event, branded packaging, catering team at work. (3) Team headshots (Ramsey/Karissa/Thomas/Maraya). (4) Mezzanine event-mode shots — leather lounges with people, fireplace lit, cocktail reception in progress. (5) **MORE patio photos** — we have one good wide-angle (string lights, agave, umbrella, heat tower, sectional) but need: patio crowd at golden hour, food being served outdoors, the outdoor bar in action, daytime brightness, post-sunset string-light glow. The patio is a real selling point — we're under-photographed there. (6) Exterior of building on Monroe + street-level identifier shot. (7) Espresso Margarita close-up (have hero but no detail shot). Build into the next professional shoot brief.
- **Form integrations for launch.** /now-hiring form should sync to existing Now Hiring Google spreadsheet (whatever Squarespace currently routes to). Catering inquiry form should integrate to Toast catering pipeline. Loyalty signup should hit Toast rewards (or surface the Toast rewards signup URL inline). [P1 — affects /now-hiring, /private-events, homepage Klaviyo strip]
- **Resy button UX on mobile.** Currently doesn't open in a new window/tab, and once on Resy the user has no easy way back to unomastacoshop.com. Fix: add `target="_blank"` + `rel="noopener noreferrer"` to the Resy link OR embed the Resy widget inline so they never leave. Affects header + hero + reservations page. [P1 UX — mobile-blocking on reservation flow]
- ✅ **Hours reconciled 2026-05-25.** Supabase `business_hours` now matches live Squarespace + Google listing: Sun-Mon CLOSED, Tue-Thu 11am-9pm, Fri-Sat 11am-10pm. Brunch placeholder removed.
- **Listings hygiene pass.** Visit Spokane has wrong zip (99201 vs 99205) + outdated description. Audit Yelp/Yahoo/Restaurantji/Bing Places/Apple Business Connect for claim status. Add task to bring all third-party listings in sync with master reference. [P2]
- **Wire Google Places API for website reviews + schema.** Fetches live rating + 5 most-recent Google reviews. Powers `/about` reviews section, `aggregateRating` JSON-LD. Free tier should cover us. [P2 — improves AI search citation odds]
- **Standing review response cadence.** Use `local-business-marketing-os:review-responses` skill weekly on Google + Yelp. Mixed reviews surfaced (one "degraded" feedback, "white rice in the bowl" mention) — worth getting in front of. [P2]
- **🚨 Tracking setup decision.** Live Squarespace site uses GTM container `GTM-T6L25CLD` (wrapper that fires GA4 + other tags). GA4 Property ID = `383242412`. Need to: (1) grab actual GA4 Measurement ID from GA4 Admin → Data streams; (2) decide whether to re-use `GTM-T6L25CLD` on rebuild or wire GA4/Meta Pixel directly via gtag.js. [P1 — blocks launch]
- **Phone number captured:** (509) 960-7989. Already added to master reference doc.
- **Unify Cloudinary upload paths in studio.** `/app/bulk-upload` routes to Cloudinary correctly. `/upload` (public) and `/app/submit-asset` route to Supabase Storage and skip Cloudinary entirely. Result: 29 existing assets are in Storage, no Cloudinary transformations applied. Either (a) modify the submit routes to also use `uploadToCloudinary()`, or (b) document that admins should always use bulk-upload going forward. [STUDIO project, not website]
- **Backfill 29 existing Supabase Storage assets to Cloudinary** if we want consistent optimization. One-time script that reads each Storage URL, re-uploads to Cloudinary via `uploadToCloudinary()`, writes Cloudinary fields back to the asset row. Optional — current assets work for the website as-is, just aren't optimized.

---

## 🗨 Capture patterns (for chat)

Use these at the start of any message — Claude treats them as **side actions** that don't interrupt the current work in flight.

| Pattern | What happens |
|---|---|
| `log: [idea]` or `backlog: [idea]` | Adds a one-liner to INBOX. Brief ack, back to work. |
| `idea: [thought]` | Same as above |
| `done: [item]` | Moves item from NOW → DONE with today's date |
| `defer: [item]` | Moves from NOW / NEXT UP → FUTURE |
| `priority: [item] [P1/P2/P3]` | Updates priority tag on an existing item |
| `triage` or `sweep inbox` | Process all current INBOX items into proper sections |

**Examples:**
- "log: add a 'view our story' video on the about page" → into INBOX
- "log: catering needs its own hero photography — taco platters, full table spreads" → into INBOX
- "done: contact strip" → moves to DONE
- "defer: schema markup foundation" → moves from NEXT UP to FUTURE
- "triage" → Claude reads INBOX, sorts items, suggests priorities, asks for confirmation before moving

**Pro tip:** While Lovable is building (3–10 min), that's the perfect window to dump captures. Hit ideas one after another — Claude can batch process 10 as fast as 1.

---

## How to use this file

- **Now** = active work this week
- **Next up** = queued for the next 1–2 weeks once Now clears
- **Future** = parked or low-priority ideas, no commitment
- **Done** = recently completed (last 30 days), trim periodically

For each item: title, _why it matters_, effort (S/M/L), dependencies if any, notes.

Priority tags:
- **P1** = blocks launch
- **P2** = important but launch can go without
- **P3** = nice-to-have

---

## NOW (this week)

### Build out remaining homepage sections **P1** · M
- Verify all 7 sections render on `/`: hero, venues intro, venues cards (3-up), dinner feature, testimonials, mezzanine teaser, visit/contact strip
- Mobile responsive pass — DevTools at 375px, real iPhone test
- Fix any 404s in console (especially the old `brand_assets` query if it still lingers)

### Finish the contact/hours strip **P1** · S
- Lovable's own suggestion. Hours table styling, "Today is open until X" logic, click-to-call, click-to-map
- Pulls from `business_hours` table (we seeded placeholders — real hours need to be edited)

### Enforce banned terms guard **P1** · S
- Lovable's suggestion. Adds runtime check that flags banned-words usage in rendered copy. Catches future regressions where Lovable might re-invent off-brand copy.
- References `slug:voice_never_principles_words` brand_guideline record

### Build /menu hub page **P1** · M
- 4 cards: Lunch, Dinner, Brunch, Cocktails
- Each card image-driven, links to /menu/[daypart]
- ✅ Brunch card is LIVE — links to /menu?tab=brunch (Sundays 10am–4pm)

### Build /menu/dinner page **P1** · M
- Hero band with Antonio "DINNER" headline
- Menu sections + items from Supabase (`getMenuSections('dinner')`)
- Reserve CTA (Resy button)
- Feast callout

### Build /mezzanine page **P1** · L
- Sub-brand theme: black bg, electric pink #E22790, DIN/Oswald + Poppins fonts
- Hero from site_content `/mezzanine` block
- 3 use-case cards (private dinners, buyouts, cocktail receptions)
- Inquiry strip with mailto:karissa@unomastacoshop.com

### Build /about page **P1** · M
- Hero + brand narrative + team grid + visit strip
- Pull from brand_guidelines (business_identity_concept, business_team_contact, positioning_summary)

### Fix /debug page query args **P3** · XS
- `getSiteContent('home')` → should be `getSiteContent('/')`
- `resolveImageByTags('role:hero')` → should test specific tags like `role:hero-dinner`
- Cosmetic — data layer already verified working

---

## NEXT UP (1–2 weeks)

### Real photography upload **P1** · M (depends on shoot)
- Currently the homepage hero falls back to the "Uno Mas - Pink" logo because no asset is tagged `role:hero-cantina`. Same for Mezzanine, patio, dinner plate close-ups.
- Need shots of:
  - Cantina interior (wide + close detail) → tag `role:hero-cantina`, `role:venue-cantina`
  - Mezzanine mood (leather, fireplace, dark) → `role:hero-mezzanine`, `role:venue-mezzanine`
  - Patio (outdoor energy) → `role:hero-patio`, `role:venue-patio`
  - Dinner plates: Surf & Turf, Carne Asada, Achiote Shrimp, Feast → tag with the menu item slug (`carne-asada`, `surf-turf`, etc.) for menu page autobinding
  - Espresso Margarita + bar shots → `role:hero-cocktails`
  - Team headshots → `role:team-[firstname]`
  - Exterior storefront → `role:exterior`
- Upload via Studio Asset Browser, set status='approved', tag with role:* convention
- Once uploaded, homepage hero auto-updates next page load — no code change

### Schema markup foundation **P1** · M
- JSON-LD Restaurant schema on /, /about (address, phone, hours, cuisine, priceRange, geo)
- Menu + MenuSection + MenuItem schemas on /menu, /menu/dinner
- LocalBusiness with OpeningHoursSpecification
- AggregateRating if Google reviews can be licensed/embedded
- Single biggest lever for AI search ranking (Google AI Overviews, Perplexity, ChatGPT)

### llms.txt + sitemap.xml + meta tags **P1** · S
- Static llms.txt at root with brand summary for AI crawlers
- Dynamic sitemap.xml from routes
- Per-page meta tags (title ≤60ch, description ≤155ch, og:image from Cloudinary/Supabase Storage)
- robots.txt allowing all, pointing to sitemap

### Google Maps embed on contact strip **P2** · S
- Lovable's own suggestion. Embed the 2020 N Monroe address as an interactive map
- Or use a static Google Maps image with click-through link if interactive feels heavy

### Add /menu/lunch + /menu/brunch + /menu/cocktails **P2** · M
- Currently menu_sections only has dinner + cocktails seeded. Need lunch/brunch data added.
- Then duplicate the dinner page template for each daypart
- ✅ Brunch is LIVE at /menu?tab=brunch (Sundays 10am–4pm, launched July 2026)

### SEO review (Lovable's suggestion) **P2** · S
- Run Lovable's built-in SEO audit
- Address top issues (page speed, semantic HTML, alt text, internal linking)

### Third-party listings management — Phase 2 **P2** · M (deferred per 2026-05-26 SEO planning)
- **Decision 2026-05-26:** defer Yelp + TripAdvisor + Visit Spokane + Apple Business Connect + Bing Places claim/management to a later phase. Focus current sprint on owned SEO (schema, llms.txt, site content).
- Top "best Mexican Spokane" Google results are dominated by these directories — long-term we must invest here, but not blocking launch.
- When ready, sequence: claim → audit current data → write standard responses → set weekly review-response cadence (see #35).

### Resy widget — inline embed (parked, deferred) **P3** · S
- **Parked** — Resy OS portal currently doesn't expose the inline-widget configuration UI in a discoverable way
- We're using Resy's button widget pointing to the venue page in a new tab instead. Works fine for 95% of bookings.
- When ready: Resy Manager → look for "Marketing → Widgets" or "Integrations → Embed" — copy the inline JS snippet (different from the button code we have)
- Replace the button on `/reservations` page with an inline party-size/date picker
- Public widget API key (safe to expose): `g47nf19Sg6grqO50HcS2HDIUIO8PjEGM`
- Resy Venue ID: `87582`

### Resy button brand styling **P3** · S
- **Decision 2026-05-17:** kept Resy's default widget (orange "Book Now" with in-page modal). In-page modal UX wins over brand consistency for now.
- If brand purity becomes important later, two paths:
  - **Path A** (recommended): swap to a custom pink #E22690 button that opens Resy in a new tab. No widget needed. ~20 lines of code, fully on-brand, can't break from Resy-side updates.
  - **Path B**: keep widget but use MutationObserver to force-rewrite text + colors after Resy injects. More fragile.
- Trigger to revisit: brand audit findings, or if Resy widget appearance ever conflicts with major design direction

### Toast loyalty (Cantina Club) signup form via Klaviyo **P2** · M
- Klaviyo form on homepage + about + footer for "Join the Cantina Club"
- Submits to Klaviyo segment tagged `loyalty interest`
- Klaviyo flow handles email/SMS welcome and explains in-restaurant signup path
- Avoid embedding live loyalty member balance (Toast's consumer API is messy — defer to v2)

---

## FUTURE (no commitment)

### Blog / journal section for local SEO **P2** · L
- `/journal` with 3–5 starter posts: "Best brunch in Spokane," "Why house-smoked carnitas matter," "What makes a tequila bar," etc.
- Targets local SEO keywords from brand_guidelines `digital_search_terms` record
- Long-term traffic engine

### Performance tuning to 90+ Lighthouse mobile **P2** · M
- Image optimization (responsive srcsets, lazy load, AVIF/WebP)
- Critical CSS inlining
- Defer non-critical JS
- Font display optimization (Antonio + Montserrat)
- Target: Performance ≥90, Accessibility ≥95, Best Practices ≥95, SEO 100

### 301 redirect map from Squarespace **P1 pre-launch** · M
- Pull list of every old URL from current Squarespace site
- Map each → new equivalent on the rebuilt site
- Critical for SEO preservation when DNS flips
- Save as `netlify.toml` redirect rules

### DNS cutover unomastacoshop.com → Netlify **P1 launch** · S (single action, low effort, high stakes)
- After all P1 launch items done and team-reviewed
- Update A/CNAME records at registrar
- 4–24 hour propagation window
- Keep Squarespace site reachable but un-indexed for 2 weeks as rollback insurance

### Press / accolades section **P2** · S
- Inlander coverage, awards, etc.
- Adds AI-search credibility (citation signals)
- Schema.org Review + AggregateRating if usable

### Brunch page (full design) once details locked **P2** · M
- Currently just a placeholder in nav
- Full menu, hero, "Mother's Day launch" callout
- Trigger to build: brunch menu finalized + Sundays-confirmed launch date

### Phase 1 Business Hub (per Creative Studio roadmap) **P3** · XL
- From `docs/uno-mas-creative-studio-roadmap.md`
- Studio becomes source of truth for hours, menu, photos
- Auto-syndicates changes to: website, Google Business Profile, Apple Business Connect, Yelp, Facebook, Instagram, Klaviyo
- Edit in studio once → propagates everywhere
- Long timeline (months) but unlocks the multiplier on the studio investment

### Phase 2 Website Builder absorbed into Studio **P3** · XL
- From studio roadmap
- Edit website pages inside the Creative Studio app
- Section-by-section visual editor with live preview
- One-click publish via Netlify Deploy API
- Replaces the standalone Lovable workflow

### Multi-brand mode (Mezzanine as sibling site) **P3** · L
- If The Mezzanine grows into its own destination brand
- `mezzanine.unomastacoshop.com` as a sibling site
- Separate Lovable project, same Supabase, brand_mode filter on guidelines
- Currently handled via theme provider on `/mezzanine/*` routes — sufficient for now

### Vista Social + scheduling integrations **P3** · L
- Pull from Vista Social into a "Latest from social" homepage section
- Show recent Instagram/TikTok posts as gallery
- Bidirectional: publishable approved campaigns push back into Vista Social

### Catering / events lead capture **P2** · M
- Dedicated `/catering` and `/private-events` pages with intake forms
- Forms route to karissa@unomastacoshop.com
- Track conversion in GA4 for Mezzanine sales pipeline reporting
- Per business goals: catering target is $8K/month, structured outreach

### AI search optimization deepdive **P3** · M
- Beyond JSON-LD schema and llms.txt
- Pre-built FAQ blocks for "best Mexican Spokane," "is Uno Más kid-friendly," etc.
- Optimize meta descriptions for AI Overview pull
- Monitor Perplexity / ChatGPT citation patterns

### Interactive 3D venue walkthrough **P3** · XL
- If/when budget allows. 3D scan of cantina + Mezzanine + patio.
- Embedded on /about or each venue page
- High wow-factor for events sales

### Email signup gates for menu PDFs **P3** · S
- Soft email capture: download dinner menu PDF in exchange for email
- Adds to Klaviyo segment
- Low-effort, low-conversion but cumulative

---

## DONE (recent — last 30 days)

### 2026-05-16 → 2026-05-17 — Foundation sprint
- ✅ Fixed Generate Concepts 2000-char validation error in studio (archived 4 oversized brand_guidelines records, imported 39 curated ones)
- ✅ Inventoried Creative Studio app, mapped what existed before duplicating work
- ✅ Created website tables in studio's Supabase: `site_content`, `menu_sections`, `menu_items`, `business_hours`, `hours_overrides`, `site_events`
- ✅ Seeded website data: 6 menu_sections, 6 menu_items, 8 business_hours rows, 9 site_content blocks
- ✅ Tagged all 29 existing assets with `role:*` convention (logos by color, tacos, food shots, brand pink)
- ✅ Reconnected website Lovable project to studio's Supabase (`coandmppuqqzcbbhcien`)
- ✅ Added missing RLS policies allowing anon read of `assets` (approved + non-archived) and `brand_guidelines` (active)
- ✅ Built homepage v1 with real data from site_content, brand_guidelines, business_hours, assets
- ✅ Wired Resy button widget (link-based, opens venue page in new tab) on header, hero, and /reservations
- ✅ Created this backlog file

### Earlier (pre-sprint, for context)
- ✅ Initial Creative Studio Lovable app built with 17 tables, brand_guidelines, copy library, campaign management
- ✅ Cloudinary integration set up (used by studio for AI generation outputs; website uses Supabase Storage for now)
- ✅ Brand intelligence MDs created in `uno-mas` GitHub repo (`brand-intelligence-center/*.md`)
- ✅ Content studio HTML template library built (48 templates, manifest.json) for studio use

---

## Notes & References

- **📘 Master brand reference (start here):** `UNO-MAS-MASTER-REFERENCE.md` in this workspace. Canonical doc for brand, menu, hours, social, tech stack, SEO, voice. Reference at start of any new session.
- **Supabase project:** `coandmppuqqzcbbhcien` ("Ramsey Uno Mas Database") — single source of truth for both studio AND website
- **Brand voice:** Source records have `slug:voice_*` tags in brand_guidelines table. Never invent copy; pull from records.
- **Banned words:** `slug:voice_never_principles_words` record. taco shop, authentic Mexican, mouthwatering, mixology, artisanal, etc.
- **Tag convention for assets:** `role:hero-{slot}`, `role:logo-{color}`, `role:menu-{item-slug}`, `role:venue-{name}`, `role:team-{firstname}`, plus existing `category:*` and `orientation:*` prefixes
- **Studio roadmap:** `docs/uno-mas-creative-studio-roadmap.md` in the `uno-mas` GitHub repo
- **Weekend sprint guide:** `uno-mas-weekend-sprint-v2.md` in this workspace

---

## How items move

1. New idea → drop in **Future** with date and effort estimate
2. When prioritized → move to **Next up** with priority tag
3. When started this week → move to **Now**
4. When complete → move to **Done** with completion date
5. Stale items in **Now** > 2 weeks → demote back to Next or Future

---

*Update this file as you go. It's the persistent memory of the project — don't rely on chat sessions to remember.*
