# Uno Más Website — Consolidated Status & Handoff

**Last updated:** 2026-06-15
**Purpose:** Single source of truth for the website rebuild. Read this at the start of any new Cowork session to get fully caught up, then close other chats. The chat is disposable — this doc + the live systems below are the real record.

**To resume in a fresh session, say:** *"Read UNO-MAS-WEBSITE-STATUS.md in Marketing HQ and catch up, then [your next request]."*

---

## The systems (where the work actually lives — not in any chat)

| System | ID / URL | Notes |
|---|---|---|
| **Live site** | https://uno-mas-site-builder.lovable.app | Published. Hosting still on Lovable (DNS cutover to unomastacoshop.com pending). |
| **Lovable editor** | https://lovable.dev/projects/78c4ac75-6325-4f38-a44b-278bb2194cf2 | Project `uno-mas-site-builder`. Stack: TanStack Start + Tailwind + shadcn. |
| **Supabase** | project `coandmppuqqzcbbhcien` | Source of truth for menu, hours, `site_content`, `assets`, `event_inquiries`. Publishable key is public/safe. |
| **Cloudinary** | cloud `drxrfyq9i` | Image CDN. Website photos live under `uno-mas/website/...`. |
| **Instagram feed** | Behold feed `https://feeds.behold.so/7d1MKXgymEKVVzqlCIoS` | Powers the homepage Phone section. Auto-updates. Filter is Reels/videos. |
| **Analytics** | GTM `GTM-T6L25CLD` · GA4 `G-YXKMDL0KF2` · Meta Pixel `1737601003250529` | GTM installed site-wide; events listed below. |

---

## Current state of the site (all DONE + published)

