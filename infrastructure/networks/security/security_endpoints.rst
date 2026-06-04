.. _security_endpoints:

Security Endpoints
------------------

``Infrastructure > Network > Integrations > (select Security Server) > Firewall > Rules``

Overview
^^^^^^^^

Security endpoints represent the source and destination objects in firewall rules and security policies within a network security integration. Endpoints can include IP addresses, IP ranges, network segments, security groups, or service profiles that define what traffic is allowed or denied.

In |morpheus|, security endpoints are managed as part of the firewall configuration within a security server integration. They provide the building blocks for defining security policies and access control.

Managing Endpoints in Firewall Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating or editing firewall rules within a security server integration, source and destination endpoints are configured as rule parameters:

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired security server integration
#. Click the **Firewall** tab
#. Create or edit a firewall rule
#. Configure endpoints in the source and destination fields:

   :Source: The originating endpoint (IP, group, segment, or "Any")
   :Destination: The target endpoint (IP, group, segment, or "Any")
   :Service/Port: The service or port specification
   :Action: Allow or Deny
   :Enabled: Toggle rule enforcement

Endpoint Types
^^^^^^^^^^^^^^

Depending on the security integration, the following endpoint types may be available:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Endpoint Type
     - Description
   * - IP Address
     - A single IPv4 or IPv6 address
   * - IP Range/CIDR
     - A range of IP addresses specified in CIDR notation
   * - Security Group
     - A named group of resources that share the same security policy
   * - Network Segment
     - A logical network segment or subnet
   * - Virtual Machine
     - A specific virtual machine instance
   * - Any
     - Matches all traffic regardless of source or destination

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to security endpoint management requires the ``Infrastructure: Network Firewalls`` permission (``infrastructure-network-firewalls``) with ``read``, ``managerules``, or ``full`` access.
