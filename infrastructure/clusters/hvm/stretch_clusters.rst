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
