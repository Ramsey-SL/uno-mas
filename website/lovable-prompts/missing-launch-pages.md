# Lovable Prompt — Missing Launch Pages + Redirects + SEO Lite (paste into Lovable chat)

**Project:** uno-mas-site-builder
**Date:** 2026-05-26
**Scope:** Build the remaining pages from the Squarespace site that the new Lovable site is missing. Add the 301 redirect for `/catering` → `/private-events`. Implement launch-essential SEO (basic schema, sitemap, robots.txt, 404 page). This is the **final build prompt before DNS cutover.**

---

## PASTE BELOW THIS LINE INTO LOVABLE

Build three new pages and add launch-essential SEO infrastructure. We're preparing to replace the current Squarespace site at unomastacoshop.com with this Lovable build via DNS cutover.

Use the same lighter visual treatment as the rest of the site: cream `#fafaf7` body, near-black `#1a1a1a` text, brand pink `#E22690` accents, warm-dark hero bands. Antonio Bold for headlines, Montserrat for body.

---

## PAGE 1: /now-hiring

### Hero band
- Kicker: "Now Hiring"
- Headline (Antonio Bold, white on warm-dark hero): **"GOOD PEOPLE. GOOD WORK. GOOD PAY."**
- Subhead: "Uno Más is hiring — front and back of house. If you take your craft seriously and work well with others, we want to talk."

### Section 1 — Why work here
2-column on desktop, 1-column on mobile.

Left column (body copy):
> We run a full lunch and dinner program at 2020 N Monroe — elevated food, a serious bar, and a team that actually functions like one.
>
> We pay competitively based on experience. Every role — front and back — is part of the tip pool. That's not common. It's intentional. We believe good service is a team effort, and we compensate everyone accordingly.

Right column: image from `role:hero-cantina` or `role:venue-cantina`.

