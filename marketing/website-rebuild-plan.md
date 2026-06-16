# Uno Más Website Rebuild — Planning Doc

**Goal:** Move unomastacoshop.com off Squarespace onto a Netlify-hosted stack with Cloudinary for media, AI-assisted editing in Lovable/Claude, big-bang cutover, and a Mezzanine sub-brand section. Built for speed, mobile, local SEO, and AI-search rankings.

**Decisions already locked in:**
- Editing model: AI-assisted in Lovable/Claude
- Migration: Big bang (build first, flip DNS in one move)
- In scope: Resy + Toast loyalty integration, schema markup + AI-search optimization, Mezzanine sub-brand section

**Decision still open:** Framework. This doc walks through the four options with pros/cons specific to Uno Más and full stack costs, then recommends one.

---

## TL;DR Recommendation

**Build it in Lovable (React + Supabase) with Astro-style optimization patterns, hosted on Netlify, media on Cloudinary.**

Why this wins for Uno Más specifically:
1. You're already building the Creative Studio app in Lovable. Same stack = one source of truth, shared brand_guidelines table, shared components.
2. "AI-assisted editing in Lovable/Claude" is the editing model you chose — Lovable is literally the only option that delivers that natively today. The other frameworks would need bolt-on tooling.
3. Resy + Toast + Klaviyo integrations are easier in React (every vendor has a JS SDK or embed).
4. The Mezzanine sub-brand section becomes a routing concern, not a separate build.
5. The cost penalty vs Astro is real but small (~$20–40/mo more), and the velocity gain is huge.

**Realistic monthly stack cost:** ~$60–120/mo all-in. Detailed below.

---

## Framework Comparison (Pros/Cons for Uno Más)

### Option 1 — Lovable (React + Supabase) ⭐ RECOMMENDED

**What it is:** Modern React app, built and edited inside Lovable's AI-assisted IDE. Supabase for database, auth, file storage. Deployed to Netlify.

**Pros for Uno Más:**
- **Already in your stack.** Creative Studio is being built here. Same `brand_guidelines` table powers both the app and the website's brand-consistent content.
- **AI-assisted editing is native.** Your team types "change the dinner hero subhead to ___" and Lovable does it. This is your stated editing model.
- **Resy integration is easy.** Embed widget or API call from React component. Same for Toast loyalty data via Klaviyo or direct.
- **Mezzanine sub-brand handled via routing.** `/mezzanine/*` routes load a different theme provider with different colors/fonts. No separate codebase, no separate hosting bill.
- **You own the codebase.** Pushed to your `uno-mas` GitHub repo. Future devs can pick it up. No vendor lock-in beyond Supabase (which is open-source-friendly).
- **AI search-readiness:** Easy to add JSON-LD schema, structured data, and llms.txt files. Server-side rendering via Netlify build gives crawlers clean HTML.

**Cons for Uno Más:**
- **Heavier than Astro by default.** React ships more JavaScript. Mitigations: use SSR/SSG via Vite plugins, code-split aggressively, lazy-load below-fold content. Lighthouse 90+ is achievable but takes attention.
- **Lovable plan cost.** $20–50/mo recurring vs free tools.
- **SEO ceiling.** Slightly lower than Astro/Hugo if not carefully tuned. Realistic 90-95 Lighthouse vs Astro's 98-100 out of the box.
- **Team needs to learn Lovable's editor.** Not hard — they already use it for Creative Studio — but it's still a tool.

**Monthly cost (Lovable path):**
- Lovable Pro: ~$20–40/mo
- Supabase Free tier (or Pro $25/mo when you grow): $0–25/mo
- Netlify Free tier (covers ~100GB bandwidth): $0
- Cloudinary Free tier (25GB storage, 25k transforms): $0
- Domain (already own): $0
- **Total: $20–65/mo**

**One-time cost:** Build time is the cost. Realistically 40–80 hours of Lovable-assisted work + your review. If outsourced to a developer, $5–15K depending on scope.

---

### Option 2 — Astro + Decap CMS

**What it is:** Astro is a modern static site generator built for content sites. Decap is a free, open-source git-based CMS (form-based editing that commits to GitHub).

**Pros for Uno Más:**
- **Fastest possible site.** Astro ships near-zero JavaScript. Lighthouse 100s are routine. This is the best technical SEO foundation available.
- **Decap CMS is free and self-hosted.** No per-seat costs.
- **Git-based editing = full version history.** Every team edit is a commit. Easy to revert mistakes.
- **Pure HTML/CSS output.** Search engines and AI crawlers love it.
- **Cheap to host.** Static files on Netlify, free tier covers everything.

