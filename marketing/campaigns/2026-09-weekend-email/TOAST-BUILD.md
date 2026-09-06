# Toast drag-and-drop build sheet — Weekend email

Build this natively in Toast rather than pasting image slices. You get live text, real
buttons, working dark mode and much better deliverability.

**Assets to upload:** `export/toast-assets/` — four files, all sized for email
(1200px wide = 2× a 600px body, so they stay sharp on retina).

| File | Use |
|---|---|
| `00-logo-navy.png` | Header logo |
| `01-margs-chips.jpg` | Block 1 photo |
| `02-late-night-tacos.jpg` | Block 2 photo |
| `03-sunday-brunch.jpg` | Block 3 photo |

---

## Before you start — two settings

**Body width:** 600px. **Body background:** `#FAFAF8` (warm off-white).

**Fonts.** The brand faces are Antonio (headlines) and Montserrat (body). Toast almost
certainly won't offer either. Pick the closest available and stay consistent:

- Headlines → a heavy condensed sans. **Oswald** or **Archivo Narrow** if offered;
  otherwise **Arial Black**, or Impact as a last resort.
- Body → **Montserrat** if offered; otherwise **Arial** / **Helvetica**.

Do not mix — one headline face, one body face, throughout.

> If Toast's fonts look wrong enough to hurt the brand, tell me and I'll export just the
> headlines as transparent PNGs. You'd keep live text for the body and buttons, which is
> where deliverability and accessibility actually matter, and get exact type on the
> headlines.

**Colours** — paste these hex values exactly:

| Name | Hex | Used for |
|---|---|---|
| Navy | `#003366` | Hero headline, body text on light |
| Pink | `#E22690` | Block 1 accent + button, hero eyebrow |
| Blue | `#18BCDC` | Block 2 accent + button |
| Gold | `#C79A16` | Block 3 accent |
| Yellow | `#FFEC00` | The big prices ($25 / $10) |
| Ink | `#0E1116` | Dark block backgrounds |
| Off-white | `#FAFAF8` | Body background |
| Footer grey | `#F0EFEB` | Footer background |

---

## SUBJECT & PREVIEW

- **Subject:** `Three things worth showing up for.`
- **Preview text:** `Margs + chips through Sunday, new Late Night Happy Hour, Sunday brunch.`

---

## BLOCK 1 — Header · image block

- `00-logo-navy.png`, displayed at **150px wide**, centred
- Padding: 34px top, 0 bottom
- Link: `https://unomastacoshop.com`
- Alt: `Uno Más Tacos & Tequila`

## BLOCK 2 — Hero · text block

Background `#FAFAF8`, centred, 44px top / 40px bottom padding.

- **Eyebrow** — 12px, bold, ALL CAPS, letter-spacing wide, colour `#E22690`
  `THIS WEEKEND AT UNO MÁS`
- **Headline** — 46px, bold, ALL CAPS, line-height ~0.93, colour `#003366`
  `THREE THINGS WORTH SHOWING UP FOR.`
- **Sub-headline** — 16px, regular, colour `#6B6B6B`, max ~390px wide
  `One runs all weekend and then disappears. One's brand new. One's Sunday. All of it on North Monroe.`

> Note the accent: **Uno Más**, never "Uno Mas". Check it survives paste into Toast.

---

## BLOCK 3 — $25 Margs + Chips · image + dark section

**3a · Image block:** `01-margs-chips.jpg`, full 600px width, no padding, no rounding.
Alt: `Chips with salsa, guacamole and queso.`

**3b · Text block** directly beneath, **background `#0E1116`**, centred, 30px top /
34px bottom padding, **zero gap above** so it meets the photo cleanly.

- **Meta** — 11px, bold, ALL CAPS, wide letter-spacing, colour `#E22690`
  `NOW THROUGH SUNDAY 4PM`
- **Headline** — 40px, bold, ALL CAPS, colour `#FFFFFF`
  `2 HOUSE MARGS + CHIPS & DIP`
- **Price** — 84px, bold, colour `#FFEC00`
  `$25`
- **Body** — 15px, colour `#9AA4B2`, max ~420px
  `Two house margaritas and chips with your choice of salsa, guac, or queso. Running all day, every day we're open — right through Sunday.`

**3c · Button block:** background `#E22690`, text `#FFFFFF`, 13px bold ALL CAPS,
fully rounded, 14px/30px padding, centred.
Label `SEE WHAT ELSE IS ON` → `https://unomastacoshop.com`

