# Lovable Template Handoff — Editable Fresh Sheet Generator

**Goal:** A web app where you fill out a form, see the fresh sheet update live, and download a print-ready PDF.

**What this gives you:** Reuse the design template for every promo (Mother's Day, summer, anniversary, etc.) without me rebuilding the layout each time.

---

## ARCHITECTURE — at a glance

```
┌─────────────────────────────────────────────────────────────┐
│ Lovable React App                                           │
│                                                             │
│  ┌──────────────┐         ┌─────────────────────────────┐   │
│  │ Form (left)  │ ──→     │ Live Preview (right)        │   │
│  │              │ state   │                             │   │
│  │ Color theme  │         │  [renders the fresh sheet   │   │
│  │ Headline     │         │   exactly like v9, 4-up]    │   │
│  │ Subhead      │         │                             │   │
│  │ Dates        │         │                             │   │
│  │ 4 specials   │         │                             │   │
│  │ Tagline      │         │                             │   │
│  │ Address      │         │                             │   │
│  └──────────────┘         └─────────────────────────────┘   │
│         ↓                                                   │
│  [ Download PDF ] ──→ html2pdf.js → user.pdf                │
└─────────────────────────────────────────────────────────────┘
```

Form on the left, live preview on the right, **Download PDF** button pipes the preview through a client-side PDF library. No backend needed. Everything runs in the user's browser.

---

## TECH STACK (Lovable defaults work)

| Layer | Tool |
|---|---|
| Framework | React (Lovable's default) |
| Styling | Tailwind (Lovable's default) |
| PDF generation | `html2pdf.js` (recommended) OR `@react-pdf/renderer` (more complex but more control) |
| Form state | React `useState` |
| Fonts | Google Fonts (Antonio + Montserrat + Playfair Display) — already used in your design |
| Brand assets | Stored in `/public/brand-assets/` folder of the Lovable app |

---

## THE LOVABLE PROMPT (paste this in)

Copy everything between the `===` lines into Lovable's prompt box to bootstrap the app:

===

Build a React app that generates a print-ready Cinco de Mayo-style fresh sheet PDF for a restaurant. The app has two columns: a form on the left and a live preview on the right.

**Form fields:**
- Color theme dropdown: Pink, Teal, Yellow, Navy, Blue
- Eyebrow text (e.g. "Pre-Cinco · May 1 + 2")
- Headline line 1 (e.g. "Cinco")
- Headline line 2 (e.g. "Starts Today")
- Subhead (e.g. "We're not waiting till Tuesday")
- Date range (e.g. "FRI MAY 1 · SAT MAY 2")
- Four specials, each with: price, item name, icon (dropdown: margarita, shot, hotdog, corn, lime, agave, jalapeno, taco, tequila-bottle)
- Tagline (e.g. "Get a little lost at Uno Más.")
- Address line (e.g. "2020 N Monroe · @unomastacoshop")
- Number of cards per page: 1, 2, or 4

**Color themes** — each one sets the accent color for the logo, headline accent ("Starts Today"), and date banner:
- Pink: #E22690
- Teal: #27F3DE
- Yellow: #FFEC00 (use navy logo + navy banner text since yellow doesn't read on white)
- Navy: #003366
- Blue: #18BCDC

**Card design specs:**
- Card size: 4.25 × 5.5 inches (quarter of letter)
- White background
- Navy double-rule border, 1.5px, 0.10in inset, 4px corner radius
- Layout top to bottom:
  1. Logo image (1.7in wide, centered)
  2. Tagline "TACOS & TEQUILA" — Montserrat 800, 9pt, 0.34em letter-spacing, accent color
  3. Headline (line 1 in Antonio 700 navy, 32pt; line 2 in Antonio 700 accent color, 38pt — block display)
  4. Italic subhead in Playfair Display, 12pt, navy, with em-dashes flanking
  5. Pink/teal/yellow/blue ribbon banner (accent color) with white-or-navy text "FRI MAY 1 · SAT MAY 2" in Antonio 14pt, 2.5 letter-spacing
  6. Specials list — 4 rows with: price (Antonio 24pt navy), icon (0.45in SVG), name (Antonio 13pt navy caps)
     Each row separated by a navy dotted bottom border
  7. Italic tagline in Playfair Display, 13pt, navy
  8. Address line in Montserrat 600, 8pt, 0.20em letter-spacing, navy uppercase

**Fonts (load from Google Fonts):**
- Antonio (weights 400, 600, 700)
- Montserrat (weights 400, 500, 600, 700, 800, 900)
- Playfair Display (italic 400)

**PDF download:**
- Use `html2pdf.js` library (`pnpm add html2pdf.js`)
- Letter size, 0 margin, render at 300 DPI for print quality
- If 4-up: arrange 4 identical cards in a 2x2 grid on letter page
- If 2-up: arrange 2 cards side by side on letter page (8.5" x 5.5")
- If 1-up: render one card centered on letter page
- Add dashed cut lines between cards (for 4-up and 2-up)

**Icon library:** Bundle these SVG line-art icons in `/public/icons/`:
- margarita, shot, hotdog, corn, lime-wedge, agave, jalapeno, taco, tequila-bottle

**Brand logos:** Bundle these PNG logo files (different colors of the same script "Uno Más" + "Tacos & Tequila") in `/public/logos/`:
- logo-pink.png, logo-teal.png, logo-yellow.png, logo-navy.png, logo-blue.png

The app should auto-pick the right logo based on the selected color theme. For yellow theme, use logo-navy.png since yellow doesn't read on white.

===

---

## EDITABLE FIELDS — THE COMPLETE LIST

| Field | Default value | Type |
|---|---|---|
| Color theme | Pink | Dropdown (Pink/Teal/Yellow/Navy/Blue) |
| Eyebrow | Pre-Cinco · May 1 + 2 | Text input |
| Headline line 1 | Cinco | Text input |
| Headline line 2 | Starts Today | Text input |
| Subhead | We're not waiting till Tuesday | Text input |
| Date range | FRI MAY 1 · SAT MAY 2 | Text input |
| Special 1 — price | $8 | Text input |
| Special 1 — name | House Margs | Text input |
| Special 1 — icon | margarita | Dropdown |
| Special 2 — price | $3 | Text input |
| Special 2 — name | Latin Candy Shots | Text input |
| Special 2 — icon | shot | Dropdown |
| Special 3 — price | $10 | Text input |
| Special 3 — name | Sonoran Dogs | Text input |
| Special 3 — icon | hotdog | Dropdown |
| Special 4 — price | $8 | Text input |
| Special 4 — name | Street Corn | Text input |
| Special 4 — icon | corn | Dropdown |
| Tagline | Get a little lost at Uno Más. | Text input |
| Address | 2020 N Monroe · @unomastacoshop | Text input |
| Cards per page | 4 | Radio (1 / 2 / 4) |

---

## ASSETS YOU'LL NEED TO UPLOAD TO LOVABLE

All of these are already in this campaign folder under `_brand-assets/`:

**Logos (PNGs, transparent backgrounds):**
- `logo-script-pink.png`
- `logo-script-teal.png`
- `logo-script-yellow.png`
- `logo-script-navy.png`
- `logo-script-blue.png`

**Icons (SVGs, transparent, navy ink):**
- `icon-set-margarita.svg`
- `icon-set-shot.svg`
- `icon-set-hotdog.svg`
- `icon-set-corn.svg`

**Optional additional icons (engraving PNGs, transparent):**
- `icon-margarita-transparent.png` (more detailed copper engraving version)
- `icon-shot-lime-transparent.png`
- `icon-jalapeno-transparent.png`
- `icon-lime-wedge-transparent.png`

In Lovable, drop these into `/public/brand-assets/` and reference them in the React component as `/brand-assets/[filename]`.

---

## PDF DOWNLOAD CODE (drop into Lovable)

```jsx
import html2pdf from 'html2pdf.js';

function downloadPDF() {
  const element = document.getElementById('print-area');
  const opt = {
    margin: 0,
    filename: 'fresh-sheet.pdf',
    image: { type: 'jpeg', quality: 0.98 },
    html2canvas: {
      scale: 3,                          // 3x = ~300 DPI
      useCORS: true,
      letterRendering: true,
      backgroundColor: '#FFFFFF'
    },
    jsPDF: {
      unit: 'in',
      format: 'letter',
      orientation: 'portrait'
    }
  };
  html2pdf().set(opt).from(element).save();
}
```

The `print-area` div should wrap the live preview at exactly 8.5×11 inches (with the 4 cards inside it). When the button is clicked, `html2pdf.js` snapshots that element and saves it as a print-ready PDF.

---

## WHY THIS APPROACH WORKS WELL FOR YOU

1. **No server needed.** Everything runs in the browser. Lovable's free tier handles it.
2. **Fast iteration.** When you want a new layout (Mother's Day, anniversary, summer), you don't need a designer — just open the app, type new copy, pick colors, download.
3. **Brand-locked.** The form constrains people to brand colors and approved typography. They can't "improve" the design by accident.
4. **Print quality.** `html2pdf.js` at scale 3 gives you ~300 DPI which prints sharp on cardstock.
5. **No file sync issues.** Every download is a fresh file with the current state.

---

## STRETCH FEATURES (phase 2)

If you want to push this further later:
- **Save presets:** Let users save named templates ("Cinco 2026", "Mother's Day Brunch") that can be loaded again
- **Brand switcher:** Add a dropdown for Uno Más vs The Mezzanine — swaps logo, fonts, color palette
- **AI copy assist:** Add a "Suggest" button that pings Claude API to generate new headline/tagline options
- **Version history:** Save every download with a thumbnail so you can revisit past sheets
- **Multi-language:** English/Spanish toggle for a Spokane bilingual audience

---

## QUICK START STEPS

1. Open Lovable, paste the prompt above into a new project
2. Wait for the initial build
3. Upload all the files from `_brand-assets/` to `/public/brand-assets/` in the Lovable file explorer
4. Test the form — type a new headline, change theme, see preview update
5. Click Download PDF — confirm it prints correctly at 100% scale on letter
6. Iterate: ask Lovable to tweak font sizes, add fields, etc.

If you hit a snag during the Lovable build, send me the error and I'll help debug.