**Cons for Uno Más:**
- **NOT AI-assisted editing.** Decap is form-based — "fill in the Hero Headline field." Doesn't match your stated editing preference.
- **Separate from Lovable.** Two different stacks, two different mental models. The Creative Studio app and the website don't share components or state.
- **Resy/Toast integrations require more setup.** Astro components can do it, but it's more manual than React.
- **Dynamic features are harder.** Anything stateful (logged-in user, loyalty, real-time menu) needs to fall back to client-side React or hit external APIs.
- **Team setup time.** Decap admin panel needs to be configured per content type (hero, menu item, blog post, event).

**Monthly cost (Astro path):**
- Astro: free
- Decap CMS: free
- Netlify Free: $0
- Cloudinary Free: $0
- **Total: $0/mo**

**One-time cost:** Build is ~30–60 hours of dev work. $3–10K outsourced. Slightly cheaper than Lovable because the framework does more of the work.

**Verdict for Uno Más:** Best technically. Worst fit for your editing preference. Worth it only if you change your mind on AI-assisted editing.

---

### Option 3 — Webflow → Netlify export (or Webflow hosting)

**What it is:** Webflow is a visual page builder. You design pages in a Figma-like UI, no code. Export static HTML or host on Webflow's CDN.

**Pros for Uno Más:**
- **True drag-and-drop editing.** Team designs visually, sees results live.
- **Strong design control.** Pixel-perfect, animations, interactions.
- **Good built-in CMS for blog/menu/events.**
- **Solid SEO defaults.**

**Cons for Uno Más:**
- **Highest recurring cost.** $39–49/mo per site for CMS plan, plus $23/mo per additional editor seat. Mezzanine sub-brand likely means a second site = double the bill.
- **Not the editing model you chose.** Webflow is visual, not AI-assisted. Doesn't unlock the "type what you want in plain English" workflow.
- **Disconnected from your Lovable Creative Studio.** Different platform, no shared brand database. Your `brand_guidelines` would have to be manually mirrored.
- **Resy/Toast integration is harder.** Custom code embeds work but feel hacky.
- **Vendor lock-in.** If Webflow changes pricing or features, you're stuck.

**Monthly cost (Webflow path):**
- Webflow CMS plan: $39/mo (per site, billed annually)
- Mezzanine as second site: +$39/mo → $78/mo
- Or single site with subdirectory: $39/mo (limits brand separation)
- Cloudinary Free: $0
- Netlify Free (if exporting): $0
- **Total: $39–78/mo**

**One-time cost:** Designer time to build pages, ~$3–8K if outsourced. Lower if you DIY.

**Verdict for Uno Más:** Strong tool, wrong fit. The cost is fine, but it competes with rather than complements your Lovable Creative Studio investment.

---

### Option 4 — Framer

**What it is:** Modern visual page builder. Think Webflow's younger, faster cousin. Strong motion, clean output, growing CMS.

**Pros for Uno Más:**
- **Beautiful design output.** Strongest motion/animation of any visual tool.
- **Fast performance.** Modern build pipeline.
- **Reasonable price.** $20–30/mo per site.
- **Built-in CMS.**

**Cons for Uno Más:**
- **Not AI-assisted editing.** Visual builder. Same mismatch as Webflow.
- **Newer ecosystem.** Fewer integrations than Webflow. Resy/Toast embeds work but with more fiddling.
- **Less SEO-mature.** Improving fast, but not yet at Astro's level.
- **Disconnected from Lovable.** Same problem as Webflow.

**Monthly cost (Framer path):**
- Framer Pro: $20–30/mo
- Mezzanine as second site: ~$40–60/mo total
- Cloudinary Free: $0
- **Total: $20–60/mo**

**One-time cost:** Similar to Webflow.

**Verdict for Uno Más:** Cheaper Webflow. Same fundamental fit problem.

---

## Editing Workflow — AI-Assisted in Lovable/Claude

This is what your team's daily editing actually looks like, assuming Lovable framework:

**Scenario 1 — Update the dinner hero copy:**
- Karissa opens Lovable.
- Types: "On the dinner page, change the hero subhead from 'X' to 'Y' and swap the photo for the new Surf & Turf shot from Cloudinary."
- Lovable makes the change, shows preview. Karissa clicks Approve. Live in 30 seconds.

**Scenario 2 — Add a new menu item:**
- Open Lovable. Type: "Add a new dinner item: Achiote Cilantro Shrimp, $30, 'Wild prawns, citrus achiote glaze, charred lime, herbed rice.' Use the photo at cloudinary.com/...".
- Lovable updates the menu page (or, better: updates the menu record in Supabase, which the page reads from).

**Scenario 3 — Run a promotional banner:**
- Type: "Add a banner across the homepage saying 'Mother's Day Brunch — Sundays 10am–4pm' linking to /brunch, brand pink background, dismissible."
- Lovable does it, can schedule it to auto-disappear after a date.

