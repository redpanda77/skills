# Claude Code Operating Rules

Completion is determined by validation scripts, not by TodoWrite, summaries, or conversational memory.

## Long-running task protocol

- Use `PLAN.md` as the task map.
- Use `CLOSED_TASKS.md` and `validation-manifest.json` as the closed-work baseline.
- Work from the first incomplete task in PLAN.md.
- Do not treat a completed subtask as final completion.
- Run relevant verification after changes.
- Do not mark a task closed unless its closure contract exists and validation passes.
- If validation fails, continue fixing — do not stop.
- Stop only when `done-check.sh` passes or a real blocker exists.
- Update `PLAN.md` current state before stopping.

## Real blockers (require human input)

- Destructive deletion of production data
- Production deployment or database migration
- Credential or secret handling
- Billing or external-service changes
- Ambiguous product decision that cannot be inferred from the repo
