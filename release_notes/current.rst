.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. IMPORTANT:: |morpheus| 5.4.9 adds the "Provisioning: State" Role permission. This permission determines access to the State tab for Terraform-backed Instances and is set to "None" by default. On upgrade, only System Admin users will be able to see the State tab for these Instances. For other users who should have this access, edit their Roles to include "Provisioning: State" permissions.

.. warning:: Morpheus |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

Release Dates
  - |morphVer|-1 |releasedate|

New Features
============

:API & CLI: - Updating Kubernetes Clusters via |morpheus| API or CLI now allows toggling the "Managed" attribute or adding an "API Token" value as you can already through |morpheus| UI. :superscript:`5.5.2`
:Azure: - Azure workloads can now be provisioned to different regions from the resource group (if desired) as you can from the Azure web console. :superscript:`5.5.2`
:Clouds: - Added ability to associate existing VMs (Infrastructure > Compute > Virtual Machines) to different Clouds. **NOTE: This is not a migration tool. Once a workload has been moved to a new Cloud, use this functionality to associate the existing managed VM record to the new Cloud and wipe out the newly discovered unmanaged VM record. This preserves the original VM record and associated historical data while recognizing the new Cloud and continuing monitoring operations from the new VM** :superscript:`5.5.2`
:Google Cloud (GCP): - Cloud sync for GCP Clouds is no longer interrupted when Projects are disabled or do not have API access granted. :superscript:`5.5.2`
:Network: - Network labels (display names) are now editable from the Network tab of the Instance detail page.
:Plans and Pricing: - Added capability to export Service Plans list as a CSV document (Administration > Plans & Pricing > Plans). :superscript:`5.5.2`
:PowerDNS: - PowerDNS integrations now include the "Create Pointers" option to automatically create reverse records as other DNS integrations currently do. :superscript:`5.5.2`
:Roles: - "Provisioning: State" role permission added to control access to the State tab on Terraform Instance detail pages. **IMPORTANT: This permission is "None" by default for all users other than System Admins. Following upgrade, users which are not System Admins will no longer have access to the State tab. Role permissions will need to be updated for all users which need access to the State tab.** :superscript:`5.5.2`
:Rubrik: - Rubrik integration settings are updated to remove username and password fields and replace them with an API key field. Existing integrations will continue to work unless upgraded to the latest Rubrik versions which require MFA to be enabled. :superscript:`5.5.2`
:Security:  - Velocity templates upgraded to 2.3 (CVE-2022-13936). :superscript:`5.5.2`
            - aws-java-sdk-s3 upgraded to version 1.12.261 (CVE-2022-31159). :superscript:`5.5.2`
            - esapi upgraded to version 2.3.0.0 (CVE-2022-23457). :superscript:`5.5.2`
            - mysql-connector-java upgraded to 8.0.28 (CVE-2022-21363). :superscript:`5.5.2`
            - xmlsec upgraded to 2.2.3 (CVE-2021-40690). :superscript:`5.5.2`
:vCloud Director: - VMs for multi-node vCD Instances are now created within the same vApp on the vCD side. Previously, a separate vApp was created for each VM. :superscript:`5.5.2`


Fixes
=====

:API & CLI: - Fixed an issue that caused OpenStack, Huawei, and OTC Clouds created via |morpheus| API and CLI not to work properly. :superscript:`5.5.2`
             - Fixed an issue that prevented adding deployment versions of type "fetch" using the no prompt approach and specifying the fetch URL option in the command. :superscript:`5.5.2`
             - Fixed an issue that prevented upload of Virtual Images of type azure-reference via |morpheus| CLI. :superscript:`5.5.2`
             - Tags can now be added normally via |morpheus| API and CLI to Instances added by provisioning an App Blueprint. Previously, these needed to be passed via the customOption block in an update JSON block. :superscript:`5.5.2`
             - When creating Azure Resource Pools via |morpheus| API, the inventory flag now defaults to true to minimize confusion. :superscript:`5.5.2`
