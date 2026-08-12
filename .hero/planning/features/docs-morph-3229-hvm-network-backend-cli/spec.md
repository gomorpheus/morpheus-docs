---
title: "Document through CLI screens what is happening on the backend when various HVM networking constructs are added"
slug: docs-morph-3229-hvm-network-backend-cli
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, networking, cli, troubleshooting]
tracker_id: MORPH-3229
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Document through CLI screens what is happening on the backend when various HVM networking constructs are added

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3229

Jira description (verbatim):

> Document through CLI screens what is happening on the backend when various HVM networking constructs are added

The current `infrastructure/clusters/hvm/hvm_networks.rst` already describes backend objects for five network types; `virtual_switches.rst` and `troubleshooting.rst` contain adjacent host-level guidance.

## Goal

Add reproducible, read-only host CLI verification for layout 2.0 Virtual Switches. Explicitly distinguish this supported ``hvmcli`` surface from the five legacy UI/plugin network types, which do not have a stable one-to-one ``hvmcli`` representation.

## Kickoff

Extend existing HVM network documentation with verified read-only CLI evidence for layout 2.0 Virtual Switches without implying that legacy network types map to ``hvmcli``.

**Status:** planning — backend prose exists; exact commands and safe output examples need lab capture.

**Pick up at:** verify the layout 2.0 ``virtswitch`` and ``network`` read-only commands against product source and rendered documentation.

→ `.hero/planning/features/docs-morph-3229-hvm-network-backend-cli/spec.md`

**Files:** `infrastructure/clusters/hvm/hvm_networks.rst`, `infrastructure/clusters/hvm/virtual_switches.rst`, `infrastructure/clusters/hvm/troubleshooting.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Document only the stable layout 2.0 read-only command contract. Retain the legacy network-type descriptions as UI/plugin concepts and avoid invented mappings to layout 2.0 objects.

## Changes

1. Retain `infrastructure/clusters/hvm/hvm_networks.rst` as the legacy UI/plugin network reference; do not claim its five network types map to `hvmcli`.
2. Update `infrastructure/clusters/hvm/virtual_switches.rst` with layout 2.0 read-only `virtswitch` and `network` verification.
3. Cross-link the canonical command reference from `tools/hvmcli/network.rst`.

## Acceptance Criteria

- WHEN a layout 2.0 Virtual Switch is created THE DOCUMENTATION SHALL show the stable read-only ``hvmcli virtswitch`` and ``hvmcli network`` commands used to verify it.
- THE DOCUMENTATION SHALL distinguish the five legacy UI/plugin network constructs from layout 2.0 Virtual Switches and SHALL NOT claim a one-to-one ``hvmcli`` mapping for them.
- THE DOCUMENTATION SHALL label variable output and sanitize host-specific values.
- IF a command can mutate networking THEN THE DOCUMENTATION SHALL exclude it from verification steps.

## Boundaries

No CLI utility implementation, unsupported manual backend modification, packet-capture tutorial, or network plugin redesign.

## Risks

- Command output may vary by HVM layout and plugin version.
- Unverified CLI examples can encourage unsupported manual remediation.

## Validation

Compare the documented commands with `HvmcliVirtswitch`, `HvmcliUtility`, and their command-construction tests in the product source, verify the rendered cross-links, and run `make build`.
