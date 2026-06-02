---
name: doc-planning-decision-tree
description: Decision tree for what docs to create based on audit findings. Use after the audit phase to plan documentation.
---

# Planning: What Docs to Create

## Overview
After the audit phase, use the 5 audit reports to decide what docs are needed. Create a doc only if it is missing or stale. Never create a doc for code that does not exist.

## Decision Tree

### TECH_STACK.md
- Does a tech stack doc exist? → YES → Is it stale? → NO → Skip
- Does a tech stack doc exist? → NO → Create
- Does a tech stack doc exist? → YES → Is it stale? → YES → Update

### GETTING_STARTED.md
- Does a setup/run doc exist? → YES → Is it tested and working? → YES → Skip
- Does a setup/run doc exist? → NO → Create
- Does a setup/run doc exist? → YES → Is it tested and working? → NO → Update

### ARCHITECTURE.md
- Does an architecture doc exist? → YES → Is it stale? → NO → Skip
- Does an architecture doc exist? → NO → Are there >3 domains or >2 layers? → YES → Create
- Does an architecture doc exist? → NO → Are there >3 domains or >2 layers? → NO → Skip

### STRUCTURE.md
- Does a structure doc exist? → YES → Is it stale? → NO → Skip
- Does a structure doc exist? → NO → Is the directory structure complex or unconventional? → YES → Create
- Does a structure doc exist? → NO → Is the directory structure complex or unconventional? → NO → Skip

### CONVENTIONS.md
- Does a conventions doc exist? → YES → Is it stale? → NO → Skip
- Does a conventions doc exist? → NO → Are there linting rules or patterns? → YES → Create
- Does a conventions doc exist? → NO → Are there linting rules or patterns? → NO → Skip

### TESTING.md
- Does a testing doc exist? → YES → Is it stale? → NO → Skip
- Does a testing doc exist? → NO → Do tests exist? → YES → Create
- Does a testing doc exist? → NO → Do tests exist? → NO → Skip

### DEVELOPMENT.md
- Does a development workflow doc exist? → YES → Is it stale? → NO → Skip
- Does a development workflow doc exist? → NO → Create

### API.md
- Does an API doc exist? → YES → Is it stale? → NO → Skip
- Does an API doc exist? → NO → Do API routes or services exist? → YES → Create
- Does an API doc exist? → NO → Do API routes or services exist? → NO → Skip

### DATABASE.md
- Does a database doc exist? → YES → Is it stale? → NO → Skip
- Does a database doc exist? → NO → Does a database or schema exist? → YES → Create
- Does a database doc exist? → NO → Does a database or schema exist? → NO → Skip

### DEPLOYMENT.md
- Does a deployment doc exist? → YES → Is it stale? → NO → Skip
- Does a deployment doc exist? → NO → Is there hosting or CI/CD? → YES → Create
- Does a deployment doc exist? → NO → Is there hosting or CI/CD? → NO → Skip

### TROUBLESHOOTING.md
- Does a troubleshooting doc exist? → YES → Is it stale? → NO → Skip
- Does a troubleshooting doc exist? → NO → Are there known issues? → YES → Create
- Does a troubleshooting doc exist? → NO → Are there known issues? → NO → Skip

### DESIGN.md
- Does a design doc exist? → YES → Is it stale? → NO → Skip
- Does a design doc exist? → NO → Is there a custom design system or theme? → YES → Create
- Does a design doc exist? → NO → Is there a custom design system or theme? → NO → Skip

## Output

Produce a plan:

```markdown
## Documentation Plan

| Doc | Action | Priority | Source |
|-----|--------|----------|--------|
| TECH_STACK.md | Create | High | Tech Stack Audit |
| ARCHITECTURE.md | Update | High | Architecture Audit |
| TESTING.md | Create | Medium | Testing Audit |
```

**Priority:** High = critical for onboarding, Medium = helpful, Low = nice to have
**Source:** Which audit report identified the need
