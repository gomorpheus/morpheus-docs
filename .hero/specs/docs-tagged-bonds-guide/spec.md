---
type: feature
status: delivering
horizon: now
tags: [documentation, networking, hvm, field-feedback]
parent: docs-field-feedback-improvements
---

# Tagged Bonds Networking Guide

## Objective

Clearly document when and how to use tagged bonds (VLAN-tagged bond interfaces) — current docs are noted as "vague."

## Acceptance Criteria

1. Explains what tagged bonds are and when to use them vs other approaches
2. Provides concrete configuration examples
3. Compares tagged bonds with trunk ports, access ports, and untagged bonds
4. Includes use cases (separating VM traffic, storage traffic, migration traffic on a single bond)
5. Documents how this maps to Virtual Switch configuration in HVM

## Changes

- `infrastructure/clusters/hvm/virtual_switches.rst` — Expand tagged bond section with examples and use cases
