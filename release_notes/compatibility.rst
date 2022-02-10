.. _compatibility:

*******************************************
|morphver| Compatibility & Breaking Changes
*******************************************

When installing and upgrading to |morpheus| |morphver|, refer to the following to ensure compatibility.

Breaking Changes
================

- 4.2.1+: Appliance: OS: Ubuntu 14.04 has reached its end of life (EOL) and is no longer supported as a Morpheus Appliance Host Operating System. Any |morpheus| Appliance running on 14.04 must be upgraded to 16.04, 18.04 or 20.04 BEFORE upgrading to 4.2.1+. Upgrades on 14.04 will not succeed
- 4.2.1+: Clouds: VirtualBox, VirtuSteam, and MetaCloud Cloud Types are no longer supported or available
- 4.2.1+: Puppet: |morpheus| integration now supports version 6+. Puppet versions prior to 6 are no longer supported
- 4.2.1+: Tasks: Python: Virtual environment are now used for Python Tasks. **Note:** ``virtualenv`` is required on all Appliance App nodes
- 4.2.4: For appliances with externalized MySQL databases, due to MySQL deprecation of the "EDT" timezone you may need to update your database timezone to UTC or another compatible value. If this is not done, you will receive errors referencing timezone and |morpheus| will not start. |morpheus| should handle this change automatically for all-in-one appliances.
- 5.0.0+: When upgrading to 5.0.0+ from 4.x.x, any bearer tokens that have been generated are deleted which requires users to request new bearer tokens
- 5.2.1 & 4.2.5: API: Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``. Previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags``
- 5.2.3+: ``codeready`` (codeready-builder-for-rhel-8-x86_64-rpms) repo access required for RHEL 8+ Appliances, replacing the previous PowerTools/powertools requirement
- 5.2.6, 5.3.1: Appliance & Agent java version updated to ``8u292-b10``. jdk8u292 disables TLS 1.0 and 1.1 by default
- 5.2.9: OpenStack v2 Identity API is deprecated as of v5.2.9 (and is removed as of v5.3.3)
- 5.3.2+: :menuselection:`Provisioning --> Deployments` has been moved to :menuselection:`Provisioning --> Code --> Deployments`
- 5.3.2+: The local code repository path moved from ``/var/opt/morpheus/morpheus-ui/repo`` to ``/var/opt/morpheus/morpheus-local/repo`` to reduce potential shared storage issues and performance restrictions. The reconfigure process creates the folders and sets the paths in application.yml, no manual intervention is needed unless symlinks exisit on ``/var/opt/morpheus/morpheus-ui/repo/git`` which will need to be removed prior to reconfiguring 5.3.2. The old ``/var/opt/morpheus/morpheus-ui/repo`` path will be automatically deleted in a fulture release but can be manually recursively deleted at any time for storage reclamation.
- 5.3.3: Support for OpenStack v2 Identity API is removed
- 5.3.4: Major UI navigation structure changes. Refer to the :ref:`Navigation Updates` reference table
- 5.4.2: ServiceNow: Instance and Blueprint specific exposures will be removed from ServiceNow plugin support. More advanced configurations of Instances and Blueprints, in addition to Workflows, can be exposed utilizing Catalog Items
- 5.4.2: vCloud Director: vCD 9.x will no longer be supported by Morpheus
- 5.4.2: After upgrading, it is recommended that you manually perform one "Daily" refresh Amazon Clouds to ensure availability of Amazon Service Plans for each region. To manually refresh a Cloud, navigate to Infrastructure > Clouds > (Selected Amazon Cloud) and select "Daily" from the REFRESH dropdown menu. If this is not done, |morpheus| may not show Amazon Service Plans in the provisioning wizard until after Midnight UTC following the upgrade when the next automatic Daily sync would run.
- 5.4.3: |morpheus| Worker/Gateway v5.4.3 packages are now available. Existing Worker & Gateway nodes must be upgraded to v5.4.3 for compatibility with |morpheus| v5.4.3 Appliances.
- 5.4.3: vCloud Director: Support for integrations with vCD 9 ended

|morpheus| Application OS
=========================

|morpheus| can be installed on the following platforms. Please note the table below is for |morpheus| Application OS support, not |morpheus| Agent OS Support.

.. note:: If CentOS 8.2 is pinned to 8.2.2004 vault, the PowerTools repository will need to be pinned to 8.2.2004 to access freerdp-libs 2.0.0

.. list-table:: **Supported Appliance Operating Systems**
   :widths: auto
   :header-rows: 1

   * - OS
     - Version(s)
     - Notes
   * - Amazon Linux
     - 2
     -
   * - CentOS
     - 7.x, 8.x
     - If CentOS 8.2 is pinned to 8.2.2004 vault, the PowerTools repository will need to be pinned to 8.2.2004 to access freerdp-libs 2.0.0
   * - Debian
     - |debianVersion|
     - FreeRDP 2.0 is not compatible with Debian 9. guacd will remain at 1.0.0 for Appliances running on Debian 9.
   * - RHEL
     - 7.x, 8.x
     -
   * - SUSE Linux Enterprise Server (SLES)
     - 12, 15
     -
   * - Ubuntu
     - 16.04, 18.04, 20.04
     - 14.04 is no longer supported for Appliance OS. Existing Appliances on 14.04 must upgrade to 16.04, 18.04 or 20.04 PRIOR to upgrading to v4.2.1+. Note: 14.04 is still supported by the |morpheus| Agent.

Services
========

|morphver| Service Version Changes
----------------------------------

:Appliance: - Java: Updated jdk to v11.0.14
            - MySQL: Embedded MySQL updated to v5.7.37 :superscript:`5.2.15`
            - Tomcat: Updated to v9.0.58
:Agent: - Added FIPS compliant el8 |morpheus| Agent node & vm-node packages. Compatible with RHEL 8, CentOS 8, and Oracle Linux 8
        - Agent Node & VM Node Packages: Java: Updated jdk to v11.0.14
        - |morpheus| Windows Agents updated to v1.8.0, fixes Windows Bare-Metal Servers displaying incorrect core count :superscript:`5.2.15`

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
     - - Node and VM Node Package versions updated to v3.2.5
       - Java jdk & jre updated to 11.0.14+9
   * - Morpheus Linux Agent
     - |linuxagentver|
     - No changes
   * - Morpheus Windows Agent
     - |winagentver|
     - |morpheus| Windows Agents updated to v1.8.0, fixes Windows Bare-Metal Servers displaying incorrect core count :superscript:`5.2.15`
   * - Morpheus macOS Agent
     - |macagentver|
     - |morpheus| macOS agent updated to |macagentver|
     - Java jdk & jre updated to 11.0.14+9


|

.. Security
.. ========

.. CVEs Addressed
.. --------------

|

Upgrade Paths & Methods
=======================

The following table shows supported version upgrade paths and methods.

.. include:: /release_notes/upgrade_table.rst

|

Integrations
============

.. note:: Current iterations of Amazon AWS, Microsoft Azure, Google Cloud Platform, Digital Ocean, HPE OneView, OpenTelekom Cloud, IBM Bluemix, Softlayer and UpCloud are all supported.

.. include:: /release_notes/compatibility_table.rst
