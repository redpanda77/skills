---
name: doc-troubleshooting
description: How to create TROUBLESHOOTING.md. Use when documenting common issues and how to fix them.
---

# Creating TROUBLESHOOTING.md

## Overview
TROUBLESHOOTING.md documents common issues and how to fix them. It lives in `docs/TROUBLESHOOTING.md`.

## Core Principle
Every issue that wastes a developer's time more than once belongs in this doc.

## Step-by-Step Creation

### 1. Common Issues

```markdown
## Common Issues

### Issue: "Module not found" after adding a new file

**Symptom:** `Error: Cannot find module './NewComponent'`
**Cause:** Import path is wrong or file extension is missing.
**Fix:**
1. Check the file exists: `ls src/components/NewComponent.tsx`
2. Check the import path: `import { NewComponent } from './NewComponent'`
3. If using Next.js, check the file is in the right directory.

### Issue: Tests fail after pulling main

**Symptom:** `pnpm test` fails after `git pull origin main`
**Cause:** Dependencies changed or database schema changed.
**Fix:**
1. Run `pnpm install`
2. Run `pnpm migrate:up`
3. Run `pnpm test` again

### Issue: App won't start

**Symptom:** `pnpm dev` fails with port error
**Cause:** Another process is using port 3000.
**Fix:**
1. Find the process: `lsof -i :3000`
2. Kill it: `kill -9 <PID>`
3. Or use a different port: `pnpm dev --port 3001`

### Issue: TypeScript errors after refactor

**Symptom:** `tsc` fails with type errors
**Cause:** Refactored type not propagated.
**Fix:**
1. Run `pnpm typecheck` to see all errors
2. Update types in the source file
3. Update imports in consumer files
4. Run `pnpm typecheck` again
```

### 2. Debugging Tips

```markdown
## Debugging Tips

### Frontend
- Use React DevTools to inspect component tree
- Use Network tab to check API calls
- Use Console to see errors and warnings

### Backend
- Check logs: `pnpm logs` or `docker logs <container>`
- Use debugger: `debugger;` in code or `node --inspect`
- Check database: `pnpm db:studio` or `psql`

### Tests
- Run single test: `pnpm test CharacterCard`
- Run with debug: `pnpm test:debug CharacterCard`
- Check test output: `pnpm test:verbose`
```

### 3. Known Gotchas

```markdown
## Known Gotchas

### Database connection pool exhaustion
**Symptom:** `FATAL: sorry, too many clients already`
**Cause:** Default pool size is too small for local dev.
**Fix:** Increase `max_connections` in `docker-compose.yml` or use connection pooling.

### Cache invalidation after schema change
**Symptom:** Old data still appears after migration
**Cause:** Redis cache not cleared after schema change
**Fix:** Run `pnpm cache:clear` after every migration

### Biome vs ESLint conflicts
**Symptom:** Formatting rules conflict between Biome and VS Code
**Cause:** VS Code default formatter overrides Biome
**Fix:** Set VS Code default formatter to Biome in workspace settings
```

## Verification Checklist
- [ ] Common issues are listed with symptoms, cause, and fix
- [ ] Fixes are step-by-step and tested
- [ ] Debugging tips are specific to the codebase
- [ ] Known gotchas are codebase-specific (not generic)
- [ ] Issues are ordered by frequency (most common first)
