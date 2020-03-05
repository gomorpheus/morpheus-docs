AWS
---

Overview
^^^^^^^^

AWS is the Amazon public cloud, offering a full range of services and features across the globe in various datacenters. AWS provides businesses with a flexible, highly scalable, and low-cost way to deliver a variety of services using open standard technologies as well as proprietary solutions. This section of documentation will help you get |morpheus| and AWS connected to utilize the features below:

Features
^^^^^^^^

* Virtual Machine Provisioning
* Containers
* Backups / Snapshots
* Resources Groups
* Migrations
* Auto Scaling
* Load Balancing
* AWS Marketplace Search and Provisioning
* Remote Console
* Periodic Synchronization
* Lifecycle Management and Resize
* Restore from Snapshots
* EC2
* RDS
* S3
* ELBs
* ALBs
* Route53
* IAM Profile sync and assignment
* Network Sync
* Security Group Sync (selectable when provisioning, will not appear in Security Groups section)
* Pricing Sync
* Assign Elastic IP's
* Network Pools
* MetaData Tag creation

|morpheus| can provide a single pane of glass and self-service portal for managing instances scattered across both AWS and private cloud offerings like VMWare and Hyper-V.

Requirements
^^^^^^^^^^^^

AWS IAM Security Credentials
  Access Key
  Secret Key
  Sufficient User Privileges (see MinimumIAMPolicies_ section for more info)
Security Group Configuration for Agent Install, Script Execution, and Remote Console Access
  Typical Inbound ports open from |morpheus| Appliance: 22, 5985, 3389
  Typical Outbound to |morpheus| Appliance: 80, 443

  .. NOTE:: These are required for |morpheus| agent install, communication, and remote console access for windows and linux. Other configurations, such as docker instances, will need the appropriate ports opened as well. Cloud-init Agent Install mode does not require incoming access for port 22.
Network(s)
  IP assignment required for Agent install, Script Execution, and Console if the |morpheus| Appliance is not able to communicate with AWS instances private ip's.

.. NOTE:: Each AWS Cloud in |morpheus| is scoped to an AWS Region and VPC Multiple AWS Clouds can be added and even Grouped. Verify Security groups are properly configured in all Regions |morpheus| will scope to.

Adding an AWS Cloud
^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds`
#. Select `+ Create Cloud`
#. Select AWS
#. Enter the following:

   Name
     Name of the Cloud in |morpheus|
   Location
     Description field for adding notes on the cloud, such as location.
   Visibility
     For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   Region
     Select AWS Region for the Cloud
   Access Key
     Access Key ID from AWS IAM User Security Credentials.
   Secret Key
     Secret Access Key associate with the Access Key ID.
   Use Host IAM Credentials
     Must be marked to use secure token service (STS) AssumeRole
   Role ARN
     Supports security token service (STS) to AssumeRole by entering an AWS Role ARN
   Inventory
     Basic
      |morpheus| will sync information on all EC2 Instances in the selected VPC the IAM user has access to, including Name, IP Addresses, Platform Type, Power Status, and overall resources sizing for Storage, CPU and RAM, every 5 minutes. Inventoried EC2 Instances will appear as Unmanaged VM's.
     Full
      In addition to the information synced from Basic Inventory level, |morpheus| will gather Resource Utilization metrics for Memory, Storage and CPU utilization per VM.
     Off
      Existing EC2 Instances will not be inventoried

     .. NOTE:: Cloud Watch must be configured in AWS for |morpheus| to collect Memory and Storage utilization metrics on inventoried EC2 instances.

#. The AWS cloud is ready to be added to a group and saved. Additional configuration options available:

IMAGE TRANSFER STORE
  S3 bucket for Image transfers, required for migrations into AWS.

.. include:: /integration_guides/Clouds/advanced_options.rst

.. NOTE:: All fields and options can be edited after the Cloud is created.

.. include:: iampolicies.rst
