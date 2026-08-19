---
title: "Tenant Hierarchy and Supported Nesting"
slug: docs-multitenancy-hierarchy
type: feature
status: planning
size: medium
horizon: next
tags: [documentation, multitenancy, tenants, hierarchy]
parent: docs-multitenancy-guide
relates-to: [docs-morph-11023-parent-tenant-field]
created: 2026-08-12
---

# Tenant Hierarchy and Supported Nesting

## Context

`administration/tenants/tenants.rst` documents the **Parent Tenant** creation field, but the surrounding conceptual content still presents a flat Master Tenant-to-Subtenant model. No page states whether arbitrary N-level nesting is supported or documents its depth, lifecycle, navigation, and ownership limitations.

## Goal

Establish and document the supported tenant hierarchy model, including maximum depth, ownership and access relationships, creation permissions, reparenting behavior, lifecycle effects, scale limits, and terminology.

## Approach

Investigate before editing. Use `../morpheus-ui` implementation and tests where available, then obtain product confirmation for limits or security behavior that cannot be established from source. Treat each operation independently because the code contains both recursive descendant checks and direct-child-only checks. Add a topology diagram or concrete three-level example only after the model is verified.

## Changes

1. Audit the product implementation, API schema, tests, and approved product guidance for tenant parent-child relationships and hierarchy limits.
   - Review `PermissionService.canAccessTenant` and `loadTenantQueryOptions` for recursive descendant-aware reads.
   - Review UI and API `AccountsController`, `AccountUsersController`, `MorpheusSwitchUserFilter`, and Tenant datasets for direct-child restrictions.
   - Determine whether the 10-iteration ancestry guard is a supported depth limit or only circular-reference protection.
2. Update `administration/tenants/tenants.rst` with the canonical hierarchy model, supported depth, creation context, lifecycle rules, and limitations.
3. Reconcile flat two-level statements in `administration/tenants/configuring_multi_tenancy.rst` and `getting_started/guides/tenancy.rst` with verified nested behavior.
4. Add a hierarchy example that distinguishes the Master Tenant, ancestor, direct parent, child, descendant, and sibling Tenants.

## Acceptance Criteria

- THE DOCUMENTATION SHALL state whether N-level nesting is supported and identify the supported maximum depth or lack of a published fixed maximum.
- THE DOCUMENTATION SHALL identify who can create and administer a child Tenant at each supported level.
- THE DOCUMENTATION SHALL explain whether existing Tenants can be reparented.
- THE DOCUMENTATION SHALL explain disable and delete behavior for a Tenant that has descendants.
- THE DOCUMENTATION SHALL identify applicable tenant-count or hierarchy scale limits.
- THE DOCUMENTATION SHALL distinguish operations that traverse all descendants from operations restricted to direct children.
- IF behavior is unverified THEN THE DOCUMENTATION SHALL identify it as requiring confirmation rather than presenting an inferred rule.

## Boundaries

- Resource inheritance details belong to `docs-multitenancy-resource-inheritance`.
- Identity, delegated administration, and reporting details belong to `docs-multitenancy-administration-limitations`.
- Do not change the product or propose a new hierarchy model.

## Risks

The Parent Tenant field proves that a parent relationship exists but does not prove unlimited depth, recursive inheritance, or complete delegated administration. `PermissionService` has a parent-chain traversal guard after 10 iterations, but that alone is not evidence of a published ten-level support limit. Published claims must be source-backed or approved by a technical owner.

## Validation

- Exercise creation and lifecycle operations in at least a Master -> child -> grandchild topology when a suitable environment is available.
- Compare UI results with API behavior and implementation tests.
- Build the affected Sphinx pages and review terminology across all three canonical tenant guides.

## Kickoff

Determine the actual supported tenant hierarchy before rewriting the conceptual model.

**Pick up at:** reconcile recursive `PermissionService` ancestry checks with direct-child Tenant controller, dataset, user-management, and impersonation paths; then record confirmed depth and per-operation limits before editing docs.

-> `.hero/planning/features/docs-multitenancy-hierarchy/spec.md`
