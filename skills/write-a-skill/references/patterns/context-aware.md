# Pattern: Context-Aware Tool Selection

**Use when:** Same outcome, different tools depending on context.

## Characteristics
- Clear decision criteria
- Fallback options
- Transparency about choices
- Configurable thresholds

## Structure

```md
## Workflow: [Name]

### Decision Tree
1. Assess input/context
2. Evaluate criteria:
   - If [condition A]: Use [Tool X]
   - If [condition B]: Use [Tool Y]
   - If [condition C]: Use [Tool Z]
   - Else: Use [Fallback]

### Execute
Based on decision:
- Call appropriate tool
- Apply service-specific settings
- Generate access/output

### Explain
Provide context to user:
- Why this tool was selected
- Relevant constraints considered
- Alternative options available
```

## Example

```md
## Workflow: Smart File Storage

### Decision Tree
1. Check file type and size
2. Determine best storage location:
   - Large files (>10MB): Use cloud storage MCP
   - Collaborative docs: Use Notion/Docs MCP
   - Code files: Use GitHub MCP
   - Temporary files: Use local storage

### Execute Storage
Based on decision:
- Call appropriate MCP tool
- Apply service-specific metadata
- Generate access link

### Provide Context to User
Explain why that storage was chosen:
- File size considerations
- Collaboration requirements
- Persistence needs
```

## Key Techniques

1. **Decision criteria:** Measurable conditions (size, type, user count)
2. **Fallback chain:** Ordered preferences with defaults
3. **Explainability:** Always tell user why decision was made
4. **Override option:** Allow user to force specific tool
