---
name: doc-testing
description: How to create TESTING.md. Use when documenting test strategy, test structure, and how to run tests.
---

# Creating TESTING.md

## Overview
TESTING.md documents how to test this codebase. What to test, how to run tests, and what tools are used. It lives in `docs/TESTING.md`.

## Core Principle
Tests are a developer tool, not a checkbox. Every test must be fast, reliable, and meaningful.

## Step-by-Step Creation

### 1. Test Tools

```markdown
## Test Tools

| Tool | Purpose | Command | Config |
|------|---------|---------|--------|
| Vitest | Unit tests | `pnpm test` | `vitest.config.ts` |
| Playwright | E2E tests | `pnpm test:e2e` | `playwright.config.ts` |
| React Testing Library | Component tests | `pnpm test:ui` | `vitest.config.ts` |
| MSW | API mocking | `pnpm test` | `mocks/handlers.ts` |

## Coverage

| Type | Target | Command |
|------|--------|---------|
| Unit | >80% | `pnpm test:coverage` |
| Integration | >60% | `pnpm test:integration` |
| E2E | Critical paths only | `pnpm test:e2e` |
```

### 2. Test Structure

```markdown
## Test Structure

```
features/
├── character-review/
│   ├── ui/
│   │   ├── CharacterCard.tsx
│   │   └── CharacterCard.test.tsx      # Component test
│   ├── hooks/
│   │   ├── useCharacterReview.ts
│   │   └── useCharacterReview.test.ts  # Hook test
│   └── services/
│       ├── characterApi.ts
│       └── characterApi.test.ts        # Service test
```

- Tests live next to the code they test.
- One test file per source file.
- Test file name matches source file + `.test`.
```

### 3. What to Test

```markdown
## What to Test

### Unit Tests
- Pure functions (utils, helpers)
- Hooks (state, effects, callbacks)
- Services (API calls, data transformation)

### Component Tests
- Render without crashing
- User interactions (click, type, submit)
- Props and state changes
- Error states

### E2E Tests
- Critical user flows (onboarding, checkout, login)
- Cross-page navigation
- Data persistence
- Mobile viewport

### Don't Test
- Third-party libraries
- Simple CSS
- Type definitions
- Implementation details (test behavior, not structure)
```

### 4. Running Tests

```markdown
## Running Tests

```bash
# All tests
pnpm test

# Watch mode
pnpm test:watch

# Coverage
pnpm test:coverage

# E2E
pnpm test:e2e

# E2E headed
pnpm test:e2e:headed

# Specific file
pnpm test CharacterCard
```
```

## Verification Checklist
- [ ] Test tools are listed with commands
- [ ] Coverage targets are realistic
- [ ] Test structure matches the codebase
- [ ] What to test and what not to test is clear
- [ ] Running commands are tested and working
