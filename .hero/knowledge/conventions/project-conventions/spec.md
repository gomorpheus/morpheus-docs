---
title: Project Conventions
type: convention
status: active
created: 2026-06-04
scope: ["*"]
tags: [imported, conventions]
---

## Coding conventions

- **Don't assume.** Surface tradeoffs and ask questions if anything is unclear. Present multiple interpretations instead of picking one silently.
- **Simplicity first.** Write the minimum code that solves the problem. No speculative features, no unnecessary abstractions, and no error handling for impossible scenarios.
- **Surgical changes.** Touch only what is strictly required. Do not "improve" nearby code or refactor unrelated sections. Match the existing style perfectly.
- **Verify before reporting done.** Define clear success criteria for every task. Run tests or validation scripts and iterate until the criteria are met before reporting completion.
- Read a file before editing it
- Run tests after making changes
- Search the codebase before creating new files
- Make one logical change at a time and verify it before moving on
- Do not suppress errors or warnings to make tests pass
- If a fix attempt fails twice, stop and reassess the approach

<!-- Add project-specific conventions here -->

<!-- Imported from: AGENTS.md -->
