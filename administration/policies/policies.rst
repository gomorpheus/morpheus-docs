.. _policies:

Policies
========

Overview
--------

Policies add governance, ease of use, cost-savings, and auditing features to |morpheus|. |morpheus| enables end users to create Policies scoped to Users, Roles, Groups, Clouds, Tenants, Networks, Plans, and Global scoping to give Admins full control and governance over their environments. The available scoping will vary from one Policy type to another. See the section below for information on each Policy type and guides for more complex Policy implementation.

Policy Types
------------

Approve Delete
  Sets an approval requirement for deleting Instances or Apps within the Policy scope. When setting the Policy, users have the option of using Morpheus Approvals or an Approval Integration such a ServiceNow. On delete request, Instances will be shut down and only deleted if approved.
Approve Provision
  Sets an approval requirement for provisioning Instances or Apps within the Policy scope. When setting the Policy, users have the option of using Morpheus Approvals or an Approval Integration such a ServiceNow.
Approve Reconfigure
  Sets an approval requirement for reconfiguring Instances and servers within the Policy scope. When setting the Policy, users have the option of using Morpheus Approvals or an Approval Integration such a ServiceNow.
Approve Workflow Execute
  If enabled, when Workflows are executed on workloads within the Policy scope, an Approval is generated. This could apply when a Workflow is executed from the Workflows list page or from the detail page for an Instance or server. Approvals can be targeted to |morpheus| internal Approvals or targeted to a third-party integration (such as ServiceNow). The Workflow will not begin to execute until after the approval is granted.
Backup Creation
  Disable or enable the ability to create a backup when provisioning an instance.
Backup Targets
  A master account can determine storage provider options for backups with Backup Targets policies.
Budget
  Sets a maximum total combined price for all instances in the Group, Cloud, Tenant or owned by the User this policy is applied to.
Cluster Resource Name
  The name of Cluster hosts (master and workers) when creating Kubernetes, Docker and KVM Clusters. Pre-populates a fixed or editable Resource Name value for the cluster using ${variable} naming patterns and/or text, including ${sequence} numbering. Toggle whether sequence numbers are reusable (after the resource using them is destroyed) by enabling `Reuse Naming Sequence Numbers <https://docs.morpheusdata.com/en/latest/administration/settings/settings.html#provisioning>`_ in |AdmSet|
Cypher Access
  Granularly set LIST, READ, WRITE, and DELETE access to arbitrary Cypher secret paths scoped globally or to specific Roles and Users. See the section below for a guide to establishing a Cypher access policy.
Delayed Delete
  Delayed Delete Policies allow for soft deletion of Instances and Apps. Instead of deleting immediately, Instances and Apps with a Delayed Delete policy applied will be shutdown upon deletion request and hidden by default from the UI. The Instance/App will then be in ``Pending Removal`` status. In order to see Instances pending deletion on the Instances list page (|ProIns|), you must filter for "Pending Removal" status. These Instances will not show when filtered for "All Statuses"
Expiration
  Sets an expiration timeframe in days after which the Instance will be deleted. Extensions can be auto-approved or require approval immediately or after x amount of auto-extensions using Morpheus Approvals or an Approval Integration. See |morpheus| `Knowledge Base <https://support.morpheusdata.com/s/article/How-to-create-an-extensions>`_ for more information about Expiration policies
File Share Storage Quota
  Sets a Storage Quota for File Share usage (in GB) to scoped User, Role, Tenant or Global.
Hostname
  The ``hostname`` or ``computer name`` which is set in the OS and DNS. On some platforms, hostnames are restricted by length, spaces, and/or special characters. Pre-populates a fixed or editable name for hostnames/machine names using ${variable} naming patterns and/or text, including ${sequence} numbering. Toggle whether sequence numbers are reusable (after the resource using them is destroyed) by enabling `Reuse Naming Sequence Numbers <https://docs.morpheusdata.com/en/latest/administration/settings/settings.html#provisioning>`_ in |AdmSet|
Instance Name
  Pre-populates a fixed or editable name for Instance Names using ${variable} naming patterns and/or text, including ${sequence} numbering. Toggle whether sequence numbers are reusable (after the resource using them is destroyed) by enabling `Reuse Naming Sequence Numbers <https://docs.morpheusdata.com/en/latest/administration/settings/settings.html#provisioning>`_ in |AdmSet|. Note that it's not recommended administrators include ">", "<", "%", "$", or "=" in naming policies
Max Containers
  Sets the max number of Containers for the Group or Cloud the Policy is added to.
Max Cores
  Sets the max number of total of Cores combined for Instances in the Group or Cloud the Policy is added to, includes the option to include or exclude container resources in the Policy.
Max Hosts
  Sets the max number of total Hosts in the Group or Cloud the Policy is added to.
