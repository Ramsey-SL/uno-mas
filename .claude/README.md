# The agent no longer lives here

**Moved 2026-08-25** to its own repo: **`uno-mas-marketing-agent`** (`~/projects/uno-mas-marketing-agent`).

This repo is now **content only** — the ecosystem registry, brand docs, campaigns, changelog.
The agent's *behavior* — skills, the session-start protocol, session logs, scripts — lives in the
agent repo so it's portable across platforms and devices.

**Why there is only one copy:** two copies of the skills would drift, which is the exact failure
this whole system exists to prevent. `~/.claude/skills/*` symlinks point at the **agent repo**.

## Set up / repair

```bash
bash ~/projects/uno-mas-marketing-agent/scripts/install.sh
```

Start every session with **`/unomas-start`**.
