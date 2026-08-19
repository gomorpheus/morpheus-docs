---
title: "Multi-Tenancy Documentation"
slug: docs-multitenancy-guide
type: initiative
status: planning
size: medium
horizon: next
tags: [documentation, multitenancy, tenants, enterprise]
relates-to: [docs-morph-11023-parent-tenant-field]
child:
  - docs-multitenancy-hierarchy
  - docs-multitenancy-resource-inheritance
  - docs-multitenancy-administration-limitations
created: 2026-08-12
---

# Multi-Tenancy Documentation

## Vision

Give Enterprise administrators an accurate model for designing and operating tenant hierarchies, including whether tenants can be nested to N levels, the supported depth and scale boundaries, how access is explicitly scoped at each level, and which capabilities remain limited to the Master Tenant or direct parent.

## Goal

Publish one coherent, code-backed multi-tenancy guide and limitations matrix that distinguishes recursively descendant-aware capabilities from direct-child-only operations and prevents broad resource visibility from being presented as a tenant-branch access control.

## Current Coverage

The documentation covers flat Master Tenant-to-Subtenant workflows, Tenant and User Roles, basic resource sharing, tenant login, and the **Parent Tenant** field. It does not provide a supported N-level hierarchy model or a consolidated limitations reference.

Initial review of `../morpheus-ui` confirms that hierarchy behavior is not uniform:

- `PermissionService.canAccessTenant` walks the parent chain for descendant checks, with a safety stop after more than 10 iterations.
- `AccountsController`, `AccountUsersController`, `MorpheusSwitchUserFilter`, and Tenant option sources commonly scope non-root administrators to their own Tenant and direct children.
- The root Master Tenant can list or select all Tenants in several administration paths.
- Resource access uses object-specific ownership, `ResourcePermission` records, Role permissions, and endpoint filters. A resource's broad `visibility` setting is not a substitute for hierarchy-scoped access and must not be recommended for this use case.

Known gaps include:

- Maximum supported hierarchy depth and tenant-count limits
- Which tenant contexts can create, view, edit, disable, delete, or impersonate descendants
- Whether a tenant can be reparented and what happens when a tenant with descendants is disabled or deleted
- Ancestor, parent, sibling, and descendant resource permission, ownership, assignment, and filtering behavior
- Role, policy, quota, pricing, identity-source, integration, notification, and branding inheritance
- Login, subdomain, API, reporting, billing, search, and audit behavior across hierarchy levels
- Features that support only the Master Tenant-to-direct-Subtenant model

## Specs

- [ ] `docs-multitenancy-hierarchy` - Confirm and document hierarchy terminology, supported depth, lifecycle behavior, navigation, and hard limits.
- [ ] `docs-multitenancy-resource-inheritance` - Document explicit resource permissions, assignment, inheritance, and policy behavior at each relationship level.
- [ ] `docs-multitenancy-administration-limitations` - Document delegated administration, roles, identity, login, integrations, reporting, and unsupported or Master-only operations.

## Dependencies

- Product engineering or support confirmation is required for hierarchy depth, scale limits, reparenting, deletion, and inheritance behavior not established by implementation or tests.
- `../morpheus-ui` is the implementation source of truth. Review controller, service, dataset, Role, and permission logic rather than extrapolating from the Tenant form alone.
- `docs-multitenancy-hierarchy` must establish canonical terminology and supported topology before the other children publish hierarchy-dependent claims.
- The completed `docs-morph-11023-parent-tenant-field` work is a UI-field reference, not evidence of unlimited nesting or inherited behavior.

## Acceptance Criteria

- THE DOCUMENTATION SHALL state whether N-level nested tenancy is supported and identify the maximum supported depth or explicitly state that no published fixed depth exists.
- THE DOCUMENTATION SHALL distinguish Master Tenant, ancestor, direct parent, child, descendant, and sibling behavior.
- THE DOCUMENTATION SHALL provide a verified capability and limitations matrix for hierarchical tenancy.
- THE DOCUMENTATION SHALL distinguish recursive descendant-aware checks from direct-child-only administration paths.
- THE DOCUMENTATION SHALL use explicit tenant permissions, ownership, assignment, and endpoint tenant filters for scoped access and SHALL NOT recommend broad resource visibility as a hierarchy filter.
- THE DOCUMENTATION SHALL reconcile flat-Subtenant language with the current Parent Tenant workflow.
- IF a hierarchy behavior cannot be verified THEN THE DOCUMENTATION SHALL not infer support from the presence of the Parent Tenant field.

## Boundaries

- This initiative documents existing supported product behavior; it does not request new tenant hierarchy capabilities.
- Multi-tenancy remains an Enterprise-only feature unless licensing guidance changes separately.
- Product limits and security boundaries must not be inferred from UI availability or a single successful lab scenario.
- Broad resource visibility is outside the hierarchy-scoping model because it can expose resources beyond the intended branch.

## Validation

- Trace each hierarchy and limitation claim to implementation, tests, approved product guidance, or an identified technical reviewer.
- Review `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/PermissionService.groovy`, Tenant controllers and datasets, `RoleService.groovy`, and object-specific permission services.
- Test representative three-level and deeper hierarchies when a suitable environment is available.
- Build the Sphinx documentation and verify all navigation, includes, tables, and cross-references.
- Review the completed guide with product engineering, security, and support before publication.

## Progress

- Existing documentation audited on 2026-08-12.
- Parent Tenant field coverage exists, but N-level behavior and limitations are not documented.
- Initial `../morpheus-ui` review found both recursive ancestry checks and direct-child-only paths; documentation must describe capability per operation rather than claiming uniform N-level behavior.
- Three child specs are ready for investigation and design.

## Kickoff

Audit and document supported multi-tenancy hierarchy behavior without inferring N-level support from the Parent Tenant field.

**Status:** planning - current coverage is known; product behavior and limits require verification.

**Pick up at:** start `docs-multitenancy-hierarchy`, establish the supported topology and depth, then use that model for the inheritance and administration children.

-> `.hero/planning/initiatives/docs-multitenancy-guide/spec.md`

**Files:** `administration/tenants/tenants.rst`, `administration/tenants/configuring_multi_tenancy.rst`, `getting_started/guides/tenancy.rst`, `administration/roles/`

**Skip:** do not describe nesting as unlimited or recursively inherited until verified, and do not use broad resource visibility as a tenant-branch filter.
