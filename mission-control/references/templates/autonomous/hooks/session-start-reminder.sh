#!/usr/bin/env bash
set -euo pipefail

if [ -f PLAN.md ]; then
  cat <<'TEXT'
Long-running task protocol (Mission Control):
- PLAN.md is the task map.
- CLOSED_TASKS.md and validation-manifest.json are the closed-work baseline.
- done-check.sh is the completion authority.
- Do not rely on TodoWrite or conversation memory for completion.
- Continue from the first incomplete task in PLAN.md.
- Do not mark a task closed unless its closure contract exists and validation passes.
- Stop only when done-check.sh passes or a real blocker exists.
TEXT
fi