:Amazon: - Users can now successfully provision to AWS Clouds when Service Control Policies for Tagging are set in AWS. :superscript:`5.5.2`
:Ansible Tower: - Ansible Tower Tasks and Workflows can now be run against the server context. Previously they could only be run against the Instance context. :superscript:`5.5.2`
:Ansible: - Ansible Tasks and Workflows now use the '/var/opt/morpheus/morpheus-local/workspace' directory instead of '/var/opt/morpheus/morpheus-ui/workspace'. :superscript:`5.5.2`
           - Fixed an issue that caused App provisioning to fail if the Ansible command options field was locked on the App Blueprint. :superscript:`5.5.2`
           - When |morpheus| Agent is installed but the command bus is not used, |morpheus| will now use the SSH username and keypair. :superscript:`5.5.2`
:Automation Scale Thresholds: - Fixed an issue that could cause Scale Thresholds to repeatedly create and destroy VMs under certain configurations. :superscript:`5.5.2`
:Automation Tasks: - Fixed an issue that prevented users from creating or editing Tasks if they did not have "Infrastructure: Credentials" permissions set to Full on their Roles. :superscript:`5.5.2`
                  - When a Task is referencing a file tracked in a Github repository that does not exist, the Task detail page can now be viewed rather than a 403 error page being displayed. :superscript:`5.5.2`
                  - When selecting many Instances or servers (typically around 15 or more), and running a Task or Workflow against them, the desired automation is now run on all selected workloads rather than just some. :superscript:`5.5.2`
:Azure: - Azure Clouds no longer lose their scope (Resource Group and Region) when updating the Client Secret used to authenticate the Cloud. :superscript:`5.5.2`
         - Fixed an issue that caused a Cloud costing refresh for a previous month to raise invoice amounts, which required costing to be rebuilt to be accurate once again. :superscript:`5.5.2`
         - Fixed an issue that prevented creating a new Azure Load Balancer to associate with an Instance if one was created at provision time and later removed via the Instance detail page. :superscript:`5.5.2`
         - Fixed an issue that preventing costing sync from ever completing for very large Azure Clouds. :superscript:`5.5.2`
:Backups:    - Added a cleanup job to eventually expire out stuck or failed "in progress" backup jobs. This prevents a situation where a backup job can be stuck with no way to delete it. :superscript:`5.5.2`
:Blueprints: - App Blueprints can no longer be saved with identical names to other App Blueprints by pre-pending them with leading whitespace characters (which would be automatically removed after the validation step). :superscript:`5.5.2`
              - App Blueprints which currently have Apps deployed from them can no longer be deleted. UI messages are surfaced to inform the user why the App Blueprint cannot be deleted. :superscript:`5.5.2`
:Buckets: - Fixed an issue that could cause "inactive" AWS S3 Buckets to still be visible in the UI. :superscript:`5.5.2`
:Catalog: - Fixed a display issue that caused very long Input help blocks to overset the Catalog Item order window. :superscript:`5.5.2`
           - Fixed an issue that caused very long Input labels to wrap incorrectly and end up behind the field itself. :superscript:`5.5.2`
           - Fixed an issue that could cause areas of the Service Catalog Cart page to be formatted incorrectly if Input labels, Input values, or Catalog Item names/descriptions were very large. :superscript:`5.5.2`
           - Fixed some odd behavior that could arise for Inputs in Service Catalog items depending on the interaction between dependent, visibility, and required settings related to other Input values. :superscript:`5.5.2`
           - The "More" button near the bottom of the Executions tab on the Catalog Inventory page now expands as expected. :superscript:`5.5.2`
           - When editing an existing Service Catalog item that uses a |morpheus|-included logo, the saved logo no longer disappears from the Edit Catalog Item modal. :superscript:`5.5.2`
           - Workflow-based Service Catalog items no longer have potential to hang when multiple typeahead Input values are selected. :superscript:`5.5.2`
:Distributed Worker: - Fixed an issue that caused Distributed Workers to disconnect which interrupted sync with associated Clouds. :superscript:`5.5.2`
:Identity Sources: - Fixed CSP dev console errors that could appear in logs when viewing the Identity Sources list page. :superscript:`5.5.2`
:Infoblox: - Improved validation on Infoblox integration add/edit modal to only allow a throttle rate up to 5000ms. If a greater time is entered, the value will be set to 5000. :superscript:`5.5.2`
:Jobs: - Fixed an issue that could prevent a Job from executing properly if done from the Job detail page (Provisioning > Jobs > Selected Job > Execute). :superscript:`5.5.2`
:Kubernetes:  - Fixed an issue that caused Kubernetes Clusters provisioned to OpenStack Clouds with floating IP addresses to be unreachable from outside the cluster due to certificates being registered to private addresses rather than public. :superscript:`5.5.2`
              - Fixed an issue that could cause External Kubernetes clusters to become stuck in the deprovisioning state during deletion and never leave the UI. :superscript:`5.5.2`
              - Required fields are now respected when adding external Kubernetes clusters. :superscript:`5.5.2`
