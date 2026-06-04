Server Migration
----------------

Overview
^^^^^^^^

|morpheus| supports migrating virtual machines between hosts, clusters, or resource pools within a cloud. The migration (also referred to as VM Move) allows you to relocate a workload to a different compute target without reprovisioning.

Migration is supported for cloud types that provide native VM mobility, such as VMware vSphere (vMotion), Nutanix AHV, and other hypervisor platforms.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Compute`` role permission at **Full** level is required to perform migrations.

Migrating a Server
^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Compute > Virtual Machines`` or to the server detail page
#. Select the target server
#. Click :guilabel:`ACTIONS`
#. Select **Migrate**
#. In the migration dialog, configure:

   TARGET HOST
     Select the destination hypervisor host. Available hosts are filtered based on the server's current cloud and compatibility.
   TARGET RESOURCE POOL
     Select the destination resource pool or cluster (if applicable). This may be required for cross-cluster migrations.
   TARGET DATASTORE
     Select the destination datastore for the VM's storage (for storage migrations or combined compute+storage moves).
   PRIORITY
     Migration priority level (where supported by the hypervisor):

     - **Low** — Background migration with minimal impact
     - **Normal** — Standard priority
     - **High** — Prioritized migration

#. Click :guilabel:`EXECUTE`

The migration operation runs asynchronously. Progress can be monitored on the server's History tab.

Migration Types
^^^^^^^^^^^^^^^

Live Migration (vMotion)
  The VM is moved while running, with no downtime. Requires shared storage or storage vMotion capability between source and destination hosts.

Cold Migration
  The VM is powered off, moved to the new location, and optionally powered back on. Used when live migration prerequisites are not met.

Storage Migration
  Only the VM's storage is relocated to a different datastore. The VM remains on the same host.

.. NOTE:: Migration availability and options depend on the underlying cloud type and hypervisor capabilities. Not all cloud types support all migration modes.

Monitoring Migration Status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Migration operations appear in the server's **History** tab with status indicators:

- **Running** — Migration is in progress
- **Complete** — Migration finished successfully
- **Failed** — Migration encountered an error (check event details for the failure reason)
