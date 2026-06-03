---
description: Trace where something came from — multi-hop graph traversal showing the chain of decisions, specs, and commits that led to a target's existence.
---
Resolve the user's target (a spec slug, an `<spec-slug>:AC-N` criterion id,
a file path, or a commit SHA) and walk origin edges in reverse so the
chain reads oldest-first.

1. If the user named a specific target, run:

       hero why <target>

2. If the target is ambiguous, ask once. Origin edge types walked:
   `belongs_to`, `satisfied_by`, `attempted_in`, `decided_in`,
   `supersedes`, `mentions`, `depends_on`, `derived_from`,
   `originated_in`, `closes`, `fixes`. Default depth is 4 hops; pass
   `--depth N` to extend.

3. The output is a markdown trace. Surface it verbatim to the user;
   then summarize the throughline in one sentence so the chain is
   meaningful even if the user skims.

For a flat dump of every adjacent edge instead of the recursive trace,
use `hero why <target> --edges`.

$ARGUMENTS
