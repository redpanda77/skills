---
name: handoff
description: Compact the current conversation into a handoff document so a fresh agent can continue this work. Use when context is large, switching tasks or branches, preparing for a new session, or when the user says "handoff", "hand off", "save context", "resume later", or "new session".
argument-hint: What will the next session be used for?
---

Write a handoff document so a fresh agent can continue this work without re-reading the full conversation.

## Step 1 — Determine the target path

1. Check git branch (`git rev-parse --abbrev-ref HEAD`). Use `no-git` if not in a repo.
2. Generate a unique filename: `YYYY-MM-DD-HHMM-<branch>.md` using `date +%Y-%m-%d-%H%M`.
3. Target: `docs/handoffs/<filename>`. Create the directory if needed.
4. If prior handoffs exist, read the most recent (sort by filename) and carry forward still-relevant open questions.

## Step 2 — Detect the handoff type

| Signal | Type |
|--------|------|
| git repo + edited source files + plan/todos | **Code task** |
| requirements/, context files, running skill workflow | **Document/workflow** |
| Neither | **Lightweight** |

## Step 3 — Write the document

Use the templates in `references/templates.md` for the structure. All types share a common header + footer; insert the type-specific middle.

## Rules

- **Point, don't paste** — reference files by path; never dump their contents.
- **Don't duplicate CLAUDE.md** — only note deviations.
- **No orphan sections** — omit any section that would be empty.
- **Aim for ~600 tokens** — orient the next agent, don't re-explain the project.
- **Unique files only** — never overwrite an existing handoff.
- **Reference the previous handoff** — carry forward still-relevant open questions.

## After writing

Print the full file path so the user can open a fresh session with it.

Then ask: "Want me to set up a `/handoff` slash command or a Stop hook so this runs automatically? (yes / no)"