---

## BLOCK 4 — Late Night Happy Hour · image + dark section

**4a · Image block:** `02-late-night-tacos.jpg`, full 600px width.
Alt: `Street tacos in holders.`

**4b · Text block**, background `#0E1116`, centred, same padding as 3b.

- **Meta** — 11px, bold, ALL CAPS, colour `#18BCDC`
  `FRIDAY & SATURDAY · 8–10PM`
- **Headline** — 40px, bold, ALL CAPS, colour `#FFFFFF`
  `LATE NIGHT HAPPY HOUR`
- **Price** — 84px, bold, colour `#FFEC00`
  `$10`
- **Body line 1** — 15px, colour `#9AA4B2`
  `Pick any two street tacos for $10 — carne asada, al pastor chicken, carnitas, barbacoa, batata, hongos.`
- **Body line 2** — 14px, **semibold**, colour `#FFFFFF`
  `House margs $6 · Pints $5 · Shots $4 · Marg pitchers $30. Both nights, 8–10pm.`

> Line 2 is deliberately white and bolder — it's a price list, and it disappears if you
> style it the same grey as line 1.

**4c · Button block:** background `#18BCDC`, text `#FFFFFF`.
Label `SEE THE LATE NIGHT MENU` → `https://unomastacoshop.com/menu?tab=late-night`

---

## BLOCK 5 — Sunday Brunch · image + dark section

**5a · Image block:** `03-sunday-brunch.jpg`, full 600px width.
Alt: `Churro french toast.`

**5b · Text block**, background `#0E1116`, centred, same padding.

- **Meta** — 11px, bold, ALL CAPS, colour `#C79A16`
  `SUNDAY · 10AM–4PM`
- **Headline** — 40px, bold, ALL CAPS, colour `#FFFFFF`
  `SUNDAY BRUNCH`
- **Body** — 15px, colour `#9AA4B2`
  `Churro french toast, birria, and margaritas that start at 10am. Our busiest service of the week — a reservation is the move.`

*(No price line on this block.)*

**5c · Button block:** background `#C79A16`, text `#FFFFFF`.
Label `RESERVE A TABLE` → `https://unomastacoshop.com/reservations`

---

## BLOCK 6 — Sign-off · text block

Background `#FAFAF8`, centred, 22px top / 48px bottom. Thin `#E4E4E0` divider above.

- 36px, bold, ALL CAPS, colour `#003366` — `GET A LITTLE LOST.`
- 14px, colour `#8A8A8A` — `2020 N Monroe St, Suite C · Spokane`

## BLOCK 7 — Footer · text block

Background `#F0EFEB`, centred, 36px padding. Logo `00-logo-navy.png` at 150px on top.

```
2020 N Monroe St, Suite C · Spokane, WA 99205
(509) 960-7989 · tacos@unomastacoshop.com
Tue–Thu 11am–9pm · Fri–Sat 11am–10pm · Sun 10am–4pm · Closed Mondays
Instagram · TikTok · unomastacoshop.com
```

Then Toast's own unsubscribe / physical-address merge tags — **use Toast's, don't
hand-type them**, or you break compliance and the unsubscribe link.

Links: Instagram `https://instagram.com/unomastacoshop` ·
TikTok `https://www.tiktok.com/@unomastacosandtequila` · `https://unomastacoshop.com`

---

## Before you send

- [ ] Send yourself a test. Check **Gmail app, Apple Mail, and Outlook** — Outlook is
      where dark backgrounds and custom fonts most often break.
- [ ] Check the accent renders: **Uno Más**, not `Uno Mas` or `Uno Mテ｡s`.
- [ ] Check the en-dashes in `8–10pm` and `10am–4pm` didn't become mojibake.
- [ ] Tap all four links on a phone.
- [ ] View with images blocked — the alt text should still explain each block.
- [ ] Dark-mode check: the `#0E1116` sections should stay dark; the off-white ones may
      invert in some clients, which is fine as long as the navy text stays legible.
- [ ] Confirm no `21+` language anywhere and no reference to the retired 3–5pm Happy Hour.

## Timing

Playbook rule: don't send email and SMS on the same day unless it's a major event.
Planned: **SMS Thursday → this email Friday → SMS Saturday.** If the email slips to
Saturday it collides with the Saturday SMS — move one.
