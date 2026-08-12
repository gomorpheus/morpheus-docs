Docker Clusters
===============

Provisions a new Docker Cluster managed by Morpheus.

Docker Data Volume
------------------

Docker host layouts can expose a configurable data volume in addition to the operating system volume. Configure the volumes required by the selected layout and target Cloud in the provisioning wizard. A separate Docker-data disk is not a universal prerequisite; do not add one unless the selected layout or your storage design requires it.

To create a new Docker Cluster:

#. Navigate to ``Infrastructure > Clusters``
#. Select :guilabel:`+ ADD CLUSTER`
#. Select ``Docker Cluster``
#. Populate the following:

   CLOUD
    Select target Cloud
   CLUSTER NAME
    Name for the Docker Cluster
   RESOURCE NAME
    Name for Docker Cluster resources
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
#. Populate the following (options depend on Cloud Selection and will vary):

   LAYOUT
    Select from available layouts.
   PLAN
    Select plan for Docker Host
   VOLUMES
     Configure volumes for Docker Host. The available operating system and data-volume options depend on the selected layout and Cloud
   NETWORKS
    Select the network for Docker Master & Worker VM's
   NUMBER OF HOSTS
    Specify the number of hosts to be created
   User Config
     CREATE YOUR USER
       Select to create your user on provisioned hosts (requires Linux user config in |morpheus| User Profile)
     USER GROUP
       Select User group to create users for all User Group members on provisioned hosts (requires Linux user config in |morpheus| User Profile for all members of User Group)
   Advanced Options
    DOMAIN
      Specify Domain for DNS records
    HOSTNAME
      Set hostname (defaults to Instance name)

#. Select :guilabel:`NEXT`
#. Select optional Workflow to execute
#. Select :guilabel:`NEXT`
#. Review and select :guilabel:`COMPLETE`
