#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
echo "== validate-hook-config on examples =="
for f in examples/settings-*.json; do
  echo "-- $f"
  python3 scripts/validate-hook-config.py <"$f"
done
echo "== block-dangerous-bash with safe command =="
python3 -c "import json,subprocess; subprocess.run(['scripts/block-dangerous-bash.sh'], input=json.dumps({'tool_input':{'command':'npm test'}}).encode(), check=True)"
echo "== block-dangerous-bash with rm -rf =="
out=$(python3 -c "import json,subprocess; r=subprocess.run(['scripts/block-dangerous-bash.sh'], input=json.dumps({'tool_input':{'command':'rm -rf build'}}).encode(), capture_output=True); print(r.stdout.decode())")
echo "$out" | jq -e '.hookSpecificOutput.permissionDecision == "deny"' >/dev/null
echo "OK: deny path works when jq is available."
echo "All tests passed."
