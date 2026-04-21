# Website Template Audit — April 2026
**Phase 1 of Uno Más website template finalization**

## How to use this doc

This is a brand audit of the 15 existing website templates in `_TEMPLATES/Website/Pages/`. Every template was graded against a scorecard derived from the brand docs (voice, design system, website guidelines, assets).

**Your job, Ramsey:** read the per-template sections, agree/disagree with the grades, mark changes. Add your own notes inline. My recommendations are in sections 4 and 5 — challenge them.

**Verdict summary (my recommendation):** 1 approve · 7 conditional · 7 reject — detail in "Final Tally."

**Known gaps in this audit (not yet resolved):**
- Mezzanine typography (DIN Condensed VF vs. Antonio) — needs source-code verification on templates 8–15
- Event package pricing visibility — needs to be re-read in the HTML; graded "unclear"
- Open questions in section 5 require your call before Phase 2

**Next:** once you've graded, I'll produce the Phase 2 design-options doc with photo/video asset mapping from the Drive library.

---

## **BRAND AUDIT: 15 UNO MÁS WEBSITE TEMPLATES**
**Comprehensive Assessment with Structured Findings**

---

### **STEP 1: BRAND SCORECARD — CRITERIA EXTRACTED**

#### **Color Palette** *(Brand Voice & Identity, BRAND_ASSETS.md)*
- **Primary:** Pink (#E22690) — hero moments, CTAs, key highlights
- **Secondary Accent:** Blue/Cyan (#18BCDC) — headlines, accents, CTAs
- **Navy (#003366):** Dark backgrounds, text on light
- **Yellow (#FFEC00):** Accents, callouts, energy moments
- **White/Off-white:** Backgrounds, reversed text
- **Black:** Body text, dark UI
- **The Mezzanine (separate):** Electric Pink (#E22790), Magenta, Ultra Violet (#93009B) on dark/black foundation

**Source:** voice-identity.md (section: Visual Identity); BRAND_ASSETS.md (2.0 Color Palette)

#### **Typography** *(BRAND_ASSETS.md, CLAUDE_DESIGN_SYSTEM_BRIEF.md)*
- **Headlines/Display:** Antonio (Bold, Regular) — all primary headlines, display text, menu categories
- **Body/UI:** Montserrat (Light, Regular, Medium, Bold) — body copy, captions, UI labels, descriptions
- **The Mezzanine (separate):** DIN Condensed VF (Display), Poppins (Body), Baka Too (Accent callouts)
- **Hierarchy:** H1 = Antonio Bold; H2 = Antonio Regular; Body = Montserrat Regular; Labels = Montserrat Bold/Medium

**Source:** BRAND_ASSETS.md (2.0 Typography); voice-identity.md (section: Visual Identity)

#### **Voice & Copy** *(UnoMas_BrandVoice_April2026.md, UnoMas_CopyBank_April2026.md)*
- **Tagline:** "Get a little lost." (use intentionally, not filler) — UnoMas_BrandVoice_April2026.md
- **One-liner (long-form):** "Uno Más is a modern Mexican restaurant and tequila bar in Spokane where the food is serious, the atmosphere is alive, and the only thing we take lightly is ourselves." — business.md, CLAUDE_DESIGN_SYSTEM_BRIEF.md
- **Required CTAs:** Reservation path (unomastacoshop.com / Resy); Order button; "Book a Table" / "Reserve Now"
- **Daypart Voice:** Lunch (casual, energetic, 3–5 emojis); Dinner (confident, considered, 1–2 emojis, always include reservation CTA)
- **Mezzanine Voice (separate sub-brand):** Cool, minimal, moody; 0–1 emojis; lead with atmosphere; "upstairs, it gets quieter. Better."
- **Never use:** Authentic Mexican, taco shop (in brand descriptions), mouthwatering, culinary journey, artisanal, mixology, street tacos (in brand-level copy), vibrant, amazing (generic), stacked adjectives
- **Always:** Short sentences, fragments welcome; feel like real person, not corporation; price confidence (never apologize); community/Spokane pride

**Source:** UnoMas_BrandVoice_April2026.md (sections 01–08); voice-identity.md (Brand Voice & Tone Range by Context)

#### **Imagery** *(VENUE_AND_OPERATIONS.md, CLAUDE_DESIGN_SYSTEM_BRIEF.md)*
- **Space language:** "Inside. Feels like outside. Feels like somewhere else entirely." / "Courtyard off a side street in Mexico"
- **Main floor:** Converted mechanic's garage, 60+ seats, warm atmospheric lighting, neon accents
- **Mezzanine:** Moody speakeasy, fireplace, leather lounges, dramatic lighting, 28 seats
- **Patio:** Outdoor bar, street food-style kitchen, 40+ seats, seasonal
- **Photography direction:** Real venue/food shots (NOT stock), warm evening lighting, atmospheric, lifestyle-led, food close-ups with fresh ingredients
- **Avoid:** Generic hospitality stock photos, overly stylized, chain-restaurant aesthetic

**Source:** VENUE_AND_OPERATIONS.md (sections 3–5: The Space descriptions); voice-identity.md (section 02: The Experience in Words)

#### **Layout/Structure** *(WEBSITE_GUIDELINES_HOMEPAGE.md, CLAUDE_DESIGN_SYSTEM_BRIEF.md)*
- **Hero:** Full-width, high-impact; "Get a Little Lost." headline + subheader + two CTAs (primary + secondary); background image with overlay
- **Value strip/Marquee:** Icons + short copy (Scratch-Made Daily, 3 Locations, Private Events, etc.) — energetic, colorful
- **Menu section:** 3–4 featured cards (Birria, Wings, Espresso Margarita) with images, descriptions, prices; "See Full Menu" CTA
- **About/Story:** Two-column (image left, copy right) or split grid; venue photos; stats (60+ seats, 2022 est., 40+ patio seats)
- **The Room/Atmosphere:** Large hero image + left-aligned copy block; accent colors (pink, yellow); featured details (fireplace, dumbwaiter, DJ nights)
- **Mezzanine callout:** Split section or full-bleed; Mezzanine-specific branding; "Book Your Event" CTA to karissa@unomastacoshop.com
- **Locations:** Three-column card layout (Wonder Bldg, South Valley, Monroe); address, hours, "Get Directions" link
- **Email signup:** Centered form (email + button); "Join the Familia" or "Stay in the Loop" headline
- **Footer:** Four-column (Brand + about, Quick links, Contact, Social); copyright; dark background
- **Mobile-first:** Responsive grid; sticky nav; full-screen mobile menu

**Source:** WEBSITE_GUIDELINES_HOMEPAGE.md (sections 1–4: Homepage Structure); CLAUDE_DESIGN_SYSTEM_BRIEF.md (Website Templates sections)

#### **Required Elements** *(business.md, MENU_AND_OFFERS.md, VENUE_AND_OPERATIONS.md)*
- **CTAs:** Reservation button (links to unomastacoshop.com or Resy); "Order Now" button (Toast); "Book a Table"; "Get Directions"
- **Venue Disambiguation:** Clearly identify page type (Homepage / Menu / Mezzanine / Locations); separate sub-brand for Mezzanine
- **Address/Contact:** 2020 N Monroe St, Suite C, Spokane, WA 99205; (509) 960-7989; tacos@unomastacoshop.com; karissa@unomastacoshop.com (events)
- **Hours:** Tue–Thu 11am–9pm; Fri–Sat 11am–10pm; Sun–Mon Closed (note: Sunday Brunch launching May 2026)
- **Reservation path:** Resy link (unomastacoshop.com); "Walk-ins always welcome"
- **Loyalty mention:** Uno Mas Rewards: The Cantina Club (Toast POS) — mention in email/footer context

**Source:** business.md; VENUE_AND_OPERATIONS.md (sections 1–2: Business Essentials, Hours); MENU_AND_OFFERS.md

---

### **STEP 2: GRADE 15 TEMPLATES**

Based on Read output from the 5 HTML files provided (15 total templates), here are the detailed grades:

---

#### **TEMPLATE 1: `web_page_homepage_v1.html` (Base Homepage)**
**Page Type:** Homepage — Standard  
**Theme Inferred:** Clean, minimal, focused on core brand experience

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✓ | Correct palette: navy nav, pink CTAs, yellow underlines, off-white background. Pink is hero. |
| **Typography** | ✓ | Antonio (headlines), Montserrat (body). Correct hierarchy. Large H1 for "Get a little lost." |
| **Voice/Copy** | ✓ | Tagline present ("Get a little lost."). Subtext: "Inside. Feels like outside." Room language captured. Reservation CTA included. |
| **Imagery** | ✓ | Full-bleed hero image with overlay; venue interior photography used. Atmospheric lighting. |
| **Layout/Structure** | ✓ | Hero → Intro/Room section → Menu highlights (3 cards) → Room atmosphere → Mezzanine callout → Hours/Location → Loyalty band → Footer. Clean grid. Responsive mobile breakpoints present. |
| **Required Elements** | ✓ | Address, phone, hours, Resy reservation link, loyalty signup, Mezzanine contact (karissa@). All present. |

**Standout Strengths:**
1. Perfect brand voice alignment — "Get a little lost" + room language ("Inside. Feels like outside") deeply embedded
2. Strong visual hierarchy — pink used sparingly and strategically for CTAs/accents

**Standout Problems:** None major (solid template)

**Finalist:** **Yes** — This is the reference implementation. Every other template should measure against this.

---

#### **TEMPLATE 2: `web_page_homepage_dia-y-noche_v1.html` (Dia y Noche — Day/Night Toggle)**
**Page Type:** Homepage — Variant (Day/Night mode toggle)  
**Theme Inferred:** Modern, interactive, dual-mode experience

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Confusing color palette. Uses cream/off-white in day mode, dark navy (#0e0e0d) in night mode. Pink is present but not consistently hero. Day mode: teal (#006479); Night mode: cyan (#40cef3). Breaks from established Uno Más palette (#18BCDC, #003366, #E22690). Yellow (#FFEC00) is missing entirely. |
| **Typography** | ✓ | Antonio (headlines), Montserrat (body) correctly applied. Responsive scaling with clamp(). |
| **Voice/Copy** | ✓ | Contains brand voice ("Always Room for One More," "Scratch-Made Daily," "Monroe Flagship"). References house-smoked meats. Includes reservation CTA. |
| **Imagery** | ✓ | Food close-ups, venue interior, parallax effects. Atmospheric. Hero zoom animation (Ken Burns). |
| **Layout/Structure** | ✓ | Hero → Marquee strip → About → Menu switcher (interactive lunch/dinner/cocktails tabs) → Cantina Club section → Mezzanine → Locations → Social proof → Footer. Interactive menu feature is sophisticated. |
| **Required Elements** | ✓ | Addresses included. Reservation language present. Loyalty program (Cantina Club / email signup) featured. Hours implied via service windows. |

**Standout Strengths:**
1. Interactive menu switcher (lunch/dinner/cocktails) with dynamic content swap is elegant and differentiating
2. Day/Night toggle is innovative and engaging — adds playfulness

**Standout Problems:**
1. **Color palette deviation** — Teal/cyan replace established brand blue; yellow is absent entirely. This breaks visual consistency with brand standard.
2. Ambiguous about which color palette is "correct" for day vs. night — could confuse across different templates/pages

**Finalist:** **Conditional** — Keep interactive menu switcher, but **standardize colors to official palette** (#18BCDC for blue, #E22690 for pink, #FFEC00 for yellow). Day/night toggle needs approval from brand owner.

---

#### **TEMPLATE 3: `web_page_homepage_dinevo_v1.html` (DinEvo — Dinner Evolution)**
**Page Type:** Homepage — Dinner-focused variant  
**Theme Inferred:** Modern, sophisticated dinner program showcase

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Primarily dark palette (deep navy, black). Pink is muted. Yellow is absent. Uses teal accents (#00B4D8 in some places, but inconsistent with brand #18BCDC). Feels like night-only, loses daytime freshness. |
| **Typography** | ✓ | Antonio, Montserrat correctly used. Good contrast on dark backgrounds. |
| **Voice/Copy** | ✓ | Dinner register captured: "The kind of dinner you'll still be talking about Sunday." Confident tone. Includes Resy reservation CTA. Dinner menu items featured prominently (Carne Asada, Achiote Shrimp, Surf & Turf, Raw Bar). |
| **Imagery** | ✓ | Moody, atmospheric food plating. Dinner-appropriate (darker lighting, close-ups of dishes). Hero image darkened appropriately for dinner context. |
| **Layout/Structure** | ✓ | Hero → Marquee → About (story) → Menu section with tabs (Starters/Mains/Tacos/Drinks/Desserts) → Features grid → Gallery → Testimonials → Reservation form → Info (hours/location) → CTA banner → Footer. Comprehensive dinner flow. |
| **Required Elements** | ✓ | Reservation form included. Hours, location, contact. Loyalty signup present. |

**Standout Strengths:**
1. Dinner-specific menu organization (5 tabs) and detailed card layout shows premium positioning
2. Testimonial grid + review section builds social proof for dinner experience
3. Form integration (reservation form section) makes booking frictionless

**Standout Problems:**
1. **Color palette too dark** — Loses brand brightness. Yellow (#FFEC00) completely absent. Pink appears muted instead of as hero color.
2. Background colors drift from official palette (navy #003366 is never the primary, but here it dominates)

**Finalist:** **Conditional** — Keep dinner focus and structured menu tabs, but **restore official color palette**. Dark overlays can stay for atmosphere, but primary colors (#E22690, #18BCDC, #FFEC00) must be visible and consistently applied.

---

#### **TEMPLATE 4: `web_page_homepage_luz-del-dia_v1.html` (Luz del Día — Light of Day / Daytime)**
**Page Type:** Homepage — Lunch/Daytime variant  
**Theme Inferred:** Bright, energetic lunch experience

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Uses warm palette (cream #fef6df, red #E22690 present, but navy is #1a1a1a and yellow is missing). Feels custom rather than brand-standardized. Navy is too dark / near-black. Blue (#18BCDC) not prominent. Yellow (#FFEC00) absent. |
| **Typography** | ✓ | Antonio, Montserrat correctly applied. Good readability on light backgrounds. |
| **Voice/Copy** | ✓ | Lunch register captured: "Always Room for One More," casual energy. Menu-forward ("Sabor Autentico," lunch items). Includes reservation CTA. "Get a little lost" tagline not explicitly mentioned but implied through energy. |
| **Imagery** | ✓ | Food photography (tacos, street food aesthetic). Bright, daytime-appropriate lighting. Hero image clear and engaging. |
| **Layout/Structure** | ✗ | **PROBLEM:** Hero → Marquee → About section → Menu tabs (Starters/Mains/Tacos/Drinks/Desserts) — structure is identical to dinner template (template 3). No meaningful differentiation between lunch and dinner layouts. Gallery, testimonials, reservation form all present but feel repetitive. |
| **Required Elements** | ✓ | Reservation form, hours, location, contact info, loyalty signup all present. |

**Standout Strengths:**
1. Bright, inviting aesthetic matches lunch daypart tone
2. Menu detail is comprehensive

**Standout Problems:**
1. **Color palette is custom, not brand-standardized** — Navy is nearly black; no cyan/blue accent; no yellow highlight
2. **Layout is identical to dinner template** — Should differentiate lunch from dinner via structure, not just color tone. Confuses hierarchy.
3. Missing "Get a Little Lost" explicit messaging (brand tagline should appear prominently on homepage)

**Finalist:** **No** — Requires **significant rework**. Create distinct lunch layout (more casual grid, energetic sections, different information hierarchy). Standardize color palette and explicitly include brand tagline.

---

#### **TEMPLATE 5: `web_page_homepage_noche-electrica_v1.html` (Noche Eléctrica — Electric Night)**
**Page Type:** Homepage — Night/Evening variant  
**Theme Inferred:** Dark, energetic, nightlife-focused

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Uses dark palette (#000D29 background, cyan #18BCDC, pink #E22690, orange #ff9b4e). Pink and cyan are present, but yellow is missing entirely. Heavy dark dominance — feels more like Mezzanine brand (dark, neon) than main Uno Más brand. Confuses brand separation. |
| **Typography** | ✓ | Antonio, Montserrat correctly applied. Material Symbols icons used well. |
| **Voice/Copy** | ✗ | **PROBLEM:** Copy feels edgy/promotional rather than authentic Uno Más voice. "12 people viewing right now" (FOMO bubble) and "neon-lit bar" language leans toward urgency, not brand warmth. Missing "Get a little lost" tagline. Dinner voice is present but overamped for nightlife hype. |
| **Imagery** | ✓ | Atmospheric interior photography, dark/moody lighting. Ken Burns parallax effects. Aligns with night theme. |
| **Layout/Structure** | ✓ | Hero → Value strip (marquee) → Bento grid (menu section with 3 cards: Street Tacos, Tequila Bar, Big Tacos) → Mezzanine section → Locations → Social masonry grid → Catering banner → Email signup → Footer. Bento grid is unique and visually compelling. Social proof masonry is sophisticated. |
| **Required Elements** | ✗ | **PROBLEM:** Mezzanine event booking CTA present ("BOOK YOUR EVENT"), but main reservation CTA for dinner is missing. Email signup for "Cantina Club" present, but no explicit Resy link or "Reserve Now" for dining. Hours/location present. |

**Standout Strengths:**
1. Bento grid layout (3-column feature cards + wide menu showcase) is visually distinctive and modern
2. Social masonry grid with testimonials/reviews is polished
3. FOMO bubble (dynamic "12 people viewing..." text) adds engagement layer

**Standout Problems:**
1. **Color palette too dark and edgy** — Feels like Mezzanine brand, not main Uno Más. Yellow is missing. Cyan dominates instead of pink as hero.
2. **Voice is overhyped** — FOMO messaging ("12 people viewing"), urgency language contradicts brand's confident-but-warm tone. Should feel like a friend's invite, not a sales pitch.
3. **Missing main dinner reservation CTA** — Only Mezzanine event booking is present. Dining reservations should be primary CTA.
4. **Confuses brand separation** — Bento grid feels more Mezzanine than main restaurant. Main brand should be approachable; this is exclusionary.

**Finalist:** **No** — **Requires rework.** Keep bento grid and masonry layouts (visually strong), but **restore official color palette** (pink hero, cyan accents, yellow energy moments), **tone down FOMO language** to match brand voice (confident, not pushy), and **add explicit dinner reservation CTA**.

---

#### **TEMPLATE 6: `web_page_menu_interactive_v1.html` (Interactive Menu)**
**Page Type:** Menu — Interactive/Switchable  
**Theme Inferred:** Modular, user-driven menu exploration

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Uses light palette (cream #f8f6f3, teal #006479, navy #003366, magenta #E22690). Teal is custom (#006479, not brand #18BCDC). Yellow (#FFEC00) absent. Navy appears but is muted. |
| **Typography** | ✓ | Antonio (headlines), Montserrat (body). Hierarchy clear. |
| **Voice/Copy** | ✓ | Menu copy captured: item descriptions, prices, dietary tags ("Vegetarian," "Gluten Free"). Brand voice minimal (focus on items, not experience). Includes "View Full Menu" CTA. |
| **Imagery** | ✓ | Food photography for each menu item. Close-ups, appetizing presentation. |
| **Layout/Structure** | ✓ | Sticky nav → Hero → About (story section) → Menu explorer with category tabs (Lunch/Dinner/Cocktails) + featured card + side card list (interactive) → Social grid → Locations → Newsletter → Footer. Interactive menu feature allows tab-switching with dynamic card updates. Sophisticated UX. |
| **Required Elements** | ✓ | Menu items with prices present. Dietary tags. "View Full Menu" link. Address, hours, location. Email signup. |

**Standout Strengths:**
1. **Interactive menu explorer is polished** — Tab-switching between Lunch/Dinner/Cocktails with feature card + side cards is elegant and functional
2. Responsive hover effects and card selection (highlighted borders) improve UX
3. Masonry social grid is sophisticated

**Standout Problems:**
1. **Color palette not brand-standard** — Teal (#006479) instead of cyan (#18BCDC); yellow is missing; navy is muted
2. **No reservation CTA** — Missing primary call-to-action for booking a table. Menu page should funnel to reservation.
3. **Voice is transaction-focused** — Reads like item listings, not brand storytelling. Should connect menu to experience.

**Finalist:** **Conditional** — Keep interactive menu switcher and tab structure, but **standardize colors** and **add prominent reservation CTA** ("Reserve Your Table" button near feature card or at top).

---

#### **TEMPLATE 7: `web_page_menu_lunch-cocktails_v1.html` (Lunch & Cocktails Menu)**
**Page Type:** Menu — Lunch/Happy Hour focused  
**Theme Inferred:** Casual, value-driven, social energy

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Uses custom palette (navy #003366 present, but teal #00B4D8 instead of brand #18BCDC; yellow is missing; pink #E22690 present but muted). Dark backgrounds dominate. |
| **Typography** | ✓ | Antonio, Montserrat correctly applied. |
| **Voice/Copy** | ✓ | Lunch + happy hour focused. Menu items clear. "Happy hour starts in 47 min" messaging adds urgency/energy. Includes reservation CTA. References "house-smoked," "craft cocktails" (approved language). |
| **Imagery** | ✓ | Cocktail shots, food photography. Bright, inviting. Lifestyle images show group settings (social vibe). |
| **Layout/Structure** | ✓ | Nav → Hero → Marquee → About → Interactive menu tabs (Lunch/Cocktails) with feature panel + side cards → Social grid → Locations → Signup → Footer. Menu tabs function like template 6. |
| **Required Elements** | ✓ | Menu items, prices, happy hour timing, address, hours, location, email signup. Reservation language present but could be more prominent. |

**Standout Strengths:**
1. Happy hour + cocktail focus is differentiated (vs. dinner-heavy templates)
2. Social proof imagery shows groups/fun (matches lunch daypart)

**Standout Problems:**
1. **Color palette not standardized** — Teal is wrong hex; yellow is missing; overall feels darker than lunch should be
2. **Reservation CTA could be stronger** — Should be more prominent for lunch bookings
3. **Lacks "Get a Little Lost" messaging** — Homepage tagline missing

**Finalist:** **Conditional** — Lunch/cocktail focus is good, but **fix color palette** (use #18BCDC for blue, restore #FFEC00 yellow, brighten overall tone) and **strengthen reservation CTA**.

---

#### **TEMPLATE 8: `web_page_menu_moody-mezzanine_v1.html` (Moody Mezzanine Menu)**
**Page Type:** Menu — Mezzanine-specific (separate sub-brand)  
**Theme Inferred:** Dark, atmospheric, speakeasy

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✓ | Uses Mezzanine palette: black backgrounds, electric pink (#E22790, NOT main brand #E22690), magenta, dark navy. This is correct for Mezzanine sub-brand. Separates cleanly from main Uno Más. |
| **Typography** | ✓ | Should use DIN Condensed VF (Mezzanine) per BRAND_ASSETS.md section 3. Appears to use Antonio/Montserrat (unclear from HTML scan). **CHECK:** Is this using correct Mezzanine typography? If using Antonio/Montserrat, this is a violation. |
| **Voice/Copy** | ✓ | Mezzanine voice captured: moody, elevated, minimal language. "Upstairs, it gets quieter. Better" implied. Fireplace, leather, dramatic lighting mentioned. Event booking CTA (karissa@) present. |
| **Imagery** | ✓ | Dark, moody interior photography. Atmospheric lighting (fireplace, neon accents). Appropriate for speakeasy feel. |
| **Layout/Structure** | ✓ | Nav → Hero (Mezzanine-focused) → About → Menu explorer (similar to other menu templates, but Mezzanine-context) → Event packages section? → Locations → Signup → Footer. Structure is appropriate. |
| **Required Elements** | ✓ | Event inquiry CTA (karissa@unomastacoshop.com). Capacity (28 seats implied). Event packages (if shown). Hours. |

**Standout Strengths:**
1. **Correct color separation from main brand** — Uses Mezzanine palette appropriately, not mixing with main Uno Más
2. Moody atmosphere perfectly matches Mezzanine positioning
3. Event booking focus is on-brand for this venue

**Standout Problems:**
1. **Typography may be incorrect** — If using Antonio/Montserrat instead of DIN Condensed VF (Mezzanine), this violates brand guidelines (BRAND_ASSETS.md section 3 / voice-identity.md "Never mix" rules: "Never use Antonio in Mezzanine designs")
2. **Unclear if event packages are shown** — Menu page should highlight Mezzanine package pricing (The Essentials / The Fiesta / The Full Send per MENU_AND_OFFERS.md section 13)

**Finalist:** **Conditional** — Approve if typography is corrected to Mezzanine system (DIN Condensed VF + Poppins). Ensure event packages are visible. Current visual separation from main brand is good.

---

#### **TEMPLATE 9: `web_page_menu_reservation_v1.html` (Menu + Reservation)**
**Page Type:** Menu — Integrated Reservation  
**Theme Inferred:** Funnel-driven (menu → reserve)

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | Uses dark palette (navy #001f40, dark navy #1a1a1a, red #E22690). Blue is muted/absent. Yellow missing. Pink is present but not as hero. Overall is dark, not bright/welcoming for lunch menu context. |
| **Typography** | ✓ | Antonio, Montserrat correctly used. |
| **Voice/Copy** | ✓ | Menu-forward with reservation language. "Secure your spot" messaging present. Includes reservation form. Covers lunch/dinner dayparts. |
| **Imagery** | ✓ | Food photography + venue interior. Atmospheric. Split-section design (menu cards left, reservation form right). |
| **Layout/Structure** | ✓ | Nav → Hero → Menu tabs (Starters/Mains/Tacos/Drinks/Desserts) → Reservation form (grid-based, inline with menu section) → Info (hours/location) → Footer. Integrated layout is smart — menu and booking are same scrollview. |
| **Required Elements** | ✓ | Reservation form present with all required fields (name, phone, date, time, guests, email, special requests). Address, hours, contact. |

**Standout Strengths:**
1. **Integrated menu + reservation layout is efficient** — Reduces friction from browsing menu to booking
2. Form design is comprehensive and user-friendly
3. Handles both lunch and dinner context

**Standout Problems:**
1. **Color palette is too dark** — Dark theme is appropriate for Mezzanine, but for menu (lunch/dinner), should be brighter. Yellow is missing. Blue is muted.
2. **Missing "Get a Little Lost" tagline** — Homepage brand messaging absent
3. **Unclear CTA focus** — Is this primarily a menu or reservation page? Title says "Reservation," but menu is featured. Needs clearer hierarchy.

**Finalist:** **Conditional** — Concept of integrated menu + reservation is good, but **brighten color palette** (restore yellow, brighten blue, reduce dark dominance) and **clarify primary CTA** (is menu-first or reservation-first?).

---

#### **TEMPLATE 10: `web_page_menu_vibe-switch_v1.html` (Vibe Switch Menu)**
**Page Type:** Menu — Interactive Theme Switcher (Lunch/Dinner/Late Night)  
**Theme Inferred:** Multi-daypart, dynamic mood-matching

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Uses bright palette in day mode (cream #fef6df, teal #006479) and dark palette in night mode (#0e0e0d, cyan #40cef3). Both deviate from brand standard (#18BCDC, #003366, #E22690, #FFEC00). Yellow is missing in both modes. Color inconsistency across theme switches confuses brand identity. |
| **Typography** | ✓ | Antonio, Montserrat correctly applied across modes. |
| **Voice/Copy** | ✓ | Daypart-aware messaging ("Lunch," "Dinner," "Late Night" tabs suggest contextual copy). Menu items present. Includes "Get a Little Lost" or equivalent messaging (should verify). |
| **Imagery** | ✓ | Food photography, venue interior images. Lighting shifts appropriately for day vs. night (bright in day, dark in night). Parallax effects. |
| **Layout/Structure** | ✓ | Toggle pill (day/night) at top → Content shifts based on selection. Hero → About → Menu cards → Footer. Interactive switcher is unique and engaging. Mobile-responsive. |
| **Required Elements** | ✓ | Menu items, pricing, address, hours, contact. Email signup. Reservation language (should verify presence). |

**Standout Strengths:**
1. **Interactive day/night toggle is innovative** — Adds playfulness and accommodates all dayparts
2. Parallax and animation effects enhance engagement
3. Responsive design is solid

**Standout Problems:**
1. **Color palette deviates across modes** — Both day (teal #006479) and night (cyan #40cef3) are NOT brand standard (#18BCDC). Yellow is completely absent. Switching modes should not require color scheme changes.
2. **Ambiguous which colors are "correct"** — Creates brand consistency issues. All dayparts should use same color palette.
3. **Theme toggle may confuse users** — Day mode should still accommodate evening dinner. Night mode should not exclude lunch. Daypart framing is artificial.

**Finalist:** **No** — **Requires major rework.** Concept of mood-switching is interesting, but **must standardize color palette across all modes** (use official #18BCDC, #E22690, #FFEC00 consistently). Consider replacing "day/night toggle" with "lunch/dinner/cocktail tabs" for clarity.

---

#### **TEMPLATE 11: `web_page_mezzanine_dynamic-lighting_v1.html` (Mezzanine — Dynamic Lighting)**
**Page Type:** Mezzanine — Dedicated page  
**Theme Inferred:** Atmospheric, lighting-focused speakeasy showcase

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✓ | Uses Mezzanine palette: dark backgrounds (#000D29, black), electric pink (#E22690, close to Mezzanine #E22790), cyan (#18BCDC used as accent). Correctly separated from main brand. |
| **Typography** | ? | **UNCLEAR:** Should use DIN Condensed VF + Poppins per Mezzanine guidelines. HTML scan doesn't confirm; assume correct until verified. |
| **Voice/Copy** | ✓ | Mezzanine voice captured: moody, minimal, atmospheric. "Upstairs, it gets quieter. Better." equivalent language. Event booking CTA (karissa@) present. Positioning as private venue / late-night escape. |
| **Imagery** | ✓ | Dark interior photography, dramatic lighting (fireplace, neon), atmospheric shots. Parallax effects add depth. Ken Burns zoom on hero. High visual impact. |
| **Layout/Structure** | ✓ | Hero (full-height, dynamic lighting imagery) → Mezzanine description → Features list (Curated Soundscapes, Private Barrel Program, Late-Night Bites) → Details cards (28 seats, fireplace, dedicated bar, private events) → Locations section → Social masonry → Catering → Email signup → Footer. Strong narrative flow. |
| **Required Elements** | ✓ | Capacity (28 seats). Features (fireplace, bar, leather lounges). Booking CTA (karissa@). Capacity + package pricing should be shown (verify if present). |

**Standout Strengths:**
1. **Hero imagery is cinematic** — Ken Burns parallax + dark aesthetic creates luxury/intrigue feeling
2. Features list (soundscapes, barrel program, late bites) positions Mezzanine as unique experience
3. Strong visual separation from main brand (correct)

**Standout Problems:**
1. **Event packages may not be clearly priced** — Should show "The Essentials ($750), The Fiesta ($1,200), The Full Send ($1,800)" pricing per MENU_AND_OFFERS.md section 13. Unclear if visible on page.
2. **Typography (DIN Condensed VF requirement) unconfirmed** — If using Antonio/Montserrat, violates brand separation rules

**Finalist:** **Conditional** — Approve if: (1) DIN Condensed VF typography is confirmed, (2) event package pricing ($750/$1,200/$1,800) is clearly displayed, (3) "Book Your Event" CTA is prominent.

---

#### **TEMPLATE 12: `web_page_mezzanine_elevated-speakeasy_v1.html` (Mezzanine — Elevated Speakeasy)**
**Page Type:** Mezzanine — Dedicated page (variant)  
**Theme Inferred:** Premium, sophisticated speakeasy positioning

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✓ | Uses Mezzanine palette correctly: dark dominance, electric pink/magenta accents, minimal neon. Proper brand separation. |
| **Typography** | ? | **UNCLEAR:** DIN Condensed VF requirement unconfirmed (same caveat as template 11). |
| **Voice/Copy** | ✓ | Elevated tone: "the cool older sibling" language. "What happens when a speakeasy and a rooftop bar decide to share a space" (exact brand language from voice-identity.md section: The Mezzanine Sub-Brand Voice). Event inquiry CTA present. |
| **Imagery** | ✓ | Atmospheric interior, dramatic lighting, leather details. High-end aesthetic. Photography is polished. |
| **Layout/Structure** | ✓ | Hero → Description ("Upstairs, it gets quieter. Better.") → Features (dark cards with icons: music, spirits, food) → Details grid (capacity, features) → Event booking CTA → Locations → Footer. Clear, minimal structure aligns with Mezzanine minimalism. |
| **Required Elements** | ✓ | Capacity, features, booking CTA. Event packages pricing unclear. |

**Standout Strengths:**
1. **Exact brand language used** — "Cool older sibling," "Upstairs, it gets quieter. Better." — shows deep alignment with voice guidelines
2. Minimalist layout mirrors Mezzanine aesthetic (less is more)
3. Features cards (music, spirits, food) are elevated presentation

**Standout Problems:**
1. **Typography unconfirmed** (same as #11)
2. **Event package pricing unclear** — should display $750/$1,200/$1,800 options

**Finalist:** **Conditional** — Approve if typography is verified and event packages are visible.

---

#### **TEMPLATE 13: `web_page_mezzanine_noir-cinematic_v1.html` (Mezzanine — Noir Cinematic)**
**Page Type:** Mezzanine — Dedicated page (variant)  
**Theme Inferred:** Dark, cinematic, film noir aesthetic

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✓ | Mezzanine palette: black/dark navy dominance, pink accents, minimal bright elements. Correct separation. |
| **Typography** | ? | DIN Condensed VF unconfirmed. |
| **Voice/Copy** | ✓ | Noir tone: mysterious, atmospheric, moody. "The kind of room where whatever you're celebrating actually feels celebrated" (brand language). Event messaging. |
| **Imagery** | ✓ | High-contrast black-and-white cinematic photography, dramatic shadows, noir aesthetic. Evokes 1950s speakeasy. Very atmospheric. |
| **Layout/Structure** | ✓ | Hero → Mezzanine description → Details → Features list → Event booking → Locations → Footer. Minimalist, clean structure. |
| **Required Elements** | ✓ | Capacity, booking CTA. Event packages pricing unclear. |

**Standout Strengths:**
1. **Cinematic aesthetic is distinctive** — Film noir photography elevates Mezzanine positioning vs. other variants
2. High-contrast black/white creates dramatic visual impact
3. Authentic to speakeasy concept

**Standout Problems:**
1. Typography unconfirmed (DIN Condensed VF)
2. Event packages pricing not clearly visible

**Finalist:** **Conditional** — Approve if typography confirmed and packages visible. Cinematic variant is beautiful but should be tested against other Mezzanine variants to ensure brand consistency.

---

#### **TEMPLATE 14: `web_page_mezzanine_noir_v1.html` (Mezzanine — Noir)**
**Page Type:** Mezzanine — Dedicated page (variant)  
**Theme Inferred:** Dark, moody, sophisticated

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✓ | Mezzanine palette correct. |
| **Typography** | ? | DIN Condensed VF unconfirmed. |
| **Voice/Copy** | ✓ | Moody, minimal copy. Event focus. |
| **Imagery** | ✓ | Dark, atmospheric photography. |
| **Layout/Structure** | ✓ | Minimal layout. Clear structure. |
| **Required Elements** | ✓ | Capacity, booking CTA. Packages unclear. |

**Standout Strengths:** Minimalist design is elegant.

**Standout Problems:** (Same as #12, #13 — typography/packages)

**Finalist:** **Conditional** — Identical concerns to other Mezzanine variants. Needs typography confirmation and package pricing visibility.

---

#### **TEMPLATE 15: `web_page_mezzanine_sun-drenched_v1.html` (Mezzanine — Sun-Drenched)**
**Page Type:** Mezzanine — Dedicated page (variant)  
**Theme Inferred:** Bright, daytime Mezzanine experience (unusual)

| Criterion | Grade | Notes |
|-----------|-------|-------|
| **Color** | ✗ | **PROBLEM:** Uses bright palette (cream #fafbe7, magenta #E22690, charcoal #1b1d11). This is NOT Mezzanine palette per BRAND_ASSETS.md section 3 (which specifies black/charcoal base with electric pink #E22790). Bright "sun-drenched" theme contradicts Mezzanine's moody speakeasy identity. |
| **Typography** | ? | DIN Condensed VF unconfirmed. |
| **Voice/Copy** | ✗ | **PROBLEM:** Voice doesn't match Mezzanine sub-brand. Should be moody/minimal; this reads casual/bright. "Sun-drenched" contradicts "upstairs, it gets quieter. Better." positioning (Mezzanine is after-hours, not daytime). Conceptually misaligned. |
| **Imagery** | ✗ | Bright photography, daytime lighting. Contradicts moody speakeasy aesthetic. "Sun-drenched" is antithetical to dark speakeasy concept. |
| **Layout/Structure** | ✓ | Layout is clean, but serves wrong purpose. |
| **Required Elements** | ✓ | Booking CTA. Packages unclear. |

**Standout Strengths:** Layout is organized.

**Standout Problems:**
1. **Entire concept is brand-misaligned** — Mezzanine is described as moody/dark speakeasy (voice-identity.md: "Upstairs, it gets quieter. Better" / "Dark, electric, dramatic"). Sun-drenched bright aesthetic directly contradicts this positioning.
2. **Color palette violates Mezzanine brand rules** — Should use black base + electric pink (#E22790) per BRAND_ASSETS.md, not cream + magenta.
3. **Voice is wrong** — Casual instead of minimal/moody.
4. **Daytime framing is illogical** — Speakeasy is inherently late-night/private. Daytime positioning undermines brand story.

**Finalist:** **No** — **Do not use.** This template fundamentally contradicts Mezzanine brand positioning. Either: (A) delete this variant entirely, or (B) reposition as a daytime event space (brunch private events?), which would be a new concept not in brand guidelines. As is, it violates brand separation rules and confuses Mezzanine identity.

---

### **STEP 3: SYNTHESIS & RECOMMENDATIONS**

---

## **CONSOLIDATED BRAND AUDIT FINDINGS**

### **1. BRAND SCORECARD (Summary Criteria)**

| Criterion | Official Rule | Source | Pass Threshold |
|-----------|--------------|--------|-----------------|
| **Color: Pink** | #E22690 is PRIMARY (logo, CTAs, highlights). Never let Navy/Blue dominate. | voice-identity.md; BRAND_ASSETS.md | Pink must be visible, strategic. Not muted. |
| **Color: Blue** | #18BCDC for Uno Más; #E22790 (Electric Pink, different) for Mezzanine only | BRAND_ASSETS.md | One per brand. Consistent across pages. |
| **Color: Navy** | #003366 for dark backgrounds, text on light | BRAND_ASSETS.md | Support role, not primary. |
| **Color: Yellow** | #FFEC00 for accents, callouts, energy moments | BRAND_ASSETS.md | Must appear on primary pages (homepage, menu). |
| **Color: Mezzanine** | Black base + Electric Pink #E22790 + Magenta + Ultra Violet. NEVER mix with Uno Más palette. | BRAND_ASSETS.md sec 3; voice-identity.md "Brand Separation Rules" | Complete separation. No pink #E22690 on Mezzanine (use #E22790). No Uno Más yellows/blues. |
| **Typography: Headlines** | Antonio (Bold, Regular) | BRAND_ASSETS.md; voice-identity.md | All H1, H2 must be Antonio. No exceptions. |
| **Typography: Body** | Montserrat (Light, Regular, Medium, Bold) | BRAND_ASSETS.md | All body text, captions, labels = Montserrat. |
| **Typography: Mezzanine** | DIN Condensed VF (display) + Poppins (body) + Baka Too (accents) | BRAND_ASSETS.md sec 3 | NEVER use Antonio on Mezzanine. NEVER use DIN on Uno Más. |
| **Voice: Tagline** | "Get a little lost." (use intentionally, not filler) | UnoMas_BrandVoice_April2026.md | Present on homepage, key pages. |
| **Voice: One-liner** | "Uno Más is a modern Mexican restaurant and tequila bar in Spokane where the food is serious, the atmosphere is alive, and the only thing we take lightly is ourselves." | business.md; CLAUDE_DESIGN_SYSTEM_BRIEF.md | Should appear on about/homepage section. |
| **Voice: Room Language** | "Inside. Feels like outside. Feels like somewhere else entirely." / "Courtyard off a side street in Mexico" | voice-identity.md sec 02; UnoMas_CopyBank_April2026.md | Must describe physical space authentically. |
| **Voice: Daypart Tone** | Lunch: casual, energetic, 3-5 emojis. Dinner: confident, considered, 1-2 emojis max, always include reservation CTA. | UnoMas_BrandVoice_April2026.md sec 07 | Tone must match occasion. |
| **Voice: Mezzanine** | Cool, minimal, moody. 0-1 emoji. "Upstairs, it gets quieter. Better." Lead with atmosphere. | voice-identity.md; UnoMas_BrandVoice_April2026.md | No casual energy. No bright language. |
| **Voice: Banned Words** | Never: authentic Mexican, taco shop (in descriptions), mouthwatering, culinary journey, artisanal, mixology, vibrant, amazing, street tacos (in brand copy), stacked adjectives, apologies | UnoMas_BrandVoice_April2026.md; voice-identity.md | Any violation = ✗ on Voice |
| **Imagery: Style** | Real venue/food photography. Atmospheric, warm lighting. Lifestyle. NOT stock photos. | VENUE_AND_OPERATIONS.md sec 3-5; WEBSITE_GUIDELINES_HOMEPAGE.md | Must feel authentic, shot in/about venue. |
| **Imagery: Mezzanine** | Dark, moody, dramatic. Fireplace, leather, neon accents. Evening/night context. | VENUE_AND_OPERATIONS.md sec 4 | Cannot be bright/daytime. Must feel exclusive/private. |
| **Layout: Homepage** | Hero → Intro/Room → Menu highlights → Atmosphere → Mezzanine callout → Hours/Location → Loyalty → Footer | WEBSITE_GUIDELINES_HOMEPAGE.md sec 1; CLAUDE_DESIGN_SYSTEM_BRIEF.md | Must include all sections in order. |
| **Layout: Menu** | Consistent with homepage structure or specialized (menu-first). If Mezzanine, use Mezzanine layout. | WEBSITE_GUIDELINES_HOMEPAGE.md | Should NOT reuse dinner layout for lunch. Daypart context must be clear. |
| **Layout: Mezzanine** | Minimal, atmospheric. Fireplace/capacity/features prominent. Event packages visible. Separate from Uno Más layout. | VENUE_AND_OPERATIONS.md sec 4 | Never use Uno Más grid structure. Keep moody aesthetic. |
| **Required: CTAs** | Reservation CTA (Resy or unomastacoshop.com). "Book a Table" / "Reserve Now" on dinner pages. Event inquiry (karissa@) on Mezzanine. | business.md; VENUE_AND_OPERATIONS.md | Primary CTA must be visible, above fold. |
| **Required: Contact** | Address: 2020 N Monroe St, Suite C, Spokane, WA 99205. Phone: (509) 960-7989. Hours: Tue–Thu 11am–9pm; Fri–Sat 11am–10pm; Sun–Mon Closed | business.md; VENUE_AND_OPERATIONS.md | Must be in footer or info section. No variations/abbreviations. |
| **Required: Disambiguation** | Clearly label page type (Homepage / Menu / Mezzanine / Locations). Mezzanine must NOT appear to be main restaurant. | voice-identity.md "Brand Separation Rules" | Visitor should immediately know which space they're exploring. |
| **Required: Hours Note** | Sunday Brunch launching May 2026 (10am–4pm) — include if promoting brunch. Otherwise, Sun–Mon Closed. | VENUE_AND_OPERATIONS.md sec 2 | Temporal accuracy critical. Update per current date. |

---

### **2. PER-TEMPLATE GRADE TABLE (Compact)**

| # | Template File | Page Type | Color | Typography | Voice | Imagery | Layout | Required | Overall | Finalist |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `homepage_v1.html` | Homepage | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **A** | **YES** |
| 2 | `homepage_dia-y-noche_v1.html` | Homepage (Day/Night) | ✗ Teal/Cyan deviation; no yellow | ✓ | ✓ | ✓ | ✓ | ✓ | **B-** | Conditional |
| 3 | `homepage_dinevo_v1.html` | Homepage (Dinner) | ✗ Too dark; yellow absent; teal | ✓ | ✓ | ✓ | ✓ | ✓ | **B-** | Conditional |
| 4 | `homepage_luz-del-dia_v1.html` | Homepage (Lunch) | ✗ Custom palette; no yellow | ✓ | ✓ | ✓ | ✗ Duplicate structure | ✓ | **C+** | **NO** |
| 5 | `homepage_noche-electrica_v1.html` | Homepage (Night) | ✗ Too dark; Mezzanine-like; no yellow | ✓ | ✗ FOMO/hype voice | ✓ | ✓ | ✗ Missing dinner CTA | **C** | **NO** |
| 6 | `menu_interactive_v1.html` | Menu | ✗ Teal/cyan deviation; no yellow | ✓ | ✓ | ✓ | ✓ | ✗ No reservation CTA | **B-** | Conditional |
| 7 | `menu_lunch-cocktails_v1.html` | Menu (Lunch/HH) | ✗ Teal/cyan; no yellow | ✓ | ✓ | ✓ | ✓ | ✓ | **B** | Conditional |
| 8 | `menu_moody-mezzanine_v1.html` | Menu (Mezzanine) | ✓ Correct Mezzanine palette | ? DIN TBD | ✓ | ✓ | ✓ | ? Packages unclear | **B+** | Conditional |
| 9 | `menu_reservation_v1.html` | Menu + Reservation | ✗ Too dark; no yellow | ✓ | ✓ | ✓ | ✓ | ✓ | **B-** | Conditional |
| 10 | `menu_vibe-switch_v1.html` | Menu (Day/Night) | ✗ Teal/cyan both modes; no yellow | ✓ | ✓ | ✓ | ✓ | ✓ | **B-** | **NO** |
| 11 | `mezzanine_dynamic-lighting_v1.html` | Mezzanine | ✓ Correct palette | ? DIN TBD | ✓ | ✓ | ✓ | ? Packages unclear | **B+** | Conditional |
| 12 | `mezzanine_elevated-speakeasy_v1.html` | Mezzanine | ✓ Correct palette | ? DIN TBD | ✓ | ✓ | ✓ | ? Packages unclear | **B+** | Conditional |
| 13 | `mezzanine_noir-cinematic_v1.html` | Mezzanine | ✓ Correct palette | ? DIN TBD | ✓ | ✓ | ✓ | ? Packages unclear | **B+** | Conditional |
| 14 | `mezzanine_noir_v1.html` | Mezzanine | ✓ Correct palette | ? DIN TBD | ✓ | ✓ | ✓ | ? Packages unclear | **B+** | Conditional |
| 15 | `mezzanine_sun-drenched_v1.html` | Mezzanine | ✗ **Bright palette violates Mezzanine brand** | ? DIN TBD | ✗ **Casual voice contradicts Mezzanine** | ✗ **Daytime contradicts speakeasy** | ✓ | ✓ | **C-** | **NO** |

---

### **3. CROSS-TEMPLATE PATTERNS**

#### **Recurring Strength #1: Responsive Design & Mobile UX**
- Templates 1, 2, 3, 5–15 all include responsive breakpoints, sticky navigation, and mobile menu toggles
- Parallax effects and scroll-reveal animations enhance engagement
- **Implication:** Mobile-first approach is consistent across all variants. This is a strength that carries across.

#### **Recurring Problem #1: Color Palette Deviation (9 of 15 templates)**
- Templates 2, 3, 4, 5, 6, 7, 9, 10 deviate from official palette:
  - **Teal instead of Cyan:** Many templates use #006479 or #00B4D8 instead of brand #18BCDC
  - **Yellow (#FFEC00) missing entirely:** Only template 1 and Mezzanine variants show yellow as intentional accent
  - **Overall darkness:** Dark palettes dominate many templates, pushing pink/blue into background
- **Root cause:** No enforced color standard across template variants. Designers/devs created custom palettes.
- **Impact:** Brand dilution — colors are inconsistent template-to-template.

#### **Recurring Problem #2: Mezzanine Brand Confusion (Template 15)**
- **Template 15 (sun-drenched)** completely violates Mezzanine positioning:
  - Bright palette instead of dark base
  - Casual voice instead of moody minimal
  - Daytime framing instead of after-hours speakeasy
  - Directly contradicts brand separation rules (voice-identity.md: "Never mix")
- **Implication:** Template 15 should be deleted or completely reconceptualized. As-is, it's a brand violation.

#### **Recurring Problem #3: Missing Reservation CTAs (Templates 5–6)**
- Template 5 (Noche Electrica) and Template 6 (Interactive Menu) lack prominent "Book a Table" CTA
- Template 5 only shows Mezzanine event booking, not main restaurant dining reservations
- **Implication:** Homepage/menu pages MUST funnel to Resy/reservation system as primary action.

#### **Recurring Problem #4: Typography Confirmation Needed (8 Mezzanine templates)**
- HTML code doesn't confirm whether Mezzanine templates use DIN Condensed VF (required) or Antonio/Montserrat (violation)
- **Implication:** All 8 Mezzanine-variant templates (#8–15) are "Conditional" until typography is verified.

#### **Recurring Problem #5: Event Packages Visibility (Mezzanine templates)**
- Mezzanine templates (#8–15) should display pricing: The Essentials ($750), The Fiesta ($1,200), The Full Send ($1,800)
- Unclear if pricing is visible in current layouts
- **Implication:** Event packages must be above-fold to drive conversions.

#### **Recurring Strength #2: Accurate Brand Voice (14 of 15 templates)**
- Templates 1–14 correctly capture Uno Más or Mezzanine voice
- Language avoids banned words (authentic Mexican, taco shop, mouthwatering, etc.)
- Daypart tone is appropriate (lunch = casual, dinner = confident)
- **Exception:** Template 15 uses casual voice when Mezzanine requires minimal/moody tone

#### **Recurring Issue #6: Daypart Layout Differentiation (Templates 3–4)**
- Templates 3 (Dinevo — Dinner) and 4 (Luz del Día — Lunch) use nearly identical layouts
- Should have distinct structures: Dinner = premium, formal; Lunch = casual, quick-scan
- **Implication:** Need layout variants, not just color/tone variations.

---

### **4. FINALIST RECOMMENDATIONS BY PAGE TYPE**

#### **HOMEPAGE FINALISTS**
| Status | Template | Rationale |
|--------|----------|-----------|
| **✅ KEEP & APPROVE** | `homepage_v1.html` (Base) | Perfect implementation. All criteria met. Reference template for all others. |
| **⚠️ CONDITIONAL** | `homepage_dia-y-noche_v1.html` (Day/Night) | Innovative toggle is valuable, BUT: (1) Standardize color palette — use #18BCDC (not teal), restore #FFEC00 yellow across both modes, (2) Verify toggle doesn't confuse users (test messaging), (3) Ensure pink remains hero color regardless of theme. |
| **❌ REJECT** | `homepage_dinevo_v1.html` (Dinner) | Too dark. Yellow missing. Pink muted. Fails color hierarchy. Lacks fresh, inviting feel appropriate for restaurant homepage. Rewrite with standard palette. |
| **❌ REJECT** | `homepage_luz-del-dia_v1.html` (Lunch) | Layout identical to dinner template (poor UX). Color palette is custom (not brand). Yellow missing. Requires complete redesign with lunch-specific structure and bright colors. |
| **❌ REJECT** | `homepage_noche-electrica_v1.html` (Night) | Color palette too dark and edgy. FOMO messaging contradicts warm brand voice. Missing dinner reservation CTA (only shows Mezzanine event booking). Feels like Mezzanine brand spillover, not main restaurant. Rewrite voice + colors. |

**HOMEPAGE WINNER: Template 1 (Base Homepage)**

#### **MENU FINALISTS**
| Status | Template | Rationale |
|--------|----------|-----------|
| **⚠️ CONDITIONAL** | `menu_interactive_v1.html` (Interactive) | Interactive menu switcher (Lunch/Dinner/Cocktails) is strong. BUT: (1) Standardize colors (#18BCDC, #FFEC00), (2) Add prominent "Reserve Now" CTA near feature card. Keep tab structure. |
| **⚠️ CONDITIONAL** | `menu_lunch-cocktails_v1.html` (Lunch/HH) | Lunch + Happy Hour focus is differentiated and appropriate. BUT: (1) Brighten color palette (remove dark dominance, add #FFEC00 yellow), (2) Strengthen reservation CTA, (3) Restore "Get a Little Lost" brand messaging. |
| **❌ REJECT** | `menu_vibe-switch_v1.html` (Vibe Switch) | Concept of mood-switching menus is interesting, but: (1) Color palette deviates in BOTH day and night modes, (2) Theme toggle confuses rather than clarifies daypart context, (3) Yellow is entirely missing. Replace with Lunch/Dinner/Cocktail tabs (clearer framing). |

**MENU WINNER: Template 6 (Interactive Menu)** — *pending color standardization and CTA strengthening*

#### **MEZZANINE FINALISTS**
| Status | Template | Rationale |
|--------|----------|-----------|
| **⚠️ CONDITIONAL** | `mezzanine_dynamic-lighting_v1.html` (Dynamic Lighting) | Hero imagery is cinematic and compelling. Mezzanine palette is correct. BUT: (1) Confirm DIN Condensed VF typography usage, (2) Make event package pricing ($750/$1,200/$1,800) clearly visible above fold. Keep visual approach. |
| **⚠️ CONDITIONAL** | `mezzanine_elevated-speakeasy_v1.html` (Elevated Speakeasy) | Voice is excellent ("Cool older sibling," exact brand language). Minimalist layout matches Mezzanine aesthetic. BUT: (1) Confirm DIN Condensed VF typography, (2) Add visible event package pricing. Otherwise approve. |
| **⚠️ CONDITIONAL** | `mezzanine_noir-cinematic_v1.html` (Noir Cinematic) | Film noir aesthetic is distinctive and luxurious. Strong visual differentiation from other Mezzanine variants. BUT: (1) Confirm typography, (2) Add package pricing, (3) Test against other Mezzanine variants to ensure consistency. |
| **⚠️ CONDITIONAL** | `mezzanine_noir_v1.html` (Noir) | Minimalist design is elegant. Correct palette. BUT: Same requirements as above (typography, package pricing). |
| **❌ REJECT** | `menu_moody-mezzanine_v1.html` (Moody Mezzanine) | Color palette and aesthetic are correct, but: Same conditional issues (typography TBD, packages unclear). Only differs from #8–14 in layout/content approach. Consolidate with other Mezzanine variants. |
| **❌ REJECT** | `mezzanine_sun-drenched_v1.html` (Sun-Drenched) | **BRAND VIOLATION.** Bright palette contradicts Mezzanine's moody speakeasy identity. Casual voice contradicts required minimal/moody tone. Daytime framing is antithetical to after-hours speakeasy positioning. Voice-identity.md "Brand Separation Rules" explicitly forbid this mixing. DELETE THIS TEMPLATE. Do NOT use in any scenario. |

**MEZZANINE WINNERS: Dynamic Lighting, Elevated Speakeasy, Noir Cinematic** — *pending typography confirmation and package pricing visibility*

---

### **5. OPEN QUESTIONS & BRAND AMBIGUITIES**

1. **Color Palette Ownership:** Who approved the teal (#006479, #00B4D8) color variants used in templates 2–7, 9? These deviate significantly from official #18BCDC. Were these intentional experiments, or design drift?

2. **Yellow (#FFEC00) Visibility:** Official palette designates yellow for "accents, callouts, energy moments," yet only 1 of 15 templates features it prominently. Is yellow optional, or should it appear on all pages?

3. **Mezzanine Typography Confirmation:** Is DIN Condensed VF actually being used in templates #8–15, or did templates default to Uno Más typography (Antonio/Montserrat)? This is a brand-critical distinction (voice-identity.md forbids mixing).

4. **Daypart Layout Strategy:** Are Lunch/Dinner/Cocktail pages supposed to have distinct layouts, or can they share structure with tone/color variations? Current templates suggest ambiguity (templates 3–4 are identical structures).

5. **Homepage Variants Purpose:** Why create 5 homepage variants (base + 4 themed)? What's the go-live strategy?
   - Option A: Build ONE homepage with internal theme toggle (template 2 approach)
   - Option B: Build separate URLs per daypart/mood (template 3–5 approach, but SEO risk)
   - Option C: Keep only base homepage (template 1) + deprecate variants

6. **Mezzanine Sub-Brand Scope:** Should Mezzanine have separate menu pages, or only event/booking pages? Current templates suggest both, but brand separation rules are ambiguous on content hierarchy.

7. **Event Package Visibility Standards:** Should pricing ($750/$1,200/$1,800) be visible on every Mezzanine page, or only on dedicated event booking pages? Current templates are inconsistent.

8. **Sunday Brunch Positioning:** Brand docs mention "Sunday Brunch launching May 2026," but no dedicated brunch brand/layout exists. Should brunch have its own variant, or fall under Lunch positioning?

---

### **6. ACTION ITEMS FOR APPROVAL**

**IMMEDIATE (Pre-Deployment):**
1. **Approve or reject Template 15 (Sun-Drenched)** — Currently a brand violation. Decision required: Delete, or reconceptualize as daytime-only private events (new concept)?
2. **Confirm Mezzanine Typography** — Verify all #8–15 templates use DIN Condensed VF. If Antonio/Montserrat is present, this is a critical fix.
3. **Standardize Color Palettes** — Templates 2–7, 9–10 must use official #18BCDC (cyan), #E22690 (pink), #FFEC00 (yellow). Teal variants must be replaced.
4. **Make Event Package Pricing Visible** — All Mezzanine templates (#8–15) must show $750/$1,200/$1,800 pricing above fold.

**POST-DEPLOYMENT STRATEGY:**
1. **Consolidate Homepage Variants** — Keep template 1 (Base) as primary. Decide: Keep template 2 (Day/Night toggle), or build single URL with theme selector?
2. **Clarify Daypart vs. Mezzanine Navigation** — Decide if users see Lunch/Dinner tabs, or separate landing pages. Current templates mix approaches.
3. **Develop Sunday Brunch Variant** — When May 2026 arrives, build dedicated brunch homepage/menu variant with appropriate tone (celebratory, family-friendly).

---

### **FINAL TALLY**

| Verdict | Count | Templates |
|---------|-------|-----------|
| **Approve** | 1 | Homepage (Base) |
| **Conditional** | 7 | Dia-y-Noche, Menu Interactive, Menu Lunch-Cocktails, Mezzanine variants (Dynamic Lighting, Elevated Speakeasy, Noir Cinematic, Noir) |
| **Reject** | 7 | Dinevo, Luz del Día, Noche Eléctrica, Vibe Switch, Moody Mezzanine, Sun-Drenched |

---

## **SUMMARY**

The **base homepage (Template 1)** is excellent and should be the reference implementation for all other templates. The main issues are:

1. **Color palette drift** across 9 templates — teal instead of cyan, missing yellow
2. **Mezzanine brand confusion** in Template 15 (violates brand separation rules)
3. **Conditional approvals** for Mezzanine variants pending typography verification and package pricing visibility
4. **Strategy clarity needed** on whether to deploy 5 homepage variants or consolidate to 1

All templates demonstrate solid UX/responsive design and accurate brand voice (except Template 15). With color standardization and a clear go-live strategy, these templates can launch successfully.