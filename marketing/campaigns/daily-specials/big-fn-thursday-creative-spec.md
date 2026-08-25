# Big F’N Thursday — Creative Spec

> Everything needed to build the replacement Thursday creative. Pulled from the **live site
> codebase** (Lovable project `78c4ac75-6325-4f38-a44b-278bb2194cf2`,
> `src/components/WhatsOnThisWeek.tsx`) and the repo menu docs on **2026-08-20**.
> Burrito Thursday is retired — see the changelog entry for that date.

---

## 1. The offer, exactly as the site states it

| Field | Value (verbatim from `WhatsOnThisWeek.tsx`) |
|---|---|
| Day name | **Big F’N Thursday** |
| Eyebrow | Every Thursday |
| Abbr (watermark) | THU |
| Line 1 | `$10 Big F’N Quesadilla` |
| Line 2 | `$10 menu cocktails, fresh sheet` |
| Note | New cocktails every Thursday. |
| Ticker string | `BIG F’N THURSDAY · $10 BFQ + $10 MENU COCKTAILS` |
| Accent color | **Blue `#18BCDC`** |
| Icon | `uno-mas/website/icons/quesadilla-lineart-teal` |

Note the apostrophe is a **typographic** `’` (U+2019), not `'` — "Big F’N". Match it in copy.

## 2. The BFQ is an existing menu item — this is a discount, not a new dish

| | |
|---|---|
| Menu name | **The Big F*** Quesadilla (BFQ)** |
| Regular price | **$15** (brunch: $14 + protein) |
| Thursday price | **$10 base** — protein add-ons charged on top, at normal prices |
| Description | "The size of a medium pizza. Loaded with melted cheese. *It's exactly what it sounds like.*" |
| Protein add-ons | Skirt Steak +$9 · Carnitas +$7 · Grilled Chicken +$6 |

**This is the creative hook: $15 → $10 on the item people already order.** Lead with the size and
the name — the menu doc's own guidance is *"BFQ = the name does the work."*

✅ **CONFIRMED 2026-08-20:** the **$10 is the base price** (cheese quesadilla). Protein add-ons are
charged **on top at normal menu prices** — Skirt Steak +$9 · Carnitas +$7 · Grilled Chicken +$6.
So a Thursday BFQ with carnitas is $17, not $10.

**Copy implication:** never write "$10 BFQ with your choice of protein." Write **"$10 Big F’N
Quesadilla"** and let the protein add-ons sit in the menu where they already live. If a piece has
room for fine print, `Proteins additional` is the safe qualifier.

✅ **NAMING — CONFIRMED CONVENTION 2026-08-20 (not a conflict):** the menu keeps
**"Big F*** Quesadilla"**; marketing uses **"Big F’N Quesadilla"**. Both are intentional. Use
`Big F’N` in all consumer creative; leave the menu language exactly as it is.

## 3. Exact design tokens (from the live tile component)

Reuse these so print matches web:

- **Accent / day color:** `#18BCDC` (blue). Used for eyebrow, day headline, offer-line tags, the
  70×4px rounded rule rotated `-1deg`, and the giant ghost `THU` watermark at **12% alpha**.
- **Type:** headline **Antonio 700**, uppercase, `clamp(26px, 3vw, 38px)`, line-height `0.95`,
  letter-spacing `0.01em`. Eyebrow **Montserrat 700**, 11px, uppercase, letter-spacing `0.2em`.
  Offer lines **Montserrat 600**, 14px. Note **Montserrat 500**, 12.5px, `#6b6b6b`.
- **Body text color:** `#1a1a1a`. **Headline navy elsewhere:** `#06243F`.
- **Card:** white, `border-radius 18px`, `min-height 210px`, `padding 24px`,
  `box-shadow 0 18px 40px -22px rgba(0,0,0,.25)`.
- **Texture overlay:** `uno-mas/website/icons/icons-pattern-forramsey-02-1.png`, 300px tile, **5% opacity**.
- **Icon treatment (Cloudinary transform chain, verified 200 OK):**
  `e_make_transparent:45/e_colorize,co_rgb:18BCDC/e_trim/c_fit,h_160,f_auto,q_auto`
  applied to `uno-mas/website/icons/quesadilla-lineart-teal`, rendered at **64px** height.

## 4. Copy bank (approved, in voice)

**Social — day-of**
> It's called Big F’N Thursday. We didn't name it quietly. 🧀
> $10 Big F’N Quesadilla. $10 menu cocktails off the fresh sheet — new ones every week.

**Poster / table tent**
> BIG F’N THURSDAY — $10 BIG F’N QUESADILLA · $10 MENU COCKTAILS

**SMS**
> Uno Más: Big F’N Thursday 🧀 $10 Big F’N Quesadilla + $10 menu cocktails. Your Thursday plan is set. (STOP to opt out)

**Email subject**
> Big F’N Thursday. $10 BFQ, $10 menu cocktails.

**Web tile subline**
> $10 Big F’N Quesadilla. $10 menu cocktails off the fresh sheet — new pours every week.

## 5. Still to build

- [ ] **Poster 4:5** — replaces `_RETIRED-2026-08-poster-burrito-thursday.html`.
- [ ] **AI-image prompt set** in `chatgpt-prompts.md` section C. Hero direction: a **big griddled
      quesadilla, cut into wedges, cheese pulling**, beside a tequila cocktail; natural warm light,
      no blue cast; accent Blue `#18BCDC`; offer panel white-on-blue
      `"$10 BIG F’N QUESADILLA · $10 MENU COCKTAILS"`; `"UNO MÁS"` wordmark.
- [ ] **Regenerate `_gallery.html`** — it's a generated file still showing burrito copy.
- [ ] **Photo asset:** no BFQ hero shot confirmed in the DAM under `category-food`. Needs a shoot
      or a DAM search before the poster can use real photography rather than AI.
- [ ] **`poster-midweek-lineup.html`** text is updated, but its `.png` preview needs re-rendering.
