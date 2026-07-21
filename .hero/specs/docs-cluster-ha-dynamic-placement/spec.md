---
type: feature
status: delivering
horizon: now
tags: [documentation, hvm, cluster, ha, field-feedback]
parent: docs-field-feedback-improvements
---

# Cluster HA & Dynamic Placement Details

## Objective

Expand documentation on cluster HA behavior and provide more detail on how Dynamic Placement makes decisions.

## Acceptance Criteria

1. Documents cluster HA behavior beyond the existing Pacemaker doc — what happens on host failure, VM restart order, fencing
2. Explains the Dynamic Placement algorithm: what metrics are evaluated, threshold calculations, and decision logic
3. Documents tunable parameters and their practical effect
4. Includes guidance on when to use conservative vs aggressive settings
5. Covers the relationship between HA, Dynamic Placement, and maintenance mode

## Changes

- `infrastructure/clusters/hvm/vm_placement.rst` — Expand Dynamic Placement algorithm details
- `infrastructure/clusters/hvm/` — Expand or add HA behavior documentation
