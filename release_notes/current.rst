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

Kubernetes Amazon EKS
Kubernetes Azure EKS
Brownfield Kubernetes Cluster Support

VMware NSX
----------

NSX Object Permissions
NSX-V Security Groups
NSX Object Quota Policies

Security Config
---------------

NIST Database

ServiceNow
----------

ServiceNow custom application changes

HashiCorp
---------

Terraform Provider

Platform support
----------------

Installer support for RHEL 8

Provisioning Jobs
-----------------

Jobs can now be executed at a single point in time

Cloud Enhancement - SCVMM
-------------------------

Pull non-Managed VM IPs from SCVMM

AWS Security Enhancement
------------------------

AWS support security token service AssumeRole

UI Changes
----------

Instance Prov Wizard: Tags renamed Labels, Metadata key/value pairs are now Tags. Change made to align Morpheus UI with public cloud terminology.

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

4.2.0 Fixes here
