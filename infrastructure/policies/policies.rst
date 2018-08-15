Policies
========

Overview
--------

Policies add governance, ease of use, cost-savings, and auditing features to |morpheus| . Policies can be created in the Policies tabs in Groups and Clouds. Policy generation is a role permission.

Policies apply towards any instance provisioned into a group or cloud with active policies. Cloud policies will override matching or conflicting group policies during provisioning.

Available Policy Types
^^^^^^^^^^^^^^^^^^^^^^

Expiration
  Sets an expiration timeframe in days after which the Instance will be deleted. Extensions can be auto-approved or require approval immediately or after x amount of auto-extensions using Morpheus Approvals or an Approval Integration.
Host Name
  Pre-populates a fixed or editable name for Hosts and Virtual Machines using ${variable} naming patterns and/or text.
Hostname
  Pre-populates a fixed or editable name for hostnames/machine names using ${variable} naming patterns and/or text.
Instance Name
  Pre-populates a fixed or editable name for Instance Names using ${variable} naming patterns and/or text.
Max Containers
  Sets the max number of Containers for the Group or Cloud the Policy is added to.
Max Cores
  Sets the max number of total of Cores combined for Instances in the Group or Cloud the Policy is added to.
Max Hosts
  Sets the max number of total Hosts in the Group or Cloud the Policy is added to.
Max Memory
  Sets the max number of total of RAM combined for Instances in the Group or Cloud the Policy is added to.
Max Storage
  Sets the max number of total of Storage combined for Instances in the Group or Cloud the Policy is added to.
Max VMs
  Sets the max number of Virtual Machines for the Group or Cloud the Policy is added to.
Power Scheduling
  Adds a Power Schedule for the Instances in a Group or Cloud. Power Schedules can be created in ``Operations -> Scheduling``
Provision Approval
  Sets an Approval requirement for Provisioning into a Group or Cloud using Morpheus Approvals or an Approval Integration such a Service Now.
Shutdown
  Sets a shutdown timeframe in days upon provision after which the Instance will be stopped. Extensions can be auto-approved or require approval immediately or after x amount of auto-extensions using Morpheus Approvals or an Approval Integration.
User Creation
  Controls the "CREATE YOUR USER" flag in the User Config options during provisioning do be always disabled, always enabled, enabled by default, or disabled by default.


Creating Policies
-----------------

Policies can be created, edited, and set to active or inactive in the a
group or cloud detail pane under the Policies tab.

To create a Policy for a Cloud:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Resource Limitation Policies apply to all Instances in the Cloud the Policy is added to. Approval, Naming, Power, Shutdown and Expiration Policies apply to Instances created or moved into the Group after the Policy is enabled.

#. Navigate to ``Infrastructure -> Clouds``
#. Select a Cloud by clicking on the name of the Cloud to go to the Cloud Detail page.
#. Select the ``POLICIES`` tab in the Cloud Detail page.
#. Select :guilabel:`+ ADD` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuration options.
#. Select :guilabel:`SAVE CHANGES`

To create a Policy for a Group:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Resource Limitation Policies apply to all Instances in the Group the Policy is added to. Approval, Naming, Power, Shutdown and Expiration Policies apply to Instances created after the Policy is enabled.

#. Navigate to ``Infrastructure -> Clouds``
#. Select a Cloud by clicking on the name of the Cloud to go to the Cloud Detail page.
#. Select the ``POLICIES`` tab in the Cloud Detail page.
#. Select :guilabel:`+ ADD` and choose from the available policy types.
#. Refer to Policy Types sections below for Configuraiton options.
#. Select :guilabel:`SAVE CHANGES`

Policy Types
------------

Expiration Policies
^^^^^^^^^^^^^^^^^^^

Expiration policies set an expiration timeframe for any instance provisioned into the cloud or group the policy is added to. When an instance expires, it is terminated and deleted.

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

