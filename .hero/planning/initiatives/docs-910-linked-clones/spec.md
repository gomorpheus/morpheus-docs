---
title: "9.1.0 Docs: Linked Clones for VMware and HVM"
slug: docs-910-linked-clones
type: initiative
status: completed
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-9719
completed_at: 2026-08-19T14:52:23Z
---

# 9.1.0 Docs: Linked Clones for VMware and HVM

## Summary

Document the shared VMware and HVM linked clone workflow for Morpheus 9.1.0, including source guest preparation and platform-specific dependencies.

## Scope

- Creating linked clones
- Preparing Windows and Linux source guests
- Configuring the resulting Virtual Image
- Storage efficiency benefits
- Limitations and constraints
- Managing clone chains

## Acceptance Criteria

1. Verify the UI labels and document `More` > `Create Linked Clone` from an Instance snapshot on the **Backups** tab.
2. State that the action creates a linked clone Virtual Image record for later provisioning rather than immediately creating a VM.
3. Cover both VMware and HVM/KVM and link the shared workflow from snapshot, Virtual Image, HVM, and VDI documentation.
4. Provide Windows Sysprep and Linux cloud-init, machine identity, SSH host key, and persistent network-rule preparation guidance.
5. Explain source VM and snapshot dependencies, VMware resize limitations, and HVM host/storage migration constraints.

## Sources

- Jira Epic: MORPH-9719
