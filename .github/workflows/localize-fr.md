---
on:
  push:
    branches: [dev-9.1]
    paths:
      - "**/*.rst"
      - "**/*.md"
  workflow_dispatch:
    inputs:
      base_ref:
        description: "Git ref to diff English docs against (default HEAD~1)"
        required: false
        type: string
  steps:
    - name: Skip localization bot loop commits
      id: skip_bot
      if: github.event_name == 'push'
      env:
        COMMIT_MSG: ${{ github.event.head_commit.message }}
      run: |
        if echo "$COMMIT_MSG" | grep -qiE '^\[localize/fr\]|^chore\(localize/fr\):'; then
          echo "Auto-localization commit; skipping." >&2
          exit 1
        fi

engine: copilot

permissions:
  contents: read
  copilot-requests: write

network: defaults

tools:
  edit:
  bash:
    - "python3:*"
    - "pip:*"
    - "msgfmt:*"
    - "make:*"
    - "sphinx-intl:*"
    - "git:*"
    - "cat:*"
    - "head:*"
    - "tail:*"
    - "grep:*"
    - "wc:*"
    - "sort:*"
    - "mkdir:*"

imports:
  - shared/localization-conventions.md
  - uses: shared/localization-pre-agent.md
    with:
      lang: fr

safe-outputs:
  create-pull-request:
    title-prefix: "[localize/fr] "
    labels: [localization, fr, automation]
    draft: true
    branch-prefix: localize/fr/

max-ai-credits: 2000
---

{{#runtime-import .github/workflows/shared/localization-conventions.md}}

# Incremental French (fr) localization

Synchronize French Sphinx gettext translations when English documentation changes.

## Before you start

1. Read `/tmp/gh-aw/agent/manifest.json` (written by the prepare step).
2. If the file is missing, or `pending_entry_count` is 0, call the **noop** safe output and stop immediately.
3. Read the glossary at the path in `manifest.glossary`.

## Workflow

1. For each file in `manifest.pending_files`:
   - Open the `.po` file at `path`.
   - Translate only entries with an empty `msgstr` or a `#, fuzzy` flag.
   - Leave already-translated, non-fuzzy entries unchanged.
   - Apply the glossary and conventions above.
2. Remove `#, fuzzy` from entries you update.
3. Validate each modified file: `msgfmt --check -o /dev/null <path>`.
4. Create a **draft pull request** with:
   - Title prefix already set to `[localize/fr]`
   - Body listing:
     - English files that changed (`english_files_changed`)
     - `.po` files updated and entry counts
     - Note that this is an incremental Copilot localization run

Do not modify files outside `locale/fr/`. Do not touch `tools/translate/work/`.

Commit message format: `chore(localize/fr): sync translations for English doc changes`
