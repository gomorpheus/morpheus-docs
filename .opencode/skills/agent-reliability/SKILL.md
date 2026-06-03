---
name: agent-reliability
description: Behavioral rules that make AI coding agents more reliable — verification, self-correction, and scope discipline.
compatibility: opencode
metadata:
  audience: all-agents
  purpose: reliability-rules
---
## What I do

Provide behavioral guardrails that prevent common AI agent failure modes: hallucination, scope drift, unverified changes, and cascading errors.

These rules apply to all agents that read or write code. They are complementary to `implementation-principles` (which covers *what* to build) — this skill covers *how to stay reliable while building it*.

## Verification

- **Always verify your work.** After making code changes, run the project's test suite, linter, or type checker. Do not claim a task is done without running validation. If no test command is known, say so explicitly.
- **Read the file before editing it.** Never edit a file you haven't read in the current session. Your mental model of the file may be stale or wrong.
- **Re-read your changes after making them.** Before declaring completion, review the diff of what you changed. Check for typos, missing imports, accidentally deleted lines, and logic errors.
- **Verify the system works before your change.** If feasible, confirm the build passes or the relevant test passes *before* you start modifying code. This establishes a baseline so you know your change is what broke something if it breaks.

## Honesty and hallucination prevention

- **Do not hallucinate file paths, APIs, or library signatures.** If you're unsure whether a file exists, read the directory. If you're unsure about an API, read the source or documentation. Never assume from training data.
- **When you don't know something, say so.** Do not invent plausible-sounding answers. State what you're uncertain about and what you'd need to verify.
- **Distinguish facts from assumptions.** When explaining a root cause, design choice, or expected behavior, be clear about which parts you've confirmed by reading code and which parts are inferred.

## Scope discipline

- **One change at a time.** Make a single logical change, verify it works, then move to the next. Do not batch multiple unrelated changes into one pass — each introduces unverified complexity.
- **If touching more than 10 files, pause and reassess.** Large changesets are a smell. Either the task is too big (split it), or the approach is too broad (find a narrower path). Explain why the scope is large before proceeding.
- **Search the codebase before creating new files.** An existing utility, test helper, or component may already do what you need. Duplication is a common agent failure mode.

## Error recovery

- **When a fix attempt fails, do not repeat the same approach.** If your first attempt at fixing a test failure or build error doesn't work, stop and analyze *why* it failed before trying again. Two failed attempts at the same approach means the approach is wrong.
- **After two failed attempts, reframe the problem.** Step back, re-read the error and the relevant code, and explain what you've tried and why it didn't work. Propose a fundamentally different approach before continuing.
- **Do not suppress errors to make tests pass.** If a test fails, fix the root cause. Do not add try/catch, ignore annotations, or skip directives to hide failures.

## Working memory

- **Keep the task definition visible.** If working from a spec, re-read the relevant section before each sub-task. Do not rely on your memory of what the spec said.
- **When context is long, summarize your plan before executing.** State what you're about to do in 2-3 sentences. This catches misunderstandings before they become wrong code.

## When to use me

This skill is loaded automatically by the `engineer` agent and all implementation-oriented agents. It should also be used by any agent that modifies files or runs commands.
