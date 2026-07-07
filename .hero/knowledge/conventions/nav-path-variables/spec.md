---
title: Navigation Path Variables
type: convention
status: active
created: 2026-07-07
scope: ["**/*.rst"]
tags: [docs, rst, convention]
---

## Navigation Path Variables

All UI menu click paths in documentation MUST use RST substitution variables defined in `conf.py` rather than hardcoded inline text.

### Why

If menu items are reshuffled in a UI update, paths only need to be updated in one place (`conf.py`) rather than across hundreds of doc files. This project has experienced major navigation restructuring before (v5.3.4 / v8.0.7) and variables prevented mass rewrites.

### How

Use the pipe-delimited substitution variables defined in `conf.py`'s `rst_prolog`:

```rst
Navigate to |TooAIInt| and click :guilabel:`+ New Integration`.
```

Renders as: "Navigate to Tools > AI Services > Integrations and click **+ New Integration**."

### Naming Pattern

Variables follow abbreviated PascalCase of the menu hierarchy:

| Pattern | Example | Expands To |
|---------|---------|-----------|
| `|SectionSubPage|` | `|AdmSetApp|` | Administration > Settings > Appliance |
| `|ProIns|` | — | Provisioning > Instances |
| `|InfClo|` | — | Infrastructure > Clouds |
| `|TooAIMCP|` | — | Tools > AI Services > MCP Servers |

### Rules

1. **ALWAYS** use an existing substitution variable when one exists for the path
2. **If no variable exists**, add one to `conf.py` in the `rst_prolog` section following the naming pattern
3. **`:menuselection:`** role is acceptable ONLY for truly one-off paths that will never repeat, but variables are strongly preferred
4. **Do NOT** hardcode raw path text like `Tools > AI Services > Integrations` in RST files

### Anti-patterns

```rst
# BAD - hardcoded path
Navigate to Tools > AI Services > Integrations

# BAD - menuselection when a variable exists
Navigate to :menuselection:`Tools --> AI Services --> Integrations`

# GOOD - substitution variable
Navigate to |TooAIInt|
```

### Variable Location

All navigation variables live in `conf.py` within the `rst_prolog` string (approximately lines 65-230). They are grouped by top-level menu section (Library, Provisioning, Operations, Infrastructure, Backups, Monitoring, Tools, Administration).
