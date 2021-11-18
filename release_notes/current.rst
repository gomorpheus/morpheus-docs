.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

.. include:: /release_notes/navChanges.rst

|

New Features
============

:API & CLI: - Added BGP configuration for Tier-0 routers via |morpheus| API and CLI :superscript:`5.2.12`
             - Added static route configuration for Tier-0 and Tier-1 routers via |morpheus| API and CLI :superscript:`5.2.12`
             - Improved NSX-T Tier-0 and Tier-1 Gateway consiguration via |morpheus| API :superscript:`5.2.12`
             - Snapshot support added to billing API
             - Virtual Image support added to billing API
:Amazon: - EKS now supported for all regions with AWS EKS services. Added ``us-west-1``,``ap-east-1``,``ap-south-1``,``ap-northeast-3``,``ca-central-1``,``eu-south-1``,``me-south-1``,``sa-east-1``,``us-gov-east-1``&``us-gov-west-1``
:Azure: - Updated Azure costing sync to account for Azure CSP customers using Azure Plan :superscript:`5.2.12`
         - When using Azure global clouds, available storage accounts are now filtered by the location of the resource group. Previously this list was unfiltered and provisioning could fail if the resource group and storage account were in different locations
:Clusters: - Add Cluster and Add Host Wizards now show pricing information on the confirmation page of the wizard, as the Add Instance Wizard does
:Dashboard: - Added performance improvements for |morpheus| Dashboard (UI and calls to the Dashboard API) in specific scenarios where |morpheus| is managing a very high number of workloads :superscript:`5.2.11`
:Inputs: - Added new Text Area Input-type. Users can determine the size of the text area by specifying the number of rows
:Morpheus Worker: - The |morpheus| worker can now also be used as a proxy server between the |morpheus| appliance and on-prem Cloud hosts. See the `install guide <https://docs.morpheusdata.com/en/latest/administration/integrations/integrations.html#distributed-workers>`_ for more details
:NSX: - Added UI tab for NSX-T DHCP management (Infrastructure > Networks > Integrations > Selected NSX-T integration > DHCP tab) :superscript:`5.2.11`
       - Added ability to specify a member group to be associated with NSX-T load balancer server pools :superscript:`5.2.12`
       - Added capability to create and manage BGP neighbors for NSX-T routers :superscript:`5.2.12`
       - Added support for configuring DHCP on NSX-T routers. When adding or editing an NSX-T router (Infrastructure > Networks > Routers > Selected NSX-T router > EDIT button), expand the IP address management section and configure DHCP options :superscript:`5.2.11`
       - Fixed NSX-T distributed firewall missing source and destination types in Morpheus UI :superscript:`5.2.12`
       - Source and destination IP addresses for distributed firewall rules (of any category) are now synced back to |morpheus| :superscript:`5.2.11`
       - Sync, create and manage NSX-T DHCP relays :superscript:`5.2.11`
       - Sync, create and manage NSX-T DHCP servers :superscript:`5.2.11`
:Plugins: - Added ability to create network-type plugins for performing CRUD operations on networks and subnets. See the `Morpheus Developer Portal <https://developer.morpheusdata.com/>`_ for more information.
           - Added plugin support for Delete Approval policies
           - Added plugin support for Reconfigure Approval Policies
           - Added plugin support for associating virtual images with node types
:Policies: - Added approve delete policies, these can be tied into internal (Morpheus) approvals or approvals through a ServiceNow integration
            - Added reconfigure approval policies, which tie into either internal (Morpheus) approvals or approvals through a ServiceNow integration
:Reports: - Added Tag Compliance Inventory report to show VMs which are outside of existing tag compliance policies
:Security: - jknack/handlebars.java updated to 4.3.0 (CVE-2021-23369) :superscript:`5.2.12`
:Service Catalog: - Self-Service Catalog provisioning is now available from the standard Persona (Provisioning > Catalog) in addition to the dedicated Persona it has always existed in.
:ServiceNow: - CMDB sync times significantly improved
              - ServiceNow RITM and CI records are now updated even when provisioning fails
              - ``object_id`` now set correctly for discovered servers so that matches can be made rather than duplicates when discovery is enabled both in Morpheus and ServiceNow
