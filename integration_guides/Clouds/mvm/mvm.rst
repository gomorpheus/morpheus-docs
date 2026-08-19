MVM Cloud
---------

Overview
^^^^^^^^

MVM (Morpheus Virtual Machine) Cloud, also known as HVM (HPE Virtual Machine), is |morpheus|'s native KVM-based hypervisor platform. Unlike MVM *Clusters* which are managed via ``Infrastructure > Clusters``, the MVM Cloud integration provides a cloud-level abstraction for provisioning and managing KVM virtual machines across distributed hypervisor hosts.

The MVM Cloud integration uses the ``kvmContainerService`` for provisioning and ``MvmHostService`` for host management.

.. NOTE:: MVM Cloud and MVM Clusters serve different purposes. The MVM Cloud is a traditional cloud integration for VM provisioning. MVM Clusters provide clustered hypervisor management with features like HA, live migration, and shared storage. Both use KVM underneath.

Features
^^^^^^^^

- KVM virtual machine provisioning and lifecycle management
- Virtual image management with template-based provisioning
- Host hypervisor management
- Network configuration (bridges, VLANs, OVS)
- Storage profile management
- Auto-scaling support
- Brownfield VM import
- Console access

Prerequisites
^^^^^^^^^^^^^

- One or more Linux hosts with KVM/QEMU installed and configured
- |morpheus| Agent installed on hypervisor hosts (or ability to install)
- Network connectivity between |morpheus| and hypervisor hosts
- Sufficient CPU, memory, and storage resources for VM provisioning
- Libvirt service running on target hosts

Adding an MVM Cloud
^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clouds``
#. Select :guilabel:`+ ADD`
#. Choose **MVM** (or **HVM**) from the cloud type list
#. Configure:

   NAME
     Friendly name for the cloud
   CODE
     Unique code identifier
   LOCATION
     Optional location descriptor
   VISIBILITY
     Public (all tenants) or Private (master tenant only)
   TENANT
     Owning tenant for the cloud

#. Select :guilabel:`NEXT` and configure Group assignment
#. Complete the wizard

After adding the cloud, hypervisor hosts must be added to provide compute capacity.

Adding Hypervisor Hosts
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the MVM Cloud detail page
#. Select the **Hosts** tab
#. Click :guilabel:`+ ADD`
#. Configure the host connection:

   SSH HOST
     IP address or hostname of the KVM hypervisor
   SSH USERNAME
     User with sudo privileges
   SSH PASSWORD / KEY
     Authentication credentials
   
#. |morpheus| will connect, install the agent, and begin managing the host

Instance Types
^^^^^^^^^^^^^^^

MVM Cloud supports two Instance Types:

- **KVM** (code: ``kvm``) — Standard KVM virtual machine
- **HVM** (code: ``mvm``) — High-performance virtual machine optimized for the Morpheus HVM hypervisor

Both use the same underlying ``kvmContainerService`` for provisioning.

Virtual Images
^^^^^^^^^^^^^^

MVM/HVM provisioning supports QCOW2 and RAW Virtual Images. A multi-disk QCOW2 image requires one QCOW2 file per disk and a file named ``metadata.json`` on the same Virtual Image. The manifest maps filenames to disk capacities, guest device names, ordering, and the boot disk. Upload the QCOW2 files before the manifest.

See :ref:`multi-disk-qcow2-images-for-hvm-kvm` for the manifest schema and upload procedure.

Provisioning
^^^^^^^^^^^^^

To provision a VM on MVM Cloud:

#. Navigate to ``Provisioning > Instances``
#. Select :guilabel:`+ ADD`
#. Choose the KVM or HVM Instance Type
#. Select the MVM Cloud as the target
#. Configure:

   IMAGE
     Select from available virtual images (typeahead from synced images)
   PLAN
     Select a service plan (CPU, RAM, storage configuration)
   NETWORK
     Select the target network (bridge, VLAN)
   HOST
     Optionally pin to a specific hypervisor host
   VOLUMES
     Configure disk(s) — size, type, datastore

#. Complete the wizard

Storage Profiles
^^^^^^^^^^^^^^^^^

MVM Cloud supports storage profiles that define storage characteristics:

- Storage backend type
- Performance tier
- Replication settings
- Volume type defaults

Storage profiles are configured via seed data and can be customized for specific environments.

Networking
^^^^^^^^^^^

MVM Cloud networking supports:

- **Linux bridges** — Standard Linux bridge interfaces
- **Open vSwitch (OVS)** — SDN-capable virtual switching
- **VLANs** — VLAN tagging on bridge/OVS ports
- **Direct/passthrough** — SR-IOV and PCI passthrough for high-performance networking

MVM Cloud vs MVM Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 37 37
   :header-rows: 1

   * - Feature
     - MVM Cloud
     - MVM Cluster
   * - Management model
     - Cloud integration (flat)
     - Cluster (master/worker topology)
   * - Navigation
     - Infrastructure > Clouds
     - Infrastructure > Clusters
   * - High Availability
     - Manual
     - Built-in HA, fencing
   * - Live Migration
     - Not available
     - Supported
   * - Shared Storage
     - Per-host
     - Cluster-wide (Ceph, NFS)
   * - Provisioning
     - Direct to host
     - Scheduler-placed
   * - Use case
     - Simple KVM environments
     - Production hyperconverged

Troubleshooting
^^^^^^^^^^^^^^^^

- **Host not connecting:** Verify SSH connectivity and that the user has sudo access. Check that libvirt is running on the host.
- **No images available:** Ensure virtual images have been uploaded or synced. Images must be in a KVM-compatible format (QCOW2, RAW).
- **Only one disk or missing data disks:** Confirm the multi-disk QCOW2 image includes a valid ``metadata.json`` file and that each manifest filename matches an uploaded QCOW2 file.
- **Wrong disk size or boot disk:** Confirm capacities are expressed in bytes, disk positions are unique, and the intended root disk has ``boot`` set to ``true``.
- **Provisioning fails:** Check available capacity on the target host. Verify storage pools have free space.
- **Network errors:** Confirm bridge interfaces exist on the hypervisor host and match the configured network names.
- **Console not working:** Ensure VNC/SPICE ports (5900+) are accessible from the |morpheus| appliance to the hypervisor host.
