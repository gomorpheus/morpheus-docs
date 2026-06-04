.. _security_roles:

Security Roles
--------------

Overview
^^^^^^^^

Security roles in |morpheus| control user access to network security features. These roles work within the broader |morpheus| role-based access control (RBAC) system to determine which users can view, create, edit, or delete security-related resources such as firewall rules, security groups, and security server integrations.

Network Security Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following permissions govern access to network security features in |morpheus|. These are configured in ``Administration > Roles > (select Role) > Infrastructure`` section:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Permission
     - Access Levels
     - Description
   * - Infrastructure: Network Integrations
     - None, Read, Full
     - Controls access to view and manage network/security server integrations
   * - Infrastructure: Network Firewalls
     - None, Read, Manage Rules, Full
     - Controls access to firewall groups and rules within network and security server integrations
   * - Infrastructure: Network DHCP Server
     - None, Read, Full
     - Controls access to DHCP server management
   * - Infrastructure: Network DHCP Relay
     - None, Read, Full
     - Controls access to DHCP relay management
   * - Infrastructure: Network Router Redistribution
     - None, Read, Full
     - Controls access to route redistribution configuration
   * - Infrastructure: Network Routers
     - None, Read, Full, Group
     - Controls access to router management including BGP neighbors

Permission Access Levels
^^^^^^^^^^^^^^^^^^^^^^^^

None
  No access to the resource. The associated UI elements are hidden.

Read
  View-only access. Users can see configuration but cannot make changes.

Manage Rules
  (Firewalls only) Users can create, edit, and delete individual rules within existing firewall groups but cannot create or delete groups themselves.

Full
  Complete access including creation, editing, and deletion of resources.

Group
  (Routers only) Access is limited to routers within the user's assigned Groups.

Configuring Security Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Administration > Roles``
#. Select the target role
#. Scroll to the **Infrastructure** permissions section
#. Set the appropriate access level for each network security permission
#. Click :guilabel:`SAVE CHANGES`

.. NOTE:: Changes to role permissions take effect immediately. Users with active sessions will see the updated permissions on their next page load.

Best Practices
^^^^^^^^^^^^^^

- Grant ``Manage Rules`` access to operations teams that need to update firewall rules without modifying the integration structure
- Use ``Group`` access for router permissions when multiple teams share an |morpheus| tenant but manage separate network infrastructure
- Restrict ``Full`` access to network security integrations to senior network administrators
- Use ``Read`` access for auditors or compliance personnel who need visibility without modification capability
