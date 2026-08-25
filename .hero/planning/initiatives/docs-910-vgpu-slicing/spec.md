---
title: "9.1.0 Docs: NVIDIA vGPU Slicing"
slug: docs-910-vgpu-slicing
type: initiative
status: planning
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-5321
claimed_by: mcp-agent
claimed_at: 2026-08-24T08:54:42-04:00
---

# 9.1.0 Docs: NVIDIA vGPU Slicing

## Summary

Document NVIDIA vGPU slicing configuration and management for Morpheus 9.1.0.

## Scope

- vGPU slice profiles and configuration
- Assigning GPU slices to VMs
- Monitoring GPU slice utilization
- Supported GPU models and drivers

## Acceptance Criteria

1. Distinguish whole-GPU passthrough from NVIDIA SR-IOV vGPU VF slicing and exclude incomplete MIG/mdev workflows.
2. Document homogeneous and heterogeneous segmentation, Segment Type creation, and profile availability filtering.
3. Document NVIDIA vGPU Manager and guest-driver prerequisites without hard-coding an unapproved driver build.
4. Explain NVIDIA License System, Client Configuration Tokens, and Q-series/vWS, B-series/vPC, and A-series/vApps requirements as separate from Morpheus licensing.
5. Document Service Plan GPU Count and GPU Type behavior, including Any GPU, physical types, Segment Types, and pre-created VF reservation.
6. Document manual assignment, power disruption, placement, migration, maintenance, teardown, and capacity limitations.

## Sources

- Jira Epic: MORPH-5321
