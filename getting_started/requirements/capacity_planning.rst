Capacity and Planning
=====================

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
   * - AIO
     - 4
     - 16
     - 200
     - N/A
   * - AIO
     - 4
     - 32
     - 400
     - N/A
   * - 3-Node HA
     - 4
     - 16
     - 400
     - 50
   * - 3-Node HA
     - 8
     - 32
     - 400
     - 50

The table provides initial resource recommendations, not fixed workload or object limits. Actual capacity depends on managed VMs and systems, Agent use, Clouds, integrations, automation concurrency, active users, retention, and workload behavior. Due to ease of installation and maintenance, strongly consider an AIO architecture unless high availability, zero-downtime upgrades, or workload-specific sizing requires a multi-node architecture. An AIO architecture cannot tolerate failure and is unavailable during upgrades; a 3-Node HA architecture provides redundancy and supports zero-downtime upgrades when properly designed.

Both AIO and 3-Node HA nodes can be **scaled up** by adding CPU or memory. A 3-Node HA architecture can also be **scaled out** to add capacity and redundancy, whereas an AIO configuration cannot add application nodes. The 3-Node HA architecture should always have an odd number of nodes for quorum. For VME Manager limits and values that HPE has not published, see :doc:`HPE VM Essentials Maximums </infrastructure/clusters/hvm/maximums>`.

.. IMPORTANT:: Customer architectures and requirements will vary.  Please contact your account manager if you wish to deploy or transition to a HA environment, which can help right-size the environment

Additional information around the various architectures can be found here:

    :ref:`installation-overview`

    :ref:`distributed-overview`
