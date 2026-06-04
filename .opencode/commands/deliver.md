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
| `--autopilot` | Run to completion without intermediate confirmations. Stop only on test failure, drift warning, boundary violation, or any non-`DONE` Completion Ledger item (PARTIAL, SKIPPED, BLOCKED). |
| `--dry-run` | Run analysis and planning. Produce a delivery plan (file list, agent assignments, estimated changes) but write NO code. |

### Autopilot mode

Suppress confirmation prompts during the delivery loop. Check `hero drift`
after implementation, run tests if a runner is configured, validate the
engineer's **Completion Ledger** against the spec, and:
- **PARTIAL rows:** loop back to the engineer with instructions to finish
  them. Do not halt. Only escalate if a second pass returns PARTIAL on the
  same row with a specific written obstacle.
- **SKIPPED / BLOCKED rows:** halt and surface — these need user judgment.
- **Test failure / drift warning / boundary violation:** halt and surface.

If `--halt-on` is provided (comma-separated: `drift`, `test`, `boundary`,
`lint`, `ledger`), only halt on those specific conditions.

Persistence rule (`agent-reliability` — "Persistence on continuous tasks")
applies: do not yield between phases unless a true blocker fires. PARTIAL
is NOT a blocker — finish the work. SKIPPED and BLOCKED ARE blockers —
halt and surface. "This is taking a while" is NOT.

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
   - Require a **Completion Ledger** from the engineer covering every acceptance criterion and Changes item (see `engineer.md` — "Closing output"). Validate it against the spec.
   - Commit with a message referencing the spec slug and tracker ID
   - Only set `status: completed` if the ledger is fully `DONE`. PARTIAL rows are sent back to the engineer to finish (see "Validate the Completion Ledger" above); SKIPPED / BLOCKED rows halt and surface — do not flip status without sign-off. `hero spec verify` or the async runner will auto-archive completed specs to specs/.
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
   [list]. Mode: autopilot. I'll halt on test failures, boundary violations,
   or non-`DONE` Completion Ledger items."
4. Execute sequentially using the autopilot flow for each
5. Between each spec: run `hero drift`, run tests, validate the Completion
   Ledger, commit atomically
6. If a spec returns PARTIAL rows: loop the engineer to finish them before
   moving on — do not move to the next spec with PARTIAL rows unhandled.
   If a spec returns SKIPPED / BLOCKED rows or a test/drift failure: log
   the failure, skip the spec (do NOT flip to `completed`), continue with
   the next.
7. At the end: summary of delivered (fully `DONE`), halted (with SKIPPED /
   BLOCKED rows for user judgment), and failed (with reasons). PARTIAL
   should not appear in the final summary — it should have been resolved
   in step 6.

## Single spec mode

For a single spec delivery, follow the standard pre-flight and delivery workflow as the `feature-delivery-lead` agent.

**Pre-flight — check for mockups.** Before delegating to the engineer, check whether `.hero/mocks/{slug}/` exists for the spec being delivered. If it does, list the file paths inside it in the kickoff context handed to the engineer (e.g. "Mockups available for this spec: `.hero/mocks/{slug}/index.html` — read if a visual reference helps."). Don't render or quote the HTML; let the engineer open it if useful. The same check applies in batch and queue modes — surface mockup paths in the kickoff for each spec.

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
5. **Validate the Completion Ledger** — the engineer's closing artifact
   (see `engineer.md` — "Closing output") enumerates every acceptance
   criterion and every `## Changes` item with a `DONE` / `PARTIAL` /
   `SKIPPED` / `BLOCKED` status. Before flipping spec status:
   - Confirm every acceptance criterion and every Changes item has a row.
   - Cross-check each `DONE` against actual code and test evidence on disk.
     Challenge performative `DONE` marks; downgrade rows that lack evidence.
   - For user-visible behavior, confirm the Exercise-the-feature check is
     populated — unit tests alone are not sufficient evidence.
   - **PARTIAL is not an acceptable end state — finish the work.** PARTIAL
     means the engineer ran out of time, energy, or attention, not that the
     work is intrinsically un-doable. Do NOT ask the user "ship as-is or
     chase these down?" — the standing answer is *chase them down*. Send
     the ledger back to the engineer with the PARTIAL rows and explicit
     instructions to complete them, then re-validate. Only after a second
     pass *still* returns PARTIAL on the same row — with a written reason
     that names a specific obstacle (not "minor polish," not "low value")
     — may you surface it to the user. The bar: would a careful engineer
     reading this spec next week consider the work finished? If no, keep
     working.
   - **SKIPPED and BLOCKED** are legitimate human-judgment escalations.
     SKIPPED needs the user's call on scope; BLOCKED names a real external
     obstacle. Surface these with the specific row, the engineer's stated
     reason, and a concrete recommendation — not an open-ended question.
   - Do NOT flip to `completed` while any row remains non-`DONE`. In
     autopilot mode, PARTIAL re-enters the engineer loop automatically;
     SKIPPED / BLOCKED halt the run.
