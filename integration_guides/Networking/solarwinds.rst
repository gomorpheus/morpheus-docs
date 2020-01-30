SolarWinds IPAM
---------------

Features
^^^^^^^^

- Automate static IP assignment across environments using Solarwinds IPAM
- Network pool sync: Network pools can be set on networks in |morpheus| for automated IP allocation and record creation
- Optional Network Pool allocation and record sync. ``Inventory Existing`` option syncs all individual IP records and corresponding status. Inventory is not required for provisioning
- Grid and list displays with IP record overlays and color coding for static, available, reserved and transient status
- Manual IP Host record creation from Network Pool detail pages


Adding SolarWinds to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Click :guilabel:`+ ADD`
#. Select `SolarWinds`
#. Enter in the following information

    Name
      Name of the SolarWinds Integration in |morpheus|
    Enabled
      Deselect to disable sync with the SolarWinds endpoint
    URL
      URL of the SolarWinds server, ex: ``http://10.30.20.10``
    Username
      Username of SolarWinds API User. API and root level propagating read access required, read/write access required for target networks and domains.
    Password
      SolarWinds User password

#. Click :guilabel:`SAVE CHANGES`

Consuming SolarWinds in |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On saving your new integration, SolarWinds networks will be synced and can be viewed by navigating to ``Infrastructure > Network > IP POOLS``. They're also viewable from the detail section of the SolarWinds integration at ``Infrastructure > Network > INTEGRATIONS > (your SolarWinds integration) > NETWORK POOLS``.

.. image:: /images/integration_guides/networking/solarwinds/networkpools.png

Host records can also be viewed here by clicking on the name of a SolarWinds network.

.. image:: /images/integration_guides/networking/solarwinds/hostrecords.png

Integrating with SolarWinds will also sync DNS zones, which can be viewed in ``Infrastructure > Network > DOMAINS``. They can also be viewed from within the integration detail page at ``Infrastructure > Network > INTEGRATIONS > (your SolarWinds integration) > ZONES``.

Adding IP Pools to Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| can automatically assign the next available SolarWinds IP in an IP/Network Pool and create the corresponding DNS records. |morpheus| will also remove the records upon teardown. To enable this, add an SolarWinds IP/Network Pool to the `Network Pool` section on a Network(s).

#. Navigate to ``Infrastructure > Network > Networks``
#. Select a Network name and click :guilabel:`EDIT`
#. In the NETWORK POOL typeahead field, search for and select the name of the selected IP/Network Pool.

   * Gateway, DNS, and CIDR must be populated for static/pool IP assignment
   * Select ALLOW IP OVERRIDE to allow selecting between DHCP, static IP address entry, and pool address selection at provision time
   * Deselect DHCP server if a DHCP server will not be used on the network (only static and/or IP Pool IP assignment)

#. Select :guilabel:`SAVE CHANGES`

Creating Host Records
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Select a Network Pool from ``Infrastructure > Network > IP POOLS``
#. Click :guilabel:`+ ADD`
#. Enter the following

   HOSTNAME
    Hostname for the record
   IP ADDRESS
    IP address for the Host Record

#. Select :guilabel:`SAVE CHANGES`

.. image:: /images/integration_guides/networking/solarwinds/createhost.png
  :width: 80%
  :align: center

Creating Zone Records
^^^^^^^^^^^^^^^^^^^^^

#. Select a domain from ``Infrastructure > Network > DOMAINS``
#. Click :guilabel:`+ ADD`
#. Complete the fields in the CREATE ZONE RECORD modal
#. Click :guilabel:`SAVE CHANGES`
