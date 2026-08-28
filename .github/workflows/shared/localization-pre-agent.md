---
description: Install deps and prepare incremental localization manifest before Copilot runs
runtimes:
  python: "3.12"
pre-agent-steps:
  - name: Install Python dependencies
    run: pip install -r requirements.txt
  - name: Prepare localization manifest
    id: prepare
    env:
      LANG_CODE: ${{ github.aw.import-inputs.lang }}
      COMMIT_MSG: ${{ github.event.head_commit.message || '' }}
      BASE_REF: ${{ github.event.before || 'HEAD~1' }}
      EVENT_NAME: ${{ github.event_name }}
      MANIFEST_PATH: /tmp/gh-aw/agent/manifest.json
    run: |
      set -euo pipefail
      mkdir -p /tmp/gh-aw/agent
      args=(--lang "$LANG_CODE" --manifest "$MANIFEST_PATH")
      if [ "$EVENT_NAME" = "push" ]; then
        args+=(--check-skip-commit --commit-message "$COMMIT_MSG")
        args+=(--check-english-changes --base-ref "$BASE_REF" --head-ref HEAD)
      fi
      if python3 tools/translate/prepare_diff_localize.py "${args[@]}"; then
        echo "has_work=true" >> "$GITHUB_OUTPUT"
      else
        code=$?
        if [ "$code" -eq 2 ] || [ "$code" -eq 3 ] || [ "$code" -eq 4 ]; then
          echo "has_work=false" >> "$GITHUB_OUTPUT"
          exit 0
        fi
        exit "$code"
      fi
import-schema:
  lang:
    type: string
    required: true
---
