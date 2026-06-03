---
description: Challenge or revise a bug diagnosis — push back on the root cause with new context.
---
Route this challenge to the `feature-delivery-lead` agent, which manages the
re-investigation flow with the `debug-investigator`.

**Two modes**, detected from the feedback language:

| Mode | Trigger language | Behavior |
|---|---|---|
| **Layer** (default) | "also consider", "I think it's related to", "what about" | Merges the engineer's hypothesis with the existing analysis |
| **Reject** | "wrong", "not correct", "off base", "re-diagnose", "start over" | Archives current analysis into Investigation History, starts fresh |

**Flow:**

1. Read the existing bug spec at `.hero/planning/bugs/<slug>/spec.md`
2. If no diagnosis exists, error and suggest `/diagnose` first
3. Detect mode from the feedback language
4. **Layer**: pass original analysis + engineer feedback to `debug-investigator`
   with instructions to produce a merged analysis incorporating both
5. **Reject**: archive the current Root Cause / Fix Plan into
   `## Investigation History`, then pass engineer feedback as the starting
   hypothesis to a fresh `debug-investigator` run
6. Update the spec with revised findings
7. Append a new round to `## Investigation History`

**The agent must write all findings into the spec file on disk.** The spec file
is the deliverable, not chat output.

Load the `challenge-diagnosis` skill for the investigation history format and
re-diagnosis protocol.

---

## Session Title

Set a session title reflecting the challenge (e.g. "challenge: auth-timeout —
race condition hypothesis").

---

Challenge: $ARGUMENTS
