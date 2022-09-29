.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. IMPORTANT:: |morpheus| 5.4.9+ adds the "Provisioning: State" Role permission. This permission determines access to the State tab for Terraform-backed Instances and is set to "None" by default. On upgrade from a version prior to 5.4.9, only System Admin users will be able to see the State tab for these Instances. For other users who should have this access, edit their Roles to include "Provisioning: State" permissions.

.. .. important::  Security: CVE-2022-35912: Morpheus v5.5.1-2 and v5.4.8-2 are now available in response to CVE-2022-35912, a Grails Framework remote code execution vulnerability. v5.5.1-2 and v5.4.8-2 include the Grails v5.1.9 update that mitigates the vulnerability. At this time, the Grails vulnerability is only confirmed for grails frameworks running on Java 8. Morpheus versions v5.4.4 and higher are on Java 11. Customers on morpheus v5.4.3 or earlier are highly advised to upgrade to at minimum v5.4.4 or higher, and out of an abundance of caution we recommend all customers upgrade to v5.5.1-2 or v5.4.8-2 in the event the vulnerability is found to be exploitable on Java 11.

.. warning:: Morpheus |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

New Features
============

:API & CLI: - Alert and Contact creation is now handled as expected through |morpheus| API and CLI when "Monitoring" Role permission is set to "User" level. :superscript:`5.4.15.5.2`
             - ``library-node-types`` add and update commands in |morpheus| CLI now properly support passing in ``evars`` and ``evars-json`` parameters. :superscript:`5.4.15.5.2`
:Alerts: - Users with "Monitoring" Role permission set to "User" can now only edit and delete contacts they've created and can only set alert rules for Apps/Instances they can access (even when selecting all). :superscript:`5.4.15.5.2`
:Amazon: - Jakarta (ap-southeast-3) and UAE (me-central-1) regions added for scoping Amazon AWS Clouds. :superscript:`5.5.2`
:Network: - Network labels (display names) are now editable from the Network tab of the Instance detail page. :superscript:`5.4.15.5.2`
:Puppet: - Support added for Puppet Agent 7. :superscript:`5.5.2`
:SCVMM: - Reconfiguring SCVMM Instances or VMs between dynamic and static service plans now includes improved memory validation. :superscript:`5.5.2`
:ServiceNow: - Added support for using a MID server during credential validation (in both single and multi-tenant installations) as well as support for using a MID server when fetching the auth token. :superscript:`5.4.15.5.2`
:Terraform: - Additional actions (Edit Inputs and Edit State) have been added under the Actions Menu on Terraform App and Terraform Instance detail pages. :superscript:`5.5.2`
             - Improved Terraform state file cleanup procedures after Terraform apply and delete actions are taken. :superscript:`5.4.15.5.2`
             - Support added for Terraform 1.2.x Apps and Instances. :superscript:`5.5.2`
             - Terraform Spec Templates can now reference directories of a Git repository and automatically onboard all files (including those in subdirectories) into the Spec Template similar to the way Terraform App Blueprints can already reference directories. Previously, Terraform Spec Templates needed to reference individual .tf files :superscript:`5.5.25.4.1`
             - Terraform variables flagged as "sensitive" are now masked from all areas of |morpheus| UI. Previously they were masked in provisioning wizards but could be revealed in some other places. :superscript:`5.5.2`
:Usage: - Calls to the billing API now includes a ``usages`` block in the return payload which includes resource information (CPU cores, memory, disk sizes, etc.) for the Instance/VM. This ensures users can access this information for accurate billing even in situations where the associated price types are resource-agnostic (such as "Everything" price types) :superscript:`5.4.15.5.2`


Fixes
=====

:API & CLI: - Fixed an issue that caused the ``price-sets list`` command in |morpheus| CLI to fail with an Unexpected Error. :superscript:`5.4.15.5.2`
             - Fixed an issue with the |morpheus| CLI ``clouds-add`` command not prompting for stored credential sets to authenticate the cloud integration. :superscript:`5.5.2`
