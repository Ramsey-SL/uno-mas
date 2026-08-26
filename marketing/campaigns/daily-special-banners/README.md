# Daily Special Site Banners

**Status: LIVE as of 2026-08-25.** Template of record: the **Full Send shell**.

## What shipped

One reusable component, three configs. Only one tile can ever render, because each is
gated to its own weekday.

| Day | Gate | Headline | Offers |
|---|---|---|---|
| Tuesday | `useIsSpokaneDay(2)` | Taco / **Tuesday** | BOGO Street Tacos (till 5pm) · $6 House Margs · $30 Marg Pitchers |
| Wednesday | `useIsSpokaneDay(3)` | Beer & / **Bites** | $5 Pints · $10 Loaded Nachos · $10 Loaded Masa Fries |
| Thursday | `useIsSpokaneDay(4)` | Big F'N / **Thursday** | $10 Big F'N Quesadilla (proteins extra) · $10 Tequila Cocktails (*menu only) |

## Where it lives (Lovable, project 78c4ac75-6325-4f38-a44b-278bb2194cf2)

- `src/components/DaySpecialBanner.tsx` — the component. Full Send chrome, `.ds-scope`.
- `src/config/daySpecials.ts` — the three configs. **Add a day here, not in the component.**
- `src/components/useIsSpokaneDay.ts` — the weekday gate (America/Los_Angeles, SSR-safe).
- `src/routes/index.tsx` — all three mounted above `<HomeHero />`.
- `FullSendBanner` stays in `src/routes/index.tsx`, gated off, as the template of record.
- `TacoTuesdayBanner.tsx` **deleted** — the simplified version it held is superseded.

## Design rules this template encodes

Kept from Full Send: torn-paper clip-path, pink + teal starbursts bleeding off the corners,
yellow sparks, halftone blob, kicker, two-line headline with the second line in pink,
hand-drawn underline swoosh, torn-paper yellow price swatches with a pink sub-line,
`ds-drop` bounce-in (guarded by `prefers-reduced-motion`).

Removed on Ramsey's call (2026-08-25): the teal ribbon, the chooser list, the italic-serif
fine print, and the CTA button. The **whole tile is the click target** instead —
`<Link to="/menu">` firing `trackEvent("nav_click", {location:"day_special_banner"})`.
No button means no measurement otherwise.

**Art never goes behind text.** The corner photos get their own radial-masked zone at the
bottom corners and fade out before they reach the price swatches. Do not solve an overlap
with opacity.

## Open

- **Photo quality.** Deferred by Ramsey to the Cloudinary workflow — most corner photos are
  2048px iCloud shared-album derivatives (`needs-hires-swap`), and Thursday has no true BFQ
  hero at all. Fix upstream in the DAM, then swap the public_ids in `daySpecials.ts`.
- **`ALL DAY` sub-lines** are still on Tue/Wed. Ramsey cut these from the earlier simplified
  tile as implied; they survived into the approved comps. One-line removal when he calls it.
- **Fri/Sat Late Night Happy Hour tile** — offer runs 8-10pm only, so it needs an hour gate,
  not just a day gate. Not built.
- **Sunday** — likely redundant against the existing `SundayBrunchFeature` band.
- **Tuesday naming** — "Taco Tuesday" shipped; alternates in `tuesday-name-options.md`.

## Mockup archive

`fullsend-template-days.html` is the approved comp. The earlier explorations
(`banner-set-mockups`, `bold-variants`, `rebalanced`, `color-options`, `g1-borders-and-load`,
`no-overlap`, `compare-live-tiles`) are kept only as a record of what was rejected and why —
`compare-live-tiles.html` is the useful one, it's the side-by-side that showed Full Send
carried ten craft elements against the simplified tile's three.

---

# Collision handling — weekly promo × day special (shipped 2026-08-25)

**Chosen: E1 — crossfade rotator with a flipping reference bar.**

`PromoSlot` now owns every decision. The tiles are presentational and gate nothing.

| Weekly promo live? | Day special today? | Renders |
|---|---|---|
| no | no | `null` |
| no | yes | solo day tile, no bar |
| yes | no | solo weekly tile, no bar |
| **yes** | **yes** | **rotator + flipping bar** |

## Rules the rotator encodes

- **Slide 1 is always the weekly promo.** It expires; the day special doesn't. Slide two
  reliably gets less attention, so whatever must be seen goes first — permanently.
- **The bar always carries the offer that is NOT in the hero.** It flips with the tile. This is
  what makes the rotator safe: a guest who never waits for slide two still reads both offers,
  and a screen reader gets both from a single pass.
- **Offset crossfade** — outgoing `opacity .32s ease-out`, incoming `opacity .5s ease-in .18s`.
  The 180ms delay means the two tiles are never both at half opacity, so there is no unreadable
  beat mid-transition. Do not "simplify" this to a symmetric fade.
- **5000ms dwell.** Noted at design time that this is short for the longest tile (~14 words plus
  two qualifiers); Ramsey chose 5s. Change `ROTATE_MS` in `PromoSlot.tsx` if it reads rushed live.
- **Height is locked** with `.track{display:grid}` + both slides at `grid-area:1/1`. The slot
  takes the taller tile so the page never jumps. **Keep collision-day tiles close in length.**
- Pauses on hover and on focus. An explicit pause via the button outranks both and stays paused.
  `IntersectionObserver` at 0.35 stops it rotating off screen.
- `prefers-reduced-motion: reduce` → no rotation at all, both tiles stacked and static, no bar,
  no controls, no interval.

## Accessibility — three defects found and fixed post-ship

1. The inactive slide was `aria-hidden` but its `<Link>` was still keyboard-focusable — focus
   landed in a hidden subtree and announced nothing (WCAG 4.1.2). Now `tabIndex={-1}` +
   `aria-hidden` on the inactive link itself.
2. Dots declared `role="tab"` / `aria-selected` with no `tablist` and no `tabpanel` — invalid
   ARIA. Now plain buttons with `aria-label`, active state via a `.on` class.
3. The control cluster sat directly on top of `.corner.rgt`, so the dots and the pause button
   were invisible over a dark photo. Now on a translucent cream pill with a shadow.

**Rule for any future overlay control:** the bottom corners belong to the photos. Anything placed
there needs its own ground, not a heavier tint.

## Files

- `src/components/PromoSlot.tsx` — all decisions, the rotator, the bar
- `src/components/DaySpecialBanner.tsx` — now exports `PromoTile` (presentational), `DS_CSS`, `DS_TEAR`
- `src/config/daySpecials.ts` — three day configs, each with `barLabel` + `barItems`
- `src/config/weeklyPromo.ts` — `WEEKLY_PROMOS` + `useActiveWeeklyPromo()`
- `src/components/useIsSpokaneDay.ts` — adds `spokaneDateISO()` and `useIsSpokaneWithin(start,end)`

Adding a weekly promo is one entry in `WEEKLY_PROMOS` with a Spokane date window. Collision
handling is then automatic.

## ⚠ Needs Ramsey's confirmation

The gift card window is set **2026-08-27 → 2026-08-30** — the *marketing launch* date, so the
tile does not announce the promo before the Thursday push. The *offer* window was discussed as
starting Wednesday 08-26. If the tile should be up for the Wednesday soft open, change
`startISO` to `"2026-08-26"`. One line.

## Not solved

Fri/Sat, **Late Night Happy Hour (8–10pm) overlaps the gift card promo** — three offers in one
slot, and Late Night needs an *hour* gate as well as a day gate. `PromoSlot` currently handles
exactly two. Launch is 2026-08-28.
