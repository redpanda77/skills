
## Long-running task protocol (Mission Control)

Completion is determined by `done-check.sh`, not by TodoWrite, summaries, or conversational memory.

- Use `PLAN.md` as the task map.
- Use `CLOSED_TASKS.md` and `validation-manifest.json` as the closed-work baseline.
- Work from the first incomplete task in PLAN.md.
- Do not mark a task closed unless its closure contract exists.
- If `done-check.sh` fails, continue fixing — do not stop.
- Stop only when `done-check.sh` passes or a real blocker exists.