:UI: - After receiving a password reset email and submitting the form to reset the password, the user is redirected to the login screen rather than logged into the product. This ensures two-factor authentication is still honored if set. :superscript:`5.2.11`
      - Errors are now surfaced into the History tab of the Instance detail page if issues occur when taking Snapshots in supported Clouds :superscript:`5.2.11`
      - Localization features added, including a global language settings and override capabilities for individual users
      - Reorganized main application menu. The Library, which was previously under Provisioning, is now a top-level section. Service Catalog provisioning can now be done in the Standard Persona in addition to the Service Catalog Persona. Many more smaller changes
:VMware: - The root Folder (``/``) is now exposed in VMware Cloud Resources sections, allowing the same configuration and access control as sub-folders. Previously configuration and access settings were only exposed for sub-folders :superscript:`5.2.12`


Fixes
=====

:API & CLI: - API calls to get all servers or to get a specific server no longer contain duplicate zone or plan keys
             - Added additional prompts to the ``network-routers add`` CLI workflow to enable selection of Edge Clusters and/or Tier-0 Gateways for NSX-T Tier-1 and Tier-0 Gateways :superscript:`5.2.12`
             - Fixed an issue that caused GET calls for specific networks, network proxies, and network routers not to work properly for Subtenant users :superscript:`5.2.12`
             - Fixed an issue that prevented custom networks from being created through |morpheus| API :superscript:`5.2.12`
             - Message of the Day (MOTD)-type Policies are now returned when issuing GET requests for policies :superscript:`5.2.11`
             - Resizing network interface counts via |morpheus| API no longer causes VMs to reboot under certain conditions :superscript:`5.2.12`
             - The ``clone`` API endpoint now accepts ``tag`` and ``label`` payloads correctly. Previously they needed to be issued using a legacy format which caused confusion :superscript:`5.2.12`
             - The content (script) of PowerShell Tasks is now displayed correctly when creating or viewing such Tasks in |morpheus| CLI :superscript:`5.2.12`
             - Users can now add Layouts to default Instance Types via |morpheus| API and CLI :superscript:`5.2.12`
             - When issuing GET calls for specific Instances, controller information is now populated in the response :superscript:`5.2.11`
             - When issuing a Tenant delete call to |morpheus| API, the ``removeResources`` flag is now ``true`` by default. Previously, this was ``false`` by default :superscript:`5.2.12`
             - When making a GET call for all Instances or for a specific Instance, |morpheus|-generated system tags are no longer returned :superscript:`5.2.12`
             - When provisioning an Instance or getting a specific Instance via API, the ``labels`` and ``tags`` objects are now returned even when there are no labels or tags
:Amazon: - Amazon plans are now synced rather than seeded into the product by |morpheus|. This should ensure any currently-valid plan is available
          - Disks added to VMs after provisioning are now deleted along with the VM at teardown time. Previously disks added later would remain :superscript:`5.2.12`
          - Updates made to base Ubuntu 18 image for AWS :superscript:`5.2.11`
:Ansible: - Fixed an issue which caused Ansible integrations not to inherit the "No Proxy" configuration in global Appliance Settings (Administration > Settings > Appliance) :superscript:`5.2.12`
:Apps: - Corrected an issue that caused Instance counts on Apps to appear incorrectly to users which weren't the owner of the App :superscript:`5.2.12`
        - Fixed an issue where App Instances would default to one CPU core at provision time rather than the default number of CPU cores indicated on the Blueprint :superscript:`5.2.11`
        - When provisioning multi-tier Apps, environment variables are now set at a consistent time following App completion to ensure data accuracy :superscript:`5.2.12`
:Automation: - Reassigning an Instance from the Primary Tenant to a Subtenant will no longer break Ansible Task execution in certain cases :superscript:`5.2.11`
:Azure Stack: - Removed the ability to select certain unsupported disk types from the provisioning wizard. Selecting these types would cause the provisioning to fail if the user did not know those types were not allowed :superscript:`5.2.11`
:Azure: - Adding resource pools to Azure Clouds which are scoped to all regions now works correctly
         - Fixed an issue that caused Instance or server details (plan, datastore, etc.) not to display corrected when reconfiguring an Instance or server that was previously converted to managed :superscript:`5.2.12`
         - The Edit Instance dialog can now be used to change the Group on a SQL Server DBaaS on Azure Instance :superscript:`5.2.12`
         - When provisioning to Azure using ARM Spec Templates, a "pending" string is no longer temporarily appended to server names during the provisioning process which caused DNS issues in some cases :superscript:`5.2.12`
