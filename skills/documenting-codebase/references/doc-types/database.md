---
name: doc-database
description: How to create DATABASE.md. Use when documenting database schema, migrations, and data flow.
---

# Creating DATABASE.md

## Overview
DATABASE.md documents the database schema, migrations, and how data flows. It lives in `docs/DATABASE.md`.

## Core Principle
The database schema is the data model. Every table, every column, every relationship must be documented.

## Step-by-Step Creation

### 1. Schema

```markdown
## Schema

### Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `characters` | Store characters | `id`, `hanzi`, `pinyin`, `meaning`, `hsk_level` |
| `users` | User accounts | `id`, `email`, `password_hash`, `created_at` |
| `reviews` | Review sessions | `id`, `user_id`, `character_id`, `score`, `created_at` |

### Relationships

```
users ||--o{ reviews : has
characters ||--o{ reviews : has
```

### Indexes

| Table | Index | Purpose |
|-------|-------|---------|
| `reviews` | `user_id, created_at` | Fast query by user and date |
| `characters` | `hsk_level` | Filter by HSK level |
```

### 2. Migrations

```markdown
## Migrations

| Migration | Description | Date |
|-----------|-------------|------|
| `001_create_users` | Create users table | 2026-01-01 |
| `002_create_characters` | Create characters table | 2026-01-02 |
| `003_create_reviews` | Create reviews table | 2026-01-03 |

### Running Migrations

```bash
# Up
pnpm migrate:up

# Down
pnpm migrate:down

# Create new
pnpm migrate:create <name>
```
```

### 3. Data Flow

```markdown
## Data Flow

### Write Flow
```
[Frontend] → [API Route] → [Service] → [Repository] → [Database]
```

### Read Flow
```
[Database] → [Repository] → [Service] → [API Route] → [Frontend]
```

### Caching
```
[Database] → [Redis] → [Service] → [Frontend]
```

- Cache TTL: 5 minutes for character lists
- Cache invalidation: On review creation
```

## Verification Checklist
- [ ] All tables are listed with purpose
- [ ] Relationships are documented
- [ ] Indexes are listed with purpose
- [ ] Migrations are documented
- [ ] Data flow is traced for read and write
- [ ] Caching strategy is documented
