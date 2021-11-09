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
- 5.3.2+: The local code repository path moved from ``/var/opt/morpheus/morpheus-ui/repo`` to ``/var/opt/morpheus/morpheus-local/repo`` to reduce potential shared storage issues and perfomace restrictions. The reconfigure process creates the folders and sets the paths in application.yml, no manual intervention is needed unless symlinks exisit on ``/var/opt/morpheus/morpheus-ui/repo/git`` which will need to be removed prior to reconfiguring 5.3.2. The old ``/var/opt/morpheus/morpheus-ui/repo`` path will be automatically deleted in a fulture release but can be manually recursivly deleted at any time for storage reclaimation.
- 5.3.3: Support for OpenStack v2 Identity API is removed
- 5.3.4: Major UI navigation structure changes. Refer to :ref:`navchanges` refrence table

|morpheus| Application OS
=========================

|morpheus| can be installed on the following platforms. Please note the table below is for |morpheus| Application OS support, not |morpheus| Agent OS Support.

.. important:: Existing |morpheus| Appliances on 14.04 must upgrade to 16.04, 18.04 or 20.04 PRIOR to upgrading to v4.2+.

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

- Java upgraded to 8u312-b07 :superscript:`5.2.12`
- MySQL upgraded to 5.7.35 :superscript:`5.2.12`
- Nginx upgraded to 1.20.1 :superscript:`5.2.12`
- RabbitMQ upgraded to 3.9.8 :superscript:`5.2.12`
- Tomcat upgraded to 9.0.54 :superscript:`5.2.12`

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


Security
========

CVEs Addressed
--------------

- CVE-2021-23369

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
