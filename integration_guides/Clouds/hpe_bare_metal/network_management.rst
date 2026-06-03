Network Management
^^^^^^^^^^^^^^^^^^

At a high level, there are two network modes in which a cloud can be configured to operate: 
- Unmanaged network mode (
- Unmanaged
- ).

 
- Managed network mode (
- ArubaCX-Int
- ).

Network modes are created during cloud creation.

Unmanaged Networks
------------------

The unmanaged Network mode is used when the network infrastructure is not managed by HPE Morpheus.

 In this case, there is a minimal configuration that is created as default when the cloud gets created with the network mode set to Unmanaged network. This minimal configuration includes a default Resource Pool that can be used to associate compute servers with, and a default unmanaged network that is available during instance provisioning to attach with compute servers.

 The default unmanaged network is configured as an untagged network with DHCP as the IP allocation method. This allows a compute instance provisioned to come up with network connectivity without any specific network configuration required from the user.

 The unmanaged network assumes: 
* The network infrastructure to be configured correctly for the untagged network to work correctly.

* A DHCP server stood up in the infrastructure for that network.



  Users can create other networks (VLANs) if required, in addition to the default unmanaged network, and use them in their BM instance. NOTE  
* If the
* ALLOW IP OVERRIDE
* checkbox is selected (allows selection of DHCP or static IP or IP Pool), ensure that the
* CIDR
* and
* GATEWAY
* fields are configured correctly.

* At present, only one physical interface is supported for the unmanaged network mode.

The network consumption by an instance is the same as for managed networks.

Managed Networks
----------------

The managed network mode is used when the network infrastructure is to be managed by Morpheus. In this case, the user can selectArubCX-Intduring the cloud creation.

  AddingHPE ArubaCX Plugin
 In the managed network mode, the Aruba CX switches are supported as managed switches. To enable that, the ArubaCX plugin needs to be loaded.

 You can load the ArubaCX plugin jar using theAdministration>Integrations.

Creating ArubaCX Network Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  The network integration allows the user to specify the switch information. It is expected that there are 2 switches per rack acting as the top-of-rack (ToR) switches. You need to specify information for a switch pair for a rack. If there are more than 1 rack, then information for the switch pair for each rack is required.


#. Log in to the
#. HPE
#. |morpheus| Enterprise Software web interface using your administrator credentials. 
#. Navigate to
#. Infrastructure
#. >
#. Network
#. >
#. Integrations.
#. Click the
#. Add
#. to add a new integration. 
#. Select
#. HPE
#. Aruba CX Switches
#. under the
#. Networking
#. section.

 
#. Enter the following details for the network integration:   
  - Name
  - for network integration 
  - Username/Password
  - for the switches 
  - Switch pair IP Addresses
  - for each pair of switches   

  
#. Click the
#. Add Network Integration
#. to create the Network Integration.

Networks Configuration
----------------------

Once the network integration is created, networks can be created using the specific network integration that was created. Networks essentially define the VLAN that they represent along with other attributes such as the subnet’s IPv4 prefix, IP address allocation method, gateway address, DNS, etc. The screenshot below shows those details.

 TheVLAN Trunksspecifies the trunk VLANs to be added when this network is consumed by an instance. TheVLAN IDfield represents the primary VLAN for this network. This VLAN is configured as the untagged VLAN when this network is consumed by an instance.

 TheNetwork Servicecorresponds to the network integration that was created. This specifies that the network is to be created in the infrastructure (switches) specified in the network integration selected.

 ThePrivatecheckbox specifies that the network is a private network. By default, all networks are public. If private is selected, the primary VLAN in this network is not configured on the uplink connection. This would render them unreachable from outside of the cloud infrastructure. This is typically used for workload networks that are used to communicate between only the workload servers and other infrastructure within the private cloud.

 The configuration of a network will result in the primary VLAN in that network being provisioned on the network switches. The server ports are configured when those networks are consumed during the provisioning of a compute instance.

Creating Network Using ArubaCX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating Network Using the ArubaCX Integration
Prerequisites
  Before starting to create networks using integration, ensure that a Bare metal cloud is created with the ‘Network Mode’ set to the integration. If the Bare metal cloud already exists then ensure that ‘Network Mode’ is set to integration.

Perform the following to create the network:


#. Log in to the
#. HPE
#. |morpheus| Enterprise Software web interface using your administrator credentials. 
#. Navigate to
#. Infrastructure
#. >
#. Network.
#. Click the
#. Add
#. to add a new integration. 
 
#. Enter the following details for the network: 
  - Group
  - for the network 
  - Network Service
  - specifies the Network Integration to use 
  - Name
  - for the network 
  - Gateway, DNS
  - information if required 
  - CIDR
  - for the subnet 
  - Primary
  - VLAN ID
  - for the network 
  - Check the
  - Private
  - checkbox if a private network 
  - VLAN trunks
  - for the network (optional) 
  - Choose
  - Network Pool
  - to be one of the IP pools configured   
#. Click
#. Save Changes
#. to create the network.

Network Usage
^^^^^^^^^^^^^

Networks are attached to interfaces on a compute server. The interfaces can be the physical ports themselves or bond interfaces that combine two physical ports into an aggregated pipe. Bond interfaces provide the benefits of aggregated bandwidth on a single interface and also high availability by providing port-level redundancy.

 Once the decision is made on what kind of interfaces to use, networks can be chosen from the preconfigured list to attach to the network interfaces. This determines which VLANs are configured on which switch ports (or LAGs). As mentioned earlier, the primary VLAN is provisioned as an untagged VLAN, and the trunk VLANs are provisioned as tagged VLANs on the server ports.

 The supported bond types are: 
* Static Bond: This uses an L2+L3-based hash on the server OS and a static LAG on the switches. 
* LACP Bond: This uses the LACP mode on the server OS and LACP LAG on the switches. 
* Switch Independent Bond: This uses the balance-tlb mode on Linux servers and the switch-independent mode on Windows. The switch is configured as independent physical ports.

Specifying Network Usage
^^^^^^^^^^^^^^^^^^^^^^^^

  Perform the following to specify networks used during instance provisioning:


#. Log in to the
#. HPE
#. |morpheus| Enterprise Software web interface using your administrator credentials. 
#. Navigate to
#. Provisioning
#. >
#. Instances.
#. Select
#. HPE
#. Bare Metal (ILO) Server
#. as the type. 
#. Click
#. Next.
#. Specify a
#. Group
#. ,
#. Cloud
#. , and a
#. Name
#. for the Instance. 
#. Click
#. Next.
#. Select a
#. Network.
#. Select an
#. interface type
#. (Bond/Physical). 
#. Specify any required
#. virtual interface.
#. Click
#. Next
#. and complete.  
#. For physical interfaces, the interfaces represent the physical ports in their display order. Virtual networks specify that tagged networks under the primary network specified are to be configured on the server OS with an IP interface. If any of those tagged networks are not required to be configured on the server OS as an IP interface, do not specify a virtual interface for those.

