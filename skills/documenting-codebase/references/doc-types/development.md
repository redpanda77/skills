---
name: doc-development
description: How to create DEVELOPMENT.md. Use when documenting development workflow, how to make changes, and how to contribute.
---

# Creating DEVELOPMENT.md

## Overview
DEVELOPMENT.md documents how to work with the codebase. How to make changes, branch strategy, PR process, and release flow. It lives in `docs/DEVELOPMENT.md`.

## Core Principle
A developer should know how to make a change and get it to production without asking anyone.

## Step-by-Step Creation

### 1. Development Workflow

```markdown
## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/<description>
```

Branch naming:
- `feature/<description>` — New features
- `fix/<description>` — Bug fixes
- `refactor/<description>` — Refactoring
- `docs/<description>` — Documentation

### 2. Make Changes

- Write code following `docs/CONVENTIONS.md`
- Write tests for new logic
- Run tests: `pnpm test`
- Run lint: `pnpm lint`

### 3. Commit

```bash
git commit -m "feat: add character review flow"
```

Commit format: `type: description`
- `feat:` — New feature
- `fix:` — Bug fix
- `refactor:` — Code change without behavior change
- `docs:` — Documentation
- `test:` — Tests
- `chore:` — Maintenance

### 4. Open PR

PR template:
- What changed
- Why it changed
- How to test
- Screenshots (if UI)

### 5. Merge

- PR requires 1 approval
- CI must pass
- Squash and merge
```

### 2. Adding a New Feature

```markdown
## Adding a New Feature

1. Create feature directory in `features/<name>/`
2. Add `ui/`, `hooks/`, `stores/`, `services/`, `types/`, `utils/`
3. Add tests for each file
4. Add route in `app/<name>/page.tsx`
5. Update `ARCHITECTURE.md` if new domain
6. Update `STRUCTURE.md` if new pattern
```

### 3. Release Flow

```markdown
## Release Flow

| Environment | Branch | Trigger | How |
|-------------|--------|---------|-----|
| Staging | `main` | Merge to main | Auto-deploy via GitHub Actions |
| Production | `release/*` | Tag push | Manual approval in GitHub Actions |

### Hotfix

```bash
git checkout -b hotfix/<description> origin/main
# Fix, test, commit
git push origin hotfix/<description>
# Open PR to main, merge
# Cherry-pick to release branch
```
```

## Verification Checklist
- [ ] Branch naming is clear
- [ ] Commit format is specified
- [ ] PR requirements are documented
- [ ] Adding a feature is step-by-step
- [ ] Release flow is documented
- [ ] Hotfix process is documented
