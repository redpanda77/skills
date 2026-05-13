#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

if grep -rq "BLOCKED_AGENT" PLAN.md CLOSED_TASKS.md src tests 2>/dev/null; then
  echo "BLOCKED_AGENT marker found."
  exit 1
fi

if grep -qi "^## Blockers" PLAN.md && ! grep -qi "None" PLAN.md; then
  echo "PLAN.md contains blockers."
  exit 1
fi
