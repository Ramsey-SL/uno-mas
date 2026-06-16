# Uno Más Website — Master Messaging Doc

**Owner:** Ramsey
**Created:** 2026-05-28
**Purpose:** Single source of truth for ALL copy across the new Uno Más website. Every headline, subheader, body block, CTA. 2–3 options per piece (or LOCKED if already approved). Mark your picks → I push bulk updates to Supabase `site_content` + draft any Lovable prompts needed for hardcoded copy.

---

## How to use this doc

1. **Read top-to-bottom or jump to a page section.**
2. **For each piece of copy**, do one of:
   - ✅ Mark a picked option (write `PICK: A` or your custom edit)
   - ✏️ Edit any option inline
   - ➕ Add your own (`D: ...`)
   - 🗑 Strike through any to delete
3. **When done**, save the file. Tell me you're ready.
4. **I push picks to:**
   - **Supabase `site_content`** for in-CMS copy (hero, sections, teasers — most things)
   - **Lovable prompt** for hardcoded copy (header nav, footer chrome, button labels, 404, etc.)

---

## 🎙 Brand voice quick reference

**Uno Más voice:** Confident, self-aware, group-chat energy. Tom Segura/Bert Kreischer register. Short sentences, fragments welcome.

**Mezzanine sub-brand voice:** Cool, minimal, moody. Atmosphere-forward. 0–1 emojis. Tom Segura register only.

**ALWAYS:**
- Feel like a real person, not a corporation
- Reflect Spokane pride / Monroe Street identity
- Short. Direct. Confident.
- Kid-friendly at all times (no 21+ language)

**NEVER use:**
- taco shop *(in brand-level copy)* · authentic Mexican · street tacos *(brand-level)* · mouthwatering · culinary journey · leverage/utilize · artisanal · mixology · amazing *(generic)* · vibrant · "perfect for any occasion" · stacked adjectives · "We apologize for…"

**Use instead:**
- Modern Mexican · house-smoked · Get a little lost · craft cocktails · The Mezzanine on Monroe · 2020 N Monroe · Hit different · Your move · So we did a thing… · Make good choices

---

## 🏠 `/` HOMEPAGE

### Hero band

**Where:** Supabase `site_content` (page_slug='/', block_key='hero')
**Current:** Headline "GET A LITTLE LOST." · Subhead "Modern Mexican. Craft cocktails. A speakeasy upstairs." · CTAs "Reserve a table" / "See the menu"

**Kicker (small text above headline) — 3 options:**

- A. "Modern Mexican · Spokane"
- B. "Tacos & tequila on Monroe"
- C. "2020 N Monroe · Spokane"

**Headline — 3 options:**

- A. **GET A LITTLE LOST.** *(current — brand tagline, recommend keep)*
- B. **NOT WHAT YOU EXPECTED. ON PURPOSE.**
- C. **MODERN MEXICAN. SPOKANE ORIGINAL.**

**Subhead — 3 options:**

- A. "Modern Mexican. Craft cocktails. A speakeasy upstairs." *(current)*
- B. "Three venues at 2020 N Monroe. Lunch, dinner, late nights, and the room upstairs you'll keep telling people about."
- C. "Tacos that started a restaurant. A dinner program that grew out of it. And an upstairs that surprised everyone."

**Primary CTA button — 2 options:**

- A. "Reserve a table" *(current)*
- B. "Book a table"

**Secondary CTA button — 2 options:**

- A. "See the menu" *(current)*
- B. "Open the menu"

### Venues intro band

**Where:** Supabase site_content (page_slug='/', block_key='venues-intro')
**Current:** Kicker "Three venues, one address" · Headline "WALK IN ONCE. PICK YOUR NIGHT."

**Kicker — 3 options:**

- A. "Three venues, one address" *(current)*
- B. "One address. Three rooms."
- C. "2020 N Monroe · Three ways to spend a night"

**Headline — 3 options:**

- A. **WALK IN ONCE. PICK YOUR NIGHT.** *(current)*
- B. **THREE ROOMS. ONE DOOR.**
- C. **THE CANTINA. THE MEZZANINE. THE PATIO.**

### Venue cards (3-up) — LOCKED 2026-05-28

✅ Locked copy:

- **The Cantina** — *Lunch, dinner, full bar. Inside feels like outside.* → /menu/dinner
- **The Mezzanine** — *Upstairs speakeasy. Private events. Atmosphere-first.* → /mezzanine
- **The Patio** — *Outdoor bar. Street food. Spokane summer.* → /menu

### Dinner feature band

**Where:** Supabase site_content (page_slug='/', block_key='dinner-feature')
**Current:** Kicker "Dinner is served." · Headline "PLATES THAT SURPRISE PEOPLE." · Body about Surf & Turf, etc. · CTA "See the dinner menu"

**Kicker — 3 options:**

