# Weekend email — image export for Toast

Rendered from `mockup-9-poster.html` at **600px CSS width @ 2× = 1200px actual**, the
standard for email: 600px is the safe body width, and 2× keeps it sharp on retina
screens where a 1× image looks soft.

Full email is **600 × 3335 CSS px** (1200 × 6671 actual).

## Use the slices, not the full image

| File | CSS size | Weight | Contains |
|---|---|---|---|
| `slice-01.jpg` | 600×403 | 57KB | Logo + hero headline |
| `slice-02.jpg` | 600×852 | 213KB | $25 margs + chips block |
| `slice-03.jpg` | 600×874 | 210KB | Late Night Happy Hour block |
| `slice-04.jpg` | 600×726 | 189KB | Sunday brunch block |
| `slice-05.jpg` | 600×478 | 56KB | Sign-off + footer |
| **Total** | | **725KB** | |

Cut lines land in background gaps between blocks — nothing is sliced through a photo,
headline or button.

`uno-mas-weekend-email_1200w_full.jpg` (733KB) and `_full.png` (4MB) are the whole email
in one piece. The PNG is archival only — **do not send it**, it's far too heavy.

## How to assemble in Toast

Upload the five slices in order and stack them with **no gaps and no padding between
them**, each set to 600px display width. Any spacing between slices shows as a seam.

Set the click-through per slice:

| Slice | Link |
|---|---|
| 01 | `https://unomastacoshop.com` |
| 02 | `https://unomastacoshop.com` |
| 03 | `https://unomastacoshop.com/menu?tab=late-night` |
| 04 | `https://unomastacoshop.com/reservations` |
| 05 | `https://unomastacoshop.com` |

This is the main reason to slice rather than send one tall image — a single image can
only carry one link, so the "See the late night menu" and "Reserve a table" buttons
would both be dead.

## Alt text (set this — many people see it before the images load)

- 01 — `Uno Más. Three things worth showing up for this weekend.`
- 02 — `Two house margaritas plus chips and dip for $25, now through Sunday 4pm.`
- 03 — `Late Night Happy Hour, Friday and Saturday 8 to 10pm. Any two street tacos $10.`
- 04 — `Sunday Brunch, 10am to 4pm. Reserve a table.`
- 05 — `Get a little lost. 2020 N Monroe St, Suite C, Spokane. (509) 960-7989.`

## Known trade-offs of an image-only email

1. **Images off = blank email.** Many clients block images by default, and Outlook
   often does. Alt text is the only fallback, which is why it's set above.
2. **No live text** — nothing is selectable, searchable, or resizable, and screen
   readers get only the alt text.
3. **Deliverability.** Image-only emails with little or no real text score worse with
   spam filters. Add a line or two of live text in Toast above or below the images —
   even just the offer and the address — to reduce the risk.
4. **Dark mode** won't invert; the image renders exactly as-is. Fine here, since the
   design is already mostly dark.

If Toast has a drag-and-drop builder with text, image and button blocks, rebuilding the
layout natively there beats pasting images — live text and real buttons. Ask me and
I'll write it out block by block.
