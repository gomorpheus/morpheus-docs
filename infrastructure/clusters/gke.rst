GKE Clusters
------------

Provisions a new Google Kubernetes Engine (GKE) Cluster in target Google Cloud.

.. note:: Ensure proper permissions exist for the Google Clouds service account to create, inventory and manage GKE clusters. 

Create an GKE Cluster
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure - Clusters``
#. Select :guilabel:`+ ADD CLUSTER`
#. Select ``GKE Cluster``
#. Populate the following:

    CLOUD
     Select target Cloud
    CLUSTER NAME
     Name for the GKE Cluster
    RESOURCE NAME
     Name for GKE Cluster resources/hosts
    DESCRIPTION
     Description of the Cluster
    VISIBILITY
     Public
       Available to all Tenants
     Private
       Available to Master Tenant
    LABELS
     Internal label(s)

    LAYOUT
     Select cluster layout for GKE Cluster
    RESOURCE POOL
     Specify an available Resource Pool from the selected Cloud
    GOOGLE ZONE
     Specify Region for the cluster
    VOLUMES
     Cluster hosts volume size and type
    NETWORKS
     Select GCP subnet(s) and config 
    WORKER PLAN
     Service Plan for GKE worker nodes
    RELEASE CHANNEL
     Regular, Rapid, Stable or Static 
    CONTROL PLANE VERSION
     Select from available synced GKE k8's versions
    NUMBER OF WORKERS
     Number of worker nodes to be provisioned

#. Select :guilabel:`NEXT`
#. Select optional Workflow to execute
#. Select :guilabel:`NEXT`
#. Review and select :guilabel:`COMPLETE`
