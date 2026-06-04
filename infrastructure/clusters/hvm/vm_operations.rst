VM Lifecycle on Clusters
========================

Live Migration
--------------

Live migration moves a running VM from one cluster host to another with no downtime to the guest operating system.

Requirements
^^^^^^^^^^^^

- The VM must be running (powered on)
- The VM's storage must reside on a shared datastore (HPE Clustered Datastore or NFS). VMs with local storage cannot be live-migrated
- No host devices (GPU/USB passthrough) are attached to the VM
- The target host must have sufficient available memory
- Network connectivity between source and target hosts

Initiating a Live Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters > [Cluster] > Virtual Machines``
#. Select the VM to migrate
#. Click :guilabel:`Actions` > :guilabel:`Move`
#. Select the target host from the available hosts list
#. Confirm the migration

.. NOTE:: |morpheus| automatically determines whether to perform a live or cold migration based on the VM's current power state and storage configuration.

What Happens During Live Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. A migration lock is acquired to prevent concurrent migrations of the same VM
#. Storage pools are refreshed on the target host to ensure it can access the VM's disks
#. Network preparation ensures the target host has the correct bridge configurations
#. The ``virsh migrate`` command executes, transferring the VM's memory state to the target host
#. Upon completion, the VM's parent host reference is updated in |morpheus|
#. The migration lock is released

Migration Options
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Option
     - Description
   * - Migration Timeout
     - Maximum time allowed for the migration to complete before it is cancelled
   * - CPU Throttling
     - When enabled, throttles the VM's CPU during migration to help convergence for memory-intensive workloads

Cold Migration
--------------

Cold migration moves a powered-off VM to a different host. This is used when:

- The VM is powered off
- The VM has local storage that cannot be live-migrated
- Live migration failed and the VM was subsequently powered off

For cold migration, the VM's XML definition is relocated and storage volumes (if local) are copied to the target host.

VM Pinning
----------

VM pinning prevents a VM from being automatically migrated by maintenance mode evacuation or Dynamic Resource Scheduling (DRS). Pinned VMs remain on their assigned host unless manually moved by an administrator.

Use Cases
^^^^^^^^^

- VMs with host-level hardware dependencies (GPU passthrough, USB devices)
- License-bound VMs that must run on specific hosts
- VMs with local storage that cannot be migrated
- System VMs (cluster management agents)

Behavior of Pinned VMs
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Scenario
     - Behavior
   * - Maintenance mode
     - Pinned VMs are skipped during evacuation
   * - DRS rebalancing
     - Pinned VMs are excluded from placement calculations
   * - Host failure
     - Pinned VMs are **not** automatically failed over to another host
   * - Manual migration
     - Pinned VMs can be manually moved by an administrator

.. WARNING:: Pinned VMs on a failed host will not be automatically recovered. If the host fails, the pinned VM remains offline until the host recovers or an administrator manually intervenes.

Placement Strategy
-------------------

Each VM has a placement strategy that determines how |morpheus| handles its host assignment:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Strategy
     - Behavior
   * - Auto (default)
     - VM may be moved by DRS, maintenance mode, or failover. The preferred host is updated when the VM is migrated.
   * - Pinned
     - VM is locked to its current host. Only manual migration by an administrator can relocate it.

Dynamic Resource Scheduling (DRS)
----------------------------------

DRS automatically balances VM placement across cluster hosts based on resource utilization. DRS runs during each cluster sync cycle.

Modes
^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Mode
     - Description
   * - Failover Only (default)
     - DRS only moves VMs when a host has failed and VMs need to be restarted on surviving hosts
   * - Dynamic Placement
     - DRS actively rebalances VMs across hosts to distribute memory utilization evenly

DRS respects:

- VM pinning (pinned VMs are never moved by DRS)
- Maintenance mode flags (hosts in maintenance are excluded)
- Host-VM Group affinity and anti-affinity rules
- Available memory thresholds

Host-VM Groups (Affinity/Anti-Affinity)
----------------------------------------

Host-VM Groups define rules that control which hosts a VM may run on. These are configured at the cluster level and enforced during provisioning, migration, and DRS operations.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Group Type
     - Description
   * - Affinity
     - VMs in this group should run on the specified hosts. DRS will migrate non-compliant VMs to the preferred host when it has available capacity.
   * - Anti-Affinity
     - VMs in this group should NOT run on the same host. Ensures high availability by distributing replicas.
   * - Site Group
     - Groups hosts and VMs by physical site/location. Used in stretch cluster configurations for site-aware placement.

For detailed instructions on creating and managing Host-VM Groups, see :doc:`../host_vm_groups`.

DRS and Affinity Enforcement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When DRS runs with dynamic placement enabled, it evaluates affinity groups:

- VMs in an **affinity group** that are not on their preferred host are migrated back (if the preferred host is online and has capacity)
- VMs in an **anti-affinity group** that violate the rule (running on the same host as another group member) are migrated to separate hosts

.. NOTE:: Affinity rules are best-effort. If enforcing a rule would exceed host capacity or violate other constraints, the VM remains in its current location until conditions allow compliance.

VM Failover Behavior
---------------------

When a host fails (detected after 140 seconds of missed heartbeat writes), the Designated Coordinator assigns the failed host's VMs to surviving hosts:

#. VMs are assigned to hosts based on available memory (most available memory first)
#. Only VMs with ``auto`` placement strategy are failed over
#. Pinned VMs are not automatically restarted
#. VM XML definitions from the heartbeat directory are used to restart VMs on their assigned hosts

For detailed failover timelines and scenarios, see :doc:`failure_scenarios`.
