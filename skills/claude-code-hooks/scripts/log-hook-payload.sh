#!/usr/bin/env bash
# Append JSON hook stdin to a log file (safe default path). Override with CLAUDE_CODE_HOOK_LOG.
set -euo pipefail
LOG="${CLAUDE_CODE_HOOK_LOG:-${TMPDIR:-/tmp}/claude-code-hooks-payload.log}"
{
  echo "----- $(date -u +"%Y-%m-%dT%H:%M:%SZ") -----"
  cat
  echo
} >>"$LOG"
exit 0
