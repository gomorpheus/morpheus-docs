Kubernetes Clusters
-------------------

Creating Kubernetes Clusters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provisions a new Kubernetes Cluster in selected target Cloud using selected Layout.

System (|morpheus| provided) Kubernetes Layouts:

Morpheus provides the following layouts for VMware vCenter, VMware Fusion, AWS, Openstack and Nutanix Clouds types.

Kubernetes Cluster 1.14 on Ubuntu 16.04, Weave, OpenEBS
  Kubernetes Master and 3 Worker Nodes
Kubernetes 1.14 on Ubuntu 16.04, Weave, OpenEBS
  Single Kubernetes Master

To create a new Kubernetes Cluster:

#. Navigate to ``Infrastructure - Clusters``
#. Select :guilabel:`+ ADD CLUSTER`
#. Select ``Kubernetes Cluster``
#. Populate the following:

   CLOUD
    Select target Cloud
   CLUSTER NAME
    Name for the Kubernetes Cluster
   RESOURCE NAME
    Name for Kubernetes Cluster resources
   DESCRIPTION
    Description of the Cluster
   VISIBILITY
    Public
      Available to all Tenants
    Private
      Available to Master Tenant
   TAGS
    Internal label(s)

   LAYOUT
    Select from available layouts. System provided layouts include Single Master and Cluster Layouts.
   PLAN
    Select plan for Kubernetes Master
   VOLUMES
    Configure volumes for Kubernetes Master
   NETWORKS
    Select the network for Kubernetes Master & Worker VM's
   CUSTOM CONFIG
    Add custom Kubernetes annotations and config hash
   CLUSTER HOSTNAME
    Cluster address Hostname (cluster layouts only)
   POD CIDR
    POD network range in CIDR format ie 192.168.0.0/24 (cluster layouts only)
   WORKER PLAN
    Plan for Worker Nodes (cluster layouts only)
   LOAD BALANCER
    Select an available Load Balancer (cluster layouts only) }

Kubernetes Cluster Detail Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tabs::

    .. tab:: SUMMARY

        .. image:: /images/infrastructure/clusters/kubeClusterSummary.png

    .. tab:: NAMESPACES

        .. image:: /images/infrastructure/clusters/kubeClusterNamespaces.png

    .. tab:: WIKI

        .. image:: /images/infrastructure/clusters/kubeClusterWiki.png

    .. tab:: MASTERS

        .. image:: /images/infrastructure/clusters/kubeClusterMasters.png

    .. tab:: WORKERS

        .. image:: /images/infrastructure/clusters/kubeClusterWorkers.png

    .. tab:: CONTAINERS

        .. image:: /images/infrastructure/clusters/kubeClusterContainers.png

    .. tab:: HISTORY

        .. image:: /images/infrastructure/clusters/kubeClusterHistory.png
