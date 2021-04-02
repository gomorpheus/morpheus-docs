Compute
=======

Overview
--------

The `Infrastructure -> Compute` section provides a universal stage for viewing and managing Hosts, Virtual Machines, Containers, Resources, Bare Metal and Hypervisors across Clouds.

In this section you can:

* View & Manage and Hosts, Virtual Machines, Containers, Resources, Bare Metal and Hypervisors
* Add manual Virtual Machines and Bare Metal Hosts
* Convert Hosts, Virtual Machines and Bare Metal to Managed

  .. IMPORTANT:: When local firewall management is enabled, Morpheus will automatically set an IP table rule to allow incoming connections on tcp port 22 from the Morpheus Appliance.

  .. //==== permissions
  
Hosts
-----

Hosts in |morpheus| are hypervisors and Docker hosts that your VMs and Container are hosted on, such as ESXi, Hyper-V and Docker hosts. These hosts are populated from integrated clouds, hosts provisioned from Morpheus, or manually added hosts.

Provisioning new hosts takes place in the Infrastructure > Clusters section of |morpheus|. For example, provisioning a new Docker cluster in that section will begin the process of creating a |morpheus|-managed Docker cluster with one host (by default). Additional hosts and custom layouts can also be created. See the `Clusters section <https://docs.morpheusdata.com/en/latest/infrastructure/clusters/clusters.html>`_ of |morpheus| docs for more information.

Virtual Machines
----------------

The Virtual Machines tab lists all managed and unmanaged VMs across |morpheus|. Managed VMs are either provisioned by |morpheus|, or are inventoried/discovered VMs that have been converted to managed. Unmanaged VMs are typically inventoried/discovered VMs from Cloud integrations.

Bare Metal
----------

Bare Metal hosts are from PXE Boot or manually added in this section. Bare Metal hosts that are also Hypervisors will be listed in both the Bare Metal and Hypervisor sections.

Containers
----------

Resources
---------

.. toggle-header::
    :header: Resource Types **Click to Expand/Hide**
    
          .. include:: /infrastructure/compute/resourcetypes.rst

Bare Metal
----------

Hypervisors
-----------