- A. "Dinner is served." *(current)*
- B. "Dinner program · Live at 5pm"
- C. "After 5pm, we get serious."

**Headline — 3 options:**

- A. **PLATES THAT SURPRISE PEOPLE.** *(current)*
- B. **DINNER, REIMAGINED ON MONROE.**
- C. **THIS ISN'T WHAT YOU THINK. THAT'S THE POINT.**

**Body — 3 options:**

- A. "Surf & Turf. Carne Asada. A Raw Bar. The $129 Feast. This isn't what you think — that's the point." *(current)*
- B. "Skirt steak + tiger prawns. Achiote shrimp. Oysters when we can get them. The Feast for the whole table. Dinner at Uno Más is the part people don't expect."
- C. "We started as a taco shop. We grew into a dinner program. Surf & Turf, Carne Asada, The Feast — book a table and find out why."

**CTA — 2 options:**

- A. "See the dinner menu" *(current)*
- B. "Open the dinner menu"

### Testimonials section

**Where:** Supabase site_content (page_slug='/', block_key='testimonials')
**Current:** Headline "SPOKANE IS TALKING." + 2 quote cards

**Section headline — 3 options:**

- A. **SPOKANE IS TALKING.** *(current)*
- B. **WHAT PEOPLE ARE SAYING.**
- C. **DON'T TAKE OUR WORD FOR IT.**

**Quote cards:** Use the existing customer/press quotes from brand intel — no options needed unless you want to rotate them.

### Cantina Club teaser band *(NEW from homepage-polish prompt)*

**Where:** Lovable component (hardcoded after homepage polish prompt runs)
**Status:** Not yet built. Will land with `LOVABLE-PROMPT-homepage-polish.md`.

**Kicker — 3 options:**

- A. "The Cantina Club"
- B. "Loyalty program"
- C. "Eat better, more often."

**Headline — 3 options:**

- A. **JOIN THE CLUB. EAT BETTER, MORE OFTEN.**
- B. **MEMBERS GET MORE.**
- C. **SAVE YOUR SEAT AT THE BAR.**

**Subhead — 3 options:**

- A. "Members spend 107% more than non-members because they get it. Loyalty rewards, exclusive drops, first dibs on Mezzanine events. Sign up at the bar — or get on the list."
- B. "Free drinks. Birthday perks. Mezzanine first-access. The Cantina Club is how regulars get treated like family. Email below or sign up next time you're in."
- C. "Membership earns you rewards every visit. Plus exclusive event invites, birthday surprises, and a heads-up when something new drops."

**Form button — 2 options:**

- A. "Get On The List"
- B. "Join the Club"

### Mezzanine teaser — LOCKED 2026-05-28

✅ Locked copy (in Supabase site_content):

- Kicker: *The Mezzanine on Monroe*
- Headline: **AN ESCAPE YOU DIDN'T KNOW EXISTED.**
- Body: *Speakeasy above Uno Más. Private dinners. Watch parties. The nights people keep talking about.*
- CTA: *Find the stairs*

### Hours / contact strip (bottom of homepage)

**Where:** Lovable component (pulls hours from Supabase business_hours)

**"Hours today" heading — 2 options:**

- A. "Hours today" *(current)*
- B. "Open today"

**"Find us" heading — 2 options:**

- A. "Find us" *(current)*
- B. "Where to find us"

**"Book a table" heading — 2 options:**

- A. "Book a table" *(current)*
- B. "Reserve your table"

---

## 📋 `/menu` MENU HUB

### Hero

**Where:** Lovable component (hardcoded) — currently says "The Kitchen & Bar" / "Made fresh. Priced honest. Worth every bite."

**Headline — 3 options:**

- A. **THE KITCHEN & BAR.** *(current)*
- B. **EVERYTHING WE COOK.**
- C. **THE MENU.**

**Subhead — 3 options:**

- A. "Made fresh. Priced honest. Worth every bite." *(current)*
- B. "Lunch, dinner, cocktails, brunch. Modern Mexican on Monroe."
- C. "From street tacos to the $129 Feast. Modern Mexican, four ways to spend an hour."

### Daypart cards (4-up)

**Lunch card:**
- A. "Lunch — Burritos, Bowls, Tacos."
- B. "Lunch — Tue–Sat · 11am–5pm"
- C. "Lunch — Daytime Mexican on Monroe"

**Dinner card:**
- A. "Dinner — Elevated plates. Serious technique."
- B. "Dinner — 5pm to close. Carne Asada and beyond."
- C. "Dinner — Surf & Turf, the Feast, and the rest."

**Cocktails card:**
- A. "Cocktails — Craft drinks. Serious pours."
- B. "Cocktails — Espresso Margaritas. House Margaritas. Tequila flights."
- C. "Cocktails — Modern margaritas. Serious tequila."

