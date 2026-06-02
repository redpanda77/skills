---
name: handoff-templates
description: Handoff document templates for code-task, document-workflow, and lightweight handoff types. Use when writing the middle section of a handoff document.
---

# Handoff Templates

All types share a **common header + footer**. Insert the **type-specific middle** between them.

## Common header (all types)

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

## Code task middle

```
## Plan & Todo State
<!-- Path to the plan file. List checked-off items as DONE and the immediate next item as NEXT.
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

## Document/workflow middle

```
## State Documents
<!-- Every file that holds durable state for this workflow, with its role.
     Format: path — what it contains / when to read it -->

## Document Progress
<!-- Bullet list of docs that exist (✓) vs. still to write (○), each with path.
     For structured workflows note the last completed phase and the next. -->

## What Worked / What Didn't
<!-- Key decisions or dead ends. Only include if non-obvious. -->

## Open Questions
<!-- Unresolved blockers or decisions. -->
```

## Lightweight middle

```
## What Was Done
<!-- Bullet list of completed actions. Reference file paths, not content. -->

## Open Questions
<!-- Unresolved blockers or decisions. -->
```

## Common footer (all types)

```
## Next Steps
<!-- Numbered, immediately actionable items. -->

## Resume Prompt
<!-- A single copy-pasteable message to open a fresh session. Must reference the handoff file path and mention which skills to activate. -->
```
