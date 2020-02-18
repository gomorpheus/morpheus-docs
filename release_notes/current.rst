.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. important:: |morphver| requires Elasticsearch v7.x. Please refer to :ref:`upgrading` and `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to |morphver| if your Appliance's Elasticsearch is external.

.. important:: v3.6.0 or later required to upgrade to |morphver|. Upgrading from v3.6.x to v4.x contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x, a database backup is recommended due to MySQL version upgrade.

.. important:: It is recommend to upgrade existing VM and Host Agents after upgrading to |morphver| for Automation tasks with large task outputs/results when executing over |morpheus| Agent Command Bus.

New Features
============

Kubernetes
----------

- Kubernetes Amazon EKS
- Kubernetes Azure EKS
- Brownfield Kubernetes Cluster Support

VMware NSX
----------

- NSX Object Permissions
- NSX-V Security Groups
- NSX Object Quota Policies

Security Config
---------------

- NIST Database

ServiceNow
----------

- ServiceNow custom application changes

HashiCorp
---------

- Terraform Provider

Platform support
----------------

- The |morpheus| installer now supports Red Hat Enterprise Linux 8 (RHEL 8): `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/jobs/jobs.html#creating-jobs>`_

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

- Git and Github integrations now utilize HTTPS and do not require SSH
- Git integration now exists for Groovy Script-type Automation Tasks

Cloud Enhancement - SCVMM
-------------------------

- IP addresses for non-managed VMs in SCVMM are now pulled into Morpheus

Cloud Enhancement - Google Cloud Platform (GCP)
-----------------------------------------------

- API Proxy values can now be set under Advanced Options for GCP clouds (when creating new integration or editing an existing one) as is already possible for other clouds: `LINK <https://docs.morpheusdata.com/en/4.2.0/integration_guides/Clouds/google/google.html#advanced-options>`_

AWS Security Enhancement
------------------------

- AWS support security token service AssumeRole

Security Changes
----------------

- New toggle added to `Administration > Settings > APPLIANCE` requiring the agent to validate the presence of an SSL certificate in order to connect the appliance to the instance being managed: `LINK <https://docs.morpheusdata.com/en/4.2.0/administration/settings/settings.html#id1>`_

UI Changes
----------

- Create Clusters wizard (`Infrastructure > Clusters > + ADD CLUSTER`) now allows users to specify the number of worker nodes or the number of hosts for Kubernetes clusters or Docker/KVM clusters, respectively
- Workflows with a visibility value of "Public" are now viewable and executable by Tenants: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/automation/automation.html#add-workflow>`_
- In |morpheus| UI, TAGS have been renamed to LABELS and METADATA has been renamed to TAGS in all places where these fields appear, such as the Instance provisioning wizard, clone wizard, App wizard, Blueprint wizard, and perhaps other places. This change was made to align |morpheus| UI more closely with public cloud terminology. |morpheus| variables and API naming conventions are not affected.
- Approvals (`Operations > Approvals`) can be sorted by DATE CREATED

API Enhancements
================

4.2.0 API Enhancements here

CLI Enhancements
================

.. note:: CLI vXXXXXXXX corresponds to the release of the Morpheus API version XXXXX

4.2.0 CLI Enhancements here

CVEs Addressed
==============

4.2.0 CVEs addressed here

Fixes
=====

- Removed a hard-coded message stating "You have logged out of morpheus." when users who were authenticated through a SAML integration logged out. This could cause confusion when using white-labeled Morpheus appliances.
- Removed a message stating "If supported by your identity provider and configuration, you have also been logged out of your identity provider" that appeared in some instances when logging out of |morpheus| through Identity Source authentication
- Fixed an issue where the HISTORY tab of an ARM Blueprint App detail page would only show deployment information if a VM resource was being deployed
- Creation of networks and routers are now asynchronous processes to improve performance and prevent modal timeout in some scenarios
- Updated |morpheus| installer to force a version of FreeRDP which is compatible with Guacd. CentOS/RHEL 7.7+ include FreeRDP 2.0 by default which is not compatible.
