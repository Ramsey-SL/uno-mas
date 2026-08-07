# Cantina Club / Loyalty + Marketing-Migration — RESUME HERE

*Session handoff · last updated 2026-08-07. Pick up the Cantina Club + loyalty + marketing-platform work from here on any device. Read this first, then the linked files.*

---

## TL;DR — where we are
Building **Uno Más Rewards: The Cantina Club** as **ONE tiered program**: a **FREE tier live now** (the current Toast loyalty) + **PREMIUM paid tiers coming later** (a few weeks out — NOT public yet). In parallel: migrating marketing off Klaviyo (email→Toast, SMS→Toast/Twilio) to save ~$150/mo, and standing up a messaging framework + rewards webpage.

**Active task:** finish the **messaging framework** (answer the 8 questions below), then **repopulate the rewards webpage** from it, then graphics + real build.

---

## ⭐ KEY DECISION (2026-08-07)
- **One program, tiered.** Free Toast loyalty = the entry tier of "The Cantina Club." Premium paid tiers become an *extension* of it. **Do NOT rename to "Más Rewards"** (earlier idea — overridden). Keep **"Uno Más Rewards: The Cantina Club."**
- Premium tiers are **not public yet.** Public materials show only the free program (+ a soft "more coming" teaser).

---

## ❓ OPEN QUESTIONS — answer these next
*(Full framework w/ drafts: `brand-intelligence-center/cantina-club-messaging-framework.md`)*

1. **Premium tiers (the big one):** how many, names (keep Cantina Member / OG / La Familia?), prices ($25/$50/$99 · founding $225/$450/$900?), which perks are premium vs. free, and **the single reason to upgrade when the free tier already pays 10% back.**
2. In one sentence — the **feeling** you want a member to have.
3. Pick the **promise one-liner** ("The more you come, the more you get" / "Rewards for the regulars" / "Become a regular, get treated like one" / your own).
4. Free tier: lead with **value** ($10 + 10% back) or **belonging**? *(recommend value hook.)*
5. Growth focus: **convert first-timers** vs **deepen best regulars**?
6. **Hero hook/tagline** for the club.
7. **Free-item reward** name (e.g., "1 Free House Margarita") + do Toast **points expire**?
8. Confirm/reprioritize the **4 message pillars** (§6 of the framework).

---

## WORKSTREAM STATUS

### 1. Messaging framework — IN PROGRESS
- File: `brand-intelligence-center/cantina-club-messaging-framework.md` (drafts filled; answer the 8 Qs above).
- Extends the brand `brand-intelligence-center/messaging-framework.md` (StoryBrand + Golden Circle).

### 2. Rewards webpage — MOCKUP for approval
- Local mockup now in the repo: **`website/cantina-club-rewards-mockup/index.html`**.
- View it: open the file in a browser, or `cd` into that folder and run `python3 -m http.server 8899` → http://localhost:8899.
- Status: hero reworked to explain + sell the club; pop-up signup + inline form (front-end only). **Awaiting: finalize messaging framework → repopulate → approve → graphics + real build.**
- Real-build note: Toast's hosted signup page can't be restyled/iframed — plan is a branded page + pop-up that hands off to Toast enrollment.

### 3. Toast loyalty program — LIVE, optimize
- Current config: **$10 just for joining** (100-pt signup bonus) · **1 pt/$1** · **$10 back every 100 pts (10%)** · **$10 birthday**. Signup = phone number.
- Named "Uno Más Cantina Club" in Toast — keep (per decision).
- TODO in Toast: finish the **Free Item Reward** (needs name + eligible item); turn **ON "Day & time bonus" 2× points** for Sunday brunch / slow nights; consider Dining-option 2× for online orders.
- Playbook (mechanics/copy/team script/flows): `marketing/mas-rewards-loyalty-playbook.md` *(ignore its "Más Rewards" naming — superseded; treat as The Cantina Club free tier).*

