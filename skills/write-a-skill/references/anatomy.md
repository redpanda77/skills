# Skill Anatomy

A Claude Code skill is a folder containing a `SKILL.md` file and optional supporting files. The folder name usually becomes the slash command (e.g., `.claude/skills/deploy-staging/` becomes `/deploy-staging`).

---

## 1. Skill Directory

```
~/.claude/skills/<skill-name>/          # Global (user-wide)
.claude/skills/<skill-name>/            # Project-local
```

- Folder name must be **kebab-case** (`my-skill`, not `mySkill` or `my_skill`).
- Do **not** put a `README.md` inside the skill folder. The `SKILL.md` is the entry point.

## 2. SKILL.md

Every skill requires a `SKILL.md` at the root of the folder. It has two parts:

1. **YAML frontmatter** between `---` markers
2. **Markdown instructions** below the frontmatter

### Minimal Example

```yaml
---
name: my-skill
description: What this skill does and when to use it
---

## Instructions
Do the task this way:
1. ...
2. ...
3. ...
```

## 3. Frontmatter

All fields are optional, but `description` is strongly recommended because Claude uses it to decide when to load the skill.

### Common Fields

```yaml
---
name: my-skill
description: What this skill does and when to use it
when_to_use: Extra trigger guidance or example requests
argument-hint: "[issue-number] [branch]"
arguments: [issue, branch]
disable-model-invocation: true
user-invocable: true
allowed-tools: Read Grep Bash(git *)
disallowed-tools: AskUserQuestion
model: inherit
effort: high
context: fork
agent: Explore
paths: ["src/**/*.ts", "packages/api/**"]
shell: bash
---
```

### Key Field Reference

| Field | Purpose |
|-------|---------|
| `name` | Display label (kebab-case). Usually the folder name drives the command. |
| `description` | What it does + when to use it + key capabilities. Under 1024 chars. |
| `disable-model-invocation: true` | Prevents auto-trigger. Use for side-effect workflows (deploy, commit). |
| `user-invocable: false` | Hides from slash-command menu. Use for background reference knowledge. |
| `allowed-tools` | Pre-approves tools while the skill is active. |
| `context: fork` | Runs in an isolated subagent instead of inline. |
| `agent: Explore` | Uses a specific built-in agent when forked. |

## 4. Markdown Body / Instructions

The actual behavior Claude follows when the skill is active. Keep it concise because the content stays in context across turns.

- **Reference content:** API conventions, style guides, domain rules.
- **Task content:** Deploy process, commit workflow, review checklist, code-generation recipe.

### Example Task Body

```markdown
Fix GitHub issue $issue.

Process:
1. Read the issue description.
2. Find the affected code.
3. Implement the fix.
4. Add or update tests.
5. Summarize the changes.
```

## 5. Arguments and Substitutions

Skills can accept arguments passed via the slash command.

| Syntax | Meaning |
|--------|---------|
| `$ARGUMENTS` | The entire argument string |
| `$ARGUMENTS[0]` or `$0` | First positional argument |
| `$issue` | Named argument (declare `arguments: [issue]`) |

### Example

```yaml
---
name: fix-issue
description: Fix a GitHub issue by number
arguments: [issue]
argument-hint: "[issue-number]"
disable-model-invocation: true
---

Fix GitHub issue $issue.
```

Invoked as: `/fix-issue 123`

### Environment Variables

Claude Code also supports:
- `${CLAUDE_SESSION_ID}`
- `${CLAUDE_EFFORT}`
- `${CLAUDE_SKILL_DIR}`

## 6. Dynamic Context Injection

Run a shell command before Claude sees the skill and inject its output inline.

```markdown
## Current changes
!`git diff HEAD`

## Instructions
Summarize the diff and flag risks.
```

The `!` prefix tells Claude Code to execute the command and replace the placeholder with the output.

## 7. Supporting Files

A skill directory can include extra files. `SKILL.md` should act as the overview/navigation file; larger docs and helper scripts live beside it.

### Recommended Structure

```
my-skill/
├── SKILL.md              # Required entry point
├── reference.md            # Optional deep-dive docs
├── examples.md             # Optional usage examples
└── scripts/
    └── helper.py           # Optional deterministic helpers
```

### Design Guidelines

- Keep `SKILL.md` under ~500 lines.
- Link to support files when the topic is deep or rarely needed.
- Use `references/` for domain docs, schemas, and API guides.
- Use `scripts/` for deterministic validation or generation helpers.

---

## Summary

A solid skill has:
1. A clear, kebab-case folder name
2. A short `SKILL.md` with precise frontmatter
3. Concise, actionable instructions
4. Optional arguments for parameterized workflows
5. Optional tool permissions for smoother execution
6. Optional support files linked from the main doc
