Adding VLANs to Morpheus KVM Hosts (CentOS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Getting Started
```````````````

This guide will go over how to configure VLANs on a |morpheus| KVM Host. To get started, the first step is to go ahead and add the KVM host to morpheus and allow morpheus to configure it just like any other kvm host. When provisioning a manual kvm host be sure to enter the proper network interface name for the management network (not the trunk port). For example ``eno2`` could be a management network while ``eno1`` could be the trunk port network that the VLAN's are going to be on as in this example.

Setting up a VLAN Interface
```````````````````````````

Before a VLAN can be used by KVM, an interface definition must first be configured for said vlan. In CentOS this is done by defining a network script in ``/etc/sysconfig/network-scripts``.

.. NOTE:: It is highly recommended that NM_CONTROLLED is set to NO or NetworkManager is disabled entirely as it tends to get in the way.

If our trunk network is called ``eno1`` we need to make a new script for each VLAN ID we would like to bridge onto. In our example we are going to look at **VLAN 211**. To do this we need to make a new script called *ifcfg-eno1.211* (note the VLAN Id is a suffix to the script name after a period as this is conventional and required).

.. code-block:: bash

   TYPE=Ethernet
   PROXY_METHOD=none
   BROWSER_ONLY=no
   BOOTPROTO=none
   NAME=eno1.211
   DEVICE=eno1.211
   ONBOOT=yes
   NM_CONTROLLED=no
   VLAN=yes DEVICETYPE=ovs
   OVS_BRIDGE=br211

There are a few important things to note about this script. Firstly there is a flag called ``VLAN=yes`` that enables the kernel tagging of the VLAN. Secondly we have defined an OVS_BRIDGE name. Morpheus utilizes openvswitch for its networking which is a very powerful tool used even by Openstack's Neutron. It supports not just VLANs but VxLAN interfacing.

The **OVS_BRIDGE** name means we also need to define a bridge port script called ``br211`` by making a script called ``ifcfg-br211``:

.. code-block:: bash

   DEVICE=br211
   ONBOOT=yes
   DEVICETYPE=ovs
   TYPE=OVSBridge
   NM_CONTROLLED=no
   BOOTPROTO=none
   HOTPLUG=no

These configurations will enable persistence on these interfaces so that a reboot of the host will retain connectivity to the bridges. Next up, the interfaces need to be brought online. This can be done by restarting all network services but if a typo is made networking could be stuck disabled and access over SSH could be broken. To do this by interface simply run:

.. code-block:: bash

   ifup eno1.211
   ifup br211
   ovs-vsctl
   add-br br211

Defining a LibVirt Network
``````````````````````````

Now that the bridge interface is defined properly for OVS, it must be defined in LibVirt so that Morpheus will detect the network and KVM can use it properly. By convention, these resource configurations are stored in ``/var/morpheus/kvm/config``.

An XML definition must be created to properly define the network. In this case the network is named ``public 185.3.48.0.xml``:

.. code-block:: bash

   <network>
   <name>public 185.3.48.0</name>
   <forward mode="bridge"/>
   <bridge name="br211"/>
   <virtualport type="openvswitch"/>
   </network>

This configuration defines the network name that will be synced into morpheus for selection as well as the type of interface being used (in this case a bridge to the ``br211`` interface over openvswitch).

Now that this xml specification is defined it must be registered with libvirt via the virsh commands:

.. code-block:: bash

   virsh net-define "public 185.3.48.0.xml"
   virsh net-autostart "public 185.3.48.0"
   virsh net-start "public 185.3.48.0"

Once this is completed, simply refresh the cloud in morpheus and wait for the network to sync into the networks list. Once the network is synced make sure the appropriate settings are applied to it within Morpheus. This includes setting the CIDR, Gateway, Nameservers and if using IP Address Management, the IPAM Pool.
