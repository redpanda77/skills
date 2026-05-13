#!/usr/bin/env bash
set -euo pipefail

cat <<'TEXT'
After this edit:
- run the relevant validation command
- update PLAN.md current state with progress and verification result
- if closing a task, ensure a closure contract exists in PLAN.md
- do not stop unless done-check.sh passes or a real blocker exists
TEXT
