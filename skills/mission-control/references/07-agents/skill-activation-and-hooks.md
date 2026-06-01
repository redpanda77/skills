# Skill Activation and Hooks

**Critical clarity: Hooks only activate when the skill is loaded.** The skill's frontmatter declares the hooks. They are not global unless the skill is active.

## How skill activation works

The chain is:

```
1. User invokes a skill (e.g., `/curriculum`)
2. The skill's frontmatter is loaded
3. Hooks declared in the skill's frontmatter are activated
4. The skill loads any sub-skills referenced in its body
5. The skill runs its router or setup commands
6. The skill delegates to the exact named subagent
7. The subagent loads its own frontmatter (including `skills:`)
8. Hooks remain active for the duration of the skill session
```

## Skill frontmatter with hooks

```yaml
---
name: curriculum
description: Entry shim for /curriculum commands. Loads curriculum-generator, runs the router, and executes one bounded legal action.
argument-hint: continue | status | level N | audit | repair
hooks:
  PreToolUse:
    - matcher: Write|Edit|MultiEdit|NotebookEdit|Bash|Agent|Task|TaskCreate|TaskUpdate|TaskList|TaskGet
      hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_worker_boundary_guard.py"
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_task_sync_guard.py"
  PostToolUse:
    - matcher: Bash|Agent|Task|TaskCreate|TaskUpdate|TaskList|TaskGet
      hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_task_sync_guard.py"
    - matcher: Write|Edit|MultiEdit|NotebookEdit
      hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_post_tool_validate.py"
  Stop:
    - hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_stop_guard.py"
  SubagentStop:
    - hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_subagent_stop_verify.py"
  TaskCompleted:
    - hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_subagent_stop_verify.py"
  PreCompact:
    - matcher: manual|auto
      hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_pre_compact_guard.py"
  PostCompact:
    - hooks:
        - type: command
          command: "$CLAUDE_PROJECT_DIR/.claude/hooks/curriculum_post_compact_audit.py"
          async: true
---
```

### Hook events

| Event | When it fires | Typical hook |
|-------|---------------|--------------|
| `PreToolUse` | Before any tool call | Worker boundary guard, task sync guard |
| `PostToolUse` | After any tool call | Tool output validation, task sync |
| `Stop` | When user tries to exit | Stop guard, done-check verification |
| `SubagentStop` | When a subagent stops | Subagent receipt verification |
| `TaskCompleted` | When a task completes | Receipt verification |
| `PreCompact` | Before context compaction | Pre-compact guard |
| `PostCompact` | After context compaction | Post-compact audit |

### Hook scoping

Hooks are scoped in two ways:

1. **Per-skill** — declared in the skill's frontmatter, active only when the skill is loaded
2. **Cross-cutting** — declared in `.claude/settings.json`, active for all sessions

### Rules

- Per-skill hooks override cross-cutting hooks for the same event
- A hook missing from the skill frontmatter is not active during that skill session
- The `matcher` field filters which tool calls trigger the hook
- `async: true` means the hook runs in the background and does not block
- Hooks are commands (scripts), not inline logic

## How agents load skills

An agent loads skills via the `skills:` field in its frontmatter:

```yaml
---
name: curriculum-lesson-repair-worker
category: repair_worker
description: Use when the router detects a lesson judge failed...
tools: Read, Write
skills:
  - curriculum-generator
---
```

The `curriculum-generator` skill is loaded into the agent's context before the agent reads anything else. This gives the agent domain knowledge without duplicating it in the agent body.

### Rules

- The agent's `skills` field lists only the domain skills it needs
- The system skill is loaded automatically by the harness
- The parent skill (e.g., `curriculum`) is not the same as the agent's skill (e.g., `curriculum-generator`)
- Do not put harness mechanics in domain skills — put them in the system skill

## The curriculum example

The `curriculum` skill is an entry shim:

1. **User types `/curriculum`** — the `curriculum` skill is loaded
2. **Hooks activate** — `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`, etc.
3. **Skill loads sub-skill** — `curriculum-generator` is loaded for deeper rules
4. **Skill runs router** — `python3 curriculum_scripts/runtime/curriculum_start.py --json`
5. **Router produces a card** — with `status`, `run`, `requires_worker`, `target`, `then`
6. **Skill delegates** — calls the exact named subagent with the exact handoff prompt
7. **Subagent loads its skill** — `curriculum-generator` via `skills:` frontmatter
8. **Hooks remain active** — throughout the subagent's execution
9. **Subagent returns receipt** — `WORKER_RECEIPT` JSON
10. **Hook verifies receipt** — `curriculum_subagent_stop_verify.py` checks the receipt

### Rules

- The parent does not pre-read worker context packs — the worker reads them
- The parent does not run validators — the parent runs the router, which decides whether to validate
- The parent does not construct delegation by reading worker prompts — it uses the router card
- The skill is the operator, not the worker

## Rules

- Hooks are part of the control system, not obstacles to bypass
- Hook blocks are protocol feedback — fix the route, prompt, or pack, not the hook
- Hook changes are control-layer maintenance and require Escape Protocol
- Hooks are not global unless declared in `settings.json` — they are per-skill
- The agent's `skills` frontmatter field activates the skill; the skill's frontmatter activates the hooks
