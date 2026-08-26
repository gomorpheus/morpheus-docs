# AI Translation Pipeline

Translates Sphinx documentation `.po` files into target languages using AI models, constrained by the official Morpheus UI glossary for terminology consistency.

## Prerequisites

```bash
pip3 install openai anthropic sphinx-intl
```

Set your API key:
```bash
export OPENAI_API_KEY=sk-...
# or
export ANTHROPIC_API_KEY=sk-ant-...
```

## Workflow

### 1. Extract glossary from UI translations

```bash
python3 tools/translate/extract_glossary.py
```

This parses `../morpheus-ui/morpheus-ui/grails-app/i18n/messages_es_ES.properties` and outputs `tools/translate/glossary.json` with 4,000+ term mappings.

### 2. Extract translatable strings (if not done)

```bash
make gettext
make intl-update
```

### 3. Translate a section

```bash
# Dry run to see what would be translated
python3 tools/translate/translate_po.py locale/es/LC_MESSAGES/getting_started --dry-run

# Translate a single file
python3 tools/translate/translate_po.py locale/es/LC_MESSAGES/getting_started/getting_started.po -v

# Translate an entire section
python3 tools/translate/translate_po.py locale/es/LC_MESSAGES/getting_started -v --report report_getting_started.json

# Translate all Spanish locale files
python3 tools/translate/translate_po.py locale/es/LC_MESSAGES -v --report report_full.json
```

### 4. Build the translated docs

```bash
make html-es
```

## Options

| Flag | Description |
|------|-------------|
| `--lang LANG` | Target language (default: `es`) |
| `--glossary PATH` | Path to glossary JSON |
| `--model MODEL` | AI model: `gpt-4o` (default), `claude-sonnet-4-20250514` |
| `--batch-size N` | Entries per API call (default: 20) |
| `--dry-run` | Preview without making API calls |
| `--resume` | Skip already-translated entries (default: on) |
| `--no-resume` | Re-translate all entries |
| `--report PATH` | Write JSON report to file |
| `--verbose` / `-v` | Detailed progress output |
| `--section NAME` | Translate only one section subdirectory |

## Multi-locale Support

Glossaries are extracted per language from the Morpheus UI i18n files:

| Language | Glossary | Source | Terms |
|----------|----------|--------|-------|
| Spanish | `glossary.json` | `messages_es_ES.properties` | ~4,438 |
| French | `glossary_fr.json` | `messages_fr.properties` | ~4,427 |
| German | `glossary_de.json` | `messages_de.properties` | ~4,417 |
| Portuguese | `glossary_pt.json` | `messages_pt_BR.properties` | ~3,490 |

Translate all strings for a language:

```bash
# Spanish (existing)
python3 tools/translate/translate_po.py locale/es/LC_MESSAGES -v --glossary tools/translate/glossary.json

# French
python3 tools/translate/translate_po.py locale/fr/LC_MESSAGES --lang fr --glossary tools/translate/glossary_fr.json -v

# German
python3 tools/translate/translate_po.py locale/de/LC_MESSAGES --lang de --glossary tools/translate/glossary_de.json -v

# Portuguese
python3 tools/translate/translate_po.py locale/pt/LC_MESSAGES --lang pt --glossary tools/translate/glossary_pt.json -v
```

Build shortcuts:

```bash
make html-es    # Spanish
make html-fr    # French
make html-de    # German
make html-pt    # Portuguese
make intl-build LANG=fr  # Any language
```

To add a new language:

```bash
# 1. Generate .po files for the new locale
sphinx-intl update -p _build/gettext -l fr -d locale

# 2. Extract glossary for the new language (if UI translations exist)
python3 tools/translate/extract_glossary.py path/to/messages_fr.properties

# 3. Translate
python3 tools/translate/translate_po.py locale/fr/LC_MESSAGES --lang fr --glossary tools/translate/glossary_fr.json -v
```

## Glossary

The glossary (`glossary.json`) is extracted from the Morpheus UI i18n properties file and ensures product terms match the UI exactly:

- Instance → Instancia
- Cloud → Nube
- Workflow → Flujo de trabajo
- Infrastructure → Infraestructura
- etc.

## How It Works

1. Parses `.po` files to find untranslated `msgid` entries
2. Batches entries (default: 20 per API call)
3. Builds a prompt with relevant glossary terms + markup preservation rules
4. Calls the AI model for translation
5. Writes translated `msgstr` values back to the `.po` file
6. Supports resume — re-running won't re-translate already-translated entries

## Validation

After translation, validate with:

```bash
# Check .po file syntax
find locale/es -name "*.po" -exec msgfmt --check {} \;

# Build and check for warnings
make html-es
```
