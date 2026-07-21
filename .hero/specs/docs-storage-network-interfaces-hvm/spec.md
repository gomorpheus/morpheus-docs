---
type: feature
status: delivering
horizon: now
tags: [documentation, hvm, networking, storage, field-feedback]
parent: docs-field-feedback-improvements
---

# Storage Network Interfaces for HVM

## Objective

Document the process and options for adding storage network interfaces to HVM hosts.

## Acceptance Criteria

1. Explains what "storage network interfaces" means in HVM context (dedicated NICs/VLANs for storage traffic)
2. Documents when to add them (iSCSI, NFS, FC-over-Ethernet)
3. Step-by-step configuration in Morpheus UI
4. Covers relationship with Virtual Switches and traffic separation

## Changes

- `infrastructure/clusters/hvm/` — Add or expand storage networking section
