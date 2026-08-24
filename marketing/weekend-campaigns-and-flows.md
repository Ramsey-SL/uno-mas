# Uno Más — Weekend Traffic Campaigns + Nurture Flows

> ## 🔴 THE OFFER IN THIS DOC IS RETIRED (2026-08-23)
> **"Spend $60, get $10 off" was the FIRST weekend test and it is OVER.** Every reference to it
> below — subject lines, SMS copy, brunch nudges — is **retired creative**, useful as a template
> only. Do not send it.
>
> **Weekend offers are a rotating weekly TEST, not a standing offer.** Current status and the full
> test history live in **`marketing/campaigns/weekend-promos/executions-log.md`** — check there
> before writing any weekend copy.
>
> The always-on nurture flows further down this doc (welcome, win-back, birthday, post-visit) are
> **still valid** — only the weekend spend-threshold offer is retired.

**Platform:** Toast (email + SMS) · **Audience:** full guest list
**Voice:** relaxed, friendly, Spokane, tacos & tequila, "one more." Never corporate.
**Note:** Cantina Club is intentionally left OUT of these (not public yet). A club-launch flow comes later.

**Fill these in before sending:** `[BRUNCH DAYS/HOURS]` · `[RESERVE LINK]` (your Resy/OpenTable/booking link) · `[OFFER]` (see below) · `[MENU LINK]`

---

## ⭐ LOCKED OFFER — this weekend
**~~Spend $60 this weekend (Fri–Sun), get $10 off.~~ RETIRED 2026-08-23 — first test, now over.** Redemption: "show this text/email at your table" (simplest) or set up a Toast promo code (e.g., `WEEKEND10`). Focus send: **Sunday brunch reminder.**

### Finalized sends (fill `[BRUNCH HOURS]` + `[RESERVE LINK]`)

**Friday — Email**
Subject A: `$10 on us this weekend 🌮` · Subject B: `Spend $60, save $10 — Fri thru Sun`
Preheader: `Tacos, margs, Sunday brunch — $10 off when you hit $60.`
> Weekend's here — and so is a little something from us.
> Spend **$60 this weekend (Fri–Sun)** and we'll take **$10 off**. Tacos, margaritas, the whole table.
> And save room for **Sunday brunch** — [BRUNCH HOURS], $6 margs and everything you show up for.
> **[Reserve your table →]([RESERVE LINK])** · Just show this at your table.
CTA: Reserve a table

**Friday — SMS**
> Uno Más 🌮 This weekend: spend $60, save $10 (Fri–Sun). Tacos, margs & Sunday brunch. Reserve: [RESERVE LINK] — show this text to redeem. Reply STOP to opt out.

**Saturday night — SMS (Sunday brunch teaser)**
> Uno Más ☀️ Brunch tomorrow! Sunday [BRUNCH HOURS] — $6 margs + your $10-off-$60 still good all weekend. Save a seat: [RESERVE LINK]. Reply STOP to opt out.

**Sunday morning — SMS (the reminder)**
> Uno Más 🍳 Sunday brunch is ON — [BRUNCH HOURS]. Bring the crew, grab $10 off $60, we'll handle the mimosas. Walk in or reserve: [RESERVE LINK]. Reply STOP to opt out.

**Sunday morning — Email (optional)**
Subject: `Sunday brunch is calling 🍳`
> Slow morning? Make it a good one. Brunch today [BRUNCH HOURS] — $6 margs, and $10 off when you spend $60. **[Reserve →]([RESERVE LINK])**

*(Section A below is the original reference sequence; the finalized copy above supersedes it for this weekend.)*

---

# SECTION A — This-Weekend Traffic Push (one-time sends)

**Cadence:**
| When | Channel | Purpose |
|---|---|---|
| Thursday ~11am | Email | Announce the weekend + brunch |
| Friday ~4pm | Email + SMS | Reservation push ("lock your table") |
| Saturday ~9am | SMS | Day-of brunch nudge |
| Sunday ~9:30am | SMS | Last-call brunch |

### 1) Thursday — Email (announce)
**Subject A:** Brunch is back this weekend 🍳🍹
**Subject B:** Your weekend plans, sorted
**Preheader:** Bottomless mimosas, $6 margs, and a table with your name on it.
**Body:**
> Weekend's almost here — and so is brunch.
>
> Join us **[BRUNCH DAYS/HOURS]** for the good stuff: our full brunch spread, **bottomless mimosas for $15** with any entrée, and margaritas that make Saturday feel like a story.
>
> Tables fill up fast. Grab yours before they're gone.
>
> **[Reserve your table →]([RESERVE LINK])**
>
> See you soon. One more reason to get a little lost at Uno Más. 🌮
**CTA button:** Reserve a table

### 2) Friday — Email (reservations)
**Subject A:** Don't wing your Saturday
**Subject B:** Weekend tables are going fast
**Preheader:** Reserve now — brunch + margs are calling.
**Body:**
> This weekend's looking busy (in the best way). If brunch or a margarita night is in your plans, lock it in now so you're not waiting at the door.
>
> 🍳 Brunch **[BRUNCH DAYS/HOURS]** · 🍹 $15 bottomless mimosas · tacos & tequila all day
>
> **[Reserve your table →]([RESERVE LINK])**
**CTA button:** Reserve now

