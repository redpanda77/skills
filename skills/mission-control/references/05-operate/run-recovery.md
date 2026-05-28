# Recovery

Run when `PLAN.md` already exists and you need to resume.

## Steps

1. Read `PLAN.md` — find current task and last verification
2. Read `CLOSED_TASKS.md` — see what's protected
3. Read `validation-manifest.json` — check closed baseline
4. Run `git status` and `git log --oneline -10`
5. Report: current task, last completed, done-check status, any blockers
6. Ask user: resume, check status, upgrade tier, or reset task?

## Resume execution

- Run `./run-agent.sh` if it exists
- Or paste execution prompt into new session

## Rules

- Do not re-do closed tasks
- If done-check already passes: report complete
- If done-check fails: continue from first open task
- If BLOCKED_AGENT markers exist: report them first
- Invoke `write-a-skill` for detailed recovery procedures. Never design them manually.
