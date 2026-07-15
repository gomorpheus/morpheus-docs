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

Configuring Dynamic Placement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dynamic Placement settings are configured when editing a cluster:

#. Navigate to |InfClu| and select the cluster
#. Click :guilabel:`Edit`
#. Enable the **Dynamic Placement** toggle to activate DRS for the cluster
#. Set the **Aggressiveness** level to control how actively VMs are rebalanced
#. Click :guilabel:`Save`

When Dynamic Placement is disabled (the default), the cluster operates in Failover Only mode and no automatic rebalancing occurs.

Aggressiveness Levels
^^^^^^^^^^^^^^^^^^^^^^

The aggressiveness level controls how readily |morpheus| migrates VMs to rebalance the cluster. Higher aggressiveness results in tighter balancing but more frequent live migrations. Three levels are available:

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Level
     - Description
   * - Conservative (default)
     - Tolerates significant imbalance before acting. Best for production workloads where minimizing migrations is a priority.
   * - Moderate
     - Balances migration frequency against cluster evenness. Suitable for mixed workloads.
   * - Aggressive
     - Actively pursues even distribution across hosts. Appropriate for clusters where balanced resource utilization is more important than migration overhead.

Threshold Parameters
^^^^^^^^^^^^^^^^^^^^^

Each aggressiveness level sets a group of threshold parameters that govern the DRS algorithm:

.. list-table::
   :widths: 25 15 15 15 50
   :header-rows: 1

   * - Parameter
     - Conservative
     - Moderate
     - Aggressive
     - Description
   * - Imbalance Threshold
     - 1.5
     - 1.4
     - 1.2
     - A host is considered overloaded when its memory usage exceeds the cluster mean multiplied by this value. At 1.5 (conservative), a host must be 50% above the mean before any migration is considered.
   * - Target Low Threshold
     - 0.9
     - 0.95
     - 1.0
     - A destination host is eligible to receive a VM only if its memory and CPU usage are below the cluster mean multiplied by this value. At 0.9 (conservative), the target must be at least 10% below the mean.
   * - Cooldown Period
     - 60 min
     - 30 min
     - 15 min
     - Minimum time after a VM has been migrated before it can be moved again. Prevents VMs from bouncing between hosts.
   * - Max Moves Per Cycle
     - 2
     - 3
     - 5
     - Maximum number of VM migrations that can occur in a single DRS evaluation cycle (each cluster sync).
   * - Min Std Dev Improvement
     - 8%
     - 5%
     - 2%
     - A proposed migration is only executed if it would reduce the cluster's resource utilization standard deviation by at least this percentage. Prevents marginal moves that provide little benefit.
   * - CV Threshold
     - 0.08
     - 0.05
     - 0.03
     - The coefficient of variation (standard deviation / mean) for both memory and CPU across all hosts. If the cluster CV is already below this value, DRS skips balancing entirely because the cluster is considered well-balanced.

How the Algorithm Works
^^^^^^^^^^^^^^^^^^^^^^^^

During each cluster sync cycle, Dynamic Placement evaluates the cluster as follows:

#. **Cluster balance check** — Calculate the coefficient of variation (CV) for memory and CPU across all hosts. If both values are below the CV Threshold, the cluster is considered balanced and no action is taken.
#. **Identify overloaded hosts** — Hosts whose memory usage exceeds the mean multiplied by the Imbalance Threshold are flagged.
#. **Select VMs to move** — On each overloaded host, eligible VMs are evaluated for migration. A VM is eligible if it uses the ``Auto`` placement strategy, has no local storage or assigned devices, is powered on, is not in an active backup, is not in an affinity group, and has not been migrated within the cooldown period.
#. **Select target hosts** — Target hosts must have memory and CPU usage below the mean multiplied by the Target Low Threshold. The move is also validated to ensure it would not push the target host above the Imbalance Threshold.
#. **Validate improvement** — The algorithm simulates the move and confirms it would reduce the cluster's standard deviation by at least the Min Std Dev Improvement percentage.
#. **Execute migrations** — Approved moves are executed up to the Max Moves Per Cycle limit.

.. NOTE:: Dynamic Placement uses the overcommit-adjusted memory values when evaluating hosts. See the :ref:`Memory Overcommit` section below for details.

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
