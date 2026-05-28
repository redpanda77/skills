---
name: skill-invocation
description: Reference for skill invocation modes — automatic, slash command, user-invocable, disable-model-invocation, and task workflow. Use when deciding how a skill should be triggered.
---

# Invocation Modes

How the skill gets loaded and executed.

## Automatic Invocation

The skill loads automatically when the user's query matches the skill's description.

**When to use:** The skill handles a common, specific task that the user shouldn't have to remember to invoke.

**Requirements:**
- Description must be specific with clear trigger phrases
- Must not overtrigger (test with unrelated queries)
- Consider adding negative triggers: `Do NOT use for...`

**Example:**
```yaml
description: Generates Python unit tests from function signatures. Use when user asks for "test this", "write tests", or "unit test coverage".
```

## Slash Command

User explicitly invokes the skill by typing `/skill-name`.

**When to use:** The skill is a tool the user intentionally reaches for, not something that should interrupt normal flow.

**Requirements:**
- Name should be memorable and related to the function
- Can be used alongside auto-invocation for the same skill
- Useful for skills that are powerful but niche

**Example:**
```
User: /security-review
```

## User-Invocable

The user can request the skill by name in natural language: "use the security-review skill".

**When to use:** You want users to be able to call the skill explicitly without remembering a slash command.

**Requirements:**
- Name is clear and descriptive
- Skill is listed in the user's available skills

## Disable Model Invocation

The skill never loads automatically. It only runs when explicitly invoked by the user (via slash command or by name).

**When to use:** The skill is dangerous, expensive, or only appropriate in specific contexts where the user must consciously opt in.

**Requirements:**
- Set `disable-model-invocation: true` in frontmatter (platform-specific)
- Description should still explain what it does, but the system won't auto-match
- User must explicitly request it

## Task Workflow

Some skills are designed to be triggered as part of a task or cron job, not by direct user query.

**When to use:** Background automation, scheduled tasks, or skills that run as part of a larger agent workflow.

**Requirements:**
- Skill must be self-contained (no user interaction needed)
- Should handle errors gracefully without user input
- Often used with `context: fork` for isolated execution

## Choosing the Right Mode

| User Says | Mode |
|-----------|------|
| "help me write tests" | Automatic |
| "I need to run the security audit" | Automatic |
| User types `/cleanup-branches` | Slash command |
| "use the security-review skill" | User-invocable |
| Dangerous or irreversible operation | Disable model invocation |
| Background task, scheduled job | Task workflow |

## Testing Invocation

Before shipping, verify:
- **Should trigger:** Test 3–5 relevant queries
- **Should NOT trigger:** Test 3–5 unrelated queries
- **Paraphrase test:** Test variations of the trigger phrase
- **Negative trigger test:** Test queries that match the domain but are out of scope
