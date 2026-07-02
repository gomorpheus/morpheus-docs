---
type: initiative
status: completed
horizon: now
tags: [i18n, spanish, localization]
sprint: i18n-spanish-v1
completed_at: 2026-07-02T15:21:29Z
---

# Spanish (es) Documentation Localization

## Objective

Translate the full HPE Morpheus Enterprise documentation site into Spanish using AI-powered translation, with terminology aligned to the official Morpheus UI Spanish locale (`messages_es_ES.properties`).

## Context

- 729 translatable content files (526 .rst + 203 .md) across 15 content directories
- Sphinx 4.2.0 on Read the Docs — supports i18n via gettext/sphinx-intl
- No existing i18n infrastructure — greenfield setup
- Official Spanish product terminology exists in `../morpheus-ui/morpheus-ui/grails-app/i18n/messages_es_ES.properties` (9,501 entries)
- Infrastructure designed for multi-locale expansion (fr, de, ja, etc. later)

## Terminology Reference

Source: `../morpheus-ui/morpheus-ui/grails-app/i18n/messages_es_ES.properties`

| English | Spanish |
|---|---|
| Instance | Instancia |
| Cloud | Nube |
| Group | Grupo |
| Workflow | Flujo de trabajo |
| Task | Tarea |
| Network | Red |
| Backup | Backup |
| Library | Biblioteca |
| Integration | Integración |
| Monitoring | Monitoreo |
| Provisioning | Aprovisionamiento |
| Infrastructure | Infraestructura |
| Security | Seguridad |
| Administration | Administración |

## Design Decisions

1. **Locale code:** `es` (generic Spanish for broad reach; terminology aligns with Spain UI locale)
2. **Translation method:** AI-comprehensive — model-generated translation of full corpus
3. **Glossary constraint:** AI pipeline constrained by official UI terminology
4. **What stays in English:** Code blocks, CLI commands, API endpoints, file paths, "HPE Morpheus Enterprise"
5. **Multi-locale ready:** Infrastructure supports adding arbitrary locales later
6. **RST/Markdown markup:** Must be preserved intact through translation pipeline
7. **`rst_prolog` substitutions:** Product names kept in English, UI navigation paths translated

## Risks

| Risk | Mitigation |
|---|---|
| AI mistranslates technical content | Glossary constraint + QA validation spec |
| RST/Markdown markup corruption | Build validation catches broken builds |
| `myst_parser` Markdown i18n edge cases | Infrastructure spec includes compatibility testing |
| `rst_prolog` substitution handling | Strategy defined in infrastructure spec |
| Rate limits on large file count (729) | Pipeline designed for batching + resumability |

## Children

### Phase 1: Infrastructure (blocking — must complete first)
- i18n-infrastructure
- i18n-ai-translation-pipeline

### Phase 2: Translation (parallel — all run concurrently after Phase 1)
- es-translate-administration
- es-translate-backups
- es-translate-getting-started
- es-translate-infrastructure
- es-translate-integration-guides
- es-translate-library
- es-translate-monitoring
- es-translate-operations
- es-translate-personas
- es-translate-provisioning
- es-translate-release-notes
- es-translate-security
- es-translate-shared
- es-translate-tools
- es-translate-troubleshooting

### Phase 3: Validation (gate — after all translations complete)
- es-validation-qa
