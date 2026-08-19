---
title: "Procedure for optimization in windows vm to be done for 10Gbps speed between vm's on different cluster hosts."
slug: docs-morph-7129-windows-network-throughput
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, windows, networking, performance]
tracker_id: MORPH-7129
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---
# Procedure for optimization in windows vm to be done for 10Gbps speed between vm's on different cluster hosts.

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7129

> We have tested below optimization on windows vm’s after which optimal throughput for Windows OS (10GB throughput) achieved between vm’s across different cluster hosts in same cluster.
>
> We need to document the same.
>
> Procedure:-
>
> Optimizations applied for optimal throughput for Windows OS (10GB throughput)  
> Disable-NetAdapterLso -Name "_"_  
> _Disable-NetAdapterChecksumOffload -Name "_"  
> Enable-NetAdapterRss -Name "\*"  
> netsh int tcp set global autotuninglevel=normal  
> netsh int tcp set global rss=enabled
>
> HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters  
> MaxUserPort=65534 (DWORD)  
> TcpTimedWaitDelay=30 (DWORD)

## Goal
Publish a support-reviewed Windows guest networking optimization procedure with prerequisites, exact commands, rollback guidance, and measured scope, without promising universal 10 Gbps throughput.

## Kickoff
Use `infrastructure/clusters/hvm/guest_os_notes.rst` as the canonical guest-specific location and cross-link from `infrastructure/clusters/hvm/hvm_networks.rst` only if needed. Before writing, obtain the tested Windows versions, NIC model/driver, HVM release, workload methodology, command corrections, reboot requirements, risks, and rollback steps. The Jira commands and registry values are unverified input, not publication-ready truth. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Add a qualified troubleshooting/optimization subsection to existing Windows guest guidance. Separate measured test results from supported guarantees.

## Changes
1. Add reviewed prerequisites, commands, registry changes, verification, and rollback to `infrastructure/clusters/hvm/guest_os_notes.rst`.
2. Add a concise cross-reference from `infrastructure/clusters/hvm/hvm_networks.rst` if readers troubleshooting inter-host throughput would otherwise miss it.

## Acceptance Criteria
- WHEN a supported Windows guest has low inter-host throughput THE DOCUMENTATION SHALL provide the approved diagnostic and optimization sequence.
- THE DOCUMENTATION SHALL identify tested versions, required privileges, side effects, restart requirements, and rollback steps.
- THE DOCUMENTATION SHALL not guarantee 10 Gbps outside the approved test conditions.
- IF any Jira command is malformed or unsupported THEN THE DOCUMENTATION SHALL exclude it until corrected by Engineering.

## Boundaries
No product performance change, Linux tuning, or general network benchmark guide.

## Risks
These settings can reduce offload behavior and alter system-wide TCP behavior. Delivery is blocked pending Windows/HVM Engineering validation.

## Validation
Reproduce the approved test, verify commands and rollback on supported Windows versions, build docs, and obtain performance/support sign-off.
