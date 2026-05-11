# Complete Skill Writing Guide

From Anthropic's official guide to building skills for Claude.

## Core Design Principles

### Progressive Disclosure
Three-level system for managing context window and token usage:

1. **Level 1 (YAML Frontmatter):** Always loaded. Contains name and description with strict trigger conditions. Just enough to decide when to use the skill.

2. **Level 2 (SKILL.md body):** Loaded only when skill is triggered. Core step-by-step instructions.

3. **Level 3 (Linked files):** Stored in `references/` folder. Navigated only when deep-dive context needed (API pagination rules, brand guidelines, etc.).

### Composability
Skills play well with others. Don't assume exclusive access. Handle your domain and gracefully co-exist with other active skills.

### Portability
Functions identically across Claude.ai, Claude Code, and API (assuming environment supports required tools).

## Instructional Principles

### Problem-First vs. Tool-First

**Problem-First:** Orchestrating multiple tools to achieve an outcome.
```
"Set up a new project workspace" → Coordinates Notion, Linear, Slack MCPs
```

**Tool-First:** Enhancing a specific integration.
```
"Here is how you properly use the Notion integration" → Best practices for Notion MCP
```

### Specific & Actionable
Avoid vague: "Validate the data."

Provide deterministic: "Run `python scripts/validate.py --input {filename}`. Verify start date is not in the past."

### Anticipatory Error Handling
Map out what to do when things break:
```
If you see "Connection refused":
1. Verify MCP server running: Settings > Extensions
2. Check API key valid
3. Try reconnecting
```

### Iterative Refinement
For complex tasks, build in review steps:
```
1. Generate first draft
2. Check against quality checklist
3. Fix identified issues
4. Re-validate
5. Finalize only when threshold met
```

## Technical Requirements

### File Structure
```
your-skill-name/
├── SKILL.md              # Required - main skill file
├── scripts/              # Optional - executable code
├── references/           # Optional - documentation
│   ├── api-guide.md
│   └── examples/
└── assets/               # Optional - templates
```

### Critical Rules

| Rule | Requirement |
|------|-------------|
| SKILL.md naming | Exactly `SKILL.md` (case-sensitive) |
| Folder naming | kebab-case: `skill-name` |
| No README.md | Don't include README.md inside skill folder |
| No XML in frontmatter | Forbidden: `< >` characters |
| No reserved names | Can't use "claude" or "anthropic" in name |

### YAML Frontmatter Fields

**Required:**
```yaml
name: skill-name            # kebab-case only
description: What it does. Use when [triggers].
```

**Optional:**
```yaml
license: MIT                # If open source
compatibility:              # Environment needs
  - "Requires Python 3.8+"
  - "Network access for API calls"
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: service-name  # If MCP-related
```

## Writing Effective Descriptions

The description is **the only thing Claude sees** when deciding which skill to load. Appears in system prompt alongside all skills.

**Structure:**
```
[What it does] + [When to use it] + [Key capabilities]
```

**Good examples:**
```yaml
# Specific and actionable
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".

# Includes trigger phrases
description: Manages Linear project workflows including sprint planning, task creation, and status tracking. Use when user mentions "sprint", "Linear tasks", "project planning", or asks to "create tickets".

# Clear value proposition
description: End-to-end customer onboarding workflow for PayFlow. Handles account creation, payment setup, and subscription management. Use when user says "onboard new customer", "set up subscription", or "create PayFlow account".
```

**Bad examples:**
```yaml
# Too vague
description: Helps with projects.

# Missing triggers
description: Creates sophisticated multi-page documentation systems.

# Too technical
description: Implements the Project entity model with hierarchical relationships.
```

## Writing Main Instructions

**Recommended structure:**
```md
# Skill Name

## Instructions

### Step 1: [First Major Step]
Clear explanation of what happens.

Example:
```bash
python scripts/fetch_data.py --project-id PROJECT_ID
```

Expected output: [describe success]

## Examples

### Example 1: [common scenario]
User says: "..."
Actions:
1. Step one
2. Step two
Result: Expected outcome

## Troubleshooting

### Error: [Common error]
Cause: [Why it happens]
Solution: [How to fix]
```

**Best Practices:**
1. **Be specific and actionable**
   - ✅ Good: `Run python scripts/validate.py --input {filename}`
   - ❌ Bad: "Validate the data before proceeding"

2. **Include error handling**
   - Common issues with causes and solutions
   - MCP connection troubleshooting
   - Validation failure scenarios

3. **Reference bundled resources**
   - "Before writing queries, consult `references/api-patterns.md`"
   - "Use `scripts/validate.py` for format checking"

## MCP Integration

### Kitchen Analogy
- **MCP** = Professional kitchen (tools, ingredients, equipment)
- **Skills** = Recipes (step-by-step instructions)

### Integration Patterns

**Without skills:**
- Users connect MCP but don't know what to do
- Inconsistent results per session
- Support tickets asking "how do I do X"

**With skills:**
- Pre-built workflows activate automatically
- Consistent, reliable tool usage
- Best practices embedded

### When to Use Skills + MCP

| Use Case | Skill Purpose |
|----------|---------------|
| Problem-first | User wants outcome → Skill orchestrates right MCP calls |
| Tool-first | User has MCP access → Skill provides optimal workflows |

