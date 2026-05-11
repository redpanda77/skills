#!/usr/bin/env bash
set -euo pipefail

TASK_ID="${1:?Usage: close-task-check.sh TASK_ID [REPO_PATH]}"
REPO="${2:-.}"
CONTROL_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$REPO"

echo "Checking closure for $TASK_ID..."

grep -q "$TASK_ID" PLAN.md || { echo "Task $TASK_ID not found in PLAN.md"; exit 1; }
grep -A40 "$TASK_ID" PLAN.md | grep -qi "Closure Contract" || { echo "No closure contract for $TASK_ID"; exit 1; }
grep -A40 "$TASK_ID" PLAN.md | grep -qi "Evidence" || { echo "No evidence section for $TASK_ID"; exit 1; }

"$CONTROL_DIR/validate-closed-tasks.sh" "$REPO"
"$CONTROL_DIR/validate-global.sh" "$REPO"
"$CONTROL_DIR/validate-no-tampering.sh" "$REPO"

echo "$TASK_ID can be promoted to closed."
