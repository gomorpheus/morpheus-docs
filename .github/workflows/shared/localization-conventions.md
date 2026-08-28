---
description: Shared translation rules for Morpheus Sphinx gettext localization
---

## Morpheus documentation localization conventions

These rules apply when translating Sphinx `.po` files under `locale/<lang>/LC_MESSAGES/`.

### Scope

- Translate only entries listed in the workflow manifest (`pending_files`) for this run.
- Do not re-translate entries that already have a non-empty `msgstr` unless they are marked `#, fuzzy`.
- Never modify English source files (`.rst`, `.md` outside `locale/`).

### Glossary (required)

- Read the language glossary JSON path from the manifest (`glossary`).
- When a glossary term appears in English text, use the exact target-language translation from the glossary.

### Markup and terminology

- Preserve ALL markup byte-for-byte: `` `code` ``, `|substitutions|`, `:ref:`, `:doc:`, `:menuselection:`, `:numref:`, hyperlink targets.
- `:guilabel:` text stays in English — do not translate the label value.
- Do NOT translate: code blocks, CLI commands, file paths, URLs, environment variables, API field names, package names, version numbers, JSON/YAML keys, log output, host/VM/datastore names.
- Keep product names in English: HPE Morpheus, Morpheus, Morpheus Data.

### Quality

- Fluent, professional technical documentation in the target language.
- Keep the same number of sentences; do not merge, split, or drop sentences.
- After editing `.po` files, run `msgfmt --check -o /dev/null <file>` on each modified file.

### Manual bulk localization commits

Commits tagged `[bulk-i18n]`, `[skip-localize]`, or `chore(i18n): bulk` are intentional full-locale updates and must not be overwritten or re-triggered by incremental localization.
