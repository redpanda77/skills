---
name: doc-deployment
description: How to create DEPLOYMENT.md. Use when documenting how the app runs in production and how to deploy it.
---

# Creating DEPLOYMENT.md

## Overview
DEPLOYMENT.md documents how the app runs in production and how to deploy it. It lives in `docs/DEPLOYMENT.md`.

## Core Principle
Deployment should be boring. It should be documented so anyone can do it without asking.

## Step-by-Step Creation

### 1. Infrastructure

```markdown
## Infrastructure

| Component | Provider | Purpose | Spec |
|-----------|----------|---------|------|
| App | Vercel | Host Next.js app | Pro plan |
| Database | Neon | Postgres | 2 vCPU, 8GB RAM |
| Cache | Upstash | Redis | 1GB |
| Storage | Cloudflare R2 | File uploads | 100GB |
| CDN | Cloudflare | Static assets | Pro plan |

### Architecture

```
[User] → [Cloudflare CDN] → [Vercel Edge] → [Next.js App] → [Neon DB]
                                    ↓
                              [Upstash Redis]
```
```

### 2. Environments

```markdown
## Environments

| Environment | URL | Branch | Auto-deploy |
|-------------|-----|--------|-------------|
| Development | localhost | any | No |
| Staging | staging.example.com | main | Yes |
| Production | example.com | release/* | Manual |

### Environment Variables

| Variable | Development | Staging | Production |
|----------|-------------|---------|------------|
| `DATABASE_URL` | Local Postgres | Staging Neon | Production Neon |
| `API_KEY` | Test key | Staging key | Production key |
| `DEBUG` | true | false | false |
```

### 3. Deploying

```markdown
## Deploying

### Staging

Merge to `main` triggers auto-deploy.

### Production

1. Create release branch: `git checkout -b release/2026-06-01`
2. Push branch: `git push origin release/2026-06-01`
3. Open PR to `production`
4. Get approval
5. Merge → triggers deploy

### Rollback

```bash
# Rollback to previous release
git revert <commit>
git push origin release/2026-06-01
```

Or in Vercel dashboard: Promote previous deployment.
```

## Verification Checklist
- [ ] Infrastructure components are listed
- [ ] Architecture diagram is included
- [ ] Environments are documented with URLs
- [ ] Environment variables are listed per environment
- [ ] Deploy process is step-by-step
- [ ] Rollback process is documented
