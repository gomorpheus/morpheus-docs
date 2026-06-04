---
description: Investigate a bug, classify the root cause, and produce a fix spec.
---
**Before creating any file**, check whether the user is working in a sub-folder workspace. If so, preserve that workspace's `subproject:` frontmatter and write the spec under the workspace's `.hero/` root; otherwise write under the project `.hero/` root.

**Stamp the active domain in frontmatter.** New bug specs MUST emit a `domain:` field reflecting the workspace's active domain — run `hero domain` (or read the `domain` key from `.hero/hero.json`; empty means engineering) and write that value. This keeps bug specs under the correct DSKG namespace partition.

Route this bug investigation to the `debug-investigator` agent.

Pass the bug report and any spec path or tracker ID to the agent. The `debug-investigator` handles the complete diagnosis workflow: pre-flight status check, investigation, root cause classification, fix planning, spec writing, and tracker posting.

**Before starting work**, emit `hero next ask` to capture the bug report
the user pasted in. This preserves session intent across compaction — see
the `next-handoff-emit` skill for the full pattern.

**The agent must write all findings into the spec file on disk.** The spec file is the deliverable, not chat output.

**Always include a `## Kickoff` section** in the fix spec. Follow the `kickoff-prompt` skill — the kickoff is a paste-ready cold-start prompt for picking the fix work back up in a fresh session. Skipping it excludes the spec from `hero queue` and triggers a `hero check` advisory.

**After writing the fix spec, run `hero index --if-stale -q`** so it surfaces in `hero search` / `hero list` / MCP tools without anyone needing to run a manual reindex.

**Before proposing a fix direction**, call `hero_anchor` to check project tripwires. If any proposed fix would reintroduce a forbidden dependency, pattern, or tool, eliminate that direction and find an alternative within project constraints.

If the `debug-investigator` returns with `Needs more research? → Yes`, that is an acceptable outcome — report it to the user and move on.

---

## Batch Mode: Diagnosing Multiple Bugs

When asked to diagnose multiple bugs (e.g. "diagnose 10 bugs", "work through the imported bugs"):

1. **Always select from locally imported specs.** Run `hero search --list --type bug` to see what's available. Apply filters like `--status planning` or `--since YYYY-MM-DD` to narrow the list. **Never query the tracker to pick work items.**
2. **Filter out closed/completed specs.** Only select specs with an open status (`planning`, `draft`, `active`). Skip anything marked `completed` or `superseded`.
3. **Present the selection to the user** before starting work. Show the list of bugs you plan to diagnose and get confirmation.
4. **Default: one at a time.** Run each bug through the `debug-investigator` agent sequentially. Complete the full diagnosis for one bug — including writing the spec AND posting to the tracker (Step 8 of the agent) — before moving to the next.

### Parallel batch mode

If the user explicitly asks to run diagnoses in parallel (e.g. "run each in an agent", "diagnose all of them at once"), launch multiple Task agents. **Each agent must follow these rules:**

1. **Each agent runs as the `debug-investigator`**. Tell each agent: "You are the `debug-investigator`. Load the `debugging-investigation` skill. Diagnose the bug described in the spec at `<spec-path>`. Write all findings into the spec file on disk. After writing the spec, post results to the tracker (see step 6)."
2. **Include the bug context** in each agent's prompt — the spec path, the tracker ID, and a brief description of the bug. The agent will read the full spec and any tracker issues.
3. **Each agent MUST write findings to its spec file on disk.** The spec file is the deliverable. If the agent only reports findings in its response without updating the spec file, the diagnosis is incomplete.
4. **File safety: never delete, move, or rename spec files.** Each agent works only on its assigned spec. Do not run `hero spec complete`, do not move files between directories. The only file operation allowed is editing the assigned spec in-place.
5. **No cross-agent file access.** Each agent reads and writes only its own assigned spec.
6. **Each agent MUST post to the tracker.** If the spec has a `tracker_id` and a tracker is configured, the agent must run:
   - `hero sync attach <tracker_id> <spec-path> <tracker_id>-diagnosis.md` to upload the diagnosis
   - `hero sync comment <tracker_id> "<summary>"` to post a brief summary (root cause, fix location, severity)
   If the agent skips this step, the diagnosis is incomplete even if the spec file was written.

### After all agents complete

Review the results:
1. For each bug, verify the spec file still exists on disk and contains investigation findings
2. For each bug with a `tracker_id`, verify the agent posted to the tracker (check its output for "Comment posted" / "File attached" confirmation). Re-run any that missed the posting step.
3. Report any agents that failed to write to their spec file or post to tracker — re-run those individually

Provide a summary table:

| Bug | Spec | Root Cause | Severity | Status |
|-----|------|-----------|----------|--------|
| PROJ-123 | `.hero/planning/bugs/slug/spec.md` | [1-line summary] | high | diagnosed |
| PROJ-456 | `.hero/planning/bugs/slug/spec.md` | insufficient info | — | needs-research |

---

## Session Title

On the **first interaction**, set a concise session title reflecting the bug being diagnosed (e.g. "diagnose: null pointer in cart total", "diagnose: PROJ-456 export timeout").

---

Bug report: $ARGUMENTS
