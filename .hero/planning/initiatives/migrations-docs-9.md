---
type: initiative
status: completed
horizon: now
title: "Migrations Documentation Overhaul for 9.0.0"
tags: [migrations, 9.0.0, vmware-to-hvm]
---

# Migrations Documentation Overhaul for 9.0.0

## Objective

Rewrite the Tools > Migrations documentation to accurately reflect the current capabilities of the bulk migration feature, targeting IT Operations teams migrating from VMware to HVM. Remove outdated limitations, document the automated Windows driver injection workflow, and clarify the technical architecture at an operator-friendly level.

## Key Changes from Code Review

- **No VM batch limit** — all VMs in a plan run in parallel (was incorrectly stated as 20)
- **Automated Windows VirtIO driver injection** — SATA→VirtIO bus swap with helper disk, no manual prep needed for driver injection
- **ISO fallback** for Windows VirtIO install when network MSI fails
- **Agent pulls disks from VMware** over HTTPS (HttpNfcLease), not NFS — async NFS note is irrelevant
- **QCOW2 thin provisioning** on GFS2/NFS targets
- **Ceph RBD support** as a target datastore
- **UEFI boot support** preserved from source
- **MAC address preservation** optional
- **48-hour transfer timeout**
- **Storage controller mapping** — SCSI→VirtIO-SCSI, IDE/SATA→VirtIO Block

## Target Audience

VMware IT Operations teams evaluating or executing migration from vSphere to HPE Morpheus HVM. Assume familiarity with VMware concepts (vCenter, datastores, networks) but not with KVM/libvirt internals.

## Scope

- Rewrite overview, requirements, plans, and Windows pages
- Add architecture diagram description (agent-pull model)
- Add post-migration validation section
- Remove incorrect batch limit and NFS async recommendations
- Update Windows section to reflect automated driver injection (manual steps only needed as fallback)
