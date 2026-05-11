# Validation Design

This page helps you design the validation stack for your specific project.

## The stack model

Done-check is not one script that does everything. It's a top-level authority that delegates to sub-validators:

```
done-check.sh
  ├── validate-no-blockers.sh    checks: no open tasks, no BLOCKED_AGENT markers
  ├── validate-global.sh         checks: typecheck + lint + full test suite
  ├── validate-closed-tasks.sh   checks: closed-task regression tests still pass (Tier 2+)
  └── validate-no-tampering.sh   checks: no test weakening or config changes (Tier 2+)
```

For Tier 1, `done-check.sh` can inline these checks directly without sub-scripts. For Tier 2+, separate scripts allow them to be called independently and make the layout clearer.

## What belongs in each validator

### done-check.sh
Top-level only. Calls other scripts. Its job is orchestration, not checking.

```bash
./validate-no-blockers.sh
./validate-closed-tasks.sh   # Tier 2+
./validate-global.sh
./validate-no-tampering.sh   # Tier 2+
echo "done-check passed"
```

If Tier 1, inline the checks directly:
```bash
# no open tasks
grep -q "Status: open" PLAN.md && exit 1
# tests pass
npm test
echo "done-check passed"
```

### validate-global.sh
All the deterministic checks that must pass for the project to be in a good state:
- Typecheck
- Lint
- Test suite
- No agent marker strings

Customize for your stack:

| Stack | Typecheck | Lint | Test |
|-------|-----------|------|------|
| TypeScript/Node | `tsc --noEmit` | `eslint .` | `npm test` |
| Python | `mypy src/` | `ruff check .` | `pytest` |
| Go | `go build ./...` | `golint ./...` | `go test ./...` |
| Ruby | `steep check` | `rubocop` | `bundle exec rspec` |

### validate-closed-tasks.sh
Reads `validation-manifest.json` and re-runs the registered test files for each closed task.

This is how you prevent later tasks from silently breaking earlier ones. Claude closes T001 and registers its tests. When working on T004, if a change breaks T001's tests, `validate-closed-tasks.sh` catches it before Claude can close T004.

Only useful if you're registering tests in `validation-manifest.json`. If Claude won't be doing that (e.g. no test suite exists yet), skip this or leave it as a no-op.

### validate-no-tampering.sh
Detects if Claude has modified control files or weakened tests. Checks:
- `done-check.sh` / `run-agent.sh` modified? Block.
- Test files have `.skip` / `xit(` / `xdescribe(` patterns? Block.
- `package.json` or test config changed? Flag for human review.

This matters most when Claude is writing tests as part of the task — it could theoretically write weak tests that pass trivially. The tamper check is a second defense layer.

### validate-no-blockers.sh
Cheap to run, run it first:
- `BLOCKED_AGENT` marker in any file? Block.
- Open tasks in PLAN.md? Block.
- Unchecked `- [ ]` items in global DoD? Block.

## Design questions to answer before writing done-check.sh

**1. What is the minimum bar for "done"?**
The answer should be an executable command, not a description. "Tests pass" → `npm test`. "Type-safe" → `tsc --noEmit`. Never "Claude reviewed it" — that's not checkable.

**2. What breaks your project in ways tests won't catch?**
If you have a separate typecheck step, missing types might not fail tests. If you have lint rules that encode architecture decisions, lint must be in the check. Add anything that has caught real bugs in the past.

**3. Are you building tests as part of this task?**
If yes, you can't rely on pre-existing tests being complete. The tamper-detection check becomes more important, and you should probably use Tier 2. Consider what "regression done" means: if Claude is writing tests for new code, the closure contract needs to specify what the tests must cover, not just that tests exist.

**4. How long does your full validation suite take?**
If it takes > 5 minutes, the Stop hook will add visible latency every time Claude tries to stop. Consider a fast-check mode: a subset of tests that runs in < 30 seconds for the hook, with full tests run only before task closure.

Fast check in `stop-if-not-done.sh`:
```bash
# Quick check (runs fast, approximate)
if ./done-check-fast.sh >/dev/null 2>&1; then
  exit 0
fi
```

Full check in `close-task-check.sh`:
```bash
# Thorough check (runs slow, exact)
./done-check.sh
```

**5. Do you have integration or e2e tests?**
If yes, decide: are they part of done-check? E2e tests can be slow and flaky. If they're unreliable, don't gate done-check on them — they'll cause infinite retry loops. Mention them in the PLAN.md Global DoD as manual steps instead.

## Concrete done-check.sh examples

### Node/TypeScript project, Tier 1
```bash
#!/usr/bin/env bash
set -euo pipefail

grep -q "Status: open" PLAN.md 2>/dev/null && { echo "Open tasks remain."; exit 1; }
grep -rq "BLOCKED_AGENT" . 2>/dev/null && { echo "Blocker marker found."; exit 1; }

npm run typecheck
npm run lint
npm test

echo "done-check passed"
```

### Python project, Tier 2
```bash
#!/usr/bin/env bash
set -euo pipefail

CONTROL="$(dirname "$0")"
REPO="${1:-.}"

"$CONTROL/validate-no-blockers.sh" "$REPO"
"$CONTROL/validate-closed-tasks.sh" "$REPO"
"$CONTROL/validate-global.sh" "$REPO"
"$CONTROL/validate-no-tampering.sh" "$REPO"

echo "done-check passed"
```

With `validate-global.sh` containing:
```bash
mypy src/
ruff check .
pytest -x --tb=short
```

### Minimal shell-only project
```bash
#!/usr/bin/env bash
set -euo pipefail

grep -q "Status: open" PLAN.md 2>/dev/null && exit 1
bash -n src/*.sh        # syntax check all shell files
./tests/run-tests.sh    # custom test runner

echo "done-check passed"
```

## Connecting done-check to the Stop hook

The Stop hook calls done-check.sh. If it exits non-zero, Claude is blocked from stopping and receives the error output as its next input.

```
Claude tries to stop
  → Stop hook runs done-check.sh
  → done-check.sh runs validate-*.sh
  → if any validator fails, done-check exits 1
  → Stop hook returns {"decision": "block", "reason": "done-check.sh failed: [output]"}
  → Claude reads the failure reason and continues
```

This means your validators must produce clear, actionable error messages. "Tests failed" is not enough. "3 tests failed in tests/parser.test.ts: expected null, got undefined" tells Claude what to fix.

Make validators verbose on failure, silent on success.
