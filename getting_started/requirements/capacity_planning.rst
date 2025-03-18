Capacity and Planning
====================

There are many different architectures |morpheus| can be deployed as.  However, the most common architectures are an All-In-One (AIO) single node and a 3-Node Highly Available (HA) cluster. These architectures can have many variables to determine the capacity of each node, as each users' environment will be different.  Example factors that determine the capacity are:

    * Number of virtual machines (VMs)/systems/instances that |morpheus| will manage, also know as Workload Elements (WLEs)
    * If the WLEs will have agents installed
    * The number of clouds added to |morpheus|
    * The technologies used, such as: Kubernetes, Terraform, ARM, etc.
    * The number of concurrent worflows
    * Number of active users

Although there are many factors that can contribute to the capacity planning, even outside the list above, below are recommended initial specifications.

.. list-table:: **Recommendations**
   :widths: auto
   :header-rows: 1

   * - Architecture
     - # of CPUs per node
     - Memory (GB) per node
     - Local Storage (GB) per node
     - Shared Storage (NFS)
     - Supported WLEs
   * - AIO
     - 4
     - 16
     - 200
     - N/A
     - 5,000
   * - AIO
     - 4
     - 32
     - 400
     - N/A
     - 10,000
   * - 3-Node HA
     - 4
     - 16
     - 400
     - 50
     - 10,000
   * - 3-Node HA
     - 8
     - 32
     - 400
     - 50
     - 20,000

In the above recommendations, an AIO can support ~5,000 WLEs with agents installed at the base requirements.  Due to ease of installation and maintenance, an AIO architecture should be strongly considered for smaller environments that will manage less than a few thousand WLEs.  However, the AIO architecture cannot tolerate failure and will be unavailable during upgrades, unlike the 3-Node HA, which is the likely choice for ensuring zero downtime upgrades and high availability.  A 3-Node HA architecture *could* support ~15,000 WLEs with agents installed (3 x 5,000) at the base requirements but it is best to consider the possible loss of a node, which would be an effective support of ~10,000 WLEs with agents installed (2 x 5,000).

In the case of both the AIO and 3-Node HA architectures, |morpheus| nodes can be **scaled up** to a maximum of 32GB of memory, which can support more WLEs per node.  Adding more CPU or memory is possible, without adding additional nodes. Also, in the case of the 3-Node HA architecture, |morpheus| can be **scaled out**, which can support additional WLEs per node added and provides additional redundancy, whereas the AIO configuration cannot add additional nodes.  The 3-Node HA architecture should always have an odd number of nodes for quorum.

.. IMPORTANT:: Customer architectures and requirements will vary.  Please contact your account manager if you wish to deploy or transition to a HA environment, which can help right-size the environment

Additional information around the various architectures can be found here:

    :ref:`installation-overview`

    :ref:`distributed-overview`
