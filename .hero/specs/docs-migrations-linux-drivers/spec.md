---
type: initiative
status: delivering
horizon: now
tags: [migrations, linux, drivers, documentation]
---

# Migrations Overview: Linux Driver Injection Details

## Objective

Expand the Migrations Overview documentation (`tools/migrations/overview.rst`) to include detailed information about how Linux VMs are prepared during the migration process — specifically driver injection, VirtIO module loading, initramfs rebuilding, and any guest OS reconfiguration that occurs on the Linux side.

## Context

The current overview documents Windows driver injection (VirtIO drivers, ISO fallback, SATA-to-VirtIO reconfigure phase) but says almost nothing about what happens on Linux guests during the **Prepare** and **Finalize** phases. Users migrating Linux workloads need to understand:

- What VirtIO/QEMU modules are loaded or verified
- Whether initramfs/initrd is rebuilt to include VirtIO drivers
- How different distros are handled (RHEL-family vs Debian-family vs SUSE)
- Whether network interface naming changes (e.g. vmxnet3 → virtio)
- Any GRUB or bootloader reconfiguration that occurs
- Filesystem/fstab changes (if disk device paths change)

### Key Implementation Detail: Package Installation Requires Network or Mirror Access

Unlike Windows — where VirtIO drivers are installed from the Morpheus appliance URL or a local ISO (no internet needed) — Linux guest preparation uses standard package managers (`yum install qemu-guest-agent` for RHEL-family, `apt-get` for Debian-family, etc.). This means:

- **The source Linux VM must be able to reach a package repository** (either the public internet or an internal yum/apt mirror) during the Prepare phase
- This is handled via `MigrationPlanService` calls in the Morpheus application layer (see `morpheus-ui` source)
- Air-gapped environments **must** have an internal mirror configured on the source VM's repos before migration, or the Prepare phase will fail

This is a critical difference from Windows migrations and must be clearly documented so users in restricted network environments can plan accordingly.

## Acceptance Criteria

1. The overview includes a new section (or expands "Migration Phases") documenting the Linux-specific preparation steps during the Prepare phase
2. Driver injection details cover at minimum: virtio_blk, virtio_net, virtio_scsi module verification/injection
3. Initramfs rebuild process is documented per distro family (dracut for RHEL/Rocky/Alma, update-initramfs for Debian/Ubuntu, mkinitrd for SUSE)
4. Network interface reconfiguration behavior is documented (what happens to interface naming)
5. Any bootloader or fstab adjustments are noted
6. **Documents that Linux guest prep uses `yum install` / `apt-get install` for qemu-guest-agent** — requires internet or internal mirror access (contrast with Windows which pulls from appliance URL/ISO)
7. Includes a note/admonition for air-gapped or restricted-network environments explaining the mirror requirement
8. The content follows existing doc conventions (RST format, admonition style, list-table usage)

## Changes

- `tools/migrations/overview.rst` — Add "Linux Guest Preparation" section with driver injection details
