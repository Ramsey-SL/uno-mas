# KLAVIYO BUILD SHEET — Cinco at Uno Más — Pre-Cinco
**Template starting point:** Your image-based template (`email-28eaa0aa.html`) — 4 stacked images on hot pink (#e22690)
**Target structure:** Hybrid (your 4 image slots + native text/button blocks added between)
**Goal:** Get the full message through even when images don't load + improve deliverability and click-tracking

---

## KLAVIYO MESSAGE-LEVEL FIELDS

| Field | Value |
|---|---|
| Subject line | **Cinco starts today.** |
| A/B test variant | Why wait till Tuesday? |
| Preview text | Two days of pre-Cinco on the patio — $8 margs, $3 candy shots, and Sonoran dogs off the grill. |
| From name | Uno Más |
| From email | tacos@unomastacoshop.com |
| Reply-to | tacos@unomastacoshop.com |
| Send time | Friday, May 1, 2026 — 11:00 AM PT |
| Audience | All marketing-subscribed contacts |

---

## BUILD ORDER (top to bottom in the Klaviyo editor)

### Block 1 — Image (KEEP existing slot 1)
**Dimensions:** 600 × 135px
**Design into the image:**
- Uno Más logo (white/cream version on hot pink)
- Eyebrow text: **PRE-CINCO · MAY 1 + 2**
**Image link URL:** Resy reservation URL
**ALT text:** `Uno Más — Cinco at Uno Más — Pre-Cinco, May 2 + 3`

---

### Block 2 — Image (KEEP existing slot 2)
**Dimensions:** 600 × 425px
**Design into the image:**
- Background: patio photo (daytime, drinks visible)
- Headline overlay: **CINCO STARTS TODAY.**
- Subhead: *We're not waiting till Tuesday.*
- Bottom-corner badge: **Fri May 1 + Sat May 2**
**Image link URL:** Resy reservation URL
**ALT text:** `Cinco starts today. We're not waiting till Tuesday.`

---

### Block 3 — Text block (ADD THIS — new)
**Background:** Match template hot pink (#e22690) OR swap to cream (#F5F0E8) for a section break
**Text color:** Cream (#F5F0E8) on pink, OR navy (#003366) on cream
**Padding:** 24px top, 24px sides, 16px bottom
**Font:** Arial/Helvetica, 16px, line-height 1.5, centered

**Paste this copy:**

> Cinco's on a Tuesday this year. That's a long time to wait.
>
> So we're starting early. This Friday and Saturday, the patio is open, the grill is going, and we're opening the patio, firing up the grill, and starting Cinco specials early — $8 margs, $3 shots, and street food coming hot off the patio. Tuesday will still be Tuesday. But the long weekend starts now.

---

### Block 4 — Image (KEEP existing slot 3)
**Dimensions:** 552 × 414px
**Design into the image:** The specials block — reuse the fresh sheet card art for visual consistency
- Eyebrow: ★ THE PRE-FUNK ★
- $8 House Margaritas
- $3 Latin Candy Shots
- $10 Sonoran Hot Dogs *(off the grill — patio only)*
- $10 Street Corn *(on the cob — the right way)*
**ALT text:** `$8 House Margaritas, $3 Latin Candy Shots, $10 Sonoran Hot Dogs, $10 Street Corn — Friday and Saturday only.`

---

### Block 5 — Text block (ADD THIS — new)
**Style:** Same as Block 3. Centered.

**Paste this copy:**

> Call it the warm-up. Call it the pre-game. Call it the long weekend.
>
> We just call it open.
>
> **Friday May 1 + Saturday May 2**
> 2020 N Monroe, Spokane
> Regular hours both days.
> *And yes — we're open Cinco Tuesday too.*

---

### Block 6 — Button block (ADD THIS — native Klaviyo button)
**Button text:** RESERVE YOUR TABLE
**Button URL:** `https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila`
**Button styling:**
- Fill: Gold (#F4C430) OR cream (#F5F0E8)
- Text color: Navy (#003366) — bold, all caps
- Padding: 16px top/bottom, 32px left/right
- Border-radius: 4px (subtle) or 999px (full pill)
- Font size: 16–18px, weight 800
- Alignment: center
- Wrapper padding: 24px top, 16px bottom

---

### Block 7 — Text block (ADD THIS — new)
**Style:** Smaller text, centered, italic for tagline.

**Paste this copy:**

> Walk-ins always welcome. The patio fills up fast — book ahead if you're rolling deep.
>
> See you out there. *(Then again on Tuesday.)*
>
> *Get a little lost at Uno Más.*

---

### Block 8 — Image (OPTIONAL — KEEP existing slot 4 OR drop)
**Decision:**
- **Keep it** if you have a great Sonoran-dog-on-grill or marg-pour photo to use as a visual closer (no text overlay — the button above carries the CTA)
- **Drop it** if you'd rather end on the closer text — cleaner, faster scroll

If keeping:
**Dimensions:** 552 × 414px
**ALT text:** `Sonoran dogs hot off the patio grill at Uno Más.`
**Image link:** Resy URL (defensive — gives clickers a backup CTA)

---

### Block 9 — Footer text block (ADD THIS — new, required)
**Background:** Cream (#F5F0E8) OR navy (#003366) for max contrast
**Text:** Small (11–12px), centered

**Paste this copy:**

> **Uno Más Tacos & Tequila**
> 2020 N Monroe St, Suite C · Spokane, WA 99205
> (509) 960-7989 · tacos@unomastacoshop.com
>
> [Reserve](RESY_URL) · [Instagram](IG_URL) · [Facebook](FB_URL)
>
> {% unsubscribe %}

Replace placeholders with:
- RESY_URL: `https://resy.com/cities/spokane-wa/venues/uno-mas-tacos-and-tequila`
- IG_URL: `https://www.instagram.com/unomastacoshop`
- FB_URL: `https://www.facebook.com/UnoMasTacoShop/`

---

## VISUAL HIERARCHY CHECK (before scheduling)

Read the email **with images turned off** — your subscribers WILL see this version.
Make sure these still work:
- [ ] Subject line + preview text tell the story (Klaviyo inbox preview)
- [ ] Body prose (Block 3, 5, 7) carries the full message
- [ ] Native button (Block 6) is visible and clickable
- [ ] ALT text on every image is real copy, not "image1.jpg"
- [ ] Footer + unsubscribe present

Then turn images back on and confirm:
- [ ] Logo loads
- [ ] Hero headline overlay is legible
- [ ] Specials graphic is sharp on Retina
- [ ] Mobile preview: button is thumb-tappable above the fold

---

## WHY THIS BEATS IMAGE-ONLY

| Metric | Image-only | Hybrid (recommended) |
|---|---|---|
| Deliverability (Gmail/Apple) | ⚠️ flagged | ✅ clean |
| Images-off rendering | ❌ blank | ✅ full message |
| Dark mode | ⚠️ pink everywhere | ✅ adapts |
| Click tracking | ⚠️ image-link only | ✅ native button analytics |
| Accessibility | ❌ poor | ✅ screen-reader friendly |
| Time to design | 4 images | 3 images + paste copy |

---

## FALLBACK — IF YOU REALLY DON'T WANT TO EDIT THE TEMPLATE

If the lift to add blocks is too much before tomorrow's send, **at minimum add ONE text block at the bottom** (after Image 4) with:

1. Body prose (Block 3 + 5 copy combined into one paragraph)
2. The native CTA button
3. The footer (Block 9)

That's the legally-required minimum (unsubscribe + sender info) plus a working button. You'd still have the deliverability/dark-mode tradeoffs, but you'd have a click-trackable CTA and the message would still send if images break.
