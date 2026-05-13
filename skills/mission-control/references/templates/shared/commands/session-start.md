---
description: Orient at session start — check for handoff, read state, surface current phase and task, suggest next action. Always run this first.
---

Orient for this session. Run before doing anything else.

## Steps

1. **Check for handoff file.**
   Run: `ls handoffs/ 2>/dev/null | sort -r | head -5`
   If any file exists, read the most recent one. Surface the Resume Prompt to the user.
   This takes priority — present the resume prompt before continuing.

2. **Read `.mission-control/state.json`.**
   Note: `project_type`, `scope_locked`, `current_phase`, `current_task`, `blockers`.

3. **Scope check (human-in-the-loop / evaluation projects only).**
   If `scope_locked = false`:
   Stop and tell the user: "Scope is not locked. The foundations interview (T000) must complete before phase work starts. T000 produces `shared/config/scope.md` and `scope.json`."
   Do not proceed with any other task until the user confirms scope approach.

4. **Read PLAN.md.**
   - Find `current_task` section — read its name, acceptance criteria, closure contract.
   - Count open / closed tasks total.
   - Note current phase status: are all prior phase tasks closed?

5. **Print orientation summary:**

   ```
   ── Session Start ─────────────────────────────────
   Project type : [project_type]
   Scope locked : [yes / no]
   Phase        : [current_phase or "n/a"]
   Current task : [current_task] — [task name]
   Progress     : [N closed] / [total tasks]
   Blockers     : [none / list]

   Next action  : [one sentence — what the first task requires]
   ──────────────────────────────────────────────────
   ```

6. **Suggest next action.** One sentence. Do not start work until the user confirms.
