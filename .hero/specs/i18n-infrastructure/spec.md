---
type: feature
status: completed
horizon: now
tags: [i18n, infrastructure]
depends_on: []
parent: docs-i18n-spanish
sprint: i18n-spanish-v1
phase: 1
completed_at: 2026-07-02T14:27:18Z
---

# Sphinx i18n Infrastructure Setup

## Objective

Set up the complete Sphinx internationalization infrastructure to support locale-based documentation builds, starting with Spanish (es) and designed for multi-locale expansion.

## Changes

- `conf.py` — Add `locale_dirs`, `gettext_compact`, language selector config
- `Makefile` — Add `gettext`, `intl-update`, `intl-build` targets
- `requirements.txt` — Add `sphinx-intl`
- `locale/es/LC_MESSAGES/` — Create directory structure
- `.readthedocs.yml` — Configure multi-language build support

## Acceptance Criteria

1. `make gettext` successfully extracts .pot files from all 729 source files (both .rst and .md)
2. `sphinx-intl update -l es` generates .po files in `locale/es/LC_MESSAGES/`
3. `make html` with `language=es` builds successfully with untranslated .po files (falls back to English)
4. myst_parser Markdown files are correctly extracted to .pot format
5. `rst_prolog` substitutions are handled (product names remain English, navigation paths extractable)
6. Directory structure supports adding additional locales (e.g., `locale/fr/`, `locale/de/`)
7. Read the Docs configuration supports serving the Spanish build

## Notes

- Sphinx 4.2.0 gettext support is mature but myst_parser may need `myst_gettext_mode` configuration
- The `rst_prolog` has ~250 substitution definitions — test that these don't generate noise in .pot files
- Consider whether `gettext_compact = False` (one .pot per source file) or `True` (one .pot per top-level dir) is better for the AI pipeline
