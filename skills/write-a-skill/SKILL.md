---
name: write-a-skill
description: Create agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, build, write, or author a new skill; when user mentions "skill", "SKILL.md", "agent capability", or asks how to make Claude follow specific workflows.
---

# Write a Skill

Create skills that teach Claude specific workflows, domains, or MCP integrations.

## Core Design Principles

### Progressive Disclosure (Most Critical)
Manage context window and token usage by loading only what's needed:

| Level | Content | When Loaded |
|-------|---------|-------------|
| **1. Frontmatter** | Name + description with strict triggers | Always (system prompt) |
| **2. SKILL.md body** | Core step-by-step instructions | When skill triggered |
| **3. Linked files** | Deep docs in `references/` folder | Only when needed |

### Composability
Skills work alongside others. Don't assume exclusive access. Handle your domain and gracefully co-exist with other active skills.

### Portability
Functions identically across Claude.ai, Claude Code, and API (assuming environment supports required tools).

---

## Quick Start Process

```
User: "Help me create a skill for [use case]"

1. Define use cases (2-3 concrete scenarios)
2. Validate frontmatter (kebab-case name, trigger-rich description)
3. Select workflow pattern (see references/patterns/)
4. Structure content (SKILL.md + references/)
5. Generate test suite
6. Review for anti-patterns
```

## Step-by-Step Guide

### Step 1: Gather Requirements

Before asking anything, check for `CONTEXT.md` in the project root and read it if present — use its terminology throughout the skill you create.

Then use `AskUserQuestion` to cover:
- What task/domain does this skill cover?
- What 2-3 specific use cases should it handle?
- Does it need executable scripts or just instructions?
- Any reference materials (API docs, style guides, schemas)?
- Is this enhancing an MCP integration?
- Global skill (`~/.claude/skills/`) or project-local (`.claude/skills/`)?

### Step 2: Validate Frontmatter

**Required format:**
```yaml
---
name: skill-name              # MUST be kebab-case
description: [What it does]. Use when [specific triggers].
---
```

**Description formula:**
```
[What it does] + [When to use it/Triggers] + [Key capabilities]
```

**Reject and rewrite if:**
- Too vague ("Helps with projects")
- Missing trigger phrases (no "Use when...")
- No specific keywords or file types mentioned

**Example:**
```yaml
# BAD - too vague
description: Helps with documents.

# GOOD - specific + triggers
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", or "design-to-code handoff".
```

### Step 3: Select Workflow Pattern

Diagnose the need and select a pattern. See [references/patterns/README.md](references/patterns/README.md).

| Pattern | Use When |
|---------|----------|
| **Sequential** | Multi-step process in specific order |
| **Multi-MCP** | Workflow spans multiple services |
| **Iterative** | Output improves with refinement loops |
| **Context-Aware** | Same outcome, different tools by context |
| **Domain-Specific** | Specialized knowledge beyond tool access |

### Step 4: Apply Progressive Disclosure

**Separation of concerns:**

| Component | Location | When to Split |
|-----------|----------|---------------|
| Core workflow | SKILL.md | Keep under 100 lines |
| Detailed schemas | `references/` | Always (never in SKILL.md) |
| Usage examples | `references/examples/` | >3 scenarios |
| Validation scripts | `scripts/` | Deterministic operations |

### Step 5: Generate Test Suite

**Triggering tests:**
```
Should trigger:
- "[Exact phrase from use case 1]"
- "[Paraphrased version]"
- "[Related technical term]"

Should NOT trigger:
- "[Adjacent but wrong domain]"
- "[Generic request - should use built-in]"
```

**Functional tests:**
```
Test: [Use case 1]
Given: [Input conditions]
When: Skill executes
Then: [Expected outcome]
```

### Step 6: Review Anti-Patterns

**Critical checks:**
- [ ] Name is kebab-case (not snake_case or CamelCase)
- [ ] No README.md inside skill folder
- [ ] No XML tags `< >` in frontmatter
- [ ] Description under 1024 characters
- [ ] Includes "Use when..." triggers
- [ ] No time-sensitive data (version numbers, percentages)
- [ ] Consistent terminology throughout

**If MCP-related:**
- [ ] Problem-first OR tool-first framing is clear
- [ ] MCP tool names verified against server docs
- [ ] Error handling for common MCP failures

---

## Output Format

Present the skill as:

1. **SKILL.md** - frontmatter + core workflow (under 100 lines)
2. **references/** - detailed docs, schemas, examples
3. **scripts/** - deterministic helpers (optional)
4. **Test suite** - triggering + functional tests
5. **Review checklist** - anti-patterns verified

See [references/GUIDE.md](references/GUIDE.md) for complete technical reference, MCP integration, testing strategies, and troubleshooting.

For Category 2 (Workflow Automation) deep dive: [references/workflow-automation.md](references/workflow-automation.md)
