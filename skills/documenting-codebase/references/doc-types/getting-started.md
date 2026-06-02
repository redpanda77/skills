---
name: doc-getting-started
description: How to create GETTING_STARTED.md. Use when documenting how to run the codebase locally.
---

# Creating GETTING_STARTED.md

## Overview
GETTING_STARTED.md is the first doc a developer reads. It answers: how do I run this thing locally? It lives in `docs/GETTING_STARTED.md` or at the repo root.

## Core Principle
A developer should be able to go from `git clone` to running the app in under 15 minutes. If it takes longer, the doc is wrong.

## Step-by-Step Creation

### 1. Prerequisites

```markdown
## Prerequisites

| Tool | Version | Check |
|------|---------|-------|
| Node.js | 18.x | `node --version` |
| pnpm | 8.x | `pnpm --version` |
| Docker | 24.x | `docker --version` |
| Git | 2.x | `git --version` |
```

### 2. Clone and Install

```markdown
## Clone and Install

```bash
git clone <repo>
cd <repo>
pnpm install
```
```

### 3. Environment Variables

```markdown
## Environment Variables

Copy `.env.example` to `.env.local` and fill in:

| Variable | Required | Description | How to get |
|----------|----------|-------------|------------|
| `DATABASE_URL` | Yes | Postgres connection string | See `docs/DATABASE.md` |
| `API_KEY` | Yes | External API key | Ask team lead |
| `DEBUG` | No | Enable debug logging | `true` or `false` |
```

### 4. Run the App

```markdown
## Run the App

```bash
# Development
pnpm dev

# With hot reload
pnpm dev:watch

# With staging data
pnpm dev:staging
```

Open http://localhost:3000
```

### 5. Verify It Works

```markdown
## Verify It Works

1. Run tests: `pnpm test`
2. Run lint: `pnpm lint`
3. Open the app and check the health endpoint: `http://localhost:3000/health`
```

## Verification Checklist
- [ ] Prerequisites are listed with version checks
- [ ] Clone and install steps are copy-pasteable
- [ ] Environment variables are documented with how to get them
- [ ] Run commands are tested and working
- [ ] Verification steps confirm the setup is correct
