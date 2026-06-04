---
title: Development Workflow & Commands
type: context
status: active
created: 2026-06-04
tags: [imported, commands, dev-workflow]
---

## CLI Commands

These are run in the terminal, not as slash commands:
- `hero status` — workspace state and active specs
- `hero search <query>` — find specs by keyword
- `hero snapshot` — render the project-shape rollup (surfaces, stages, recent activity, risks)
- `hero sync import` — import issues from tracker as spec scaffolds
- `hero sync pull <slug>` — sync spec status from tracker
- `hero note <slug>` — quick note capture
- `hero check` — health check
- `hero peer list` — list registered sibling repos with reachability + manifest status
- `hero peer show <alias>` — inspect one peer (manifest contents, in-flight handoffs)
- `hero peer call <alias> --mode=advisory "..."` — ask peer's Hero a question (no writes on peer)
- `hero peer call <alias> --mode=spec-out "..."` — have peer's Hero design a spec natively on its side
- `hero handoff <spec> <alias>` — async-drop a local spec on peer's queue
- `hero handoff status` / `hero handoff accept <spec>` — track handoffs across the boundary
- `hero admin repos add <alias> <path>` — register a sibling repo as a peer (one-time setup)

## Build

```bash
make build
```

## Test

```bash
make test
```

<!-- Imported from: AGENTS.md -->
