Infoblox
========

Features
--------

* Network Pools synchronization
* Automatic IP Reservations, DNS A/PTR record creation and deletion

Adding Infoblox Integration
---------------------------

#. Navigate to `Infrastructure - Network - Services`
#. Select :guilabel:`+ ADD` -> IPAM -> Infoblox
#. Enter the following:

   .. image:: /images/infrastructure/network/infoblox/infoblox_settings.png

   NAME
    Name of the
   Enabled
    Deselect to disable the Integration
   URL
    Infoblox wapi url. Example: https://x.x.x.x/wapi/v2.2.1

    .. INFO:: The Infoblox wapi version can be found at https://x.x.x.x/wapidoc/

   USERNAME
    Infoblox user username
   PASSWORD
    Infoblox user password
   Disable SSL SNI Verification
    Leave selected to disable SSL SNI Verification
   NETWORK FILTER
    Filter which networks are synced into |morpheus|. Example: Network Filter: ``[ network_view=default&*Building=work ]``
   TENANT MATCH ATTRIBUTE
     This can be set to the name of the extended attribute in Infoblox where |morpheus| will check for the id of a morpheus tenant.  This allows for setting the tenant’s |morpheus| id to an extended attribute field on a network view or network in Infoblox, and when the network or view is discovered by morpheus, it will be auto assigned to the right tenant.
   IP MODE
    Static IPs or DHCP Reservations

#. Select :guilabel:`SAVE IPAM INTEGRATION`

Upon save the Infoblox IPAM integration will be created.

Adding IP Pools to Networks
---------------------------

|morpheus| can automatically assign the next available Infoblox IP in an IP/Network Pool and create the corresponding DNS records, as well as remove the records upon teardown. To enable this, add an Infoblox IP/Network Pool to the `Network Pool` section on a Network(s).

#. Navigate to `Infrastructure - Network- Networks`
#. Select a Network name and EDIT, or select `ACTIONS - Edit`
#. In the `NETWORK POOL` section, search for and select the name of the IP/Network Pool.

   * Gateway, DNS and CIDR must be populated for static/pool IP assignment
   * Select `Allow IP Override` to allow selecting between DHCP, Static entry and Pool Selection at provision time
   * Deselect DHCP server if a DHCP server will not be used on the network (only static and/or IP Pool IP assignment)

#. Select :guilabel:`SAVE CHANGES`
