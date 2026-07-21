---
type: feature
status: delivering
horizon: now
tags: [documentation, library, virtual-images, field-feedback]
parent: docs-field-feedback-improvements
---

# Virtual Image Options Reference

## Objective

Document what each option on the Virtual Images detail page actually does, which cloud types each option applies to, and resolve perceived conflicts between the UI and existing docs.

## Acceptance Criteria

1. Every option/field on the Virtual Images create/edit form is documented with a clear description
2. A matrix shows which options apply to which cloud types (VMware, HVM, AWS, Azure, etc.)
3. Options that are cloud-specific are clearly marked
4. Conflicts between current docs and UI behavior are identified and resolved
5. Includes notes on options that have no effect for certain cloud types

## Changes

- `library/virtual_images/virtual_images.rst` — Expand field reference and add cloud applicability matrix
