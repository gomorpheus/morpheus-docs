.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - Added CRUD support for NSX-T network service integrations. Previously it was only possible to list the available network server details. See API documentation for further details :superscript:`6.0.8`
             - Added ``/instances/stats`` endpoint to return summary details related to Instances which may also be filtered to return stats on just specific groupings of Instance. Additional details are available in |morpheus| API documentation :superscript:`6.0.8`
:Identity Sources: - SAML SSO identity sources using HTTP-POST binding are now working as expected when integrated with |morpheus| Tenants :superscript:`6.0.8`
:Kubernetes: - Updated Calico image retrieval to pull from quay.io to avoid customers hitting Docker Hub image pull rate limits :superscript:`6.0.8 6.3.0`
              - Upgrade default Kubernetes Cluster Layouts to version 1.28 :superscript:`6.0.8 6.3.0`
:Plugins: - Improvements added to Task-type Plugins. See Developer Portal documentation for more details :superscript:`6.3.0`
:ServiceNow: - ServiceNow Catalog Items built using Forms can no longer be exposed to an integrated ServiceNow appliance. This is not yet supported but will be in the future :superscript:`6.3.0`


Fixes
=====

:API & CLI: - Fixed a 500 error that would appear from the call to list AWS Security Groups during the ``instances add`` CLI workflow to add a new AWS Instance
             - The ``backupProviderType`` input parameter is now optional when creating a backup through the API. Previously creating backups would fail without providing it :superscript:`6.0.8 6.3.0`
             - The ``backupType`` property for the create backup API call is now properly handling a non-Morpheus backup type :superscript:`6.0.8 6.3.0`
:Ansible Tower: - When hosts are deleted from |morpheus| they are now removed from all Ansible Tower inventories. Previously if they were part of multiple inventories they would only be removed from one :superscript:`6.0.8 6.3.0`
:Azure: - Fixed an issue that caused discrepancies in reported Azure costing when Azure Clouds were scoped to a specific region :superscript:`6.0.8`
:Backups: - Fixed an issue that could cause the wrong backup provider to be selected when there were multiple of the same type integrated (ex. Veeam). The provider associated with the Cloud is now always selected :superscript:`6.0.8 6.3.0`
:Catalog: - Fixed an issue that made Instance detail pages inaccessible if the Catalog Item they were provisioned from was later deleted
           - Fixed an issue that prevented Catalog Items from consuming Cypher values
           - We are now properly handling the setting of resource pool IDs dependent on the scoping of the AWS Cloud. We are also validating that resource pool IDs are valid when provisioning to a Cloud scoped to a single VPC
:Forms: - Fixed an issue that caused Provisioning-type Inputs on Forms to become associated with different dependent fields after saving which caused the resulting Catalog Items not to work properly
:Inputs: - Fixed an issue that prevented the initial value from being set when the "REMOVE NO SELECTION" attribute was set on an Input
:Installer: - The entry ``skip-log-bin`` is now being written to the embedded MySQL 8 bin log file at ``/opt/morpheus/embedded/mysql/my.cnf``. This results in logging being turned off by default in MySQL 8 on the appliance :superscript:`6.0.8`
:Kubernetes: - Editing and resaving packages on Kubernetes Cluster Layouts after the initial save is now working properly :superscript:`6.0.8 6.3.0`
:Plugins: - Fixed an issue related to displaying dependent fields in custom backup plugins within the backups section of the provisioning wizard :superscript:`6.0.8 6.3.0`
           - Having incompatible plugins installed will no longer prevent UI startup following an upgrade :superscript:`6.0.8 6.3.0`
:Route 53: - Removed warning about insecure HTTP URLs from Amazon Route53 Add Integration modal since there is no URL value requested on that modal :superscript:`6.0.9`
:Security: - Tomcat upgraded to 9.0.80 to mitigate CVE-2023-41080 :superscript:`6.0.8`
:ServiceNow: - Fixed an issue that could cause duplicate entries in ServiceNow CMDB in specific cases involving multiple |morpheus| Tenants :superscript:`6.0.8 6.3.0`
              - For ServiceNow Approvals, |morpheus| now sends the unique username in addition to the non-unique display name to ensure the approver can properly evaluate who is making the request :superscript:`6.0.8 6.3.0`
:XaaS: - Attempting to utilize the user variable ``morpheus['user']['username']`` within a Python Task targeting an XaaS Instance will no longer cause the Task to fail :superscript:`6.0.8 6.3.0`

Embedded Plugins
=========================

:Plugin API: Compatible Plugin API version updated to |pluginVer|
:BigIp: bigip-plugin updated to v1.1.0
:Bluecat: bluecat-plugin updated to v1.1.1
:Infoblox: infobox-plugin updated to v1.2.1
:Microsoft DNS: msdns-plugin updated to v2.1.1
:phpIPAM: phpipam-plugin updated to v1.1.1
:PowerDNS: powerdns-plugin updated to v1.0.4
:Rubrik: rubrik-plugin updated to v1.1.0
:Solarwinds: solarwinds-plugin updated to v1.0.3

Appliance & Agent Updates
=========================

:Installer: The entry ``skip-log-bin`` is now being written to the embedded MySQL 8 bin log file at ``/opt/morpheus/embedded/mysql/my.cnf``. This results in logging being turned off by default in MySQL 8 on the appliance
:Node Package: |morpheus| Node and VM Node packages updated to v3.2.18 with updated repo GPG keys.
:Tomcat: Embedded Tomcat updated to |tcver|