:Layouts: - The "Permissions" selection inside the Action menu on a Layout Detail page (Library > Blueprints > Layouts > Selected Layout) now works correctly. :superscript:`5.5.2`
:MicrosoftDNS: - Fixed an issue causing PTR records to be created in the wrong zone when creating MicrosoftDNS records via |morpheus| API. :superscript:`5.5.2`
:Monitoring: - Added TLS support for RabbitMQ-type checks (Monitoring > Checks). :superscript:`5.5.2`
:NSX-T: - BGP Enable Status for NSX-T Tier0 Routers is now returned in a GET call to the |morpheus| API for the router. :superscript:`5.5.2`
         - The Host Records tab is now hidden for NSX-T networks which are not associated with IP Pools to avoid confusion. :superscript:`5.5.2`
:OpenStack: - A more descriptive error is now surfaced when attempting to create an OpenStack Security Group when the SG quota is already reached. :superscript:`5.5.2`
             - Fixed an issue that could cause additional disks to be shown in |morpheus| UI (not in the Cloud backend) when deploying Windows workloads to OpenStack Clouds. :superscript:`5.5.2`
             - Fixed an issue that could cause discrepancy between network interface labels on an OpenStack Instance and that which was being reported on the Instance detail page in |morpheus|. :superscript:`5.5.2`
:Oracle Cloud: - Currency and conversion rate are now being handled correctly for non-USD costing for Oracle Cloud workloads. :superscript:`5.5.2`
                - Fixed an issue that prevented |morpheus| Agent install for OCI Windows 2019 Instances unless the VM IP address was added to the WinRM port on the security group outbound rule. :superscript:`5.5.2`
                - Updated the manner in which |morpheus| displays the number of CPU cores for Oracle Cloud workloads to better reflect the specifics of Oracle CPU count. :superscript:`5.5.2`
:Plans and Pricing: - When adding Price Sets to plans, it's no longer possible for very long Price Set text to overset the Edit Price Plan modal. :superscript:`5.5.2`
                  - When deleting a Service Plan, Instances associated with that Plan will have their Plans automatically updated to a new one. Previously, under certain scenarios, the Plan association could remain tied to the now-deleted Plan. :superscript:`5.5.2`
:Plugins: - Custom Catalog Plugins now have access to the "Dark Mode" themed versions of icon images. :superscript:`5.5.2`
:Policies: - Cloud-scoped Delayed Delete and Delete Approval Policies now apply as expected to XaaS (Workflow-based) Instance Types. :superscript:`5.5.2`
            - Fixed an issue that could cause Tagging Policies not to be applied if a Naming Policy did not also apply to the workload being provisioned. :superscript:`5.5.2`
            - Fixed an issue that would rename hosts in clusters which were under a cluster naming policy if the host was later edited. :superscript:`5.5.2`
:Provisioning: - Fixed an issue that prevented Safari web browser users from setting a custom memory amount at provision time for Service Plans which allowed it. :superscript:`5.5.2`
                - Fixed an issue that prevented hostnames from being set correctly if given in all caps and the Instance contained multiple VMs. :superscript:`5.5.2`
                - Fixed awkward line wraps that could appear in certain tabs of the Instance provisioning wizard. :superscript:`5.5.2`