## Testing

### Three Test Types

**1. Triggering Tests**
Goal: Skill loads at right times
- ✅ Triggers on obvious tasks
- ✅ Triggers on paraphrased requests
- ❌ Doesn't trigger on unrelated topics

**2. Functional Tests**
Goal: Skill produces correct outputs
- Valid outputs generated
- API calls succeed
- Error handling works
- Edge cases covered

**3. Performance Comparison**
Goal: Skill improves results vs baseline
- Compare with/without skill
- Count tool calls and tokens
- Track success rates

### Iteration Signals

| Issue | Signal | Solution |
|-------|--------|----------|
| Undertriggering | Skill doesn't load when it should | Add more trigger phrases |
| Overtriggering | Loads for irrelevant queries | Add negative triggers, be specific |
| Execution issues | Inconsistent results | Improve instructions, add error handling |

## Troubleshooting

### Skill Won't Upload

| Error | Cause | Solution |
|-------|-------|----------|
| "Could not find SKILL.md" | Wrong filename | Rename to `SKILL.md` (case-sensitive) |
| "Invalid frontmatter" | YAML issue | Check delimiters, quotes, formatting |
| "Invalid skill name" | Spaces/capitals | Use kebab-case: `my-skill-name` |

### Skill Doesn't Trigger

Symptom: Never loads automatically

Debugging:
1. Ask Claude: "When would you use the [skill name] skill?"
2. Claude will quote the description
3. Adjust based on what's missing

**Fix:** Revise description to be more specific. Add trigger phrases.

### Skill Triggers Too Often

Solutions:
1. Add negative triggers:
   ```yaml
   description: Advanced data analysis for CSV. Use for statistical modeling. Do NOT use for simple exploration.
   ```

2. Be more specific:
   ```yaml
   # Too broad: description: Processes documents
   # Better: description: Processes PDF legal documents for contract review
   ```

### MCP Connection Issues

**Checklist:**
1. Verify MCP server connected
2. Check authentication/permissions
3. Test MCP independently (without skill)
4. Verify tool names match exactly

### Instructions Not Followed

**Common causes:**
1. **Too verbose** - Keep concise, use bullets
2. **Buried instructions** - Put critical steps at top
3. **Ambiguous language** - Be explicit

**Advanced fix:** For critical validations, bundle a script instead of relying on language instructions.

### Large Context Issues

**Symptoms:** Slow responses, degraded quality

**Solutions:**
1. Optimize SKILL.md size (<5,000 words)
2. Move detailed docs to `references/`
3. Reduce enabled skills (evaluate if >20-50)

## Distribution

### Current Model (2026)

**Individual users:**
1. Download skill folder
2. Zip if needed
3. Upload via Claude.ai Settings > Capabilities > Skills
4. Or place in Claude Code skills directory

**Organization:**
- Admins can deploy workspace-wide
- Automatic updates
- Centralized management

### Open Standard

Skills are published as an open standard for portability across platforms.

### Recommended Approach

1. **Host on GitHub**
   - Public repo
   - Clear README (repo-level, NOT in skill folder)
   - Installation instructions and screenshots

2. **Document MCP Integration**
   - Link skill from MCP docs
   - Explain value of using both
   - Provide quick-start guide

3. **Positioning**
   - Focus on outcomes, not features
   - Tell the MCP + skills story
   - Example: "MCP gives access; skills teach workflows"

## Checklist

Before finalizing:

**Frontmatter:**
- [ ] Name is kebab-case
- [ ] Description includes "Use when..." triggers
- [ ] Description under 1024 chars
- [ ] No XML tags in frontmatter

**SKILL.md:**
- [ ] Quick start example included
- [ ] Workflows have clear steps
- [ ] Concrete examples provided
- [ ] Troubleshooting covers common errors
- [ ] Under 100 lines OR split to references/

**Structure:**
- [ ] No README.md inside skill folder
- [ ] References one level deep
- [ ] Scripts included only if deterministic
- [ ] No time-sensitive data

**Testing:**
- [ ] Triggers on relevant queries
- [ ] Doesn't trigger on unrelated queries
- [ ] Workflows complete successfully
- [ ] Error handling works

## Use Case Categories

### Category 1: Document & Asset Creation
Used for: Consistent, high-quality output (documents, designs, code, etc.)

**Key techniques:**
- Embedded style guides
- Template structures
- Quality checklists
- No external tools required

### Category 2: Workflow Automation
Used for: Multi-step processes with consistent methodology

**Key techniques:**
- Step-by-step workflows with validation gates
- Templates for common structures
- Built-in review suggestions
- Iterative refinement loops

### Category 3: MCP Enhancement
Used for: Workflow guidance to enhance MCP tool access

**Key techniques:**
- Coordinate multiple MCP calls in sequence
- Embed domain expertise
- Provide context users would otherwise specify
- Error handling for common MCP issues

## Success Criteria

### Quantitative
- Triggers on 90% of relevant queries
- Completes workflow in X tool calls
- 0 failed API calls per workflow

### Qualitative
- Users don't need to prompt about next steps
- Workflows complete without correction
- Consistent results across sessions
