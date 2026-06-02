---
name: gitnexus-overview
description: How to use GitNexus for codebase analysis when creating documentation. GitNexus is the primary tool for understanding connections, data flows, and data structures.
---

# GitNexus Integration

## Overview
GitNexus is the primary tool for codebase intelligence when documenting. It understands the codebase as a graph — call relationships, imports, execution flows, and component hierarchies. Use it instead of `find` or `grep` for structural analysis.

## Core Principle
Documentation must reflect the actual code graph, not a manual interpretation. GitNexus reveals the ground truth.

## When to Use GitNexus

| Task | GitNexus Command | Why Not `grep` |
|------|-----------------|----------------|
| Understand data flow | `gitnexus_query` | `grep` misses dynamic imports and re-exports |
| Find all consumers | `gitnexus_impact` | `grep` gives false positives/negatives |
| Map directory structure | `gitnexus_context` | `tree` shows files, not relationships |
| Check circular deps | `gitnexus_cypher` | Manual tracing is error-prone |
| Pre-commit validation | `gitnexus_detect_changes` | No manual substitute |

## Mandatory GitNexus Usage

### 1. Before Analyzing Codebase Structure

```bash
# Get 360-degree view of key symbols
npx gitnexus context <SymbolName>

# Query execution flows related to core concepts
npx gitnexus query "data flow" --repo <repo>
```

**Must use for:**
- Every domain identified in `ARCHITECTURE.md`
- Every shared primitive (Button, Card, Input, Modal, etc.)
- Every data store or service layer
- Every critical user path

### 2. Before Mapping Data Flow

```bash
# Trace full execution flow
npx gitnexus query "authentication flow" --repo <repo>

# Find upstream/downstream dependencies
npx gitnexus impact <SymbolName> --direction both
```

**Must use for:**
- Data entry points (API, database, file system)
- Data transformations (services, reducers, middleware)
- Data exit points (UI, API responses, file writes)
- State management flows

### 3. Before Documenting Directory Structure

```bash
# Check for circular dependencies in the structure
npx gitnexus cypher "MATCH (a:File)-[r]->(b:File), (b)-[r2]->(a) WHERE r.type = 'IMPORTS' AND r2.type = 'IMPORTS' RETURN a.filePath, b.filePath"

# Understand component hierarchies
npx gitnexus context <ComponentName>
```

### 4. Before Committing Documentation

```bash
# Verify structural analysis matches reality
npx gitnexus detect_changes
```

## GitNexus Tools Quick Reference

| Tool | Command | Use When |
|------|---------|----------|
| `query` | `gitnexus_query({query: "concept", repo: "repo"})` | Find code by concept/execution flow |
| `context` | `gitnexus_context({name: "SymbolName", repo: "repo"})` | 360-degree view of one symbol |
| `impact` | `gitnexus_impact({target: "Symbol", direction: "upstream", repo: "repo"})` | Blast radius before documenting |
| `detect_changes` | `gitnexus_detect_changes({scope: "all", repo: "repo"})` | Pre-commit scope check |
| `cypher` | `gitnexus_cypher({query: "MATCH ...", repo: "repo"})` | Custom graph queries |

## Keeping the Index Fresh

```bash
# After code changes, re-run analysis
npx gitnexus analyze

# With embeddings preserved
npx gitnexus analyze --embeddings

# Check freshness
npx gitnexus status
```

## Rules

- Never use `find` or `grep` as a substitute for GitNexus when GitNexus is available.
- Every `ARCHITECTURE.md` data flow must be verified with `gitnexus_query` or `gitnexus_impact`.
- Every `DESIGN.md` component spec must be verified with `gitnexus_context`.
- If GitNexus is unavailable, document the exception in the doc's notes.

## Error Handling

- GitNexus not installed: Prompt user to install `npx gitnexus` or use manual analysis with explicit caveat.
- Index stale: Run `npx gitnexus analyze` before proceeding.
- Query returns no results: Verify the symbol name or try a broader query.
