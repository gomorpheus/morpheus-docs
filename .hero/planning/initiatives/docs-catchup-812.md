---
title: "Docs Catch-Up: Sync to HPE Public Portal 8.1.2 Content"
type: initiative
status: active
priority: high
horizon: now
---

# Docs Catch-Up: Sync to HPE Public Portal 8.1.2 Content

## Objective

Bring this documentation repository into parity with the content published on the HPE public documentation portals (Enterprise `sd00007732en_us` and VM Essentials `sd00007735en_us`) at version 8.1.2. This is a content-sync initiative — identifying what's changed, what's new, and what's been restructured on the public sites, then reflecting those changes here.

## Background

The HPE public portals represent the latest published state of the docs at 8.1.2. This repository has fallen behind in certain areas. This initiative systematically diffs the public portal content against what's in the repo and catches up section by section.

### Scraping Infrastructure

- **Script**: `tools/scrape_hpe_docs.py` — pulls all pages via the HPE API
- **TOC API**: `https://support.hpe.com/hpesc/public/api/document/<docId>/toc`
- **Page API**: `https://support.hpe.com/hpesc/public/api/document/<docId>/render?page=<GUID>.html`
- **Output**: `_scraped/sd00007732en_us/` (Enterprise), `_scraped/sd00007735en_us/` (Essentials)

### Key Differences Identified

Enterprise portal has content this repo may need updates for:
- **Getting Started**: Capacity & Planning, Core Functionality (Discovery, Agent), IPv6, Data Encryption
- **Infrastructure**: HVM clusters (major expansion), Compute section, Boot/PXE section, Trust (Vault, external Cypher appliance)
- **Library**: Blueprints (Helm, K8s, ARM, CloudFormation), Catalog Items, Cluster Layouts, Options/Forms, Variables
- **Administration**: Policies section, Distributed Workers, Software Licenses, Whitelabel, Email Templates
- **Integration Guides**: HPE Bare Metal (BMaaS) — large new section, ArubaCX DSS, HPE Alletra MP Storage, CN2 networking
- **User Guides**: New structured guides (AWS, Azure, VMware getting started, XaaS, Terraform, VDI, Tagging, Cypher Policies, Tenancy)

## Children

- catchup-getting-started
- catchup-operations
- catchup-provisioning
- catchup-library
- catchup-infrastructure
- catchup-backups
- catchup-monitoring
- catchup-tools
- catchup-administration
- catchup-integration-guides
- catchup-user-guides
- catchup-troubleshooting
- catchup-personas

## Approach

For each section:
1. Run the scraper to get the latest portal content (`python3 tools/scrape_hpe_docs.py both`)
2. Diff the portal TOC against the repo's RST structure
3. Identify new pages, removed pages, and pages with significant content changes
4. Update repo RST files to match the 8.1.2 published content
5. Apply tier annotations per the `unified-docs-merge` initiative convention (once established)

## Dependencies

- `unified-docs-merge` — tier annotation convention (needed for marking tier-specific content)
- Scraped content in `_scraped/` (run scraper first)

## Success Criteria

- Every page in the Enterprise portal TOC has a corresponding RST file in this repo
- Content in repo matches 8.1.2 published state (no stale pre-8.1.2 content remaining)
- New sections (HVM expansion, HPE BMaaS, User Guides, etc.) are fully present
- No broken cross-references after restructuring
