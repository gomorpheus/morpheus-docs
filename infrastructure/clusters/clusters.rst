Clusters
========

``Infrastructure -> Clusters`` is for creating and managing Container clusters, including Kubernetes Clusters, |morpheus| manager Docker Clusters, or Cloud specific Kubernetes services such as EKS.

Creating Clusters
-----------------

.. NOTE:: Clusters will automatically be created for Clouds with existing Docker Hosts upon upgrade to 4.0.0. Multiple Docker Hosts in the same Cloud will be added to the same Cluster.

The following Cluster Types can be created from the ``Infrastructure - Clusters`` page:

Kubernetes
  Provisions a new Kubernetes Cluster
Docker
  Provisions a new Docker Cluster managed by Morpheus
EKS
  Provisions a new Elastic Kubernetes Service (EKS) Cluster in target AWS Cloud

.. Requirements
.. ^^^^^^^^^^^^

.. include:: /infrastructure/clusters/kubernetes.rst
.. include:: /infrastructure/clusters/docker.rst
.. include:: /infrastructure/clusters/eks.rst
