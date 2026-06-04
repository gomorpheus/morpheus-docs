---
title: "Catch-Up: Getting Started"
type: feature
slug: catchup-getting-started
status: planning
priority: high
horizon: now
parent: docs-catchup-812
---

# Catch-Up: Getting Started

## Purpose

Sync the `getting_started/` section with the 8.1.2 Enterprise portal content.

## Key Gaps to Investigate

- **Capacity and Planning** — new page in portal, may not exist in repo
- **Core Functionality** section: Morpheus Discovery, Agent docs (expanded), Communication Data, VMware Support Statement
- **Additional Configuration**: Data Encryption, IPv6, logback config — may be new or updated
- **Installation**: verify 3-Node HA and Full HA docs are current
- **Upgrades & Maintenance**: Scaling Morpheus Nodes, UI war files, morpheus-ctl tips

## Scope

- `getting_started/` directory
- Compare portal TOC against repo structure
- Add missing pages, update stale content

## Acceptance Criteria

- [ ] All portal pages under "Getting Started" have corresponding RST files
- [ ] Content matches 8.1.2 published state
- [ ] New pages (Capacity & Planning, Core Functionality) added if missing
