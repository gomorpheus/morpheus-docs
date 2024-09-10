.. _compatibility:

*******************************************
|morphver| Compatibility & Breaking Changes
*******************************************

When installing and upgrading to |morpheus| |morphver|, refer to the following to ensure compatibility.

Breaking Changes
================

<<<<<<< HEAD
- 6.2.2, 6.0.7 contain embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
- 6.2.2, 6.0.7 Minimum v6.x required to upgrade for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
=======
- 6.3.0: Version 6.3.0 is the first version to require Plugin API 1.0.0+. Small changes will need to be made in order to make plugins created for prior versions of |morpheus| compatible with 6.3.0+. See the `related article in our KnowledgeBase <https://support.morpheusdata.com/s/article/Making-plugins-compatible-with-Morpheus-6-3-0?language=en_US>`_ on the small changes that will need to be made to ensure plugin compatibility
- 6.2.2, 6.0.7 |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
- 6.2.2, 6.0.7 Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
>>>>>>> 9c93d839 (update aurora rds bullet on the breaking changes page)
- 6.2.2, 6.0.7 Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1
- 6.1.1 contains database datatype mondifications on account_invoice and account_invoice_item that may cause long initial ui start up times while the modifications are ran in MySQL for environments with over 100k invoice records when upgrading from any version other than 6.0.3
- 6.1.1 relocates the embedded plugin folder and remove the previous folder. For HA environments using shared storage, rolling upgrades from any version other than 6.0.3 are not advised as the embeeded plugins will not be found on non-upgraded nodes after one node is upgraded.
- 6.1.1: NSX-V networking integration support is removed and no longer supported as of |morpheus| 6.1.1
- 6.0.3 contains database datatype mondifications on account_invoice and account_invoice_item that may cause long initial ui start up times while the modifications are ran in MySQL for environments with over 100k invoice records.
- 6.0.3 relocates the embedded plugin folder and remove the previous folder. For HA environments using shared storage, rolling upgrades are not advised as the embeeded plugins will not be found on non-upgraded nodes after one node is upgraded.
- 6.0.0: NSX-V support is deprecated though still supported as of |morpheus| 6.0.0. It will be removed and unsupported in 6.1.1 and higher.
- 6.0.0+: In |morpheus| 6.0.0+, many third party integrations have been moved out of the core installer package and converted to |morpheus| plugins. As a result, during the upgrade process your appliance will need to be able to access share.morpheusdata.com, the online repository for all |morpheus| plugins. Where this is not possible, users may instead apply the supplemental installer package which is also available at |morpheus| Hub alongside the main installer package.
- 6.0.0+: In |morpheus| 6.0.0+, older service specific system provided Instance Types and Layouts were deprecated and disabled. Updating to 6.0.0 will not affect existing Instances that are associated with the disabled types, however existing catalog item configurations, blueprints and api requests that use disabled Instance Types and layouts will need to be updated.
- 5.5.2: VM Node Packages: Due to build java version requiremnets, the i386.deb and i386.rpm (32-bit) VM Node Packages can no longer be updated, and remain on v3.2.9.
- 5.4.12: Guacd: Guacd is now complied iwth libssh2-1.10.0 on all platforms. Appliances on SLES15 may need openssl-devel manually installed for guacd to succesfully compile.
- 5.4.12: Session Manager: Morpheus features a new session manager that was necessary in order to resolve expiring connections from the agents due to a Spring framework update. This new session manager no longer requires Sticky Sessions and they can now be turned off at the load balancer if so desired. However, keeping them on is totally reasonable as well as it reduces overall system load. Rolling restarts no longer kick you out of your session if sticky sessions are off as it distributes your session data across the morpheus nodes in an HA environment. Additionally, overall system load is reduced as a result of the new session manager.
- 5.4.9: |morpheus| 5.4.9 adds the "Provisioning: State" Role permission. This permission determines access to the State tab for Terraform-backed Instances and is set to "None" by default. On upgrade, only System Admin users will be able to see the State tab for these Instances. For other users who should have this access, edit their Roles to include "Provisioning: State" permissions.
- 5.4.5: Warning: Database indexes added for account_usage and metadata_tag tables. Customers with very large account_usage and/or metadata_tag tables (10 million+) may experience slower initial morpheus-ui loading time after upgrading to 5.4.5, as well as additional database load.
- 5.4.5: 'AVI Load Balancer' renamed to 'NSX Advanced Load Balancer'
- 5.4.5: Cloud Types disabled by default: Dell, HPE (NOT HPE Oneview), Supermicro and Cloud Foundry. Users would still be able to re-enable this clouds in the appliance settings. Does not affect existing Clouds.
- 5.4.5: A10 Load Balancer type has been disabled, and will no longer be an option when adding new Load Balancers. Contact |morpheus| if you need to re-enable A10 Load Balancer option. This does not affect existing Load Balancers.
- 5.4.5: |morpheus| Cluster type "Combo Cluster" renamed to "KVM/Docker Cluster"
- 5.4.5:  Greenfield managed vm's (provisioned with |morpheus|) can no longer be deleted in |morpheus| without removing the actual vm/infrastructure. Restriction does not apply to brownfield vm's that have been converted to managed.
- 5.4.4: The Venafi and AppDynamics integrations are deprecated in v5.4.4 and will be removed in v5.4.5. AppDynamic will return as a plugin at a later date.
- 5.4.4: The morpheus-ui logging configuration file has changed from logback.groovy to logback.xml in v5.4.4 (/opt/morpheus/conf/logback.xml). The logback.groovy file from previous versions can be removed, and any updates to logback.groovy will not result in any logging configuration changes.
- 5.4.3: vCloud Director: Support for integrations with vCD 9 ended
- 5.4.3: |morpheus| Worker/Gateway v5.4.3 packages are now available. Existing Worker & Gateway nodes must be upgraded to v5.4.3 for compatibility with |morpheus| v5.4.3 Appliances.
- 5.4.2: vCloud Director: vCD 9.x will no longer be supported by Morpheus
- 5.4.2: ServiceNow: Instance and Blueprint specific exposures will be removed from ServiceNow plugin support. More advanced configurations of Instances and Blueprints, in addition to Workflows, can be exposed utilizing Catalog Items
- 5.4.2: After upgrading, it is recommended that you manually perform one "Daily" refresh Amazon Clouds to ensure availability of Amazon Service Plans for each region. To manually refresh a Cloud, navigate to Infrastructure > Clouds > (Selected Amazon Cloud) and select "Daily" from the REFRESH dropdown menu. If this is not done, |morpheus| may not show Amazon Service Plans in the provisioning wizard until after Midnight UTC following the upgrade when the next automatic Daily sync would run.
- 5.3.4: Major UI navigation structure changes. Refer to the :ref:`Navigation Updates` reference table
- 5.3.3: Support for OpenStack v2 Identity API is removed
- 5.3.2+: The local code repository path moved from ``/var/opt/morpheus/morpheus-ui/repo`` to ``/var/opt/morpheus/morpheus-local/repo`` to reduce potential shared storage issues and performance restrictions. The reconfigure process creates the folders and sets the paths in application.yml, no manual intervention is needed unless symlinks exisit on ``/var/opt/morpheus/morpheus-ui/repo/git`` which will need to be removed prior to reconfiguring - 5.3.2+ The deprecated ``/var/opt/morpheus/morpheus-ui/repo`` path will be automatically deleted in a future release but can be manually recursively deleted at any time for storage reclamation.
- 5.3.2+: :menuselection:`Provisioning --> Deployments` has been moved to :menuselection:`Provisioning --> Code --> Deployments`
- 5.2.9: OpenStack v2 Identity API is deprecated as of v5.2.9 (and is removed as of v5.3.3)
- 5.2.6, 5.3.1: Appliance & Agent java version updated to ``8u292-b10``. jdk8u292 disables TLS 1.0 and 1.1 by default
- 5.2.3+: ``codeready`` (codeready-builder-for-rhel-8-x86_64-rpms) repo access required for RHEL 8+ Appliances, replacing the previous PowerTools/powertools requirement
- 5.2.1 & 4.2.5: API: Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``. Previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags``
- 5.0.0+: When upgrading to 5.0.0+ from 4.x.x, any bearer tokens that have been generated are deleted which requires users to request new bearer tokens
- 4.2.4: For appliances with externalized MySQL databases, due to MySQL deprecation of the "EDT" timezone you may need to update your database timezone to UTC or another compatible value. If this is not done, you will receive errors referencing timezone and |morpheus| will not start. |morpheus| should handle this change automatically for all-in-one appliances.
- 4.2.1+: Tasks: Python: Virtual environment are now used for Python Tasks. **Note:** ``virtualenv`` is required on all Appliance App nodes
- 4.2.1+: Puppet: |morpheus| integration now supports version 6+. Puppet versions prior to 6 are no longer supported
- 4.2.1+: Clouds: VirtualBox, VirtuSteam, and MetaCloud Cloud Types are no longer supported or available
- 4.2.1+: Appliance: OS: Ubuntu 14.04 has reached its end of life (EOL) and is no longer supported as a Morpheus Appliance Host Operating System. Any |morpheus| Appliance running on 14.04 must be upgraded to 16.04, 18.04, 20.04 or 22.04 BEFORE upgrading to 4.2.1+. Upgrades on 14.04 will not succeed