:Puppet: - Fixed an issue that caused the Puppet agent not to be installed correctly on Windows workloads. :superscript:`5.5.2`
:Reports: - Fixed a memory consumption issue caused when exporting very large reports (Operations > Reports) to CSV. It should now be safe to export very large reports. :superscript:`5.5.2`
:Roles: - When renaming Multitenant User Roles, the new Role name is now reflected in the Roles list on the User detail. :superscript:`5.5.2`
:Security: - Fixed an issue that allowed Primary Tenant users to view Subtenant Group information via |morpheus| API by modifying the request in a specific way. :superscript:`5.5.2`
:ServiceNow: - Fixed an issue that caused Naming Policy errors when provisioning Service Catalog items via ServiceNow integration. :superscript:`5.5.2`
:Settings: - Removed the "Default Appliance Locale" setting from the global settings (Administration > Settings) panel for Subtenants. This option was not meant to be exposed to Subtenants and only the Primary Tenant's setting applied to the appliance anyway. :superscript:`5.5.2`
:Tenants: - Fixed an issue that prevented deletion of Tenants if they had Archive buckets associated with them. :superscript:`5.5.2`
           - Improvements added to the Tenant delete process which, under certain conditions, could become stuck due to SQL constraint issues. :superscript:`5.5.2`
:Terraform: - Fixed a display issue that could cause individual VM components of a Terraform App (such as an EC2 Instance) to be labeled as a container rather than a VM. :superscript:`5.5.2`
             - Fixed an issue that led to large Terraform Apps causing the web browser tab to consume large amounts of memory and crash. :superscript:`5.5.2`
             - Terraform App detail pages no longer return 404 errors during the early part of the provisioning process. :superscript:`5.5.2`
:UI: - Fixed a UI rendering issue on the edit modal for an existing identity source. :superscript:`5.5.2`
      - Fixed an issue on the VMs list page (Infrastructure > Compute > Virtual Machines) that could cause the Power On/Off fly-out menu to be partially cut off. :superscript:`5.5.2`
      - Fixed an issue that caused Input fields to overset the Service Catalog item box when its associated help block was very long. :superscript:`5.5.2`
      - Fixed an issue that caused Input name labels to overlap each other on Service Catalog item pages if the label was very long. :superscript:`5.5.2`
      - Fixed an issue that could cause text on the Instance Provisioning wizard Review tab to overset the menu window. :superscript:`5.5.2`
      - Fixed an issue that hid the IP addresses from the Instance detail page when viewed at narrow (mobile) widths. :superscript:`5.5.2`
      - Search bars in |morpheus| (Instance list, server list, etc.) will now search properly on numerals entered as search terms. :superscript:`5.5.2`
      - Updated help block text for Tenant Visibility settings to more accurately reflect the current functionality of Visibility settings. :superscript:`5.5.2`
:Users: - Fixed an issue that prevented deleting a user which had created a credential (Infrastructure > Trust). :superscript:`5.5.2`
:VMware: - Fixed an issue that could cause VMware VMs to fail to boot when using multiple disks and Cloud-init. :superscript:`5.5.2`
          - Fixed an issue that could cause snapshots not to be cleaned up after execution of clone process on VMware Clouds. :superscript:`5.5.2`
:Virtual Images: - Fixed an issue that cleared manual configurations set in |morpheus| on Virtual Images synced from VMware Content Library after the next Cloud sync. :superscript:`5.5.2`
                  - Fixed an issue that could cause failures when uploading Virtual Images via |morpheus| CLI when the same image could be uploaded fine via |morpheus| UI. :superscript:`5.5.2`
:vCloud Director: - Datastores now sync in correctly when vCD Clouds are integrated using the System Admin user. :superscript:`5.5.2`


Appliance, Node & Agent Updates
===============================

:Appliance: - Elasticsearch: Embedded elasticsearch default tmp_dir changed to /var/tmp/elasticsearch. Resolves issue when /var/run is noexec. Note: elasticsearch tmp_dir can be modified with ``default['morpheus_solo']['elasticsearch']['tmp_dir']`` in morpheus.rb (applies to previous versions too) :superscript:`5.5.2`
            - Java: morpheus-appliance embedded Java updated to |java| :superscript:`5.5.2`
            - MySQL: Embedded MySQL upgraded to |mysqlver|. :superscript:`5.5.2`
            - Tomcat: Embedded Tomcat upgraded to |tcver|. :superscript:`5.5.2` :superscript:`CVE-2022-23181`
:Node packages: - Cleanup: Legacy code remeoved that could have caused path conflictes when install morpheus-agent on morpheus-applaince hosts. :superscript:`5.5.2`
                - Java: morpheus-node & morpheus-vm-node embedded Java updated to |java| :superscript:`5.5.2`
                - morpheus-node & morpheus-vm-node packages updated to v3.2.9 :superscript:`5.5.2`
