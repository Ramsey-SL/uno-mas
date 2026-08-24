# Send Plan — Week of Mon Aug 24, 2026

**Platform:** Toast (email + SMS) · **Audience:** Cantina Club / marketing list
**Goal:** lift **Wednesday and Thursday**, the two soft days · **Created:** 2026-08-23

---

## The week at a glance

| Day | Send | Carries | Why |
|---|---|---|---|
| **Tue Aug 25** | **SMS** | Taco Tuesday + tease Wednesday's gift card | Tuesday already works — use it to prime the soft day |
| **Wed Aug 26** | **Email** | 🎁 **Gift card promo launch** + Beer & Bites + Late Night announce | Soft day, and the promo's first day. Email carries the most explanation. |
| **Thu Aug 27** | **SMS** | Big F'N Thursday + gift card + Late Night tease | Soft day. Short, high-intent. |
| **Fri Aug 28** | ⭐ **SMS — recommended add** | Late Night LAUNCH + gift card | Biggest news of the week. Drafted and ready. |

---

## ⚠️ The gap: Friday is your biggest news of the week and has no send

**Late Night launches Friday Aug 28** — a brand-new daypart. Right now nothing announces it on the
day it starts. Thursday's SMS teases it, but a new program launching with no launch-day send is a
missed shot.

**Recommend one short Friday SMS**, sent ~4pm:
> `Late Night starts tonight. 8-10pm: two street tacos $10, $6 margs, $7 palomas, $30 pitchers. Spend $50, take a $10 gift card home.`
*(GSM-7, 132 units, single segment)*

Four sends in a week is a lot for the same list. If that's too much, **drop Thursday's SMS and move
it to Friday** — Friday has genuinely new news, Thursday is a recurring special the list already
knows. Your call; I'd take the Friday send.

---

## 🔴 SMS encoding rule — this changes how we write every text

**"á" is not in the GSM-7 character set.** Writing **"Uno Más"** in an SMS body forces the whole
message into UCS-2 encoding, which drops the single-segment limit from **160 characters to 70** —
so a normal-length text becomes **2 segments and costs double.**

*(Quirk worth knowing: `é`, `à`, `ö`, `ñ`, `ü` **are** in GSM-7. Only `á`, `í`, `ó`, `ú` are missing.)*

**Three ways to handle it:**

| Option | Effect |
|---|---|
| **Write "Uno Mas" (no accent) in SMS bodies** | Single segment, half the cost. **Recommended.** |
| **Omit the brand name from the body entirely** | Also single segment — the sender ID already identifies you. Frees ~9 chars. |
| Keep "Uno Más" | Every SMS costs ~2× for the same content |

⚠️ **This needs Ramsey's ruling** — `CLAUDE.md`'s brand rule requires the accent on all
human-readable surfaces and permits ASCII only for "technical compatibility." **SMS encoding is
arguably exactly that**, but it's a brand-rule exception and shouldn't be made silently.
**All drafts below use ASCII "Uno Mas" or omit the name**, pending that ruling.

**Also verify:** does Toast auto-append the opt-out line? If so, drop `Reply STOP to opt out.` from
the body — it frees 25 characters and avoids a doubled disclaimer.

---

## TUESDAY Aug 25 — SMS  ✅ READY TO SEND

**Send 11am** — lunch BOGO is a lunch offer; reach them before they decide.

```
It's Taco Tuesday. BOGO street tacos at lunch, $6 margs + $30 pitchers all day. 2020 N Monroe. Tomorrow: spend $50, get a $10 gift card.
```
`GSM-7 · 136/160 units · 1 segment` — opt-out auto-appended, do not add it.

**Two deliberate choices here:**
- **Brand name omitted from the body.** The sender ID already identifies you, and omitting it avoids the `á` encoding problem entirely while freeing characters for logistics.
- **It teases Wednesday**, bending the house one-offer-per-SMS rule. Called out so you can veto: Tuesday already performs, Wednesday is the day that needs help, so mentioning tomorrow's gift card here is the highest-leverage line in the week. **If you'd rather keep it pure, cut the final sentence** — it drops to 94 units and still works.

---

## WEDNESDAY Aug 26 — EMAIL (the anchor send)

**Subject A:** `Spend $50, we'll hand you $10.`
**Subject B:** `Here's $20 for next time.`
**Subject C:** `$5 pints tonight. Plus we're giving away gift cards.`
**Preview text:** `Gift card on us through Sunday. No expiration, no catch.`

