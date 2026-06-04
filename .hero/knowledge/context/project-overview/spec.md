---
title: Project Overview
type: context
status: active
created: 2026-06-04
tags: [auto-generated, project-scan]
---

## What is morpheus-docs

This is the document repository for [Morpheus Data](https://www.morpheusdata.com "Morpheus Homepage").  All content is automatically published to the [Morpheus Docs Site](https://docs.morpheusdata.com "Morpheus Docs").

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | JavaScript |
| Language (secondary) | Python |
| Build | Make (`Makefile`) |
| Package manager | pip |

## Package Organization

- `_build/` — contains: doctrees, html
- `_ext/`
- `_images/`
- `_scraped/` — contains: sd00007732en_us, sd00007735en_us
- `_static/` — contains: storageCalculator
- `_templates/`
- `administration/` — contains: health, identity_sources, integrations, plans_pricing, +6 more
- `backups/` — contains: integrations
- `diagrams/`
- `getting_started/` — contains: additional, appliance_setup, functionality, guides, +3 more
- `images/` — contains: AwsGuideImages, administration, advanced, apps, +28 more
- `infrastructure/` — contains: clouds, clusters, compute, groups, +6 more
- `integration_guides/` — contains: Automation, Backups, Clouds, Containers, +11 more
- `library/` — contains: automation, blueprints, integrations, options, +3 more
- `linked_files/`
- `monitoring/`
- `operations/` — contains: report_types
- `personas/`
- `provisioning/` — contains: apps, catalog, code, concepts, +4 more
- `release_notes/`
- `security/`
- `shared/`
- `tools/` — contains: ai, migrations
- `troubleshooting/`
- `z_in_progress/`

## Project Structure

## Documentation

- `README.md`

## Architecture Summary

Detailed architecture documentation is available in the architecture-overview knowledge entry.

- `<harness>/commands/` — Slash command definitions (workflows like /design, /deliver, /diagnose)
- `<harness>/agents/` — Specialized agent roles (feature-delivery-lead, debug-investigator, etc.)
- `<harness>/skills/` — Domain-specific knowledge and patterns (each skill is a subdir with SKILL.md)
- `.hero/planning/` — Active specs being worked on
- `.hero/specs/` — Completed specs (archive)
- `.hero/knowledge/` — Project knowledge base (conventions, decisions, context)
-…

## Current Gaps

- **No tests** — no test files or test framework detected
- **No CI/CD** — no CI provider detected
- **No linters** — no linter or formatter configuration detected

<!-- Add project-specific context here:
- Architecture overview and key design patterns
- Deployment topology (cloud provider, regions, etc.)
- Important environment variables
- Third-party service dependencies
-->
