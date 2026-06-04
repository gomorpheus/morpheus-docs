---
title: Architecture Overview
type: context
status: active
created: 2026-06-04
tags: [imported, architecture]
---

## Project Structure

- `<harness>/commands/` — Slash command definitions (workflows like /design, /deliver, /diagnose)
- `<harness>/agents/` — Specialized agent roles (feature-delivery-lead, debug-investigator, etc.)
- `<harness>/skills/` — Domain-specific knowledge and patterns (each skill is a subdir with SKILL.md)
- `.hero/planning/` — Active specs being worked on
- `.hero/specs/` — Completed specs (archive)
- `.hero/knowledge/` — Project knowledge base (conventions, decisions, context)
- `.hero/hero.json` — Project configuration

Your harness may expose the agent/command/skill directories under its own prefix (`.claude/`, `.opencode/`, `.cursor/`, etc.) as symlinks back to the canonical paths above. Edit only the canonical files — harness directories are views.

## Project structure

Languages: JavaScript, Python

Key directories:
- `_build/`
- `_static/`
- `_templates/`
- `administration/`
- `backups/`
- `diagrams/`
- `getting_started/`
- `images/`
- `infrastructure/`
- `integration_guides/`
- `library/`
- `linked_files/`
- `monitoring/`
- `operations/`
- `personas/`
- `provisioning/`
- `release_notes/`
- `security/`
- `shared/`
- `tools/`
- `troubleshooting/`
- `z_in_progress/`

<!-- Imported from: AGENTS.md -->
