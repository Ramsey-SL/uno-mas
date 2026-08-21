# Working with the Uno Más agent — devices & tools

**Short version:** the agent is a set of files inside this repo, symlinked into `~/.claude/`.
The repo is what makes it portable. Clone the repo on a machine, run the bootstrap, and that
machine has the agent.

---

## The three commands

| Command | What it does |
|---|---|
| `/unomas-update <what changed>` | Propagate an information change across every surface |
| `/unomas-find <what you need>` | Locate a file, asset, doc, number, or design anywhere |
| `/unomas-design <what you need>` | Build a poster, menu, social graphic, ad, mockup, or site UI |

Plus the `unomas-steward` subagent for multi-surface work and full drift audits.

## Where they work

**This machine — everywhere.** VS Code extension · Claude Code desktop app · terminal (`claude`
from any directory) · `claude.ai/code` on the web with this machine connected. Same skills, because
they're installed at the user level.

**A new Mac/laptop — two commands:**

```bash
git clone git@github.com:Ramsey-SL/uno-mas.git ~/projects/uno-mas-brand
bash ~/projects/uno-mas-brand/scripts/bootstrap-agent.sh
```

That's it. The bootstrap script creates the symlinks. Everything else the agent needs — the
registry, the brand docs, the skills — came with the clone.

**What a new machine still needs separately** (these are credentials, not agent files):
- Claude Code signed in
- The claude.ai connectors authorized: Cloudinary, Google Drive, Canva, Klaviyo, Supabase, Lovable, Meta Ads
- SSH access to the GitHub repo

**Phone / iPad.** Realistically: **capture on mobile, execute on desktop.** The Claude mobile app
can't run these skills. Use mobile to note what changed or photograph a new menu, then run the
actual propagation from a laptop. Or drop files in a synced folder (see Inbox below).

## Using ChatGPT alongside Claude

ChatGPT **cannot run these skills** — they're Claude Code files. But it can absolutely be part of
the workflow, and the repo is the interop layer.

**Give ChatGPT context:** paste or upload **`marketing/brand-context-pack.md`** (~7KB, ~100 lines —
sized deliberately to paste into a chat or drop into a Project's instructions). For deeper work use
`brand-intelligence-center/system-prompt.md`. Point a ChatGPT Project at the GitHub repo if you have
a connector for it.

**The rule that keeps this from breaking:**

> **Claude Code is the only thing that WRITES. ChatGPT drafts and thinks; decisions come back
> through `/unomas-update` so they land in the repo.**

This isn't preference — it's the lesson from the Aug 2026 handoff. That package was stale in six
places (Burrito Thursday, the Mahi-Mahi special, the 21+ policy, the Wednesday offer, "The Guest
List", Squarespace) **precisely because 45 days of work happened outside the repo with no write path
back.** Good work, invisible to every other surface. Any tool without a write path back will drift
the same way.

**Practical division of labor:**

| Tool | Good at | Hand back via |
|---|---|---|
| **Claude Code** (this agent) | Anything touching real systems: propagating changes, finding files, building collateral, editing the site, querying Supabase/Toast/Cloudinary | — it writes directly |
| **ChatGPT** | Long-form ideation, copy variants, image generation, riffing on campaign concepts | Paste the outcome into `/unomas-update` or `/unomas-design` |

When ChatGPT produces something worth keeping, say: *"ChatGPT drafted this Thursday copy, add it to
the copy bank"* — and it gets filed, versioned, and made visible to every other surface.

## Portable snapshot

`~/Documents/Uno-mas-hq-2026/um-marketing-agent/` holds a **copy** of the agent — skills, the
steward, this doc, the bootstrap script, the ChatGPT context pack, and snapshots of the brand brain
and registry. Useful for reading offline, handing to someone else, or setting up a new machine.

**It is not what runs.** The repo `.claude/` is. Re-sync the snapshot with `bash refresh.sh` inside
that folder — an un-refreshed copy is exactly the drift this system exists to prevent.

## Inbox convention (for menus, photos, promo exports)

Drop files in a synced folder, then tell the agent to process it. Works from any device including
your phone, because the syncing is Drive's job, not the agent's.

```
~/uno-mas-inbox/
  menus/      updated menu PDFs / exports
  photos/     new shoot batches
  promos/     sent emails, SMS screenshots, offer cards
  misc/
```

Then: *"process the inbox"* — the agent reads what's new, works out what changed, propagates it,
files assets into Cloudinary with correct naming and tags, and reports back. This can also run on a
schedule.

## If the commands ever stop appearing

```bash
bash ~/projects/uno-mas-brand/scripts/bootstrap-agent.sh
```

Re-links everything. Safe to run repeatedly.
