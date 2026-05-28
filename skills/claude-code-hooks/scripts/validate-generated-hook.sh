#!/usr/bin/env bash
# Validate hook *settings* JSON: either stdin is a full settings doc with "hooks",
# or stdin is a PreToolUse/PostToolUse payload pointing at a JSON file that has "hooks".
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT=$(cat)
if command -v jq >/dev/null 2>&1; then
  TARGET=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null || true)
  if [[ -n "${TARGET:-}" && -f "$TARGET" ]] && jq -e '.hooks' "$TARGET" >/dev/null 2>&1; then
    python3 "$ROOT/scripts/validate-hook-config.py" <"$TARGET"
    exit $?
  fi
fi
echo "$INPUT" | python3 "$ROOT/scripts/validate-hook-config.py"
