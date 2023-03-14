IP Pools
--------

``Infrastructure -> Network -> IP Pools``

Overview
^^^^^^^^

The Networks IP Pools sections allows you to create |morpheus| IP Pools, which is an IP Range |morpheus| can use to assign available static IP addresses to instances. The IP Pool section also displays pools from IPAM integrations like Infoblox and Bluecat.

To add a |morpheus| Network Pool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Select *+ ADD* in the `Infrastructure -> Network -> IP Pools` section
2. Enter the following:
   * Name:: Name of the IP Pool in |morpheus| . The name is presented when selecting an IP Pool for a Network, so use a name that easily identifies the IP Pool.
   * Starting Address:: The starting IP address of the IP Pool address range. ex: 192.168.0.2
   * Ending Address:: The ending IP address of the IP Pool address range. ex: 192.168.0.255
3. Save Changes

.. NOTE:: Multiple Address Ranges can be added to a pool by selecting the + icon to the right of the first address range.

After saving the IP pool will be available for assignment to networks in the NETWORK POOL dropdown when adding or editing a network.
