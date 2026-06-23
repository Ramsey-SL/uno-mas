# Uno Más — Web Design System

The source of truth for the Uno Más website look & feel. Codifies what's live on the
Lovable site (homepage hero, `/about` story timeline, the Fiesta Box page). Use this to
seed **Claude Design** (or any new build) so every page starts on-brand.

- **Tokens:** [`tokens.css`](./tokens.css) (CSS variables) — colors, type, spacing, radius, shadow, motion, gradients.
- **Components:** [`UnoMasUI.tsx`](./UnoMasUI.tsx) — reference React components (Buttons, Badges, Ticket card, section shells, Typewriter).

---

## Brand in one line
Spokane's most inviting Mexican street food hangout. Relaxed, friendly, simple — never pretentious. **"Get a little lost at Uno Más."**

**Pillars:** Relaxed experience · Welcoming community · An escape from the everyday.
**Personality:** a skateboarding alpaca in a backwards cap who's buddies with everyone — not because he's popular, just genuinely nice and cool.
**Location names:** Monroe = *Tacos & Tequila* · Wonder Building = *Taco Shop* · cart = *Taco Cart*.

## Color — Brand Guide 2024 palette (authoritative)
| Role | Name | Hex |
|---|---|---|
| Primary dark | Navy | `#003366` |
| **Hero color / primary CTA** | Pink | `#E22690` |
| Accent | Blue (electric) | `#18BCDC` |
| Accent | Light Blue | `#1DBCDC` |
| Accent (logo system) | Teal | `#27F3DE` |
| Accent | Green | `#25E9B9` |
| Highlight / sun button | Yellow | `#FFEC00` |
| Neutral dark / body text | Dark Grey | `#212121` |
| Neutral light / hairline | Light Grey | `#BFBFBF` |
| Base | White | `#FFFFFF` |

**Pink is the hero color — don't let Navy or Blue dominate.** Teal + Blue are the logo's electric accent system.
There is **no magenta or orange** in the Uno Más palette (those belong to the separate *Mezzanine* sub-brand — never mix the two).
`#00223F` is used only as a darker *shade* of navy for gradient depth, not as a new color.

**Gradients (approved colors only):** CTA `135deg #18BCDC→#E22690` · Electric `135deg #18BCDC→#27F3DE` · Agave `160deg #003366→#18BCDC→#27F3DE` · Navy hero (radial teal+pink glows over `#003366→#00223F`).

## Type — Brand Guide 2024
- **Decorative:** Thirsty Rough — primary decorative font; **use very sparingly, never alongside/competing with the logo.** Licensed (not on Google Fonts) — only in produced graphics where licensed.
- **Headlines:** Antonio — uppercase, weight **600–700** (never heavier; it reads blocky), tracking `.01em`, line-height `.95`. The web workhorse for titles/section headers.
- **Body:** Montserrat (Thin → Extra-Bold available for hierarchy).
- **Eyebrow:** Montserrat, uppercase, 12px, weight 700, letter-spacing `.26em` (pink on light, yellow on navy).
- Scale: hero `clamp(2.6rem,6vw,4.8rem)` · h2 `clamp(2rem,4.6vw,3.4rem)` · lead `clamp(1.05rem,1.5vw,1.28rem)`.

## Components
- **Buttons:** `primary` (pink, 3D bottom shadow), `sun` (yellow), `ghost` (outline; on dark = translucent-white + white border so it stays visible).
- **Badges:** `TitleBadge` (yellow Antonio stamp, slight tilt — product/section titles), `ProTipSticker` (pink, pulse), section badges (yellow pill, e.g. "Add-Ons").
- **TicketCard:** white card, dashed-left edge + round notches, icon in a soft circle, optional corner tag (e.g. "Serves 4").
- **Sections:** `ScatterSection` (light bg + subtle navy brand-icon scatter, seamless cover, rotated -8°), `NavySection` (navy feature band), `CtaBand` (cyan→pink gradient).

## Motion
- **Typewriter** rotating phrase (e.g. "Great for ___" → date night / parties / when you don't want to cook…).
- **Scroll-reveal** (fade + rise) for timeline milestones; **confetti** on celebratory CTA bands; **hover lift** on cards.
- Always honor `prefers-reduced-motion` (disable animation, show end state).

## Imagery & icons
- Photography: warm, candid, natural light, **no blue/cool cast** (Uno Más). Mezzanine is the dark/dramatic exception — **never mix the two**.
- Brand icon set: line-art food/drink motifs (`icons-pattern-forramsey`) used as a subtle background texture (tinted, low opacity, full-bleed cover — not a visible grid).
- Assets live in Cloudinary cloud `drxrfyq9i` under `uno-mas/approved-assets/...`.

## Voice — quick rules
Friendly, chill, simple. Short sentences, fragments welcome. Lead with experience, prove with food. Spokane pride.
We are **relaxed** (not lazy), **casual** (not vulgar), **friendly** (not intrusive), **simple** (not plain), **cool** (not pretentious).
**Always** "Uno Más" with the accent. Avoid flowery / over-the-top language — we're a taco shop and proud of it; keep it straightforward. **Never** render/fake the logo. **Never** mix Uno Más + Mezzanine.

---
*Mirrors the live Lovable build. Update this when the site's design language changes.*