:BIND DNS: - Improved form validation when creating a BIND DNS integration. Previously 500 errors would be thrown or some fields would disappear when attempting to submit the form
:Backups: - Backup "Total Size" is no longer reported incorrectly in the UI when it exceeds 1 TB in size :superscript:`5.2.12`
           - Execute timings for scheduled backup jobs now update immediately in the UI on saving changes to the schedule. Previously the UI change could take a short time which caused confusion :superscript:`5.2.12`
:Blueprints: - The expand and contract button for configuration options now works correctly. Previously it defaulted to the expanded state and could not be contracted :superscript:`5.2.11`
:Buckets: - Fixed an issue that could cause non-Amazon S3 buckets to fail on creation when specific string sequences were contained in the endpoint URL :superscript:`5.2.11`
:Catalog: - Removed some default ElasticSearch Layouts which contained outdated versions and failed provisioning under certain scenarios
:Chef: - Improved validation on the Create Chef Integration modal. The validity of the Chef server URL is now verified before saving the new integration :superscript:`5.2.12`
        - Improved validation on the success of Chef bootstrap task execution :superscript:`5.2.12`
:Clone: - Fixed an issue that could cause NICs to be reordered during the clone process which created connectivity issues :superscript:`5.2.12`
         - Removed "autoCluster" as Datastore selection when a different Cloud is selected as target Cloud for the new clone. This is because the datastore might not be reachable from a different destination cloud and cause provisioning failures :superscript:`5.2.12`
:Costing: - Fix issue where duplicate invoice records were generated for first occurrence of an invoice in a period :superscript:`5.2.12`
:ESXi: - The number of CPU cores on discovered ESXi VMs is now synced correctly :superscript:`5.2.11`
:File Templates: - Fixed location shown in node type displaying old value after updating the paths of associated file template :superscript:`5.2.12`
:Github: - Github integrations now sync correctly for appliances configured to route traffic through a global proxy :superscript:`5.2.12`
:Groups: - Fixed an issue where Groups with no assigned Clouds would be able to see managed and discovered VMs in any Cloud :superscript:`5.2.11`
:Guidance: - Corrected an issue that would cause incorrect guidance to be given for Azure Instances :superscript:`5.2.12`
:Hosts: - Under certain conditions, the platform for discovered servers could be reported incorrectly. This has been fixed :superscript:`5.2.12`
:Identity Sources: - Fixed an issue that caused errors to be thrown when configuring a logout redirect URL for Azure AD SSO identity source integrations :superscript:`5.2.12`
:Instances: - Fixed an issue that caused details not to be loaded in properly to a reconfigure modal after converting a discovered VM with multiple disks to managed :superscript:`5.2.12`
             - Fixed an issue that caused errors to appear and made it impossible to add a new node to an Instance which had all of its nodes removed :superscript:`5.2.12`
             - Fixed an issue where networks would not be set correctly on a node added to an Instance when existing nodes had multiple networks, including IPAM networks :superscript:`5.2.12`
             - When provisioning multi-NIC Instances, it could take time for additional network interface information to populate in |morpheus|. This has been corrected :superscript:`5.2.12`
:Invoices: - Invoices are no longer being created for workloads which were awaiting provisioning approval, then cancelled or deleted :superscript:`5.2.12`
:KVM: - Fixed an issue which would cause the Instance wizard not to advance under specific configurations due to missing datastore information even when a datastore was selected :superscript:`5.2.12`
:Kubernetes: - Fixed issues with AKS and EKS Create Cluster modals, including field marked required having no validation
              - ``useGuestCustomization`` flag now set to ``true`` when provisioning Kubernetes hosts into vCD using IP Pools, even when FORCE GUEST CUSTOMIZATION is unchecked, to ensure proper provisioning
:Localization: - Missing string definitions added :superscript:`5.2.12`
:NSX-T: - Certain errors are no longer surfaced into the logs when NSX-T integrations are refreshed :superscript:`5.2.11`
         - Certain errors are no longer triggered when NSX-T integrations are refreshed :superscript:`5.2.11`
         - Created NSX-T load balancer profiles are now selectable from virtual servers :superscript:`5.2.11`
:NSX: - Fix NSX-T sync issue where segments (networks) were being disassociated from sub-tenant zones and re-associated to master tenant zones :superscript:`5.2.12`
       - Fixed an issue causing duplicate NSX-T networks to by synced into |morpheus| under certain conditions. Once the update is applied the duplicate networks will take approximately ten minutes to be removed :superscript:`5.2.12`
       - Fixed issue with NSX-V logical router DHCP relay creation :superscript:`5.2.125.2.11`
       - Fixed network ip pools not listing when creating NSX-T networks/segments :superscript:`5.2.125.2.11`
       - Improved validation errors in UI when adding or editing an invalid uplink interface for a DLR or Edge Router :superscript:`5.2.12`
       - The server address field is no longer a required field when creating NSX-T DHCP servers :superscript:`5.2.12`
