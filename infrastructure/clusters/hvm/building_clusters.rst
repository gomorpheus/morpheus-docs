Building New HVM Clusters
=========================

Prerequisites
-------------

Before creating an HVM 1.3 cluster, ensure the following requirements are met:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Requirement
     - Details
   * - Operating System
     - Ubuntu 24.04 LTS (HPE's HVM OS recommended)
   * - Minimum Hosts
     - 3 hosts for a single-site cluster
   * - CPU
     - Hardware virtualization enabled (VT-x/AMD-V)
   * - Memory
     - 32 GB RAM minimum (4 GB reserved for system)
   * - Access
     - Root SSH or passwordless sudo
   * - Network
     - Static IP on management interface
   * - Firewall
     - Port 7443 open between all hosts
   * - Storage
     - Shared storage (iSCSI, FC) accessible by all hosts

Cluster Creation
----------------

#. Navigate to ``Infrastructure > Clusters``
#. Click :guilabel:`+ Add Cluster`
#. Select **HVM** as the cluster type
#. Select the **HVM 1.3** layout
#. Complete the following fields:

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Field
        - Description
      * - SSH Hosts
        - Comma-separated IP addresses of all hosts
      * - SSH Port
        - SSH port (default: 22)
      * - Username
        - SSH username with root or sudo access
      * - Password/Key
        - Authentication credential
      * - Data Device
        - Data device path (HCI only)
      * - Management Network Name
        - Network name for management traffic
      * - Storage Network Name
        - Network name for storage traffic
      * - Compute Network Name
        - Network name for compute traffic
      * - Overlay Network Name
        - Network name for overlay traffic
      * - Compute VLANs
        - VLAN IDs for compute networks
      * - CPU Architecture/Model
        - Processor architecture selection
      * - Witness
        - Witness node selection (for stretch clusters)

#. Click :guilabel:`Complete` to begin automated provisioning

Automated Provisioning Phases
-----------------------------

Once cluster creation is initiated, |morpheus| executes the following automated phases:

Phase 1: Package Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installs required packages on all hosts:

- KVM/QEMU
- libvirt
- Corosync
- DLM
- GFS2 utilities
- Ceph libraries
- swtpm
- jq
- nfs-common

Phase 2: OVS Networking
^^^^^^^^^^^^^^^^^^^^^^^^

Configures Open vSwitch networking:

- Creates bridges for management, compute, and overlay networks
- Configures libvirt Management network

Phase 3: Host Preparation
^^^^^^^^^^^^^^^^^^^^^^^^^

Prepares each host for cluster operation:

- Firewall configuration
- libvirt configuration
- IOMMU enablement
- Hugepages configuration
- Workqueue tuning
- Directory structure creation

Phase 4: Cluster Services
^^^^^^^^^^^^^^^^^^^^^^^^^

Establishes cluster communication and coordination:

- SSH key generation and distribution via Cypher
- Corosync authkey generation and distribution via Cypher
- Corosync configuration with knet transport
- DLM configuration with fencing enabled
- Service ordering and startup (corosync → DLM)

Phase 5: iSCSI/Storage
^^^^^^^^^^^^^^^^^^^^^^^

Configures storage connectivity:

- iSCSI initiator name assignment
- Multipath configuration
- OOM protection for storage services

Phase 6: Storage Pools
^^^^^^^^^^^^^^^^^^^^^^

Creates local storage pools:

- Cloud-init ISO pool
- Local storage pool

Phase 7: Quorum Activation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activates the agent-based quorum system:

- Server sends quorumInfo to all agents
- Agents persist cluster member data to ``.quorum-nodes``
- Agents begin peer-to-peer quorum pinging

HPE Clustered Datastore (Shared LUN) Setup
-------------------------------------------

The HPE Clustered Datastore (GFS2) provides shared storage accessible by all cluster hosts simultaneously.

Adding iSCSI Targets
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters > [Cluster] > Storage > iSCSI``
#. Click :guilabel:`Add`
#. Enter the Target IP and Port (default: 3260)
#. Save the configuration

.. NOTE:: iSCSI targets are auto-discovered and auto-logged-in on all hosts in the cluster.

Creating the Datastore
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Storage > Datastores``
#. Create a new datastore with the GFS2 type

|morpheus| automatically handles:

- Formatting with ``mkfs.gfs2``
- Adding journal entries for each host (``gfs2_jadd``)
- Mounting on all cluster hosts
- Creating the libvirt storage pool
- Configuring the lock protocol (``lock_dlm``) with a lock table tied to the cluster

.. NOTE:: Mount information is persisted to ``/opt/morpheus-node/.mounts`` on each host.

Configuring Heartbeat Datastore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Edit the shared datastore properties
#. Enable the :guilabel:`Heartbeat Target` option

.. IMPORTANT:: It is recommended to configure 2 or more datastores as heartbeat targets for redundancy. Heartbeat writes occur to ALL configured datastores simultaneously. A host is considered online if its heartbeat is current on ANY configured datastore.

Verification
------------

After cluster creation, verify the cluster is healthy:

**Corosync membership:**

.. code-block:: bash

   corosync-quorumtool -s

Confirm the output shows ``Quorate: Yes``.

**DLM status:**

.. code-block:: bash

   systemctl is-active dlm
   dlm_tool status -v

Confirm all nodes show ``member=1``.

**Agent quorum:**

.. code-block:: bash

   curl -k https://localhost:7443/quorum

**UI verification:**

Navigate to ``Infrastructure > Clusters > [Cluster] > Summary > Quorum`` panel and confirm:

- Quorum status: ACHIEVED
- All nodes: ONLINE
- Coordinator: assigned
- Lockspaces: OK

Cluster Sizing
--------------

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Hosts
     - Failure Tolerance
     - Use Case
   * - 3
     - Tolerates 1 host failure
     - Minimum production cluster
   * - 5
     - Tolerates 2 host failures
     - Recommended for higher availability