**Brunch card** *(launching soon)*:
- A. Badge: "Launching Soon" — Body: "Sunday brunch is coming."
- B. Badge: "Coming Soon" — Body: "Brunch · Sundays · launching 2026."
- C. Badge: "Sundays soon" — Body: "Notify me when brunch drops."

---

## 🍽 `/menu/dinner` DINNER MENU

### Hero band

**Where:** Lovable component (hardcoded)

**Kicker — 3 options:**

- A. "Dinner service · 5pm – Close"
- B. "Tue–Sat after 5pm"
- C. "After 5pm at Uno Más"

**Headline — 3 options:**

- A. **DINNER.** *(current)*
- B. **DINNER ON MONROE.**
- C. **PLATES THAT SURPRISE PEOPLE.**

**Subhead — 3 options:**

- A. "Elevated plates. Serious technique." *(current)*
- B. "Modern Mexican. Skirt steak, tiger prawns, the $129 Feast. Built for the night you remember."
- C. "Carne Asada. Surf & Turf. The Feast. Raw Bar. This isn't what you think — that's the point."

**Primary CTA — 2 options:**

- A. "Reserve a table"
- B. "Book your table"

### Feast callout band

**Where:** Lovable component, above menu sections

**Kicker — 3 options:**

- A. "The move"
- B. "For the table"
- C. "The full spread"

**Headline — 2 options *(locked from Supabase menu_items, but framing flexible)*:**

- A. **THE UNO MÁS FEAST · $129**
- B. **THE FEAST · $129**

**Body — 3 options:**

- A. "A spread of signature dishes. Feeds 2–3. Carne Asada, Achiote Cilantro Shrimp, Al Pastor Chicken, cilantro lime rice, house-made black beans, salsa and tortillas."
- B. "Three signature plates. Rice and beans for the table. Salsa and tortillas to build with. Feeds 2–3, ends with everyone full."
- C. "Don't limit yourself to one plate when you can try it all. The Feast: Carne Asada, Achiote Shrimp, Al Pastor, all the sides. $129 covers it."

**CTA — 2 options:**

- A. "Reserve a table"
- B. "Order The Feast"

### Cross-link to cocktails (bottom of dinner page)

**Where:** Lovable component

- A. "Pair it with a cocktail → See the cocktail menu"
- B. "Need a drink? → See cocktails"
- C. "Cocktails → /menu/cocktails"

---

## 🌮 `/menu/lunch` LUNCH MENU

### Hero band

**Kicker — 3 options:**

- A. "Lunch · 11am – 5pm · Tue–Sat" *(current)*
- B. "Daytime menu · Tue–Sat 11–5"
- C. "Lunch on Monroe · Tue–Sat"

**Headline — 3 options:**

- A. **LUNCH.** *(current)*
- B. **DAYTIME MEXICAN.**
- C. **LUNCH ON MONROE.**

**Subhead — 3 options:**

- A. "Bowls. Burritos. Tacos. The 509." *(current)*
- B. "Burritos and bowls and the $23 509. Lunch at Uno Más, Tue through Sat."
- C. "The 509. The Zag. The Notorious P.I.G. Lunch around here has names."

**Hours footer — LOCKED** *(after fact-corrections prompt)*: "Lunch service · Tue–Sat · 11am–5pm"

### Cross-link to dinner (bottom)

- A. "Hungrier? See the dinner menu →"
- B. "Stay for dinner →"
- C. "Dinner program → /menu/dinner"

---

## 🍹 `/menu/cocktails` COCKTAILS

### Hero band

**Kicker — 3 options:**

- A. "Craft cocktails · Serious tequila" *(current)*
- B. "The bar at Uno Más"
- C. "Modern margaritas · Indaba collab"

**Headline — 3 options:**

- A. **COCKTAILS.** *(current)*
- B. **THE BAR.**
- C. **MARGS AND BEYOND.**

**Subhead — 3 options:**

- A. "Modern margaritas. Indaba Coffee collab. The cleanest tequila program in Spokane." *(current)*
- B. "House margaritas, Espresso Margaritas with Indaba cold brew, and a tequila program built for the obsessed."
- C. "Espresso Margarita with Indaba cold brew. Frozen margaritas in rotating flavors. The Spokane bar tequila people fly in for."

### Espresso Margarita callout *(signature)*

**Where:** Lovable component above menu sections

**Kicker — 3 options:**

- A. "Signature · Uniquely Spokane"
- B. "The Indaba collab"
- C. "Only at Uno Más"

**Headline — 2 options:**

- A. **ESPRESSO MARGARITA · $15** *(current)*
- B. **THE ESPRESSO MARG · $15**

**Body — 3 options:**

- A. "Tequila blanco + Indaba cold brew + Baileys + agave. The Indaba Coffee collab you can't get anywhere else."
- B. "Tequila + Indaba cold brew + Baileys + agave. A Spokane collab in a glass. Order once and you'll order again."
- C. "Tequila blanco. Indaba cold brew. Baileys. Agave. Order it. That's the post."

