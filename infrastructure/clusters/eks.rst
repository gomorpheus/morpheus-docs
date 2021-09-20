EKS Clusters
------------

Provisions a new Elastic Kubernetes Service (EKS) Cluster in target AWS Cloud.

.. note:: EKS Cluster provisioning is different than creating a Kubernetes Cluster type in AWS EC2, which creates EC2 instances and configures Kubernetes, outside of EKS.

|morpheus| currently supports EKS in the following regions: ``us-east-1``, ``us-east-2``, ``us-west-2``, ``ap-south-1``, ``ap-northeast-2``, ``ap-southeast-1``, ``ap-southeast-2``,
		``ap-northeast-1``, ``eu-central-1``, ``eu-west-1``, ``eu-west-2``, ``eu-west-3``, ``eu-north-1``

Create an EKS Cluster
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure - Clusters``
#. Select :guilabel:`+ ADD CLUSTER`
#. Select ``EKS Cluster``
#. Populate the following:

    LAYOUT
     Select server layout for EKS Cluster
    PUBLIC IP
     Subnet Default
       Use AWS configured Subnet setting for Public IP assignment
     Assigned EIP
       Assigned Elastic IP to Controller and Worker Nodes. Requires available EIP's
    CONTROLLER ROLE
      Select Role for EKS Controller from synced role list
    CONTROLLER SUBNET
      Select subnet placement for EKS Controller
    CONTROLLER SECURITY GROUP
      Select Security Group assignment for EKS Controller
    WORKER SUBNET
      Select Subnet placement for Worker Nodes
    WORKER SECURITY GROUP
      Select Security Group assignment for Worker Nodes
    WORKER PLAN
      Select Service Plan (EC2 Instance Type) for Worker Nodes
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
