.. _compatibility:

*******************************************
|morphver| Compatibility & Breaking Changes
*******************************************

When installing and upgrading to |morpheus| |morphver|, refer to the following to ensure compatibility.

Breaking Changes
================

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

.. note:: If CentOS 8.2 is pinned to 8.2.2004 vault, the PowerTools repository will need to be pinned to 8.2.2004 to access freerdp-libs 2.0.0

.. include:: /getting_started/requirements/applianceOsTable.rst

Services
========

|morphver| Service Version Changes
----------------------------------

:Appliance: - Java: Updated jdk to v11.0.15+10
:Agent Packages: - Agent Node & VM Node Packages: Java: Updated jdk to v11.0.15+10

|

|morphver| Service Version Compatibility
----------------------------------------

When externalizing MySQL, Elasticsearch and/or RabbitMQ services, the following versions are compatible with version |morpheus| |morphver|

+---------------------------------------+-----------------------+-------------------------------------+
| **Service**                           | **Compatible Branch** | **Morpheus Installer Version**      |
+---------------------------------------+-----------------------+-------------------------------------+
| MySQL                                 | |mysqlbranch|         | |mysqlver|                          |
+---------------------------------------+-----------------------+-------------------------------------+
| MySQL (FIPS)                          | |mysqlbranch|         | |mysqlverfips|                      |
+---------------------------------------+-----------------------+-------------------------------------+
| Percona                               | 5.7, WSREP 31         | n/a                                 |
+---------------------------------------+-----------------------+-------------------------------------+
| Elasticsearch                         | |esbranch|            | |esver|                             |
+---------------------------------------+-----------------------+-------------------------------------+
| RabbitMQ                              | |rmqbranch|           | |rmqver|                            |
+---------------------------------------+-----------------------+-------------------------------------+
| Tomcat                                |                       | |tcver|                             |
+---------------------------------------+-----------------------+-------------------------------------+
| Nginx                                 |                       | |nginxver|                          |
+---------------------------------------+-----------------------+-------------------------------------+
| OpenSSL                               |                       | |openssl|, |openssl_fips| (FIPS)    |
+---------------------------------------+-----------------------+-------------------------------------+
| Java                                  |                       | |java|                              |
+---------------------------------------+-----------------------+-------------------------------------+
| Java (macOS agent)                    |                       | |java-mac|                          |
+---------------------------------------+-----------------------+-------------------------------------+

|

|morpheus| Agent & Node Package Versions
----------------------------------------

.. list-table:: |morphver| Agent & Node Package Versions
   :widths: auto
   :header-rows: 1

   * - Package
     - Version
     - |morphver| Changes
   * - Morpheus Node and VM Node Packages
     - |nodePackageVer|
     - Node & VM Node Packages: Java: Updated jdk to v11.0.15+10
   * - Morpheus Linux Agent
     - |linuxagentver|
     - No changes
   * - Morpheus Windows Agent
     - |winagentver|
     - No changes
   * - Morpheus macOS Agent
     - |macagentver|
     - No changes

|

Security
========

CVEs Addressed
--------------

No CVEs mitigated since |previousMorphVer|
|

Security Advisories
-------------------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Advisory ID
    - Severity
    - Description
    - Updated On
  * - `MOR20220611-01 <https://docs.morpheusdata.com/en/advisory-page/security/mor22060801.html>`_
    - |advSevHigh|
    - An XXE issue was discovered in |morpheus| through 5.2.16 and 5.4.x through 5.4.4
    - 06-08-2022

Upgrade Paths & Methods
=======================

The following table shows supported version upgrade paths and methods.

.. include:: /release_notes/upgrade_table.rst

|

Integrations
============

.. note:: Current iterations of Amazon AWS, Microsoft Azure, Google Cloud Platform, Digital Ocean, HPE OneView, OpenTelekom Cloud, IBM Bluemix, Softlayer and UpCloud are all supported.

.. include:: /release_notes/compatibility_table.rst
