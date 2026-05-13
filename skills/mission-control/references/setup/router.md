# Mission Control Setup — Router

This file routes to the correct type-specific setup guide. Ask Q0 first, then read the matching file. Do not proceed without reading the full type-specific guide.

---

## Standing rules (apply to all types)

- **Always local.** Every file goes in the project's `.claude/` directory. Never write to `~/.claude/`.
- **Subagents as files.** Every subagent is a `.md` file in `.claude/agents/` with YAML frontmatter. Never embed prompts in shell scripts.
- **CLAUDE.md via skill.** Always invoke `writing-claude-md`. Never write CLAUDE.md directly.
- **System skill required.** Always invoke `write-a-skill` to create the operating manual skill. This is a hard gate — a checklist must pass before setup can complete. Do not skip it.
- **Sequential workflow.** Each phase gates the next. Use `AskUserQuestion` for every question. Do not batch questions.

---

## Q0 — Project type (ask this first)

Before asking anything else, ask:

"What kind of project is this?"

Options:
- **Autonomous loop** — Claude runs continuously without stopping; a Stop hook blocks early exit; scripts (done-check.sh) decide when work is done; you want it to keep going until finished
- **Human-in-the-loop** — work proceeds phase by phase with you reviewing between phases; agent recommends `/close-task`, you decide when tasks are done; no autonomous run loop
- **Evaluation / analysis** — data, research, or analytical pipeline; human assessment gates; coverage targets; typically no automated test suite (same setup path as human-in-the-loop)

Save as `PROJECT_TYPE`.

---

## Route

| Answer | Read this file |
|--------|---------------|
| Autonomous loop | `references/setup-autonomous.md` |
| Human-in-the-loop | `references/setup-human-in-the-loop.md` |
| Evaluation / analysis | `references/setup-human-in-the-loop.md` |

Read the full type-specific file now, then proceed with its phases. Do not mix phases from different files.

---

## Key differences between types

| | Autonomous loop | Human-in-the-loop / Evaluation |
|-|----------------|-------------------------------|
| Completion authority | `done-check.sh` script | Human runs `/close-task` |
| Task acceptance criteria | Machine-checkable commands (test pass, file exists) | File existence + non-empty + notes filled |
| Closure contract | Evidence scripts verify automatically | Evidence agent surfaces; human confirms |
| Stop hook | Blocking — prevents Claude from stopping | Non-blocking context-warning only |
| run-agent.sh | Required | Not used |
| CLOSED_TASKS.md | Required (regression tracking) | Not used |
| validation-manifest.json | Required (Tier 2+) | Not used |
| Scope lock (T000) | Optional | Strongly recommended for analytical projects |
| Milestone gates | Not applicable | Planned human review points between phases |
| Phase structure | Optional grouping | Required — phase gate rule enforced |

These differences are fundamental. The infrastructure, task format, and closure model are not interchangeable.
