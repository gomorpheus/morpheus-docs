---
title: "Multi-Tenant Resource Scoping and Policy Inheritance"
slug: docs-multitenancy-resource-inheritance
type: feature
status: planning
size: medium
horizon: next
tags: [documentation, multitenancy, resources, policies]
parent: docs-multitenancy-guide
depends-on: [docs-multitenancy-hierarchy]
created: 2026-08-12
---

# Multi-Tenant Resource Scoping and Policy Inheritance

## Context

Current documentation explains resource sharing primarily as a Master Tenant-to-Subtenant relationship. It does not state how explicit Tenant permissions, ownership, assignment, and policy behavior traverse a deeper hierarchy or where propagation stops. Broad resource `visibility` is a separate exposure control and must not be used as the hierarchy filter because it can include Tenants outside the intended branch.

## Goal

Provide a verified matrix for explicit resource permissions, ownership, assignment, and inherited controls across direct parents, children, descendants, ancestors, and siblings.

## Approach

Use the canonical hierarchy established by `docs-multitenancy-hierarchy`. Test each resource class independently; do not assume all objects use the same recursive access rules. Model scoped access through `ResourcePermission`, owner/account assignment, Role resource permissions, and endpoint-specific tenant filters. Mention broad visibility only to distinguish it from and warn against branch-scoped access.

## Changes

1. Inventory tenant-scoped resources and controls documented across Clouds, Groups, Networks, Datastores, Images, Library items, Workflows, Roles, Policies, Plans, and Pricing.
2. Trace object-specific code in `../morpheus-ui`, including `PermissionService.updateTenantPermissions`, `TenantPermissionsTrait`, `RoleService`, and each resource service's query filters.
3. Verify explicit Tenant permission, ownership, assignment, Role grant, and inherited behavior for parent-child and ancestor-descendant relationships.
4. Update `administration/tenants/configuring_multi_tenancy.rst` with a capability matrix and supported workflows.
5. Correct or cross-link resource-specific pages whose tenancy language conflicts with the canonical matrix.

## Acceptance Criteria

- THE DOCUMENTATION SHALL distinguish ownership, explicit Tenant access, use, edit, and reassignment permissions.
- THE DOCUMENTATION SHALL state whether each covered resource propagates only to direct children or recursively to descendants.
- THE DOCUMENTATION SHALL explain sibling isolation and ancestor visibility.
- THE DOCUMENTATION SHALL identify policy, quota, pricing, and Role inheritance boundaries.
- THE DOCUMENTATION SHALL NOT recommend broad resource visibility as a way to target one tenant hierarchy branch.
- THE DOCUMENTATION SHALL identify the explicit permission or assignment mechanism used for every documented resource class.
- IF resource classes behave differently THEN THE DOCUMENTATION SHALL describe them separately rather than generalizing.

## Boundaries

- Tenant creation and hierarchy lifecycle are covered by `docs-multitenancy-hierarchy`.
- Identity, login, and delegated administration are covered by `docs-multitenancy-administration-limitations`.

## Risks

Existing text uses "all Tenants" and "Subtenants" ambiguously. Those phrases can overstate recursive access in a nested hierarchy unless each resource path is verified. `PermissionService.resourceAccounts` and `updateTenantPermissions` restrict non-root management to the owner and direct children, while some object queries also admit broadly visible resources; conflating these paths could expose more than the intended hierarchy branch.

## Validation

- Test representative resources in at least three hierarchy levels.
- Confirm matrix results against implementation or approved product guidance.
- Build all changed Sphinx pages and validate cross-references.

## Kickoff

Build a source-backed matrix for explicit tenant permissions, ownership, assignment, Role grants, and policy behavior through the verified hierarchy. Do not use broad visibility as the branch filter.

-> `.hero/planning/features/docs-multitenancy-resource-inheritance/spec.md`
