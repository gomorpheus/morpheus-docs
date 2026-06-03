---
description: Create or update technical documentation and project context.
---
Route this documentation request to the appropriate specialist.

Determine the work type from the request:
- Project context, AGENTS.md, or repository instruction files → delegate to `project-context-builder`
- Technical documentation, operational docs, API docs → delegate to `documentation-engineer`

If the request is ambiguous, default to `documentation-engineer`.

Documentation request: $ARGUMENTS
