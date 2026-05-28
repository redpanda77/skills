---
name: skill-patterns
description: Index of workflow and design patterns for structuring skills. Select based on use case. Always start with the Design pattern.
---

# Workflow Patterns

9 proven patterns for structuring skills. Select based on use case.

## Design Patterns

| Pattern | Use When | Key Characteristics |
|---------|----------|---------------------|
| [Design](design.md) | Before creating any skill | Interview, type selection, progressive disclosure map |

## Execution Patterns

| Pattern | Use When | Key Characteristics |
|---------|----------|---------------------|
| [Sequential](sequential.md) | Multi-step process in specific order | Step dependencies, validation gates |
| [Multi-MCP](multi-mcp.md) | Workflow spans multiple services | Phase separation, data passing |
| [Iterative](iterative.md) | Output improves with refinement | Quality checks, loop until threshold |
| [Context-Aware](context-aware.md) | Same outcome, different tools by context | Decision tree, fallbacks |
| [Domain-Specific](domain-specific.md) | Specialized knowledge beyond tool access | Compliance checks, domain rules |
| [Feedback Loops](feedback-loops.md) | Quality must be verified before proceeding | Validator → fix → repeat |
| [Conditional Workflow](conditional-workflow.md) | Decision points determine the path | Branches, criteria, defaults |

## Content Patterns

| Pattern | Use When | Key Characteristics |
|---------|----------|-------------|
| [Templates](templates.md) | Output must follow a consistent structure | Strict or flexible formatting |
| [Examples](examples.md) | Output quality depends on seeing examples | Input/output pairs, style demonstration |

## How to Choose

**Start with:** Run the [Design interview](design.md) to determine the skill type and information architecture.

After design, select execution pattern:

- **Single service, multiple steps** → Sequential
- **Multiple services coordinated** → Multi-MCP
- **Quality matters, needs refinement** → Iterative or Feedback Loops
- **Same goal, different paths** → Context-Aware or Conditional Workflow
- **Expert domain with rules** → Domain-Specific
- **Output must meet a standard** → Templates or Examples

For non-workflow skills, see the reference structures in [Design](design.md).

## Deep Dive: Workflow Automation

For detailed coverage of Sequential, Iterative, and Feedback Loops patterns including state management, validation gates, and deterministic validation, see the individual pattern files above.

Each pattern file includes:
- **Characteristics:** What makes this pattern distinct
- **Structure:** Template for the SKILL.md section
- **Example:** Concrete real-world scenario
- **Key techniques:** Best practices for this pattern
