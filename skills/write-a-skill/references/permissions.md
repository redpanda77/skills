---
name: skill-permissions
description: Reference for skill permission boundaries, allowed-tools, safety rules, and side effects. Use when restricting what a skill can do.
---

# Permissions & Safety

Control what a skill is allowed to touch and modify.

## Allowed Tools

Restrict the tools available to a skill to the minimum necessary.

```yaml
---
name: code-reviewer
description: Reviews code for bugs. Use when user asks for "code review" or "check this function".
allowed-tools:
  - Read
  - Bash
---
```

**Principle:** Only allow tools the skill actually needs. If it only reads code, don't allow `Edit` or `Write`.

## Tool Categories

| Category | Tools | Typical Use |
|----------|-------|-------------|
| Read-only | `Read`, `WebFetch` | Analysis, review, research |
| Write-only | `Write`, `Edit` | Code generation, documentation |
| Shell | `Bash` | Running tests, scripts, git commands |
| Network | `WebFetch`, `WebSearch` | External data lookup |
| Agent | `Agent`, `TaskCreate` | Delegation to subagents |
| File ops | `Read`, `Write`, `Edit`, `Bash` | Full file system access |

## Permission Boundaries

Define what the skill is allowed to touch:

- **Read scope:** Which directories or files can it read?
- **Write scope:** Which directories or files can it modify?
- **Shell scope:** Which commands can it run? With what arguments?
- **Network scope:** Which domains or APIs can it call?

## Safety Rules

### Side Effects

Document what side effects the skill produces:
- Does it write files?
- Does it run shell commands?
- Does it make API calls?
- Does it modify git state?

**Example:**
```markdown
## Side Effects

This skill:
- Reads source files in `src/`
- Runs `pnpm test` (read-only of test results)
- Does NOT modify any files
- Does NOT commit changes
```

### Irreversible Operations

If the skill can do something irreversible (delete, drop, push, deploy), it must:
1. Be explicit in the description
2. Use `disable-model-invocation` so it only runs on explicit user request
3. Include a confirmation step in the instructions
4. Document the rollback procedure

### Secrets

Skills must never:
- Hardcode API keys, tokens, or passwords
- Log secrets to output
- Store secrets in generated files

If a skill needs credentials, instruct the user to set them as environment variables or configure them in the platform settings.

## Best Practices

- **Start restrictive, expand as needed.** It's safer to add a tool than to remove one.
- **Document why each tool is needed.** Future maintainers (and reviewers) should understand the reasoning.
- **Use negative rules.** `Never delete files. Only append or create new ones.`
- **Consider sandboxing.** If a skill runs untrusted code, use `context: fork` to isolate it.
