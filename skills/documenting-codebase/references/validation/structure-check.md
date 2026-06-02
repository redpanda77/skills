---
name: doc-structure-check
description: Mechanical validation of the documentation structure. Use after all docs are written.
---

# Structure Check

## Overview
Run these mechanical checks after writing all docs. They verify structure, not content quality.

## Checks

### 1. Map Line Count

```bash
wc -l AGENTS.md
```

**Pass:** < 100 lines
**Fail:** >= 100 lines → Restructure into `docs/` and rewrite map

### 2. Link Integrity

Check every link in `AGENTS.md` and `docs/index.md`:

```bash
# Extract all markdown links and check file existence
for file in $(grep -oP '\]\(\K[^)]+' AGENTS.md docs/index.md); do
  [ -f "$file" ] && echo "OK: $file" || echo "MISSING: $file"
done
```

**Pass:** 0 missing files
**Fail:** >0 missing files → Create missing files or remove broken links

### 3. Index Coverage

Every file in `docs/` must be listed in an index:

```bash
find docs -name "*.md" -not -name "index.md" | sort > /tmp/all-files.txt
grep -oP '\]\(\K[^)]+' docs/index.md docs/*/index.md 2>/dev/null | sort -u > /tmp/indexed-files.txt
comm -23 /tmp/all-files.txt /tmp/indexed-files.txt
```

**Pass:** 0 unindexed files
**Fail:** >0 unindexed files → Add to relevant index.md

### 4. Monolithic Doc Check

Flag any doc >200 lines:

```bash
find docs -name "*.md" -exec wc -l {} + | awk '$1 > 200 {print $1, $2}'
```

**Pass:** 0 docs >200 lines (or each has a documented reason)
**Fail:** >0 docs >200 lines → Split into multiple docs or move to subdirectory

### 5. Subdirectory Index Check

Every subdirectory with >2 files must have an `index.md`:

```bash
for dir in $(find docs -type d); do
  count=$(find "$dir" -maxdepth 1 -type f | wc -l)
  if [ "$count" -gt 2 ] && [ ! -f "$dir/index.md" ]; then
    echo "MISSING INDEX: $dir"
  fi
done
```

**Pass:** 0 missing indexes
**Fail:** >0 missing indexes → Create index.md for each flagged directory

### 6. Duplicate Doc Check

Check for docs with similar names or overlapping content:

```bash
find docs -name "*.md" | sort
# Manually review for duplicates
```

**Pass:** No obvious duplicates
**Fail:** Duplicates found → Merge or rename

## Report Template

```markdown
## Structure Validation Report

| Check | Result | Details |
|-------|--------|---------|
| Map line count | PASS/FAIL | N lines |
| Link integrity | PASS/FAIL | N broken links |
| Index coverage | PASS/FAIL | N unindexed files |
| Monolithic docs | PASS/FAIL | N docs >200 lines |
| Subdirectory indexes | PASS/FAIL | N missing indexes |
| Duplicate docs | PASS/FAIL | N duplicates |
```
