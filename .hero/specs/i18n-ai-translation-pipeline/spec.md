---
type: feature
status: completed
horizon: now
tags: [i18n, ai, tooling]
depends_on: [i18n-infrastructure]
parent: docs-i18n-spanish
sprint: i18n-spanish-v1
phase: 1
completed_at: 2026-07-02T14:30:41Z
---

# AI Translation Pipeline

## Objective

Build tooling that translates Sphinx .pot/.po files into Spanish using an AI model, constrained by the official Morpheus UI glossary to ensure terminology consistency.

## Changes

- `tools/translate/` — Translation pipeline script(s)
- `tools/translate/glossary.json` — Extracted terminology from messages_es_ES.properties
- `tools/translate/README.md` — Pipeline usage documentation

## Acceptance Criteria

1. Glossary extracted from `../morpheus-ui/morpheus-ui/grails-app/i18n/messages_es_ES.properties` into a structured format the pipeline can reference
2. Pipeline reads .pot or untranslated .po files and outputs translated .po files with populated `msgstr` entries
3. RST/Markdown markup in msgid strings is preserved exactly in translated msgstr (directives, roles, cross-refs, code spans)
4. Code blocks, CLI commands, API endpoints, and file paths are NOT translated
5. Product term "HPE Morpheus Enterprise" remains in English
6. All Morpheus product terms use official glossary translations (Instance → Instancia, etc.)
7. Pipeline supports batching and resumability (can be interrupted and restarted)
8. Pipeline produces a translation report: files processed, terms applied, any warnings
9. Output .po files pass `msgfmt --check` validation

## Design

### Glossary Extraction

Parse `messages_es_ES.properties` to extract key product terms into a JSON glossary:
```json
{
  "Instance": "Instancia",
  "Instances": "Instancias",
  "Cloud": "Nube",
  "Clouds": "Nubes",
  "Group": "Grupo",
  "Groups": "Grupos",
  "Workflow": "Flujo de trabajo",
  "Workflows": "Flujos de trabajo",
  "Task": "Tarea",
  "Tasks": "Tareas",
  "Network": "Red",
  "Networks": "Redes",
  "Backup": "Backup",
  "Backups": "Backups",
  "Library": "Biblioteca",
  "Integration": "Integración",
  "Integrations": "Integraciones",
  "Monitoring": "Monitoreo",
  "Provisioning": "Aprovisionamiento",
  "Infrastructure": "Infraestructura",
  "Security": "Seguridad",
  "Administration": "Administración"
}
```

### Translation Prompt Strategy

For each .po msgid:
1. Provide the glossary as context
2. Instruct: translate to Spanish, preserve all markup/formatting tokens, use glossary terms exactly
3. Validate output preserves markup structure before writing

### Markup Preservation

- RST roles (`:ref:`, `:doc:`, `:guilabel:`) — keep role syntax, translate display text only
- Inline code (`` `backticks` ``) — do not translate
- Directives (`.. note::`, `.. warning::`) — keep directive name, translate body
- Cross-references — keep target, translate display text if explicit

## Notes

- Consider whether to translate one msgid at a time or batch multiple for efficiency
- The pipeline should be generic enough to rerun for other locales (just swap glossary + target language)
- Source glossary: `../morpheus-ui/morpheus-ui/grails-app/i18n/messages_es_ES.properties`
