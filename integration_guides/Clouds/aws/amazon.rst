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

1. Navigate to `Infrastructure > Clouds`
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
   Secret Access Key associated with the Access Key ID.
 USE HOST IAM CREDENTIALS
   Check to use use Host IAM Credentials
 ROLE ARN
   Supports security token service (STS) to AssumeRole by entering an AWS Role ARN
 EXTERNAL ID
   When required to AssumeRole, included the needed External ID
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

KMS KEY ID
  For specify an AWS KMS key for encrypting EBS Volumes when volume encryption is enabled

Enhanced Invoice Costing Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AWS cloud integrations in |morpheus| will sync highly-granular costing data through the use of AWS Costing & Utilization Reports (CUR). If desired, users can turn on costing in the |morpheus| Cloud configuration without linking a CUR to use AWS Cost Explorer instead. |morpheus| version 4.2.3 also simplified the way CUR reports can be selected or created in order to sync costing data. The section below discusses setting up enhanced costing through CUR reports both in 4.2.3 and versions prior. For additional details on setting up costing with AWS GovCloud, see the next section.

.. NOTE:: Even with a costing report configured in the Cloud integration as described below, the COSTING value must also be set to "Costing and Reservations" in order for enhanced invoice data to be brought into |morpheus|. Confirm this setting by editing the Amazon Cloud integration, and checking the COSTING value in the Advanced Options panel before continuing.

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

        Using the |morpheus| interface to create a CUR, and optionally a new S3 bucket, the IAM user requires permissions in AWS to be successful.  By default, only the root user will have access to billing (including CUR), but billing can be enabled for IAM users
        following Amazon's documentation for `Activating IAM Access <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html>`_.  Once IAM access is activated, policies need to be assigned to the user being configured on the cloud
        in |morpheus|.  If the user is an administrator of the AWS account, no additional policies are needed.  Below are some example policies needed for different scenarios:

          .. toggle-header::
            :header: Creating a new CUR and new S3 bucket **Click to Expand/Hide**

              .. code-block:: json

                {
                  "Version": "2012-10-17",
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Action": [
                              "s3:PutBucketPolicy",
                              "s3:CreateBucket",
                              "s3:ListBucket",
                              "s3:GetBucketPolicy",
                              "cur:DescribeReportDefinitions",
                              "cur:PutReportDefinition"
                          ],
                          "Resource": "*"
                      }
                  ]
                }

          .. toggle-header::
            :header: Creating a new CUR and using an existing S3 bucket **Click to Expand/Hide**

              .. code-block:: json

                {
                  "Version": "2012-10-17",
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Action": [
                              "s3:ListBucket",
                              "s3:GetBucketPolicy",
                              "cur:DescribeReportDefinitions",
                              "cur:PutReportDefinition"
                          ],
                          "Resource": "*"
                      }
                  ]
                }

          .. toggle-header::
            :header: Using an existing CUR **Click to Expand/Hide**

              .. code-block:: json

                {
                  "Version": "2012-10-17",
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Action": [
                              "cur:DescribeReportDefinitions"
                          ],
                          "Resource": "*"
                      }
                  ]
                }

        .. IMPORTANT:: The user configured on the cloud will need access to the objects in the S3 bucket configured on the CUR.  If creating the CUR via the |morpheus| UI, this should be done automatically.  If an existing CUR report or existing S3 bucket was selected, ensure the user has permissions to access the
          objects in the configured S3 bucket.  Alternatively, the **COSTING KEY** and **COSTING SECRET** can be used to configure a different user that has access to the S3 bucket.

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