:Network: - Added validation to API calls to create or edit network proxies to ensure names are unique :superscript:`5.2.11`
           - Fixed an issue causing network groups not to be handled properly on Instance or VM reconfigure :superscript:`5.2.11`
           - Fixed an issue that caused Tenant permissions not to be set up properly for subnets in Subtenants :superscript:`5.2.11`
           - Fixed an issue that caused old IP addresses not to be freed up in some scenarios when a new network and IP pool was selected on Instance reconfigure :superscript:`5.2.11`
           - Fixed an issue that could cause NICs to be relabeled when adding a network to an Instance or server via reconfigure :superscript:`5.2.11`
           - Fixed an issue that could cause the first network interface in the list to be automatically set as the primary during Cloud sync, even if the user had set another to be primary :superscript:`5.2.12`
:Node Types: - AMI selection field for Amazon Node Types is now a Typeahead field. Previously, in environments with access to very large numbers of AMIs, it would not be possible to edit the AMI selection in certain scenarios due to the size of the dropdown menu :superscript:`5.2.12`
:Nutanix: - Improved process for cleaning up IP pools when Nutanix clouds are deleted :superscript:`5.2.11`
:OpenStack: - When Primary Tenant admins set an OpenStack Cloud and associated load balancer to be private to a Tenant, Users in the Tenant can now view load balancer detail pages :superscript:`5.2.12`
             - When reconfiguring OpenStack Instances with multiple disks, disks no longer change size without user input in certain scenarios :superscript:`5.2.11`
:Option Lists: - Added form validation so that invalid Option Lists could not be saved :superscript:`5.2.12`
                - Morpheus user objects and object attributes are now accessible in LDAP-type Option Lists :superscript:`5.2.11`
                - Validation added for JSON and CSV-based manual Option Lists. Previously these forms would accept invalid JSON and CSV which would cause the Option List not to function correctly :superscript:`5.2.12`
:Oracle Cloud: - Fixed an issue that caused Oracle Cloud Flex Plan workload costs to report as significantly more expensive than they should have :superscript:`5.2.12`
                - Fixed an issue that could cause Morpheus Agent to not be installed on Windows boxes in Oracle cloud :superscript:`5.2.11`
                - Increased timeout on Oracle Cloud agent install to 1 Hour to account for long Windows startup times :superscript:`5.2.12`
:Plans & Pricing: - Corrected an issue that caused Plans to appear differently when reconfiguring from the server detail page vs the Instance detail page :superscript:`5.2.11`
                  - Corrected some default plans which showed incorrect resource counts (core, etc.) in plan descriptions when compared to the same plan in the target cloud :superscript:`5.2.12`
                  - Improved UI warning messages and handling when attempting to reconfigure an Instance beyond the custom range of core, memory, or storage configured on its plan :superscript:`5.2.12`
:Policies: - Added more validation on Policy creation. Policies now require a unique name and additional validation has been added to ensure uniqueness of the type, config and scope combination :superscript:`5.2.12`
            - Max Cores Policies now include cores in the master node in the total cores count. Previously only worker node cores were counted toward the policy
            - Policies scoped to a Tenant are no longer removed if the Tenant is deleted. The Policy now remains in |morpheus| but is no longer scoped to the non-existent Tenant :superscript:`5.2.12`
:PowerDNS: - Fixed an issue that limited the PowerDNS Zones List Page to just the first 25 zone entries :superscript:`5.2.12`
:Provisioning: - Changes made to Cloud filtering during provisioning which will prevent users from being able to select Clouds which should not be applicable to the selected Instance Type and/or Group in certain cases :superscript:`5.2.12`
                - Corrected an issue that caused Inputs (Option Types) not to appear correctly when provisioning from an ARM-based Spec Template which was sourced from an integrated repository :superscript:`5.2.12`
                - Fixed issue with $sequence variable reiteration on 35 when using copies and "Reuse Naming Sequence Numbers" is enabled. :superscript:`5.2.11`
:Proxies: - Fixed an issue preventing proxies from being set correctly on SLES and OpenSUSE :superscript:`5.2.11`
:Reports: - Corrected an issue that could cause inaccurate cost values to be shown on the Tenant Cost Report :superscript:`5.2.12`
           - Fixed an issue that caused mismatched columns when opting for CSV output of the Cloud Migration Report :superscript:`5.2.12`
           - Fixed an issue where Reports or Analytics dashboards could show clouds as having more discovered VMs than they would actually show from the Cloud detail page :superscript:`5.2.11`
