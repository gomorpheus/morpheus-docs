---
title: "9.1.0 Release Notes & Documentation Updates"
slug: docs-910-release-notes
type: initiative
status: planning
horizon: now
tags: [9.1.0, release-notes, documentation]
priority: 1
jira: [MORPH-13232, MORPH-13190, MORPH-13191]
---

# 9.1.0 Release Notes & Documentation Updates

## Summary

Master initiative tracking all documentation updates for the Morpheus 9.1.0 release (target: 2026-08-31). Coordinates release notes, new feature documentation, and bug fix documentation.

## Child Initiatives (69 total, excluding SDN)

See all `docs-910-*` initiatives in `.hero/planning/initiatives/`. Key groupings:

### HVM / VM Essentials (UBS)
- docs-910-hvm-network-plugin, docs-910-virtswitch-port-groups, docs-910-virtswitch-networks
- docs-910-host-profiles, docs-910-hvm-host-backup-restore, docs-910-vme-bulk-operations
- docs-910-cross-cluster-live-migration, docs-910-combined-live-migration, docs-910-migration-concurrency
- docs-910-vnic-connect-disconnect, docs-910-vm-shutdown-options, docs-910-advanced-reconfigure
- docs-910-affinity-placement-view, docs-910-affinity-rules, docs-910-linked-clones
- docs-910-datastore-maintenance-mode, docs-910-storage-drs, docs-910-storage-io-control
- docs-910-rdm-disks, docs-910-storage-migration-snapshot-guard
- docs-910-legacy-os-support, docs-910-vm-console-hvm, docs-910-vdisk-encryption
- docs-910-cpu-ready-metric, docs-910-vme-additional-metrics, docs-910-gpu-metrics
- docs-910-kv-labels, docs-910-advanced-list-management, docs-910-hvm-ubuntu-2604

### Monitoring & Administration
- docs-910-perf-charts-iops, docs-910-monitoring-time-ranges, docs-910-native-alerting
- docs-910-log-rotation-gui, docs-910-vme-log-settings, docs-910-action-logging
- docs-910-readonly-appliance-settings, docs-910-qemu-guest-agent

### Storage & Backup
- docs-910-alletra-replication-phase2, docs-910-unified-file-phase2, docs-910-veeam-hvm

### BMaaS / Bare Metal
- docs-910-bmaas-hardening, docs-910-bmaas-pxe-boot, docs-910-bfs-brownfield-import, docs-910-bm-multi-vlan

### HKS / Kubernetes
- docs-910-hks-pco-lite, docs-910-hks-enhancements, docs-910-hks-package-updates
- docs-910-hks-gateway-api, docs-910-hks-hybrid-layout

### Security
- docs-910-stig-morpheus-fips, docs-910-stig-hvmos-fips

### PCO / Platform
- docs-910-pco-phase2, docs-910-pco-rollback, docs-910-pco-host-management
- docs-910-morpheus-advanced, docs-910-approval-framework
- docs-910-system-updates, docs-910-vme-update-mechanism, docs-910-swap-primary-network

### Other
- docs-910-hvmcli, docs-910-aruba-cx-support-bundle, docs-910-plugin-readme
- docs-910-password-management, docs-910-import-existing-system, docs-910-vgpu-slicing
- docs-910-olvm-stateless, docs-910-history-prior-90, docs-910-ubs-small-defects

## Scope

### Release Notes (release_notes/9_1_0.rst)
- New features section (populated from epics)
- Bug fixes (from MORPH-13190)
- Regressions addressed (from MORPH-13191)
- Appliance & agent updates
- Compatibility table updates

### Documentation Updates (MORPH-13232)
- All new feature pages referenced from child initiatives
- Updated navigation for new sections
- Cross-references from existing pages to new content

## Sources

- Jira Epics: MORPH-13232, MORPH-13190, MORPH-13191
- Release target: Morpheus 9.1.0 (2026-08-31)
