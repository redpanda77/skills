#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

if git diff --name-only | grep -E '(^|/)(done-check\.sh|run-agent\.sh|\.claude/|judge-rubric|hidden-tests/)'; then
  echo "Protected control files were modified."
  exit 1
fi

if git diff -- tests | grep -E '\.skip|xit\(|xdescribe\(|expect\(true\)|assert\(true\)|TODO_AGENT|PLACEHOLDER_AGENT'; then
  echo "Suspicious test weakening detected."
  exit 1
fi

if git diff --name-only | grep -E '(package\.json|jest\.config|vitest\.config|playwright\.config|eslint|tsconfig)'; then
  echo "Build/test config changed. Requires human review."
  exit 1
fi
