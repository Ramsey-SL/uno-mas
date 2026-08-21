---
name: unomas-design
description: Build Uno Más visual work — posters, flyers, table tents, menus, social graphics, ads, print collateral, mockups, one-pagers, decks, and site UI — on-brand and using real DAM assets. Use whenever Ramsey asks to design, make, build, mock up, lay out, or produce a graphic, poster, menu, ad creative, social post visual, or any visual deliverable for Uno Más or The Mezzanine.
---

# Uno Más — Design Production

You produce finished, on-brand visual work. Never a description of a design — the design.

## Step 0 — Load brand truth (always)

1. `~/projects/uno-mas-brand/CLAUDE.md` — brand name rule, voice, Visual Identity quick ref.
2. `~/projects/uno-mas-brand/design-system/tokens.css` — **the canonical palette, type, spacing, radius, shadow tokens.** Use these values verbatim; don't eyeball colors.
3. `~/projects/uno-mas-brand/marketing/brand-guidelines/` — `01-brand-colors`, `02-typography`, `03-logo-rules`, `06-photography-style`, `07-design-layout-rules`, and `11-mezzanine-brand-identity` when the piece is Mezzanine.
4. `~/projects/uno-mas-brand/marketing/ecosystem-registry.md` — for the fact you're putting on the piece. **Never design around a price, date, or offer you haven't verified against its canonical owner** (registry §3). A beautiful poster with last month's price is worse than no poster.

## Step 1 — Route to the right medium

| Ramsey wants | Build it as | Notes |
|---|---|---|
| **Poster, flyer, table tent, print menu, print insert** | **Self-contained HTML at exact pixel dimensions** — the house pattern | See §2. This is the default for print. |
| **Social graphic** (IG/FB feed, story, TikTok cover) | HTML at `1080×1350` (4:5 feed) or `1080×1920` (9:16 story) | Same house pattern, different canvas. |
| **Editable-by-Ramsey / handoff to Karissa** | **Canva** via MCP | Brand kits: Uno Más `kAFqKpAzOh0`, Mezzanine `kAGze1MPDmA`. Use `create-design-from-brand-template` / `generate-design`, then `export-design`. |
| **Multi-concept exploration, screen flows, several artboards to compare** | the **`design` skill** (canvas of `.dc.html` artboards) | Right call when Ramsey needs to *choose*, not receive one answer. |
| **Website / app UI** | **Lovable** `send_message` on the relevant project | Marketing site `78c4ac75-…`, Cantina Connect `9e76084a-…`. Use design-system tokens. Always append the typecheck-only instruction (see `unomas-update` skill). |
| **Report, one-pager, deck-style doc to share** | **Artifact** (load `artifact-design` first) | For things with an audience, not print. |
| **Chart / dashboard / data graphic** | load the **`dataviz`** skill first | Then apply the Uno Más palette. |
| **AI-generated photography or illustration** | Write the prompt set; hand to Gemini/ChatGPT | Follow `marketing/image-generation-playbook.md` and its rubric. |

When it's ambiguous, prefer HTML — it's versionable, reviewable in the repo, and exports to print.

## Step 2 — The house print pattern (copy it, don't reinvent)

Working examples live in `marketing/campaigns/daily-specials/`: `poster-taco-tuesday.html`,
`poster-midweek-lineup.html`, `table-tent.html`. Read one before you start.

The pattern:
- **Single self-contained `.html` file.** Google Fonts `@import` for Antonio + Montserrat. All CSS inline in one `<style>`. No build step, no external JS.
- **Exact canvas:** `.poster{width:1080px;height:1350px;position:relative;overflow:hidden}` for 4:5. Set `-webkit-print-color-adjust:exact;print-color-adjust:exact`.
- **Photo layer** `.bg{position:absolute;inset:0;object-fit:cover}` + a **scrim** gradient over it so type stays legible: `linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.05) 32%,rgba(0,0,0,.35) 60%,rgba(10,5,20,.95) 100%)`.
- **Content layer** `position:absolute;inset:0;display:flex;flex-direction:column;justify-content:space-between;padding:62px 64px 56px`.
- **Print block:** `@media print{body{background:#fff;padding:0}@page{size:1080px 1350px;margin:0}.poster{box-shadow:none}}`
- **A `.hint` div at the top** (hidden in print) telling Ramsey how to export: *"Print-ready 1080×1350 (4:5). Export: Cmd+P → Save as PDF, or screenshot at 2×."*
- **Embed the photo as a base64 data URI** so the file is portable and prints reliably. Fetch from Cloudinary, then base64 it.
- Render a preview to PNG and **look at it** before handing it over.

