Policies
========

Overview
--------

Policies add governance, ease of use, cost-savings, and auditing features to |morpheus| . Policies can be created in the Policies tabs in Groups and Clouds. Policy generation is a role permission.

Policies apply towards any instance provisioned into a group or cloud with active policies. Cloud policies will override matching or conflicting group policies during provisioning.

Available Policy Types
----------------------

-  Expiration
-  Host Name
-  Hostname
-  Instance Name
-  Max Containers
-  Max Cores
-  Max Hosts
-  Max Memory
-  Max Storage
-  Max VMs
-  Power Scheduling
-  Provision Approval
-  Shutdown

Creating Policies
-----------------

Policies can be created, edited, and set to active or inactive in the a
group or cloud detail pane under the Policies tab.

To create a Policy for a Cloud:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cloud Policies apply to all Instances in the Cloud the Policy is added to.

#. Navigate to ``Infrastructure -> Clouds``
#. Select a Cloud by clicking on the name of the Cloud to go to the Cloud Detail page.
#. Select the ``POLICIES`` tab in the Cloud Detail page.
#. Select :guilabel:`+ ADD` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuraiton options.
#. Select :guilabel:`SAVE CHANGES`

To create a Policy for a Group:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Group Policies apply to all Instances in the Group the Policy is added to.

#. Navigate to ``Infrastructure -> Clouds``
#. Select a Cloud by clicking on the name of the Cloud to go to the Cloud Detail page.
#. Select the ``POLICIES`` tab in the Cloud Detail page.
#. Select :guilabel:`+ ADD` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuraiton options.
#. Select :guilabel:`SAVE CHANGES`

Expiration Policies
^^^^^^^^^^^^^^^^^^^

Expiration policies set an expiration timeframe for any instance
provisioned into the cloud or group the policy is added to. When an
instance expires, it is terminated and deleted.

Configuration options for expiration policies:

Expiration Type
  * User Configurable- expiration timeframe is editable during provisioning
  * Fixed Expiration- user cannot change expiration timeframe

Expiration Days
  Configures the number of days the instance is allowed to exist before being removed.
Renewal Days
  If the instance is renewed, this is the number of days by which the expiration date is increased.
Notification Days
  This allows an email notice to be sent out X days before the instance is set to expire.
Notification Message
  Customizable message for notification emaila. The default message is ``Instance ${instance?.name} is set to expire on ${instance?.expireDate}``
Auto Approve Extensions
  Enable this to auto-approve extension requests, bypassing approval workflows.

Instances with expirations show the time until expiration in the instance detail pane. Instances with active expiration policies can be extended by selecting the EXTEND NOW button in the instance detail pane. The extension length is set in the policy by the RENEWAL DAYS field.

Expirations can also be added to any instance during provisioning by entering the number of days in the EXPIRATION DAYS field in the Lifecycle section of the automation section of the provisioning wizard. Expiration can be added to any instance even if no policies have been created.

Instance and Host Names
^^^^^^^^^^^^^^^^^^^^^^^

Naming Policies will populate a fixed or editable name for instances, hosts and hostnames. The Name Pattern field uses ${variable} string interpolation.

NAMING TYPE
  User Configurable
    Naming pattern will pre-populate during provisioning but can be edited by the user.
  Fixed Name
    Naming pattern will pre-populate during provisioning and cannot be changed.

NAME PATTERN
  The Name Pattern field uses ``${variable}`` string interpolation.

  Commonly used variables for naming patterns include:

  .. code-block:: bash

    ${groupName}
    ${groupCode}
    ${cloudName}
    ${cloudCode}
    ${type}
    ${accountID}
    ${account}
    ${accountType}
    ${platform}
    ${userID}
    ${userName}
    ${userInitials}
    ${provisionType}
    ${sequence} #results in 1
    ${sequence+100} #results in 101
    ${sequence.toString().padLeft(5,‘0’)} #results in 00001

  .. NOTE:: An Instance Name Policy using a naming pattern with User Initials, Cloud Code, Instance Type, and a sequential number starting at 3000 is ``${userInitials}-${cloudCode}-${type}-${sequence+3000}``, resulting in an Instance Name of **md-vmwd3-centos-3001** for the first instance, followed by **md-vmwd3-centos-3002** and so on.

  Cloud codes and Group codes are fields found in their respective configuration panes.

AUTO RESOLVE CONFLICTS
  |morpheus| will automatically resolve naming conflicts by appending a sequential -number to the name when enabled.

Shutdown Policies
^^^^^^^^^^^^^^^^^

Shutdown policies dictate the number of days an instance is allowed to run before it is shut down. Shutdown is consistent across cloud types i.e.: in VMware, a VM is powered off. In AWS, an instance is stopped. Etc.

Configuration options for shutdown policies:

Shutdown Type
  User Configurable
    Shutdown timeframe is editable during provisioning.
  Fixed Expiration
    User cannot change shutdown timeframe during provisioning.
Expiration Days
  Configures the number of days the instance is allowed to exist before being shut down.
Renewal Days
  If the instance is renewed, this is the number of days by which the shutdown date is increased.
Notification Days
  This allows an email notice to be sent out X days before the instance is set to shut down.
Notification Message
  Customizable message for notification email.
Auto Approve Extensions
  Enable this to auto-approve extension requests, bypassing approval workflows.

Provision Approval
^^^^^^^^^^^^^^^^^^

|morpheus| Provision Approvals enable an approval workflow via internal |morpheus| approval or via ServiceNow workflow. If a ServiceNow integration is present, the ServiceNow option is enabled. The Approval workflow to be selected is dynamically created by querying the ServiceNow Workflow table in the integrated ServiceNow instance.

This ServiceNow approval integration enables users to use the |morpheus| Self-Service provisioning portal to provision new instances and still respect the required ServiceNow business approval workflow.
