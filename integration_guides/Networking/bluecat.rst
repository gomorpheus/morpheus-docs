Bluecat
--------

Overview
^^^^^^^^^

Morpheus integrates with Bluecat IPAM to scope pools to networks for Static IP assignment from Infoblox to your Morpheus instances.

Adding Bluecat to Morhpeus
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Services``
#. Click :guilabel:`+ ADD`
#. Select `Bluecat`
#. Enter in the following information

    * Name
    * URL
    * Username
      * Example: http://10.34.20.23
    * Password
    * Network Filter

#. Click :guilabel:`SAVE CHANGES`


Adding IP Pools to Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| can automatically assign the next available Bluecat IP in an IP/Network Pool and create the corresponding DNS records, as well as remove the records upon teardown. To enable this, add an Bluecat IP/Network Pool to the `Network Pool` section on a Network(s).

#. Navigate to ``Infrastructure - Network- Networks``
#. Select a Network name and EDIT, or select `ACTIONS - Edit`
#. In the `NETWORK POOL` section, search for and select the name of the IP/Network Pool.

   * Gateway, DNS and CIDR must be populated for static/pool IP assignment
   * Select `Allow IP Override` to allow selecting between DHCP, Static entry and Pool Selection at provision time
   * Deselect DHCP server if a DHCP server will not be used on the network (only static and/or IP Pool IP assignment)

#. Select :guilabel:`SAVE CHANGES`
