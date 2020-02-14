.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. important:: v|morphver| requires Elasticsearch v7.x. Please refer to :ref:`upgrading` and `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to v|morphver| if your Appliance's Elasticsearch is external.

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

- Installer support for RHEL 8

SCVMM
-----

- IP addresses for non-managed VMs in SCVMM are now pulled into Morpheus

Provisioning Jobs
-----------------

- Jobs can now be executed at a single point in time: `LINK <https://docs.morpheusdata.com/en/4.2.0/provisioning/jobs/jobs.html#creating-jobs>`_

.. image:: /images/provisioning/jobs/dateandtime_job.png
  :width: 60%

Cloud Enhancement - SCVMM
-------------------------

- Pull non-Managed VM IPs from SCVMM

AWS Security Enhancement
------------------------

- AWS support security token service AssumeRole

Security Changes
----------------

- New toggle added to `Administration > Settings > APPLIANCE` requiring the agent to validate the presence of an SSL certificate in order to connect the appliance to the instance being managed: `LINK <https://docs.morpheusdata.com/en/4.2.0/administration/settings/settings.html#id1>`_

UI Changes
----------

- Instance Prov Wizard: Tags renamed Labels, Metadata key/value pairs are now Tags. Change made to align Morpheus UI with public cloud terminology.

Other UI Enhancements
---------------------

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
- Fixed an issue where the HISTORY tab of an ARM Blueprint App detail page would only show deployment information if a VM resource was being deployed
- Creation of networks and routers are now asynchronous processes to improve performance and prevent timeout of the modal in some scenarios
