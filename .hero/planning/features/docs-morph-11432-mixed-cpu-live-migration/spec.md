---
title: "DOCUMENTATION: Live migration needs VME cluster CPU model set to lowest CPU model within cluster hosts. "
slug: docs-morph-11432-mixed-cpu-live-migration
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, live-migration, cpu-compatibility]
tracker_id: MORPH-11432
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# DOCUMENTATION: Live migration needs VME cluster CPU model set to lowest CPU model within cluster hosts. 

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11432

The Jira states that mixed-generation VME cluster hosts require the cluster CPU model to be set to the lowest common model for live migration (example: EPYC-Genoa plus EPYC-Rome hosts use EPYC-Rome). Existing `vm_advanced_options.rst` says host-passthrough remains migratable across mixed generations, creating a direct documentation conflict requiring engineering resolution.

## Goal
Publish one verified CPU-compatibility rule for live migration and remove contradictory guidance.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11432-mixed-cpu-live-migration/spec.md`; reconcile `infrastructure/clusters/hvm/vm_advanced_options.rst` and `infrastructure/clusters/hvm/vm_migration.rst` only after HVM engineering confirms behavior.

## Approach
Reproduce/verify default, named-model, host-model, host-passthrough, and nested-virtualization cases before changing prescriptive text.

## Changes
1. Resolve the Jira-versus-current-doc conflict with HVM engineering and record the supported matrix in `infrastructure/clusters/hvm/vm_advanced_options.rst`.
2. Add the verified mixed-CPU prerequisite and example to `infrastructure/clusters/hvm/vm_migration.rst`, including the GUI path for cluster CPU model configuration.

## Acceptance Criteria
- WHEN a cluster contains mixed CPU generations THE SYSTEM SHALL state the verified CPU model configuration required for live migration.
- WHEN host-passthrough or nested virtualization changes the rule THE SYSTEM SHALL distinguish those cases.
- IF engineering cannot reconcile the conflict THEN THE SYSTEM SHALL block publication rather than preserve contradictory advice.

## Boundaries
No hypervisor configuration changes or universal CPU model recommendation beyond tested HVM behavior.

## Risks
Following the Jira literally may regress newer valid host-passthrough guidance.

## Validation
HVM engineering sign-off, representative mixed-generation migration test, contradiction search, build, and `make test`.