:Security: - Hid passwords to some Morpheus-owned service accounts (Twilio, Postmark, etc.) which were shared previously in ``application.groovy`` but are no longer needed by customers :superscript:`5.2.11`
            - Includes important security fixes which were first corrected in patch releases for 5.2.11 (v5.2.11-2) and 5.3.3 (v5.3.3-2) :superscript:`5.2.12`
            - Percent symbols (%) are now escaped correctly in usernames when logging in :superscript:`5.2.12`
            - Subtenant users who do not have access to private Primary Tenant networks can no longer see network information by manually adding network ID (zoneId) filters to URLs
            - The Tenant name and database ID are no longer shown in the return payload when sending a POST request to initiate a new user session :superscript:`5.2.11`
            - Users can no longer view Instance Types owned by other Tenants by adding arbitrary Instance Type ID values to request URLs :superscript:`5.2.12`
            - Users with "Infrastructure: Network Integrations" permissions set to "None" no longer see the Integrations tab in Infrastructure > Networks :superscript:`5.2.12`
:Service Catalog: - Fixed an issue that could cause Inputs to appear in a different order than they are set on the Catalog Item configuration
                  - Fixed an issue which could cause errors to be thrown when certain special characters were passed in an Input when provisioning a Service Catalog item
:ServiceNow: - Cleaned up some CMDB sync-related errors that were appearing in logs after ServiceNow sync
              - Fixed an issue causing some ServiceNow traffic not to go through a configured global proxy :superscript:`5.2.12`
              - Fixed an issue where the workflow indicated on a ServiceNow approval policy would not be honored during App provisioning :superscript:`5.2.11`
              - When exposing a Cloud to a new ServiceNow integration for provisioning which already has a CMDB server association, this association is no longer overwritten to set the new ServiceNow appliance as the Cloud's associated CMDB :superscript:`5.2.11`
:Storage: - After reconfiguring an Instance to alter storage details, this information is now refreshed live on the Storage tab without requiring a page refresh :superscript:`5.2.12`
:Tags: - Fixed an issue which caused tags not to be set when provisioning to Azure Stack Clouds :superscript:`5.2.12`
:Tasks: - Additional validation added when editing a Task to ensure the Task name is still unique prior to attempting to save changes. This change prevents 500 errors if the Task name has been editing to no longer be unique :superscript:`5.2.11`
         - Fixed an issue causing Ansible Tasks to fail and Morpheus UI to crash if the Ansible integration is connecting to Git over SSH during Task execution :superscript:`5.2.11`
         - Fixed an issue that caused remote-target Tasks to always fail under specific conditions :superscript:`5.2.11`
:Tenants: - Fixed Tenant deletion issues caused by network pool associations not being automatically removed :superscript:`5.2.12`
:UI: - Advanced table view added to Zone Records List Page (Infrastructure > Networks > Integrations > selected integration > Zone Records tab) :superscript:`5.2.12`
      - After completing the process of resetting a forgotten password, Subtenant users are redirected to the Subtenant login page rather than the login page for the Primary Tenant :superscript:`5.2.12`
      - Expand arrows now work correctly on the History page (Operations > Activity > History) and the look of the page has been updated to match other history and executions list pages
      - Fixed an issue where 500 errors could be thrown when editing global cloud-init settings (Administration > Settings > Provisioning) as a Subtenant administrator under certain conditions
      - The "Location" column in the VMs table on the Instance Detail Page has been renamed "Address(es)" to avoid potential confusion with other Location properties :superscript:`5.2.12`
      - When added or editing a Task, the SUDO checkbox is now consistently located under the CONTENT field. Previously, the placement of the checkbox was inconsistent
      - When restarting a virtual machine from the Instance detail page (Provisioning > Instances), the confirmation message now refers to a "node" rather than a "container" to prevent confusion :superscript:`5.2.12`
