Overview
--------

How Migrations Work
^^^^^^^^^^^^^^^^^^^

The bulk migration tool moves virtual machines from VMware vCenter environments to HVM Clusters. A migration requires:

- One or more integrated VMware vCenter Clouds (source)
- At least one functional HVM Cluster (destination)

See the VMware vCenter integration guide and the HVM Clusters guide elsewhere in this documentation for details on setting up those integrations.

Migration Architecture
^^^^^^^^^^^^^^^^^^^^^^

Migrations use an **agent-pull** architecture. The Morpheus Agent running on the destination HVM host connects directly to the source VMware environment over HTTPS and streams disk data using VMware's HttpNfcLease export API. This means:

- **No intermediate storage is required** — disk data flows directly from ESXi to the target HVM host
- **HVM hosts must have network access to ESXi hosts and vCenter** on the source VMware Cloud via the management network
- **Disk format conversion happens in-flight** — VMDK data is decompressed and written as QCOW2 (thin-provisioned) or raw format depending on the target datastore

.. note::

   The Morpheus Agent on HVM hosts handles the actual data transfer. Ensure agents are at version 2.10.0 or later. To upgrade, navigate to the host detail page, open the ACTIONS menu, and select "Upgrade Agent."

Migration Phases
^^^^^^^^^^^^^^^^

Each VM in a Migration Plan goes through the following phases:

#. **Precheck** — Verifies the source VM is reachable, sets credentials, and powers on the VM if needed. This step can be skipped when creating the plan.
#. **Prepare** — Installs QEMU guest tools on the source VM. For Windows, VirtIO drivers are also installed (automatically, with ISO fallback if network installation fails).
#. **Create** — Provisions a target VM shell on the HVM Cluster. Maps CPU, memory, networks, and storage controllers from the source configuration.
#. **Transfer** — Powers down the source VM and streams disk data from VMware to the target HVM host. Disks are written as thin-provisioned QCOW2 for GFS2/NFS targets or raw for block devices (including Ceph RBD).
#. **Reconfigure** *(Windows only)* — Boots the target VM on temporary SATA disks so Windows can detect and load VirtIO drivers, then shuts down and switches all disks to VirtIO bus.
#. **Finalize** — Starts the destination VM and marks the migration as complete.

All VMs in a plan are processed in parallel. Plans with many VMs will transfer them simultaneously, limited only by available bandwidth and storage I/O capacity.

Linux Guest Preparation
^^^^^^^^^^^^^^^^^^^^^^^

During the **Prepare** phase, |morpheus| installs QEMU guest tools and ensures the necessary VirtIO kernel modules are available so the VM can boot successfully on the KVM-based HVM target. The steps performed depend on the Linux distribution family.

Package Installation
````````````````````

|morpheus| uses the source VM's native package manager to install ``qemu-guest-agent``. The system detects the available package manager and runs the appropriate install command:

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Distro Family
     - Install Command
     - Notes
   * - RHEL / CentOS / Rocky / AlmaLinux (yum)
     - ``dracut --force --no-hostonly && yum install -y qemu-guest-agent``
     - Rebuilds initramfs first to ensure VirtIO drivers are included
   * - RHEL 8+ / Fedora (dnf)
     - ``dracut --force --no-hostonly && dnf install -y qemu-guest-agent``
     - Same as yum but uses dnf package manager
   * - Ubuntu / Debian
     - ``apt-get install -y qemu-guest-agent``
     - VirtIO modules typically already in default initramfs
   * - SUSE / SLES
     - ``zypper install -y qemu-guest-tools``
     - Note: package name is ``qemu-guest-tools`` (not ``qemu-guest-agent``)

The installation is retried up to 3 times with a 30-second pause between attempts if the package manager command fails (e.g., due to transient network issues or locked package databases).

.. important::

   Unlike Windows migrations — where VirtIO drivers are installed from the |morpheus| appliance URL or a bundled ISO (no internet required) — **Linux guest preparation requires access to a package repository**. The source VM must be able to reach either the public internet or an internal yum/apt/zypper mirror during the Prepare phase. If no repository is reachable, the Prepare phase will fail.

   For air-gapped or restricted-network environments, ensure an internal package mirror is configured in the source VM's repository configuration (e.g., ``/etc/yum.repos.d/`` for RHEL-family, ``/etc/apt/sources.list`` for Debian-family) **before** initiating the migration.

VirtIO Kernel Modules
`````````````````````

After package installation, |morpheus| verifies that the following VirtIO kernel modules are available (loaded or loadable) on the source VM:

- ``virtio_blk`` — VirtIO block device driver (required for disk access on the target)
- ``virtio_net`` — VirtIO network driver (required for network connectivity on the target)
- ``virtio_scsi`` — VirtIO SCSI controller driver (used when source disks map to VirtIO-SCSI)
- ``virtio_pci`` — VirtIO PCI transport (bus-level driver for all VirtIO devices)

These modules are typically included in the default kernel for all supported distributions. If a module is missing, it must be present in the kernel's module tree so it can be included during the initramfs rebuild.

Initramfs Rebuild
`````````````````

For RHEL-family distributions, the initramfs is rebuilt **before** package installation using ``dracut --force --no-hostonly``. The ``--no-hostonly`` flag ensures that all available kernel modules (including VirtIO drivers) are included in the initramfs regardless of the current running hardware. This is critical because the source VM is running on VMware hardware but must boot on KVM/VirtIO hardware after migration.

For Debian/Ubuntu, VirtIO modules are typically already included in the default initramfs and no explicit rebuild is performed during migration.

