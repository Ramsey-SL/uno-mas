# Uno Más — Website Tracking Plan (Measurement Map)

_Last updated: 2026-08-11 · Owner: Ramsey · Purpose: single source of truth for what we measure on unomastacoshop.com, ahead of the Google Search + TikTok ads launch._

Audited against live production HTML and the Lovable source (project `78c4ac75-6325-4f38-a44b-278bb2194cf2`) on 2026-08-11.

---

## 1. The stack — CANONICAL TAG IDs

> **This table is the source of truth. Don't go digging through ad platforms again — add any new ID here the day it's created.**
> Everything below is a public, client-side identifier (visible in page source). **No API keys, secrets or tokens belong in this file** — those live in Lovable project secrets / Supabase.

| Platform | ID | Status |
|---|---|---|
| GA4 | Measurement ID `G-YXKMDL0KF2`<br>Property ID `523092931`<br>Account ID `383242412` | ✅ live on all pages — verified 2026-08-11 as the only GA4 tag on the site. Measurement ID is the one used in code; Property/Account IDs are for GA4 Admin, the Data API and BigQuery links. |
| Google Ads | `AW-18385019415` | ✅ **LIVE 2026-08-11** — base tag only. Conversion actions still need `send_to` labels (§6). |
| Meta Pixel | `1737601003250529` | ✅ live on all pages (+ noscript fallback) |
| TikTok Pixel | `D9U04BRC77UDGUKDT76G` | ✅ **LIVE 2026-08-11** — base pixel, SPA pageviews, and full event mapping (§4). |
| Klaviyo | ~~`UjAfaJ`~~ | ⛔ **removed 2026-08-11.** Klaviyo retired org-wide (Aug 2026); bulk email/SMS is now Toast Marketing. Script, privacy-policy entry and all references stripped. |
| Meta Conversions API | — | ❌ not implemented (browser-only signal) |
| Google Tag Manager | — | ⛔ **deliberately not used** (owner decision, 2026-08-11). `trackEvent()` still pushes to `window.dataLayer`; nothing consumes it. Harmless — GA4 is fed directly via `gtag` — and it leaves the door open if we ever add GTM. |

**Ad + analytics accounts**

| Thing | Value |
|---|---|
| Google Ads account | `164-990-7395` |
| Google Search Console | Domain property `sc-domain:unomastacoshop.com` (owner: ramsey@strategylabs.us) |
| Google Business Profile | Place ID `ChIJ9UKRJPIZnlQRL0oaKlM3vIk` |
| TikTok handle | @unomastacosandtequila · Instagram @unomastacoshop · Facebook /UnoMasTacoShop |

**Destination URLs the conversions point at** (all off-domain — this is why click-out events are our conversion proxies)

| Action | URL |
|---|---|
| Loyalty signup | `https://www.toasttab.com/uno-mas-taco-shop-2020-n-monroe-st-suite-c/rewardsSignup` |
| Online ordering (Fiesta Box item) | `https://order.toasttab.com/online/uno-mas-taco-shop-2020-n-monroe-st-suite-c/item-fiesta-pack_8752fc0c-59e7-4b60-916a-fdac463e2992` |
| Gift cards | `https://order.toasttab.com/egiftcards/uno-mas-taco-shop-2020-n-monroe-st-suite-c` |
| Reservations | `https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila` |
| Event/catering lead form (Toast iframe) | `https://www.toasttab.com/invoice/lead?rx=4d40708e-c91d-4841-a73c-a20718867eb1&ot=0c3ac131-b2fe-4d4f-b8b2-794229325e74&form=1` |
| Job application (Google Form) | `https://docs.google.com/forms/d/e/1FAIpQLSdwxSoI-iurfb1HYtMX7HzfEYPH1yEXVxjdbaY-q1o6twNuzQ/formResponse` |

### Where the code lives