**Foundation & SEO**
- GTM installed site-wide with conversion events: `reserve_table_click`, `phone_click`, `directions_click`, `event_inquiry_view`, `cantina_club_signup`, `social_follow_click` (split phone_header / below_phone), `reel_play`, `reel_unmute`.
- Footer rebuilt with correct hours (Sun–Mon closed · Tue–Thu 11–9 · Fri–Sat 11–10), address+map, click-to-call, both emails, socials, all nav links.
- Per-page SEO titles + meta descriptions; Restaurant + Menu JSON-LD; `llms.txt`; sitemap; robots.
- **OG/social images are now dynamic** per page (resolve from each page's hero via Cloudinary, sized 1200×630). The old broken/screenshot OG images are gone.
- 301 redirects: `/catering → /private-events`, `/menu/lunch-dinner → /menu`.

**Mobile / UX / motion**
- Sticky mobile CTA bar (Reserve · Menu · Call · Directions).
- Scroll-reveal animations, Ken Burns hero, card hovers — all respect reduced-motion.
- Hero-video slot wired: upload an approved video tagged `role:hero-video` and the homepage hero becomes an ambient muted loop automatically.

**Copy (owner-reviewed via the review board, all applied)**
- Homepage: social-proof strip removed; venues header = "The Food Is Serious. The Vibe Is Not."; Patio card = "Soak Up Spokane Summers…"; dinner feature = "The dinner Spokane didn't see coming."; Cantina Club simplified (107% stat removed — interim copy, see Open Items).
- Menu hub hero "The Menus"; dinner reserve CTA "Your table's waiting."; lunch supporting copy + Build-Your-Own-Taco; brunch "Sunday brunch is coming." (coming-soon + email capture).
- Reservations hero + private-events cross-sell; About hero "Started with tacos. Didn't stop there."; **team section deleted**; Contact action cards; Fiesta Box hero + order CTA.
- Mezzanine hero "The room for the nights that matter." (events-forward).

**Forms & integrations**
- Private events page now embeds the **real Toast lead form** (catering pipeline). Supabase `event_inquiries` table + server fn remain in code as backup.
- Brunch + footer Klaviyo "Cantina Club" capture (list `TcwW8y`).

**Instagram section (homepage) — "The Phone" concept**
- Phone centerpiece plays reels; **plays once then auto-rotates** to the next reel (flip transition). Pink prev/next arrows; tap = sound toggle.
- Floating polaroids + brand sticker chips (GET A LITTLE LOST / TACOS & TEQUILA / ¡UNO MÁS!), parallax-clamped so they're never hidden behind the phone.
- "FROM OUR INSTAGRAM" kicker, on-phone @unomastacoshop identity bar with Follow pill, and a primary pink "Follow @unomastacoshop" button below. Falls back to testimonials if the feed is unavailable.

**Photography (from the iPhone shared album, 2026-06-15)**
8 clean shots uploaded to Cloudinary (`uno-mas/website/...`), tagged, and wired into Supabase `assets` — now live in these slots:
- `role:hero-cantina` + `role:venue-cantina` → TACOS-neon cantina interior (homepage hero)
- `role:hero-about` → warm wide cantina establishing shot
- `role:hero-cocktails` → house margarita on the bar (cocktails page)
- `role:exterior` → B&W Monroe storefront
- `role:venue-patio` → patio at dusk
- `role:hero-dinner` + `uno-mas-feast` → the Feast held by the team (now on the dinner Feast callout)
- plus 2 supporting cantina interiors (UNO MÁS neon bar, turquoise/pink dining)

**Earlier asset recovery (context):** A May Cloudinary reorg had 404'd 126 of 187 image URLs. Those were remapped/archived; the resolver falls back gracefully. The 8 new uploads replaced the interim placeholders on the key heroes.

---

## 🔴 OPEN / NEXT UP (what's NOT done)

1. **Interior construction "buildout" photos — IN FLIGHT, not yet uploaded.** Owner flagged ~67 files (named with "website") in `02_PHOTO_LIBRARY/.../UM - Photos - Monroe Buildout - Interior Construction/`. Identified but NOT processed. Mix of .jpeg/.jpg/.HEIC — **HEIC files need conversion** before upload. Decide where they go (a "buildout/our story" gallery? the About page?) then optimize → Cloudinary → tag → Supabase. *(This was the last thing in progress when the prior chat capped.)*
2. **Mezzanine photos — TOP PRIORITY, still zero.** The /mezzanine page uses the cantina shot as a branded fallback. The album had no clean Mezzanine room shot. Needs a dedicated shoot or a dig through other libraries for the leather-lounge/fireplace/bar.
3. **Team headshots.** Team section was deleted from /about. If it returns, it needs real photos. (3 unidentified candid portraits already sit in Cloudinary `uno-mas/team-uploads` — could be tagged if identified.)
4. **Cantina Club copy guidelines.** Interim copy is live (107% stat removed). Owner to finalize club voice/rules, then a focused copy pass.
5. **GTM verification.** Confirm the conversion events fire in GTM Preview mode (can't be verified from outside the container).
6. **Test the Toast form + Klaviyo capture** end-to-end once.
7. **Hero-video slot** is wired and empty — drop one short ambient clip (tag `role:hero-video`) from the 340 album videos (untouched) and the homepage goes to video.
8. **Birria** has no photo bound to its menu slug.
9. **DNS cutover** Squarespace → Lovable/Netlify hosting at unomastacoshop.com — still pending; see `LAUNCH-READINESS-CHECKLIST.md`.

---

## How asset uploads work (repeatable recipe)

The website resolves image slots by querying Supabase `assets` for `role:*` tags. To add a photo:
1. Optimize (≈1920px, q82, strip EXIF; convert HEIC→JPG first).
2. Stage to the public Supabase Storage bucket `approved-assets` (temporary scoped anon policy), get the public URL.
3. Cloudinary `upload-asset` fetches that URL into `uno-mas/website/<area>` with `role:` + descriptor tags.
4. Insert an `assets` row (url, cloudinary_secure_url, tags, status='approved', is_archived=false, suggested_alt_text).
5. Publish the Lovable project; the slot updates — no code change.
*(The Cloudinary connector can't read local files directly — hence the Supabase-staging hop. Temporary upload policy is dropped after.)*

---

## Useful reference docs (Marketing HQ)
- `UNO-MAS-MASTER-REFERENCE.md` — canonical brand/ops facts (address, hours, menu, voice, IDs).
- `uno-mas-website-backlog.md`, `LAUNCH-READINESS-CHECKLIST.md` — pre-existing project tracking.
- `uno-mas-website-copy-review-board.html` — the interactive copy review tool (re-export decisions anytime for a new copy pass).
- `uno-mas-reels-section-concepts.html` / `uno-mas-phone-and-wall-variations.html` — IG section concept mockups.
- `UNO-MAS-WEBSITE-QA-REPORT-2026-06-10.md` — launch QA snapshot.

---

*Keep this file current as the canonical website status. One session at a time — everything you need is here plus the live systems above.*
