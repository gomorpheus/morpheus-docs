---
title: "9.1.0 Docs: Linked Clones in HVM"
slug: docs-910-linked-clones-hvm
type: feature
status: planning
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-9719
---

# 9.1.0 Docs: Linked Clones in HVM

## Summary

Document HVM native cloning capabilities: full clone, linked clone (shared base disk with delta disks), and instant clone (clone from running VM). Replaces the previous snapshot+reprovisioning workflow.

## Acceptance Criteria

1. Distinguish full clone, linked clone, and instant clone with clear definitions and use cases (storage efficiency, provisioning speed, VDI scenarios).
2. Document how to initiate each clone type from the UI and API, including consistent behavior between UI and API.
3. Document that linked clones use a shared base disk with delta disks, resulting in reduced storage consumption and faster provisioning.
4. Document constraints: no duplicate CD-ROM attachments, no IP conflicts, correct device mapping preservation.
5. Document the relationship between linked clones and snapshots (Import as Image / Clone to Image workflows).
6. Document any known limitations (e.g., instant clone availability, VM state requirements).

## Sources

- Jira Epic: MORPH-9719
