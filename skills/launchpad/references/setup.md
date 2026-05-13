# Launchpad Setup

Run this once per project. Creates the `.plan/` system, installs slash commands, and wires up CLAUDE.md.

## Step 1 — Create folder structure

```
mkdir -p .plan/features/_archive
```

Create `.plan/active.md` using the schema in `formats/active.md` (leave feature blank for now).

## Step 2 — Install slash commands

Copy each file from `~/.claude/skills/launchpad/references/commands/` into `.claude/commands/` (create the folder if it doesn't exist):

- `start.md`
- `write-a-prd.md`
- `prd-to-tasks.md`
- `task-done.md`
- `handoff.md`
- `switch-feature.md`
- `complete-feature.md`

If any file already exists in `.claude/commands/`, show a diff and ask via `AskUserQuestion` whether to overwrite, skip, or merge.

## Step 3 — Wire up CLAUDE.md

Check for `CLAUDE.md` in the project root.

**If it doesn't exist:** invoke the `writing-claude-md` skill to create one, then return here and continue.

**If it exists:** read it, then append the following block (do not duplicate if already present):

```markdown
## Planning System

All project planning lives in `.plan/`.

At the start of every session:
1. Read `.plan/CONTEXT.md` (if it exists)
2. Read `.plan/active.md` to find the active feature
3. Read `.plan/features/[active-feature]/prd.md`
4. Read `.plan/features/[active-feature]/tasks.md`
5. Confirm the current task before writing any code

Never start coding without completing steps 1–5.
```

## Step 4 — Domain vocabulary

Ask via `AskUserQuestion`:
> "Do you want to define the project's domain vocabulary now? This creates `.plan/CONTEXT.md` using `/grill-with-docs`."
> Options: "Yes, run it now" | "I'll do it later"

If yes, invoke `grill-with-docs`. The output goes to `.plan/CONTEXT.md` (not the project root).

## Step 5 — Orientation

Print the orientation summary from `workflow.md` so the user knows how to use the system from here.

Tell the user: "You're set up. Start your first feature with `/write-a-prd`."
