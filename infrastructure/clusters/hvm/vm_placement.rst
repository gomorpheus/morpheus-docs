VM Placement & Scheduling
=========================

VM Pinning
----------

VM pinning prevents a VM from being automatically migrated by maintenance mode evacuation or Dynamic Placement. Pinned VMs remain on their assigned host unless manually moved by an administrator.

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
   * - Dynamic Placement rebalancing
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
     - VM may be moved by Dynamic Placement, maintenance mode, or failover. The preferred host is updated when the VM is migrated.
   * - Pinned
     - VM is locked to its current host. Only manual migration by an administrator can relocate it.

Dynamic Placement
------------------

Dynamic Placement automatically balances VM placement across cluster hosts based on resource utilization. It runs during each cluster sync cycle.

Modes
^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Mode
     - Description
   * - Failover Only (default)
     - Dynamic Placement only moves VMs when a host has failed and VMs need to be restarted on surviving hosts
   * - Dynamic Placement
     - Actively rebalances VMs across hosts to distribute memory utilization evenly

Dynamic Placement respects:

- VM pinning (pinned VMs are never moved)
- Maintenance mode flags (hosts in maintenance are excluded)
- Host-VM Group affinity and anti-affinity rules
- Available memory thresholds

Host-VM Groups (Affinity/Anti-Affinity)
----------------------------------------

Host-VM Groups define rules that control which hosts a VM may run on. These are configured at the cluster level and enforced during provisioning, migration, and Dynamic Placement operations.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Group Type
     - Description
   * - Affinity
     - VMs in this group should run on the specified hosts. Dynamic Placement will migrate non-compliant VMs to the preferred host when it has available capacity.
   * - Anti-Affinity
     - VMs in this group should NOT run on the same host. Ensures high availability by distributing replicas.
   * - Site Group
     - Groups hosts and VMs by physical site/location. Used in stretch cluster configurations for site-aware placement.

For detailed instructions on creating and managing Host-VM Groups, see :doc:`host_vm_groups`.

Dynamic Placement and Affinity Enforcement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When Dynamic Placement runs with dynamic placement enabled, it evaluates affinity groups:

- VMs in an **affinity group** that are not on their preferred host are migrated back (if the preferred host is online and has capacity)
- VMs in an **anti-affinity group** that violate the rule (running on the same host as another group member) are migrated to separate hosts

.. NOTE:: Affinity rules are best-effort. If enforcing a rule would exceed host capacity or violate other constraints, the VM remains in its current location until conditions allow compliance.

Memory Overcommit
-----------------

By default, |morpheus| treats VM memory allocations as hard reservations — a VM can only be placed on a host with enough free physical memory to fully back the allocation. Memory overcommit allows you to allocate more memory to VMs than the host physically has available, under the assumption that not all VMs will use their full allocation simultaneously.

Configuring Memory Overcommit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Memory overcommit is set **per host** from the host detail page:

#. Navigate to the host detail page (|InfClu| > select cluster > Hosts tab > select host)
#. Click :guilabel:`Edit`
#. Set the **Overcommit Percent** field to the desired value
#. Click :guilabel:`Save`

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Value
     - Behavior
   * - 100 (default)
     - No overcommit. VMs can only be placed if the host has enough physical memory for the full allocation.
   * - 150
     - The host advertises 150% of its physical memory as available for VM placement. A host with 128 GB of RAM would allow up to 192 GB of total VM memory allocations.
   * - 200
     - The host advertises 200% of its physical memory. A 128 GB host would allow up to 256 GB of total VM allocations.

How Overcommit Affects Placement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When |morpheus| selects a host for a new VM, it calculates available memory as:

``available = (host physical memory × overcommit percent) - reserved memory - allocated VM memory``

A host is only eligible for placement if this calculated available memory exceeds the new VM's memory requirement. This means overcommit expands the pool of eligible hosts but does not bypass the placement check entirely.

Dynamic Placement also uses the overcommit-adjusted memory when evaluating rebalancing decisions.

Overcommit Alarms
^^^^^^^^^^^^^^^^^^

When the total allocated VM memory on a host exceeds the host's physical memory capacity (adjusted by the overcommit percent), |morpheus| raises a **Host Memory Over-Committed** alarm. This alarm indicates that the host is approaching or has exceeded its overcommit threshold and may experience performance degradation if VMs simultaneously consume their full allocations.

.. WARNING:: Memory overcommit can lead to performance and stability issues if overused. When VMs on an overcommitted host simultaneously consume their full memory allocations, the host may experience severe memory pressure, swapping, or out-of-memory conditions. Consider adding swap partitions to hosts with overcommit enabled and monitor memory utilization closely.