For SUSE/SLES, the ``qemu-guest-tools`` package installation handles driver availability through the distribution's standard module inclusion mechanisms.

Network Interface Changes
`````````````````````````

When a VM moves from VMware (vmxnet3 or E1000 adapters) to HVM (VirtIO-net), network interface names may change. The behavior depends on the guest OS configuration:

- **Predictable naming (default on most modern distros):** Interface names are derived from PCI slot/topology (e.g., ``ens3``, ``enp1s0``). The name will change since the virtual hardware topology differs between VMware and KVM.
- **Legacy naming (``eth0``, ``eth1``):** If the guest uses legacy naming (via kernel parameter or udev rules), interfaces typically retain their ordinal names.

|morpheus| does not automatically reconfigure network interface bindings (IP addresses, routes, bonding) during migration. Post-migration, verify that network configuration files reference the correct interface names on the target VM.

.. note::

   For RHEL/CentOS 7+ and similar distributions using NetworkManager, connections are often bound by MAC address rather than interface name. Since |morpheus| preserves MAC addresses during migration, these connections typically reconnect automatically.

Bootloader and fstab
`````````````````````

- **GRUB configuration** — Generally requires no changes. The initramfs rebuild ensures VirtIO drivers are loaded early enough for root device access. If the source VM uses device-path references in GRUB (e.g., ``/dev/sda``), these are mapped to the corresponding VirtIO device paths on the target.
- **fstab** — Entries using UUID or LABEL references (the default on most modern distributions) require no changes. Entries using device paths (e.g., ``/dev/sda1``) may need to be updated post-migration if the device naming changes.

.. tip::

   Verify that ``/etc/fstab`` uses UUIDs or LABELs (``blkid`` to check) before migration. This avoids potential boot issues on the target related to device path changes.

Supported Configurations
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Component
     - Supported Options
   * - Source Platform
     - VMware vCenter (all supported versions)
   * - Target Platform
     - HVM Cluster (KVM-based)
   * - Guest OS (Linux)
     - Red Hat, CentOS, Rocky, AlmaLinux, SUSE, Ubuntu, Debian
   * - Guest OS (Windows)
     - Windows Server 2016, 2019, 2022, 2025; Windows 10/11
   * - Target Datastores
     - GFS2, NFS (thin QCOW2), local block devices (raw), Ceph RBD (raw)
   * - Boot Modes
     - BIOS and UEFI
   * - Storage Controllers
     - SCSI → VirtIO-SCSI, IDE/SATA → VirtIO Block (automatic mapping)

Required Permissions
^^^^^^^^^^^^^^^^^^^^

Users performing migrations require specific RBAC permissions. The table below lists the minimum permissions needed for each type of migration operation.

Bulk Migration (VMware to HVM)
``````````````````````````````

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Permission
     - Access Level
     - Purpose
   * - Services: Migrations
     - Full
     - Create, edit, execute, and manage Migration Plans. Read access allows viewing plans only.
   * - Infrastructure: Clusters
     - Full or Group
     - Access to the target HVM Cluster for VM provisioning
   * - Infrastructure: Compute
     - Full or Group
     - Create and manage server records on the target cluster
   * - Provisioning: Instances
     - Full or Group
     - Create Instance records for migrated VMs

Live Migration (Host-to-Host within a Cluster)
``````````````````````````````````````````````

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Permission
     - Access Level
     - Purpose
   * - Infrastructure: Manage Placement
     - Full
     - Move VMs between hosts, change placement strategy (Auto/Pinned)
   * - Infrastructure: Clusters
     - Full or Group
     - View cluster hosts and VM assignments
   * - Infrastructure: Compute
     - Read or higher
     - View host details and available capacity

Storage Migration (Datastore-to-Datastore)
``````````````````````````````````````````

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Permission
     - Access Level
     - Purpose
   * - Infrastructure: Manage Placement
     - Full
     - Initiate storage migration for VMs
   * - Infrastructure: Storage
     - Read or higher
     - View available datastores and capacity
   * - Infrastructure: Clusters
     - Full or Group
     - Access to the cluster containing the VM

Cross-Cloud Move (Record Migration)
````````````````````````````````````

.. list-table::
   :widths: 35 20 45
   :header-rows: 1

   * - Permission
     - Access Level
     - Purpose
   * - Infrastructure: Move Servers
     - Full
     - Move server records between Clouds. This is an administrative record-keeping operation, not a data migration.

Permission Dependencies
```````````````````````

- **Services: Migrations** requires that the user also has access to both the source Cloud (VMware) and the target Cluster (HVM). Cloud and Group access are controlled via the role's Cloud and Group permission tabs.
- **Infrastructure: Manage Placement** requires at minimum Read access to Infrastructure: Clusters and Infrastructure: Compute to view available hosts and capacity.
- Permissions follow the standard |morpheus| RBAC hierarchy: Tenant Role sets maximum permissions, User Role cannot exceed Tenant Role limits.

Recommended Role Examples
`````````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Role
     - Permissions
   * - VM Operator (limited migration)
     - Infrastructure: Manage Placement = Full, Infrastructure: Clusters = Group, Infrastructure: Compute = Group. Can live-migrate VMs within assigned clusters only.
   * - Migration Administrator
     - Services: Migrations = Full, Infrastructure: Clusters = Full, Infrastructure: Compute = Full, Provisioning: Instances = Full. Can execute bulk migrations across all clusters.
   * - Read-only Observer
     - Services: Migrations = Read, Infrastructure: Clusters = Read, Infrastructure: Compute = Read. Can view migration plans and status but cannot execute or modify.
