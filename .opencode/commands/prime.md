---
description: Load context for this session — what's in progress, active conventions, decisions, and what to watch for.
---
Load session context. Do not begin any implementation — this is context-only.

**First, read your handoff briefing.** Run `hero next path` to get the
correct file path, then read it. This is a three-section briefing (Just
finished / Next / Context to carry forward) the previous session left
behind so you can resume without re-reading the chat. Surface its contents
to the user before any other priming output.

In team mode, also check `.hero/NEXT.md` for the team roster (who's
working on what) and any recent team updates.

**Then, surface the ready queue.** Read `.hero/QUEUE.md` (or run
`hero queue --limit 5`) and show the top few ready specs with their
kickoff prompts. This gives the user paste-ready session-openers for
the parallel work paths in flight, not just the one path NEXT.md
captured. If the queue is empty, skip silently.

**Next, run `hero recap`** to get a spec-grouped summary of recent activity
(commits grouped by spec, status transitions, knowledge updates). This
complements the handoff — intent from the last session plus facts from git.
If there's no recent activity, skip this section silently.

**Then, auto-reconcile.** Run `hero check --reconcile` to fix any status
drift (specs stuck at delivering when git shows completion, etc.). This
prevents stale status from accumulating across sessions. If nothing needs
fixing, skip silently.

Then be the `session-primer` agent and orient the engineer on active work,
conventions, decisions, and risks.

Session context: $ARGUMENTS