| File | What it does |
|---|---|
| `src/routes/__root.tsx` | Deferred third-party loader — synchronous fbq/gtag/ttq stubs, loads Meta + GA4 + Google Ads + TikTok immediately for ad traffic, else on first interaction or a 2.5 s fallback. Also the Meta/TikTok SPA pageview component. |
| `src/lib/track.ts` | `trackEvent(name, params)` — the single fan-out to dataLayer, Meta (`metaPixelMapping`), GA4, and TikTok (`tiktokMapping`). |

### Raw snippets (reference only — the site does NOT use these verbatim)

The site loads all four tags through the deferred loader in `__root.tsx`, **not** as standalone `<script>` blocks. These are kept only so the IDs and canonical shapes are recorded:

```html
<!-- Google tag — serves BOTH GA4 and Google Ads from one gtag.js load -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YXKMDL0KF2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-YXKMDL0KF2');   // GA4
  gtag('config', 'AW-18385019415'); // Google Ads
</script>

<!-- Meta Pixel -->
<script>
  !function(f,b,e,v,n,t,s){/* standard Meta snippet */}(window,document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '1737601003250529');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=1737601003250529&ev=PageView&noscript=1"/></noscript>

<!-- TikTok Pixel -->
<script>
  !function(w,d,t){/* standard TikTok snippet */}(window, document, 'ttq');
  ttq.load('D9U04BRC77UDGUKDT76G');
  ttq.page();
</script>
```

**How events flow:** one helper, `src/lib/track.ts` → `trackEvent(name, params)` fans out to (1) `dataLayer.push`, (2) Meta Pixel via a curated name→standard-event map, (3) GA4 via `gtag('event', name, params)`. Add a new event once, it lands everywhere.

**Ad-traffic loading (fixed 2026-08-11, commit `0786373f`):** if the URL carries `gclid`/`gbraid`/`wbraid`/`fbclid`/`ttclid`/`msclkid`/`utm_*`, all tags load **immediately** — a bouncing paid click still fires a pageview and captures the click ID. Organic traffic keeps the deferral, now with a 2.5 s fallback (was 6 s).

**Historical note:** before 2026-08-11 every tag waited for the first interaction or a 6 s timeout, so a paid click that bounced early recorded nothing at all. Fixed above — keep the ad-param check in place through any future perf work.

---

## 2. Conversion tiers

What we optimize toward, in order of business value (highest-margin channels first, per CLAUDE.md: dinner, private events, catering).

**Tier 1 — Primary conversions** (bid on these; mark as GA4 key events; import to Google Ads; Meta/TikTok optimization events)
1. `inquiry_submit` — private event / catering lead completed
2. `loyalty_signup_click` — Cantina Club signup started
3. `reserve_table_click` — Resy reservation started
4. `order_click` — Toast online order started
5. `giftcard_buy_click` — gift card purchase started

**Tier 2 — Secondary conversions** (report on; use for audiences/remarketing; secondary optimization)
- `inquiry_open`, `loyalty_cta_click`, `phone_click`, `email_click`, `directions_click`, `tickets_click`, `application_submit`

**Tier 3 — Engagement signals** (diagnostics + audience building only, never a bid target)
- `menu_tile_click`, `menu_tab_click`, `menu_see_full_click`, `event_inquiry_view`, `social_follow_click`, `social_reel_click`, `brunch_cta`, `nav_click`

---

## 3. The event map — page by page

Legend: ✅ implemented · ⚠️ implemented with a defect · ❌ missing

### Global (every page — header, footer, sticky bar)

