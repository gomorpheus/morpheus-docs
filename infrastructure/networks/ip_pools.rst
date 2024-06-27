IP Pools
--------

``Infrastructure > Network > IP Pools``

Overview
^^^^^^^^

The IP Pools tab in the Networks section allows you to create |morpheus|-type IP Pools (which is an IP address range |morpheus| can use to assign available static IP addresses to Instances) and NSX IP Pools. The IP Pool section also displays pools synced from IPAM integrations like Infoblox, Bluecat and others.

To add a |morpheus| Network Pool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Click :guilabel:`+ ADD` in ``Infrastructure > Network > IP Pools``
2. Enter the following:
     Name
      A friendly name for the IP Pool in |morpheus|.
     Pool Type
      Currently |morpheus|-type IP Pools and NSX IP Pools (with a configured integration) can be created directly from |morpheus|
     Starting Address
      The starting IP address of the IP Pool address range. ex: 192.168.0.2
     Ending Address:
      The ending IP address of the IP Pool address range. ex: 192.168.0.255

3. Save Changes

.. NOTE:: Multiple Address Ranges can be added to a pool by selecting the + icon next to the address range.

After saving the IP pool will be available for assignment to networks in the NETWORK POOL dropdown when adding or editing a network.
