---
name: audit-testing
description: Audit subagent guide for analyzing test setup. Use when spawning a parallel audit subagent for test tools, coverage, and structure.
---

# Audit: Testing

## Scope
Analyze test files, test configs, and test structure. Report what is tested, how it is tested, and what is missing.

## Output Format

```markdown
## Testing Audit

### Test Tools
| Tool | Purpose | Config File |
|------|---------|-------------|
| [e.g., Vitest] | [e.g., Unit tests] | [e.g., vitest.config.ts] |
| [e.g., Playwright] | [e.g., E2E tests] | [e.g., playwright.config.ts] |

### Test Structure
```
<tree of test files>
```

### Coverage
| Type | Coverage | Target |
|------|----------|--------|
| [e.g., Unit] | [e.g., 75%] | [e.g., 80%] |
| [e.g., E2E] | [e.g., N/A] | [e.g., Critical paths] |

### What Is Tested
- [e.g., Utils and helpers]
- [e.g., API routes]
- [e.g., Component rendering]

### What Is NOT Tested
- [e.g., External API integrations]
- [e.g., UI animations]

### Test Commands
| Command | Purpose |
|---------|---------|
| [e.g., pnpm test] | [e.g., Run all tests] |
| [e.g., pnpm test:e2e] | [e.g., Run E2E tests] |

### Missing / Unclear
- [Anything that should be documented but isn't clear]
```

## Rules
- Find all test config files
- Find all test files
- Report coverage if available
- Identify gaps in testing
- Do NOT write a TESTING.md — only produce the audit report