:Amazon: - Fixed an issue related to |morpheus| Agent install when cloning Amazon Windows Instances. :superscript:`5.5.2`
          - Fixed an issue that caused duplicate backups to occur for AWS Instances when scheduled backups were run. :superscript:`5.5.2`
          - Fixed an issue that caused failed provisioning with AWS Aurora MySQL Instances. :superscript:`5.5.2`
          - Fixed an issue that caused the server.hostName property to be dropped after provisioning AWS Windows Instances. This could lead to configuration failures following provisioning. :superscript:`5.5.2`
:Automation Execute Schedules: - Fixed an issue that caused the Edit Execution Schedule modal window to hang if certain special cron expressions were used. :superscript:`5.5.2`
:Azure: - Additional refinements have been added to Azure costing computations to ensure complete accuracy in very specific situations. :superscript:`5.5.2`
         - Fixed an issue that could cause the backup and restore process for Azure workloads to set an incorrect storage type (Premium SSD, etc.). :superscript:`5.4.15.5.2`
         - Improved handling of situations where the Azure API returns bad or unexpected responses. :superscript:`5.5.2`
         - Private IP address changes on Azure workloads are now automatically synced back to |morpheus|. :superscript:`5.5.2`
         - Service Plans are now synced for locations of all resource groups and all other VM locations to prevent situations where VMs could be discovered and no Service Plan would be set. :superscript:`5.5.2`
:Bluecat: - When Bluecat IP Pool names are updated in the Bluecat console, the changed name will now sync back to |morpheus|. :superscript:`5.5.2`
:Blueprints: - Improved handling of situations when ARM Spec Templates are provisioned through the provisioning wizard without the adminPassword parameter set. :superscript:`5.5.2`
:Catalog: - Fixed an issue that prevented provisioning of ARM template-based App Blueprints from the Service Catalog if the item relied on password values being set as Inputs. :superscript:`5.4.15.4.95.5.2`
           - Workflow-based Service Catalog items no longer have potential to hang when multiple typeahead Input values are selected. :superscript:`5.5.2`
:CloudFormation: - Fixed an issue that caused CloudFormation Apps to fail deployment if they contained an EC2 Instance and had a UserData block. :superscript:`5.4.15.5.2`
:Clouds: - Minor cleanup has been conducted around the Change Cloud functionality to make record presentation more accurate and user-friendly. :superscript:`5.5.2`
          - The Cost History chart on Cloud Detail Pages now correctly plots small positive values higher than 0 along the Y axis. :superscript:`5.5.2`
:Code: - Fixed an issue that caused failures when creating a Task from a Code Detail Page (|ProCod|) that referred to a specific Git Tag reference. :superscript:`5.5.2`
:Costing: - Fixed an issue that could cause incorrect currency to be configured for server-type invoices and server invoice line items in specific contexts. :superscript:`5.4.15.5.2`
           - Fixed an issue that prevented configuration of GCP cloud costing using stored credentials (|InfTru|). :superscript:`5.4.15.5.2`
:Credentials: - Oauth credential sets can now be added (|InfTru|) even with very long tokens. :superscript:`5.5.2`
:Cypher: - When configuring Terraform App Blueprints, Users can no longer select and use tfvars files from Cypher if a Cypher Access Policy (|AdmPol|) restricts it from them. :superscript:`5.5.2`
:DNS: - Fixed an pagination record that prevented zone records from the 26th domain and higher from being available in DNS integrations. :superscript:`5.5.2`
:Inputs: - Fixed an issue that caused dependent Input fields not to reload in response to values added to the parent Input in certain contexts. :superscript:`5.4.15.5.2`
          - Password-type data in Inputs are no longer written to |morpheus| logs in plain text. :superscript:`5.5.2`
