Stretch Clusters & Witness Nodes
=================================

Overview
--------

A stretch cluster extends an HVM 1.3 cluster across two physical sites with a witness node in a third location for tie-breaking arbitration. This provides site-level fault tolerance while maintaining a single cluster management domain.

Requirements
------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Requirement
     - Details
   * - Hosts
     - Minimum 6 hosts (3 per site)
   * - Witness
     - 1 Distributed Worker deployed in a 3rd site
   * - Network
     - All hosts must be able to communicate with the witness, the |morpheus| manager, and each other

Witness Deployment
------------------

The witness node is a |morpheus| Distributed Worker deployed at a third site, independent from both cluster sites.

Creating the Worker Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Administration > Integrations > Distributed Workers``
#. Create a new worker configuration
#. Save the API key provided

Installing the Worker
^^^^^^^^^^^^^^^^^^^^^

On the witness host or VM:

#. Download the ``morpheus-worker`` package
#. Install with ``dpkg``:

   .. code-block:: bash

      dpkg -i morpheus-worker_<version>.deb

#. Edit ``/etc/morpheus/morpheus-worker.rb``:

   .. code-block:: ruby

      worker_url = '<URL from worker config>'
      worker['appliance_url'] = '<Morpheus appliance URL>'
      worker['apikey'] = '<any value>'
      worker['worker_key'] = '<API key from worker config>'

#. Reconfigure the worker:

   .. code-block:: bash

      morpheus-worker-ctl reconfigure

#. Verify the worker is running:

   .. code-block:: bash

      morpheus-worker-ctl tail worker

Cluster Deployment for Stretch
------------------------------

.. IMPORTANT:: Do NOT choose a witness during initial cluster creation. The witness must be added after the cluster is deployed.

#. Create the HVM cluster normally following the standard process (see :doc:`building_clusters`)
#. After deployment completes, navigate to ``Infrastructure > Clusters > [Cluster]``
#. Click :guilabel:`Edit`
#. Select the Witness Worker from the dropdown
#. Click :guilabel:`Save Changes`

Adding HPE Clustered Datastore (Shared LUN)
--------------------------------------------

Adding a Shared LUN to the cluster activates the quorum service. Quorum is not needed until shared storage is present.

.. NOTE:: Monitor host and worker logs for quorum status messages after adding shared storage.

Site Group Configuration
------------------------

Site groups define which hosts belong to each physical site for arbitration decisions.

#. Navigate to ``Infrastructure > Clusters > [Cluster] > Resources > Host / VM Groups``
#. Click :guilabel:`Add`
#. Create a Site Group with:

   - **Site Name**: A name for the site (e.g., "Site-A")
   - **Servers**: Select the hosts at this site

#. Repeat for the second site

.. WARNING:: Do NOT use ``siteWitness`` as a site group name. This name is reserved for automatic witness assignment. The witness is automatically assigned to the ``siteWitness`` group when the first site group is created.

Arbitration Behavior
--------------------

When a site failure occurs, the following arbitration logic is executed:

Failure Detection
^^^^^^^^^^^^^^^^^

A site is considered failed when ALL non-witness nodes at that site become unreachable (60-second timeout).

Decision Logic
^^^^^^^^^^^^^^

#. The surviving site checks: can I reach the witness?

   - **No** → The surviving site self-fences (cannot confirm it is the correct winner)
   - **Yes** → Proceed with arbitration

#. The alphabetically first site name always wins (deterministic tie-breaking)

Winner Actions
^^^^^^^^^^^^^^

The winning site:

- Adjusts Corosync votes to maintain quorum with remaining nodes
- Issues ``fence_ack`` for nodes at the failed site

Loser Actions
^^^^^^^^^^^^^

The losing site:

- Self-fences (stops DLM and Corosync)

Recovery
^^^^^^^^

After the failed site is restored:

- 3 consecutive healthy ping cycles (~3 minutes) must pass
- Corosync votes are restored to normal values
- Fenced nodes are rebooted and rejoin the cluster

NFS-Based Stretch Clusters
---------------------------

As an alternative to HPE Clustered Datastores (shared LUN), stretch clusters can use **NFS-backed storage** with multipath connectivity. This approach is simpler to configure because it does not require Corosync, DLM, or the quorum/arbitration services — NFS handles concurrent access at the protocol level.

When to Use NFS for Stretch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NFS-backed stretch clusters are appropriate when:

- You already have enterprise NFS infrastructure (e.g., NetApp, Pure Storage, HPE Alletra) with multipath or multi-site replication
- You want to avoid the complexity of Corosync/DLM fencing and quorum management
- Your NFS appliance provides its own high availability (active/passive failover, synchronous replication across sites)
- You need a simpler operational model with fewer moving parts

