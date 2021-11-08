.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added BGP configuration for Tier-0 routers via |morpheus| API and CLI :superscript:`5.3.4`
            - Added static route configuration for Tier-0 and Tier-1 routers via |morpheus| API and CLI :superscript:`5.3.4`
            - Improved NSX-T Tier-0 and Tier-1 Gateway consiguration via |morpheus| API :superscript:`5.3.4`
:Azure: - Updated Azure costing sync to account for Azure CSP customers using Azure Plan :superscript:`5.3.4`
:NSX: - Added ability to specify a member group to be associated with NSX-T load balancer server pools :superscript:`5.3.4`
      - Added capability to create and manage BGP neighbors for NSX-T routers :superscript:`5.3.4`
      - Fixed NSX-T distributed firewall missing source and destination types in Morpheus UI :superscript:`5.3.4`
:Security: - jknack/handlebars.java updated to 4.3.0 (CVE-2021-23369) :superscript:`5.3.4`
:VMware: - Folder selection is now mandatory during provisioning. Previously this was optional but could cause issues if a folder was not selected and users were provisioning outside their intended folders :superscript:`5.3.4`


Fixes
=====

:Amazon: - Disks added to VMs after provisioning are now deleted along with the VM at teardown time. Previously disks added later would remain :superscript:`5.3.4`
:Ansible: - Fixed an issue which caused Ansible integrations not to inherit the "No Proxy" configuration in global Appliance Settings (Administration > Settings > Appliance) :superscript:`5.3.4`
:API & CLI: - Added additional prompts to the ``network-routers add`` CLI workflow to enable selection of Edge Clusters and/or Tier-0 Gateways for NSX-T Tier-1 and Tier-0 Gateways :superscript:`5.3.4`
            - Fixed an issue that caused GET calls for specific networks, network proxies, and network routers not to work properly for Subtenant users :superscript:`5.3.4`
            - Fixed an issue that prevented custom networks from being created through |morpheus| API :superscript:`5.3.4`
            - Resizing network interface counts via |morpheus| API no longer causes VMs to reboot under certain conditions :superscript:`5.3.4`
            - The ``clone`` API endpoint now accepts ``tag`` and ``label`` payloads correctly. Previously they needed to be issued using a legacy format which caused confusion :superscript:`5.3.4`
            - The content (script) of PowerShell Tasks is now displayed correctly when creating or viewing such Tasks in |morpheus| CLI :superscript:`5.3.4`
            - Users can now add Layouts to default Instance Types via |morpheus| API and CLI :superscript:`5.3.4`
            - When issuing a Tenant delete call to |morpheus| API, the ``removeResources`` flag is now ``true`` by default. Previously, this was ``false`` by default :superscript:`5.3.4`
            - When making a GET call for all Instances or for a specific Instance, |morpheus|-generated system tags are no longer returned :superscript:`5.3.4`
:Apps: - Corrected an issue that caused Instance counts on Apps to appear incorrectly to users which weren't the owner of the App :superscript:`5.3.4`
       - When provisioning multi-tier Apps, environment variables are now set at a consistent time following App completion to ensure data accuracy :superscript:`5.3.4`
:Azure: - Fixed an issue that caused Instance or server details (plan, datastore, etc.) not to display corrected when reconfiguring an Instance or server that was previously converted to managed :superscript:`5.3.4`
        - The Edit Instance dialog can now be used to change the Group on a SQL Server DBaaS on Azure Instance :superscript:`5.3.4`
        - When provisioning to Azure using ARM Spec Templates, a "pending" string is no longer temporarily appended to server names during the provisioning process which caused DNS issues in some cases :superscript:`5.3.4`
:Backups: - Backup "Total Size" is no longer reported incorrectly in the UI when it exceeds 1 TB in size :superscript:`5.3.4`
          - Execute timings for scheduled backup jobs now update immediately in the UI on saving changes to the schedule. Previously the UI change could take a short time which caused confusion :superscript:`5.3.4`
:Chef: - Improved validation on the Create Chef Integration modal. The validity of the Chef server URL is now verified before saving the new integration :superscript:`5.3.4`
       - Improved validation on the success of Chef bootstrap task execution :superscript:`5.3.4`
:Clone: - Fixed an issue that could cause NICs to be reordered during the clone process which created connectivity issues :superscript:`5.3.4`
        - Removed "autoCluster" as Datastore selection when a different Cloud is selected as target Cloud for the new clone. This is because the datastore might not be reachable from a different destination cloud and cause provisioning failures :superscript:`5.3.4`