**For the non-AI fallback:** Lovable also gives a visual canvas. Team can click an element and edit text directly without prompting.

**Power user workflow (you / me / Claude):**
- For larger changes (new page templates, restructured navigation, schema markup updates), Claude can generate the code, push to GitHub, Lovable picks it up. Same repo, no friction.

---

## Big Bang Migration Plan

**Phase 0 — Foundation (week 1)**
- Audit current Squarespace site: list every page, every URL, every asset.
- Export all photography, copy, blog posts. Upload to Cloudinary.
- Set up Netlify project connected to `uno-mas` GitHub repo.
- Set up `new.unomastacoshop.com` staging subdomain pointing to Netlify.

**Phase 1 — Build (weeks 2–4)**
- Build core pages in Lovable: Home, Menu (lunch/dinner/brunch/cocktails), About, Reservations, Events, Mezzanine section, Contact.
- Integrate Cloudinary for all media (auto-format, auto-quality, responsive images).
- Implement JSON-LD schema: Restaurant, Menu, MenuSection, MenuItem, Event, Review.
- Add llms.txt file for AI crawlers (Perplexity, ChatGPT, Claude).
- Resy reservation embed integrated where appropriate.
- Toast loyalty signup (Cantina Club) — at minimum a Klaviyo form linked to the segment.
- Mezzanine section: separate visual theme, separate metadata, separate sitemap entries.

**Phase 2 — Polish (week 5)**
- Lighthouse audits — target 90+ on all four metrics on mobile.
- Local SEO check: Google Business Profile alignment, NAP consistency, schema validation.
- Cross-browser test, mobile test (real devices, not just emulator).
- Set up 301 redirects from every old Squarespace URL → new URL. Critical for SEO preservation.
- Submit new sitemap to Google Search Console.

**Phase 3 — Cutover (week 6 — single day)**
- Final content review with team.
- Update DNS A/CNAME records to point to Netlify.
- DNS propagates over 4–24 hours.
- Monitor 404s, Search Console errors, page speed.
- Keep Squarespace site live but inaccessible publicly for 2 weeks as rollback insurance, then cancel.

**Total realistic timeline:** 5–7 weeks if focused, 8–12 weeks if part-time.

---

## In-Scope Add-Ons

### 1. Resy + Toast Loyalty Integration

**Resy:**
- Resy provides a JavaScript embed widget. Drop it on `/reservations` page, configured to your venue ID.
- Reservation buttons on Home, Menu, Dinner pages all open the Resy modal.
- Track reservation events in GA4 for conversion attribution.

**Toast Loyalty (Cantina Club):**
- Toast itself doesn't have a great web signup form, but the integration path is:
  - Klaviyo form on the site → captures email/phone → tags as "loyalty interest"
  - Klaviyo flow sends them a sign-up link / explains how to join in-restaurant
  - Toast → Klaviyo segment sync handles the rest
- For logged-in loyalty member experiences (e.g., "you have 200 points"), that's harder — Toast's API is not consumer-friendly. Recommend skipping in v1.

### 2. Schema Markup + AI Search Optimization

This is the biggest underused lever for Uno Más specifically. AI search (Google AI Overviews, ChatGPT, Perplexity, Claude) is replacing traditional "blue links" results, especially for "best [thing] in Spokane" queries.

**JSON-LD schema to add:**
- `Restaurant` schema on home: address, phone, hours, cuisine, priceRange, photo
- `Menu` and `MenuSection` and `MenuItem` schema on menu pages
- `Event` schema for Mezzanine events / brunch launches / pop-ups
- `Review` and `AggregateRating` (pulled from Google reviews if licensable)
- `LocalBusiness` parent type with all hours and contact info
- `OpeningHoursSpecification` with proper day/hour ranges

**llms.txt file at root:** A new emerging standard. Plain-text file telling AI crawlers what your site is, how to summarize it. Place at `/llms.txt`. Format roughly:
```
# Uno Más Tacos & Tequila
Modern Mexican restaurant and tequila bar in Spokane, WA.
[brand summary, links to key pages]
```

**Other AI-search optimizations:**
- Server-side render every page (no client-side-only content) — AI crawlers don't run JS reliably.
- Clean semantic HTML (proper `<article>`, `<section>`, `<address>` tags).
- Plain English page summaries in `<meta description>`.
- Avoid generic stock copy — AI synthesizers reward distinctive language. Your Uno Más voice is an advantage here.
- Get cited: outbound mentions matter less; inbound matter. Press, Inlander coverage, Google reviews, Spokane food blogs.

### 3. Mezzanine Sub-Brand Section

**Recommended:** Single codebase, separate subroute (`/mezzanine/*`), separate theme.

