#!/usr/bin/env bash
set -euo pipefail

# done-check.sh — completion authority
# Fill in TEST_CMD and optional TYPECHECK_CMD / LINT_CMD for your project.
# For Tier 2+, uncomment the sub-validator calls and write those scripts.

TEST_CMD="${TEST_CMD:-npm test}"
TYPECHECK_CMD="${TYPECHECK_CMD:-}"
LINT_CMD="${LINT_CMD:-}"

# 1. No open tasks (if REQUIRE_ALL_TASKS_CLOSED=true)
if grep -q "Status: open" PLAN.md 2>/dev/null; then
  echo "PLAN.md still has open tasks."
  exit 1
fi

# 2. No unchecked global DoD items
if grep -q "^- \[ \]" PLAN.md 2>/dev/null; then
  echo "PLAN.md has unchecked Definition of Done items."
  exit 1
fi

# 3. No blocker markers
if grep -rq "BLOCKED_AGENT" . --include="*.md" --include="*.ts" --include="*.py" --include="*.go" --include="*.rb" --include="*.js" 2>/dev/null; then
  echo "BLOCKED_AGENT marker found in source."
  exit 1
fi

# 4. Typecheck (uncomment if applicable)
# if [ -n "$TYPECHECK_CMD" ]; then $TYPECHECK_CMD; fi

# 5. Lint (uncomment if applicable)
# if [ -n "$LINT_CMD" ]; then $LINT_CMD; fi

# 6. Tests must pass
$TEST_CMD

# --- Tier 2+ additions (uncomment and adjust paths) ---
# CONTROL="$(cd "$(dirname "$0")" && pwd)"
# "$CONTROL/validate-closed-tasks.sh" .
# "$CONTROL/validate-no-tampering.sh" .

echo "done-check passed"
