---
name: skill-lifecycle
description: Reference for skill lifecycle — context retention, auto-compaction, live reload, visibility overrides, and listing budget. Use when reasoning about how skills behave across sessions.
---

# Skill Lifecycle

How skills behave before, during, and after invocation.

## Context Retention

Skills do not automatically retain state between invocations. Each time a skill is triggered, it starts fresh with only:
- The current conversation context
- The skill's own files (SKILL.md, references, scripts)
- Any preloaded skills

**What this means:** If a skill needs to remember something across invocations, it must:
- Write state to a file (e.g., `.claude/state.json`)
- Use the project's memory system
- Ask the user to provide context

## Auto-Compaction

Long conversations with large skills may trigger context compaction. The system automatically summarizes older parts of the conversation to free up context window.

**What this means for skill authors:**
- Critical instructions should be in the first 40 lines (least likely to be compacted)
- Use progressive disclosure so deep references are only loaded when needed
- Don't rely on the agent remembering fine details from 50 messages ago

## Live Reload / Change Detection

When a skill file is modified on disk, the changes may be detected automatically depending on the platform:

- **Claude Code:** Skills are reloaded on the next invocation
- **Claude.ai:** Skills may require manual refresh or re-upload
- **API:** Skills are loaded fresh per request

**What this means:**
- Don't assume a skill change takes effect immediately
- For development, test after saving changes
- Some platforms cache skills; check documentation for refresh behavior

## Skill Visibility Overrides

A user can override which skills are visible/available in a session:

- **Enable/disable:** Turn specific skills on or off
- **Priority:** Some platforms let users prioritize which skills load first
- **Scope:** Project skills vs global skills vs plugin skills

**What this means for skill authors:**
- Don't assume your skill is the only one active
- Write composable skills that coexist gracefully
- Don't override global conventions unless necessary

## Skill Listing Budget

The system has a limit on how many skills can be loaded into the system prompt at once.

**Typical limits:**
- **Personal skills:** 20–50 depending on platform
- **Project skills:** Usually fewer, prioritized
- **Plugin skills:** Managed by the plugin system

**What this means:**
- Keep descriptions concise (under 200 chars if possible)
- Avoid overly broad trigger phrases that force the system to evaluate your skill for every query
- The more skills a user has, the more important specificity becomes

## Lifecycle Diagram

```
User Query
    ↓
System matches description against query
    ↓
Skill loaded (SKILL.md + frontmatter)
    ↓
Agent executes skill instructions
    ↓
References loaded on-demand
    ↓
Scripts executed on-demand
    ↓
Output delivered to user
    ↓
Context retained (conversation history)
    ↓
Skill state NOT retained (unless written to disk)
```

## Best Practices

- **Write state to files if needed.** Use `.claude/` or project temp directories.
- **Keep descriptions tight.** You're competing for listing budget with other skills.
- **Assume fresh start.** Each invocation is independent unless you explicitly persist.
- **Test with compaction in mind.** Put critical rules early.