:Costing: - Fix issue where duplicate invoice records were generated for first occurrence of an invoice in a period :superscript:`5.3.4`
:File Templates: - Fixed location shown in node type displaying old value after updating the paths of associated file template :superscript:`5.3.4`
:Github: - Github integrations now sync correctly for appliances configured to route traffic through a global proxy :superscript:`5.3.4`
:Guidance: - Corrected an issue that would cause incorrect guidance to be given for Azure Instances :superscript:`5.3.4`
:Hosts: - Under certain conditions, the platform for discovered servers could be reported incorrectly. This has been fixed :superscript:`5.3.4`
:Identity Sources: - Fixed an issue that caused errors to be thrown when configuring a logout redirect URL for Azure AD SSO identity source integrations :superscript:`5.3.4`
:Instances: - Fixed an issue that caused details not to be loaded in properly to a reconfigure modal after converting a discovered VM with multiple disks to managed :superscript:`5.3.4`
            - Fixed an issue that caused errors to appear and made it impossible to add a new node to an Instance which had all of its nodes removed :superscript:`5.3.4`
            - Fixed an issue where networks would not be set correctly on a node added to an Instance when existing nodes had multiple networks, including IPAM networks :superscript:`5.3.4`
            - When provisioning multi-NIC Instances, it could take time for additional network interface information to populate in |morpheus|. This has been corrected :superscript:`5.3.4`
:Invoices: - Invoices are no longer being created for workloads which were awaiting provisioning approval, then cancelled or deleted :superscript:`5.3.4`
:KVM: - Fixed an issue which would cause the Instance wizard not to advance under specific configurations due to missing datastore information even when a datastore was selected :superscript:`5.3.4`
:Localization: - Missing string definitions added :superscript:`5.3.4`
:Network: - Fixed an issue that could cause the first network interface in the list to be automatically set as the primary during Cloud sync, even if the user had set another to be primary :superscript:`5.3.4`
:Node Types: - AMI selection field for Amazon Node Types is now a Typeahead field. Previously, in environments with access to very large numbers of AMIs, it would not be possible to edit the AMI selection in certain scenarios due to the size of the dropdown menu :superscript:`5.3.4`
:NSX: - Fix NSX-T sync issue where segments (networks) were being disassociated from sub-tenant zones and re-associated to master tenant zones :superscript:`5.3.4`
      - Fixed an issue causing duplicate NSX-T networks to by synced into |morpheus| under certain conditions. Once the update is applied the duplicate networks will take approximately ten minutes to be removed :superscript:`5.3.4`
      - Fixed issue with NSX-V logical router DHCP relay creation :superscript:`5.3.45.2.11`
      - Fixed network ip pools not listing when creating NSX-T networks/segments :superscript:`5.2.115.3.4`
      - Improved validation errors in UI when adding or editing an invalid uplink interface for a DLR or Edge Router :superscript:`5.3.4`
      - The server address field is no longer a required field when creating NSX-T DHCP servers :superscript:`5.3.4`
:OpenStack: - When Primary Tenant admins set an OpenStack Cloud and associated load balancer to be private to a Tenant, Users in the Tenant can now view load balancer detail pages :superscript:`5.3.4`
:Option Lists: - Added form validation so that invalid Option Lists could not be saved :superscript:`5.3.4`
               - Validation added for JSON and CSV-based manual Option Lists. Previously these forms would accept invalid JSON and CSV which would cause the Option List not to function correctly :superscript:`5.3.4`
:Oracle Cloud: - Fixed an issue that caused Oracle Cloud Flex Plan workload costs to report as significantly more expensive than they should have :superscript:`5.3.4`
               - Increased timeout on Oracle Cloud agent install to 1 Hour to account for long Windows startup times :superscript:`5.3.4`
:Plans & Pricing: - Corrected some default plans which showed incorrect resource counts (core, etc.) in plan descriptions when compared to the same plan in the target cloud :superscript:`5.3.4`
                  - Improved UI warning messages and handling when attempting to reconfigure an Instance beyond the custom range of core, memory, or storage configured on its plan :superscript:`5.3.4`
:Policies: - Added more validation on Policy creation. Policies now require a unique name and additional validation has been added to ensure uniqueness of the type, config and scope combination :superscript:`5.3.4`
           - Policies scoped to a Tenant are no longer removed if the Tenant is deleted. The Policy now remains in |morpheus| but is no longer scoped to the non-existent Tenant :superscript:`5.3.4`
:PowerDNS: - Fixed an issue that limited the PowerDNS Zones List Page to just the first 25 zone entries :superscript:`5.3.4`
:Provisioning: - Changes made to Cloud filtering during provisioning which will prevent users from being able to select Clouds which should not be applicable to the selected Instance Type and/or Group in certain cases :superscript:`5.3.4`
               - Corrected an issue that caused Inputs (Option Types) not to appear correctly when provisioning from an ARM-based Spec Template which was sourced from an integrated repository :superscript:`5.3.4`
