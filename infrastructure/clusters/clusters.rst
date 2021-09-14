Clusters
========

Overview
--------

``Infrastructure -> Clusters`` is for creating and managing Kubernetes Clusters, |morpheus| manager Docker Clusters, KVM Clusters, or Cloud specific Kubernetes services such as EKS. The Combo Cluster is a combination Kubernetes, KVM and Functions* Cluster, with all nodes supporting all three provision types.

Cluster Types
^^^^^^^^^^^^^

+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| **Name**           | **Description**                                                                                                                                                                                                                  | **Supported Clouds** | **Provider Type**      |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Kubernetes Cluster | Provisions by default a Kubernetes cluster consisting of 1 Kubernetes Master and 3 Kubernetes Worker nodes. Additional system layouts available including Master clusters. Custom layouts can be created.                        | All                  | Kubernetes             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Docker Cluster     | Provisions by default a Morpheus controlled Docker Cluster with 1 host. Additional hosts can be added. Custom layouts can be created. Existing Morpheus Docker Hosts are automatically converted to Clusters upon 4.0.0 upgrade. | All                  | Docker                 |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| EKS Cluster        | Provisions a EKS master and 3 EC2 worker node.                                                                                                                                                                                   | AWS                  | Kubernetes             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| AKS Cluster        |                                                                                                                                                                                                                                  | Azure                | Kubernetes             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| KVM Cluster        | Provisions by default a Morpheus controlled KVM Cluster with 1 host. Additional hosts can be added. Custom layouts can be created. Existing Morpheus KVM Hosts are automatically converted to Clusters upon 4.0.0 upgrade.       | VMware, Bare Metal   | KVM                    |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Combo Cluster      | Provisions by default a Morpheus controlled Docker, VM and Functions* Cluster with 1 host. Additional hosts can be added.                                                                                                        | VMware, Bare Metal   | Morpheus               |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Ext Kubernetes     | Brings an existing (brownfield) Kubernetes cluster into Morpheus                                                                                                                                                                 | All                  | Kubernetes             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+

Requirements
------------

- Morpheus Role permission ``Infrastructure: Clusters -> Full`` required for Viewing, Creating, Editing and Deleting Clusters.
- Morpheus Role permission ``Infrastructure: Clusters -> Read`` required for Viewing Cluster list and detail pages.

Cluster Permissions
-------------------

- Cluster Permissions
    Each Cluster has Group, Tenant and Service Plan access permissions settings ("MORE" > Permissions on the Clusters list page).
- Namespace Permissions
    Individual Namespaces also have Group, Tenant and Service Plan access permissions settings

.. include:: /infrastructure/clusters/kubernetes.rst
.. include:: /infrastructure/clusters/docker.rst
.. include:: /infrastructure/clusters/eks.rst
.. include:: /infrastructure/clusters/gke.rst