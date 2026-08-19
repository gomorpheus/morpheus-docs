---
title: "Kube-vip documentation - check for, add if not available"
slug: docs-morph-4163-hks-kube-vip
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hks, kubernetes, kube-vip, networking]
tracker_id: MORPH-4163
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:12Z
---
# Kube-vip documentation - check for, add if not available

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-4163

Jira description (verbatim):

> Kube-vip documentation - check for, add if not available

A repository search found no `kube-vip` documentation. HKS/Kubernetes cluster entry points include `infrastructure/clusters/clusters.rst`, `infrastructure/clusters/kubernetes.rst`, and `library/blueprints/clusterLayouts.rst`.

## Goal

Document the supported role of kube-vip in HKS, including when it is used, VIP prerequisites, configuration ownership, failover behavior, verification, and troubleshooting.

## Kickoff

Add missing kube-vip guidance for HKS after confirming the product-managed configuration and supported deployment modes.

**Status:** planning — no local kube-vip coverage was found; implementation details are unverified.

**Pick up at:** inspect a supported HKS cluster and confirm kube-vip ownership, fields, manifests, and failover behavior with engineering.

→ `.hero/planning/features/docs-morph-4163-hks-kube-vip/spec.md`

**Files:** `infrastructure/clusters/clusters.rst`, `infrastructure/clusters/kubernetes.rst`, `library/blueprints/clusterLayouts.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add a focused HKS page explaining product-supported operations rather than a generic upstream kube-vip tutorial. Link from relevant cluster configuration.

## Changes

1. `infrastructure/clusters/hks_kube_vip.rst` — Added code-evidenced purpose, supported provision types, VIP inputs, managed manifest behavior, verification, failover, and troubleshooting.
2. `infrastructure/clusters/clusters.rst` — Exposed the page in cluster navigation.
3. `infrastructure/clusters/kubernetes.rst` — Added the HKS kube-vip cross-reference.

## Acceptance Criteria

- WHEN HKS uses kube-vip THE DOCUMENTATION SHALL explain its supported purpose, prerequisites, configuration owner, and failover behavior.
- THE DOCUMENTATION SHALL provide non-destructive verification and troubleshooting steps.
- IF users must not edit generated manifests THEN THE DOCUMENTATION SHALL state that boundary explicitly.

## Boundaries

No upstream kube-vip installation guide, unsupported manifest customization, or general load-balancer documentation.

## Risks

- **Blocker:** Jira contains no architecture or configuration details.
- Upstream kube-vip behavior may differ from the HKS-managed implementation.

## Validation

Validate against a supported HKS cluster, test VIP failover and read-only checks, obtain HKS networking review, and run `make build`.
