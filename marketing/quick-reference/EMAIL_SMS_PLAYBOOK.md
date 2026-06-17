# Uno Más — Email & SMS Playbook
*Klaviyo flows, campaign cadence, and copy rules*

---

## Platform Overview

**Email Platform:** Klaviyo
**SMS Platform:** Klaviyo (same account)
**List Source:** Toast / Uno Mas Rewards: The Cantina Club loyalty data, website signup, in-store QR codes
**Playbook files:** `05_EMAIL_SMS/` — Flow diagrams, templates, playbook doc

---

## Active Klaviyo Flows (Automated)

| Flow | Trigger | Goal |
|------|---------|------|
| Welcome Series | New subscriber | Introduce brand, drive first visit |
| Post-Purchase | Toast order completed | Thank you, loyalty nudge, upsell |
| Win-Back | 60 days no open/purchase | Re-engage lapsed customers |
| Birthday | Profile birthday date | Personal touch, drive visit |
| Loyalty Milestone | Points threshold reached | Celebrate + redeem offer |
| Abandoned Browse | Website visit, no order | Remind + incentivize |

*Full flow diagrams: `05_EMAIL_SMS/Uno-Mas-Klaviyo-Flow-Diagrams.html`*
*Full playbook: `05_EMAIL_SMS/Uno-Mas-Klaviyo-Playbook.docx`*

---

## Campaign Cadence

| Frequency | Type | Notes |
|-----------|------|-------|
| Weekly | Promotional email | Tuesday or Wednesday send, 10–11am |
| Weekly | SMS blast | Thursday or Friday, 11am–1pm |
| Monthly | Newsletter-style | Longer, more personal, highlights month |
| Event-driven | Announcements | 1 week out + day-of reminder |
| Seasonal | Big pushes | Cinco de Mayo, Holidays, Bloody Mary Bash |

**Max sends per week:** 2 emails, 1–2 SMS
**Do not send** email and SMS on the same day unless it's a major event

---

## Email Copy Rules

### Subject Lines
- **Under 50 characters** — most clients truncate longer
- Test 3 types every send:
  - **Curiosity:** "You're going to want to see this."
  - **Direct:** "Lunch special is live — today only."
  - **Personal:** "Ramsey, we saved you something."
- Avoid: ALL CAPS, excessive punctuation, spam-trigger words ("FREE!!!", "Act now")

### Preview Text
- Always write custom preview text — never leave it blank
- Should complement or continue the subject line, not repeat it
- 40–90 characters

### Email Body
- **Under 200 words** for promos — people skim
- Lead with the offer or the hook, not a greeting
- One primary CTA per email (two maximum)
- CTA buttons: action-oriented ("Order Now", "Claim Your Offer", "See the Menu")
- Sign off casually: "See you soon, — The Uno Más crew" not "Sincerely, Management"

### Design Rules
- Mobile-first — 60%+ of opens are on phone
- Use templates in `05_EMAIL_SMS/Uno-Mas-Email-Design-Templates.html`
- Hero image: food photography, high contrast, no text baked into image
- Brand colors: Pink `#E22690` (primary CTA), Navy `#003366` (background/headers), Blue `#18BCDC` (accents) — see BRAND_ASSETS.md. Do NOT use generic teal or cream palettes.
- Font: Antonio for headlines, Montserrat for body — use system font fallbacks for email reliability

---

## SMS Copy Rules

### Format
- **160 characters max** per segment (avoid going to 2 segments when possible)
- Always include: offer/info, short link, opt-out reminder on first message of new campaign
- Structure: Hook → Value → Link
  - "Lunch special is live — 2 tacos + side, $12. Order: [link]"

### Tone
- Write like a text, not a broadcast
- No corporate language — "Hey! We've got a deal..." not "Dear Valued Customer..."
- First-name personalization when possible: "Hey [First Name], tacos are calling."

### Best Practices
- Send between 11am–6pm only (respect time zones, no dinner interruption)
- Max 2 SMS per week — subscribers are protective of their texts
- Use for: flash deals, day-of reminders, events, limited-time offers
- Don't use for: general brand updates or content that belongs in email

---

## Segmentation Quick Guide

| Segment | Who | Use For |
|---------|-----|---------|
| All subscribers | Everyone | Major announcements, Cinco de Mayo |
| Engaged (opened in 30 days) | Active list | Best offer tests, loyalty rewards |
| Lapsed (60+ days no open) | At-risk | Win-back campaigns only |
| VIP (top 10% by spend/visits) | High-value | Early access, exclusive offers |
| SMS only | Phone subscribers | Time-sensitive promos only |
| Location-based | Monroe (current flagship) | Location-specific events or updates |

---

## Metrics — What to Watch

| Metric | Target | Alert If Below |
|--------|--------|---------------|
| Email open rate | 35–45% | < 25% |
| Email click rate | 3–6% | < 2% |
| SMS click rate | 8–15% | < 5% |
| Unsubscribe rate | < 0.3% | > 0.5% |
| List growth MoM | Positive | Flat or declining |

*Pull reports from Klaviyo dashboard or see `10_REPORTS/` for archived performance data.*

---

## Quick Campaign Launch Checklist

- [ ] Subject line + preview text written (3 options, A/B test 2)
- [ ] Body copy reviewed against brand voice cheat sheet
- [ ] CTA button tested — does the link work?
- [ ] Mobile preview checked in Klaviyo
- [ ] Segment selected — not blasting the full list unnecessarily
- [ ] Send time set (Tue/Wed for email, Thu/Fri for SMS)
- [ ] UTM parameters added to links for tracking

---

*Last updated: April 2026 | Folder: `_QUICK_REFERENCE/`*
*Full Klaviyo playbook: `05_EMAIL_SMS/Uno-Mas-Klaviyo-Playbook.docx`*
