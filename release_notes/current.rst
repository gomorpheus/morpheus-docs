.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. important:: |morphver| requires Elasticsearch v7.x. Please refer to :ref:`upgrading` and `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to |morphver| if your Appliance's Elasticsearch is external.

.. important:: v3.6.0 or later required to upgrade to |morphver|. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x, a database backup is recommended due to MySQL version upgrade.

.. important:: It is recommend to upgrade existing VM and Host Agents after upgrading to |morphver| for Automation tasks with large task outputs/results when executing over |morpheus| Agent Command Bus.

New Features
============

Tag Enforcement and Compliance Policy
-------------------------------------
New Tag Policy Type with enforcement and compliance scanning added.
 - A Tag policy can be enforced both actively (at provision time) as well as Passively on supported clouds.
 - A Tag policy defines the relevant key to validate the presence of as well as an optional option list to validate valid values.
 - Multiple tag policies can be combined to get an overall view of tag compliance.
 - Servers detail pages show warnings if tags are not compliant.
 - Strict will block provisioning of an instance without the valid tags. These valid tags can be manually entered in tags field set or as part of an export as tag Option Type.

.. note:: Tag Policy scanning and enforcement is only currently functional for three cloud types. Azure, Amazon, and VMware.

.. image:: /images/administration/settings/policies/tagPolicy.jpeg


.. image:: /images/administration/settings/policies/tagComplianceWarning.jpeg


﻿Annotation on 2020-02-19 at 01-47-49.png

Kubernetes
----------

- Kubernetes Azure AKS
- Brownfield Kubernetes Cluster Support, create a new Cluster (Infrastructure > Clusters) with "External Kubernetes Cluster" type to bring an existing Kubernetes cluster into Morpheus: `LINK <https://support.morpheusdata.com/s/article/How-to-add-existing?language=en_US>`_
- Reconfigure Action now available for Kubernetes Instances.

VMware NSX
----------

- NSX Object Permissions
- NSX-V Security Groups
- NSX Object Quota Policies

Security Config
---------------

- NIST Database
- Cloud-Init: Added support for hashing change passwords in target cloud-init data for any non-Ubuntu 14 based image (Ubuntu 14.04 restriction). Note: Dependent on Virtual Image OS type and version settings; ensure OS Type is accurately set.

ServiceNow
----------

- ServiceNow custom application changes


PXE Boot Menu section updates
-----------------------------

The PXE Boot Menu section in /infrastructure/boot#!boot-menus has been updated for Boot Menu creation and management, the ability to set Root and Sub Menus, and configure image and answer file scoping.

- Boot Menu Creation with
  - Enabled flag
  - Default Menu flag
  - Root Menu Flag
  - Boot Image scoping (optional)
  - Answer File scoping (optional)
  - Menu Content field
  - Sub Menu(s) selection
- Ability to edit user created Boot Menus
- System seeded Boot Menus are now displayed

Platform support
----------------

- The |morpheus| installer now supports Red Hat Enterprise Linux 8 (RHEL 8): `LINK <https://docs.morpheusdata.com/en/4.2.0/release_notes/compatibility.html>`_

Morpheus Catalog Enhancements
-----------------------------

- Ubuntu 18 catalog images have been added for the following clouds: Upcloud, Azure, DigitalOcean, IBM, Oracle Cloud, Open Telekom, SoftLayer, vCD, SCVMM, Alibaba, Hyper-V, ESXi

Provisioning Jobs
-----------------

- Jobs can now be executed at a single point in time: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/jobs/jobs.html#creating-jobs>`_

.. image:: /images/provisioning/jobs/dateandtime_job.png
  :width: 60%

Git/Github Integration
----------------------

- Git and Github integrations now have the option to utilize HTTPS and do not require SSH
- Git integration now exists for Groovy Script-type Automation Tasks

SCVMM: Discovered VM IP Address Sync
 SCVMM Cloud Discovery now syncs in IP addresses for Discover VM's.
  - Inventory Existing setting must be enabled on SCVMM Cloud config.

Cloud Enhancement - Google Cloud Platform (GCP)
-----------------------------------------------

- API Proxy values can now be set under Advanced Options for GCP clouds (when creating new integration or editing an existing one) as is already possible for other clouds: `LINK <https://docs.morpheusdata.com/en/4.2.0/integration_guides/Clouds/google/google.html#advanced-options>`_

AWS Security Enhancement
------------------------

- Now supports security token service to AssumeRole by entering AWS role ARN value when editing or integrating new Amazon cloud

.. image:: /images/integration_guides/clouds/aws_role_arn.png
  :width: 60%

Security Changes
----------------

