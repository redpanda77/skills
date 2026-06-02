---
name: audit-devops
description: Audit subagent guide for analyzing deployment and DevOps. Use when spawning a parallel audit subagent for hosting, CI/CD, and infrastructure.
---

# Audit: DevOps & Deployment

## Scope
Analyze deployment config, CI/CD, environment variables, and infrastructure. Report how the app runs and how it is deployed.

## Output Format

```markdown
## DevOps & Deployment Audit

### Infrastructure
| Component | Provider | Purpose |
|-----------|----------|---------|
| [e.g., App] | [e.g., Vercel] | [e.g., Hosting] |
| [e.g., Database] | [e.g., Neon] | [e.g., Postgres] |
| [e.g., Cache] | [e.g., Upstash] | [e.g., Redis] |

### Environments
| Environment | URL | Branch | Auto-deploy |
|-------------|-----|--------|-------------|
| [e.g., Staging] | [e.g., staging.example.com] | [e.g., main] | [e.g., Yes] |
| [e.g., Production] | [e.g., example.com] | [e.g., release/*] | [e.g., Manual] |

### Environment Variables
| Variable | Required | Description |
|----------|----------|-------------|
| [e.g., DATABASE_URL] | [e.g., Yes] | [e.g., Postgres connection] |

### CI/CD
| File | Purpose |
|------|---------|
| [e.g., .github/workflows/ci.yml] | [e.g., Test, lint, build] |
| [e.g., .github/workflows/deploy.yml] | [e.g., Deploy to Vercel] |

### Deploy Commands
| Command | Purpose |
|---------|---------|
| [e.g., pnpm deploy:staging] | [e.g., Deploy to staging] |

### Missing / Unclear
- [Anything that should be documented but isn't clear]
```

## Rules
- Read `.github/workflows/` for CI/CD
- Read `Dockerfile` and `docker-compose.yml` if present
- Read `.env.example` or `.env` for environment variables
- Check for deployment scripts in `package.json`
- Do NOT write a DEPLOYMENT.md — only produce the audit report