---

## ☀️ `/menu/brunch` BRUNCH (stub for launch SEO)

### Hero band

**Status:** Brunch deferred. Page stub recommended for SEO.

**Kicker — 2 options:**

- A. "Brunch · Sundays · Launching 2026"
- B. "Coming Soon · Sundays"

**Headline — 3 options:**

- A. **BRUNCH IS COMING.**
- B. **SUNDAY BRUNCH ON MONROE.**
- C. **MEXICAN BRUNCH IN SPOKANE.**

**Body — 3 options:**

- A. "Modern Mexican brunch. Sundays. Launching soon — get on the list and we'll tell you the day it drops."
- B. "Sunday brunch at Uno Más. Mimosas, huevos rancheros, the whole spread. Drop your email and we'll let you know when service starts."
- C. "Spokane Mexican brunch. Coming Sundays. Be first in line — leave your email and we'll send the launch date."

**Email-capture form button — 2 options:**

- A. "Get On The List"
- B. "Tell me when"

---

## 📖 `/about` ABOUT

### Hero band

**Kicker — 3 options:**

- A. "Our Story"
- B. "Built in Spokane"
- C. "How we got here"

**Headline — 3 options:**

- A. **BUILT IN SPOKANE. FED BY MEXICO.**
- B. **MODERN MEXICAN. SPOKANE ORIGINAL.**
- C. **A CONVERTED GARAGE. THREE VENUES. ONE STORY.**

**Subhead — 3 options:**

- A. "A modern Mexican kitchen and tequila bar in a converted garage on Monroe. Three venues. One address. Get a little lost."
- B. "We started as a taco shop. We grew into a restaurant, a speakeasy, and a patio. All at 2020 N Monroe."
- C. "Three venues at one address on Monroe Street in Spokane. Modern Mexican kitchen. Tequila bar. Mezzanine speakeasy. Outdoor patio."

### Brand narrative section — LOCKED *(from brand intel)*

✅ Approved copy:
> Uno Más is a modern Mexican restaurant and tequila bar at 2020 N Monroe in Spokane. We run a lunch program and an elevated dinner program. We have a full craft cocktail menu. We have The Mezzanine — a speakeasy and private event space upstairs. We are a gathering place. We are a destination.
>
> The ground floor cantina operates out of a converted mechanic's garage. Inside, it feels like outside. Feels like somewhere else entirely. The room does most of the work.
>
> Tacos are something we do exceptionally well — they are not the entirety of what we are.

**Narrative section headline — 3 options:**

- A. **WE STARTED AS A TACO SHOP. WE GREW INTO SOMETHING MORE.**
- B. **MODERN MEXICAN ON MONROE.**
- C. **THE PLACE SPOKANE COMES BACK TO.**

### Three venues section (3-up)

**Section headline — 3 options:**

- A. **THREE VENUES. ONE ADDRESS.**
- B. **THE CANTINA. THE MEZZANINE. THE PATIO.**
- C. **ONE DOOR. THREE ROOMS.**

**The Cantina blurb:**
- A. "Ground floor. Converted garage. Lunch + elevated dinner + full bar. The room does the work."
- B. "Converted garage. Inside feels like outside. Lunch service, dinner program, full bar."

**The Mezzanine blurb:**
- A. "Upstairs. Speakeasy + private events. Leather, fireplace, low light. The kind of room where whatever you're celebrating actually feels celebrated."
- B. "The Mezzanine on Monroe. Speakeasy and private event venue. 35 seated. 75 standing. Karissa runs the room."

**The Patio blurb:**
- A. "Outdoor bar + street-food kitchen. Watch parties, big groups, sunny afternoons that turn into nights."
- B. "Spokane summer. Outdoor bar. Street-food kitchen. Patio sessions that run all day."

### Team section

**Section headline — 3 options:**

- A. **WHO YOU'RE TRUSTING WITH YOUR NIGHT.**
- B. **THE TEAM.**
- C. **MEET THE TEAM.**

**Bio for Ramsey Pruchnic (Owner) — 3 options:**

- A. "Built it. Runs it. Knows every regular by name."
- B. "Owner. Spokane native. Started as a taco shop, kept building."
- C. "Owner. Built the cantina. Runs the show. Has opinions about tequila."

**Bio for Karissa Schulke (GM / Events) — 3 options:**

- A. "If you're booking the Mezzanine, you're talking to Karissa. karissa@unomastacoshop.com"
- B. "GM and events lead. Runs the Mezzanine. Books private dinners. Reach her at karissa@unomastacoshop.com."
- C. "Events + Mezzanine. The person between you and a great night. karissa@unomastacoshop.com."

**Bio for Thomas Schulke (Operations) — 3 options:**

- A. "Keeps the lights on, the kitchen moving, the floor sharp."
- B. "Operations. Makes sure nothing on the back end blows up."
- C. "Behind every smooth service. Operations lead."

