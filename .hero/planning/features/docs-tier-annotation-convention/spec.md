---
title: "Tier Annotation Convention"
type: convention
slug: docs-tier-annotation-convention
status: planning
priority: high
horizon: now
parent: unified-docs-merge
---

# Tier Annotation Convention

## Purpose

Establish a consistent pattern for marking documentation content by product tier (Enterprise, Advanced, Essentials) so readers can quickly identify what applies to their license.

## Decision Needed

Choose an annotation approach:

1. **RST admonitions** — Custom admonition like `.. tier:: Enterprise, Advanced` rendered as a colored callout
2. **Badge/role** — Inline RST role like `:tier:`Enterprise`` that renders as a small label
3. **Conditional content** — RST `only::` or `ifconfig::` directives that show/hide content per build target
4. **Sidebar annotations** — Margin notes indicating tier availability

## Requirements

- Must be scannable — readers should spot tier restrictions at a glance
- Must work in Sphinx/RST and render cleanly on ReadTheDocs
- Must not require separate builds per tier (single output)
- Should degrade gracefully to plain text (PDF export)

## Acceptance Criteria

- [ ] Convention documented with examples
- [ ] At least 2 approaches prototyped and compared
- [ ] One approach selected and applied to a pilot section
- [ ] RST directive/role implemented (if custom)
