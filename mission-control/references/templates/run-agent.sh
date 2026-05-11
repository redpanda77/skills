#!/usr/bin/env bash
set -euo pipefail

SESSION_NAME="mission-control"
MAX_ROUNDS=50

PROMPT='
Continue the current task.

Use PLAN.md as the task map.
Use CLOSED_TASKS.md and validation-manifest.json as the closed-work baseline.
Use ./done-check.sh as the completion authority.

Rules:
- Do not ask whether to continue.
- Do not stop after a subtask.
- Work from the first incomplete task in PLAN.md.
- Validate the current task after implementing it.
- Preserve all previously closed tasks.
- Do not mark a task closed unless it has a closure contract.
- If done-check.sh fails, continue fixing.
- Update PLAN.md current state before stopping.
- Stop only when done-check.sh passes or a real blocker exists.
'

for i in $(seq 1 "$MAX_ROUNDS"); do
  echo "=== Claude round $i / $MAX_ROUNDS ==="

  if ./done-check.sh >/dev/null 2>&1; then
    echo "done-check passed. Complete."
    exit 0
  fi

  claude -p \
    --permission-mode bypassPermissions \
    --resume "$SESSION_NAME" \
    "$PROMPT" || true

  if ./done-check.sh >/dev/null 2>&1; then
    echo "done-check passed. Complete."
    exit 0
  fi
done

echo "Max rounds ($MAX_ROUNDS) reached without completion."
exit 1
