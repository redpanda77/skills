# Workflow Patterns

5 proven patterns for structuring skills. Select based on use case.

| Pattern | Use When | Key Characteristics |
|---------|----------|---------------------|
| [Sequential](sequential.md) | Multi-step process in specific order | Step dependencies, validation gates |
| [Multi-MCP](multi-mcp.md) | Workflow spans multiple services | Phase separation, data passing |
| [Iterative](iterative.md) | Output improves with refinement | Quality checks, loop until threshold |
| [Context-Aware](context-aware.md) | Same outcome, different tools by context | Decision tree, fallbacks |
| [Domain-Specific](domain-specific.md) | Specialized knowledge beyond tool access | Compliance checks, domain rules |

## How to Choose

**Start with:** What does the user want to accomplish?

- **Single service, multiple steps** → Sequential
- **Multiple services coordinated** → Multi-MCP
- **Quality matters, needs refinement** → Iterative
- **Same goal, different paths** → Context-Aware
- **Expert domain with rules** → Domain-Specific

## Deep Dive: Workflow Automation

For detailed coverage of Sequential and Iterative patterns including state management, validation gates, and deterministic validation, see [../workflow-automation.md](../workflow-automation.md).