- `/` → Uno Más home (pink, agave logo, Antonio/Montserrat)
- `/menu`, `/dinner`, `/brunch` → Uno Más styling
- `/mezzanine` → Mezzanine landing (black/electric pink, DIN/Poppins/Baka Too)
- `/mezzanine/events`, `/mezzanine/private-events` → Mezzanine styling

**Technically:** Wrap the `/mezzanine/*` routes in a different `ThemeProvider` component that swaps the CSS variables (colors, fonts). The brand separation rules from your brand_guidelines stay enforced at the code level.

**Alternative:** True sibling site at `mezzanine.unomastacoshop.com`. Cleaner brand separation, more SEO domain authority overhead. Worth it only if you want Mezzanine bookings to feel like a genuinely different business. Recommend deferring this until v2.

---

## Stack Cost Summary (Recommended Path)

**Monthly recurring:**
| Item | Cost | Notes |
|---|---|---|
| Lovable Pro | $20–40/mo | Required for AI editing workflow |
| Supabase | $0–25/mo | Free tier covers small DBs; Pro at scale |
| Netlify | $0 | Free tier (100GB bandwidth) — way more than you'll use |
| Cloudinary | $0 | Free tier (25GB storage, 25k transforms) — sufficient for v1 |
| Domain | $0 | Already owned |
| **Subtotal** | **$20–65/mo** | |

**Possible add-on costs as you grow:**
| Item | When | Cost |
|---|---|---|
| Cloudinary Plus | When you hit free-tier limits (likely 6–12 months in) | $89/mo |
| Netlify Pro | If you need form spam protection, more team seats, or analytics | $19/mo per member |
| Supabase Pro | When you exceed 500MB DB or 1GB bandwidth | $25/mo |
| Schema validation tool (optional) | Schema.dev or Stencil | $15–30/mo |

**One-time build cost estimates:**
| Path | Estimate |
|---|---|
| Self-built in Lovable (you + Claude) | $0 cash, ~60–100 hours of your time |
| Hybrid: you build, contractor finishes | $3–8K |
| Fully outsourced to a developer | $10–25K |

**Realistic recommendation:** Build the v1 yourself in Lovable using Claude for the heavy code lifts and brand work. Hire a contractor only for the schema markup, performance tuning, and DNS cutover (last 1–2 weeks of work) — that's specialized, ~$1.5–3K of work, saves you weeks of headache.

---

## Local SEO + Best Practices Checklist

Built into the recommended stack from day 1:

**Performance (mobile-first):**
- Cloudinary auto-format (WebP/AVIF) and responsive `srcset`
- Lazy-load images below the fold
- Defer non-critical JS
- System fonts or font-display: swap for Antonio/Montserrat
- Target Lighthouse mobile: Performance ≥90, Accessibility ≥95, Best Practices ≥95, SEO 100

**Local SEO:**
- NAP (Name/Address/Phone) consistent everywhere — site, Google Business Profile, Yelp, Resy
- Google Business Profile fully optimized with Uno Más, Mezzanine, Patio as distinct service categories
- Local schema on every page
- "Modern Mexican Spokane," "speakeasy Spokane," "dinner Spokane," etc. as natural-language headlines (not stuffed)
- Reviews pulled in via schema where licenses allow
- City-specific landing pages if expanding catering territory (e.g., "Catering for Coeur d'Alene")

**Mobile usage:**
- Sticky mobile nav with single thumb-reachable CTA (Reservations or Call)
- Click-to-call phone number tag on mobile
- Click-to-map Google Maps integration
- Menu PDF backup but HTML menu primary (PDFs don't rank)

**AI rankings:**
- Server-side rendered HTML
- Distinct, voice-driven copy (your `voice_personality_traits` brand guidelines applied)
- Structured data on every page
- llms.txt file
- Clean URL structure (`/menu`, `/dinner`, `/mezzanine` — no `?p=42`)

---

## Next Steps

If you green-light the Lovable path, the immediate next actions are:

1. **Decide framework** — Lovable + Supabase (recommended) or one of the alternatives above
2. **Inventory current Squarespace site** — I can help build this list if you want
3. **Set up Cloudinary account** and start uploading the brand asset library
4. **Set up Netlify** connected to the `uno-mas` GitHub repo
5. **Spin up a new Lovable project** specifically for the website (separate from Creative Studio, but pulling from the same brand_guidelines table)
6. **Draft the site map** — every page and its purpose
7. **Build phase 1**

Each of those steps I can drive or assist on as you want. The biggest blocker upstream is the framework call — once that's locked, the rest is execution.

---

*Generated: 2026-05-16*
*Source documents: brand-intelligence-center/*.md, docs/uno-mas-creative-studio-roadmap.md, content-studio/manifest.json*
