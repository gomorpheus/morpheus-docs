Cluster Updates
===============

Overview
^^^^^^^^

Cluster Updates allow administrators to apply software updates, patches, and configuration changes to cluster nodes in a controlled manner. The update workflow orchestrates rolling updates across cluster members to minimize downtime and ensure cluster stability throughout the process.

Cluster updates are supported for Kubernetes clusters, MVM clusters, and Docker clusters managed by |morpheus|.

Update Workflow
^^^^^^^^^^^^^^^

The cluster update process follows a managed workflow:

1. **Preparation** — |morpheus| evaluates the cluster state and determines which nodes need updates.
2. **Cordon** — Worker nodes are cordoned (marked as unschedulable) to prevent new workloads from being placed on them.
3. **Drain** — Existing workloads are gracefully evicted from the node being updated.
4. **Update** — The update is applied to the node (OS patches, Kubernetes version upgrade, package updates, etc.).
5. **Verify** — The node's health is verified after the update.
6. **Uncordon** — The node is uncordoned and made available for scheduling again.
7. **Next Node** — The process repeats for the next node in the cluster.

This rolling approach ensures that the cluster maintains availability throughout the update process.

Executing a Cluster Update
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters``
#. Click the name of the Cluster to update
#. Click :guilabel:`ACTIONS`
#. Select **Update**
#. Review the update details:

   UPDATE TYPE
     The type of update to apply:

     - **Kubernetes Version** — Upgrade Kubernetes components to a new version
     - **OS Patches** — Apply operating system security patches and updates
     - **Package Update** — Update installed addon packages

   TARGET VERSION
     The target version to update to (for version upgrades).
   NODES
     Select which nodes to include in the update. Options:

     - **All Nodes** — Update all cluster members (rolling)
     - **Workers Only** — Update only worker nodes
     - **Specific Nodes** — Select individual nodes to update

#. Click :guilabel:`EXECUTE`

Monitoring Update Progress
^^^^^^^^^^^^^^^^^^^^^^^^^^

Update progress can be monitored from the cluster's **History** tab:

- Each node update appears as a separate history entry
- Status indicators show: Queued, Running, Complete, or Failed
- Detailed logs are available by clicking on individual history entries

Update Status Values
^^^^^^^^^^^^^^^^^^^^

- **Queued** — Update is scheduled but not yet started
- **Running** — Update is actively being applied to a node
- **Complete** — Update finished successfully
- **Failed** — Update encountered an error (manual intervention may be required)
- **Cancelled** — Update was cancelled by an administrator

.. NOTE:: If a node update fails, the rolling update process pauses to allow investigation. The remaining nodes are not updated until the failure is resolved or the update is manually resumed.

Best Practices
^^^^^^^^^^^^^^

- **Test in non-production first** — Apply updates to development or staging clusters before production.
- **Review release notes** — Check for breaking changes in the target version before upgrading.
- **Ensure backup** — Take a cluster backup or snapshot before applying major updates.
- **Monitor capacity** — Ensure the cluster has sufficient capacity to handle workloads during the rolling update (when nodes are temporarily unavailable).
- **Schedule maintenance windows** — For production clusters, schedule updates during low-traffic periods.

.. WARNING:: Cluster updates cannot be easily rolled back. Ensure you have a recovery plan (such as cluster backups or the ability to rebuild nodes) before applying updates.
