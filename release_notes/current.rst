.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. Small Update, omitting highlights this time
  .. include:: highlights.rst
.. important:: In 5.2.3 ``codeready`` (codeready-builder-for-rhel-8-x86_64-rpms) repo access required for RHEL 8+ Appliances, replacing the previous PowerTools/powertools requirement.

New Features
============

- Amazon: AWS Instances can now be cloned to AWS Clouds associated with a different account from the source Cloud. This is currently only supported by single-disk VMs as the image to be cloned is created from the root disk only
- Ansible Tower: Updated Ansible Tower integration to pass ``extra_vars`` YAML to the Tower job when using Ansible Tower with provisioning or when running Ansible Tower-type |morpheus| Tasks
- Azure: Added Azure SQL DBaaS Service Plans and Price Sets. Note: Azure Standard S4-S11 prices are not included in Azure Ratecard data.
- Backups: Azure VMs can now be restored to a current Instance, previously they needed to be restored to a new Instance
- CloudFormation: YAML templates now accepted in addition to JSON for CF Blueprints and Spec Templates both entered locally and ingested through integration with a Git repository
- Clouds: Grant `read-level access <https://docs.morpheusdata.com/en/5.2.3/administration/roles/roles.html#cloud-access-levels>`_ to Clouds for Tenants through the applied Tenant Role
- Huawei Cloud: Improved filtering to show only plan sizes which are currently available during provisioning
- Open Telekom Cloud: Improved filtering to show only plan sizes which are currently available during provisioning
- Oracle Cloud: Instance reconfigure support added for Oracle Cloud plan change and boot volume resizing
- Policies: Improved handling for budget, max containers, max cores, max hosts, max memory, and max storage policies when adding nodes to Instances (manually or through auto-scaling and thresholds)
- Policies: Improved policy handling when provisioning Instances as it relates to specific handling of copy and scale scenarios, friendlier policy warning messages, and other improvements
- Policies: Policy types including budget, max cores, max hosts, max memory, and max storage are now considered when provisioning a new cluster or when adding a new host to an existing cluster
- Policies: When completing cart checkout in the Service Catalog Persona view, the sum of all ordered items within the cart are considered against any policies that may be in place
- Policies: When provisioning Apps, Instance types containing multiple nodes (such as Redis master/replica) or Instances with scale factor are considered against policy types including budget, max containers, max cores, max memory, max storage, and max VM
- Storage: Added support for SMB2 file shares
- Tasks: Task config sourced from Git/Github repository integrations is now synced of five-minute intervals as opposed to immediately on each Task execution
- Terraform: Support added for Terraform v0.14
- UI: Executions list page (Automation > Executions) now automatically refreshes to display new executions
- Veeam: Added ability to disable Backup Repositories, Backup Servers and Managed Servers.
- Veeam: Added context for Backup Servers in Backup configuration settings
- Veeam: Managed Servers tab added.
- Veeam: Multiple visibility and permissions added for Backup Repositories, Backup Servers and Managed Servers.
- Whitelabel: Set your own "Terms and Privacy String" to be displayed on the login page. This field takes HTML markup allowing administrators to link to an outside Terms and Conditions page, Privacy Policy page, or anything else

|morpheus| API & CLI Improvements
=================================

- API/CLI: "Clone To Image" action added for API/CLI
- API/CLI: User Sources metadata can now be accessed through either |morpheus| API or CLI, User Sources information has been moved from the Users section of |morpheus| API docs to the `Identity Sources <https://apidocs.morpheusdata.com/#identity-sources>`_ section
- API/CLI: Calls to the ``api/invoices`` endpoint no longer return the list of ``lineItems`` for each Invoice by default as, in some cases, this list could be very large. Instead, a call to ``api/invoices`` now returns the new property ``lineItemCount``. Invoices has a new parameter, ``includeLineItems=true``, which can be used when needed. GET calls for a specific Invoice (``/api/invoices/:id``) will still return ``lineItems``
- API/CLI: The ``rawData`` parameter for the ``invoices`` and ``invoices-line-items`` API is now deprecated

Fixes
=====

