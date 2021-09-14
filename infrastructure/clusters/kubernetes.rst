.. _k8s:

Kubernetes Clusters
-------------------

Requirements
^^^^^^^^^^^^

- Agent installation is required for Master and Worker Nodes. Refer to `Morpheus Agent`_ section for additional information.
- Access to Cloud Front, Image copy access and permissions for System and Uploaded Images used in Cluster Layouts
   Image(s) used in Cluster Layouts must either exist in destination cloud/resource or be able to be copied to destination by Morpheus, typically applicable for non-public clouds. For the initial provision, Morpheus System Images are streamed from Cloud Front through Morpheus to target destination. Subsequent provisions clone the local Image.
- System Kubernetes Layouts require Master and Worker nodes to access to the following over 443 during K8s install and configuration:

  * Morpheus Appliance url (443)
  * https://packages.cloud.google.com
  * https://storage.googleapis.com
  * https://docs.projectcalico.org
  * https://openebs.github.io
  * https://cloud.weave.works

- Morpheus Role permission ``Infrastructure: Clusters -> Full`` required for Viewing, Creating, Editing and Deleting Clusters.
- Morpheus Role permission ``Infrastructure: Clusters -> Read`` required for Viewing Cluster list and detail pages.

Creating Kubernetes Clusters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provisions a new Kubernetes Cluster in selected target Cloud using selected Layout.

System (|morpheus| provided) Kubernetes Layouts at time of |morphver| release. Note: AKS k8s versions will dynamically update as Azure updates supported versions.


+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Cluster Type Name                                | Description                                                                            | code                                                      |
+==================================================+========================================================================================+===========================================================+
| Kubernetes Cluster GKE                           | This will provision a single kubernetes master in google                               | kubernetes-google-gke                                     |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.20 Cluster EKS                      | This will provision a single kubernetes master in amazon with weave and openebs        | kubernetes-amazon-eks-1.20                                |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Morpheus Kubernetes Manual Cluster               | This will create a kubernetes manual (self-managed) cluster                            | morpheus-kubernetes-manual-cluster                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.19.11 Cluster AKS                   | This provisions a single kubernetes master in Azure                                    | kubernetes-azure-aks-1.19.11                              |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.20.7 Cluster AKS                    | This provisions a single kubernetes master in Azure                                    | kubernetes-azure-aks-1.20.7                               |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.21.1 Cluster AKS                    | This provisions a single kubernetes master in Azure                                    | kubernetes-azure-aks-1.21.1                               |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.21.2 Cluster AKS                    | This provisions a single kubernetes master in Azure                                    | kubernetes-azure-aks-1.21.2                               |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.19.13 Cluster AKS                   | This provisions a single kubernetes master in Azure                                    | kubernetes-azure-aks-1.19.13                              |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Kubernetes 1.20.9 Cluster AKS                    | This provisions a single kubernetes master in Azure                                    | kubernetes-azure-aks-1.20.9                               |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.21 Cluster on Ubuntu   20.04    | provision a kubernetes 1.21 cluster on ubuntu 20.04 in fusion                          | kubernetes-1.21.3-ubuntu-20.04.1-fusion-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   20.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in xen                             | kubernetes-1.20.2-ubuntu-18.04.5-xen-amd64-single         |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in vmware                          | kubernetes-1.20.2-ubuntu-18.04.5-vmware-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in scvmm                           | kubernetes-1.20.2-ubuntu-18.04.5-scvmm-amd64-single       |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in opentelekom                     | kubernetes-1.20.2-ubuntu-18.04.5-opentelekom-amd64-single |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in Openstack                       | kubernetes-1.20.2-ubuntu-18.04.5-openstack-amd64-single   |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in manual                          | kubernetes-1.20.2-ubuntu-18.04.5-morpheus-amd64-single    |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in hyperv                          | kubernetes-1.20.2-ubuntu-18.04.5-hyperv-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in Huawei                          | kubernetes-1.20.2-ubuntu-18.04.5-huawei-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04 in fusion                          | kubernetes-1.20.2-ubuntu-18.04.5-fusion-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04                                    | kubernetes-1.20.2-ubuntu-18.04.5-amazon-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04                                    | kubernetes-1.20.2-ubuntu-18.04.5-google-amd64-single      |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 Cluster on Ubuntu   18.04    | provision a kubernetes 1.20 cluster on ubuntu 18.04                                    | kubernetes-1.20.2-ubuntu-18.04.5-nutanix-amd64-single     |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04 in   vmware      | kubernetes-1.20.2-ubuntu-18.04.5-vmware-amd64             |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04 in   opentelekom | kubernetes-1.20.2-ubuntu-18.04.5-opentelekom-amd64        |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04 in   Openstack   | kubernetes-1.20.2-ubuntu-18.04.5-openstack-amd64          |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04 in   manual      | kubernetes-1.20.2-ubuntu-18.04.5-morpheus-amd64           |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04 in   hyperv      | kubernetes-1.20.2-ubuntu-18.04.5-hyperv-amd64             |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04                  | kubernetes-1.20.2-ubuntu-18.04.5-amazon-amd64             |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04                  | kubernetes-1.20.2-ubuntu-18.04.5-google-amd64             |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MKS Kubernetes 1.20 HA Cluster on Ubuntu   18.04 | provision a high availability kubernetes 1.20 cluster on ubuntu 18.04                  | kubernetes-1.20.2-ubuntu-18.04.5-nutanix-amd64            |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| External Kubernetes 1.21                         | Connect to an external kubernetes cluster.                                             | kubernetes-external-1.21                                  |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| External Kubernetes 1.20                         | Connect to an external kubernetes cluster                                              | kubernetes-external-1.20                                  |
+--------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+

