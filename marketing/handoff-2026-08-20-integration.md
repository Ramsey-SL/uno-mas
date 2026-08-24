# ChatGPT Marketing Handoff — Integration Record (2026-08-20)

Source package: `~/Downloads/uno_mas_marketing_handoff_2026-08-20/` — 10 files, coverage window
**July 7 – Aug 20 2026.** Reviewed and integrated into this repo on 2026-08-20.

---

## 1. What was genuinely new — integrated

| What | Where it landed |
|---|---|
| **"Get a Little Lost" as an acquisition *platform***, not just a tagline | `marketing/campaign-architecture.md` §1 |
| **The six-step guest ladder** (Discover → Visit → Return → Join → Regular → Member) | `campaign-architecture.md` §2 |
| **"Belonging beats bargains"** retention positioning | `campaign-architecture.md` §1 |
| **Cantina Club copy guardrails** — no VIP/elite/boss-level for La Familia; never gate on positive reviews; reward frequency before spend; specific economics when selling | `campaign-architecture.md` §7 + `.claude/skills/unomas-design` |
| **12 Toast lifecycle automations** + measurement rules (incremental visits, not opens/clicks; review at 30 days then monthly) | `marketing/toast-lifecycle-automation-playbook.md` (new) |
| **Channel role definitions** for email / SMS / social / web / in-restaurant | `campaign-architecture.md` §4 |
| **Campaign pre-flight checklist** | `campaign-architecture.md` §8 |
| **16 Canva design IDs** incl. three masters | `marketing/canva-design-manifest.md` (new) |
| **`needs-hires-swap` print gate** (~141 assets are 2048px social-only) | `ecosystem-registry.md` Cloudinary section + hard gate in `unomas-design` |
| **143 new assets, `_v#` naming, 11 named promo public_ids, love-island-finale folder** | `ecosystem-registry.md` |
| **Wildfire / community-sensitive messaging precedent** | `marketing/quick-reference/COMMUNITY_SENSITIVE_MESSAGING.md` (new) |
| **New fact classes** F13 lifecycle automations, F14 campaign platform | `ecosystem-registry.md` §3 |

## 2. Where the handoff was already STALE — repo wins

The handoff was generated 2026-08-20 but reflects an earlier state. **Do not treat it as current on:**

1. **Burrito Thursday.** The handoff names it a current priority program throughout. It was **retired 2026-08** and replaced by **Big F’N Thursday** ($10 Big F’N Quesadilla + $10 menu tequila cocktail fresh sheet). Its two promo assets (`20260723_UM_PROMO_BurritoThursdays_v1`, `20260730_..._v2`) are retired creative.
2. **Mahi-Mahi / Baja fish taco special.** Presented as active development ($30 dinner plate / $12 lunch taco). The repo already resolved this **2026-08-04: Mahi-Mahi did not make the final printed brunch menu — dropped.** Do not build creative for it without a new ruling.
3. **21+ policy.** The handoff is silent on it. Ruled 2026-08-20: **kid-friendly at all times, no 21+ window anywhere including The Mezzanine** (exceptions: ticketed events, alcohol purchase).
4. ~~**Weekend spend promo.**~~ **RESOLVED 2026-08-23:** the $10-off-$60 offer was the **first of a rotating weekly test series and is now OVER.** The repo's "locked offer" framing was wrong — weekend offers rotate. Full chronology in `campaigns/weekend-promos/executions-log.md`. The redemption phrase varies per execution ("Mickey", "Mas Please", `WEEKEND10`) — always confirm the current one.
5. **Beer & Bites Wednesday** is described as "$5 drafts / draft-led." Canonical is **$5 pints · $10 loaded nachos · $10 loaded masa fries**. The promo asset name `FiveDollarDrafts` reflects the older framing.
6. **Squarespace / site migration** framing in older brand-intel is obsolete — the Lovable site is live on `unomastacoshop.com`.

**Also note:** the handoff's own source-of-truth hierarchy puts *"current Uno Más brand documentation / master prompt / GitHub documentation"* above *"recent campaign executions as examples, not permanent rules."* That is consistent with this repo's owner-wins doctrine — the handoff agrees it is the junior source.

## 3. Voice tension worth a decision

The handoff's **SMS rule** says *"avoid emojis unless they materially improve the message"* because
segment count drives cost. `CLAUDE.md`'s voice rules prescribe **3–5 emojis** for casual/social and
frame email/SMS as *"a friend texting good news."* These are not irreconcilable — the handoff rule
is a **channel-economics constraint specific to SMS** — but the repo should say so explicitly.
**Recommended:** keep the playful emoji guidance for social and email; adopt a lean-emoji rule for
SMS on cost grounds. Not applied yet — awaiting Ramsey.

## 4. Unresolved — needs a ruling

1. **Free loyalty tier name:** "Uno Más Rewards" (repo) vs **"The Guest List"** (handoff) vs "Más Rewards" (playbook). The repo's program spec logs this as an open decision; the handoff answers it with a name the repo has never used. → registry §4 item 11.
2. **Paid Cantina Club launch status** — live or not? → registry §4 item 12.
3. **"Mas Please"** — is that the live redemption phrase for the weekend offer?
4. **SMS emoji policy** — adopt the lean-SMS rule? (§3 above)

## 5. Binaries still to retrieve (8 files)

The handoff explicitly could not export these; they sit in the **ChatGPT File Library** and must be
exported manually. Highest value first:

- [ ] **`Cantina-Club-Brand-Messaging-Book.md`** (July 2026) — declared *single source of truth* for Cantina Club positioning, audience, voice, visual identity, tier language, copy guardrails. **This is the most important missing file** — it likely settles the free-tier naming question.
- [ ] **`Uno_Mas_Toast_Automation_Playbook.docx`** — triggers, timing, CTAs, KPIs, copy for the 12 automations.
- [ ] `Uno_Mas_Toast_Automation_Tracker.docx` — implementation tracker.
- [ ] `Uno_Mas_Loyalty_Staff_Quick_Guide.pdf` — staff-facing process.
- [ ] `uno-mas-klaviyo-email-clickable-sections.html` — the modular email implementation.
- [ ] `Uno_Mas_Love_Island_Bingo_60_Cards.pdf` — reusable event collateral.
- [ ] `Festive Sunday brunch menu design.png` — brunch menu creative reference.
- [ ] `Uno Más Gift Card Series Mockup.png` — physical gift-card concepts (a program the repo has nothing on).

**Note:** `.gitignore` blocks `*.pdf`, `*.png`, `*.docx`. Convert the DOCX/HTML content to `.md` in
the repo and keep the binaries in Drive / Cloudinary, per the three-tier storage model.

## 6. Net assessment

The handoff's real value is **strategic, not factual.** Its facts are behind the repo in six places.
But it carries a layer this repo genuinely lacked: *why* campaigns exist, how they ladder into
loyalty, what the channels are each for, and the guardrails that keep a loyalty program from
turning into a discount treadmill. That layer is now in `campaign-architecture.md` and wired into
`/unomas-design`'s pre-flight.

The single most operationally valuable discovery is the **`needs-hires-swap` tag** — without it,
the design agent would have happily sent a 2048px social derivative to a large-format print job.
