# 04 — Test

Verify the harness works before relying on it.

## Files in this folder

- `README.md` — this file
- `common-mistakes.md` — failure modes to watch for

## What to do

- Run `done-check.sh` → must pass on current code
- Run each hook → verify blocking works
- Spawn judge subagent on sample output → verify JSON and scores
- Run closed-task regression → verify no false failures
- Read `common-mistakes.md` → check for anti-patterns

## Next

Read `references/05-operate/README.md`
