---
title: "Multi-Tenant Administration and Limitations"
slug: docs-multitenancy-administration-limitations
type: feature
status: planning
size: medium
horizon: next
tags: [documentation, multitenancy, administration, limitations]
parent: docs-multitenancy-guide
depends-on: [docs-multitenancy-hierarchy]
created: 2026-08-12
---

# Multi-Tenant Administration and Limitations

## Context

Tenant administration guidance is distributed across Tenant, Role, identity, login, integration, reporting, and troubleshooting pages. It does not provide a consolidated statement of which operations can be delegated below the Master Tenant or how those operations behave for descendants.

## Goal

Document the administrative and operational capabilities and limitations of nested tenancy, with clear Master-only, parent-scoped, tenant-local, and unsupported classifications.

## Approach

Use the verified hierarchy terminology from `docs-multitenancy-hierarchy`. Organize findings as an operational matrix and link detailed procedures rather than duplicating them. Review both recursive helpers and each endpoint because a generic descendant check does not guarantee that a specific UI or API operation supports all descendant levels.

## Changes

1. Audit Tenant and User Roles, impersonation, identity sources, login and subdomains, branding, integrations, notifications, audit history, reporting, billing, search, API, and troubleshooting behavior in `../morpheus-ui`.
   - Include `AccountsController`, `AccountUsersController`, `MorpheusSwitchUserFilter`, Tenant and Role datasets, `PermissionService`, and `RoleService`.
2. Classify each operation as Master-only, ancestor-visible, direct-parent scoped, tenant-local, descendant-aware, or unsupported.
3. Add a consolidated limitations section to the canonical Tenant documentation.
4. Update affected role, identity, settings, and troubleshooting pages where current two-level wording is incomplete or misleading.

## Acceptance Criteria

- THE DOCUMENTATION SHALL identify which hierarchy levels can create users, assign Roles, impersonate users, and administer descendant Tenants.
- THE DOCUMENTATION SHALL explain login, subdomain, and identity-source behavior for nested Tenants.
- THE DOCUMENTATION SHALL identify the scope of reporting, billing, audit, search, integrations, notifications, and branding.
- THE DOCUMENTATION SHALL provide an explicit list of Master-only and unsupported nested-tenancy operations.
- THE DOCUMENTATION SHALL distinguish product limitations from Role permission restrictions.
- THE DOCUMENTATION SHALL distinguish recursive descendant-aware API reads from direct-child-only UI, user-management, Role, and impersonation operations.

## Boundaries

- Resource visibility and assignment are covered by `docs-multitenancy-resource-inheritance`.
- This work does not change licensing or make multi-tenancy available outside Enterprise.

## Risks

Administrative access is a security boundary. UI availability alone is insufficient evidence of authorization or descendant scope; verify API and service-layer enforcement. Do not substitute a resource's broad visibility flag for tenant authorization.

## Validation

- Test representative operations as Master, parent, child, and grandchild administrators.
- Review authorization and identity claims with product engineering or security.
- Build all changed Sphinx pages and verify navigation and cross-references.

## Kickoff

Create the operational limitations reference for delegated and nested tenant administration.

-> `.hero/planning/features/docs-multitenancy-administration-limitations/spec.md`