|morpheus| Application OS
=========================

|morpheus| can be installed on the following platforms. Please note the table below is for |morpheus| Application OS support, not |morpheus| Agent OS Support.

.. include:: /getting_started/requirements/applianceOsTable.rst

Services
========

|morphver| Service Versions & Compatibility
-------------------------------------------

.. list-table:: |morphver| Service Versions & Compatibility
   :widths: auto
   :header-rows: 1

   * - Service
     - Compatible Branch
     - Morpheus Installer Version
     - Updated in |morphver|
   * - Plugin API
     - |pluginVer|
     - |pluginVer|
     -
   * - Morpheus Worker
     - |workerVer|
     -
     -
   * - MySQL
     - |mysqlbranch|
     - |mysqlver|
     -
   * - MySQL (FIPS)
     - |mysqlbranch|
     - |mysqlverfips|
     -
   * - Elasticsearch
     - |esbranch|
     - |esver|
     -
   * - RabbitMQ
     - |rmqbranch|
     - |rmqver|
     -
   * - Tomcat
     -
     - |tcver|
     -
   * - Nginx
     -
     - |nginxver|
     -
   * - OpenSSL
     -
     - |openssl|, |openssl_fips| (FIPS)
     -
   * - Java
     -
     - |java|
<<<<<<< HEAD
     - |checkmark|
