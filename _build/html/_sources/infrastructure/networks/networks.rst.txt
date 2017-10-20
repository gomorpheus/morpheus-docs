Networks
--------

``Infrastructure -> Network -> Networks``

Overview
^^^^^^^^

The Networks section is for configuring networks across all clouds in |morpheus| . Existing networks from the Clouds added in |morpheus| will auto-populate in the Networks section.

Networks can be configured for DHCP or Static IP assignment, assigned IP pools, and configured for visibility and account assignment for multi-tenancy usage. Networks can also be set as inactive and unavailable for provisioning use.

Configuring Networks
^^^^^^^^^^^^^^^^^^^^

DHCP
....

To configure a network for DHCP:

1. Navigate to `Infrastructure -> Network -> Networks`
2. Search for the target network
3. Edit the Network by either:

   * Select `Actions -> Edit`
   * Select the Network, then select `Edit`

4. In the Network Config modal, set the DHCP flag as Active (default)
5. Save Changes

.. IMPORTANT:: The DHCP flag tells |morpheus| this network has a DHCP server assigning IP Addresses to hosts. |morpheus| does not act as the DHCP server, and provisioning to a network that has the DHCP server flag active in |morpheus| , but no DHCP server actually on the network will in most cases cause the instance to not receive an IP address.

.. NOTE:: When selecting a network with DHCP enabled during provisioning, "DHCP" will populate to the right of the selected network:

Static and IP Pools
...................

To configure a network for Static IP Assignment:

1. Navigate to `Infrastructure -> Network -> Networks`
2. Search for the target network
3. Edit the Network by either:

   * Select `Actions -> Edit`
   * Select the Network, then select `Edit`

4. In the Network Config modal, add the following:
   * Gateway
   * DNS Primary
   * DNS Secondary
   * CIDR ex 10.10.10.0/22
   * VLAN ID (if necessary)
   * Network Pool

     * Leave as "choose a pool" for entering a static IP while provisioning
     * Select a Pool to use a pre-configured |morpheus| or IPAM Integration IP Pool

   * The Permissions settings are used for Multi-Tenant resource configuration

     * Leave settings as default if used in a single-tenant environment (only one Tenant in your |morpheus| appliance)
     * To share this network across all accounts in a multi-tenant environment, select the Master Tenant and set the Visibility to Public
     * To assign this network to be used by only one account in a multi-tenant environment, select the account and set visibility to Private

   * Active

     * Leave as enabled to use this network
     * Disable the active flag to remove this network from available network options

5. Save Changes

.. NOTE:: When selecting a network with DHCP disabled and no IP Pool assigned during provisioning, an IP entry field will populate to the right of the selected network(s):

.. NOTE:: When selecting a network with an IP Pool assigned during provisioning, the name of the IP pool will populate to the right of the selected network(s). IP Pools override DHCP.