.. note::

   The tradeoff is that HA behavior depends on the NFS appliance's own failover capabilities rather than the cluster-managed quorum system. Ensure your NFS infrastructure provides the level of availability your workloads require.

Requirements
^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Requirement
     - Details
   * - Hosts
     - Minimum 2 hosts (1 per site for basic stretch, more for capacity)
   * - NFS Storage
     - Enterprise NFS appliance accessible from all hosts at both sites with multipath or replicated access
   * - Network
     - All hosts must reach the NFS endpoint(s). Low-latency cross-site links are recommended for write-heavy workloads.
   * - Witness
     - Optional. A witness is not strictly required since there is no Corosync quorum to arbitrate, but can still be configured for |morpheus|-level site awareness.

.. important::

   NFS storage must be presented as a single mountable endpoint (or a pair of endpoints for multipath) that is accessible from both sites simultaneously. If your NFS solution uses synchronous replication between sites, ensure both sites mount the same namespace.

Cluster Setup with NFS Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Deploy the HVM cluster following the standard process (see :doc:`building_clusters`)
#. When configuring storage, choose **NFS Pool** rather than HPE Clustered Datastore
#. Add the NFS datastore to the cluster:

   - Navigate to ``Infrastructure > Clusters > [Cluster] > Storage``
   - Click :guilabel:`Add Datastore`
   - Select **NFS** as the type
   - Enter the NFS server address and export path
   - The NFS mount is configured on all hosts in the cluster automatically

#. If stretching across sites, ensure the NFS endpoint is reachable from hosts at both sites before adding hosts from the second site

Adding Hosts at the Second Site
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the cluster is running with NFS storage at the primary site:

#. Prepare additional HVM hosts at the second site (see :doc:`/getting_started/installation/hvm_host_prep`)
#. Ensure the NFS endpoint is mountable from the second site hosts
#. Add the hosts to the existing cluster: ``Infrastructure > Clusters > [Cluster] > Actions > Add Host``
#. |morpheus| will configure the new hosts and mount the NFS datastore automatically

Workloads can now be migrated between hosts across sites using Live Migration, provided the NFS storage is accessible from both source and destination hosts.

Multipath NFS Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For resilient NFS access across sites, configure multipath at the network or NFS appliance level:

- **Active/Active NFS endpoints** — If your NFS solution provides multiple access points (e.g., data LIFs across sites), configure DNS round-robin or a load-balanced VIP that routes to the nearest healthy endpoint
- **Active/Passive failover** — If the NFS appliance fails over between sites, ensure the failover IP/VIP is consistent and that hosts reconnect automatically after failover (standard NFS client behavior with ``hard`` mount option)
- **Synchronous replication** — For read/write access from both sites simultaneously, the NFS backend must support synchronous replication. Asynchronous replication introduces the risk of data loss on site failure.

.. tip::

   Use the ``hard`` and ``intr`` NFS mount options in production to ensure clients wait for the NFS server to recover rather than returning errors to applications during brief network interruptions.

Failover Behavior
^^^^^^^^^^^^^^^^^^

Unlike the shared LUN model (which uses Corosync/DLM quorum and active fencing), NFS-based stretch clusters rely on:

- **NFS appliance failover** — The storage layer handles its own HA. When the NFS endpoint fails over, hosts reconnect and I/O resumes.
- **|morpheus| host monitoring** — |morpheus| detects host unreachability and can trigger workload migration to surviving hosts (via DRS/Dynamic Placement policies).
- **No fencing required** — Since NFS handles locking at the protocol level (NLM/NFSv4 leases), there is no risk of split-brain data corruption that requires active fencing.

If a full site fails:

#. |morpheus| detects hosts at the failed site as unreachable
#. If Dynamic Placement is enabled with appropriate aggressiveness, workloads are automatically migrated to surviving hosts
#. Manual migration can be triggered from ``Infrastructure > Clusters > [Cluster] > [Host] > Actions > Evacuate``
#. When the failed site recovers, hosts rejoin the cluster and become available for workload placement again

Limitations
^^^^^^^^^^^^

- **Performance** — NFS adds network overhead compared to local/Ceph storage. Cross-site NFS access is subject to network latency.
- **No cluster-level quorum** — The cluster does not independently arbitrate site failures. Failover depends on your NFS appliance's HA capabilities and |morpheus| Dynamic Placement settings.
- **Write performance across sites** — If hosts at both sites write to the same NFS volume, write performance is bounded by cross-site network latency (especially with synchronous replication).
- **Not suitable for all workloads** — Latency-sensitive applications (databases, real-time systems) may not perform well on cross-site NFS. Consider placing these workloads on local storage or site-local NFS exports.
