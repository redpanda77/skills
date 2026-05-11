#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

TEST_CMD="${TEST_CMD:-npm test}"

if [ ! -f validation-manifest.json ]; then
  echo "validation-manifest.json missing"
  exit 1
fi

jq -r '.closed_tasks[] | select(.status == "closed") | .tests[]?' validation-manifest.json | while read -r test_file; do
  if [ ! -f "$test_file" ]; then
    echo "Closed-task test missing: $test_file"
    exit 1
  fi
  $TEST_CMD -- "$test_file"
done
