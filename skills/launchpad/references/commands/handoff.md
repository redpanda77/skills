Read `.plan/active.md` and `.plan/features/[feature]/tasks.md`.

Write a handoff to `.plan/features/[feature]/handoffs/YYYY-MM-DD.md` (today's date). If the file already exists, read it first and update rather than overwrite.

Structure:
```
---
date: YYYY-MM-DD
feature: [name]
task: [TASK-NNN]
status: in-progress
---

## What was done
## Decisions made (with rationale — the why, not the what)
## Open questions
## Next task
## Resume prompt
```

Rules:
- Keep it under 500 tokens
- Point to files by path — don't paste content
- Don't duplicate anything already in CONTEXT.md or CLAUDE.md
- The Resume Prompt must be one copy-pasteable sentence to start the next session

After writing, print the file path.
