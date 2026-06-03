---
name: implementation-principles
description: Shared implementation guidance for making minimal, correct, maintainable code changes that fit existing systems.
compatibility: opencode
metadata:
  audience: engineers
  purpose: implementation-guidance
---
## What I do

Provide shared implementation guidance for execution-oriented agents.

## Core principles

- Understand the existing code before changing it.
- Make the smallest correct change that satisfies the requirement.
- Preserve project conventions unless they are clearly harmful.
- Prefer direct, maintainable code over cleverness or indirection.
- Avoid introducing abstractions without a concrete need.
- Keep scope tight and avoid opportunistic rewrites.

## Practical behavior

- Identify the smallest set of files and components that need to change.
- Reuse existing utilities, patterns, and boundaries when appropriate.
- If the requested design does not fit the actual code cleanly, say so and adjust pragmatically.
- Keep new names, helpers, and layers to a minimum.
- Consider operational consequences, not just compilation success.

## When to use me

Use this skill for nearly all coding tasks that turn requirements or plans into concrete code changes. Pair with `agent-reliability` for verification and self-correction rules.
