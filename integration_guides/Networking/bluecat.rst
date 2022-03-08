Bluecat
-------

Overview
^^^^^^^^

|morpheus| integrates with Bluecat IPAM to scope pools to networks for static IP assignment from Bluecat to your |morpheus| Instances.

Adding Bluecat to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Click :guilabel:`+ ADD`
#. Select `Bluecat`
#. Enter in the following information

    Name
      Name of the Bluecat Integration in |morpheus|
    Enabled
      Uncheck to disable sync with the Bluecat endpoint
    URL
      URL of the Bluecat server, ex: ``http://10.30.20.10``
    Username
      Username of Bluecat API User. API and root level propagating read access required, read/write access required for target Networks and Domains.
    Password
      Bluecat User password
    Network Filter
       Optionally enter the id of a config, block or network, or comma separated combination of configs, blocks and/or networks.

#. Click :guilabel:`SAVE CHANGES`

The Bluecat Integration will be saved, IP pools will sync in and populate under ``Infrastructure > Network > IP Pools``, and Domain will populate in ``Infrastructure > Network > Domains``. Pools and Domains can also be found in the Bluecat Integration details page, which can be accessed by clicking on the name of the added Bluecat Integration in ``Infrastructure > Network > Integrations``.

.. IMPORTANT:: `Quick Deployments` must be enabled in Bluecat for |morpheus| to create instantly available DNS records when using Bluecat DNS.

Adding IP Pools to Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| can automatically assign the next available Bluecat IP in an IP/Network Pool and create the corresponding DNS records, as well as remove the records upon teardown. To enable this, add an Bluecat IP/Network Pool to the `Network Pool` section on a Network(s).

#. Navigate to ``Infrastructure - Network- Networks``
#. Select a Network name and EDIT, or select `ACTIONS - Edit`
#. In the `NETWORK POOL` section, search for and select the name of the IP/Network Pool.

   * Gateway, DNS and CIDR must be populated for static/pool IP assignment
   * Select `Allow IP Override` to allow selecting between DHCP, Static entry and Pool Selection at provision time
   * Deselect DHCP server if a DHCP server will not be used on the network (only static and/or IP Pool IP assignment)

#. Select :guilabel:`SAVE CHANGES`
