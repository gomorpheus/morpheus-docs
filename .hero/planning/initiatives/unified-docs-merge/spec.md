---
title: "Unified Docs: Merge VM Essentials & Enterprise Portals for 8.1.2"
type: initiative
slug: unified-docs-merge
status: active
priority: high
horizon: now
---

# Unified Docs: Merge VM Essentials & Enterprise Portals for 8.1.2

## Objective

Merge the two separate HPE documentation portals (VM Essentials and Enterprise Software) into a single unified documentation site that covers all three product tiers: **Enterprise**, **Advanced**, and **Essentials**. The current docs (this repo) will become the single source of truth for all tiers at version 8.1.2.

## Background

HPE Morpheus now ships as **one product, one binary** with three license tiers:

| Tier | Key Characteristics |
|------|---------------------|
| **Enterprise** | Full feature set — multitenancy, full automation, all cloud integrations, all provisioning types |
| **Advanced** | Automation capabilities, broader integrations (details TBD) |
| **Essentials** | VMware/HVM hypervisor self-service only, no full automation, no multitenancy |

Previously, separate documentation portals existed:
- **VM Essentials**: `sd00007735en_us` — focused on the reduced VMware-centric feature set
- **Enterprise Software**: `sd00007732en_us` — full enterprise documentation

Since all tiers now share the same binary and deployment model, a single docs site with clear tier annotations is the correct approach.

## Principles

1. **Single source, tier-annotated** — One page per feature, with clear callouts for which tiers include it (not three separate doc sets)
2. **Essentials is additive restriction** — Document features once; mark what Essentials/Advanced exclude rather than maintaining separate reduced copies
3. **Deployment model is universal** — Installation, system requirements, and deployment docs apply to all tiers identically
4. **8.1.2 baseline** — This initiative reflects 8.1.2 state only; 9.0.0 changes will be a follow-on initiative

## Scope

### In Scope
- Audit all existing docs sections for tier-specific content
- Establish a tier annotation convention (badges, admonitions, conditional content)
- Incorporate any Essentials-only or Advanced-only content from the HPE portals that doesn't exist here
- Ensure deployment/installation docs reflect the unified product model
- Update administration docs to reflect license-tier behavior
- Remove outdated references to separate product SKUs

### Out of Scope
- 9.0.0 feature changes (follow-on initiative)
- API docs (hosted externally at apidocs.morpheusdata.com)
- CLI docs (hosted externally at clidocs.morpheusdata.com)

## Children

- docs-tier-annotation-convention
- docs-merge-essentials-content
- docs-merge-advanced-content
- docs-unified-deployment
- docs-tier-feature-matrix
- docs-administration-licensing

## Open Questions

- [ ] What is the exact Advanced tier feature set? (awaiting details)
- [ ] What annotation style should we use for tier restrictions? (admonition, badge, sidebar?)
- [ ] Are there Essentials-specific workflows that differ enough to warrant their own pages vs. callouts on existing pages?
- [ ] Should we maintain a single feature matrix page or annotate inline per section?

## Success Criteria

- Single documentation site covers all three tiers clearly
- A reader on any tier can quickly identify what applies to them
- No duplicate content across tiers
- All content from both HPE portals is accounted for (merged or explicitly deprecated)
- Deployment and installation docs are tier-agnostic
