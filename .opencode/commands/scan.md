---
description: Scan the codebase to detect the technology stack, extract code structure, and generate knowledge base entries.
---
Analyze the current project and populate the Hero knowledge base with initial entries plus code intelligence.

Load the `project-context-generation` skill for enrichment guidance.

1. Run `hero scan --dry-run` first to preview what will be detected
2. Review the output with the user — check that languages, frameworks, and tools are correctly identified
3. If the preview looks good, run `hero scan` to generate entries and code intelligence
4. Enrich only the **stub knowledge entries** that are short and clearly placeholders. **Do not rewrite code-intelligence files** (anything under `.hero/knowledge/code/` — those are regenerated on every scan). Cap enrichment to at most the five highest-value entries: any generated overview / stack / project-structure / conventions / decisions stubs. Apply the `project-context-generation` skill's guidance, then **stop** — report what you changed and what you intentionally left alone, and end the workflow. Do not chase tangents about glob configs, local dev tooling, or AGENTS.md formatting unless the user asks.

The scan automatically includes code intelligence (packages, symbols, dependencies, hot files) unless `code_scan.depth` is set to `"disabled"` in hero.json. Use `hero scan --code` to run only the code intelligence scan.

Use `--force` to overwrite existing entries when re-scanning after stack changes.

$ARGUMENTS
