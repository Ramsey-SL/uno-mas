# ⚠️ Conflicts found after syncing with the remote repo — 2026-09-03

This email was built from a local checkout that was ~20 commits stale. After fetching,
three material conflicts surfaced with work already recorded in the repo. **None have
been resolved.** Read before sending.

---

## 1. The $25 promo has an exclusion this email does not mention — BLOCKING

`marketing/campaigns/marg-dip-drop-sep2026/campaign-brief.md` states:

> **Exclusion — Not valid 8–10pm Fri & Sat during Late Night Happy Hour**

This email currently says the $25 offer runs *"all day, every day we're open — right
through Sunday"* and, in the very next block, promotes Late Night Happy Hour on Friday
and Saturday 8–10pm. As written, the email invites guests to do both at once.

**Real-world consequence:** someone arrives 8:30pm Friday expecting margs + dip for $25
and gets told no, in the middle of the promo we just texted them about.

The printed table tent also reads **WED–SUN · ALL DAY** with no exclusion.

**Needs a ruling:**
- (a) The exclusion still stands → I add a fine-print line to block one and the SMS.
- (b) The exclusion was dropped when the promo went live → update the brief, and the
  Late Night block should probably say the $25 deal is *also* available.

Until this is settled the email should not send.

## 2. Thursday naming — RESOLVED 2026-09-03

**Ruling: the name is and stays "Big F'N Thursday."** "Tequila Thursday" was my error —
I renamed it across the knowledge base and deployed it to the live site before checking
against the repo, which had it as Big F'N Thursday in 128 places since August 2026.

Reverted: the site has been changed back, and the stale rename never reached the
knowledge base (those edits were dropped in the rebase). The offer itself was never
wrong — $10 Big F'n Quesadilla + $10 tequila cocktails.

## 3. Creative system mismatch

`marketing/campaign-architecture.md` specifies that Weekly Promo Drops use the
**illustrated promo-card system** — cream ground, illustrated food and cocktails,
letterpress/riso feel — *not* the photographic pattern.

This email is photographic. That may be right for email even if print is illustrated,
but it is a deliberate documented system and this departs from it. Worth a conscious
decision rather than an accident.

---

## Also worth knowing — affects this send

`marketing/campaigns/weekend-promos/executions-log.md` flags that the **Toast email
footer reads "Uno Mas Taco Shop"** — no accent on Más, and "Taco Shop" is banned in brand
descriptions by `CLAUDE.md`. It appears in **every marketing email Toast sends**,
including this one. Fix is to rename the Toast organization to
**"Uno Más Tacos & Tequila"** before sending.