- Ansible Tower: Fixed sync data retention when Ansible Tower host is not reachable
- Amazon: Costing service now uses blended rates. Previously unblended rates were used.
- Amazon: Improved Amazon costing performance and accuracy
- API /CLI: Fixed issue with multiple User Source inputs including ``searchMemberGroups``, ``confs.doNotIncludeSAMLRequest``, and ``confs.doNotValidate*``
- Apps: Fixed brief flash of previous modal when a NEW APP modal is opened after closing a NEW APP modal.
- Apps: Fixed namespace/pool access for synced Clusters during Kubernetes & HELM App provisioning..
- Apps: Validation added to require positive integer in Lifecycle > Expiration Days filed
- Azure: ``buildNetworkInterfaceBlock`` API version updated to 2018-07-01
- Azure: Fixed a subset of Service Plans missing Price set associations
- Azure: Fixed Resource Pool Tenant Access changes persisting after provisioning ARM spec template
- AzureStack: ``update metadata`` api-version changed to 2017-12-01
- Backups: Fixed an issue that could cause Hyper-V Instance restore not to complete when restoring to a new Instance
- Clusters: Fixed issue with some Localizations causing invalid config when crating new Clusters
- Deletions: Refactored monitor check group delete for improved handling of high rate Instance deletions
- Global Proxy: No proxy patterns support added for Global Proxy
- Huawei: Fixed volume type issues limiting available ECS Flavors during provisioning.
- Identity Sources: Fixed SAML logins redirecting to |morpheus| login page after authentication from SAML provider (occurred only in 5.2.3-1)
- Instances: Fixed Instance and Container power status when there is an execution of a server-specific power schedule startup.
- Instances: Fixed issue where the disk(s) for the selected layout were add in addition to instead of replacing previously selected layouts disk(s)
- Instances: Instance List csv export now respects applied filters
- Jobs: Fixed ``Next Run`` value not respecting the timezone set on the assigned execute schedule.
- Morpheus Agent: Fixed Agent installation issue on Suselinux/OpenSuse for Appliances using a self signed certificate
- Notifications: Updated Instance Shutdown and Expiration warning email notifications to use tenant url redirect (matching provisioning notification behavior)
- Oracle Cloud: E3 Service Plans added
- OTC: Fixed user specified Floating IP bandwidth not applying
- Plans: Reverted previous change that filtered Service Plans with STORAGE value set to 0 and "CUSTOMIZE ROOT VOLUME" disabled due to not meeting minimum storage requirements of Virtual Image. Root disk size value is now set to template root disk size.
- PowerDNS: Validation added for saving PowerDNS Integration
- Reports: Fixed invalid tag filter causing reports failures
- SCAP: Fixed issue with running security scans on RHEL 7 hosts
- SCVMM: OS Type now synced for SCVMM Virtual Machines
- Security: Remediated potential XSS vulnerabilities
- vCloudDirector: Adding an additional NIC with static IP assignment to a VM with primary NIC using vCD IP Pool will no longer reboot the VM during reconfigure.
- Veeam: Added config option to remove unmanaged/discovered vm records created when Cloud sync runs during a restore but before the matching managed vm record is created, resulting in duplicate vm records.
- Veeam: Fixed Instance, Health and VM Status for restored backups
- Veeam: Fixed issue with restoring non-zipped/normal Veeam backups from Morpheus.
- Veeam: When restoring a deleted VM from a Veeam backup that was created from Morpheus, the restored Instance name will now match the original Instanc ename rather than the name of the restored backup.
- Zerto: Fixed replication group creation

Appliance Updates
=================

- Appliance & Agent Node Packages: Java upgrade to 8u282-b08
- Installer: Fixed issue with service handing for v5.x appliance upgrades during rpm/deb package upgrade/install that could cause reconfigure to fail until the services are manually restarted
- Installer: Lowered Minimum Memory validation to 7707033 (8GB) for FIPS-compliant Installers to match non-FIPS Installers.
- Appliance: Improved handling of Tomcat log rotation
- Installer: Updated RHEL 8 to use codeready repo and virt-devel module, removed PowerTools dependency

.. note:: |morpheus| v5.2.3-2 resolves cookie setting issue in v5.2.3-1 causing SAML logins to redirect to |morpheus| login page after authentication from SAML provider (occurred only in 5.2.3-1)
..
  Morpheus Hub
  ============

  Agent/Node Package Updates
  ==========================
