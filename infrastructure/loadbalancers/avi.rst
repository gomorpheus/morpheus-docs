Avi Networks (NSX ALB) Load Balancers
--------------------------------------

Overview
^^^^^^^^

|morpheus| integrates with Avi Networks (now VMware NSX Advanced Load Balancer) to provide application delivery services. The integration syncs virtual services, pools, SSL profiles, health monitors, and cloud configurations from the Avi Controller.

Adding an Avi Load Balancer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Load Balancers``
#. Click :guilabel:`+ ADD`
#. Select **AVI**
#. Fill in the following:

   GROUP
     Select the Group the Load Balancer will be available for.
   CLOUD
     Select the Cloud the Load Balancer will be available for.
   NAME
     Name of the Load Balancer in |morpheus|.
   DESCRIPTION
     Identifying information displayed on the Load Balancer list page.
   VISIBILITY
     Define Multi-Tenant visibility. **Public** allows all Tenants to see the load balancer. **Private** restricts to selected Tenants.
   API HOST
     IP address or FQDN of the Avi Controller.
   API PORT
     Controller API port (default: ``443``).
   USERNAME
     Avi Controller user with appropriate privileges.
   PASSWORD
     Password for the Avi Controller user.
   INTERNAL IP
     The internal VIP address.
   PUBLIC IP
     The external/public IP address (if applicable).
   VIP ADDRESS
     Virtual IP address for load balancing.
   VIP PORT
     Port the VIP listens on (e.g., ``80``, ``443``).

#. Click :guilabel:`SAVE CHANGES`

Once connected, |morpheus| will validate the credentials and begin syncing data from the Avi Controller.

Synced Resources
^^^^^^^^^^^^^^^^

After successful integration, |morpheus| periodically syncs the following from the Avi Controller:

Pools
  Backend server pools with their members and health status.

Virtual Services
  Virtual server configurations including VIP addresses, ports, and pool assignments.

SSL Profiles
  TLS/SSL profiles configured on the Avi Controller for certificate management.

Health Monitors
  Health check configurations used by pools to verify backend server availability.

Clouds
  Avi Cloud configurations that define the infrastructure environment (e.g., VMware, AWS, Azure, OpenStack).

Virtual Servers Tab
^^^^^^^^^^^^^^^^^^^

The Virtual Servers tab on the Avi load balancer detail page displays all virtual services synced from the controller. Each entry shows:

- **Name** — Virtual service name
- **VIP Address** — The IP address and port the service listens on
- **Pool** — The associated backend pool
- **Status** — Operational status (enabled/disabled)

Pools Tab
^^^^^^^^^

The Pools tab displays backend server pools:

- **Name** — Pool name
- **Members** — Number of backend servers in the pool
- **Health Monitor** — The health check applied to pool members
- **Status** — Pool operational status

Profiles
^^^^^^^^

Avi SSL profiles are synced and available for selection when configuring virtual servers. See :ref:`lb_profiles` for general profile management.

Status and Monitoring
^^^^^^^^^^^^^^^^^^^^^

|morpheus| monitors the Avi Controller connectivity and updates status:

- **OK** — Connected and syncing normally
- **Error** — Connection or authentication failure
- **Offline** — Avi Controller API is not reachable

A health alarm is raised when connectivity issues are detected.

.. NOTE:: The Avi integration uses session-based authentication with automatic token refresh. Ensure the configured user account does not have password expiration policies that would interrupt sync operations.

Troubleshooting
^^^^^^^^^^^^^^^

- **"error connecting to avi"** — Verify the API Host is reachable on the specified port from the |morpheus| appliance.
- **"unauthorized - invalid credentials"** — Confirm the username and password are valid on the Avi Controller.
- **"avi not found - invalid host"** — The specified URL may not point to an Avi Controller. Verify the endpoint.
- **Sync not updating** — Check that the Avi Controller is online and the configured user has read permissions on all required objects.
