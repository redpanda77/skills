# Database

## Schema

### Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|

### Relationships

```
<table> ||--o{ <table> : <relation>
```

### Indexes

| Table | Index | Purpose |
|-------|-------|---------|

## Migrations

| Migration | Description | Date |
|-----------|-------------|------|

### Running Migrations

```bash
<command>
```

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
[Database] → [Cache] → [Service] → [Frontend]
```
