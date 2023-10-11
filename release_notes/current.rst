.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to v6.2.2 for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to v6.2.2
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

Fixes
=====

:Amazon: - Fixed an issue that caused long-running deployments of CloudFormation templates to fail if the token expired during provisioning :superscript:`6.0.7`
:Azure: - Availability Options and Availability Set/Zone are now shown on the Instance detail page for Azure Instances :superscript:`6.0.7`
         - The volume and network charges are now being categorized properly for Azure clouds. Volume charges show up under the Volume type and the network charges are under the Server type as individual line items :superscript:`6.0.7`
:Backups: - The Backup Consistency and Backup Policy droplists are now implemented with appropriate dependencies in the Backups section of the Automation tab in the Instance wizard :superscript:`6.0.7`
           - When a backup result fails to delete, |morpheus| will now provide an error message in the UI to notify the user :superscript:`6.0.7`
:Catalog: - Added support for saving Catalog items without first passing a check for valid JSON in the config
           - Improved display of very long label names for custom Input fields on Catalog items
:Cluster Layouts: - Provisioning Kubernetes clusters using cloned Cluster Layouts is working now and |morpheus| is pulling in the full list of packages in the cloned Cluster Layout :superscript:`6.0.7`
:Commvault: - Commvault backup jobs no longer show as scheduled with a next run date since |morpheus| does not sync or set that information and it is managed by Commvault :superscript:`6.0.7`
             - Fixed Commvault clone backup jobs failing with errors under certain configurations :superscript:`6.0.7`
:Cypher: - Fixed failures in Cypher access via Tasks when run in the context of Instances or servers having NULL owner :superscript:`6.0.7`
:Forms: - Provisioning with volumes not set to auto inject is now working properly. Use the syntax: "volumes":<%=customOptions.volumes%>
:Hosts: - Fixed hostname generation for Windows nodes added to Instances with longer (15+ char) hostnames :superscript:`6.0.7`
         - |morpheus| will now set the display name of an Instance to its name value when converting a discovered VM to managed :superscript:`6.0.7`
:Inputs: - Added "REMOVE NO SELECTION" attribute for Select List-based Inputs. This defaults the Input to the first selection in the list rather than to an empty selection
         - Child Inputs (those configured to be dependent on another Input) attached to Catalog Items will now reload again when the parent Input value is re-set. Previously they would only load the first time the parent Input was set
:Hyper-V: - After migrating VMs to new Hyper-V hosts, |morpheus| now correctly syncs the new host details :superscript:`6.0.7`
           - |morpheus| will now discover and sync workloads from more than one Hyper-V host in the same Cloud :superscript:`6.0.7`
:Instances: - Aligned Instance counts on the main Dashboard and on the Instances list page. Depending on status (stopped, etc.), these values could be out of alignment :superscript:`6.0.7`
:Layouts: - Added Display Order property for Layouts. Layouts are listed in high-to-low order based on the Display Order in the Layouts dropdown of the provisioning wizard :superscript:`6.0.7`
:Nutanix Prism Central: - PTR registration when provisioning using the Infoblox integration is now working properly :superscript:`6.0.7`
:OpenStack: - OpenStack-type Clouds (OpenStack, Huawei, Open Telekom) now properly route traffic via proxy when an API PROXY value is configured on the Cloud :superscript:`6.0.7`
             - Provisioning to Openstack with a static IP for a cloud subnet that doesn't have DHCP enabled is working properly now :superscript:`6.0.7`
:Option Lists: - Fixed REST-sourced Option Lists not using a configured global proxy when non-SOCKS type proxies were set :superscript:`6.0.7`
:Plugins: - Help block text now displays properly when using Inputs in backup provider plugins :superscript:`6.0.7`
           - When creating a reports plugin, the 'reportResult' parameter that is passed to 'renderTemplate' method is no longer returning null for createdBy, account, and type attributes
:Roles: - All permissions types now sync properly to copies of multitenant roles within tenants :superscript:`6.0.7`
         - Fixed an issue with certain permissions filtering down correctly when a Tenant's base role was a built-in system Role (like Tenant Admin) :superscript:`6.0.7`
:Security: - Embedded Tomcat upgraded to version 9.0.80 to mitigate CVE-2023-41080 :superscript:`6.0.7`
:ServiceNow: - After provisioning of a Catalog item requested via ServiceNow integration, the status of the requested item in ServiceNow is now automatically rolled to "Closed Complete" :superscript:`6.0.7`
              - Fixed new ServiceNow integrations not appearing immediately as an approval engine selection for Approve Provision Policies :superscript:`6.0.7`
              - Removed the "Add Catalog Item" button from a ServiceNow integration detail page when the |morpheus| plugin is not installed on the ServiceNow appliance :superscript:`6.0.7`
:Tenants: - Fixed an issue that caused links to the health page and the hosts list page not to be active in new Tenants :superscript:`6.0.7`
:VMware: - Reconfiguring to add a new disk in the same datastore as the root disk to a machine that previously changed names will no longer add a new disk folder in VMware. This aligns |morpheus| behavior to that already seen in vCenter :superscript:`6.0.7`
:Zerto: - The optional Organization and Service Profile fields on a Zerto replication group are now being handled properly :superscript:`6.0.7`



Appliance & Agent Updates
=========================

:Appliance: - Embedded Elasticsearch upgraded to 8.9.0 :superscript:`6.0.7`
             - Embedded MySQL upgraded to 8.0.34 :superscript:`6.0.7`
             - Embedded Nginx upgraded to 1.25.1 :superscript:`6.0.7`
             - Embedded RabbitMQ upgraded to 3.12.2 :superscript:`6.0.7`
:Agent: - |morpheus| Linux Agent updated to v2.4.2 with fix for directory filter on bonded network stats
        - Node and VM Node Packages update to v3.2.17 with update Linux Agent

:Embedded Plugins: - Infoblox updated to v1.2.0
                   - Bluecat updated v1.1.0
                   - phpIPAM updated to v1.1.0
                   - Rubrik updated to v1.0.6
