---
type: initiative
status: delivering
horizon: now
tags: [documentation, field-feedback, usability]
---

# Field Feedback Documentation Improvements

## Objective

Address documentation gaps and usability issues reported from field teams, partners, and customers. These items range from missing guides to conflicting information to sections that are too vague for practitioners to act on.

## Context

Field feedback indicates several areas where the documentation fails to meet user expectations — either because content is missing, too vague, conflicting between sections, or not structured as practical guides. This initiative groups all reported items into actionable specs.

## Child Specs

### 1. Windows VM Domain Join Guide (`docs-windows-domain-join-guide`)

Write a guide-style document covering deploying Windows VMs and getting domain joins to work — the proper flow and setup steps including cloud-init/sysprep, unattend files, domain credentials, and DNS prerequisites.

### 2. Virtual Image Options Reference (`docs-virtual-image-options-reference`)

Document what each option on the Virtual Images detail page actually does, which cloud types each option applies to, and resolve perceived conflicts between the UI and existing documentation. Include a matrix of option vs cloud type applicability.

### 3. HVM Cluster Content for Essentials (`docs-hvm-essentials-parity`)

Copy/adapt the HVM Cluster documentation from the Enterprise guide into the Essentials documentation where applicable. Cover day-0 operations, cluster startup, network management, day-2 changes, and ongoing ops that the Essentials docs currently lack.

### 4. FC Storage Connection (`docs-fc-storage-connection`)

Document Fibre Channel storage connectivity for HVM clusters — zoning requirements, multipath configuration, LUN presentation, and datastore creation from FC LUNs.

### 5. Boot From SAN (`docs-boot-from-san`)

Document how to configure and use Boot From SAN with HVM hosts — BIOS/UEFI configuration, FC HBA setup, LUN masking, and Morpheus provisioning workflow for SAN-booted hosts.

### 6. Tagged Bonds Networking Guide (`docs-tagged-bonds-guide`)

Expand the networking documentation to clearly explain when and how to use tagged bonds (VLAN-tagged bond interfaces) — use cases, configuration examples, and comparison with other bonding/VLAN approaches. Current docs are noted as "vague."

### 7. Infrastructure Networking Overhaul (`docs-infrastructure-networking-overhaul`)

Improve the Infrastructure > Networks section with screenshots, VMware-to-HVM analogies, and step-by-step walkthroughs for common tasks: creating a new network, replicating a VMware network design, understanding network types. Partners and customers consistently struggle with this section.

### 8. Windows Cloud Guest Customization (`docs-windows-cloud-guest-customization`)

Document the recommended "cloud guest customization" image preparation approach for Windows VMs. This is the recommended approach but currently has no documentation.

### 9. Cluster HA & Dynamic Placement Details (`docs-cluster-ha-dynamic-placement`)

Expand documentation on cluster HA behavior (beyond the existing Pacemaker doc), and provide more detail on how Dynamic Placement makes decisions — the algorithm, thresholds, triggers, and how admins can tune behavior.

### 10. Host CPU Passthrough Guide (`docs-host-passthrough-guide`)

Document when to use `host-passthrough` CPU mode versus not using it — implications for live migration, performance, compatibility, and recommended use cases.

### 11. Windows VM Migration Conflict Resolution (`docs-windows-migration-conflict-resolution`)

Resolve conflicting information between the two Windows VM migration sections in the HPE published docs:
- GUID-3A8E263B-7508-4620-A5C6-5372D385F0DB (automated migration prep)
- GUID-D8021277-53D1-43E9-9799-785A2511910E (manual/legacy VirtIO driver install)

The second section appears to be legacy content that should not be needed for 9.0+ where automated driver injection handles everything. Consolidate into a single clear narrative with the manual approach clearly marked as fallback only.

### 12. Alletra MP Creating Instances Merge (`docs-alletra-creating-instances-merge`)

Merge the helpful "Creating Instances" page under the Alletra MP documentation with the main Provisioning > Instances documentation, or cross-reference clearly so users don't miss it.

### 13. Security Server Section Clarification (`docs-security-server-clarification`)

Clarify the vague "Security Server" section — what it is, when it's used, and practical configuration steps.

### 14. Storage Network Interfaces for HVM (`docs-storage-network-interfaces-hvm`)

Document the process and options for adding storage network interfaces to HVM hosts — what "storage network interfaces" means in this context, when to add them, and configuration steps.

## Acceptance Criteria

1. Each child spec is created as an independent feature spec with its own acceptance criteria
2. Specs are prioritized by field impact (networking, Windows, and Essentials gaps are highest priority)
3. Items that are moot due to virtual switch migration (netplan) are noted but not actioned

## Notes

- Netplan documentation is largely moot since HVM is moving to Virtual Switch — do not invest in new netplan content
- The HPE published doc pages (GUID-3A8E263B... and GUID-D8021277...) are JavaScript-rendered and couldn't be fetched directly, but based on context the conflict is between automated vs manual Windows VirtIO driver installation procedures
