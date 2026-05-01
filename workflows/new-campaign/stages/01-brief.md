# Stage 1 — Brief

## Goal

Collect a structured brief from the user. Save it as `campaigns/{YYYY-MM}-{slug}/brief.md`.

## What to load before this stage

- `workflows/new-campaign/CLAUDE.md` (orientation)
- `brand-intelligence-center/system-prompt.md` (brand context — always load)
- This file
- (Optional) `marketing-knowledge/knowledge-center/AUDIENCE_PERSONAS.md` if user is unsure about audience

## Steps

1. Ask the user for a campaign name (free text). Confirm.
2. Derive a kebab-case slug from the name. Use `YYYY-MM` (current year-month).
3. Create the folder: `campaigns/{YYYY-MM}-{slug}/`
4. Walk the user through the brief questions (below). Multiple choice when possible. Skip optional fields if the user says "skip".
5. Save the answers to `campaigns/{YYYY-MM}-{slug}/brief.md` using the schema below.
6. Show the user the rendered brief for review.
7. Ask: "Brief saved. Ready for Stage 2 (pick a style)?" If yes, load `stages/02-pick-style.md`.

## Brief questions

Ask one at a time. Confirm answers before moving on.

### Required

1. **Campaign name** — free text. (Already have from step 1.)
2. **Goal** — pick one:
   - drive dinner covers (Ramsey's primary conversion)
   - drive Sunday Brunch traffic
   - promote a specific offer (happy hour, special, pitcher, etc.)
   - announce an event (Cinco de Mayo, Mother's Day, etc.)
   - launch a new menu item
   - drive Mezzanine / private event inquiries
   - drive loyalty / Cantina Club signups
   - brand awareness / vibes
   - travel / visitor discovery
   - other (free text)
3. **Venue context** — pick one (per Ramsey's three-venue model):
   - The Cantina (main floor)
   - The Mezzanine (upstairs speakeasy)
   - The Patio (outdoor)
   - All three / brand-level
4. **Platform / format** — pick one:
   - Instagram post (square)
   - Instagram story (9:16)
   - TikTok / Reel
   - Flyer (printed or digital, portrait)
   - Email header graphic
   - SMS (text only, no design)
   - Web banner (landscape)
   - Paid ad (Meta / Google)
   - Other (free text)
5. **Daypart / register** — pick one (drives tone):
   - Lunch (Tom Segura register, casual, 3-5 emojis)
   - Dinner (confident considered, 1-2 emojis, reservation CTA)
   - Patio / weekend (high energy, peer first)
   - Mezzanine / late night (cool older sibling, 0-1 emojis)
   - Brunch (warm, welcoming, family-friendly)
   - Other (free text)
6. **Target audience** — free text, ~1-2 sentences. If user is unsure, offer to load `AUDIENCE_PERSONAS.md` and pick one.
7. **Key offer / message** — free text. If price/date isn't decided, use placeholders: `[ADD PRICE]` or `[ADD DATE]`.

### Optional

8. **Menu items involved** — comma-separated list. Verify against `marketing-knowledge/knowledge-center/MENU_AND_OFFERS.md`. If a user mentions an item not on the menu, flag it: "I don't see {item} in MENU_AND_OFFERS.md. Did you mean {closest match}?"
9. **Themes / inspiration** — free text. Used as guidance for AI, not copied directly.
10. **Must-include facts** — anything copy MUST mention (specific date, RSVP detail, "21+ after 9pm").
11. **Phrases to avoid** — beyond the never-say list in `system-prompt.md`, anything specific to this campaign.

## Schema for `brief.md`

```markdown
# Brief — {Campaign Name}

**Date created:** {YYYY-MM-DD}
**Slug:** {YYYY-MM}-{slug}
**Created by:** {user name or "Ramsey"}

## Required

- **Campaign name:** {answer}
- **Goal:** {answer}
- **Venue context:** {answer}
- **Platform / format:** {answer}
- **Daypart / register:** {answer}
- **Target audience:** {answer}
- **Key offer / message:** {answer}

## Optional

- **Menu items involved:** {answer or "—"}
- **Themes / inspiration:** {answer or "—"}
- **Must-include facts:** {answer or "—"}
- **Phrases to avoid:** {answer or "—"}

---

## Brief notes

> Anything the user said that doesn't fit the schema but matters for downstream stages goes here.
```

## Confirmation

After saving, show the rendered file content. Ask: "Anything you want to change before we move to Stage 2?"

## Common issues

- **User wants to skip half the questions.** OK for optional fields. For required fields, push back: "I need {field} to make a good brief. Can you take a guess?"
- **User answers something off-menu.** Verify against `MENU_AND_OFFERS.md`. Flag and ask.
- **User wants to use a banned phrase.** Per `system-prompt.md` never-say list ("authentic," "mouthwatering," "artisanal," "vibrant," "perfect for any occasion," etc.). Flag and ask: "Want to override for this campaign?"
- **User mentions an event Ramsey doesn't currently do** (e.g., "Taco Tuesday"). Per Ramsey's repo: "Taco Tuesday previously removed." Flag.
- **User changes their mind mid-brief.** Reopen the previous question.
