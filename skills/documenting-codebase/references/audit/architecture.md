---
name: audit-architecture
description: Audit subagent guide for analyzing codebase structure and architecture. Use when spawning a parallel audit subagent for domains, layering, and data flow.
---

# Audit: Architecture

## Scope
Analyze the directory structure, import graphs, domain boundaries, and data flows. Use GitNexus if available. Report how the codebase is organized and how data moves through it.

## Output Format

```markdown
## Architecture Audit

### Directory Structure
```
<tree or list of top-level dirs>
```

### Domains
| Domain | Path | Responsibility | Key Files |
|--------|------|--------------|-----------|
| [e.g., Auth] | [e.g., features/auth/] | [e.g., Login, signup] | [e.g., login-form.tsx, auth-store.ts] |

### Package Layering
```
[Layer A] → [Layer B] → [Layer C]
```

### Data Flow
```
[Source] → [Transform] → [Sink]
```

### Entry Points
| Entry Point | Path | Purpose |
|-------------|------|---------|
| [e.g., App] | [e.g., app/page.tsx] | [e.g., Main page] |

### Circular Dependencies
| File A | File B | Type |
|--------|--------|------|
| [e.g., a.ts] | [e.g., b.ts] | [e.g., IMPORTS] |

### Key Decisions
| Decision | Rationale | Consequence |
|----------|-----------|-------------|
| [e.g., Feature-based org] | [e.g., Team ownership] | [e.g., Cross-feature changes touch multiple dirs] |

### Missing / Unclear
- [Anything that should be documented but isn't clear]
```

## Rules
- Use GitNexus for import graphs and circular dependencies
- List every top-level directory with its role
- Identify 3-5 domains
- Trace at least one data flow
- Flag any circular dependencies
- Do NOT write an ARCHITECTURE.md — only produce the audit report