:Instances: - The Instance display name (the value you would change when editing an Instance and updating the Name field) is now used to set a console tab's window name and used when searching for an Instance by name. :superscript:`5.4.15.5.2`
:Kubernetes: - Fixed an issue that caused cluster stats not to be reported correctly on External (brownfield) Kubernetes clusters. :superscript:`5.5.25.4.1`
:Network: - Fixed an issue that preventing saving an IP Pool association at the time when a subnet was created requiring the user to edit the subnet once again to save the IP Pool association. :superscript:`5.5.2`
:OpenStack: - Fixed an issue that caused a UI error to be surfaced when editing an OpenStack network (though the edit would be successful and Instances would pick up the changes correctly). :superscript:`5.5.2`
             - OpenStack load balancer virtual server creation now works properly. :superscript:`5.4.15.5.2`
             - Price calculations for OpenStack Instances and Apps now correctly account for storage costs. :superscript:`5.5.2`
             - UI errors are now surfaced for situations when OpenStack load balancer creation cannot complete due to a load balancer quota having been reached. :superscript:`5.4.15.5.2`
:Plans and Pricing: - Fixed an issue that caused a random Service Plan to be accessed when users were attempting to edit an existing Virtual Image or VM Snapshot-type Service Plan. :superscript:`5.5.2`
                  - Fixed unexpected behavior related to prices (comma vs period-separated decimals) when mixed browser locales were used. :superscript:`5.5.2`
:Policies: - Fixed an issue that caused sequence numbers to be set incorrectly when used as part of a hostname policy. :superscript:`5.5.2`
:Provisioning: - Fixed an issue where |morpheus| Agent would fail to Install when workloads were provisioned to Clouds or Groups with apostrophe (') in the name. :superscript:`5.5.2`
                - When provisioning fails due to an error in a Provision-phase Workflow Task, the Instance History tab now shows a fail icon (red "x" symbol) in the provision phase history rather than a green success check icon. :superscript:`5.5.2`
:Puppet: - Improvements made to Puppet integration, including validation added when creating the integration, Puppet Tasks showing in the Instance history tab, Puppet Tasks and Puppet provisioning now include a version picker, and more. :superscript:`5.5.2`
:Reports: - Updated the UI description for the Virtual Machine Inventory report which was incorrect. :superscript:`5.4.15.5.2`
:Security: - Fixed a potential command injection vulnerability related to Ansible integrations. :superscript:`5.5.2`
            - Fixed an issue related to passwords being exposed in a specific log file. :superscript:`5.5.2`
            - The Azure access token used is no longer written into |morpheus| logs during teardown-phase actions. :superscript:`5.5.2`
:Settings: - |morpheus| will now generate email successfully when global SMTP settings are configured for an SMTP server that requires no authentication credentials. :superscript:`5.5.2`
:Terraform:  - Fixed an issue that appeared to show Terraform Apply State functionality would make unwanted changes (such as to an Instance name) though the change would not actually be made. :superscript:`5.5.2`
             - Fixed an issue that prevented saving edits to Terraform Spec Templates directly from the Spec Tab of a Terraform App Detail Page. :superscript:`5.5.2`
:UI: - An error is now surfaced when the user attempts to create a new Amazon Node Type without specifying an AMI. :superscript:`5.5.2`
      - Filters set on the Backups List Page now hold when navigating to the next page of results. :superscript:`5.5.2`
      - Fixed an issue that allowed the volumes information to overset the wizard window on the review tab of the New App Wizard. :superscript:`5.4.15.5.2`
      - Fixed an issue that caused widgets on the Instances list page to display incorrect Instance counts or incorrect running/stopped Instance counts. :superscript:`5.5.2`
      - The filters in the Type dropdown on the Backups List Page are now sorted in alphabetical order to make them easier to find. :superscript:`5.5.2`
:vCloud Director: - Fixed an issue that prevented the provisioning of library items based on uploaded OVFs which include NVRAM files. :superscript:`5.5.2`


Appliance & Agent Updates
=========================

