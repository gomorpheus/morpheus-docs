.. _compatibility:

*******************************************
|morphver| Compatibility & Breaking Changes
*******************************************

When installing and upgrading to |morpheus| |morphver|, refer to the following to ensure compatibility.

Breaking Changes
================

- 9.0.0: |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and VM node packages from the package-repo when appliance free space is needed.
- 9.0.0: Plugin API updated to 1.4.1. Plugins built against older Plugin API versions may need to be recompiled for compatibility.
- 9.0.0: HVM Cluster Layout 1.3 replaces Pacemaker with the |morpheus| Agent as the HA control plane for HPE Clustered Datastores. Existing 1.2 clusters can be upgraded via a one-click process (Infrastructure > Clusters > host > Actions > Update > HVM Cluster 1.3 Upgrade).
- 7.0.8, 8.0.0: On first ui startup after upgrade, |morpheus| will normalize all IPv6 records within |morpheus|-type pools. There will be a warning in appliance logs warning how many records will be normalized. This takes between 5-15 minutes per 1m records
- 7.0.8, 8.0.0: Updated the AccountUsage table in the appliance database to accept LONGTEXT data type to prevent data from oversetting the table in specific scenarios. Note that this schema change will take time for databases with large numbers of account usage records
- 6.3.0: Version 6.3.0 is the first version to require Plugin API 1.0.0+. Small changes will need to be made in order to make plugins created for prior versions of |morpheus| compatible with 6.3.0+. See the `related article in our KnowledgeBase <https://support.morpheusdata.com/s/article/Making-plugins-compatible-with-Morpheus-6-3-0?language=en_US>`_ on the small changes that will need to be made to ensure plugin compatibility
- 6.2.2, 6.0.7 |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
- 6.2.2, 6.0.7 Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
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
- 5.4.5: A10 Load Balancer type has been disabled, and will no longer be an option when adding new Load Balancers. This does not affect existing Load Balancers.
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
- 4.2.1+: Appliance: OS: Ubuntu 14.04 has reached its end of life (EOL) and is no longer supported as a Morpheus Appliance Host Operating System. Any |morpheus| Appliance running on 14.04 must be upgraded to 16.04, 18.04, 20.04, 22.04 or 24.04 BEFORE upgrading to 4.2.1+. Upgrades on 14.04 will not succeed

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
     - |checkmark|
   * - Morpheus Worker
     - |workerVer|
     -
     -
   * - MySQL
     - |mysqlbranch|
     - |mysqlver|
     - |checkmark|
   * - MySQL (FIPS)
     - |mysqlbranch|
     - |mysqlverfips|
     -
   * - OpenSearch
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
     - |checkmark|
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
     -
   * - Java (macOS agent)
     -
     - |java-mac|
     -


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
     - Updated to |nodePackageVer|
   * - Morpheus Linux Agent
     - |linuxagentver|
     - Updated to |linuxagentver|
   * - Morpheus Windows Agent
     - |winagentver|
     - No changes
   * - Morpheus macOS Agent
     - |macagentver|
     - No changes

|

Component Version Matrix
========================

The following table shows the supported component versions for |morpheus| |morphver|.

.. list-table::
   :widths: 30 25 45
   :header-rows: 1

   * - Component
     - Version
     - Notes
   * - |morpheus| Manager
     - |morphver|
     - Application server, API, and UI
   * - Plugin API
     - |pluginVer|
     - Required for plugin compatibility. Plugins built against older API versions may need recompilation.
   * - Linux Agent
     - |linuxagentver|
     - Backward compatible within Major version (9.x)
   * - Windows Agent
     - |winagentver|
     - Backward compatible within Major version (9.x)
   * - macOS Agent
     - |macagentver|
     - Backward compatible within Major version (9.x)
   * - Node Packages
     - |nodePackageVer|
     - VM and host provisioning packages
   * - HVM OS 24.04
     - Ubuntu 24.04 LTS based
     - Standard HVM host OS for cluster layout 1.3
   * - HVM OS 26.04
     - Ubuntu 26.04 LTS based
     - Required for confidential compute. Introduced in 9.1.0.
   * - HPE Alletra Block Storage Plugin
     - 1.14.x
     - Requires Plugin API 1.4.1+, minimum Manager version 9.0.2
   * - Embedded MySQL
     - 8.4.x LTS
     - Embedded database (or external 8.4.x+)
   * - Embedded OpenSearch
     - 2.x
     - Log indexing and search engine
   * - Embedded RabbitMQ
     - 3.12.x
     - Message queue for internal communication

Manager ↔ HVM OS Compatibility
-------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Manager Version
     - HVM OS 24.04
     - HVM OS 26.04
     - Cluster Layout
   * - 9.0.x
     - Supported
     - Not available
     - 1.2 and 1.3
   * - 9.1.x
     - Supported
     - Supported
     - 1.3
   * - 9.2.x (projected)
     - Supported
     - Supported
     - 1.3

Manager ↔ Agent Compatibility
-------------------------------

The |morpheus| Agent is backward compatible within the same Major version. Agents from any 9.x release will function with any 9.x Manager. Upgrading agents is recommended but not required for patch releases.

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Manager Version
     - Minimum Agent Version
     - Recommended Agent Version
   * - 9.0.x
     - 3.0.0
     - 3.1.0
   * - 9.1.x
     - 3.0.0
     - 3.3.0

For complete release lifecycle and support policy information, see :doc:`lifecycle`.

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
