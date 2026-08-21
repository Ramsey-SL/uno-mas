#!/usr/bin/env bash
# Install the Uno Más agent (skills + steward subagent) for the current user.
# Idempotent — safe to re-run. Repo stays the source of truth; ~/.claude gets symlinks.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS=(unomas-update unomas-find unomas-design)

echo "Uno Más agent bootstrap"
echo "  repo: $REPO"

mkdir -p "$HOME/.claude/skills" "$HOME/.claude/agents"

for s in "${SKILLS[@]}"; do
  src="$REPO/.claude/skills/$s"
  [ -d "$src" ] || { echo "  MISSING in repo: $src" >&2; exit 1; }
  ln -sfn "$src" "$HOME/.claude/skills/$s"
  echo "  linked skill  /$s"
done

agent="$REPO/.claude/agents/unomas-steward.md"
[ -f "$agent" ] || { echo "  MISSING in repo: $agent" >&2; exit 1; }
ln -sfn "$agent" "$HOME/.claude/agents/unomas-steward.md"
echo "  linked agent  unomas-steward"

echo
echo "Verifying:"
for s in "${SKILLS[@]}"; do
  printf '  %-16s ' "$s"
  grep -m1 '^name:' "$HOME/.claude/skills/$s/SKILL.md" || { echo "BROKEN" >&2; exit 1; }
done
printf '  %-16s ' "unomas-steward"
grep -m1 '^name:' "$HOME/.claude/agents/unomas-steward.md"

cat <<'EOF'

Done. Start a new Claude Code session and the commands are available:
  /unomas-update <what changed>
  /unomas-find <what you need>
  /unomas-design <what you need>

Still needed on a fresh machine (credentials, not agent files):
  - Claude Code signed in
  - claude.ai connectors authorized: Cloudinary, Google Drive, Canva, Klaviyo,
    Supabase, Lovable, Meta Ads
  - SSH access to github.com:Ramsey-SL/uno-mas
EOF
