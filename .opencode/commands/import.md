---
description: Import issues from the configured tracker into Hero spec scaffolds.
---
Import issues from the work tracker (Jira, GitHub, Linear) into Hero spec scaffolds.

The argument can be:
1. **A preset name** — matches a named filter from hero.json `import.presets` (e.g. `/import triage`)
2. **A raw JQL/filter string** — passed directly as a query (e.g. `/import type = Bug AND priority = Critical`)
3. **Empty** — uses the default filter from hero.json `import.filter`

## Steps

1. Parse the argument to determine if it's a preset name or a raw filter:
   - If the argument matches a key in `import.presets` in hero.json, use `--preset`
   - If the argument looks like a query (contains `=`, `AND`, `OR`, or field operators), use `--jql`
   - If empty, run with defaults

2. Run the appropriate `hero sync import` command:
   - Preset: `hero sync import --preset <name>`
   - Raw JQL: `hero sync import --jql "<query>"`
   - Default: `hero sync import`

3. Review the output — report how many issues were imported, skipped, and any errors

4. If an inventory report was generated, read it and summarize the highlights (critical/high counts, new items)

## Preset configuration

Presets are defined in hero.json:

```json
{
  "import": {
    "presets": {
      "my-bugs": { "assignee": "alice", "issue_type": "Bug" },
      "triage": { "assignee": "unassigned", "priority": "Critical" },
      "backlog": { "status": "To Do", "order_by": "priority DESC" }
    }
  }
}
```

To list available presets, read the project's hero.json and look under `import.presets`.

## Examples

```
/import                          # use default filter
/import triage                   # use the "triage" preset
/import my-bugs                  # use the "my-bugs" preset
/import type = Bug AND status = Open   # raw JQL query
```

$ARGUMENTS
