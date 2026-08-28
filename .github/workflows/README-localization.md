# Localization GitHub Actions (Copilot)

Incremental localization workflows keep `locale/{es,fr,de,pt}` in sync when English documentation (`.rst` / `.md`) changes on `dev-9.1`.

## Workflows

| Workflow | Language | Source |
|----------|----------|--------|
| `localize-es.md` | Spanish | English docs |
| `localize-fr.md` | French | English docs |
| `localize-de.md` | German | English docs |
| `localize-pt.md` | Portuguese | English docs |

These are [GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows) using **GitHub Copilot** as the translation engine. Each push to `dev-9.1` that changes English docs runs all four workflows in parallel (one per language).

## What triggers localization

- Push to `dev-9.1` that modifies `**/*.rst` or `**/*.md`
- Manual run via **Actions → localize-&lt;lang&gt; → Run workflow**

## What is ignored (no incremental run)

1. **Path filter** — commits that only touch `locale/**` (`.po` files) never match the push trigger.
2. **Bulk localization markers** in the commit message:
   - `[bulk-i18n]`
   - `[skip-localize]`
   - `chore(i18n): bulk`
3. **Auto-localization commits** from these workflows (`chore(localize/<lang>): ...` or `[localize/<lang>] ...` prefix).
4. **No pending strings** — after `sphinx-intl update`, if no empty/fuzzy entries need work, the agent no-ops.

Use bulk markers when committing large manual translation batches so automated runs do not fight your work.

## Setup (one-time, org admin)

1. Enable **GitHub Actions** on the repository.
2. Enable **GitHub Copilot** for the org and turn on **Copilot CLI** + **Allow use of Copilot CLI billed to the organization** in Copilot policy settings.
3. Each workflow declares `copilot-requests: write` so the Actions `GITHUB_TOKEN` can bill Copilot to the org (no personal PAT required when org billing is configured).

## Compile lock files

Agentic workflow sources (`.md`) must be compiled to `.lock.yml` before GitHub can run them:

```bash
gh extension install github/gh-aw   # once
gh aw compile localize-es
gh aw compile localize-fr
gh aw compile localize-de
gh aw compile localize-pt
git add .github/workflows/*.lock.yml
```

Recompile after editing any `.md` workflow source.

## Local testing

```bash
# Dry-run manifest generation for Spanish
python3 tools/translate/prepare_diff_localize.py --lang es --manifest /tmp/manifest.json

# Simulate bulk-i18n skip
python3 tools/translate/prepare_diff_localize.py --lang es --check-skip-commit \
  --commit-message "chore(i18n): bulk translate administration" && echo OK || echo SKIP
```

## Review flow

Each workflow opens a **draft PR** labeled `localization` for human review. Merge when translations look correct; the commit message format prevents re-trigger loops.
