# Testing Documenting Codebase

## Should Trigger

- "Document this codebase"
- "Set up docs for this project"
- "Create a knowledge base"
- "Write AGENTS.md for this repo"
- "Audit our existing documentation"
- "Update our docs"

## Should NOT Trigger

- "What is the weather?"
- "Fix this bug"
- "Write a hello world"
- "Refactor this function"

## Functional Tests

### Test 1: New Project

**Query:** "Document this codebase"

**Expected:**
- Audit step checks for existing docs
- Analyzes codebase structure
- Creates `docs/` with subdirectories
- Writes `AGENTS.md` under 100 lines
- Validates cross-links

### Test 2: Existing Docs Audit

**Query:** "Audit our docs"

**Expected:**
- Reads existing `AGENTS.md` and `docs/`
- Reports stale or missing docs
- Suggests restructuring if AGENTS.md is too long
- Does not duplicate existing docs

### Test 3: Incremental Doc

**Query:** "Create a frontend architecture doc"

**Expected:**
- Checks if `docs/FRONTEND.md` or `docs/design-docs/` already has it
- Creates only the missing doc
- Updates `AGENTS.md` or `docs/index.md` to link it

### Test 4: Plan Integration

**Query:** "Create a plan for the refactor"

**Expected:**
- Invokes `writing-plans` skill
- Stores plan in `docs/plans/` per writing-plans convention

## Performance Checklist

- [ ] Skill loads on relevant queries (3+ tests)
- [ ] Skill does NOT load on unrelated queries (3+ tests)
- [ ] Core workflow completes successfully
- [ ] Error handling works for common failures
- [ ] Edge cases handled (missing input, existing docs, no clear structure)
- [ ] No secrets in any file
- [ ] Under line target for scope (SKILL.md < 100 lines)
- [ ] Negative rules included
- [ ] References are one level deep
- [ ] No README.md inside skill folder
- [ ] No time-sensitive data
