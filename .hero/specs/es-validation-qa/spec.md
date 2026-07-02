---
type: feature
status: completed
horizon: now
tags: [i18n, spanish, qa]
depends_on: [es-translate-administration, es-translate-backups, es-translate-getting-started, es-translate-infrastructure, es-translate-integration-guides, es-translate-library, es-translate-monitoring, es-translate-operations, es-translate-personas, es-translate-provisioning, es-translate-release-notes, es-translate-security, es-translate-shared, es-translate-tools, es-translate-troubleshooting]
parent: docs-i18n-spanish
sprint: i18n-spanish-v1
phase: 3
completed_at: 2026-07-02T15:21:29Z
---

# Spanish Translation QA & Validation

## Objective

Validate the complete Spanish documentation build for correctness, terminology consistency, and publish-readiness.

## Acceptance Criteria

1. Full `make html` build with `language=es` completes with zero errors and no new warnings
2. All internal cross-references (`:ref:`, `:doc:`) resolve correctly
3. Terminology audit: grep all .po files for key product terms, verify 100% use official glossary translations
4. No untranslated strings remain (no empty msgstr entries in any .po file)
5. No English sentences left in translated output (except code blocks, commands, product name)
6. Sample 10 pages across different sections — verify readability and technical accuracy
7. Navigation (toctree) renders correctly in Spanish build
8. Search index works for Spanish content
9. Read the Docs staging build accessible and functional
10. Language selector (if enabled) switches between en/es correctly

## Notes

- Build a simple script to check for empty msgstr, terminology violations, and broken references
- Consider automated link checking (`sphinx -b linkcheck`)
- Flag any pages where the AI translation looks suspicious for human review
