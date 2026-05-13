#!/usr/bin/env bash
# PostToolUse helper: run formatter on edited file when jq is available.
set -euo pipefail
if ! command -v jq >/dev/null 2>&1; then
  exit 0
fi
FILE=$(jq -r '.tool_input.file_path // empty')
if [[ -z "$FILE" || ! -f "$FILE" ]]; then
  exit 0
fi
if command -v npx >/dev/null 2>&1 && [[ "$FILE" =~ \.(js|jsx|ts|tsx|json|md|yaml|yml)$ ]]; then
  npx --yes prettier --write "$FILE" 2>/dev/null || true
fi
exit 0