**Bio for Maraya Lindo (Executive Chef) — 3 options:**

- A. "Runs the kitchen. Carne Asada is hers. So is the Feast."
- B. "Executive Chef. The food is hers. The Feast is hers. Trust her."
- C. "Chef. Built the dinner program. The plates that surprise people start here."

### Proof points / stats band

**Section headline — 3 options:**

- A. **WHY PEOPLE COME BACK.**
- B. **WORTH PUTTING ON A SIGN.**
- C. **THE NUMBERS.**

**Stat captions:**
- 2022 — "Founded. 3+ years on Monroe." OR "On Monroe since."
- 107% — "How much more loyalty members spend." OR "Loyalty spend lift."
- 2× — "How often loyalty members visit." OR "Loyalty visit rate."
- 3 — "Venues at one address." OR "Distinct rooms."

### Visit strip *(footer-ish, bottom of about)*

**Headline — 3 options:**

- A. **FIND US.**
- B. **COME SEE THE ROOM.**
- C. **2020 N MONROE. ANY NIGHT.**

---

## 🍸 `/mezzanine` THE MEZZANINE ON MONROE

### Hero band — LOCKED 2026-05-28

✅ Locked copy:
- Kicker: *The Mezzanine on Monroe*
- Headline: **UPSTAIRS AT UNO MÁS, A QUIETER STORY.**
- Subhead: *The Mezzanine on Monroe. Speakeasy. Private events. Watch parties. The room that doesn't show up on the regular menu.*
- CTA: *Email Karissa*

### 3-stat callout band

**Stat 1: Capacity**
- A. "35-40 seated · 65-75 standing" + label "Capacity"
- B. "35 seated · 75 standing" + label "The Room"

**Stat 2: Private entrance**
- A. "Private entrance" + label "Discreet access from the alley"
- B. "Side entrance" + label "Skip the main floor"

**Stat 3: Hours**
- A. "Thu–Sat 7pm – late" + label "Open hours" *(if public hours exist)*
- B. "By appointment" + label "Private events any night"

### 3 event types (cards)

**Card 1: Private Dinners**

- A. Title: "PRIVATE DINNERS" — Body: "35-40 seated. Custom menus, full bar, dedicated server. Rehearsals, milestones, intimate corporate."
- B. Title: "PRIVATE DINNERS" — Body: "Sit-down dinners for 35-40. Custom menus from Chef Maraya. The Feast on a long table. Yours for the night."
- C. Title: "DINNER FOR YOUR PEOPLE" — Body: "Up to 40 seated. Bespoke menus. Full bar. Private staff. The dinner you'll keep telling people about."

**Card 2: Cocktail Receptions**

- A. Title: "COCKTAIL RECEPTIONS" — Body: "Up to 75 standing. Open bar, light bites, and an upstairs that doesn't feel like a banquet hall."
- B. Title: "RECEPTIONS + BUYOUTS" — Body: "Open bar, passed bites, 75-person standing capacity. Watch parties, after-parties, the kind of room your group actually fits in."
- C. Title: "PARTY OF UP TO 75" — Body: "Cocktail receptions, watch parties, networking events. We bartend, we serve, you show up."

**Card 3: Full Buyouts**

- A. Title: "FULL BUYOUTS" — Body: "Take the whole floor. Mezzanine + downstairs combo available for larger events. We'll build it around you."
- B. Title: "TAKE THE WHOLE ROOM" — Body: "Buy out the Mezzanine. Combine with downstairs for 200+. Wedding rehearsals, anniversaries, takeovers."
- C. Title: "TAKEOVER" — Body: "Mezzanine alone or the full venue. We work the menu, the bar, the layout to your night."

### What you get section (4 icons)

**Section headline — 3 options:**

- A. **WHAT YOU GET.**
- B. **THE ROOM INCLUDES.**
- C. **WHAT'S IN THE BOOKING.**

**Icon labels (4):**
- A. Sound system + lighting / Full craft bar / Fireplace + leather lounges / Dedicated event lead
- B. Music + lights / Open bar / Fireplace + leather / Karissa at every step
- C. Custom playlist / Full bartender / Fireplace, leather, low light / Your event lead

**Body paragraph — 3 options:**

- A. "Sound system. Lighting controls. A fireplace that's actually lit. Leather lounges. A private bar. A team that handles everything so you can just show up and be a guest at your own night."
- B. "Built-in sound. Dimmable lighting. A real fireplace. Custom playlist or live DJ. Your own bartender. Karissa handling logistics so you handle the toast."
- C. "Bar. Sound. Lights. Fireplace. Leather. A team that handles the part most hosts dread — so you get to enjoy your own party."

### Brand quote band (centered)

**Quote (Electric Pink, large) — 3 options:**

- A. *"What happens when a speakeasy and a rooftop bar decide to share a space."* (brand-intel approved)
- B. *"The room you book when you mean it."*
- C. *"Upstairs, it gets quieter. Better."* (brand-intel approved)