Global (Costing Aggregator Only) (v5.5.1+)
``````````````````````````````````````````

  Costing can be created for specific clouds individually, following the steps previously mentioned.  If the same account is added multiple times, using different regions, the same CUR file is available to be selected (if the configured user has access).  However,
  this can become a tedious process in needing to configure the CUR on each cloud added to |morpheus|.  However, |morpheus| has a region of `Global (Costing Aggregator Only)`, which can be chosen at the time of adding a cloud.  This region is not designed for
  deploying workloads, it is here primarily for syncing costs.  This means that the AWS account added as a cloud in |morpheus| as a Global region can sync the cost for all the other regions of the same account added as clouds into |morpheus|.

  When using AWS Organizations, if the AWS account added as a global region is the management account (formerly known as master account) and consolidated billing is enabled, costs for **all** accounts can be sync'd using the Global region.  This means when any AWS
  and/or regions in the organization are added as clouds in |morpheus|, the appropriate costs are applied to them automatically.  It does require that **Costing** is enabled on the cloud to see the costs but a Costing Report does not need to be chosen.
  This enables the use of one cloud added as Global to sync all costs and apply to all AWS clouds added in |morpheus|.

  Additionally, some costs in AWS are not region specific, for example the `Global` and `No Region` regions.  These costs do not apply to the regions of the clouds added in |morpheus|.  With the Global region added as a cloud in |morpheus|, you would be able to see
  these costs that are applicable to your accounts.

Costing and AWS GovCloud
^^^^^^^^^^^^^^^^^^^^^^^^

AWS GovCloud delivers Amazon public cloud infrastructure and features in a way that complies with U.S. government standards for security. GovCloud accounts are applied for and must be associated with a pre-existing standard AWS account and the usage and billing data for the GovCloud account is rolled up into that of the standard AWS account. For that reason, Amazon recommends creating a new standard account solely to house the GovCloud account if usage and billing must be tracked separately.

Since GovCloud accounts do not have access to billing data directly, |morpheus| must be able to access it through the associated standard account. You could do this by creating the |morpheus| cloud integration through the standard account itself or by integrating the GovCloud account and supplying an Access Key and Secret Key for the standard account when configuring costing. When needed, add the additional credentials for the standard commercial account as described below:

#. Add a new AWS Cloud or edit an existing one
#. Expand the Advanced Options section
#. Complete the following fields in addition to other required fields needed to set up costing as described in the previous section:

    - **COSTING KEY:** The AWS Key ID for an IAM user with sufficient access who is associated with the standard commercial account
    - **COSTING SECRET:** The AWS Secret Key for an IAM user with sufficient access who is associated with the standard commercial account
    - **LINKED ACCOUNT ID:** The AWS account number for the standard commercial account in which the IAM user referenced in the prior bullets resides

#. Save the changes to the AWS Cloud integration

When credentials are configured correctly, you will be able to select an existing Costing and Usage Report (CUR) from the appropriate S3 bucket if it already exists. If not, you can create one directly from the add/edit AWS Cloud modal in |morpheus|.

.. image:: /images/clouds/aws/invoiceCosting/8govcloudCosting.png
  :width: 50%

AWS Reserved Instances and Savings Plans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Amazon AWS public cloud offers Reserved Instances (RI) and Savings Plans, which allow organizations with consistent use patterns to reduce cloud spend significantly. |morpheus| analyzes AWS cloud usage and spend, which allows it to make intelligent recommendations that can lead to significant savings. This data can be reviewed in the Reservation Recommendations and Savings Plan Recommendations tables on any AWS Cloud detail page (Infrastructure > Clouds > Selected Amazon Cloud).

Savings Plans potentially offer greater than 70% savings in exchange for a commitment to consistent usage levels for a 1- or 3-year term. |morpheus| provides Savings Plan guidance based on learned analytics; allowing you to analyze Savings Plans based on different term commitments and upfront costs to choose the best savings plan.

.. image:: /images/integration_guides/clouds/aws/savingsPlan.png

Reserved Instances (RI) provide a discounted hourly rate and optional capacity reservation for EC2 instances. AWS billing automatically applies your RI-discounted rate when the attributes of EC2 instance usage match attributes of an active RI. |morpheus| provides RI guidance based on learned analytics.

.. image:: /images/integration_guides/clouds/aws/ri.png

To retrieve Reserved Instances and Savings Plans data, the user configured on the cloud will require access to **Cost Explorer**.  Below is an example IAM policy with Cost Explorer access:

  .. toggle-header::
    :header: Cost Explorer Policy **Click to Expand/Hide**

      .. code-block:: json

        {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Action": [
                      "ce:*"
                  ],
                  "Resource": "*"
              }
          ]
        }

.. include:: /integration_guides/Clouds/aws/iampolicies.rst