**One primary action: come in this week.** Modular sections, each with a real click target
(per `campaign-architecture.md` §4 and the Canva Email Module System `DAHINHHZJng`).

### Section 1 — HERO · the gift card *(primary)*
Asset: `giftcard-feed-1080x1350.png` → links to the site

> **We're not discounting anything. We're just giving you money.**
> Spend **$50** → **$10 gift card.** Spend **$100** → **$20 gift card.**
> Wednesday through Sunday. No expiration — bring it back whenever.
> *Physical card, handed to you at checkout.*

### Section 2 — TONIGHT · Beer & Bites Wednesday *(the reason to come today)*
> **$5 pints. $10 loaded nachos. $10 loaded masa fries.**
> Every Wednesday. It's the easiest night of the week to end up here.
> **[See the menu →]**

### Section 3 — FRIDAY · Late Night launches *(new news)*
Asset: `latenight-menu-1080x1350.png`
> **Late Night starts Friday.** Fri + Sat, 8–10pm.
> Pick any two street tacos **$10**. $6 margs, $7 palomas, $30 pitchers.
> The kitchen's still going. So are we.
> **[Reserve on Resy →]**

### Section 4 — Footer
Address, hours, unsubscribe. **Hours must read Tue–Thu 11am–8pm · Fri–Sat 11am–10pm · Sun 10am–4pm.**

**Send time:** 10–11am Wednesday — ahead of both lunch and the dinner decision.

---

## THURSDAY Aug 27 — SMS  ✅ READY TO SEND

**Send 3–4pm** — after the lunch decision, before dinner plans lock.

```
Big F'N Thursday: $10 Big F'N Quesadilla + $10 tequila cocktails. Spend $50, get a $10 gift card. Late Night starts Fri, 8-10pm.
```
`GSM-7 · 128/160 units · 1 segment` — opt-out auto-appended, do not add it.

Carries all three things at once: tonight's special, the running gift-card promo, and tomorrow's
launch. Brand name omitted for the same encoding reason.

⚠️ **"Big F'N" lands on every phone on the list.** It's the correct marketing rendering per
`CLAUDE.md` and it's on your menu — just confirm it's a conscious choice, since SMS has no
preview cushion.

**Alternative — gift-card led**, if Thursday *covers* matter more than promoting the special:
```
Spend $50 tonight, take a $10 gift card home. Plus Big F'N Thursday: $10 Big F'N Quesadilla + $10 tequila cocktails.
```
`GSM-7 · 1 segment`

---

## FRIDAY Aug 28 — SMS  ⭐ RECOMMENDED ADDITION

**Send 4pm.** Late Night launches tonight — your biggest news of the week.

```
Late Night starts tonight, 8-10pm. Two street tacos $10, $6 margs, $7 palomas, $30 pitchers. Spend $50, take a $10 gift card home.
```
`GSM-7 · 130/160 units · 1 segment` — opt-out auto-appended, do not add it.

Note it says **"Two street tacos $10"**, never "$10 tacos" — Big A** tacos are already $10 each.

**If four sends in five days is too many:** drop Thursday and send this instead. Friday has
genuinely new news; Thursday is a recurring special the list already knows.

---

## Copy checks applied

- Price-confident, no apology, no "save" framing on the gift card — **"we're giving you"**
- No banned words (`authentic Mexican`, `mouthwatering`, `culinary journey`, `artisanal`, `mixology`, `perfect for any occasion`)
- Short sentences, fragments fine
- Every send names **exact prices and days** — specific beats vague
- Hours stated as **8pm** close Tue–Thu wherever they appear
- Late Night stated as **Fri + Sat only**
- One clear primary action per send

## Before you send — two mechanical notes

1. **Do not paste the opt-out into any body.** Toast adds it. Confirmed 2026-08-23.
2. **If you add a Resy or menu link to any SMS**, re-check the segment count. Toast's link shortening
   changes the character math, and every draft above is sized with **zero** links. A shortlink is
   typically ~23 characters — Tuesday (136) and Friday (130) would still fit; Thursday (128) would fit
   but leaves little room. Verify in Toast's preview before scheduling.

## Measurement

Per `toast-lifecycle-automation-playbook.md` — judge on **incremental visits, not opens.**
Track **Wed and Thu covers vs. the prior three Weds/Thurs**, gift cards issued per day, and
Friday's Late Night covers. Opens and clicks are diagnostics, not the result.
