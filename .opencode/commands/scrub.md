---
description: Scrub the codebase for quality issues — dead code, weak types, duplication, bad comments, defensive programming, and legacy cruft.
---
Route this scrub request to the appropriate specialist(s) based on what the user wants cleaned up.

## Scrub concerns

Each concern maps to a specialist agent:

| Concern | Agent | What it does |
|---|---|---|
| `duplication` | `dedup-scrubber` | Find and consolidate duplicated code, apply DRY where it reduces complexity |
| `types` | `type-scrubber` | Consolidate shared types, remove weak types (`any`, `interface{}`, `unknown`), strengthen typing |
| `dead-code` | `deadcode-scrubber` | Find and remove unused functions, types, constants, imports, and unreachable code |
| `dependencies` | `dependency-scrubber` | Untangle circular or overly coupled dependencies, simplify import graphs |
| `defensive` | `defensive-scrubber` | Remove error-swallowing, unnecessary panic recovery, fallback patterns that hide bugs |
| `legacy` | `legacy-scrubber` | Remove deprecated, backwards-compat, and fallback code paths; make code singular |
| `comments` | `comment-scrubber` | Remove AI slop, narrating comments, stubs, misleading docs; keep only useful comments |
| `all` | all of the above | Run every scrub agent sequentially |

## Routing

1. If the user specifies a concern (e.g., `/scrub dead-code`), delegate to that agent only.
2. If the user says "all" or provides no specific concern, run **all agents sequentially** in the order listed above.
3. If the user describes a problem that maps to a concern (e.g., "there's a lot of copy-pasted code"), route to the matching agent.
4. If ambiguous, ask: "Which concern do you want to scrub? Options: duplication, types, dead-code, dependencies, defensive, legacy, comments, or all."

## Pre-flight

Before delegating to any agent:

1. Load the `code-scrub` skill for methodology and rules.
2. Load `stack-detection` to determine the project's language and tooling, then load the relevant stack skill.
3. Ensure `go build ./...` (or equivalent) passes before starting — don't scrub a broken build.

## Workflow per agent

Each scrub agent will:
1. **Research** — systematically scan the codebase for their concern
2. **Assess** — write a critical assessment with findings categorized by confidence (high/medium/low)
3. **Implement** — apply all high-confidence fixes
4. **Verify** — run build and tests after changes

## Post-scrub

After all requested agents complete:
1. Run the full build and test suite one final time.
2. Summarize: what was found, what was changed, what was left as recommendations.
3. If `knowledge.auto_capture` is enabled, capture any novel conventions or patterns discovered during scrub to `.hero/knowledge/`.

Scrub request: $ARGUMENTS
