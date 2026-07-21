---
type: feature
status: delivering
horizon: now
tags: [documentation, hvm, cpu, performance, field-feedback]
parent: docs-field-feedback-improvements
---

# Host CPU Passthrough Guide

## Objective

Document when to use `host-passthrough` CPU mode versus not using it.

## Acceptance Criteria

1. Explains what host-passthrough does (exposes host CPU features directly to guest)
2. Documents the tradeoff: performance vs live migration compatibility
3. Clarifies when to use it (single-host, homogeneous clusters, specific CPU feature requirements)
4. Clarifies when NOT to use it (heterogeneous clusters, live migration priority)
5. Documents how to configure it in Morpheus (instance type, virtual image, or cluster-level setting)

## Changes

- `infrastructure/clusters/hvm/` — Add CPU passthrough section (or new file)
