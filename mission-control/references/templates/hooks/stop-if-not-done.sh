#!/usr/bin/env bash
set -euo pipefail

input="$(cat)"

if echo "$input" | jq -e '.stop_hook_active == true' >/dev/null 2>&1; then
  exit 0
fi

if ./done-check.sh >/dev/null 2>&1; then
  exit 0
fi

cat <<'JSON'
{
  "decision": "block",
  "reason": "done-check.sh has not passed. Continue working from PLAN.md. Do not ask whether to continue. Validate current work, preserve closed tasks, fix failures, update PLAN.md current state, and stop only when done-check.sh passes or a real blocker exists."
}
JSON
