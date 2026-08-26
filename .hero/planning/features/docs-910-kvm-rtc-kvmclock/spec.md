---
title: "9.1.0 Docs: KVM RTC Catchup and kvmclock"
slug: docs-910-kvm-rtc-kvmclock
type: feature
status: planning
horizon: now
tags: [9.1.0, docs]
priority: 4
jira: MORPH-15231
---

# 9.1.0 Docs: KVM RTC Catchup and kvmclock

## Summary

Document the libvirt XML configuration change: RTC clock mode set to "catchup" with kvmclock enabled for Linux guests, and clock set to "localtime" for Windows guests. This improves guest time synchronization with the host.

## Acceptance Criteria

1. Document the behavioral change in the Guest OS Notes section: Linux guests now use kvmclock with RTC catchup mode for host time sync.
2. Document that Windows guests use localtime instead of UTC for the clock offset.
3. Note this is automatic (no user configuration required) and applies to new and restarted VMs.
4. Document any impact on live migration or snapshot/restore time drift scenarios.

## Sources

- Jira: MORPH-15231
