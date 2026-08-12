---
title: "Document the process of adding network interfaces to netplan and surfacing to the HVM cluster in the UI"
slug: docs-morph-3257-hvm-netplan-interfaces
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, networking, netplan, cli]
tracker_id: MORPH-3257
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---
# Document the process of adding network interfaces to netplan and surfacing to the HVM cluster in the UI

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3257

Jira description (verbatim):

> Document the process of adding network interfaces to netplan and surfacing to the HVM cluster in the UI. Show how to do this using the CLI utility to show off that functionality.

Related host preparation and network configuration exist in `getting_started/installation/hvm_host_prep.rst`, `infrastructure/clusters/hvm/virtual_switches.rst`, and `infrastructure/clusters/hvm/managing_hosts.rst`.

## Goal

Provide a validated procedure to add a host NIC through Netplan, safely apply it, trigger supported HVM discovery, and verify that the interface appears in cluster UI inventory.

## Kickoff

Document safe Netplan interface addition and supported HVM discovery using the current CLI utility.

**Status:** planning — related host and switch pages exist; utility name, commands, and refresh behavior need confirmation.

**Pick up at:** perform the change on a supported host while capturing rollback steps, CLI output, and UI state.

→ `.hero/planning/features/docs-morph-3257-hvm-netplan-interfaces/spec.md`

**Files:** `getting_started/installation/hvm_host_prep.rst`, `infrastructure/clusters/hvm/virtual_switches.rst`, `infrastructure/clusters/hvm/managing_hosts.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Place OS-level preparation in host prep and link from virtual-switch management. Use Netplan validation/rollback and only the officially supported HVM CLI/discovery mechanism.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` with Netplan preflight, edit, safe apply, rollback, and interface verification.
2. Update `infrastructure/clusters/hvm/virtual_switches.rst` with the supported CLI discovery/refresh and UI verification sequence.
3. Update `infrastructure/clusters/hvm/managing_hosts.rst` with a concise interface-inventory cross-reference.

## Acceptance Criteria

- WHEN an administrator adds a physical interface THE DOCUMENTATION SHALL provide safe Netplan validation, application, and rollback steps.
- WHEN the interface is available to the OS THE DOCUMENTATION SHALL show the supported CLI action and where the interface appears in HVM UI.
- IF the CLI utility or command is not confirmed THEN delivery SHALL not invent it.

## Boundaries

No network architecture design, unsupported direct database updates, bonding tutorial, or remote-change procedure without rollback safeguards.

## Risks

- **Blocker:** Jira does not name the CLI utility or supported command.
- Applying Netplan remotely can sever management connectivity.

## Validation

Test add/apply/discover/remove on a supported host, validate rollback from a bad configuration, run `make build`, and peer-review with HVM networking engineering.