:VMware: - Fixed a sporadic issue where automatic downscale features could leave VMs in vCenter despite being removed from Morpheus :superscript:`5.2.11`
          - Fixed an issue that caused Instance snapshots not to be deleted properly :superscript:`5.2.11`
          - Fixed an issue that caused VMware clouds with only discovered VMs and Snapshots to not delete properly :superscript:`5.2.11`
          - Fixed an issue that could cause folder and resource pool selections not to be honored and the VM provisioned into the datacenter root in very specific scenarios :superscript:`5.2.11`
          - Fixed an issue that prevented VMware Clouds from being deleted in specific cases :superscript:`5.2.12`
          - Fixed an issue where Instances provisioned with multiple NICs could show incorrect MAC addresses and network assignment would fail
          - Fixed an issue where reconfiguring Instances with many disks could cause the individual disks to report incorrect sizes requiring the user to input them manually prior to executing the reconfigure :superscript:`5.2.11`
          - Fixed failed backups and snapshots remaining in "in progress" state :superscript:`5.2.12`
          - VMware Guest Customizations no longer override the keyboard layout to ``en-us`` which caused confusion for users who may have set the layout differently on their images
          - When discovering VMs on VMware, for example, we are now setting the OS Information to a specific value such as CentOS 64-bit, CentOS 8 64-bit, or Windows Server 2016, as appropriate :superscript:`5.2.12`
          - When provisioning an MKS cluster into VMware, guest customization is always used when IP pools are being used rather than DHCP to avoid issues :superscript:`5.2.12`
:Veeam: - Disabled Veeam backup integrations will no longer appear as backup targets in Instance and App provisioning wizards :superscript:`5.2.11`
:Virtual Images: - Fixed an issue where Virtual Image conversion processes would consistently fail under certain conditions :superscript:`5.2.11`
                  - Uploading OVA image files to NSFv3 file share buckets will no longer stop after the first file under certain conditions, such as when they contain multiple TAR files :superscript:`5.2.12`
:Whitelabel: - Fixed an issue that caused the filename of the primary Tenant logo image to appear in the Subtenant settings are even if the Subtenant had successfully applied their own logo image (which displays correctly) :superscript:`5.2.11`
:Wiki: - Wiki notes are no longer lost when an Instance is assigned to a different Tenant :superscript:`5.2.12`
:Workflows: - Attempting to delete a Workflow which is associated with a Layout, now surfaces a helpful UI warning that the action can't be completed rather than throwing a 500 error :superscript:`5.2.12`
             - Fixed an issue that could cause errors to be thrown when running a Workflow containing WinRM Tasks with an execute context of "None" :superscript:`5.2.12`
             - Fixed an issue which prevented some Inputs from being reordered if additional Inputs were added later after the Workflow was initially saved :superscript:`5.2.12`
             - The failure of a post-provisioning workflow task is now reflected in the instance state (warning) and workflow and task states (error) :superscript:`5.2.12`
:XenServer: - Fixed an issue where networks were not changed correctly when reconfiguring Xen Instances to change networks :superscript:`5.2.11`
:vCloud Director: - Corrected an issue that could cause vCD plan resizing to fail when updating the number of max cores and cores per socket :superscript:`5.2.11`
                  - Fixed agent not installing when ICMP is blocked :superscript:`5.2.12`
                  - Fixed an issue that could cause Kubernetes clusters not to honor their associated custom plans in some cases when provisioned to vCD :superscript:`5.2.12`
                  - Fixed an issue where editing Instances in vCD clouds would cause 500 errors (though the changes would be successfully saved) :superscript:`5.2.11`
                  - Fixed issue with header parsing when connecting to vCD through load balancer :superscript:`5.2.12`
                  - The Resources tab of a VCD cloud detail page now is properly displaying vApp names in the Pools section :superscript:`5.2.12`
                  - When reconfiguring vCD Instances with multiple disks, disks no longer change size without user input in certain scenarios :superscript:`5.2.11`


Appliance & Agent Updates
=========================

:Appliance: - Fixed upgrade issue with SLES 12/15 where morpheus-ctl command was removed during rpm post removal. Note this does not fix previous rpm post removal scripts and rpm -U ... --force will still need to be ran when upgrading to 5.2.12 on SLES 12/15. :superscript:`5.2.12`
             - Java upgraded to 8u312-b07 :superscript:`5.2.12`
             - MySQL upgraded to 5.7.35 :superscript:`5.2.12`
             - Nginx upgraded to 1.20.1 :superscript:`5.2.12`
             - Optimizations added to improve page load times :superscript:`5.2.11`
             - RabbitMQ upgraded to 3.9.8 :superscript:`5.2.12`
             - Tomcat upgraded to 9.0.54 :superscript:`5.2.12`
             - `morpheus-playbooks` configuration updated to use Cloudfront instead of s3 bucket url :superscript:`5.2.12`



.. ..