|


To create a new Kubernetes Cluster:

#. Navigate to ``Infrastructure > Clusters``
#. Select :guilabel:`+ ADD CLUSTER`
#. Select ``Kubernetes Cluster``
#. Select a Group for the Cluster
#. Select :guilabel:`NEXT`
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
   LABELS
    Internal label(s)

#. Select :guilabel:`NEXT`
#. Populate the following:

   .. note:: VMware sample fields provided. Actual options depend on Target Cloud

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
   NUMBER OF WORKERS
    Specify the number of workers to provision
   LOAD BALANCER
    Select an available Load Balancer (cluster layouts only) }
   User Config
     CREATE YOUR USER
       Select to create your user on provisioned hosts (requires Linux user config in |morpheus| User Profile)
     USER GROUP
       Select User group to create users for all User Group members on provisioned hosts (requires Linux user config in |morpheus| User Profile for all members of User Group)
   Advanced Options
    DOMAIN
      Specify Domain override for DNS records
    HOSTNAME
      Set hostname override (defaults to Instance name unless an Active Hostname Policy applies)

#. Select :guilabel:`NEXT`
#. Select optional Workflow to execute
#. Select :guilabel:`NEXT`
#. Review and select :guilabel:`COMPLETE`

   - The Master Node(s) will provision first.
   - Upon successful completion of VM provision, Kubernetes scripts will be executed to install and configure Kubernetes on the Masters.
       .. note:: Access to the sites listed in the `Requirements`_ section is required from Master and Worker nodes over 443
   - After Master or Masters are successfully provisioned and Kubernetes is successfully installed and configured, the Worker Nodes will provision in parallel.
   - Provision status can be viewed:
      - From the Status next to the Cluster in ``Infrastructure -> Clusters``
      - Status bar with eta and current step available on Cluster detail page, accessible by selecting the Cluster name from ``Infrastructure -> Clusters``
   - All process status and history is available
     - From the Cluster detail page History tab, accessible by selecting the Cluster name from ``Infrastructure -> Clusters`` and the History tab
     - From `Operations - Activity - History`
     - Individual process output available by clicking `i` on target process

#. Once all Master and Worker Nodes are successfully provisioned and Kubernetes is installed and configured, the Cluster status will turn green.

    .. IMPORTANT:: Cluster provisioning requires successful creation of VMs, Agent Installation, and execution of Kubernetes workflows. Consult process output from ````Infrastructure -> Clusters - Details`` and morpheus-ui current logs at ``Administration - Health - Morpheus Logs`` for information on failed Clusters.