6. **Cold audit pass** — once the ledger is fully `DONE` (or non-`DONE`
   rows have explicit user sign-off), spawn a **fresh** subagent to audit
   the delivery before you flip status. This is the second set of eyes
   the lead cannot be, because the lead watched the work happen.

   Invoke a general-purpose subagent with the `delivery-audit` skill
   loaded. Hand it ONLY artifacts on disk — no commentary, no framing,
   no "this looks good to me":
   - Spec path (absolute)
   - Diff command (`git diff <base>...HEAD` or equivalent)
   - The engineer's Completion Ledger, verbatim
   - Test evidence (paths to test output, exercise notes)

   The audit writes a durable report file to disk and returns three
   blocks:
   - `<AUDIT_VERDICT>` — verdict (SHIP/HOLD), surface (noteworthy/clean),
     confidence, report_path
   - `<AUDIT_HEADLINE>` — **always populated**, the delivery receipt:
     AC count, audit verdict, report path, then a **New files** table,
     a **Modified files** table (each with a one-line description of
     what each file does or what changed), and a **Tests** summary
   - `<AUDIT_HIGHLIGHTS>` — populated when surface=noteworthy or
     verdict=HOLD; 1–5 bullets naming specific concerns

   Route based on the verdict:

   - **HOLD** → do NOT flip to `completed`. Read the highlights and the
     report file, route the specific concerns back to the engineer to
     address, re-validate the ledger, re-run the audit.
     **Bounded retry:** if the same row returns HOLD after 2 engineer
     passes, stop looping and escalate to the user with the auditor's
     concerns and a concrete recommendation. Do not grind indefinitely —
     a row that resists two focused passes usually needs human judgment
     (the spec was wrong, the approach was wrong, or a dependency is
     missing). Surface that, don't paper over it.
   - **SHIP + noteworthy** → quote the full `<AUDIT_HEADLINE>` (file
     tables and all) AND the `<AUDIT_HIGHLIGHTS>` bullets in your final
     response. Link to the full report at `report_path`. Proceed to
     step 7.
   - **SHIP + clean** → quote the full `<AUDIT_HEADLINE>` (file tables
     and all) in your final response. The receipt is earned signal on
     every delivery — do NOT collapse it to a one-liner. What you skip
     on a clean SHIP is the highlights block (because there's nothing
     to flag), not the inventory. Proceed to step 7.

   **What's always shown vs. conditional:**
   - **Always:** the full headline — what landed, file-by-file, plus
     test summary. This is the durable delivery receipt the user reads
     on every delivery; it's the only scannable record of what changed
     without diving into the diff.
   - **Conditional (only when noteworthy or HOLD):** highlights —
     downgrades, soft skips, concerns the auditor wants the user's eyes
     on.
   - **Always written to disk, linked from chat:** the full report file
     for when the user wants depth (evidence, line numbers, full
     reasoning).

   The signal-preservation rule is: make **highlights** conditional, not
   the inventory. A clean SHIP still gets the full file table — that's
   the point of running the audit.

   Do not skip this step in supervised mode. The cost is one subagent
   call; the value is catching performative `DONE` rows AND producing a
   durable delivery record.
7. **Refresh the kickoff** — when status flips (planning → delivering,
   delivering → completed) or after meaningful chunks land, rewrite the
   spec's `## Kickoff` section so "Pick up at:" reflects *now*, not
   "two commits ago." Follow the `kickoff-prompt` skill. After mutating
   the spec, run `hero index --if-stale -q` so the new state surfaces
   in `hero search` / `hero list` / `hero_*` MCP tools immediately.
   The pre-commit hook will refresh `.hero/QUEUE.md` automatically; if
   you're not committing right away, run `hero queue write -q` to
   refresh the snapshot manually.
8. **Suggest what's next** — your final response to the user must end
   with a concrete "Next up" suggestion. Not a list of options to choose
   from, not "let me know what you want to do" — a single recommended
   next move, named specifically. Examples:

   - "Next up: deliver `<dep-slug>` — it's the only remaining blocker on
     `<parent-slug>`."
   - "Next up: open the PR for this branch (`gh pr create`) and request
     review from the team."
   - "Next up: run `/diagnose <bug-slug>` — it's the highest-severity bug
     in the queue and touches code adjacent to what we just changed."
   - "Next up: take a break — the active spec list is empty and the
     queue is healthy."

   Use `hero_kickoff` or `hero_pulse` to inform the suggestion if you're
   uncertain. Always emit the suggestion via the `next-handoff-emit`
   pattern so it lands in `.hero/NEXT.md` and the per-user handoff file
   — that way the next session resumes with the same recommendation
   visible from the first prompt.

When delivery is complete and the Completion Ledger is fully `DONE` (or
non-`DONE` rows have explicit user sign-off), set the spec's
`status: completed` in the frontmatter and run `hero spec verify <slug>` —
verify auto-archives a completed spec to `.hero/specs/<slug>/`, so you
don't need a separate `hero spec complete` step. The async runner does the
same auto-archive at the tail of every successful agent delivery.

Do not hand-write `completed_at:` when you flip the status — `hero spec
verify` stamps the canonical timestamp automatically (RFC 3339 UTC) so
downstream consumers like the Sprint Dashboard read an authoritative
value. Hand-writing the field is harmless (idempotent) but unnecessary.

The Completion Ledger replaces the older "implementation summary" pattern.
Soft prose summaries that gloss skipped or partial work are explicitly
out — the ledger is the artifact of record.

### Spec-to-PR linking

After completing delivery, if the work was committed on a branch with an
open PR (check with `gh pr view` or equivalent), annotate the PR:

1. Add a comment linking back to the spec: "Delivered from Hero spec: `<slug>` — <title>"
2. If the spec has a `tracker_id`, mention it in the PR description
3. If a tracker is configured, use `hero_claim` to update the tracker issue
   with the PR link

This closes the spec→code→PR chain so reviewers can trace requirements.

Spec or work item: $ARGUMENTS
