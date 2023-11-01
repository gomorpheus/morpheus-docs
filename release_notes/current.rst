.. _Release Notes:

*********************************
|60x| |releasetype| Release Notes
*********************************

.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to v6.0.7+ for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6 prior to upgrading to v6.0.7+
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added CRUD support for NSX-T network service integrations. Previously it was only possible to list the available network server details. See API documentation for further details :superscript:`6.2.3`
             - Added ``/instances/stats`` endpoint to return summary details related to Instances which may also be filtered to return stats on just specific groupings of Instance. Additional details are available in |morpheus| API documentation :superscript:`6.2.3`
             - The ability to refresh a cluster has been added to |morpheus| API and CLI
:Identity Sources: - SAML SSO identity sources using HTTP-POST binding are now working as expected when integrated with |morpheus| Tenants :superscript:`6.2.3`
:Kubernetes: - Updated Calico image retrieval to pull from quay.io to avoid customers hitting Docker Hub image pull rate limits :superscript:`6.3.0 6.2.3`
              - Upgrade default Kubernetes Cluster Layouts to version 1.28 :superscript:`6.3.0 6.2.3`


Fixes
=====

:API & CLI: - The ``backupProviderType`` input parameter is now optional when creating a backup through the API. Previously creating backups would fail without providing it :superscript:`6.3.0 6.2.3`
             - The ``backupType`` property for the create backup API call is now properly handling a non-Morpheus backup type :superscript:`6.3.0 6.2.3`
:Ansible Tower: - When hosts are deleted from |morpheus| they are now removed from all Ansible Tower inventories. Previously if they were part of multiple inventories they would only be removed from one :superscript:`6.2.3 6.3.0`
:Backups: - Fixed an issue that could cause the wrong backup provider to be selected when there were multiple of the same type integrated (ex. Veeam). The provider associated with the Cloud is now always selected :superscript:`6.3.0 6.2.3`
:Kubernetes: - Editing and resaving packages on Kubernetes Cluster Layouts after the initial save is now working properly :superscript:`6.2.3 6.3.0`
:Nutanix Prism Central: - The handling of the UEFI setting on the Virtual Image and Instance Type and the Secure Boot setting on the Instance Type for Nutanix Prism Central Cloud Instance provisioning is working properly
:Plugins: - Fixed an issue related to displaying dependent fields in custom backup plugins within the backups section of the provisioning wizard :superscript:`6.3.0 6.2.3`
           - Having incompatible plugins installed will no longer prevent UI startup following an upgrade :superscript:`6.2.3 6.3.0`
:Policies: - The approval of extensions on expiration and shutdown Policies on Instances is now working properly
:Security: - Closed a potential HTML injection vulnerability
            - Tomcat upgraded to 9.0.80 to mitigate CVE-2023-41080 :superscript:`6.2.3`
:ServiceNow: - Fixed an issue that could cause duplicate entries in ServiceNow CMDB in specific cases involving multiple |morpheus| Tenants :superscript:`6.3.0 6.2.3`
              - For ServiceNow Approvals, |morpheus| now sends the unique username in addition to the non-unique display name to ensure the approver can properly evaluate who is making the request :superscript:`6.3.0 6.2.3`
:Workflows: - Scoping Workflows to a platform (Linux or Windows) now results in proper filtering when choosing to run a Workflow against a workload. Windows Workflows are not shown as an option for Linux workloads, for example
             - When a Workflow has a Task in the Configuration phase and that Workflow is referenced in a Workflow Policy, it is executed as expected during the Configuration phase on Instance provision
:XaaS: - Attempting to utilize the user variable ``morpheus['user']['username']`` within a Python Task targeting an XaaS Instance will no longer cause the Task to fail :superscript:`6.2.3 6.3.0`

Embedded Plugins
=========================

:Infoblox: infobox-plugin updated to v1.2.1
:Microsoft DNS: msdns-plugin updated to v2.1.1
:PowerDNS: powerdns-plugin updated to v1.0.3
:Solarwinds: solarwinds-plugin updated to v1.0.2

Appliance & Agent Updates
=========================

:Installer: The entry ``skip-log-bin`` is now being written to the embedded MySQL 8 bin log file at ``/opt/morpheus/embedded/mysql/my.cnf``. This results in logging being turned off by default in MySQL 8 on the appliance
:Node Package: |morpheus| Node and VM Node packages updated to v3.2.18 with updated repo GPG keys.
:Tomcat: Embedded Tomcat updated to |tcver|
