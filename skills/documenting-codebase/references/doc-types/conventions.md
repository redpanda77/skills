---
name: doc-conventions
description: How to create CONVENTIONS.md. Use when documenting code conventions, linting rules, and patterns.
---

# Creating CONVENTIONS.md

## Overview
CONVENTIONS.md documents how to write code in this codebase. Naming, file organization, patterns, and anti-patterns. It lives in `docs/CONVENTIONS.md`.

## Core Principle
Conventions are enforced, not suggested. Every rule must be backed by a linter, a test, or a CI check.

## Step-by-Step Creation

### 1. Linting and Formatting

```markdown
## Linting and Formatting

| Tool | Purpose | Command | Config |
|------|---------|---------|--------|
| Biome | Lint, format, organize imports | `pnpm lint` | `biome.json` |
| React Doctor | React-specific rules | `pnpm doctor` | `.react-doctor.json` |
| TypeScript | Type checking | `pnpm typecheck` | `tsconfig.json` |

## Rules

### Biome
- Organize imports automatically
- No `console.log` in production code
- No unused variables
- No implicit `any`

### React Doctor
- No `useEffect` without cleanup
- No missing `key` props in lists
- No direct state mutation
- No `dangerouslySetInnerHTML` without justification
```

### 2. Naming Conventions

```markdown
## Naming

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `CharacterCard.tsx` |
| Hooks | camelCase, `use` prefix | `useCharacterReview` |
| Stores | camelCase, `use` + `Store` | `useCharacterStore` |
| Utils | camelCase | `formatDate` |
| Constants | SCREAMING_SNAKE_CASE | `MAX_RETRY_COUNT` |
| Files | kebab-case | `character-review.ts` |
| Directories | kebab-case | `character-review/` |
```

### 3. File Organization

```markdown
## File Organization

- One component per file
- Colocate tests: `CharacterCard.test.tsx`
- Colocate stories: `CharacterCard.stories.tsx`
- Keep files under 200 lines. Split if larger.
- Group related files in directories, not prefixes.
```

### 4. Patterns and Anti-Patterns

```markdown
## Patterns

- **Feature-based organization** — Code lives in the feature it serves.
- **Colocation** — Tests, stories, and styles live next to the component.
- **Explicit imports** — No barrel files (index.ts) for internal modules.
- **Error boundaries** — Every route has an error boundary.

## Anti-Patterns

- **Mixing data and UI** — Don't fetch data inside components. Use hooks.
- **Prop drilling** — Use stores or context for shared state.
- **Global styles** — Use Tailwind or CSS-in-JS. No global CSS.
- **Any types** — Every variable must have a type.
```

## Verification Checklist
- [ ] Linting tools are listed with commands
- [ ] Naming conventions cover all file types
- [ ] File organization rules are specific
- [ ] Patterns are backed by real code examples
- [ ] Anti-patterns are explained with why they are bad
