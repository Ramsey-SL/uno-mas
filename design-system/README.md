# Uno Más — Web Design System

The source of truth for the Uno Más website look & feel. Codifies what's live on the
Lovable site (homepage hero, `/about` story timeline, the Fiesta Box page). Use this to
seed **Claude Design** (or any new build) so every page starts on-brand.

- **Tokens:** [`tokens.css`](./tokens.css) (CSS variables) — colors, type, spacing, radius, shadow, motion, gradients.
- **Components:** [`UnoMasUI.tsx`](./UnoMasUI.tsx) — reference React components (Buttons, Badges, Ticket card, section shells, Typewriter).

---

## Brand in one line
Modern Mexican kitchen + tequila bar in Spokane. Confident, playful, a little chaotic. **"Get a little lost."**

## Color
| Role | Hex |
|---|---|
| Navy (primary dark) | `#06243F` |
| Brighter navy (gradient top) | `#0C3D72` |
| Pink (primary accent / CTA) | `#E22690` |
| Cyan (secondary accent) | `#18BCDC` |
| Yellow (highlight / sun button) | `#FFEC00` |
| Magenta (gradient) | `#BF28BF` |
| Orange (warm accent) | `#E8761B` |
| Ink / Muted / Line | `#0A1F33` / `#5A6B7B` / `#E6E9EE` |
| Paper / White | `#FAF8F4` / `#FFFFFF` |

**Gradients:** Fiesta `135deg #E22690→#BF28BF→#FF8A3D` · CTA `135deg #18BCDC→#E22690` · Navy hero (radial cyan+pink glows over `#0C3D72→#0A2C4F`).

## Type
- **Display:** Antonio — uppercase, weight **600–700** (never heavier; it reads blocky), tracking `.01em`, line-height `.95`.
- **Body:** Montserrat.
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
Short sentences, fragments welcome. Lead with experience, prove with food. Spokane pride. Price confidence.
**Always** "Uno Más" with the accent. **Never** corporate/apologetic, never "taco shop" in brand copy, never the banned words (authentic, mouthwatering, culinary journey, artisanal, mixology, leverage, utilize, vibrant). Never render/fake the logo. Never mix Uno Más + Mezzanine.

---
*Mirrors the live Lovable build. Update this when the site's design language changes.*
