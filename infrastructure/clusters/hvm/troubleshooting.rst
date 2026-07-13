Troubleshooting & Diagnostics
==============================

Quick Health Check (UI)
-----------------------

Navigate to ``Infrastructure > Clusters > [Cluster] > Summary > Quorum`` panel.

The Quorum panel displays:

- Quorum status (ACHIEVED / LOST)
- Total nodes / reachable / online / offline count
- Fenced node count
- Designated Coordinator
- Down hosts
- Lockspaces status
- Configured datastores
- Witness status
- Site information

Diagnostic Commands
-------------------

.. NOTE:: HVM 1.3 does not use Pacemaker or ``pcs`` commands. Use the commands below for all cluster diagnostics.

Corosync
^^^^^^^^

In HVM 1.3, Corosync provides the node membership list to DLM but is **not** used for quorum decisions. The |morpheus| Agent runs its own quorum system (via the ``morphd`` QuorumCheckService), which is how split quorum is achieved for stretch clusters and two-node GFS2 configurations. Corosync's ``Quorate`` state has no impact on cluster operation.

List cluster members:

.. code-block:: bash

   corosync-quorumtool -l

Query Corosync configuration map:

.. code-block:: bash

   corosync-cmapctl

DLM
^^^

Check DLM status (verbose):

.. code-block:: bash

   dlm_tool status -v

List DLM lockspaces:

.. code-block:: bash

   dlm_tool ls

Manually acknowledge a fence (use with caution):

.. code-block:: bash

   dlm_tool fence_ack <node_id>

Agent Quorum
^^^^^^^^^^^^

Query the agent quorum endpoint (returns JSON):

.. code-block:: bash

   curl -k https://localhost:7443/quorum

View cluster member configuration:

.. code-block:: bash

   cat /opt/morpheus-node/.quorum-nodes

View heartbeat configuration:

.. code-block:: bash

   cat /opt/morpheus-node/.hb

View mounted datastores:

.. code-block:: bash

   cat /opt/morpheus-node/.mounts

GFS2 Filesystem
^^^^^^^^^^^^^^^

Check active GFS2 mounts:

.. code-block:: bash

   mount | grep gfs2

Check for GFS2 withdrawal:

.. code-block:: bash

   cat /sys/fs/gfs2/*/withdraw

Check for hanging mounts:

.. code-block:: bash

   ps -aux | grep mount

Log Files
^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Log Location
     - Contents
   * - ``/var/log/dlm_controld/dlm_controld.log``
     - DLM control daemon log
   * - ``/var/log/kern.log``
     - Kernel messages (GFS2/DLM events)
   * - ``journalctl -u dlm``
     - DLM systemd journal
   * - ``dmesg``
     - Kernel ring buffer (recent events)

Common Issues
-------------

Node Unreachable
^^^^^^^^^^^^^^^^

**Symptoms:** Node shows as OFFLINE in the Quorum panel.

**Resolution:**

#. Verify the |morpheus| agent is running on the affected host
#. Check network connectivity between hosts
#. Confirm port 7443 is open and accessible
#. Check agent logs for connectivity errors

DLM Wait Fencing
^^^^^^^^^^^^^^^^^

**Symptoms:** DLM operations stall, waiting for fence acknowledgement.

**Resolution:**

- The |morpheus| agent should automatically issue ``fence_ack`` after confirming the fenced node cannot access storage
- If automatic fencing is not resolving:

  .. code-block:: bash

     dlm_tool fence_ack <node_id>

.. WARNING:: Only issue a manual ``fence_ack`` if you have confirmed the target node can no longer access shared storage. Incorrect use can lead to data corruption.

GFS2 Withdrawn
^^^^^^^^^^^^^^

**Symptoms:** GFS2 filesystem enters withdrawn state, I/O operations fail.

**Resolution:**

#. Attempt to unmount and remount the filesystem
#. If remount fails, reboot the affected host
#. Investigate the cause (storage connectivity, DLM issue) before the host rejoins

Corosync Shows Not Quorate
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptoms:** ``corosync-quorumtool -s`` shows ``Quorate: No``.

**Impact:** In HVM 1.3, this has **no impact** on cluster operation. The |morpheus| Agent manages its own quorum independently of Corosync's quorate state. Corosync is used only to provide a node list to DLM, not for quorum decisions.

**When this occurs:**

- One or more nodes are down or a network partition has occurred
- This is expected in two-node clusters and stretch cluster configurations where Corosync alone cannot achieve majority quorum

**Resolution:**

- No action is required for the Corosync quorate state itself
- Check the |morpheus| Agent quorum endpoint (``curl -k https://localhost:7443/quorum``) to verify the actual cluster quorum status
- If the Agent quorum also shows issues, investigate network connectivity between hosts and ensure the |morpheus| Agent is running on all nodes

APD Activated
^^^^^^^^^^^^^

**Symptoms:** VMs on shared storage have been shut down automatically.

**Resolution:**

#. Restore storage connectivity to the affected host
#. Restart the affected VMs once storage is confirmed healthy
#. Investigate the root cause of the storage path failure

Agent Not Sending Quorum
^^^^^^^^^^^^^^^^^^^^^^^^

**Symptoms:** Agent is running but quorum data is not being sent or received.

**Resolution:**

#. Check ``/opt/morpheus-node/.quorum-nodes`` exists and contains valid cluster member data
#. Verify agent connectivity to other cluster hosts on port 7443
#. Restart the agent if configuration is correct but quorum is not functioning

Emergency Procedures
--------------------

.. WARNING:: Emergency procedures should only be used when automated recovery has failed. Incorrect use can lead to data loss or split-brain conditions.

Force Rejoin a Fenced Node
^^^^^^^^^^^^^^^^^^^^^^^^^^

Reboot the fenced node. Upon boot, the agent will re-enter the quorum cycle and rejoin the cluster when healthy.

Clear Stuck DLM
^^^^^^^^^^^^^^^

.. code-block:: bash

   dlm_tool fence_ack <node_id>

.. IMPORTANT:: Only use this command if you have confirmed the target node cannot access shared storage. This tells DLM the node is safely fenced.

Force Restart Cluster Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   systemctl restart corosync
   systemctl restart dlm

.. WARNING:: Use extreme caution restarting cluster services in production. This will temporarily disrupt cluster communication and may trigger fencing of the restarted node.
