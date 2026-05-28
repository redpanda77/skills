# Three-pass compression framework

Use when an existing CLAUDE.md is over 150 lines or the user reports the agent is ignoring rules.

## Pass 1 — Ruthless deduplication

- Read every rule. Merge any that express the same constraint in different words.
- Delete rules now enforced by a linter, formatter, CI gate, or pre-commit hook.
- Run `/memory` — if Claude has already recorded a rule in auto-memory, remove it from the file.
- If a rule hasn't been violated in a year, ask whether it's still necessary.

## Pass 2 — Convert prose to commands

Prose is context-expensive and interpretation-prone. Replace with commands and file references.

| Before | After |
|--------|-------|
| "Make sure tests pass before merging" | `Run pnpm test and pnpm e2e before marking ready` |
| "Be careful with the auth module" | `See lib/auth/CLAUDE.md. Never modify session.ts without approval.` |
| "Follow our commit conventions" | `Commit format: type(scope): description. Run pnpm commitlint after staging.` |
| "Write good tests" | `Every public function in lib/ has a test in lib/__tests__/` |

## Pass 3 — Separate always-loaded from on-demand

Anything folder-specific moves into a nested `CLAUDE.md` in that folder. Root must be **scannable in 90 seconds**.

## Targets

- Root: under 80 lines
- Package-level: 30–60 lines each
- Compressed root for mature repos: ~14 lines (see `template.md`)

## Validation

After compression, run the before/after test in `testing.md`:

- Same 3 representative prompts against original vs. compressed.
- Equivalent or better adherence with less context = compression worked.
- Missing rules → identify which removed line was load-bearing, restore in compressed form.
