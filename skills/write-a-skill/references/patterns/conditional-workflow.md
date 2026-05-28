---
name: skill-conditional-workflow-pattern
description: Conditional workflow pattern for decision-based skills. Use when the skill must guide the agent through decision points.
---

# Conditional Workflow Pattern

Guide the agent through decision points where the path depends on the input or context.

## Structure

```markdown
## [Workflow Name]

1. Determine the [decision criteria]:

   **[Condition A]?** → Follow "[Path A]" below
   **[Condition B]?** → Follow "[Path B]" below
   **[Condition C]?** → Follow "[Path C]" below

2. [Path A]:
   - [Step 1]
   - [Step 2]
   - [Step 3]

3. [Path B]:
   - [Step 1]
   - [Step 2]
   - [Step 3]

4. [Path C]:
   - [Step 1]
   - [Step 2]
   - [Step 3]
```

## When to Use

- The task has multiple valid approaches depending on input
- The agent must choose between tools, formats, or strategies
- Context determines the correct path
- Different user intents require different workflows

## Key Techniques

1. **Decision criteria are measurable** — "File size > 10MB" not "large file"
2. **Default path is explicit** — "If none of the above, use [default path]"
3. **Paths are complete** — Each path should be a full workflow, not a partial one
4. **Limit branches** — 2–3 paths are ideal. More than 4 is a sign the skill should be split
5. **Push large branches to references** — If a branch is complex, put it in a reference file

## Example

```markdown
## Document modification workflow

1. Determine the modification type:

   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow:
   - Use docx-js library
   - Build document from scratch
   - Export to .docx format

3. Editing workflow:
   - Unpack existing document
   - Modify XML directly
   - Validate after each change
   - Repack when complete
```

## Anti-Patterns

- **Nested conditions** — If a path has its own decision tree, split it into a reference file
- **Vague conditions** — "If it's complex" is not a decision criteria
- **Incomplete paths** — A path that says "handle appropriately" is not a path
- **Too many options** — More than 4 branches overwhelms the agent