### 4. Marketing platform migration — IN PROGRESS
- **Email → Toast.** Combined + deduped list built: `Toast_Email_Upload_READY.csv` (**4,222** opted-in emails). Upload via Toast → Email Marketing → Subscribers → Upload + certify consent.
- **SMS.** Toast now allows SMS upload too; also built a **Twilio SMS engine inside the app** (staff `/sms` console) as the cheaper option (~$60–130/mo vs SlickText $169–319). Master list: `Uno_Mas_SMS_MASTER_READY.csv` (**6,280**, tiered: 1,464 verified / 2,887 loyalty / 1,929 asserted) + `SimpleTexting_SMS_Upload_READY.csv`.
- **Consent reality:** only **1,464 verified** SMS-consented (Klaviyo "All SMS Subscribers"); the rest need a **"reply YES" re-opt-in** before texting. Loyalty numbers (3,479) = strong basis, still re-confirm.
- **Klaviyo** ≈ $150/mo — cancel once email is uploaded + SMS list is imported. Verified email opt-in list ~6,249 (Klaviyo "Uno Mas - Marketing Opt In").
- Data files live on LaCie: `"/Volumes/lacie-exter/Google Drive/Uno_Mas_HQ /Uno Mas Customer Database/"` (+ `Loyalty Database/`). Klaviyo raw exports + consent-mapped file in `~/Downloads/`.
- If SMS via Twilio: needs Twilio account + **10DLC** (1–2 wk) + secrets `TWILIO_ACCOUNT_SID` / `TWILIO_AUTH_TOKEN` / `TWILIO_MESSAGING_SERVICE_SID`; inbound webhook `…/api/public/webhooks/twilio-sms`.

### 5. Cantina Club APP ("Cantina Connect", Lovable) — BUILT in preview, NOT published
- **Lovable project id:** `9e76084a-a5cc-4ca3-8a3f-82ec78aa3f10` · editor `https://lovable.dev/projects/9e76084a-a5cc-4ca3-8a3f-82ec78aa3f10` · preview base `https://id-preview--9e76084a-a5cc-4ca3-8a3f-82ec78aa3f10.lovable.app`
- **Demo staff login:** `demo@unomas.com` / `CantinaClub2026!`
- **Built:** staff console (member search/add, redeem partial credit, log visit, perk buttons, savings + credit-redeemed "total value", 21+ verification, giveaway leaderboard, analytics, staff-signup attribution); member portal + `/portal/demo`; marketing pages `/welcome /program /member-experience /join`; `/demo` hub (PWA add-to-home-screen); Stripe subscriptions (15th-of-month proration); Twilio SMS engine `/sms`.
- **⚠️ DB is PAUSED** (Supabase idled out over the long gap) — resume it in Lovable/Supabase before the app works again; then apply the pending SMS-tables migration.
- **Pending to go live:** connect Stripe test key; wire real email (Resend/SMTP) for portal magic links; Twilio keys + 10DLC; build the giveaway "draw a winner" (dice/wheel — spec in session); customer portal → live (phone OTP before launch). Nothing published; preview links are unlisted (share carefully).
- Full detail also in the `project_cantina_club_app` assistant memory.

---

## DESIGN ASSETS / PROMPTS
- **Keychain tiers (paid club):** Cantina Member = TEAL (NippyCustom Y12) · Cantina OG = PINK (Y14) · La Familia = GOLD (Y59 or black + gold engraving). Member number on the back. Full ChatGPT design prompt was produced in-session (regenerate if needed).
- **Graphic/design prompts** for social + email + table tents live inside `marketing/weekend-campaigns-and-flows.md` and `marketing/mas-rewards-loyalty-playbook.md`.

---

## MARKETING CONTENT PRODUCED THIS SESSION (in repo)
- `marketing/weekend-campaigns-and-flows.md` — weekend traffic push (locked offer: **$10 off $60, Fri–Sun** + Sunday brunch reminder; code word **"Más Please"**) + always-on email/SMS nurture flows.
- `marketing/mas-rewards-loyalty-playbook.md` — loyalty program design, webpage copy, tabletop, team script + staff incentives, email/SMS flows (naming superseded — it's The Cantina Club free tier).
- `brand-intelligence-center/cantina-club-messaging-framework.md` — the framework (this is the current source of truth to finish).
- `website/cantina-club-rewards-mockup/index.html` — the webpage mockup.

---

## GUARDRAILS
- **Premium/paid Cantina Club is NOT public yet** — public materials = free program only.
- **21+** applies to the paid club's alcohol perks (app enforces DOB + ID check at signup) — the free loyalty program is all-ages.
- **Brand name:** always "Uno Más" (accent); program always "Uno Más Rewards: The Cantina Club," never "loyalty program."
- **SMS compliance:** first message includes "Reply STOP to opt out"; re-opt-in the non-verified list before marketing to them; keep single-segment (no emoji/accents) when 160-char matters.

---

## IMMEDIATE NEXT ACTIONS
1. Answer the **8 questions** → I finalize the messaging framework.
2. **Repopulate the rewards webpage** from the framework → approve.
3. Fire **graphics** to the design agent → **build the real page + site-wide pop-up** (Toast hand-off).
4. In Toast: finish Free Item Reward + turn on Day&time 2× for brunch.
5. Upload `Toast_Email_Upload_READY.csv`; decide SMS platform (Toast vs Twilio) + run the re-opt-in; then cancel Klaviyo.
