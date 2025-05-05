Network Considerations
^^^^^^^^^^^^^^^^^^^^^^

In order to run |morpheus| effectively in production, network redundancy and throughput must be considered. Network bonding is an important component to building redundancy into the environment so we will briefly discuss it here before showing some example network configurations. Ultimately the environment is your own but this discussion and the example network configurations that follow will help in planning out an effective operating environment for |morpheus|.

Network Bonding
```````````````

Network bonding is the combining of multiple network adapters into a single logical interface. This is done to build in redundancy and to increase throughput. Network bonds are configured at the operating system level and there are multiple types of network bonds depending on hardware support and other factors. Here we will call out two types of network bonds that are effective for virtualization and utilized in the example configurations that follow. Once established, we can later offer up these bonded interfaces as a compute network (for virtual machine traffic) or storage network (for interacting with external storage) when creating our cluster within the |manager| UI.

**Link Aggregation Control Protocol (LACP) 802.3ad**

LACP offers dynamic link aggregation with automatic negotiation, meaning the host and switch can communicate to determine the best available transmission parameters. It also includes load balancing and failover capabilities in the event of a failure somewhere in the path (failed interface, switch, etc). Bear in mind that LACP bonds require hardware support from a compatible switch but most current enterprise-grade switches do support it. If you have supported hardware and high availability and dynamic load balancing are important for your workloads, this is a good choice of bond type.

**Balanced XOR**

Balanced XOR is another bond type worth considering, especially if your switch hardware does not support LACP. It's simpler to set up and provides basic load balancing and failure but is less fexible and dynamic as compared to LACP. It's a good choice in environments where LACP is not supported or where dynamic load balancing is not required.

Example Network Configurations
``````````````````````````````

If you have the capability to do so, it's recommended you set up networking with full redundancy. Such a setup could include two network switches and hosts with at least six network interfaces spread across two network cards. This would allow for failover in the event of the loss of a switch and/or one of the host network cards in addition to separating management and compute network traffic to their own interfaces. Hosts with only four NICs each can still be configured for full redundancy but would have to converge management and compute traffic across the same interfaces. Keep in mind also that these examples use MPIO (multi-path input/output) for storage. It would also be possible to use bonding for storage depending on capabilities of the environment. MPIO is recommended whenever fibre channel or iSCSI LUNs are being used for GFS2 datastores.

**Six NICs with LACP bonds and MPIO for storage traffic**

.. image:: /images/vmeInstall/network1.png

- Six network interfaces
- One VLAN for management
- N VLANs for compute
- Two VLANs for storage
- Management and compute interfaces bonded on the hosts
- MLAG bonding on switches for management and compute

In the diagram note that each host has two network cards with four network interfaces on each card. We have a management network where the host IP address will go, which is an LACP-based bond that is replicated on the switches in a multi-chassis link aggregation group (MLAG). We also have a compute VLAN trunk to create networks for provisioning workloads onto. This is a similar bond interface with LACP and MLAG. For storage, it's recommended you use either fibre channel or iSCSI connectivity. To support that, in this example, two separate networks are created so MPIO can be configured (Multi-path Input/Output). MPIO provides multiple physical paths between hosts and storage devices which, like other considerations here, offers increased throughput and resiliency.

**Six NICs with XOR bonds and MPIO for storage traffic**

.. image:: /images/vmeInstall/network2.png

- Six network interfaces
- One VLAN for management
- N VLANs for compute
- Two VLANs for storage
- Management and compute interfaces bonded on the hosts
- MLAG bonding on switches for management and compute

This configuration is very similar to the previous one but the MLAGs have been removed from the switches and changed the bonding type to XOR. As mentioned previously, this model might be a good selection for environments with switches that don't support LACP bonds.

**Four NICs with LACP bonds and MPIO for storage traffic**

.. image:: /images/vmeInstall/network3.png

- Four network interfaces
- Management and compute VLANs on the same network trunk
- Two VLANs for storage
- Management interfaces bonded on hosts
- Compute interfaces bonded on hosts
- MLAG bonding on switches for management and compute

If there aren't enough interfaces available to separate the management and compute networks, a network configuration similar to the one shown here might be a good option. In this configuration, since there are only four network interfaces per host, the management and compute are converged. Once again, we have an LACP bond on this converged interface with MLAG on switches. We also have separate networks to handle storage MPIO.

**Four NICs with XOR bonds and MPIO for storage traffic**

.. image:: /images/vmeInstall/network4.png

- Four network interfaces
- Management and compute VLANs on the same network trunk
- Two VLANs for storage
- Management interfaces bonded on hosts
- Compute interfaces bonded on hosts
- MLAG bonding on switches for management and compute

This network example is very similar to the previous one with LACP bonds replaced with XOR bonds and MLAG removed. All configuration is handled at the host level. Other configurations are unchanged.
