Kubernetes
==========

Overview
--------

The Kubernetes Cloud type allow users to inventory and provision to existing Kubernetes clusters. New Kubernetes clusters can also be provisioning using Docker mode setting in clouds and provisioning new Docker hosts.

Add Kubernetes Cloud
--------------------

#. Navigate to Infrastructure -> Clouds
#. Select `+ CREATE CLOUD`, select Kubernetes Cloud, and then click Next.
#. Enter the following into the Create Cloud modal:

   Name
    Name of the Cloud in |morpheus|
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   API URL
    Kubernetes API URL
   API TOKEN
    Kubernetes User API Token
   Inventory Existing Instances
    If enabled, existing Containers will be inventoried and appear in the Containers tab for the Kubernetes Cloud..

#. Save Changes

Create Kubernetes Cluster
-------------------------

Kubernetes Clusters can be provisioned into any Cloud Type by setting the CONTAINER MODE to Kubernetes in the Advanced Settings of a Cloud.

.. IMPORTANT:: The CONTAINER MODE must be set prior to provisioning any Docker Hosts. Once Docker Hosts exist in a Cloud, the CONTAINER MODE setting cannot be changed.

Once the CONTAINER MODE is set on a Cloud, a Kubernetes Cluster can be created by selecting :guilabel:`+ CONTAINER HOST` ->  `Kubernetes Master` and then `Kubernetes Worker` from `Infrastructure -> Hosts` or `Infrastructure -> Clouds` -> select Cloud -> `Hosts`.

IMPORTANT:: For the Kubernetes Cluster to be successfully created, the Kubernetes Master must finish provisioning before the worker(s) are created. Do not start provisioning a worker in the cluster until the Master is completed.
