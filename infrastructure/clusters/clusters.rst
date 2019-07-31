Clusters
========

``Infrastructure -> Clusters`` is for creating and managing Container clusters, including Kubernetes Clusters, |morpheus| manager Docker Clusters, or Cloud specific Kubernetes services such as EKS.

Creating Clusters
-----------------

.. NOTE:: Clusters will automatically be created for Clouds with existing Docker Hosts upon upgrade to 4.0.0. Multiple Docker Hosts in the same Cloud will be added to the same Cluster.

The following Cluster Types can be created from the ``Infrastructure - Clusters`` page:

+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| **Name**           | **Description**                                                                                                                                                                                                                  | **Supported Clouds** | **Provision Type **    |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Kubernetes Cluster | Provisions by default a Kubernetes cluster consisting of 1 Kubernates Master and 3 Kubernetes Worker nodes. Additional system layouts available including Master clusters. Custom layouts can be created.                        | All                  | Docker                 |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Docker Cluster     | Provisions by default a Morpheus controlled Docker Cluster with 1 host. Additional hosts can be added. Custom layouts can be created. Existing Morpheus Docker Hosts are automatically converted to Clusters upon 4.0.0 upgrade. | All                  | Docker                 |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| EKS Cluster        | Provisions a EKS master and 3 EC2 worker node.                                                                                                                                                                                   | AWS                  | Docker                 |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| KVM Cluster        | Provisions by default a Morpheus controlled KVM Cluster with 1 host. Additional hosts can be added. Custom layouts can be created. Existing Morpheus KVM Hosts are automatically converted to Clusters upon 4.0.0 upgrade.       | All                  | VM                     |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+
| Triforce           | Provisions by default a Morpheus controlled Docker, VM and Functions* Cluster with 1 host. Additional hosts can be added.                                                                                                        | VMware, Bare Metal   | Docker, VM, Functions* |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------+


.. Requirements
.. ^^^^^^^^^^^^

.. include:: /infrastructure/clusters/kubernetes.rst
.. include:: /infrastructure/clusters/docker.rst
.. include:: /infrastructure/clusters/eks.rst