NOTE:: Expiration and Shutdown Policies will be enforced on Instances moved into a Group with an Active Policy or Instances created when converting an unmanaged host to managed.

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
    ${accountId}
    ${account}
    ${accountType}
    ${platform}
    ${userId}
    ${userName}
    ${userInitials}
    ${provisionType}
    ${sequence} #results in 1
    ${sequence+100} #results in 101
    ${sequence.toString().padLeft(5,‘0’)} #results in 00001

  An example Instance Name Policy using a naming pattern with User Initials, Cloud Code, Instance Type, and a sequential number starting at 3000 is ``${userInitials}-${cloudCode}-${type}-${sequence+3000}``, resulting in an Instance Name of **md-vmwd3-centos-3001** for the first instance, followed by **md-vmwd3-centos-3002** and so on.

  Cloud codes and Group codes are fields found in their respective configuration panes.

  .. NOTE:: Static text can also be used in conjunction with ${variable}'s, such as ``morpheus${cloudCode}${type}${sequence+3000}``

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

.. NOTE:: Expiration and Shutdown Policies will be enforced on Instances moved into a Group with an Active Policy or Instances created when converting an unmanaged host to managed.

Provision Approval
^^^^^^^^^^^^^^^^^^

|morpheus| Provision Approvals enable an approval workflow via internal |morpheus| approval or via ServiceNow workflow. If a ServiceNow integration is present, the ServiceNow option is enabled. The Approval workflow to be selected is dynamically created by querying the ServiceNow Workflow table in the integrated ServiceNow instance.

This ServiceNow approval integration enables users to use the |morpheus| Self-Service provisioning portal to provision new instances and still respect the required ServiceNow business approval workflow.

Power Schedules
^^^^^^^^^^^^^^^

Power Schedules set daily times to shutdown and startup instances. Power schedule can be created and managed in ``Operations -> Scheduling``.

.. NOTE:: Power Schedule Policies will apply to Instances created in a Group or Cloud after the Policy is enabled, and will not apply to pre-existing Instances.

Configuration options for Power Schedule Policies:

DESCRIPTION
  Add details about your Policy for reference in the Policies tab.
Enabled
  Policies can be edited and disabled or enabled at any time. Disabling a Power Schedule Policy will prevent the Power Schedule from running on the Groups Instances until re-enabled.
ENFORCEMENT TYPE
  * User Configurable: Power Schedule choice is editable by User during provisioning.
  * Fixed Schedule: User cannot change Power Schedule setting during provisioning.
POWER SCHEDULE
  Select Power Schedule to use in the Policy. Power schedule can be added in ``Operations -> Scheduling``
TENANTS
  Leave blank for the Policy to apply to all Tenants, or search for and select Tenants to enforce the Policy on specific Tenants.

Max Resources
^^^^^^^^^^^^^

Max Resource policies allow setting quotas for Clouds and Groups for maximum amount of Memory, Storage, Cores, Hosts, VM's, or Containers that can be created in the Cloud or Group the Policy is assigned to.

Configuration options for Max Resources Policies:

Max Containers
    Sets the max number of Containers for the Group or Cloud the Policy is added to.
Max Cores
    Sets the max number of total of Cores combined for Instances in the Group or Cloud the Policy is added to.
Max Hosts
    Sets the max number of total Hosts in the Group or Cloud the Policy is added to.
Max Memory
    Sets the max number of total of RAM combined for Instances in the Group or Cloud the Policy is added to.
Max Storage
    Sets the max number of total of Storage combined for Instances in the Group or Cloud the Policy is added to.
Max VMs
    Sets the max number of Virtual Machines for the Group or Cloud the Policy is added to.
Tenants
    Leave blank for the Policy to apply to all Tenants, or search for and select Tenants to enforce the Policy on specific Tenants.

User Creation
^^^^^^^^^^^^^

The User Creation policy controls the "CREATE YOUR USER" flag in the User Config options during provisioning do be always disabled, always enabled, enabled by default, or disabled by default.

Configuration options for User Creation Policies:

TYPE
  User Creation
DESCRIPTION
  Description to identify the policy config
Enabled
  Policies enforcement can be disabled or enabled at any time.
ENFORCEMENT TYPE
  * User Configurable: User Creation choice is editable by User during provisioning.
  * Fixed: User cannot change User Creation setting during provisioning.
CREATE USER
  Check to allow or force user creation. Uncheck to disable by default or force no user creation.
TENANTS
  Leave blank for the Policy to apply to all Tenants, or search for and select Tenants to enforce the Policy on specific Tenants.
