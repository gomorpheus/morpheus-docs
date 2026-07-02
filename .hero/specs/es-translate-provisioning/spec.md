---
type: feature
status: completed
horizon: now
tags: [i18n, spanish, translation]
depends_on: [i18n-infrastructure, i18n-ai-translation-pipeline]
parent: docs-i18n-spanish
sprint: i18n-spanish-v1
phase: 2
completed_at: 2026-07-02T15:17:32Z
---

# Translate: Provisioning (es)

## Objective

Translate all documentation in the `provisioning/` directory (~29 files) into Spanish using the AI translation pipeline.

## Changes

- `locale/es/LC_MESSAGES/provisioning/*.po` — Translated .po files

## Acceptance Criteria

1. All .po files for `provisioning/` have populated msgstr entries (no untranslated strings)
2. Translated .po files pass `msgfmt --check` validation
3. `make html` with language=es builds the provisioning section without errors or warnings
4. Product terminology matches official glossary (spot-check representative pages)
5. All RST/Markdown markup preserved — no broken cross-references, directives, or formatting
