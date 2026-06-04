.. _vdi-allocations:

VDI Allocations
================

Overview
--------

VDI Allocations represent the assignment of a VDI Pool instance to a specific user. When a user requests a virtual desktop session, |morpheus| creates an allocation that binds an available Instance from the pool to that user for the duration of their session (non-persistent pools) or indefinitely (persistent pools).

Allocations are managed automatically by |morpheus| but can be monitored and manually managed by administrators.

Allocation Lifecycle
---------------------

Each allocation progresses through the following statuses:

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - Status
     - Description
     - Next State
   * - preparing
     - Instance is being provisioned or started for the user
     - available / failed
   * - available
     - Instance is ready and waiting for user connection
     - reserved
   * - reserved
     - Instance is actively assigned to a user session
     - releasing / shutdown
   * - starting
     - Instance is being powered on (persistent pools, returning user)
     - reserved
   * - releasing
     - Session has ended; instance is being released back to the pool
     - (destroyed for non-persistent)
   * - shutdown
     - Instance has been shut down (persistent pools after timeout)
     - starting (on next request)
   * - repossess
     - Allocation is being forcibly reclaimed
     - (destroyed)
   * - failed
     - Instance failed to provision or start
     - (requires admin intervention)
   * - unknown
     - State cannot be determined
     - (requires admin intervention)

Allocation Behavior by Pool Type
----------------------------------

Non-Persistent Pools
^^^^^^^^^^^^^^^^^^^^

- When a user requests a desktop, an available allocation is assigned
- When the lease timeout expires after disconnect, the Instance is **destroyed**
- A new Instance is provisioned to maintain the pool's minimum size
- User data is not preserved between sessions

Persistent Pools
^^^^^^^^^^^^^^^^

- On first request, a new allocation is created and bound to the user permanently
- When the lease timeout expires, the Instance is **shut down** (not destroyed)
- On next request, the same Instance is powered back on
- User data, installed applications, and customizations are preserved

Viewing Allocations
--------------------

Administrators can view allocations through:

Via VDI Pool Detail
^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Tools > VDI Pools``
#. Select a pool
#. View the Allocations tab showing all current allocations for that pool

Via API
^^^^^^^

``GET /api/vdi-allocations`` returns all allocations with filtering support:

- Filter by pool: ``?vdiPoolId=<id>``
- Filter by user: ``?userId=<id>``
- Filter by status: ``?status=reserved``

Allocation Fields
^^^^^^^^^^^^^^^^^^

Each allocation record contains:

- **Pool** — The parent VDI Pool
- **Instance** — The assigned |morpheus| Instance
- **User** — The assigned user (null if unassigned/available)
- **Status** — Current allocation status
- **Persistent** — Whether this is a persistent allocation
- **Recyclable** — Whether the allocation can be recycled (reused)
- **Release Date** — When the allocation will be released (after timeout)
- **Last Reserved** — Timestamp of last user assignment
- **Sessions** — Active VDI sessions on this allocation

Lease Timeout Behavior
-----------------------

The lease timeout controls when allocations are released after user disconnect:

- **Non-persistent pools:** Recommended timeout of ~10 minutes. After expiry, the VM is destroyed.
- **Persistent pools:** Recommended timeout of ~1 hour. After expiry, the VM is shut down.

.. IMPORTANT:: Lease timeouts auto-extend for as long as the user is logged into or browsing any area of the |morpheus| application. Once the user closes their browser or logs out, timeouts stop auto-extending.

Pool Sizing and Allocations
-----------------------------

Allocations interact with pool sizing parameters:

- **Minimum Idle** — Minimum number of available (unassigned) allocations to maintain. |morpheus| proactively provisions instances to meet this threshold.
- **Initial Pool Size** — Number of instances provisioned when the pool is created.
- **Maximum Pool Size** — Hard cap on total allocations (reserved + available).

When an allocation is released (non-persistent), the pool controller checks if the available count has dropped below the minimum idle threshold and provisions replacements.

Managing Allocations
---------------------

Releasing an Allocation
^^^^^^^^^^^^^^^^^^^^^^^

Administrators can force-release an allocation:

- This disconnects any active user session
- For non-persistent pools: triggers instance destruction
- For persistent pools: triggers instance shutdown

Viewing Session Details
^^^^^^^^^^^^^^^^^^^^^^^

Each allocation tracks its VDI sessions (``VdiSession`` records) which contain:

- Session start/end times
- Connection protocol (RDP, VNC)
- Client information
- Session duration

Local User Creation
^^^^^^^^^^^^^^^^^^^^

The ``localUserCreated`` field tracks whether |morpheus| has created the user's local account on the VDI desktop. This ensures:

- Windows domain credentials or local accounts are configured on first use
- Subsequent sessions reuse the existing local account
- User profiles are available immediately on connection

Troubleshooting
----------------

- **Allocation stuck in "preparing":** Check the Instance provisioning status in ``Provisioning > Instances``. The underlying VM may have failed to provision.
- **Allocation stuck in "releasing":** The Instance destruction may be failing. Check cloud connectivity and VM power state.
- **No available allocations:** Pool may be at maximum capacity or minimum idle threshold is set too low for demand.
- **User cannot connect:** Verify the allocation status is "reserved" and the Instance is powered on. Check Guacamole connectivity.
- **Persistent allocation not preserving data:** Ensure the pool type is set to Persistent and the Instance is shutting down (not being destroyed).
