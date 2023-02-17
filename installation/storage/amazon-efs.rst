.. _amazon-efs:

Amazon EFS
----------

Introduction
^^^^^^^^^^^^

Amazon Elastic File System (EFS) automatically grows and shrinks as you add and remove files with no need for management or provisioning.  It can be designed to be multi-AZ
capable, allows scaling up, and minimal downtime.

At the time of this writing, |morpheus| is designed to use the NFS protocol for shared storage, which EFS supports.

Create Amazon EFS (UI)
^^^^^^^^^^^^^^^^^^^^^^

.. note:: The following configuration has recommended values but requirements may differ per customer

#. Login to the AWS console:

    http://console.aws.amazon.com/

#. Navigate to the ``EC2`` section by searching at the top
#. Click the ``Security Groups`` link on the left side
#. Create a Security Group that allows ``Inbound`` for port ``2049`` to allow NFS traffic from the nodes
#. Once the Security Group is crearted, navigate to the ``Amazon EFS`` section by searching at the top
#. Click the ``Get started`` button.  If the ``Get started`` button is not available, click the ``File systems`` link on the left side and then click the ``Create file system`` button
#. Click the ``Customize`` button, which will provide many more settings
#. Ensure the following settings are chosen for the ``File system settings`` page:
    
    .. list-table:: **Minimum Required File system Settings**
        :header-rows: 1

        * - Setting
          - Value
        * - Storage Class
          - Standard

#. Click the ``Next`` button
#. Ensure the following settings are chosen for the ``Network access`` page:
    
    .. list-table:: **Minimum Required File system Settings**
        :header-rows: 1

        * - Setting
          - Value
        * - Virtual Private Cloud (VPC)
          - Choose the appropriate VPC
        * - Mount targets
          - Choose one subnet from at least two AZs and assign the Security Group previously created

#. Click the ``Next`` button
#. On the ``File system policy`` page, click the ``Next`` button, as nothing will be modified
#. Finally, click the ``Create`` button after reviewing the settings

  .. note:: Any settings not listed above can be kept at their default, or items such as usernames, VPCs, maintenance, etc. are all preferences of the customer and will not affect the performance or availability

Create Amazon EFS (CLI)
^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with using the AWS CLI, you can run the following commands to more easily create the file system, instead of using the UI.

#. Install the AWS CLI following the documentation:

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#. Setup the authentication for the AWS CLI, using one of the many methods.  Environment variables are recommended:

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

#. Finally, run the below commands to create the shared storage:

  Documentation:  https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html

  .. code-block:: bash

      # Set all variables to preferred values
      creation_token="morpheusefs"
      security_groups="sg-0c3fdeff0a97d2a1b"
      subnet_id1="subnet-0ed95648b7e27a375"
      subnet_id2="subnet-00422803877471552"

      # Create EFS
      file_system_id=$(aws efs create-file-system --creation-token $creation_token \
        --performance-mode generalPurpose \
        --encrypted \
        --backup | grep "FileSystemId" | awk '{print $2}' | sed -r 's/"|,//g')

      # Wait a few seconds before proceeding, for the EFS to be fully created
      # Create mount for subnet1
      aws efs create-mount-target --file-system-id $file_system_id \
        --subnet-id $subnet_id1 \
        --security-groups $security_groups

      # Create mount for subnet2
      aws efs create-mount-target --file-system-id $file_system_id \
        --subnet-id $subnet_id2 \
        --security-groups $security_groups