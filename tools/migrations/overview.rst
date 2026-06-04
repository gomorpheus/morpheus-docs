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