| Element | Event | Params | Tier | Status |
|---|---|---|---|---|
| Header "Reserve a table" | `reserve_table_click` | `location: "header"` | 1 | ✅ |
| Mobile drawer "Reserve a table" | `reserve_table_click` | `location: "mobile-drawer"` | 1 | ✅ |
| Header/drawer "Join Rewards" | `loyalty_cta_click` | `location: "header" \| "mobile-drawer"` | 2 | ✅ |
| Sticky mobile bar — Reserve | `reserve_table_click` | `location: "sticky_mobile"` | 1 | ✅ |
| Sticky mobile bar — Call | `phone_click` | `location: "sticky_mobile"` | 2 | ✅ |
| Sticky mobile bar — Directions | `directions_click` | `location: "sticky_mobile"` | 2 | ✅ |
| Sticky mobile bar — Menu | `nav_click` | `location: "sticky_mobile"`, `label` | 3 | ✅ |
| Footer address + phone + Get Directions | `directions_click` / `phone_click` | `location: "footer" \| "footer_button"` | 2 | ✅ |
| Footer email links (tacos@ / karissa@) | `email_click` | `location: "footer"`, `inbox` | 2 | ✅ |
| Footer Instagram / Facebook | `social_follow_click` | `network`, `location: "footer"` | 3 | ✅ |
| Email/SMS signup | `email_signup` | `source` | 2 | ⛔ n/a on-site — Klaviyo removed Aug 2026. List growth now runs through Toast (Cantina Club). If we ever add an on-site capture form, wire `email_signup` to it. |

### `/` Homepage

| Element | Event | Tier | Status |
|---|---|---|---|
| Fiesta Box teaser → Toast | `order_click` (`location: "home_fiesta_teaser"`) | 1 | ✅ |
| "See what's inside" | `nav_click` | 3 | ✅ |
| Menu collection tiles | `menu_tile_click` (`tab`, `location`) | 3 | ✅ |
| Cantina Club band → `/cantina-club` (both CTAs) | `loyalty_cta_click` (`location: "home_band"`, `label`) | 2 | ✅ |
| Instagram follow / reel clicks | `social_follow_click` / `social_reel_click` | 3 | ✅ |
| Love Island ticket CTA | `tickets_click` | 2 | ✅ |
| Brunch banner + feature CTAs | `brunch_cta` / `brunch_feature_cta` | 3 | ✅ |
| Visit-section map link | `directions_click` (`location: "home_visit"`) | 2 | ✅ |

### `/cantina-club` — loyalty (Tier 1, currently invisible)

| Element | Event | Tier | Status |
|---|---|---|---|
| Hero "Join free — get $10" → Toast `rewardsSignup` | `loyalty_signup_click` (`location: "cantina_club_hero"`) | 1 | ✅ **live** (+ opens in new tab) |
| Closing "Join the Cantina Club" → Toast | `loyalty_signup_click` (`location: "cantina_club_closer"`) | 1 | ✅ **live** (+ opens in new tab) |
| "See how it works" anchor | `nav_click` | 3 | ✅ |

> ✅ Both Toast links now carry `target="_blank" rel="noopener noreferrer"`, so the session survives the click-out.

### `/private-events` — highest-margin lead path

| Element | Event | Tier | Status |
|---|---|---|---|
| Hero "Inquire" | `inquiry_open` (`source: "/private-events"`) | 2 | ✅ |
| 4 × room card "Inquire →" | `inquiry_open` | 2 | ✅ now sends `placement` (`hero` / `room_card` + card title / `packages` / `inquiry_section`) |
| Packages "Plan Your Event" | `inquiry_open` | 2 | ✅ |
| Inquiry section scrolled into view | `event_inquiry_view` | 3 | ✅ |
| **Form actually submitted** | `inquiry_submit` | **1** | ❌ **not measurable.** The dialog embeds a cross-domain Toast lead iframe — we cannot observe the submit. See §5. |
| `karissa@` mailto | `email_click` (`location: "private_events"`) | 2 | ✅ |

### `/mezzanine`

| Element | Event | Tier | Status |
|---|---|---|---|
| Hero "Inquire", 3 × package "Book…", band "Inquire" | `inquiry_open` (`source: "/mezzanine"`) | 2 | ✅ now sends `placement` (`hero` / `package_<slug>` / `band`) — shows which price point the ads sell |
| Phone + `karissa@` in the contact block | `phone_click` / `email_click` (`location: "mezzanine_contact"`) | 2 | ✅ |

### `/catering`

| Element | Event | Tier | Status |
|---|---|---|---|
| 3 × "Request a catering quote" | `inquiry_open` (`source: "/catering"`) | 2 | ✅ |
| **Quote form submitted** | `inquiry_submit` | **1** | ❌ not measurable (same Toast iframe issue) |