- New toggle added to `Administration > Settings > APPLIANCE` requiring the agent to validate the presence of an SSL certificate in order to connect the appliance to the instance being managed: `LINK <https://docs.morpheusdata.com/en/4.2.0/administration/settings/settings.html#id1>`_

UI Changes
----------

- Create Cluster wizard (`Infrastructure > Clusters > + ADD CLUSTER`) now allows users to specify the number of worker nodes or the number of hosts for Kubernetes clusters or Docker/KVM clusters, respectively

  .. image:: /images/infrastructure/clusters/workers_cluster_wizard.png
    :width: 60%

- Workflows with a visibility value of "Public" are now viewable and executable by Tenants: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/automation/automation.html#add-workflow>`_

TAGS have been renamed to LABELS and METADATA has been renamed to TAGS
  In |morpheus| UI, TAGS have been renamed to LABELS and METADATA has been renamed to TAGS in all places where these fields appear, such as the Instance provisioning wizard, clone wizard, App wizard, Blueprint wizard, and perhaps other places. This change was made to align |morpheus| UI more closely with public cloud terminology.

  .. note:: |morpheus| variables and API naming conventions have not been changed.

Approvals (`Operations > Approvals`) can be sorted by DATE CREATED

Recent Activity Report now displays Impersonated User info.
  The Recent Activity Report in /operations/activity now shows "User as Impersonated User" for activity records from an Impersonated User. Impersonations were previously shown in the Dashboard Activity section, as well as the Audit Log and UI Logs, and now shown in the Recent Activity Report too.
CloudFormation: Improved conditional resource handling
  When Conditional Resources fail to create when provisioning CloudFormation Instances or Apps, the resources are removed instead of remaining in Morpheus as Failed.
vCloud Director: API Version Specification
  The API Version can now be specified in vCloud Director Cloud configurations.
   - API VERSION field added to vCD Cloud configs
   - To override system API version, enter version in API VERSION field
     - example API verison value: ``31.0``

VMware: Tag Enhancements
  Post-Provision Tag additions, updates, and/or removals in Morpheus on VMware Instances are now synced into VMware
Azure: Tag Enhancements
  Post-Provision Tag additions, updates, and/or removals in Morpheus on Azure Instances are now synced into Azure
IBM Cloud: Frankfurt 4 & 5 Datacenters now supported
 Frankfurt 4 & 5 Datacenters are now available for IBM Clouds.
Softlayer: Frankfurt 4 & 5 Datacenters now supported
 Frankfurt 4 & 5 Datacenters are now available for Softlayer Clouds.
Policies: Network Quotas
 Network Quota Policies limit the number of Networks that can be created within the Policy's scope.
  - Once the Quote limit is reached, Users will not be able to create additional Networks within the applicable Policy Enforcement scope.
  - Scopes include:

    - Global
    - Tenant
    - Group
    - Cloud
    - Role
    - User

Policies: Router Quotas
 Router Quota Policies limit the number of Router that can be created within the Policy's scope.
  - Once the Quote limit is reached, Users will not be able to create additional Routers within the applicable Policy Enforcement scope.
  - Scopes include:

    - Global
    - Tenant
    - Group
    - Cloud
    - Role
    - User

API Enhancements
================

4.2.0 API Enhancements here

CLI Enhancements
================

.. note:: CLI vXXXXXXXX corresponds to the release of the Morpheus API version XXXXX

4.2.0 CLI Enhancements here

Fixes
=====

- Removed a hard-coded message stating "You have logged out of morpheus." when users who were authenticated through a SAML integration logged out. This could cause confusion when using white-labeled Morpheus appliances.
- Removed a message stating "If supported by your identity provider and configuration, you have also been logged out of your identity provider" that appeared in some instances when logging out of |morpheus| through Identity Source authentication
- Fixed an issue where the HISTORY tab of an ARM Blueprint App detail page would only show deployment information if a VM resource was being deployed
- Creation of networks and routers are now asynchronous processes to improve performance and prevent modal timeout in some scenarios
- Updated |morpheus| installer to force a version of FreeRDP which is compatible with Guacd. CentOS/RHEL 7.7+ include FreeRDP 2.0 by default which is not compatible.
- The Activity page (Operations > Activity) now identifies actions taken by impersonated Users in the same way they are on the Dashboard (Operations > Dashboard), for example, "Author: User1 as User2"
- Fixed an issue where the reconfigure function did not work properly on Instances provisioned to a kubernetes host in some cases
- Fixed an issue preventing a second router from being added to a |morpheus|-created Openstack network in certain scenarios

CVEs Addressed
==============

4.2.0 CVEs addressed here
