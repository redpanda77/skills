#!/usr/bin/env bash
set -euo pipefail

input="$(cat)"
cmd="$(echo "$input" | jq -r '.tool_input.command // ""')"

if echo "$cmd" | grep -qE 'rm -rf|git push --force|kubectl apply|terraform apply|npm publish|pnpm publish|yarn publish|drop database|TRUNCATE TABLE|docker system prune|git reset --hard'; then
  cat <<JSON
{
  "decision": "block",
  "reason": "Blocked risky command: $cmd. Ask the user explicitly before destructive, deployment, publishing, database, or production-impacting actions."
}
JSON
  exit 0
fi

exit 0