### Section 2 — Open positions (callouts)
3-up card row with role categories. (We don't need to list every specific opening; the application form handles that.)
- **Front of House** — Servers, bartenders, host staff
- **Back of House** — Line cooks, prep, dishwashers
- **Events / Mezzanine** — Event coordinator support

### Section 3 — Apply
Embedded Google Form for applications. Use this exact URL (it's the same form on the Squarespace site):
```
https://docs.google.com/forms/d/e/1FAIpQLSdwxSoI-iurfb1HYtMX7HzfEYPH1yEXVxjdbaY-q1o6twNuzQ/viewform?embedded=true
```

Iframe height 1200px, no border. Mobile responsive.

Below the form, fallback text: "Issues with the form? Email tacos@unomastacoshop.com with your résumé and the role you're interested in."

### SEO
- `<title>`: "Jobs at Uno Más — Now Hiring in Spokane | Uno Más Tacos & Tequila"
- meta description: "Modern Mexican restaurant on Monroe is hiring front and back of house. Tip pool for everyone. Apply at Uno Más in Spokane."
- og:image: `role:hero-cantina`

---

## PAGE 2: /fiesta-box

### Hero band
- Kicker: "To-Go · Take It Home"
- Headline (Antonio Bold, white on warm-dark hero): **"TACO FIESTA BOX."**
- Subhead: "Everything you need for an epic taco night at home or on the go."
- Primary CTA button (pink `#E22690`): "Order A Fiesta Box" → `https://order.toasttab.com/online/uno-mas-taco-shop-2020-n-monroe-st-suite-c` (open in new tab)

### Section 1 — What you get
Cream background section. Centered content. List with kicker.

Headline: "What you get"

```
🌮 10 fresh 4" corn tortillas
🔥 Your choice of protein (Steak, Carnitas, Chicken Tinga, or Barbacoa)
🍋 Lime wedges
🌶 House salsa
🍚 Cilantro lime rice & black beans
🌿 Chopped cilantro & onion
```

Below the list:
"Want the full spread? Add our Chip & Dips Trio or Margaritas To-Go at checkout."

CTA button below: "Order A Fiesta Box" (same URL)

### Section 2 — Perfect for
4-up grid:
- Busy weeknight dinners
- Game day gatherings
- Birthday parties
- "I don't feel like cooking" nights

### Section 3 — Bottom CTA band
Dark `#1a1a1a` band:
- Headline: "WE'VE GOT YOU."
- CTA: "Order A Fiesta Box"

### Image
Use any asset tagged `role:menu-tacos` or `category:tacos` for the hero. Fallback: `role:hero-lunch`.

### SEO
- `<title>`: "Taco Fiesta Box — Order Online | Uno Más Spokane"
- meta description: "10 tortillas, your choice of protein, sides, and fixings. Order Uno Más's Taco Fiesta Box for pickup in Spokane. Perfect for taco night at home."
- og:image: Fiesta Box image if available, otherwise `role:hero-lunch`
- JSON-LD: `Offer` schema with price (if known) + availability

---

## PAGE 3: /privacy-policy

### Hero (tight, not full-bleed)
- Kicker: "Legal"
- Headline (Antonio Bold, near-black on cream): **"PRIVACY POLICY."**

### Body
Single column, max-width 720px, body font Montserrat at ~15px line-height 1.7.

Use this approved copy (adapted from a standard restaurant template):

```markdown
**Last updated: 2026-05-26**

Uno Más Tacos & Tequila ("Uno Más," "we," "us," or "our") respects your
privacy. This Privacy Policy describes how we collect, use, and protect
information when you interact with our website unomastacoshop.com.

## Information we collect
When you visit our site, make a reservation, sign up for our email list,
or fill out a contact form, we may collect:
- Your name, email address, and phone number
- Reservation details (date, party size, special requests) via our
  reservation partner Resy
- Order details if you place a takeout or catering order via Toast
- Standard website analytics data (pages viewed, time on site, device
  type, approximate location) via Google Analytics and Meta Pixel

## How we use it
- To respond to your inquiries and confirm reservations
- To send marketing emails or SMS if you've opted in (you can unsubscribe
  at any time)
- To improve our website and understand what's working
- To run paid advertising on Meta and Google, including showing ads to
  visitors who've interacted with our site

## Third-party services
We share limited data with the following partners as needed to operate
our business:
- **Resy** — reservation management
- **Toast** — point-of-sale, online ordering, and loyalty program
- **Klaviyo** — email and SMS marketing
- **Google Analytics + Google Ads** — website analytics and advertising
- **Meta (Facebook/Instagram)** — advertising and retargeting

Each of these has its own privacy practices. We do not sell your data.

## Your choices
- **Unsubscribe** from marketing email or SMS at any time using the link
  in our messages
- **Cookies and tracking** — you can disable cookies in your browser
  settings or opt out of personalized advertising
- **Data requests** — email tacos@unomastacoshop.com to request access
  to or deletion of your personal information

## Contact
Questions about this policy?
Email: tacos@unomastacoshop.com
Phone: (509) 960-7989
Address: 2020 N Monroe St, Suite C, Spokane, WA 99205
```

### SEO
- `<title>`: "Privacy Policy | Uno Más Tacos & Tequila"
- meta description: "How Uno Más collects, uses, and protects your information."
- robots: `noindex, follow` (we don't want the privacy policy ranking in search results, but link equity should pass through)

---

## 301 REDIRECT: /catering → /private-events

Add a permanent 301 redirect from `/catering` to `/private-events` so the Squarespace URL `unomastacoshop.com/catering` doesn't 404 after DNS cutover. This is the only old URL that needs a redirect (other Squarespace URLs map 1:1 to new URLs).

If using Netlify, add to `netlify.toml`:
```toml
[[redirects]]
  from = "/catering"
  to = "/private-events"
  status = 301
  force = true
```

If using a React Router setup, add the redirect at the route level.

---

## LAUNCH SEO LITE — implement these site-wide

### `robots.txt` at root
```
User-agent: *
Allow: /
Sitemap: https://unomastacoshop.com/sitemap.xml
```

### `sitemap.xml` at root
Auto-generate from all routes. Static is fine for v1. Include:
- `/`
- `/menu`
- `/menu/dinner`
- `/menu/lunch`
- `/menu/cocktails`
- `/menu/brunch` (if it exists)
- `/about`
- `/mezzanine`
- `/private-events`
- `/reservations`
- `/contact`
- `/now-hiring`
- `/fiesta-box`
- (Skip `/privacy-policy` — noindex)

Each entry: `<priority>` 1.0 for /, 0.8 for menu pages, 0.6 for others.
Each entry: `<changefreq>` weekly for /, monthly for others.

### Custom 404 page (`/404` or fallback route)
- Hero band similar to other pages
- Headline: "GOT A LITTLE TOO LOST."
- Subhead: "This page doesn't exist. Wander back to one of these:"
- Card grid linking to: `/menu/dinner`, `/menu/lunch`, `/mezzanine`, `/`
- Same footer as other pages

### JSON-LD basic schema (add to `<head>` of `/`)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Uno Más Tacos & Tequila",
  "alternateName": ["Uno Más", "Uno Mas"],
  "url": "https://unomastacoshop.com",
  "telephone": "+1-509-960-7989",
  "email": "tacos@unomastacoshop.com",
  "image": "https://res.cloudinary.com/drxrfyq9i/image/upload/20260125_UM_VENUE_InteriorDownstairsBar_FINAL_mb6tuz",
  "priceRange": "$$",
  "servesCuisine": ["Mexican", "Latin American", "Tacos"],
  "acceptsReservations": "True",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2020 N Monroe St, Suite C",
    "addressLocality": "Spokane",
    "addressRegion": "WA",
    "postalCode": "99205",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 47.6764702,
    "longitude": -117.4263699
  },
  "hasMap": "https://www.google.com/maps/search/?api=1&query=2020+N+Monroe+St+Suite+C+Spokane+WA+99205",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday","Wednesday","Thursday"],
      "opens": "11:00",
      "closes": "21:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Friday","Saturday"],
      "opens": "11:00",
      "closes": "22:00"
    }
  ],
  "sameAs": [
    "https://www.instagram.com/unomastacoshop",
    "https://www.tiktok.com/@unomastacosandtequila",
    "https://www.facebook.com/UnoMasTacoShop/"
  ]
}
</script>
```

### Per-page OG images
Every page should have its own `<meta property="og:image">` pointing to the page-specific Cloudinary URL (not the default Lovable preview). Pull via `role:hero-{page}` tag where available.

---

## ACCEPTANCE CRITERIA

After this build:
- `/now-hiring` page exists with hero, body, Google Forms embed, and renders cleanly mobile + desktop
- `/fiesta-box` page exists with hero, item list, Toast online-ordering CTA (opens new tab), and "Perfect for" grid
- `/privacy-policy` page exists with hero + body content as written
- `/catering` URL redirects (301) to `/private-events` (no 404)
- `robots.txt` exists at root pointing to sitemap
- `sitemap.xml` exists at root listing all 13 indexed routes
- Custom 404 page renders on unknown routes
- `/` (homepage) has the full Restaurant JSON-LD schema in `<head>`
- Every page has a unique `<title>` and `<meta description>`
- Every page has a page-specific `<meta og:image>` (no more Lovable default preview)

Out of scope: deeper schema (Menu, MenuItem, FAQPage, Event, BreadcrumbList) — deferred to Phase 2.
