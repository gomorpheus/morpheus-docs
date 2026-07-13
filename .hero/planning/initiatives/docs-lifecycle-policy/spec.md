---
title: "Component Lifecycle & Support Policy Documentation"
slug: docs-lifecycle-policy
type: feature
status: planning
horizon: now
tags: [9.1.0, lifecycle, support-policy, compatibility, UBS]
priority: 1
jira: MORPH-7920
---

# Component Lifecycle & Support Policy Documentation

## Summary

Provide clear documentation covering the release cadence, component compatibility, support windows, and upgrade paths for all platform components. Enterprise customers need this to plan patching cycles, upgrades, and long-term platform operations.

## Problem

There is no consolidated documentation explaining:
- How often releases ship and what the versioning scheme means
- Which component versions are compatible with each other
- How long each release is supported
- What upgrade paths are valid

## Scope

This work touches multiple doc sections. Proposed locations:

### 1. Release Cadence & Versioning (`release_notes/lifecycle.rst` — NEW)

Document for all components:
- **Manager (Morpheus appliance):** Major (annual), Minor (quarterly), Patch (as needed)
- **HVM ISO / Host OS:** Release frequency, tied to Manager minors
- **Agent:** Ships with each Manager release, backward compatible N-2
- **Plugins (Alletra, Aruba CX, etc.):** Independent release cycle, compatibility declared per plugin version

### 2. Component Compatibility Matrix (`release_notes/compatibility.rst` — EXPAND)

Expand existing compatibility page with a matrix showing supported combinations of:
- Manager version ↔ HVM Host OS version
- Manager version ↔ Agent version
- Manager version ↔ Plugin versions (Alletra MP, Aruba CX, etc.)
- HVM Host OS ↔ Ubuntu base version ↔ Kernel version
- Minimum upgrade-from version for each release

### 3. Support Policy (`release_notes/support_policy.rst` — NEW)

Document:
- **Support model:** Define which releases are actively supported (e.g., N-1: current + previous minor)
- **Duration:** Each minor release supported for X months from GA
- **Security patches:** Available for all supported releases
- **End-of-support timelines:** Table with projected dates
- **Extended support:** Whether available and under what terms
- **Ubuntu OS lifecycle:** Relationship to Ubuntu LTS upstream (24.04 supported until 20xx)

### 4. Upgrade Policy (expand `release_notes/compatibility.rst` upgrade section + `infrastructure/clusters/hvm/upgrading.rst`)

Document:
- Supported upgrade paths (e.g., 8.x → 9.0 requires intermediate stop at 8.1.x)
- Rolling vs non-rolling upgrade availability per version hop
- Downtime expectations per upgrade type
- HVM cluster layout upgrade (1.2 → 1.3) as a separate operation from Manager upgrade
- Agent upgrade policy (automatic vs manual, compatibility window)

## Existing Content to Integrate

| Location | Current Content | Action |
|---|---|---|
| `release_notes/compatibility.rst` | Cloud integration versions, upgrade path table | Expand with component matrix |
| `release_notes/upgrade_table2.rst` | Upgrade path table (version → version) | Keep, link from new lifecycle page |
| `infrastructure/clusters/hvm/upgrading.rst` | HVM cluster upgrade procedures | Add cross-reference to lifecycle policy |
| `getting_started/installation/overview.rst` | Component list | Cross-reference compatibility |

## Acceptance Criteria

- [ ] Release cadence documented for Manager, HVM ISO, Agent, and Plugins
- [ ] Component compatibility matrix with supported version combinations
- [ ] Support policy with defined model (confirm N-1 or other with product management), duration, and EOL dates
- [ ] Upgrade paths clearly documented with intermediate version requirements
- [ ] Cross-references from existing upgrade/compatibility pages to new content
- [ ] No VMware-specific trademarked terminology

## Notes

- The actual support durations and EOL dates need input from product management
- Plugin compatibility may need per-plugin release notes or a separate matrix
- Ubuntu LTS lifecycle should reference Canonical's published dates

## Kickoff

You are delivering documentation for the Morpheus platform lifecycle and support policy (MORPH-7920). The goal is to create clear documentation that enterprise customers can use to plan patching, upgrades, and long-term operations.

Start by creating `release_notes/lifecycle.rst` with the release cadence section, then expand `release_notes/compatibility.rst` with the component matrix, then create `release_notes/support_policy.rst`. Cross-reference from existing pages. Check with product management for actual support window durations before publishing EOL dates.