Max Load Balancer Pools
  Sets the max number of load balancer pools within the policy scope
Max Memory
  Sets the max number of total of RAM combined for Instances in the Group or Cloud the Policy is added to, includes the option to include or exclude container resources in the Policy.
Max Pool Members
  Sets the maximum number of members in a load balancer pool
Max Snapshots
  Set the maximum number of Snapshots that may be stored for each Instance or VM within the scope. Once the limit is met, |morpheus| will warn the user when attempting to create more snapshots until the number is reduced
Max Storage
  Sets the max number of total of Storage combined for Instances in the Group or Cloud the Policy is added to, includes the option to include or exclude container resources in the Policy.
Max Virtual Servers
  Sets the maximum number of virtual servers within the policy scope
Max VMs
  Sets the max number of Virtual Machines for the Group or Cloud the Policy is added to.
Message of the Day (MOTD)
  Message of the Day"" Policy for displaying Alerts in |morpheus|. Configurable as a pop-up or full-page notification with Info, Warning and Critical message types.

  .. note:: Requires role permission: ``Admin: Message Of the Day`` set to "Full" to create and manage MOTD Policies.

Network Quota
  Limits the number of networks that can be created within the policy's scope
Object Storage Quota
  Sets a Storage Quota for Object Storage usage (in GB) to scoped User, Role, Tenant or Global.
Power Scheduling
  Adds a Power Schedule for the Instances in a Group or Cloud. Power Schedules can be created in |LibAutPow|
Router Quota
  Limits the number of routers that can be created within the policy's scope
Shutdown
  Sets a shutdown timeframe in days upon provision after which the Instance will be stopped. Extensions can be auto-approved or require approval immediately or after x amount of auto-extensions using Morpheus Approvals or an Approval Integration.
Storage Server Storage Quota
  Sets a Storage Quota for selected Storage Server (in GB), applied Globally or per specified Tenants.
Tags
  Requires the user to add compliant Tags at provision time, this can be enforced on a strict or passive basis

  .. note:: Tag scanning and enforcement is currently only available for Azure, Amazon, Google, and VMware clouds. For a more comprehensive guide on implementing Tag Policies, see the associated article in our `KnowledgeBase <https://support.morpheusdata.com/s/article/How-to-work-with-cloud-tagging-policies?language=en_US>`_.

User Creation
  Controls the "CREATE YOUR USER" flag in the User Config options during provisioning do be always disabled, always enabled, enabled by default, or disabled by default.
User Group Creation
  Forces User Creation of members in the selected User Group during Provisioning.
Workflow
  Forces execution of selected Workflow for Instance Provisioning.


Creating Policies
-----------------

Policies can be created in three different locations.

* |AdmPol|
* ``Infrastructure > Groups > Group > Policies``
* ``Infrastructure > Clouds > Cloud > Policies``

Policies can be disabled and re-enabled at anytime.

.. IMPORTANT:: Precedence is applied to matching or conflicting Policies in the following order: Cloud > Group > Role > User > Global.

To create a Global Policy:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmPol|
#. Select :guilabel:`+ ADD Policy` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuration options.
#. Under Filter next to scope select :guilabel:`Global`
#. Select :guilabel:`SAVE CHANGES`


To create a Policy for a User:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmPol|
#. Select :guilabel:`+ ADD Policy` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuration options.
#. Under filter next to scope select :guilabel:`User` a drop down menu will appear below allowing you to select a user
#. Select :guilabel:`SAVE CHANGES`

To create a Policy for a Role:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmPol|
#. Select :guilabel:`+ ADD Policy` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuration options.
#. Under filter next to scope select :guilabel:`Role` a drop down menu will appear below allowing you to select a Role
#. For ``APPLY INDIVIDUALLY TO EACH USER IN ROLE``
    - Select for Max Resource/Quota Policies to be calculated per user
    - Leave unselected to calculate by total usage of all users within that Role.
#. Select :guilabel:`SAVE CHANGES`

To create a Policy for a Cloud:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Resource Limitation Policies apply to all Instances in the Cloud the Policy is added to. Approval, Naming, Power, Shutdown and Expiration Policies apply to Instances created or moved into the Group after the Policy is enabled.

#. Navigate to ``Infrastructure > Clouds``
#. Select a Cloud by clicking on the name of the Cloud to go to the Cloud Detail page.
#. Select the ``POLICIES`` tab in the Cloud Detail page.
#. Select :guilabel:`+ ADD` and choose from the available policy types.
#. Refer to Policy Type sections below for Configuration options.
#. Select :guilabel:`SAVE CHANGES`

To create a Policy for a Group:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Resource Limitation Policies apply to all Instances in the Group the Policy is added to. Approval, Naming, Power, Shutdown and Expiration Policies apply to Instances created after the Policy is enabled.

