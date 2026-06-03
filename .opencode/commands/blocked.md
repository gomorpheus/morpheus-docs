---
description: List open features that can't move forward — joined dependency tree plus failing/regressed acceptance criteria.
---
Surface every open Feature whose progress is blocked. Two kinds of
blockers are joined automatically:

1. **Dependency-blocked** — Features whose `depends_on` / `blocks`
   edges point at specs not yet `completed` / `accepted`.
2. **AC-blocked** — Features whose Criterion nodes are `failing` or
   `regressed`. (Phase-3 of `acceptance-criteria-graph` flips status
   from run-result ingest, so this surfaces real test/AC failures.)

Run:

    hero blocked

The output is a tree of open features with their blockers underneath.
Surface it verbatim, then call out the most actionable item — usually
the deepest leaf (a failing AC, an upstream spec still in `planning`).

If the user asks "what's stuck on me?", filter mentally by
`claimed_by` from `hero status` first, then route here.

$ARGUMENTS
