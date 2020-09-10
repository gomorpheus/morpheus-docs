AWS
---

Overview
^^^^^^^^

AWS is the Amazon public cloud, offering a full range of services and features across the globe in various datacenters. AWS provides businesses with a flexible, highly scalable, and low-cost way to deliver a variety of services using open standard technologies as well as proprietary solutions. This section of documentation will help you get |morpheus| and AWS connected to utilize the features below:

Features
^^^^^^^^

* Instance, Service, Infrastructure Provisioning & Synchronization
* EKS Cluster Creation & Synchronization
* |morpheus| Kubernetes, Docker & KVM Cluster Creation 
* ELB Classic Load Balancer Creation & Synchronization
* ELB Application Load Balancer (ALB) Creation & Synchronization
* Security Group Creation & Synchronization
* Security Group Rule Creation & Synchronization
* Network Synchronization
* VPC Creation & Synchronization
* CloudFormation Provisioning & Resource Synchronization 
* Terraform Provisioning & Resource Synchronization
* Pricing & Costing Synchronization
* MetaData Tag Creation & Synchronization
* S3 Bucket Creation & Synchronization
* Route53 Automation & Synchronization
* IAM Profile Synchronization and Assignment
* RDS Support 
* Backups / Snapshots
* Migrations
* Auto Scaling
* Remote Console (SSH & RDP)
* Lifecycle Management and Resize
* Restore from Snapshots
* Elastic IP Assignment
* Network Pools
* Enhanced Invoice Costing


Requirements
^^^^^^^^^^^^

AWS IAM Security Credentials
  Access Key
  Secret Key
  Sufficient User Privileges (see MinimumIAMPolicies_ section for more info)
Security Group Configuration for Agent Install, Script Execution, and Remote Console Access
  - Typical Inbound ports open from |morpheus| Appliance: 22, 5985, 3389 (22 & 3389 required for Console. 22 & 5985 required for agent-less comms)
  - Typical Outbound to |morpheus| Appliance: 443 (Required for Agent install & comms)

  .. NOTE:: These are required for |morpheus| agent install, communication, and remote console access for windows and linux. Other configurations, such as docker instances, will need the appropriate ports opened as well. Cloud-init Agent Install mode does not require incoming access for port 22.
  
Network(s)
  IP assignment required for Agent install, Script Execution, and Console if the |morpheus| Appliance is not able to communicate with AWS instances private ip's.

.. NOTE:: Each AWS Cloud in |morpheus| is scoped to an AWS Region and VPC. Multiple AWS Clouds can be added and even grouped if different region and VPC combinations are needed. It's also recommended you verify Security Groups are properly configured in all regions |morpheus| Clouds will scope to.

Adding an AWS Cloud
^^^^^^^^^^^^^^^^^^^

1. Navigate to `Infrastructure -> Clouds`
2. Select `+ Create Cloud`
3. Select AWS
4. Enter the following:

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````
 REGION
   Select AWS Region for the Cloud
 ACCESS KEY
   Access Key ID from AWS IAM User Security Credentials.
 SECRET KEY
   Secret Access Key associate with the Access Key ID.
 USE HOST IAM CREDENTIALS
   Check to use use Host IAM Credentials
 ROLE ARN
   Supports security token service (STS) to AssumeRole by entering an AWS Role ARN
 INVENTORY
   Basic
    |morpheus| will sync information on all EC2 Instances in the selected VPC the IAM user has access to, including Name, IP Addresses, Platform Type, Power Status, and overall resources sizing for Storage, CPU and RAM, every 5 minutes. Inventoried EC2 Instances will appear as Unmanaged VM's.
   Full
    In addition to the information synced from Basic Inventory level, |morpheus| will gather Resource Utilization metrics for Memory, Storage and CPU utilization per VM.
   Off
    Existing EC2 Instances will not be inventoried

   .. NOTE:: Cloud Watch must be configured in AWS for |morpheus| to collect Memory and Storage utilization metrics on inventoried EC2 instances.

 USE VPC
    Specify if the target account is using EC2-VPC or EC2-Classic Platform. In almost all cases, VPC should be selected, and then select the target VPC from the synced available VPC's list, or `All` VPC's.
   
5. The AWS cloud is ready to be added to a group and saved. Additional configuration options available:

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

In addition to standard AWS costing data (Enabled by editing the AWS cloud integration and setting the COSTING value to "Costing" or "Costing and Reservations"), |morpheus| can utilize highly-granular data from AWS Costing and Utilization Reports (CUR) in its integration. Once enabled, this data can be consumed by accessing Invoice endpoints of |morpheus| API and eventually through the UI after a future update. Continue on with this section to enable these reports in the AWS web console and configure the |morpheus| cloud integration to work with this report data.

In |morpheus| version 4.2.3 and higher, |morpheus| can do most of the legwork to create or sync in the CUR report for you. In versions prior, the report needed to be set up within the AWS web console and the configuration information provided to the |morpheus| cloud integration. Both processes are outlined below.

.. content-tabs::

    .. tab-container:: tab1
        :title: v4.2.3 and Above

        In |morpheus| 4.2.3+, edit the Amazon cloud integration or create a new Amazon Cloud to get started. On the Create/Edit Cloud modal, open the advanced options section. The relevant fields for configuring invoice costing are shown below:

        .. image:: /images/clouds/aws/invoiceCosting/0billingFields.png

        In the example case above, a new report and a new S3 bucket are created but |morpheus| will also sync in buckets and reports that meet the required parameters if they already exist. For reports to be synced they must meet the requirements listed below:

        - Hourly time granularity
        - Include resource IDs
        - GZIP compression
        - CSV format

        If you don't currently have a report meeting those criteria, you can create one by selecting "New Report" from the REPORT NAME dropdown menu. A new S3 bucket can be created in similar fashion if needed. You may also want to review the section below on configuration for |morpheus| 4.2.2 and below to note policies that will be applied to your selected bucket and Cost Explorer permissions required for the AWS cloud user associated with the |morpheus| Cloud integration.

        In the end, the following fields must be filled in order to complete the process:

        - **COSTING BUCKET:** The S3 bucket name
        - **COSTING REGION:** The region the bucket was created in
        - **COSTING FOLDER:** This is the report path prefix if you configured one earlier
        - **COSTING REPORT NAME:** The name given to your CUR report
        - **COSTING KEY:** If the IAM user for this AWS cloud integration does not have access to the S3 bucket with the CUR data, enter the AWS Key ID for an IAM user with access
        - **COSTING SECRET:** If the IAM user for this AWS cloud integration does not have access to the S3 bucket with the CUR data, enter the AWS Secret Key for the IAM account whose Key ID you entered in the previous field
        - **LINKED ACCOUNT ID:** If the IAM user for this AWS cloud integration does not have access to the S3 bucket with the CUR data, enter the AWS account number that the IAM user from the above step resides in

        .. NOTE:: If the AWS cloud account is a GovCloud account, enter the COSTING KEY, COSTING SECRET, and LINKED ACCOUNT ID for the master commercial account your GovCloud account is associated with.
    


    .. tab-container:: tab2
        :title: v4.2.2 and Below

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

        Save changes to your cloud integration.

        .. IMPORTANT:: It may take as long as one hour for |morpheus| to process the next CUR report.


.. include:: /integration_guides/Clouds/aws/iampolicies.rst