Intra-Kubernetes Cluster Port Requirements
``````````````````````````````````````````

The table below includes port requirements for the machines within the cluster (not for the |morpheus| appliance itself). Check that the following ports are open on Control-plane and Worker nodes:

.. list-table:: **Control-plane node(s)**
  :widths: auto
  :header-rows: 1

  * - Protocol
    - Direction
    - Port Range
    - Purpose
    - Used By
  * - TCP
    - Inbound
    - 6443
    - Kubernetes API Server
    - All
  * - TCP
    - Inbound
    - 6783
    - Weaveworks
    - 
  * - TCP
    - Inbound
    - 2379-2380
    - etcd server client API
    - kube-apiserver, etcd
  * - TCP
    - Inbound
    - 10250
    - kubelet API
    - Self, Control plane
  * - TCP
    - Inbound
    - 10251
    - kube-scheduler
    - Self
  * - TCP
    - Inbound
    - 10252
    - kube-controller-manager
    - Self

.. list-table:: **Worker node(s)**
  :widths: auto
  :header-rows: 1

  * - Protocol
    - Direction
    - Port Range
    - Purpose
    - Used By
  * - TCP
    - Inbound
    - 10250
    - kubelet API
    - Self, Control plane
  * - TCP
    - Inbound
    - 30000-32767
    - NodePort Services
    - All

Adding Worker Nodes
^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure - Clusters``
#. Select ``v MORE`` for the target cluster
#. Select ``ADD (type) Kubernetes Worker``

   NAME
      Name of the Worker Node. Auto=populated with ``${cluster.resourceName}-worker-${seq}``
   DESCRIPTION
      Description of the Worker Node, displayed in Worker tab on Cluster Detail pages, and on Worker Host Detail page
   CLOUD
      Target Cloud for the Worker Node.

#. Select :guilabel:`NEXT`
#. Populate the following:

   .. note:: VMware sample fields provided. Actual options depend on Target Cloud

   SERVICE PLAN
    Service Plan for the new Worker Node
   NETWORK
    Configure network options for the Worker node.
   HOST
    If Host selection is enabled, optionally specify target host for new Worker node
   FOLDER
    Optionally specify target folder for new Worker node
      Advanced Options
       DOMAIN
         Specify Domain override for DNS records
       HOSTNAME
         Set hostname override (defaults to Instance name unless an Active Hostname Policy applies)

#. Select :guilabel:`NEXT`
#. Select optional Workflow to execute
#. Select :guilabel:`NEXT`
#. Review and select :guilabel:`COMPLETE`

.. note:: Ensure there is a default StorageClass available when using a Morpheus Kubernetes cluster with OpenEBS so that Kubernetes specs or HELM templates that use a default StorageClass for Persistent Volume Claims can be utilised.

Kubernetes Cluster Detail Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


       - Cluster status check results icon
       - Name of the Cluster
       - Last sync date, time and duration
       - Edit, Delete and Actions buttons
          - Actions
              - Refresh
                  - Sync the Cluster Status
              - Permissions
                 View and edit Cluster Group, Tenant and Service Plan Access
              - View API Token
                 Displays API Token for Cluster
              - View Kube Config
                 Displays Cluster Configuration
       - Costs this month (to date, when ``Show Costing`` is enabled)
       - Cluster resource utilization stats
       - Counts for current Masters, Workers, Containers, Services, Jobs and Discovered Containers in the Cluster

.. tabs::

    .. tab:: SUMMARY

       .. image:: /images/infrastructure/clusters/kubeClusterSummary.png

       Kubernetes Cluster summary tab contains:

       - More Cluster metadata including Name, Type, Created By, Worker CPU, Worker Memory (used/max), Worker Storage (used/max), Enabled: Yes/No, and Description.
       - Memory chart with total Cluster Free and Used Memory over last 24 hours
       - Storage chart with total Cluster Reserved and Used Storage over last 24 hours
       - CPU chart with total Cluster CPU Utilization over last 24 hours
       - IOPS Chart with total Cluster IOPS over last 24 hours
       - IOPS Chart with total Cluster Network utilization over last 24 hours

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