### Inquire band (bottom CTA)

**Headline — 3 options:**

- A. **PLAN YOUR EVENING.**
- B. **BOOK THE ROOM.**
- C. **GET THE KEYS.**

**Body — 3 options:**

- A. "Karissa runs Mezzanine events. The fastest way to lock something in is to email her with your date and guest count."
- B. "Tell us the date, the guest count, the vibe. Karissa builds the rest. Same-day response, every time."
- C. "Email Karissa with your night. She'll send back a plan within 24 hours."

**CTA — 2 options:**

- A. "Email Karissa"
- B. "Plan the night"

### Cross-link back to Uno Más (small bottom link)

- A. "Looking for the dinner menu? → unomastacoshop.com/menu/dinner"
- B. "Downstairs? → /menu/dinner"
- C. "Uno Más main menu → /menu"

---

## 🎉 `/private-events` PRIVATE EVENTS + CATERING

### Hero band

**Kicker — 3 options:**

- A. "Private Events · Catering · Buyouts"
- B. "Karissa-led private events"
- C. "Events at Uno Más"

**Headline — 3 options:**

- A. **WHATEVER YOU'RE CELEBRATING DESERVES THE ROOM.**
- B. **EVENTS BUILT AROUND YOU.**
- C. **THREE VENUES. ONE TEAM. ANY OCCASION.**

**Subhead — 3 options:**

- A. "Three venues. Twenty guests to two hundred. Mezzanine dinners, patio takeovers, full buyouts, off-site catering."
- B. "From 20 to 200+. Mezzanine private dinners, patio takeovers, full restaurant buyouts. Plus off-site catering when you bring the party home."
- C. "Mezzanine dinners. Patio takeovers. Full buyouts. Off-site catering. We staff it, plate it, pour it — you toast."

**CTA — 2 options:**

- A. "Inquire"
- B. "Email Karissa"

### 4 event types (cards) — capacities locked, descriptions flex

**Mezzanine Dinners (35-40 seated · 65-75 standing):**
- A. "Upstairs. Private entrance. Full bar. Leather lounges and a fireplace. The kind of room where whatever you're celebrating actually feels celebrated."
- B. "Sit-down dinners for 35-40 in the Mezzanine. Private bar, custom menus, dedicated staff."

**Patio Takeovers (40-80 standing):**
- A. "Outdoor bar. Street-food kitchen. Daytime energy that runs into the night."
- B. "Buy out the patio. Outdoor bar + grill. Watch parties, summer happy hours, milestones in the sun."

**Full Buyouts (150-200+):**
- A. "All three spaces. Custom menu options. We handle the room, you handle the toast."
- B. "The whole venue. Cantina, Mezzanine, Patio. Custom menus, full staff, your night start-to-finish."

**Off-Site Catering (25-500+):**
- A. "We bring it to you. Tacos, plates, full setups. Quote within 24 hours."
- B. "Off-site. We pack it, deliver it, set it up. Office lunches to weddings. Quote in 24 hours."

### "What's included" 3-icon row

**Section headline — 3 options:**

- A. **WHAT'S INCLUDED.**
- B. **WHAT YOU GET.**
- C. **EVERY EVENT INCLUDES.**

**Icon labels:**
- A. "Custom menus tailored to your group" / "Full bar + craft cocktails" / "Dedicated event coordinator (Karissa)"
- B. "Custom menu" / "Full bar" / "Karissa runs your event"

### "How it works" 3-step section

**Section headline — 3 options:**

- A. **HOW IT WORKS.**
- B. **THE PROCESS.**
- C. **HOW TO BOOK.**

**Step 1 — 2 options:**

- A. "Tell us about your event → fill the inquiry form OR email karissa@unomastacoshop.com"
- B. "Send us the date, guest count, vibe. Form or email."

**Step 2 — 2 options:**

- A. "We build a proposal → menu, pricing, layout, timing — usually back to you within 24-48 hours"
- B. "Karissa sends a custom plan within 48 hours. Menu, pricing, layout, timing."

**Step 3 — 2 options:**

- A. "You show up. We handle the rest. → from setup to cleanup, you're a guest at your own event."
- B. "Day-of, just show up. We staff, plate, pour, clean. You toast."

### Inquiry form intro

**Heading above the form — 3 options:**

- A. **SEND US YOUR NIGHT.**
- B. **TELL US ABOUT YOUR EVENT.**
- C. **THE INQUIRY FORM.**

**Form CTA button — 2 options:**

- A. "Send Inquiry"
- B. "Send to Karissa"

### Footer band

**Closing line — 3 options:**

- A. "Talking with Karissa is the fastest path. karissa@unomastacoshop.com · (509) 960-7989"
- B. "Faster than the form? Email karissa@unomastacoshop.com or call (509) 960-7989."
- C. "Skip the form. karissa@unomastacoshop.com · (509) 960-7989."

