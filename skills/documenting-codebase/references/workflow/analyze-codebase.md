---
name: doc-analyze-codebase
description: How to analyze a codebase to determine what documentation is needed. Use after the audit step.
---

# Analyze Codebase

## Overview
After auditing existing docs, analyze the codebase to understand its structure, tech stack, domains, and conventions. This analysis determines what docs are needed and what they should contain.

## Core Principle
Docs must describe reality, not prescribe it. Analyze what exists, then document it.

## Step-by-Step Analysis

### 1. Use GitNexus for Structural Analysis

Before manual analysis, use GitNexus to understand the codebase graph:

```bash
# 360-degree view of the main entry point
npx gitnexus context App

# Query execution flows for core concepts
npx gitnexus query "data flow" --repo <repo>

# Check for circular dependencies
npx gitnexus cypher "MATCH (a:File)-[r]->(b:File), (b)-[r2]->(a) WHERE r.type = 'IMPORTS' AND r2.type = 'IMPORTS' RETURN a.filePath, b.filePath"
```

**Why GitNexus first:**
- It reveals the actual import graph, not just the file tree
- It finds dynamic imports and re-exports that `find` misses
- It identifies all consumers of shared primitives
- It traces transitive dependencies

**Rules:**
- Never use `find` or `grep` as a substitute for GitNexus when GitNexus is available.
- If GitNexus is unavailable, document the exception and proceed with manual analysis.

### 2. Identify Tech Stack

Read these files in order:

| File | What it tells you |
|------|-----------------|
| `package.json` | JS/TS dependencies, scripts, frameworks |
| `pyproject.toml` / `requirements.txt` | Python dependencies |
| `Cargo.toml` | Rust dependencies |
| `go.mod` | Go dependencies |
| `Dockerfile` / `docker-compose.yml` | Deployment stack |
| `.github/workflows/` | CI/CD stack |

Record:
- Primary language and framework
- Key libraries (state management, ORM, styling, testing)
- Build and deployment tools

### 3. Map Directory Structure

List top-level directories and categorize each. Use GitNexus to verify the structure:

```bash
npx gitnexus context <SymbolName>
```

```markdown
| Directory | Category | Role |
|-----------|----------|------|
| `app/` | Routes | Next.js app router pages |
| `components/` | UI | Reusable React components |
| `lib/` | Shared | Utilities, hooks, types |
| `features/` | Domains | Feature-based modules |
```

Categories:
- **Routes** — Page-level entry points
- **UI** — Reusable components, design system
- **Domains** — Feature-based business logic
- **Shared** — Utilities, types, hooks used across domains
- **Infra** — Config, CI, deployment
- **Data** — Database, schemas, migrations

### 4. Trace Data Flow

Use GitNexus to trace data flows:

```bash
npx gitnexus query "authentication flow" --repo <repo>
npx gitnexus impact <SymbolName> --direction both
```

Identify:
- Where does data enter the system? (API, database, file system)
- How does it transform? (services, reducers, middleware)
- Where does it exit? (UI, API response, file write)

Draw a simple flow:
```
[External API] → [Fetch layer] → [Store] → [Components] → [UI]
```

### 5. Identify Key Decisions

Use GitNexus to understand why the structure is the way it is:

```bash
npx gitnexus context <CustomAbstraction>
npx gitnexus query "state management" --repo <repo>
```

Look for:
- Unusual directory structure (e.g., feature-based vs layer-based)
- Custom abstractions (e.g., own router, own ORM wrapper)
- Tech choices that need explanation (e.g., "Why Zustand over Redux?")
- Performance or security trade-offs

### 5. Record Analysis

```markdown
## Codebase Analysis

### Tech Stack
- Language: ...
- Framework: ...
- Key libraries: ...

### Directory Structure
| Directory | Category | Role |

### Data Flow
```
[Source] → [Transform] → [Sink]
```

### Key Decisions
- [Decision] — [Rationale]

### Docs Needed
- [Doc] — [Why it matters] — [Priority]
```

## Verification Checklist
- [ ] Read the primary dependency file
- [ ] Listed and categorized all top-level directories
- [ ] Traced at least one data flow path
- [ ] Identified at least one key architectural decision
- [ ] Produced a prioritized list of needed docs