### `/fiesta-box`

| Element | Event | Tier | Status |
|---|---|---|---|
| Hero + closer "Order a Fiesta Box" | `order_click` (`location: "fiesta_box_hero" \| "fiesta_box_closer"`) | 1 | ✅ |

### `/giftcards`

| Element | Event | Tier | Status |
|---|---|---|---|
| "Buy a Gift Card" → Toast eGift | `giftcard_buy_click` (`location: "giftcards_hero"`) | 1 | ✅ |
| In-person directions link | `directions_click` (`location: "giftcards"`) | 2 | ✅ |

### `/menu`

| Element | Event | Tier | Status |
|---|---|---|---|
| Daypart tabs (dinner/lunch/cocktails) | `menu_tab_click` | 3 | ✅ |
| "See full menu" | `menu_see_full_click` | 3 | ✅ |
| **Order online CTA** | `order_click` | 1 | ❌ **doesn't exist.** There is no Toast online-ordering CTA anywhere on the site except the single Fiesta Box item link. Ordering-intent Search ads have no landing path — decide whether to add one. |

### `/now-hiring`

| Element | Event | Tier | Status |
|---|---|---|---|
| Native application form submit | `application_submit` (`location: "/now-hiring"`) | 2 | ✅ — this is the one true server-confirmed form submit on the site |

---

## 4. Platform event mapping

One `trackEvent()` call → four platforms. Meta mapping lives in `metaPixelMapping()` and TikTok in `tiktokMapping()`, both in `src/lib/track.ts`. **All rows below are live as of 2026-08-11.**

| Our event | GA4 | Key event? | Meta Pixel | TikTok |
|---|---|---|---|---|
| `inquiry_submit` | `inquiry_submit` | ✅ | `Lead` | `SubmitForm` |
| `inquiry_open` | `inquiry_open` | — | `Lead` *(currently; demote to `ViewContent` once `inquiry_submit` exists)* | `ClickButton` |
| `loyalty_signup_click` | `loyalty_signup_click` | ✅ | `CompleteRegistration` | `CompleteRegistration` |
| `reserve_table_click` | `reserve_table_click` | ✅ | `Schedule` | `ClickButton` |
| `order_click` | `order_click` | ✅ | `InitiateCheckout` | `InitiateCheckout` |
| `giftcard_buy_click` | `giftcard_buy_click` | ✅ | `InitiateCheckout` | `InitiateCheckout` |
| `tickets_click` | `tickets_click` | ✅ | `InitiateCheckout` | `InitiateCheckout` |
| `phone_click` | `phone_click` | ✅ | `Contact` | `Contact` |
| `email_signup` | `email_signup` | ✅ | `Subscribe` | `Subscribe` |
| `directions_click` | `directions_click` | — | `FindLocation` *(not yet mapped)* | `ClickButton` |
| `application_submit` | `application_submit` | — | `SubmitApplication` | `SubmitForm` |
| `email_click` | `email_click` | — | `Contact` | `Contact` |
| `menu_tile_click` / `menu_tab_click` / `menu_see_full_click` | same | — | `ViewContent` | `ViewContent` |
| `social_follow_click` / `social_reel_click` | same | — | `Follow` (custom) | — |
| `nav_click` / `brunch_cta` / `event_inquiry_view` | same | — | — | — |

**Naming rules:** `snake_case`, verb-last (`*_click`, `*_submit`, `*_view`). Every event carries `location` (where on the page) and, where a component repeats, `placement`. Never rename a live event — add a new one and retire the old after 30 days of overlap.

---

## 5. The measurement gap that matters most

**Event and catering leads — our two highest-margin paths — cannot be measured as conversions.** `InquireDialog` embeds a cross-domain Toast lead-capture iframe, so a submit is invisible to us. Everything we can see is "opened the dialog," which will inflate lead counts and mistrain both ad platforms.

