---
name: doc-validate
description: How to validate the documentation structure. Use as the final step after writing all docs and the map.
---

# Validate Documentation

## Overview
After writing all docs and the map, validate the structure. Check that every doc is reachable, every link works, and the map is under 100 lines.

## Core Principle
Validation is mechanical. It checks structure, not content quality.

## Step-by-Step Validation

### 1. Check Map Line Count

```bash
wc -l AGENTS.md
# Must be < 100 lines
```

If >100 lines, restructure into `docs/` and rewrite the map.

### 2. Check All Links

Verify every link in `AGENTS.md` and `docs/index.md`:

```bash
# Check AGENTS.md links
for file in $(grep -oP '\]\(\K[^)]+' AGENTS.md); do
  [ -f "$file" ] && echo "OK: $file" || echo "MISSING: $file"
done

# Check docs/index.md links
for file in $(grep -oP '\]\(\K[^)]+' docs/index.md); do
  [ -f "$file" ] && echo "OK: $file" || echo "MISSING: $file"
done
```

### 3. Check Index Coverage

Verify that every file in `docs/` is listed in an index:

```bash
# List all .md files in docs/
find docs -name "*.md" | sort

# Compare to index entries
# Every file must appear in docs/index.md or a subdirectory index.md
```

### 4. Check for Monolithic Docs

Flag any doc >200 lines that should be split:

```bash
find docs -name "*.md" -exec wc -l {} + | sort -n
# Flag any file >200 lines
```

### 5. Check for Missing Indexes

Every subdirectory with >2 files must have an `index.md`:

```bash
for dir in $(find docs -type d); do
  count=$(find "$dir" -maxdepth 1 -type f | wc -l)
  if [ "$count" -gt 2 ] && [ ! -f "$dir/index.md" ]; then
    echo "MISSING INDEX: $dir"
  fi
done
```

## Validation Report

Produce a brief report:

```markdown
## Validation Report

- AGENTS.md line count: [N] lines ([PASS/FAIL])
- Broken links: [N] ([list if any])
- Unindexed files: [N] ([list if any])
- Monolithic docs: [N] ([list if any])
- Missing subdirectory indexes: [N] ([list if any])
```

## Verification Checklist
- [ ] AGENTS.md is under 100 lines
- [ ] Every link in AGENTS.md works
- [ ] Every link in docs/index.md works
- [ ] Every file in docs/ is listed in an index
- [ ] No doc >200 lines without a reason
- [ ] Every subdirectory with >2 files has an index.md
