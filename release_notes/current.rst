.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. WARNING:: |morpheus| |morphver| only supports rolling upgrades for HA environments when upgrading from v6.0.2+.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Costing: - The date filter on the Invoices list page now defaults to the last three months to ensure quicker page loads :superscript:`6.0.6`
:NewRelic: - NewRelic monitoring has been deprecated and removed in |morpheus| 6.0.6+ and 6.2.1+. NewRelic monitoring settings are removed from global settings (|AdmSetMon|) :superscript:`6.0.6`
:Plugins: - Backup plugins that don't utilize |morpheus| Backup Jobs no longer display Job fields in the Instance and Backup wizards :superscript:`6.0.6`
:Security: - ``commons-net`` upgraded to 3.9.0 to mitigate CVE-2021-37533 :superscript:`6.0.6`
            - ``netty`` upgraded to 4.1.94 to mitigate CVE-2023-34462 :superscript:`6.0.6`


Fixes
=====

:API & CLI: - "ENABLE ROLE MAPPING PERMISSION" and "MANUAL ROLE ASSIGNMENT" options for Identity Sources in |morpheus| UI can now be toggled via |morpheus| CLI and API :superscript:`6.0.6`
:Amazon: - Amazon AWS Clouds scoped to all regions will no longer create duplicate domains or domain records
:Ansible: - When adding the Ansible Playbook Group at provision time, this group setting is now used correctly for Post Provision-phase Ansible Tasks :superscript:`6.0.6`
:Archives: - Private file access links to |morpheus| Archives now work correctly in environments with port 80 blocked :superscript:`6.0.6`
:Azure: - Fixed an issue provisioning from the built-in Azure Instance Type using Azure Marketplace synced virtual images for the first time on new appliances :superscript:`6.0.6`
         - Fixed an issue that caused Azure VMs provisioned with a static IP address to be provisioned with a DHCP-assigned address instead :superscript:`6.0.6`
         - Fixed an issue that caused Azure virtual images to disappear following Cloud sync under certain conditions :superscript:`6.0.6`
:Catalog: - Fixed an issue that prevented provisioning ARM template-based Blueprints as Catalog Items
           - Scale selections are now factored into the presented price estimate :superscript:`6.0.6`
           - When using the "Order Again" function of the |morpheus| Catalog, Input values shown in Typeahead fields are now rendered correctly :superscript:`6.0.6`
:Costing: - Fixed an issue that could cause certain hours in a month to be untracked and, thus, create undercharged invoices :superscript:`6.0.6`
:Forms: - Added quality of life improvements for Forms that ensured proper operation under certain Cloud-specific scenarios
         - Fixed disks not refreshing when changing Group or Cloud on Catalog Items created from Forms
:Google Cloud (GCP): - Sync connections to GCP Clouds no longer fail when the project name contains more than one special character or whitespace character :superscript:`6.0.6`
                  - The Cloud-Init setting is now enabled by default for GCP-synced public images and the same flag is no longer disabled for some images following a Cloud sync :superscript:`6.0.6`
:Image Builder: - Updated the Image Builder tool to send the boot script earlier in the provisioning process so that the boot script will work :superscript:`6.0.6`
:Instances: - Fixed an issue that could cause network interfaces to be removed during reconfigure under certain conditions :superscript:`6.0.6`
:Morpheus IP Pools: - When IP Pools are shared to Subtenant(s) from the |mastertenant|, Subtenant Users are no longer able to access the Pool detail page via direct entry of the URL :superscript:`6.0.6`
:NSX-T: - Adding host records to NSX-T-type IP pools through |morpheus| UI or API no longer results in a 500 error :superscript:`6.0.6`
:NetScaler: - When creating a NetScaler load balancer at provision time and selecting HTTPS protocol, the protocol is set correctly rather than the load balancer showing HTTP in NetScaler :superscript:`6.0.6`
:Network: - Search domains added to the network are now correctly appended to the search line in the /etc/resolv.conf file on the Linux VM over guest customization :superscript:`6.0.6`
:Nutanix Prism Central: - PTR registration when provisioning using the Infoblox integration is now working properly :superscript:`6.0.6`
                  - When provisioning with a static IP address to Nutanix Prism Central Clouds, the IP is now set properly on the VM :superscript:`6.0.6`
:OpenStack:  - When adding a custom Price Set to a pre-existing Service Plan, the original Price Set is no longer replaced after the nightly sync :superscript:`6.0.6`
             - When reconfiguring OpenStack VMs, the price shown in the reconfigure window now matches what is ultimately shown on the Instance detail page after the reconfigure is executed :superscript:`6.0.6`
:Plans and Pricing: - Fixed an issue that could allow max cores per socket set on the Service Plan to be exceeded :superscript:`6.0.6`
:PowerShell: - Fixed an issue that could cause the browser to hang or crash due to excessive memory utilization when executing some Powershell scripts which generated very large amounts of output :superscript:`6.0.6`
:Reports: - When "Infrastructure: Clouds" permission is set to "None" on both the Tenant and User Role, the Cloud Cost Usage and Instance Inventory Summary reports still generate properly now assuming that you have access to the specific Cloud on the Tenant Role :superscript:`6.0.6`
:ServiceNow: - ServiceNow CMDB records are now properly created for discovered Instances within configured Clouds even when the |morpheus| Catalog plugin is not installed on the ServiceNow instance :superscript:`6.0.6`
              - ServiceNow configuration items are now created following the Provisioning phase of a Provisioning Workflow to allow Post Provision-phase Tasks to update CIs, if necessary :superscript:`6.0.6`
              - ServiceNow test incidents are no longer sent when ServiceNow monitoring is disabled :superscript:`6.0.6`
              - When ``cmdb_ci_server" is set as the default business class for a ServiceNow integration, a new record is created for each Instance provisioned rather than the existing record being replaced :superscript:`6.0.6`
:Settings: - Added an Incident Retainment setting under Appliance within global settings (|AdmSet|). This provides control over the longevity of monitoring incident records in the database which can help prevent appliance performance problems :superscript:`6.0.6`
:Terraform: - When adding a new Terraform App in |morpheus| and importing an existing state file, the initial ``terraform plan`` runs will no longer show that new resources would be created if that is not the case :superscript:`6.0.6`
             - When the ``terraform destroy`` command fails, the Instance is no longer removed from |morpheus| :superscript:`6.0.6`
:Workflows: - The ``user`` variable is now accessible within Teardown-phase Tasks for non-VM based Instance Types (XaaS and potentially Terraform or CloudFormation, etc) :superscript:`6.0.6`
:XaaS: - Failed Tasks in the Teardown phase of Provisioning Workflows set on XaaS Instances will now prevent the delete action from taking place as is already the case for non-XaaS Instances :superscript:`6.0.6`
        - Post Provision-phase Tasks now run as expected for XaaS Instances :superscript:`6.0.6`


Appliance & Agent Updates
=========================

:Appliance: - Java has been upgraded to 11.0.20 :superscript:`6.0.6`
             - MySQL upgraded to 5.7.43 :superscript:`6.0.6`
             - Tomcat upgraded to 9.0.76 :superscript:`6.0.6`