## Step 3 — Brand rules that are not negotiable

- **Pink `#E22690` is the hero color / primary CTA.** Don't let navy or blue dominate a piece.
- **Palette (from `tokens.css`):** navy `#003366` · blue `#18BCDC` · teal `#27F3DE` · green `#25E9B9` · yellow `#FFEC00` · pink `#E22690` · dark grey `#212121` · warm surface `#F8F5EF`.
- **Type:** **Antonio** headlines (weight 600–700 — *never heavier, it reads blocky*), uppercase, tracking `0.01em`, leading `0.95`. **Montserrat** body. **Thirsty Rough** is decorative-only, licensed, and must never compete with the logo.
- **Eyebrows:** 12px, uppercase, weight 700, letter-spacing `.26em`.
- **NEVER mix Uno Más and Mezzanine brand elements in one design.** The Mezzanine is a distinct sub-brand: black foundation, Electric Pink `#E22790`, Magenta `#BF28BF`, Ultra Violet `#93009B`; DIN Condensed VF / Poppins / Baka Too. Cool, atmospheric, minimal.
- **Brand name is always "Uno Más"** with the accent. Check every rendered string — including ones baked into images.
- Voice on the piece follows `CLAUDE.md`: short, confident, price-confident, no banned words ("authentic Mexican", "mouthwatering", "culinary journey", "artisanal", "mixology", "perfect for any occasion").
- **BFQ rendering:** consumer creative uses `Big F’N Quesadilla`; the menu keeps `Big F*** Quesadilla`. Don't reconcile them.

## Step 4 — Source real assets, never placeholders

- **Photos/video:** Cloudinary `drxrfyq9i`, tree `uno-mas/approved-assets/{photos,videos}/<cat>`. Search by tag (`approved-assets`, `category-food`, `category-cocktails`, …). If nothing fits, check the Drive warehouse (`unomas-find` skill routes this) before resorting to AI generation.
- **House photo grade** (match the site): `e_saturation:18,e_contrast:10,e_brightness:4`; images `c_fill,g_auto`, videos `c_fill,g_center`.
- **Line-art icons** live at `uno-mas/website/icons/…`. The site recolors them with this chain — reuse it: `e_make_transparent:45/e_colorize,co_rgb:<HEX-no-hash>/e_trim/c_fit,h_160,f_auto,q_auto`.
- **Texture:** `uno-mas/website/icons/icons-pattern-forramsey-02-1.png` at ~5% opacity is the house background texture.
- **Logos:** `uno-mas/approved-assets/logos`. Follow `03-logo-rules.md` for clear space and which lockup on which background.
- Cloudinary is **free plan** — don't upload new derivatives casually. Deliver transform URLs.
- If the Cloudinary connector isn't authorized, say so and use the signed REST Admin API via curl.

## Step 5 — Deliver

- Write files into the right campaign folder: `marketing/campaigns/<campaign-slug>/`. Follow the existing naming: `poster-<slug>.html`, `table-tent.html`, `creative-copy.md`, `campaign-brief.md`.
- **Render and view a PNG preview** of anything print-bound before calling it done.
- Commit and push. Note the piece in the campaign's `campaign-brief.md` collateral list.
- If the piece supersedes existing collateral, **retire the old file** (`_RETIRED-<date>-<name>`) rather than deleting it, and say what it replaced.
- Tell Ramsey the export step (Cmd+P → Save as PDF at the stated size) and what still needs a real photo.

## Authority

Full autonomy to create files, commit, push, generate Canva designs, and read Cloudinary/Drive.
**Confirm first:** publishing to a public social account, sending a live campaign, deleting or
overwriting existing approved creative, uploading new assets that consume Cloudinary credits, or
anything that spends money.
