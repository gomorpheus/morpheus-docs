---
title: "Merge Essentials Portal Content"
type: feature
status: planning
priority: high
horizon: now
parent: unified-docs-merge
---

# Merge Essentials Portal Content

## Purpose

Audit the VM Essentials documentation portal (sd00007735en_us) and merge any unique content into this unified docs site, applying tier annotations where features are Essentials-excluded.

## Scope

- Inventory all pages in the VM Essentials portal
- Identify content that exists here but needs tier annotations (Essentials lacks it)
- Identify content unique to Essentials that doesn't exist here yet
- Mark features NOT available in Essentials: full automation, multitenancy, non-VMware/HVM clouds

## Known Essentials Restrictions

- VMware/HVM hypervisor only (no AWS, Azure, GCP, etc.)
- No full automation engine
- No multitenancy
- Self-service provisioning focus

## Acceptance Criteria

- [ ] Complete inventory of Essentials portal pages mapped to this repo
- [ ] All Essentials-excluded features annotated per the tier convention
- [ ] Any Essentials-unique content merged into appropriate sections
- [ ] No orphaned or missing content from the Essentials portal
