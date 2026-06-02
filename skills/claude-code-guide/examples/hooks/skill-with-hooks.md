# Example: skill with skill-scoped hooks (YAML frontmatter)

Use this shape in `SKILL.md` when a **hands-on** skill should validate or log only while active. Narrow matchers; avoid `"*"` on `PreToolUse` for reference skills.

```yaml
---
name: secure-operations
description: Example only — perform operations with Bash guardrails while this skill is active.
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          if: "Bash(rm *)"
          command: "./scripts/block-dangerous-bash.sh"
          args: []
---
```

Paths like `./scripts/...` resolve relative to the skill or project layout where Claude installs the skill; prefer `${CLAUDE_PROJECT_DIR}/.claude/hooks/...` for project-local scripts.

See `references/hooks-in-skills-and-agents.md` and the official [Hooks in skills and agents](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents) section.
