#!/usr/bin/env bash
set -euo pipefail

input="$(cat)"

paths="$(echo "$input" | jq -r '
  [
    .tool_input.file_path?,
    .tool_input.path?,
    (.tool_input.edits[]?.file_path?)
  ] | map(select(. != null)) | .[]
' 2>/dev/null || true)"

if echo "$paths" | grep -qE '(^|/)(done-check\.sh|run-agent\.sh|judge-rubric\.md|hidden-tests/|\.claude/hooks/|\.claude/settings\.json|validation-manifest\.json|CLOSED_TASKS\.md|validate-.*\.sh|close-task-check\.sh)'; then
  cat <<'JSON'
{
  "decision": "block",
  "reason": "Blocked attempt to edit control or validation files. The worker may not modify validators, hooks, judge rubrics, hidden tests, closed-task registry, or completion policy."
}
JSON
  exit 0
fi

exit 0
