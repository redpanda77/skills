#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

# Adapt TEST_CMD, TYPECHECK_CMD, LINT_CMD to your project.
TEST_CMD="${TEST_CMD:-npm test}"
TYPECHECK_CMD="${TYPECHECK_CMD:-}"
LINT_CMD="${LINT_CMD:-}"

if [ -n "$TYPECHECK_CMD" ]; then
  $TYPECHECK_CMD
fi

if [ -n "$LINT_CMD" ]; then
  $LINT_CMD
fi

$TEST_CMD

if grep -rq "TODO_AGENT\|FIXME_AGENT\|BLOCKED_AGENT\|PLACEHOLDER_AGENT" src tests 2>/dev/null; then
  echo "Agent marker found in source."
  exit 1
fi
