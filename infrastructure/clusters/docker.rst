Docker Clusters
---------------

Provisions a new Docker Cluster managed by Morpheus.

To create a new Docker Cluster:

#. Navigate to ``Infrastructure - Clusters``
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
   TAGS
    Internal label(s)

#. Select :guilabel:`NEXT`
#. Populate the following (options depend on Cloud Selection and will vary):

   LAYOUT
    Select from available layouts.
   PLAN
    Select plan for Docker Host
   VOLUMES
    Configure volumes for Docker Host
   NETWORKS
    Select the network for Docker Master & Worker VM's
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