:Reports: - Corrected an issue that could cause inaccurate cost values to be shown on the Tenant Cost Report :superscript:`5.3.4`
:Reports: - Fixed an issue that caused mismatched columns when opting for CSV output of the Cloud Migration Report :superscript:`5.3.4`
:Security: - Includes important security fixes which were first corrected in patch releases for 5.2.11 (v5.2.11-2) and 5.3.3 (v5.3.3-2) :superscript:`5.3.4`
           - Percent symbols (%) are now escaped correctly in usernames when logging in :superscript:`5.3.4`
           - Users can no longer view Instance Types owned by other Tenants by adding arbitrary Instance Type ID values to request URLs :superscript:`5.3.4`
           - Users with "Infrastructure: Network Integrations" permissions set to "None" no longer see the Integrations tab in Infrastructure > Networks :superscript:`5.3.4`
:ServiceNow: - Fixed an issue causing some ServiceNow traffic not to go through a configured global proxy :superscript:`5.3.4`
:Storage: - After reconfiguring an Instance to alter storage details, this information is now refreshed live on the Storage tab without requiring a page refresh :superscript:`5.3.4`
:Tags: - Fixed an issue which caused tags not to be set when provisioning to Azure Stack Clouds :superscript:`5.3.4`
:Tenants: - Fixed Tenant deletion issues caused by network pool associations not being automatically removed :superscript:`5.3.4`
:UI: - Advanced table view added to Zone Records List Page (Infrastructure > Networks > Integrations > selected integration > Zone Records tab) :superscript:`5.3.4`
     - After completing the process of resetting a forgotten password, Subtenant users are redirected to the Subtenant login page rather than the login page for the Primary Tenant :superscript:`5.3.4`
     - The "Location" column in the VMs table on the Instance Detail Page has been renamed "Address(es)" to avoid potential confusion with other Location properties :superscript:`5.3.4`
     - When restarting a virtual machine from the Instance detail page (Provisioning > Instances), the confirmation message now refers to a "node" rather than a "container" to prevent confusion :superscript:`5.3.4`
:vCloud Director: - Fixed agent not installing when ICMP is blocked :superscript:`5.3.4`
                  - Fixed an issue that could cause Kubernetes clusters not to honor their associated custom plans in some cases when provisioned to vCD :superscript:`5.3.4`
                  - Fixed issue with header parsing when connecting to vCD through load balancer :superscript:`5.3.4`
                  - The Resources tab of a VCD cloud detail page now is properly displaying vApp names in the Pools section :superscript:`5.3.4`
:Virtual Images: - Uploading OVA image files to NSFv3 file share buckets will no longer stop after the first file under certain conditions, such as when they contain multiple TAR files :superscript:`5.3.4`
:VMware: - Fixed an issue that prevented VMware Clouds from being deleted in specific cases :superscript:`5.3.4`
         - Fixed failed backups and snapshots remaining in "in progress" state :superscript:`5.3.4`
         - When discovering VMs on VMware, for example, we are now setting the OS Information to a specific value such as CentOS 64-bit, CentOS 8 64-bit, or Windows Server 2016, as appropriate :superscript:`5.3.4`
         - When provisioning an MKS cluster into VMware, guest customization is always used when IP pools are being used rather than DHCP to avoid issues :superscript:`5.3.4`
:Wiki: - Wiki notes are no longer lost when an Instance is assigned to a different Tenant :superscript:`5.3.4`
:Workflows: - Attempting to delete a Workflow which is associated with a Layout, now surfaces a helpful UI warning that the action can't be completed rather than throwing a 500 error :superscript:`5.3.4`
            - Fixed an issue that could cause errors to be thrown when running a Workflow containing WinRM Tasks with an execute context of "None" :superscript:`5.3.4`
            - Fixed an issue which prevented some Inputs from being reordered if additional Inputs were added later after the Workflow was initially saved :superscript:`5.3.4`
            - The failure of a post-provisioning workflow task is now reflected in the instance state (warning) and workflow and task states (error) :superscript:`5.3.4`


Appliance & Agent Updates
=========================

:Appliance: - `morpheus-playbooks` configuration updated to use Cloudfront instead of s3 bucket url :superscript:`5.3.4`
            - Fixed upgrade issue with SLES 12/15 where morpheus-ctl command was removed during rpm post removal. Note this does not fix previous rpm post removal scripts and ``rpm -U ... --force`` will still need to be ran when upgrading to 5.2.12 on SLES 12/15. :superscript:`5.3.4`
            - Java upgraded to 8u312-b07 :superscript:`5.3.4`
            - MySQL upgraded to 5.7.35 :superscript:`5.3.4`
            - Nginx upgraded to 1.20.1 :superscript:`5.3.4`
            - RabbitMQ upgraded to 3.9.8 :superscript:`5.3.4`
            - Tomcat upgraded to 9.0.54 :superscript:`5.3.4`
:Agent Packages: - Node & VM Node package verison updated to |nodePackageVer|
                 - |nodePackageVer| java updated to 8u312-b07
            
            
            