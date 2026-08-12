HKS Node Maintenance
====================

HKS maintenance mode prevents new Pods from being scheduled on a node and attempts to evacuate eligible workloads before maintenance. |morpheus| automates the Kubernetes cordon and drain operations when **Enter Maintenance Mode** is selected and automates uncordon when maintenance mode is exited.

Before Maintenance
------------------

#. Confirm all cluster nodes report Ready and that no other node is already in maintenance.
#. Review PodDisruptionBudgets and ensure workloads have enough healthy replicas and capacity on other worker nodes.
#. Identify workloads that use ``emptyDir`` storage; draining with deletion enabled removes that node-local data.
#. Confirm DaemonSet Pods do not need evacuation. The automated drain ignores DaemonSets.

Worker Nodes
------------

#. Open the HKS worker node and select :menuselection:`ACTIONS --> Enter Maintenance Mode`.
#. Review the maintenance options before confirming. |morpheus| cordons the node and runs a drain operation; options can allow ignoring DaemonSets, forcing eviction, or deleting ``emptyDir`` data.
#. Follow the process output. If drain fails because of a disruption budget or non-evictable workload, stop and correct that condition rather than powering off the node.
#. Verify the node reports ``SchedulingDisabled`` and that application Pods have moved to healthy nodes. DaemonSet Pods can remain.
#. Complete maintenance, power the node on if necessary, and select **Exit Maintenance Mode**. |morpheus| uncordons the node. Confirm it reports Ready and accepts a test workload.

Control-plane Nodes
-------------------

Maintain one control-plane node at a time. Before entering maintenance, confirm another powered-on control-plane node is available to execute cluster operations and that removing the target node will preserve etcd quorum and Kubernetes API availability. Stop if quorum is already degraded or the remaining control-plane nodes are not healthy.

#. Enter maintenance mode from the control-plane node's Actions menu.
#. Monitor the cordon-and-drain process and verify the Kubernetes API remains available through another control-plane node.
#. Perform the planned maintenance without changing additional control-plane nodes.
#. Exit maintenance mode, then confirm the node is Ready, uncordoned, and participating normally before proceeding to another node.

.. warning:: Do not force a control-plane drain to bypass a quorum or API-availability problem. Resolve cluster health first.
