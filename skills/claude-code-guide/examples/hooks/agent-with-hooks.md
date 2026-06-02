# Example: subagent with hooks

Subagents use the **same** `hooks:` structure in their definition file. **`Stop` in subagent context maps to `SubagentStop`** for hook purposes.

```yaml
---
name: verifier
description: Example subagent — illustrative hooks block only.
hooks:
  SubagentStop:
    - hooks:
        - type: prompt
          prompt: "Verify completion criteria before stopping. Context: $ARGUMENTS"
          timeout: 30
---
```

Prefer **`SubagentStop`** explicitly when authoring new configs so matchers and mental models stay aligned with the event that actually fires.

Official note: [Hooks in skills and agents](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents).
