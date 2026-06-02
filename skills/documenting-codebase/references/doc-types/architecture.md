---
name: doc-architecture
description: How to create ARCHITECTURE.md — the top-level domain map, package layering, and data flow doc. Use when documenting system architecture.
---

# Creating ARCHITECTURE.md

## Overview
ARCHITECTURE.md is the top-level map of the codebase. It lives at the repo root and answers: what are the domains? How do packages layer? Where does data flow?

## Core Principle
ARCHITECTURE.md is a map, not a specification. It describes the current structure, not a future ideal.

## When to Create
- No ARCHITECTURE.md exists
- The codebase has >3 domains or >2 package layers
- New team members struggle to understand the codebase
- Refactoring is planned and the current state needs recording

## Step-by-Step Creation

### 1. Domain Map

List every domain and its responsibilities:

```markdown
## Domain Map

| Domain | Path | Responsibility | Key Files |
|--------|------|--------------|-----------|
| Auth | `features/auth/` | Login, signup, session | `login-form.tsx`, `auth-store.ts` |
| Dashboard | `features/dashboard/` | Metrics, charts, alerts | `metrics-panel.tsx`, `chart-utils.ts` |
| Settings | `features/settings/` | User preferences, config | `settings-form.tsx`, `config-api.ts` |
```

**How to identify domains:**
- Use GitNexus to query execution flows: `gitnexus query "domains" --repo <repo>`
- Look for `features/`, `domains/`, `modules/` directories
- Look for route groups in `app/` or `pages/`
- Look for distinct business capabilities (auth, billing, reporting)
- Verify with GitNexus context: `gitnexus context <DomainRoot>`

**Rules:**
- One row per domain
- Path must be relative to repo root
- Responsibility is one sentence
- Key files are the 2-3 most important files in that domain

### 2. Package Layering

Document which layer imports which:

```markdown
## Package Layering

```
UI Components → Feature Hooks → Feature Stores → Shared Services → API Client
     ↑                ↑               ↑                ↑                ↑
   (no imports    (imports UI)  (imports hooks)  (imports stores)  (imports shared)
    below)
```

**How to determine layering:**
- Use GitNexus to understand the import graph: `gitnexus context <SharedUtility>`
- Check for circular dependencies with GitNexus: `gitnexus cypher "MATCH (a:File)-[r]->(b:File), (b)-[r2]->(a) WHERE r.type = 'IMPORTS' AND r2.type = 'IMPORTS' RETURN a.filePath, b.filePath"`
- Identify shared utilities that are imported everywhere
- Read `import` statements across the codebase as secondary verification

**Rules:**
- Draw arrows showing import direction
- Lower layers must not import higher layers
- Flag any circular dependencies (verified with GitNexus)

### 3. Data Flow

Trace the lifecycle of data through the system:

```markdown
## Data Flow

### User Data
```
[Browser Form] → [API Route] → [Service Layer] → [Database]
                                    ↓
                              [Auth Middleware]
```

### Sync Data
```
[External API] → [Webhook Handler] → [Queue] → [Worker] → [Database]
```
```

**How to trace data flow:**
- Use GitNexus to query execution flows: `gitnexus query "[entity] flow" --repo <repo>`
- Pick the most important entity (e.g., User, Order, Document)
- Follow it from creation to storage to retrieval
- Note transformations at each step
- Verify with GitNexus impact: `gitnexus impact <EntityService> --direction both`

### 4. Key Decisions

Record the most important architectural decisions:

```markdown
## Key Decisions

| Decision | Rationale | Consequence |
|----------|-----------|-------------|
| Feature-based organization | Teams own features end-to-end | Cross-feature changes touch multiple dirs |
| Zustand for state | Simpler than Redux, no boilerplate | No built-in devtools |
| tRPC for API | Type-safe client-server | Tied to Node.js backend |
```

**Rules:**
- One row per decision
- Include the trade-off (every decision has a cost)
- Link to the ADR if one exists

## Verification Checklist
- [ ] Domain map has one row per domain
- [ ] Package layering shows import direction
- [ ] No circular dependencies are hidden (flagged if present)
- [ ] Data flow traces at least one entity end-to-end
- [ ] Key decisions include trade-offs
- [ ] File is under 200 lines (move deep details to `docs/design-docs/`)
