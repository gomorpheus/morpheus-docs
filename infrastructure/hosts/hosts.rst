Hosts
=====

Overview
--------

The `Infrastructure > Compute` section provides a universal stage for viewing and managing Hosts and Virtual Machines from all of your Clouds.

In this section you can:

* View & Manage all Hosts, Virtual Machines & Bare Metal
* Add Hypervisors
* Convert Hosts, Virtual Machines and Bare Metal to Managed

  .. IMPORTANT:: When local firewall management is enabled, Morpheus will automatically set an IP table rule to allow incoming connections on tcp port 22 from the Morpheus Appliance.

Hosts
-----

Hosts in |morpheus| are hypervisors and Docker hosts that your VMs and Container are hosted on, such as ESXi, Hyper-V and Docker hosts. These hosts are populated from integrated clouds, hosts provisioned from Morpheus, or manually added hosts.

Provisioning new hosts takes place in the Infrastructure > Clusters section of |morpheus|. For example, provisioning a new Docker cluster in that section will begin the process of creating a |morpheus|-managed Docker cluster with one host (by default). Additional hosts and custom layouts can also be created. See the `Clusters section <https://docs.morpheusdata.com/en/latest/infrastructure/clusters/clusters.html>`_ of |morpheus| docs for more information.

.. //==== Adding Hosts
.. //==== Managing Hosts
.. //==== Removing Hosts


Virtual Machines
----------------

The Virtual Machines tab lists all managed and unmanaged VMs across |morpheus|. Managed VMs are either provisioned by |morpheus|, or are inventoried VMs that were converted to managed. Unmanaged VMs are from Cloud integrations with "Inventory Existing Instances" enabled in the Cloud settings.

.. //==== Managing Virtual Machines
.. //==== Removing Virtual Machines

Bare Metal
----------

Bare Metal hosts are from PXE Boot or manually added in this section. Bare Metal hosts that are also Hypervisors will be listed in both the Bare Metal and Hypervisor sections.

.. //==== Managing Bare Metal
.. //==== Removing Bare Metal