#. Navigate to ``Infrastructure > Groups``
#. Select a Group by clicking on the name of the Group to go to the Group Detail page.
#. Select the ``POLICIES`` tab in the Group Detail page.
#. Select :guilabel:`+ ADD` and choose from the available policy types.
#. Refer to Policy Types sections below for Configuration options.
#. Select :guilabel:`SAVE CHANGES`

Policy Types
------------

.. include:: cypherpolicies.rst

Expiration Policies
^^^^^^^^^^^^^^^^^^^

Expiration policies set an expiration timeframe for any instance provisioned into the cloud, role, group or by the user the policy is added to. When an instance expires, it is terminated and deleted.

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
  Customizable message for notification emails. The default message is ``Instance ${instance?.name} is set to expire on ${instance?.expireDate}``
Auto Approve Extensions
  Enable this to auto-approve extension requests, bypassing approval workflows.

Instances with expirations show the time until expiration in the instance detail pane. Instances with active expiration policies can be extended by selecting the EXTEND NOW button in the instance detail pane. The extension length is set in the policy by the RENEWAL DAYS field.

Expirations can also be added to any instance during provisioning by entering the number of days in the EXPIRATION DAYS field in the Lifecycle section of the automation section of the provisioning wizard. Expiration can be added to any instance even if no policies have been created.

.. NOTE:: Expiration and Shutdown Policies will be enforced on Instances created when converting a discovered host to managed.

Instance and Host Names
^^^^^^^^^^^^^^^^^^^^^^^

Naming Policies will populate a fixed or editable name for instances, hosts and hostnames. The Name Pattern field uses ${variable} string interpolation.

NAMING TYPE
  User Configurable
    Naming pattern will pre-populate during provisioning but can be edited by the user.
  Fixed Name
    Naming pattern will pre-populate during provisioning and cannot be changed.

NAME PATTERN
  The Name Pattern field uses Static text and/or ``${variable}`` string interpolation, such as ``morpheus${cloudCode}${type}${sequence+3000}``

  An example Instance Name Policy using a naming pattern with User Initials, Cloud Code, Instance Type, and a sequential number starting at 3000 is ``${userInitials}-${cloudCode}-${type}-${sequence+3000}``, resulting in an Instance Name of **md-vmwd3-centos-3001** for the first instance, followed by **md-vmwd3-centos-3002** and so on.

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
    ${platform == 'windows' ? 'w':'l'} # results in `w` for Windows platforms and `l` for Linux Platforms
    ${userId}
    ${username}
    ${userInitials}
    ${provisionType}
    ${instance.instanceContext} # Environment Code
    ${sequence} # results in 1
    ${sequence+100} # results in 101
    ${sequence.toString().padLeft(5,'0')} #results in 00001

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

.. NOTE:: Expiration and Shutdown Policies will be enforced on Instances created when converting a discovered host to managed.

Provision Approval
^^^^^^^^^^^^^^^^^^

|morpheus| Provision Approvals enable an approval workflow via internal |morpheus| approval or via ServiceNow workflow. If a ServiceNow integration is present, the ServiceNow option is enabled. The Approval workflow to be selected is dynamically created by querying the ServiceNow Workflow table in the integrated ServiceNow instance.

This ServiceNow approval integration enables users to use the |morpheus| Self-Service provisioning portal to provision new instances and still respect the required ServiceNow business approval workflow.

Power Schedules
^^^^^^^^^^^^^^^

Power Schedules set daily times to shutdown and startup instances. Power schedule can be created and managed in |LibAutPow|

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
  Select Power Schedule to use in the Policy. Power schedule can be added in |LibAutPow|
TENANTS
  Leave blank for the Policy to apply to all Tenants, or search for and select Tenants to enforce the Policy on specific Tenants.

Max Resources
^^^^^^^^^^^^^

Max Resource policies allow setting quotas for Clouds, Groups, Roles or Users for maximum amount of Memory, Storage, Cores, Hosts, VM's, or Containers that can be created in the Cloud, Group, Role or by the User the Policy is assigned to.

Configuration options for Max Resources Policies:

Max Containers
    Sets the maximum combined total of Containers in Instances per Policy Scope.
Max Cores
    Sets the maximum combined total of Cores in Instances per Policy Scope.
Max Hosts
    Sets the maximum total of Hosts per Policy Scope.
Max Memory
    Sets the maximum combined total of RAM (capacity) for Instances per Policy Scope.
Max Storage
    Sets the maximum combined total of Storage (capacity) for Instances per Policy Scope.
Max VMs
    Sets the maximum total of managed Virtual Machines per Policy Scope.
TENANTS
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