---

## 📞 `/contact` CONTACT

### Hero (tight, not full-bleed)

**Kicker — 3 options:**

- A. "Say hello"
- B. "Reach us"
- C. "Contact"

**Headline — 3 options:**

- A. **CONTACT US.**
- B. **GET IN TOUCH.**
- C. **HOW TO REACH UNO MÁS.**

**Subhead — 3 options:**

- A. "Reservations, private events, press, or just to say you loved the Birria."
- B. "Reservations via Resy. Events to Karissa. Press to tacos@unomastacoshop.com. We get back within a day."
- C. "Reservations, events, press, the rest. Pick the right address below — you'll hear back."

### Section headings

**"Find us" — 2 options:**

- A. "Find us"
- B. "Where to find us"

**"Hours" — 2 options:**

- A. "Hours"
- B. "When we're open"

### Cross-streets line (locator detail)

- A. "Behind Indaba Coffee. Corner of Knox Ave & N Monroe."
- B. "Between Knox and Shannon on N Monroe. Behind Indaba Coffee."

### Quick action cards (3-up)

**Reserve a table card:**
- A. "Reservations → Resy"
- B. "Book a table → Resy"

**Plan an event card:**
- A. "Plan an event → karissa@"
- B. "Private events → Email Karissa"

**Press / partnerships card:**
- A. "Press / partnerships → tacos@"
- B. "Press → tacos@unomastacoshop.com"

### Social section

**Heading — 3 options:**

- A. **FOLLOW US.**
- B. **WHERE TO FIND US ONLINE.**
- C. **SOCIAL.**

---

## 📅 `/reservations` RESERVATIONS

### Hero band

**Headline — 3 options:**

- A. **YOUR MOVE.**
- B. **RESERVE A TABLE.**
- C. **BOOK A TABLE.**

**Subhead — 3 options:**

- A. "Reservations recommended for dinner. Walk-ins always welcome."
- B. "Book via Resy. Walk-ins welcome anytime. Mezzanine events through Karissa."
- C. "Dinner reservations recommended. Walk-ins always open. Mezzanine bookings → Karissa."

### Walk-in note

- A. "Walk-ins always welcome — we're not that kind of place."
- B. "Walk-ins welcome. No reservation, no problem."
- C. "Walk-ins are how most people find us."

### Mezzanine cross-link (small)

- A. "Booking the Mezzanine? → /mezzanine"
- B. "Private events upstairs → /mezzanine"

---

## 👷 `/now-hiring` NOW HIRING

### Hero band

**Kicker — 3 options:**

- A. "Now hiring"
- B. "Jobs at Uno Más"
- C. "We're hiring on Monroe"

**Headline — 3 options:**

- A. **GOOD PEOPLE. GOOD WORK. GOOD PAY.**
- B. **WE'RE HIRING.**
- C. **BUILD A CAREER ON MONROE.**

**Subhead — 3 options:**

- A. "Uno Más is hiring — front and back of house. If you take your craft seriously and work well with others, we want to talk."
- B. "Hiring front and back of house. Tip pool for everyone. Apply below."
- C. "Looking for servers, bartenders, cooks, and event staff. Apply through the form below."

### "Why work here" section

**Heading — 3 options:**

- A. **WHY UNO MÁS.**
- B. **WHY WORK HERE.**
- C. **WHAT MAKES US DIFFERENT.**

**Body — 2 options:**

- A. "We run a full lunch and dinner program at 2020 N Monroe — elevated food, a serious bar, and a team that actually functions like one.  We pay competitively based on experience. Every role — front and back — is part of the tip pool. That's not common. It's intentional. We believe good service is a team effort, and we compensate everyone accordingly."
- B. "Full-service modern Mexican on Monroe. We pay above market. Front and back of house both share tips — uncommon, intentional. We run dinner like a real program and we'd rather train someone great than poach someone tired."

### Role categories (3-up)

**Front of House — 2 options:**
- A. "Servers, bartenders, host staff"
- B. "FOH — servers, hosts, bar team"

**Back of House — 2 options:**
- A. "Line cooks, prep, dishwashers"
- B. "BOH — line, prep, dish"

**Events / Mezzanine — 2 options:**
- A. "Event coordinator support"
- B. "Mezzanine event team"

### Form fallback note

- A. "Issues with the form? Email tacos@unomastacoshop.com with your résumé and the role you're interested in."
- B. "Form not loading? Email résumé to tacos@unomastacoshop.com."

---

## 📦 `/fiesta-box` FIESTA BOX — LOCKED 2026-05-28

✅ All copy locked per Ramsey 2026-05-28. See `LOVABLE-PROMPT-fiesta-box-standalone.md`.

