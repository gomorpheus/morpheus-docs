---
description: Plan a sprint by selecting and sequencing specs from a backlog or initiative.
---
Route this sprint planning request to the `feature-delivery-lead`.

The delivery lead will:
1. Read the initiative or backlog context provided
2. If a specific initiative slug is provided, load it and its child specs
3. If no initiative is specified, run `hero check` and `hero dashboard` to understand the current workspace state
4. Identify specs that are ready for the next sprint (dependencies met, not blocked)
5. Suggest a sprint scope based on:
   - Team capacity (if known from conventions/context)
   - Spec complexity and dependencies
   - Priority and business impact
6. For each selected spec, verify it has:
   - Clear acceptance criteria
   - A Changes section listing files to modify
   - An assigned owner (suggest one if unclaimed)
7. Produce a sprint plan document as a note in the knowledge base at `.hero/knowledge/notes/sprint-{date}/spec.md` containing:
   - Sprint goal (1 sentence)
   - Selected specs with delivery order
   - Dependency graph (if specs depend on each other)
   - Risk items and blockers
   - Capacity allocation (which specs go to whom)

**Sprint planning principles:**
- A sprint should be achievable in 1-2 weeks
- Include a mix of high-value features and smaller wins
- Don't overcommit — leave 20% buffer for unplanned work
- Prioritize specs that unblock other specs
- If a spec is too large for a sprint, suggest running `/split` first

## Execute mode

When the user says `/sprint execute <initiative>` or includes "execute", "run",
or "go" in the arguments:

1. Load the initiative and list its child specs in dependency order
   (use `hero_sequence` to determine optimal order)
2. Filter to specs with `status: planning` that have acceptance criteria
   and a Changes section — these are ready to deliver
3. Show the execution plan to the user: "Will deliver N specs in order:
   [list]. Mode: autopilot. Halting on: test failure, drift warning,
   boundary violation."
4. For each spec in order:
   a. Run `/deliver <slug> --autopilot`
   b. After delivery completes, run `hero drift <slug>` to verify
   c. If clean: run `hero spec complete <spec-path>`, log success, move to next
   d. If failure/drift/regression: halt, report the issue, ask whether
      to skip and continue or stop the sprint
5. At the end, produce a sprint summary: N delivered, N skipped (with reasons),
   total time, any specs remaining

**Safety rails:**
- Always show the plan before starting — never auto-execute without confirmation
- Default halt conditions: test failure, boundary violation, drift warning
- User can override with `--halt-on drift,test` to be selective
- Each spec delivery is atomic — failures don't corrupt prior work
- The sprint can be resumed: skipped specs stay at `planning`

Initiative or context: $ARGUMENTS
