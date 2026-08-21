# Using the Uno Más agent across Claude, ChatGPT, and Gemini

**The short answer:** the agent itself runs **only in Claude Code.** The three skills
(`/unomas-update`, `/unomas-find`, `/unomas-design`) are Claude Code files — ChatGPT and Gemini
cannot execute them. What ChatGPT and Gemini *can* do is work from the same brand truth and hand
results back.

---

## Capability matrix

| Platform | Runs the agent? | What it can actually do | Setup |
|---|---|---|---|
| **Claude Code** — VS Code ext · desktop app · terminal · claude.ai/code | ✅ **Full agent** | Everything. Propagate changes, find files, build collateral, edit the live site, query Supabase/Toast/Cloudinary, commit + push. **The only surface that WRITES.** | `bash scripts/bootstrap-agent.sh` |
| **claude.ai** chat · Claude mobile · Claude Projects | ❌ No skills | Read the repo (GitHub connector), answer brand questions, draft copy. Read-only. | Project + `marketing/brand-context-pack.md` in instructions |
| **ChatGPT** (Plus/Pro/Team) Custom GPT | ❌ No skills | Image prompts + generation, copy drafting, **Cloudinary DAM search** via the official connector | `marketing/custom-gpt-setup.md` |
| **Gemini** Gem | ❌ No skills | **Native image generation** (Imagen), reads `Ramsey-SL/uno-mas` live via the GitHub connection | `marketing/gemini-gem-setup.md` |

## The one rule that keeps all four in sync

> **Claude Code is the only thing that writes. Everything else drafts, then hands back through
> `/unomas-update` or `/unomas-design`.**

This isn't a preference. The August 2026 ChatGPT handoff was stale in **six** places — Burrito
Thursday, the Mahi-Mahi special, the 21+ policy, the Wednesday offer, "The Guest List," Squarespace
— because 45 days of good work happened with no write path back into the repo. Any tool without a
write path drifts the same way.

When ChatGPT or Gemini produces something worth keeping, say so in Claude Code:
*"ChatGPT drafted this Thursday copy — add it to the copy bank"* → it gets filed, versioned, and
made visible to every other surface.

## What each is genuinely best at

- **Claude Code** — anything touching real systems. If it changes a file, a database, a site, or an
  asset, it happens here.
- **ChatGPT Custom GPT** — image prompt engineering and generation, plus DAM search. The official
  Cloudinary connector OAuths to the account, so it can surface real approved assets.
- **Gemini Gem** — native image generation, and it reads the repo live so its brand context can't
  go stale the way an uploaded file does.
- **claude.ai / mobile** — capture and thinking on the go. Note what changed; propagate from a laptop.

## Keeping their context current

All three non-Claude-Code surfaces share one knowledge file: **`marketing/brand-context-pack.md`**
(~7KB, deliberately sized to paste or upload).

- **Gemini** reads the repo live → no refresh needed.
- **ChatGPT / Claude Projects** use an uploaded copy → **re-upload after any brand change.** There
  is no auto-sync. A copy of the pack also sits in
  `~/Documents/Uno-mas-hq-2026/um-marketing-agent/CHATGPT-context-pack.md` (refresh it with that
  folder's `refresh.sh`).

⚠️ **Stale knowledge files are the #1 way drift re-enters the system.** If you ruled on something
in Claude Code today, the ChatGPT GPT still believes the old thing until you re-upload.

## Current facts these assistants must have (as of 2026-08-21)

Any GPT/Gem set up before **2026-08-21** is wrong about all of these:

- **Thursday is Big F'N Thursday** — $10 Big F'N Quesadilla + $10 menu tequila cocktail fresh sheet. **Burrito Thursday is retired.**
- **Kid-friendly at all times — NO 21+ window anywhere, The Mezzanine included.** Exceptions: ticketed events, alcohol purchase.
- **One loyalty program: The Cantina Club, and it is FREE.** Paid tiers are future-state — never referenced publicly. "Uno Más Rewards" and "The Guest List" are retired names.
- **Hours: Tue–Thu 11am–8pm** (not 9pm) · Fri–Sat 11am–10pm · Sun 10am–4pm · Mon closed.
- **Taco Tuesday $6 margs / $30 pitchers.**
- **Mahi-Mahi was dropped** — never printed on the brunch menu.
- **Two creative systems** — photographic for experience, illustrated promo-card for offers. Never blend.
- **`needs-hires-swap`** — ~141 Cloudinary assets are 2048px social-only. Not for print.
- **BFQ:** `Big F'N Quesadilla` in marketing; the menu keeps `Big F*** Quesadilla`. $10 is the **base** price — proteins extra.
