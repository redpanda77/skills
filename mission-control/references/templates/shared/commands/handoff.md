---
description: Compact the current conversation into a handoff document so a fresh agent can continue this work. Use when context is large, switching tasks or branches, preparing for a new session, or when the user says "handoff", "hand off", "save context", "resume later", or "new session".
argument-hint: What will the next session be used for?
---

Write a handoff document so a fresh agent can continue this work without re-reading the full conversation.

## Step 1 — Determine the target path

1. Check if the working directory is a git repo (`git rev-parse --abbrev-ref HEAD 2>/dev/null`).
   - If yes: target is `handoffs/<branch>.md` in the project root. Create the `handoffs/` dir if needed.
   - If no git repo: use `mktemp -t handoff-XXXXXX.md`.
2. If the file already exists, **read it first** before overwriting.

## Step 2 — Detect the handoff type

Scan the current session context and check for:

| Signal | Handoff type |
|--------|-------------|
| git repo + edited source files + plan/todos | **Code task** |
| requirements/, context files, running skill workflow (e.g. grill-me, launchpad) | **Document/workflow** |
| Neither of the above | **Lightweight** |

## Step 3 — Write the document

All types share a **common header + footer**. Insert the **type-specific middle** between them.

### Common header (all types)
```
---
date: <ISO date>
branch: <branch name or "no-git">
type: <code-task | document-workflow | lightweight>
status: in-progress
---

## Goal
<!-- One sentence: what are we trying to accomplish? -->

## Active Skills
<!-- Skills invoked this session (name + one-line purpose) AND skills the next session should activate.
     Format: `skill-name` — what it does / why it's relevant -->
```

### Type-specific middle

**Code task:**
```
## Plan & Todo State
<!-- Path to the plan file (e.g. PLAN.md, .plan/). List checked-off items as DONE and the immediate next item as NEXT.
     How to re-check state: `cat <plan-path>` or read the TodoWrite task list. -->

## Active Files
<!-- Files touched this session. Two sub-lists:
     - Already edited: path — what changed
     - Next to edit: path — what needs to change and why -->

## What Worked / What Didn't
<!-- Key decisions or dead ends. Only include if non-obvious. -->

## Open Questions
<!-- Unresolved blockers or decisions. -->
```

**Document/workflow:**
```
## State Documents
<!-- Every file that holds durable state for this workflow, with its role.
     Format: path — what it contains / when to read it
     Examples: requirements/feature/context.md, memory/MEMORY.md, .plan/roadmap.md -->

## Document Progress
<!-- Bullet list of docs that exist (✓) vs. still to write (○), each with path.
     For structured workflows (grill-me, launchpad, etc.) note the last completed phase and the next. -->

## What Worked / What Didn't
<!-- Key decisions or dead ends. Only include if non-obvious. -->

## Open Questions
<!-- Unresolved blockers or decisions. -->
```

**Lightweight:**
```
## What Was Done
<!-- Bullet list of completed actions. Reference file paths, not content. -->

## Open Questions
<!-- Unresolved blockers or decisions. -->
```

### Common footer (all types)
```
## Next Steps
<!-- Numbered, immediately actionable items. If the user passed arguments, lead with steps for that focus. -->

## Resume Prompt
<!-- A single copy-pasteable message to open a fresh session. Must reference the handoff file path and mention which skills to activate. -->
```

## Rules

- **Point, don't paste** — reference files by path; never dump their contents.
- **Don't duplicate CLAUDE.md** — project context is already loaded; only note deviations.
- **No orphan sections** — omit any section that would be empty.
- **Aim for ~600 tokens** — orient the next agent, don't re-explain the project.
- **If the user passed arguments**, treat them as the next-session focus: lead Next Steps with those items and tailor the Resume Prompt.

## After writing

Print the full file path so the user can open a fresh session with it.
