Compute
=======

.. image:: /images/infrastructure/compute/infra_compute_header_5.4.3.png

.. note:: The Infrastructure ``Hosts`` page from previous versions has been renamed to ``Compute`` and updated with ``Container`` and ``Resource`` sections.

The `Infrastructure > Compute` section provides a universal stage for viewing and managing Hosts, Virtual Machines, Containers, Resources, and Bare Metal across Clouds.

In this section you can:

* View & Manage and Hosts, Virtual Machines, Containers, Resources, Bare Metal and Hypervisors
* Add manual Virtual Machines and Bare Metal Hosts
* Convert Hosts, Virtual Machines and Bare Metal to Managed

Hosts
-----

.. image:: /images/infrastructure/compute/infra_compute_header_hosts_5.3.1.png

.. sidebar:: Section Features & Filters
    :guilabel:`Record Search` :guilabel:`Custom Views` :guilabel:`CSV Export` :guilabel:`JSON Export` :guilabel:`Paging Config`

    - Standard Filters: :guilabel:`OS Type`
    - Advanced Filters: :guilabel:`Status` :guilabel:`Managed` :guilabel:`Server Type`

Hosts in |morpheus| are Hypervisors and Container hosts that VMs and Containers are hosted on, such as ESXi Hosts and Kubernetes Master and Workers. These hosts are populated from integrated clouds, hosts and clusters provisioned from Morpheus, or manually added hosts.

Provisioning new hosts takes place in the Infrastructure > Clusters section of |morpheus|. For example, provisioning a new Docker cluster in that section will begin the process of creating a |morpheus|-managed Docker cluster with one host (by default). Additional hosts and custom layouts can also be created. See the `Clusters section <https://docs.morpheusdata.com/en/latest/infrastructure/clusters/clusters.html>`_ of |morpheus| docs for more information.

Virtual Machines
----------------
.. image:: /images/infrastructure/compute/infra_compute_header_vms_5.3.1.png

.. sidebar:: Section Features & Filters
    :guilabel:`Record Search` :guilabel:`Custom Views` :guilabel:`CSV Export` :guilabel:`JSON Export` :guilabel:`Paging Config`

    - Standard Filters: :guilabel:`OS Type`
    - Advanced Filters: :guilabel:`Status` :guilabel:`Managed` :guilabel:`Server Type`

The Virtual Machines tab lists all managed and unmanaged VMs across |morpheus|. Managed VMs are either provisioned by |morpheus|, or are inventoried/discovered VMs that have been converted to managed. Unmanaged VMs are typically inventoried/discovered VMs from Cloud integrations.

Containers
----------
.. image:: /images/infrastructure/compute/infra_compute_header_containers_5.3.1.png

.. sidebar:: Section Features & Filters
    :guilabel:`Record Search` :guilabel:`Custom Views` :guilabel:`CSV Export` :guilabel:`JSON Export` :guilabel:`Paging Config`

    - Standard Filters: :guilabel:`Container Type` :guilabel:`Cloud`

The containers tab lists all Containers associated with |morpheus| Instances accessible to the user. Note additional system level containers from Kubernetes and Docker Clusters are not listed here but are acceessible in Cluster detail secitons.

Resources
---------
.. image:: /images/infrastructure/compute/infra_compute_header_resources_5.3.1.png

.. sidebar:: Section Features & Filters
    :guilabel:`Record Search` :guilabel:`Custom Views` :guilabel:`CSV Export` :guilabel:`JSON Export` :guilabel:`Paging Config`

    - Standard Filters: :guilabel:`Resource Type` :guilabel:`Cloud`

Resources represent objects that do not map to VM or Container types in |morpheus|, such as IAC resources from Terraform, Cloudformation or ARM Templates like VPC's, Gateways, Users, Policies, Brokers, API's, Endpoints, Directories, ACL's, Routes... well anything really. All resources created from IAC Templates map to iac provider resource types and |morpheus| maintains a resource object record from the mapped resource.

Expand the **Resource Types** table below to see all Resource types that will be mapped to Resource objects in |morpheus|:

- .. toggle-header:: :header: Resource Types **Click to Expand/Hide**

    .. include:: /infrastructure/compute/resourcetypes.rst
          
Bare Metal
----------
.. image:: /images/infrastructure/compute/infra_compute_header_bm_5.3.1.png

.. sidebar:: Section Features & Filters
    :guilabel:`Record Search` :guilabel:`Custom Views` :guilabel:`CSV Export` :guilabel:`JSON Export` :guilabel:`Paging Config`

    - Standard Filters: :guilabel:`OS Type`
    - Advanced Filters: :guilabel:`Status` :guilabel:`Managed` :guilabel:`Server Type`

Bare Metal hosts are from discovered, PXE Boot or manually added Bare Metal hosts. Bare Metal hosts that are also Hypervisors will be listed in the Hosts section.
