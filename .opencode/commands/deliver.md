---
description: Execute a spec — implement the planned changes, validate, and complete the work item.
---
Route this delivery request to the `feature-delivery-lead` agent for execution.

Be the `feature-delivery-lead` agent. Load the `context-injection` skill before starting.

**Before starting work**, emit a `hero next ask` capturing what the user
asked for. This preserves session intent across compaction — see the
`next-handoff-emit` skill for the full pattern (ask / suggest / reflection).

## Delivery modes

Parse the mode from the user's invocation. If no mode is specified, default
to **supervised**.

| Flag | Behavior |
|---|---|
| `--supervised` (default) | Pause at handoffs, surface decisions, ask before destructive actions. Current behavior. |
| `--autopilot` | Run to completion without intermediate confirmations. Stop only on test failure, drift warning, or boundary violation. |
| `--dry-run` | Run analysis and planning. Produce a delivery plan (file list, agent assignments, estimated changes) but write NO code. |

### Autopilot mode

Suppress confirmation prompts during the delivery loop. Check `hero drift`
after implementation, run tests if a runner is configured, and halt only
on failures. If `--halt-on` is provided (comma-separated: `drift`, `test`,
`boundary`, `lint`), only halt on those specific conditions.

### Dry-run mode

Produce a plan at `.hero/planning/features/<slug>/plan.md`:

```markdown
# Delivery plan — <slug>
Generated: <timestamp>
Mode: dry-run

## Tasks (sequenced)
1. [specialist] description → target-file (~N lines)
2. ...

## Risks
- boundary checks, drift baseline, potential conflicts

## Estimated complexity
~N lines, N specialist handoffs, ~N minutes wall time
```

Do NOT write any source files. The plan file is the only output.

## Batch mode

If the user asks to fix/deliver multiple specs (e.g. "fix the researched bugs", "deliver the 5 planned features"):

1. Run `hero search --list --type bug --status planning` (or the appropriate type/status) to find candidate specs
2. Filter to specs that have a `## Suggested Fix Approach` or `## Changes` section — these are the ones with a plan ready to execute
3. Present the list to the user for confirmation: "Found N specs ready to deliver: [list]. Proceeding with all of them sequentially."
4. **Work through them sequentially, one at a time.** Each fix:
   - Read the spec and its fix plan
   - Implement the fix
   - Run tests / build to verify
   - Commit with a message referencing the spec slug and tracker ID
   - Set the spec's `status: completed` in the frontmatter; `hero spec verify` or the async runner will auto-archive it to specs/
   - Post results to tracker if configured
5. **One commit per fix** — each fix is atomic and independently revertable
6. If a fix fails tests or creates problems, skip it, note the issue in the spec, and move to the next one
7. At the end, summarize: N fixed, N skipped (with reasons)

**Do not parallelize fixes** — they may touch overlapping code and create conflicts. Sequential delivery ensures each fix builds on a clean, tested codebase.

## Queue mode

When the user says "deliver these while I'm away", "queue these up", or
provides a list of slugs with `--autopilot`:

1. Validate all specs are ready (have Changes section, pass quality gate)
2. Sort by dependency order using `hero_sequence`
3. Show the queue and get one confirmation: "Will deliver N specs in order:
   [list]. Mode: autopilot. I'll halt on test failures or boundary violations."
4. Execute sequentially using the autopilot flow for each
5. Between each spec: run `hero drift`, run tests, commit atomically
6. If one fails: log the failure, skip it, continue with the next
7. At the end: summary of delivered, skipped, and any issues

## Single spec mode

For a single spec delivery, follow the standard pre-flight and delivery workflow as the `feature-delivery-lead` agent.

At the end of the delivery loop:

1. **Check for drift** — verify the implementation matches the spec. Address
   any divergence before moving on.
2. **Verify and expand test coverage** — confirm every acceptance criterion
   has a corresponding test. When fixing a bug, add a regression test that
   reproduces the original failure. Look at the code you touched and the
   code around it — if adjacent functions or modules lack test coverage,
   add tests for them too. Match the project's existing test patterns and
   framework. The goal is to leave coverage better than you found it.
3. **Run the test suite** — make sure everything passes, including the
   tests you just wrote and any existing tests for the affected area.
4. **Link tests to criteria** — connect each new test back to the
   acceptance criterion it verifies so regressions are traceable.
5. **Refresh the kickoff** — when status flips (planning → delivering,
   delivering → completed) or after meaningful chunks land, rewrite the
   spec's `## Kickoff` section so "Pick up at:" reflects *now*, not
   "two commits ago." Follow the `kickoff-prompt` skill. After mutating
   the spec, run `hero index --if-stale -q` so the new state surfaces
   in `hero search` / `hero list` / `hero_*` MCP tools immediately.
   The pre-commit hook will refresh `.hero/QUEUE.md` automatically; if
   you're not committing right away, run `hero queue write -q` to
   refresh the snapshot manually.

When delivery is complete and verified, set the spec's `status: completed`
in the frontmatter and run `hero spec verify <slug>` — verify auto-archives a
completed spec to `.hero/specs/<slug>/`, so you don't need a separate
`hero spec complete` step. The async runner does the same auto-archive
at the tail of every successful agent delivery.

### Spec-to-PR linking

After completing delivery, if the work was committed on a branch with an
open PR (check with `gh pr view` or equivalent), annotate the PR:

1. Add a comment linking back to the spec: "Delivered from Hero spec: `<slug>` — <title>"
2. If the spec has a `tracker_id`, mention it in the PR description
3. If a tracker is configured, use `hero_claim` to update the tracker issue
   with the PR link

This closes the spec→code→PR chain so reviewers can trace requirements.

Spec or work item: $ARGUMENTS
