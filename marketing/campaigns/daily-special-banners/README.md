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