Key elements:
- Hero: "10 STREET TACO FIESTA BOX." / "Perfect for date night, a cozy dinner, or when you just want Uno Más at home."
- How It Works (5 steps)
- What You Get (Taco Kit for Two, 10 street tacos, 5 items)
- Level Up With Add-Ons (Marg To-Go, Chip & Dip Trio, Churro 3-Pack)
- "WE'VE GOT YOU." bottom band
- Fine print: reheating + 21+

---

## ⚖️ `/privacy-policy` PRIVACY POLICY

**Status:** Single approved version in `LOVABLE-PROMPT-missing-launch-pages.md`. No options needed for legal text.

Heading — 2 options:
- A. **PRIVACY POLICY.**
- B. **OUR PRIVACY POLICY.**

---

## 🌐 SITE-WIDE — Header, Footer, CTAs, 404

### Header nav labels

**Where:** Lovable component (hardcoded)

| Slot | Current | Option B | Option C |
|---|---|---|---|
| Home | (logo) | (logo) | (logo) |
| Menu | "Menu" | "The Menu" | "Eat" |
| Reservations | "Reservations" | "Book" | "Reserve" |
| Mezzanine | "The Mezzanine" | "Mezzanine" | "Upstairs" |
| About | "About" | "Our Story" | "About Us" |

### Header CTA button

- A. "Reserve a table" *(current)*
- B. "Book"
- C. "Reserve"

### Footer

**Tagline below logo:**
- A. "Get a little lost." *(brand tagline — recommend keep)*
- B. "Modern Mexican on Monroe."

**Column 1 heading — 2 options:**
- A. "Visit"
- B. "Find us"

**Column 2 heading — 2 options:**
- A. "Explore"
- B. "Pages"

**Column 3 heading — 2 options:**
- A. "Stay in touch"
- B. "Reach us"

**Copyright line:**
- A. "© 2026 Uno Más Tacos & Tequila"
- B. "© 2026 Uno Más Tacos & Tequila · 2020 N Monroe · Spokane WA"

### Common buttons (site-wide CTAs)

Pick a single version for each so they're consistent everywhere.

**Resy reservation button label:**
- A. "Reserve a table"
- B. "Book a table"
- C. "Reserve at Resy"

**Email Karissa button (events):**
- A. "Email Karissa"
- B. "Inquire"
- C. "Plan an event"

**Toast online ordering button (Fiesta Box, etc.):**
- A. "Order Online"
- B. "Order A Fiesta Box" *(Fiesta Box specific)*
- C. "Pickup Order"

**Menu navigation CTA (homepage hero etc.):**
- A. "See the menu"
- B. "Open the menu"
- C. "Browse the menu"

### Custom 404 page

**Headline — 3 options:**

- A. **GOT A LITTLE TOO LOST.**
- B. **404. NOT THIS PAGE.**
- C. **NOTHING HERE. WANDER BACK.**

**Subhead — 2 options:**

- A. "This page doesn't exist. Wander back to one of these:"
- B. "Wrong door. Try one of these:"

**Card link labels:**
- A. /menu/dinner / /menu/lunch / /mezzanine / /
- B. "Dinner menu" / "Lunch menu" / "The Mezzanine" / "Homepage"

---

## ✅ DECISIONS LOG (mark your picks here for bulk update)

When you've gone through the doc, fill in this table so I can bulk-update.

| Page / section | Locked pick | Where it lives |
|---|---|---|
| / hero kicker | | site_content |
| / hero headline | | site_content |
| / hero subhead | | site_content |
| / hero CTAs | | site_content |
| / venues-intro | | site_content |
| / dinner-feature | | site_content |
| / testimonials heading | | site_content |
| / Cantina Club teaser | | Lovable component |
| /menu hub hero | | Lovable component |
| /menu/dinner hero + Feast | | Lovable component + site_content |
| /menu/lunch hero | | Lovable component |
| /menu/cocktails hero | | Lovable component |
| /menu/brunch stub | | Lovable component |
| /about all sections | | site_content + Lovable component |
| /mezzanine all sections | | Lovable component (hero locked in site_content) |
| /private-events all sections | | Lovable component |
| /contact all sections | | Lovable component |
| /reservations | | Lovable component |
| /now-hiring | | Lovable component |
| Header nav | | Lovable component |
| Footer | | Lovable component |
| 404 page | | Lovable component |

---

## 📦 How I'll apply your picks

Once this doc is marked up:

1. **All `site_content` rows** → single SQL transaction that updates Supabase. Live within minutes.
2. **All Lovable component changes** → consolidated into ONE Lovable prompt to paste, covering every hardcoded copy change at once.
3. **Master MD updated** with anything that's brand-strategic (taglines, voice direction, banned/preferred phrasing if it shifts).
4. **Backlog updated** with anything we intentionally defer.

---

*Edit freely. Add options. Delete things. Reorganize. This doc is yours to mark up. When you're ready, just tell me "decisions locked" and I'll push the bulk update.*
