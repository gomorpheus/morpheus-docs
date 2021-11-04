Migrations
==========

Migration Types
---------------

Hypervisor to Hypervisor
^^^^^^^^^^^^^^^^^^^^^^^^

Store
  |morpheus| will create a snapshot of existing VM and upload the snapshot to virtual image directory. Images that have been uploaded to the Virtual Images library can be converted to VHD, QCOW2, RAW and VMDK formats and then re-provisioned.

New
  |morpheus| will create a snapshot of an existing VM, convert from source format to required destination format, and then provision the VM into the target environment.

Source
  VMWare, Openstack, Xen, Nutanix* Azure* Hyper-V* (* in-development)
Destination
  Softlayer, Openstack, Metapod, Xen, Amazon, VMWare, ESXi, Nutanix, Hyper-V Supported OS Type: Windows or Linux
Service Impact
  Disruptive Migration

Virtual Image Extract
^^^^^^^^^^^^^^^^^^^^^

The Virtual Image extract capabilities allow for a virtual image to be extracted and stored in the virtual image repository or the image can be migrated into a cloud.

Source
  Any Cloud
Destination
  SoftLayer (Only)
Supported OS Type
  Windows
Service Impact
  Non Disruptive
Requirements
  Requires a separate disk or network share to store the image during conversion process. Capacity of the disk or network share should be sized appropriately to support the data that will be exported.

Live Stream
^^^^^^^^^^^

.. NOTE:: Live Stream is deprecated

Live Stream is a linux only streaming process that will take a snapshot of a volume and allow it to be streamed to a destination linux system that is either existing or new. The destination linux must already exist and it can either be a managed or unmanaged VM in |morpheus| . The destination will be overwritten from a root level perspective.

Source
  Any Cloud
Destination
  |morpheus|
Supported OS Type
  Linux (Only)
Service Impact
  Non Disruptive
Requirements
  Requires the Linux host/guest to be configured for LVM and that free space of the capacity to be streamed is available. A destination linux host/guest must be available to receive the stream.

Add Migration
-------------

1. Select the Tools link in the navigation bar.
2. Select the Migrations link in the sub-navigations bar.
3. Click the Add Migration button.
4. From the Create Migration Wizard select the type of migration, then click the :guilabel:`Next` button.

Depending on the Migration Type selected input the following, then click the :guilabel:`Next` button.

* Hypervisor to Hypervisor
    * Select Cloud, and Server
    * Input Host, Remote Port, Username, and Password
* Virtual Image Extract
    * Select Platform, Existing or New, Cloud, and Server.
    * Input Host, WinRM Port, WinRM User, WinRM Password, and Snapshot path.
* Live Stream
    * Select Platform, Existing or New, Cloud, and Server
    * Input Host, SSH Port, SSH User, SSH Password, Public Key, and Logical Volume Device.
    * Enter Destination details, then click the :guilabel:`Next` button.

5. Finalize your configuration if needed, then click the complete button.

Manually Start Migration
------------------------

If you chose to not run your migration in the Create Migration Wizard then you will be able to manually start the migration.

#. Select the Tools link in the navigation bar.
#. Select the Migrations link in the sub-navigations bar.
#. Click the actions dropdown of the row of the migration you wish start, and select Run.


Remove Migration
----------------

#. Select the Tools link in the navigation bar.
#. Select the Migrations link in the sub-navigations bar.
#. Click the actions dropdown of the row of the migration you wish remove, and select Remove.

VMware to AWS Migration
-----------------------

Requirements
^^^^^^^^^^^^

When performing a Hypervisor to Hypervisor migration from VMware to AWS, there are some requirements that must be met:

#. Add S3 Storage Provider to |morpheus|
#. Set Image Transfer Store in you AWS cloud(s) settings in |morpheus|
#. Create VM Import Service roles in your AWS account (not in |morpheus| )
#. Storage Provider selected for migration destination must be set as a Local Storage Provider (not AWS)

Add S3 Storage Provider
^^^^^^^^^^^^^^^^^^^^^^^

An AWS S3 bucket is required for VMware - AWS migrations. S3 buckets created in AWS are automatically synced into Morpheus. S3 buckets can also be created from Morpheus from ``Infrastructure -> Storage -> Buckets``

Set Image Transfer Store
^^^^^^^^^^^^^^^^^^^^^^^^

Under ``Infrastructure -> Clouds``, select your AWS cloud and click :guilabel:`EDIT`. Expand the Advanced Options section and for `IMAGE TRANSFER STORE` select the target AWS S3 Bucket and then Save.

Add VM Import Service
^^^^^^^^^^^^^^^^^^^^^

.. TIP:: Refer to the AWS document below to add the required VM Import Service role in AWS: http://docs.aws.amazon.com/vm-import/latest/userguide/import-vm-image.html

VM Import requires a role to perform certain operations in your account, such as downloading disk images from an Amazon S3 bucket. You must create a role named vmimport with a trust relationship policy document that allows VM Import to assume the role, and you must attach an IAM policy to the role.

To create the service role
``````````````````````````

Create a file named ``trust-policy.json`` with the following policy:

.. code-block:: bash

  {
     "Version": "2012-10-17",
     "Statement": [
        {
           "Effect": "Allow",
           "Principal": { "Service": "vmie.amazonaws.com" },
           "Action": "sts:AssumeRole",
           "Condition": {
              "StringEquals":{
                 "sts:Externalid": "vmimport"
              }
           }
        }
     ]
  }

You can save the file anywhere on your computer. Take note of the location of the file, because you'll specify the file in the next step.

Use the create-role command to create a role named vmimport and give VM Import/Export access to it. Ensure that you specify the full path to the location of the ``trust-policy.json`` file.

.. code-block:: bash

  aws iam create-role --role-name vmimport --assume-role-policy-document file://trust-policy.json


Create a file named `role-policy.json` with the following policy, where disk-image-file-bucket is the bucket where the disk images are stored:

.. code-block:: bash

  {
     "Version": "2012-10-17",
     "Statement": [
        {
           "Effect": "Allow",
           "Action": [
              "s3:ListBucket",
              "s3:GetBucketLocation"
           ],
           "Resource": [
              "arn:aws:s3:::disk-image-file-bucket"
           ]
        },
        {
           "Effect": "Allow",
           "Action": [
              "s3:GetObject"
           ],
           "Resource": [
              "arn:aws:s3:::disk-image-file-bucket/*"
           ]
        },
        {
           "Effect": "Allow",
           "Action":[
              "ec2:ModifySnapshotAttribute",
              "ec2:CopySnapshot",
              "ec2:RegisterImage",
              "ec2:Describe*"
           ],
           "Resource": "*"
        }
     ]
  }

Use the following put-role-policy command to attach the policy to the role created above. Ensure that you specify the full path to the location of the ``role-policy.json`` file.

.. code-block:: bash

  aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document file://role-policy.json

For more information about IAM roles, see IAM Roles in the IAM User Guide.

Storage Providers
^^^^^^^^^^^^^^^^^

Set the "Storage Provider" in the migration wizard destination as a Local Storage type, or leave as Select to use the |morpheus| Appliance.

A local image must be created by |morpheus| prior to S3 upload. A Local Storage provider can be used if one had been added in the ``Infrastructure -> Storage -> File Shares`` section. Simply leaving the Storage Provider setting as "select" will create an image on the |morpheus| appliance, provided sufficient storage existing on the |morpheus| appliance in ``/tmp``.

.. IMPORTANT:: Setting AWS as the Destination Storage Provider will result in a migration failure.

These settings will allow a successful migration from VMware to AWS using the |morpheus| migration wizard.
