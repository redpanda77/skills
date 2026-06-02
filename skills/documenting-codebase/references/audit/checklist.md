---
name: doc-audit-checklist
description: Checklist for auditing existing documentation. Use when docs may already exist.
---

# Audit Checklist

## Overview
Use this checklist when auditing existing documentation. It ensures no existing doc is missed, no stale doc is trusted, and no gap is overlooked.

## Core Principle
Trust but verify. Every existing doc must be checked for freshness and accuracy.

## Checklist

### 1. Locate All Docs

- [ ] Check repo root for `AGENTS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `README.md`
- [ ] Check for `docs/` directory and all subdirectories
- [ ] Check `.github/` for `CONTRIBUTING.md`, issue templates
- [ ] Check source directories for inline READMEs or `__docs__` folders
- [ ] Check `wiki/` or `docs/` at repo root

### 2. Classify Each Doc

For every doc found:

- [ ] Record its location
- [ ] Record its status: Exists / Missing / Partial
- [ ] Check its date: when was it last updated?
- [ ] Check its line count: is it a map (>100 lines = monolithic)?

### 3. Check for Stale Content

For every doc:

- [ ] Mentions files or paths that no longer exist?
- [ ] References dependencies that have been removed?
- [ ] Describes architecture that has been refactored?
- [ ] Includes code examples that no longer compile?
- [ ] Has no date or "last verified" timestamp?

### 4. Check for Monolithic Docs

- [ ] Is `AGENTS.md` >100 lines? If yes, flag for restructuring.
- [ ] Is `README.md` >200 lines? If yes, flag for splitting.
- [ ] Is any single doc covering multiple topics? If yes, flag for splitting.

### 5. Check for Unlinked Docs

- [ ] Is every doc reachable from `AGENTS.md` or `docs/index.md`?
- [ ] Are there docs in subdirectories without a subdirectory index?
- [ ] Are there docs that are only findable by `find`?

### 6. Identify Gaps

- [ ] Is `ARCHITECTURE.md` missing?
- [ ] Is `DESIGN.md` missing (if the project has a design system)?
- [ ] Is `FRONTEND.md` missing (if the project has a frontend)?
- [ ] Is `PRODUCT.md` missing (if the project is user-facing)?
- [ ] Is `RELIABILITY.md` missing (if the project is in production)?
- [ ] Is `SECURITY.md` missing (if the project handles user data)?
- [ ] Are feature-specific docs missing for major features?

### 7. Write the Audit Report

- [ ] List all existing docs with status and freshness
- [ ] List all stale docs with specific reasons
- [ ] List all monolithic docs with line counts
- [ ] List all gaps with priority
- [ ] Recommend actions: create / update / split / delete