### 3) Friday — SMS
> Uno Más 🌮 Weekend's here — brunch Sat & Sun + $15 bottomless mimosas. Lock your table before we fill up: [RESERVE LINK]
> Reply STOP to opt out.

### 4) Saturday morning — SMS
> Uno Más 🍳 Brunch is ON today [BRUNCH HOURS]. Bottomless mimosas $15 + $6 margs. Walk in or reserve: [RESERVE LINK]
> Reply STOP to opt out.

### 5) Sunday morning — SMS (last call)
> Uno Más ☀️ Last call for weekend brunch — today [BRUNCH HOURS]. Bring the crew, we'll bring the mimosas. Reserve: [RESERVE LINK]
> Reply STOP to opt out.

**SMS rules:** always include "Reply STOP to opt out" on the first send of a series, keep to 1 segment where possible, don't exceed ~3–4 promo texts/week.

---

# SECTION B — Always-On Nurture Flows (Toast automations)

These run automatically off guest behavior. Toast supports Welcome, Win-back, and Birthday as native automated campaigns; the weekend reminder is a recurring scheduled campaign; post-visit depends on your Toast plan.

### Flow 1 — Welcome (new subscriber / first-time guest)
**Trigger:** joins list / first order. **Goal:** second visit fast.
- **Msg 1 — Email, immediately:**
  Subject: *Welcome to the family 🌮*
  > You're in. Here's what that gets you: first dibs on specials, the occasional treat, and zero spam. Come see us — brunch, tacos, and the best margarita in Spokane are waiting.
  > **[See the menu →]([MENU LINK])** · **[Reserve →]([RESERVE LINK])**
- **Msg 2 — SMS, +1 hour:**
  > Uno Más 🌮 Thanks for joining! Here's a little welcome: [OFFER — e.g., free churros on your next visit]. Show this text. Reply STOP to opt out.
- **Msg 3 — Email, +3 days (if no visit):** brunch invite (reuse Section A Thursday email).

### Flow 2 — We Miss You / Win-back
**Trigger:** no visit in 45 days. **Goal:** reactivate.
- **Msg 1 — Email:**
  Subject: *It's been a minute…*
  > We saved you a seat. Come back this week and it's **[OFFER — e.g., a free app / $10 off $40]** — our way of saying we miss you.
  > **[Reserve →]([RESERVE LINK])**
- **Msg 2 — SMS, +4 days (if still no visit):**
  > Uno Más 🌮 We miss you! [OFFER] this week — come get lost with us again: [RESERVE LINK]. Reply STOP to opt out.

### Flow 3 — Birthday
**Trigger:** birthday month. **Goal:** celebration visit (groups spend more).
- **Msg 1 — Email, start of birthday month:**
  Subject: *It's your month — let's celebrate 🎉*
  > Birthdays were made for margaritas. Come in this month and **[OFFER — e.g., a free birthday dessert + marg]** is on us. Bring your people.
  > **[Reserve the party →]([RESERVE LINK])**
- **Msg 2 — SMS, on/near birthday:**
  > Happy birthday from Uno Más! 🎂🍹 Your free [birthday treat] is waiting this month. Reserve: [RESERVE LINK]. Reply STOP to opt out.

### Flow 4 — Post-Visit Thank-You → Review → Rebook
**Trigger:** ~3 hours after a visit (if Toast exposes visit event). **Goal:** reviews + repeat.
- **Msg 1 — Email/SMS, same evening:**
  > Thanks for coming in tonight 🌮 Hope it was a good one. If we earned it, a quick review means the world: **[Google review link]**
- **Msg 2 — Email, +5 days:** "Come back for brunch this weekend" (soft rebook + Section A hook).

### Flow 5 — Weekly Weekend Reminder (recurring scheduled)
**Schedule:** every **Thursday ~11am**, to engaged guests.
- Rotate the Section A Thursday email/SMS. This is your steady drumbeat — the single highest-leverage recurring send for weekend covers.

---

## Toast mapping cheat-sheet
| This doc | In Toast |
|---|---|
| Weekend push (Section A) | One-time scheduled Email + SMS campaigns |
| Welcome (Flow 1) | Automated "new guest / welcome" campaign |
| Win-back (Flow 2) | Automated "we miss you / lapsed" campaign |
| Birthday (Flow 3) | Automated birthday campaign |
| Weekly reminder (Flow 5) | Recurring scheduled campaign |
| Post-visit (Flow 4) | Only if your Toast plan exposes the visit trigger; else skip or send manually |

## Guardrails
- **SMS:** every series' first message carries "Reply STOP to opt out"; cap promos ~3–4/week; keep to 1 segment when you can (watch length).
- **Email:** one clear CTA per send (Reserve or Menu). Subject lines short. Test-send to yourself first.
- **No Cantina Club** references until it's public.