=======
     -
>>>>>>> 9c93d839 (update aurora rds bullet on the breaking changes page)
   * - Java (macOS agent)
     -
     - |java-mac|
     -

.. IMPORTANT:: Elasticsearch 8.10.1 was released within days of |morpheus| |morphver|. It's expected to be compatible but has not been tested. Customers managing their own Elasticsearch clusters should be aware that internal testing of the |morpheus| |morphver| was conducted on Elasticsearch 8.9.2 and we cannot recommend deploying a higher version at this time.

|

|morpheus| Agent & Node Package Versions
----------------------------------------

.. list-table:: |morphver| Agent & Node Package Versions
   :widths: auto
   :header-rows: 1

   * - Package
     - Version
     - |morphver| changes from |previousMorphVer|
   * - Morpheus Node and VM Node Packages
     - |nodePackageVer|
     - Updated to v3.2.24
   * - Morpheus Linux Agent
<<<<<<< HEAD
     - |linuxagentver| 
     - Updated to v2.6.2
=======
     - |linuxagentver|
     - Updated to |linuxagentver|
>>>>>>> 9c93d839 (update aurora rds bullet on the breaking changes page)
   * - Morpheus Windows Agent
     - |winagentver|
     - No changes
   * - Morpheus macOS Agent
     - |macagentver|
     - No changes

|

Upgrade Paths & Methods
=======================

The following table shows supported version upgrade paths and methods.

.. include:: /release_notes/upgrade_table2.rst

|

Integrations
============

.. note:: Current iterations of Amazon AWS, Microsoft Azure, Google Cloud Platform, Digital Ocean, OpenTelekom Cloud, IBM Bluemix, Softlayer and UpCloud are all supported.

.. include:: /release_notes/compatibility_table.rst
