Host-VM Groups
--------------

Overview
^^^^^^^^

Host-VM Groups define affinity and anti-affinity rules that control the placement of virtual machines on specific hosts within a cloud or cluster. These groups allow administrators to:

- Pin VMs to specific hosts (affinity)
- Prevent VMs from running on the same host (anti-affinity)
- Group hosts and VMs for licensing, compliance, or performance requirements

Host-VM Groups can be configured at the Cloud level or the Cluster (Server Group) level.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Clouds`` or ``Infrastructure: Clusters`` role permission at **Full** or **Group** access is required to create, edit, or delete Host-VM Groups.
- **Read** access allows viewing Host-VM Groups only.

Viewing Host-VM Groups
^^^^^^^^^^^^^^^^^^^^^^

From a Cloud:

#. Navigate to ``Infrastructure > Clouds``
#. Click the name of a Cloud
#. Select the **HOST-VM GROUPS** tab

From a Cluster:

#. Navigate to ``Infrastructure > Clusters``
#. Click the name of a Cluster
#. Select the **HOST-VM GROUPS** tab

The list displays all configured Host-VM Groups with their name, type, and member count.

Creating a Host-VM Group
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the Cloud or Cluster detail page
#. Select the **HOST-VM GROUPS** tab
#. Click :guilabel:`+ ADD`
#. Configure the following fields:

   NAME
     A descriptive name for the group.
   TYPE
     The group type determines the placement behavior:

     - **Affinity** — VMs in this group should run on the specified hosts. Use for workloads that need to be co-located.
     - **Anti-Affinity** — VMs in this group should NOT run on the same host. Use for high-availability configurations.
     - **Site Group** — (Cluster-level only) Groups hosts and VMs by site/location.

   RESOURCE POOL
     (Cloud-level groups) Select the resource pool that this group applies to.
   SERVERS
     Select the hosts (hypervisor servers) that are members of this group. Multiple hosts can be selected.
   TENANT PERMISSIONS
     Control which tenants can see and use this Host-VM Group:

     - **Public** — Visible to all tenants
     - **Private** — Visible only to selected tenants

#. Click :guilabel:`SAVE CHANGES`

Editing a Host-VM Group
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the Cloud or Cluster detail page
#. Select the **HOST-VM GROUPS** tab
#. Click the edit icon next to the group
#. Modify the desired fields (name, servers, permissions)
#. Click :guilabel:`SAVE CHANGES`

Deleting a Host-VM Group
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the Cloud or Cluster detail page
#. Select the **HOST-VM GROUPS** tab
#. Click the delete icon next to the group
#. Confirm the deletion in the prompt

.. WARNING:: Deleting a Host-VM Group removes the affinity/anti-affinity constraint. Existing VMs will not be automatically migrated but future placement decisions will no longer consider the deleted rule.

Use Cases
^^^^^^^^^

High Availability
  Create an anti-affinity group containing VMs that form an HA cluster (e.g., database replicas). This ensures they are placed on different hosts so that a single host failure does not take down all replicas.

Licensing Compliance
  Create an affinity group to ensure VMs that require specific host-level licenses (e.g., Oracle, SQL Server) are placed only on properly licensed hosts.

Performance Isolation
  Create affinity groups to co-locate VMs that frequently communicate with each other, reducing network latency.

.. NOTE:: Host-VM Groups are enforced by |morpheus| during provisioning and migration operations. The underlying hypervisor's native DRS/affinity rules may also apply depending on the cloud configuration.
