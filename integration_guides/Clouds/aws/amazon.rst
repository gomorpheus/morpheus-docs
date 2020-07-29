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

.. NOTE:: Each AWS Cloud in |morpheus| is scoped to an AWS Region and VPC. Multiple AWS Clouds can be added and even grouped if different region and VPC combinations are needed. It's also recommended you verify Security Groups are properly configured in all regions |morpheus| Clouds will scope to.

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
     Check to use use Host IAM Credentials
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
EBS ENCRYPTION
  Enable or disable encrytion of EBS Volumes
COSTING KEY
  For Gov Cloud pricing only, key for standard managing cost account
COSTING SECRET
  For Gov Cloud pricing only, secret for standard managing cost account

.. include:: /integration_guides/Clouds/advanced_options.rst

Enhanced Invoice Costing Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to standard AWS costing data (Enabled by editing the AWS cloud integration and setting the COSTING value to "Costing" or "Costing and Reservations"), |morpheus| can also utilize highly-granular from AWS Costing and Utilization Reports (CUR) in its integration. Once enabled, this data can be consumed by accessing Invoice endpoints of |morpheus| API and eventually through the UI after a future update. Continue on with this section to enable these reports in the AWS web console and configure the |morpheus| cloud integration to work with the report data.

Begin by logging into the `AWS Billing Console <https://console.aws.amazon.com/billing/home?#/>`_, then click :guilabel:`Create report`.

.. image:: /images/clouds/aws/invoiceCosting/1billingConsole.png

Include a name for your report and mark the box to "Include resource IDs". |morpheus| uses these resource IDs to map costs to various resources. Click :guilabel:`Next`.

.. image:: /images/clouds/aws/invoiceCosting/2reportConfig.png

On the following page, begin by identifying an S3 bucket to house reports. Click :guilabel:`Configure` near the top of the page and select an existing bucket or create a new one.

.. image:: /images/clouds/aws/invoiceCosting/4chooseBucket.png

After identifying the bucket, you must mark the box to accept the default policy being applied to the bucket. Click :guilabel:`Save`.

.. image:: /images/clouds/aws/invoiceCosting/5confirmPolicy.png

The default policy applied to the bucket is below:

.. code-block:: bash

  {
    "Version": "2008-10-17",
    "Id": "SomeID",
    "Statement": [
      {
        "Sid": "SomeStmtID",
        "Effect": "Allow",
        "Principal": {
          "Service": "billingreports.amazonaws.com"
        },
        "Action": [
          "s3:GetBucketAcl",
          "s3:GetBucketPolicy"
        ],
        "Resource": "arn:aws:s3:::bucket-name"
      },
      {
        "Sid": "SomeStmtID",
        "Effect": "Allow",
        "Principal": {
          "Service": "billingreports.amazonaws.com"
        },
        "Action": [
          "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::bucket-name/*"
      }
    ]
  }

After choosing a bucket, accepting the default policy, and saving the change, you're brought back to the report delivery page. By default, CUR reports are saved to a folder at the path ``my-report-name/date-folder``. If this bucket already contains CUR reports, you may want to specify a prefix path in the "Report path prefix" field. Outside of this field, use the default values as shown in the screenshot below, then click :guilabel:`Next`.

.. image:: /images/clouds/aws/invoiceCosting/6completeDelivery.png

On the following page, make your final review and click :guilabel:`Review and Complete`. Following this, you will see your newly configured report in the list of CUR report(s).

In addition, the AWS cloud user associated with the integration in |morpheus| needs IAM policy permission to access Cost Explorer. Attach a policy like the one below to this cloud user:

.. code-block:: bash

  {
    "Version": "2012-10-17",
    "Id": "SomeID",
    "Statement": [
      {
        "Sid": "SomeStmtID",
        "Effect": "Allow",
        "Action": [
          "ce:DescribeReportDefinitions",
          "ce:DescribeCostCategoryDefinition",
          "ce:ListCostCategoryDefinitions"
        ],
        "Resource": [
          "*"
        ]
      }
    ]
  }

.. NOTE:: If the Cost Explorer permissions are granted at the master account level, the user will see all costs for each member account; if granted at the member account, only the costs for that member account are available.

With the AWS console configuration steps complete, we can move back into |morpheus|. Keep in mind it is only necessary to set up one AWS cloud for Costing since we process all records in the CUR report.

Once back in |morpheus|, add or edit the relevant AWS cloud integration (Infrastructure > Clouds > :guilabel:`+ ADD` OR click the pencil icon in the row for the chosen AWS integration). Expand the Advanced Options drawer and complete the following fields:

- **COSTING BUCKET:** The S3 bucket name
- **COSTING REGION:** The region the bucket was created in
- **COSTING FOLDER:** This is the report path prefix if you configured one earlier
- **COSTING REPORT NAME:** The name given to your CUR report
- **COSTING KEY:** If the IAM user for this AWS cloud integration does not have access to the S3 bucket with the CUR data, enter the AWS Key ID for an IAM user with access
- **COSTING SECRET:** If the IAM user for this AWS cloud integration does not have access to the S3 bucket with the CUR data, enter the AWS Secret Key for the IAM account whose Key ID you entered in the previous field
- **LINKED ACCOUNT ID:** If the IAM user for this AWS cloud integration does not have access to the S3 bucket with the CUR data, enter the AWS account number that the IAM user from the above step resides in

.. NOTE:: If the AWS cloud account is a GovCloud account, enter the COSTING KEY, COSTING SECRET, and LINKED ACCOUNT ID for the master commercial account your GovCloud account is associated with.

.. image:: /images/clouds/aws/invoiceCosting/7morphConfig.png

.. IMPORTANT:: It may take as long as one hour for |morpheus| to process the next CUR report.

.. include:: iampolicies.rst
