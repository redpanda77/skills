#!/usr/bin/env bash
# Example PreToolUse guard — deny obvious destructive rm -rf patterns.
set -euo pipefail
if ! command -v jq >/dev/null 2>&1; then
  echo "jq is required for this example hook" >&2
  exit 2
fi
COMMAND=$(jq -r '.tool_input.command // empty')
if echo "$COMMAND" | grep -qE 'rm[[:space:]]+-rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive rm -rf blocked by example hook"
    }
  }'
  exit 0
fi
exit 0