The repo already contains the alternative: a Supabase-backed `event_inquiries` table plus `src/lib/inquiries.functions.ts` and a Resend notification to Karissa. Swapping the dialog to that native form gives us a real `inquiry_submit`, a server-side record we can use for offline conversion import, and first-party lead data. **Recommended before spending meaningful budget on event/catering keywords.**

---

## 6. Platform configuration checklist (outside the code)

**GA4**
- [ ] Mark the Tier 1 events + `phone_click` and `email_signup` as **key events** (Admin → Events)
- [ ] Confirm Enhanced Measurement page_view on history change (SPA routes) — Meta's SPA pageview is handled in `__root.tsx`; GA4 relies on Enhanced Measurement
- [ ] Define audiences: menu viewers, inquiry openers who didn't submit, loyalty non-signups

**Google Ads** (account `164-990-7395`, tag `AW-18385019415`)
- [x] Base `AW-` tag installed (2026-08-11) — gives auto-tagging/gclid capture + remarketing audiences
- [ ] **Create a conversion action per Tier 1 event** in Google Ads (Goals → Conversions → New → Website), then paste the resulting `send_to` labels here — they look like `AW-18385019415/AbC-D_efGhIjKlM`. Until these exist, the tag records audiences but zero conversions.
- [ ] Wire each label into `trackEvent()` so the matching event fires `gtag('event','conversion',{send_to:'AW-18385019415/<label>'})`
- [ ] Confirm auto-tagging is ON, and that the deferred-loader fix (§1) ships first — otherwise gclid-carrying sessions go unrecorded and conversions can't attribute back
- [ ] Set primary vs secondary conversion actions to match the Tier 1/Tier 2 split
- [ ] *(Alternative to labels: link GA4 → Google Ads and import the key events. Simpler, but 24–48 h delayed and slightly lossier.)*

**Conversion labels — fill these in as they're created**

| Event | Google Ads conversion action | `send_to` label |
|---|---|---|
| `inquiry_submit` | Event / catering lead | _TBD_ |
| `loyalty_signup_click` | Cantina Club signup | _TBD_ |
| `reserve_table_click` | Reservation started | _TBD_ |
| `order_click` | Online order started | _TBD_ |
| `giftcard_buy_click` | Gift card started | _TBD_ |
| `phone_click` | Phone call | _TBD_ |

**Meta**
- [ ] Custom conversions for `Lead` (split by `content_name`: mezzanine / private-events / catering)
- [ ] Consider Conversions API for iOS signal recovery (needs `event_id` dedup added to `trackEvent`)

**TikTok**
- [ ] Install base pixel (ID needed)
- [ ] Map the Tier 1 events above
- [ ] Consider Events API later, same dedup requirement

---

## 7. Implementation backlog (ordered)

1. ~~**Ad-click loader fix**~~ ✅ LIVE 2026-08-11 — — load tags immediately on `gclid`/`gbraid`/`wbraid`/`fbclid`/`ttclid`/`msclkid`/`utm_*`; fallback 6s → 2.5s. *Without this, everything below under-reports paid traffic — including the TikTok pixel we just installed.*
2. ~~**TikTok pixel + event mapping**~~ ✅ LIVE 2026-08-11
3. ~~**Google Ads base tag**~~ ✅ LIVE 2026-08-11 — **still needs conversion actions + `send_to` labels (§6)**
4. ~~**Loyalty tracking**~~ ✅ LIVE 2026-08-11 — `loyalty_signup_click` (Toast click-out, Tier 1) vs `loyalty_cta_click` (internal nav, Tier 2) kept separate so internal clicks never inflate the conversion
5. ~~**`placement` param + header Resy `location`**~~ ✅ LIVE 2026-08-11
6. **Native inquiry form** → real `inquiry_submit` (§5)
7. ~~**Small gaps**~~ ✅ LIVE 2026-08-11 — `email_click`, footer socials, homepage + giftcards directions, sticky menu `nav_click`
8. **Decide: online-ordering CTA** in header/menu/home, tracked as `order_click` — required if Search ads target ordering intent
9. *Optional later:* Meta CAPI + TikTok Events API with `event_id` dedup; offline conversion import from `event_inquiries`
