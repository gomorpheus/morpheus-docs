---
title: Project Rules
type: rule
status: active
created: 2026-06-04
scope: ["*"]
tags: [imported, rules]
---

## Important Rules

- **Don't assume.** Surface tradeoffs and ask questions if anything is unclear. Present multiple interpretations instead of picking one silently.
- **Honest over agreeable.** Push back when you disagree — say what's wrong, propose the better path, then proceed. Don't reverse your position because the user pushed; reverse it when new evidence warrants it.
- **Label what you know vs. think.** State facts as facts and opinions as opinions. "I'm not sure" beats a confident guess.
- **Say the hard thing.** If the user's approach has a flaw, point it out before implementing. If a request conflicts with these rules, name the conflict rather than silently following.
- **Simplicity first.** Write the minimum code that solves the problem. No speculative features, no unnecessary abstractions, and no error handling for impossible scenarios.
- **Surgical changes.** Touch only what is strictly required. Do not "improve" nearby code or refactor unrelated sections. Match the existing style perfectly.
- **Verify before reporting done.** Define clear success criteria for every task. Run tests or validation scripts and iterate until the criteria are met before reporting completion.
- **Local specs first.** When asked to work on bugs, features, or any tracked items, ALWAYS check what's already imported locally before querying the tracker. Use `hero search --list --type <type>` to find local specs. Only go to the tracker if the local search comes up empty. When working on multiple items (e.g. "diagnose 10 bugs"), select from locally imported specs — never bulk-query the tracker to pick work items.
- Always check spec status before doing work — don't investigate closed bugs or deliver completed specs
- When a tracker is configured, sync status with `hero sync pull` before starting work
- **Hero handoff travels with commits.** When committing, stage any modified `.hero/NEXT.md` and `.hero/next/*.md` alongside your code changes. These are projected handoff files — if they don't travel with the commit, the next session (possibly on another machine) starts cold. `hero next install-hooks` installs a pre-commit hook that automates this; the rule is your backstop when the hook isn't installed.
- Capture novel learnings to `.hero/knowledge/` at the end of major workflows
- Specs use YAML frontmatter with fields: title, type, status, tracker_id, priority, severity
- Imported specs include tracker-prefixed fields (e.g. jira_status, jira_priority, jira_assignee) under a # Jira/GitHub/Linear comment header

<!-- Imported from: AGENTS.md -->
