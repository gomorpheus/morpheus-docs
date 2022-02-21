.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate|

.. important:: |morpheus| Worker/Gateway v5.4.3 packages are now available. Existing Worker & Gateway nodes must be upgraded to v5.4.3 for compatibility with Morpheus v5.4.3 Appliances.

.. important:: Support for integrations with vCD 9 has ended with |morpheus| 5.4.3

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Expanded api & cli functionality for snapshots: Get a specific snapshot, revert to snapshot, create linked clone, delete a snapshot, & delete all snapshots on instance or container commands added.
             - The Instance Types list can now be filtered to list only featured Instance Types in |morpheus| API and CLI as is already possible in |morpheus| UI.
:Agent: - Added FIPS compliant el8 |morpheus| Agent node & vm-node packages. Compatible with RHEL 8, CentOS 8, and Oracle Linux 8
:Ansible: - The Command Options field on Ansible Playbook Tasks can now resolve variables so that Inputs can be consumed
:Console: - Improvements made for hypervisor console keyboard layouts. This includes the ability to select a default keyboard RDP layout in User Settings and improvements to provide clarity as to the layout expected on the Virtual Image
:Credentials: - Create and integrate an external credential store server. Integrate it with multiple appliances for easy and secure credential storage and rotation
               - Securely store credential sets and retrieve them as needed, such as when creating new integrations or writing automation scripts
:Google Cloud Platform: - Name is now displayed along with the reserved static IP addresses when assigning a static IP address at provision time
:Integrations: - Added Git repository caching setting to Git, Github, and Ansible integrations. When enabled, repositories are cached every five minutes and when disabled, code is pulled from the repository on each execution
:Kubernetes: - 1.22 & 1.21 Support added for VMware, Amazon, External and Manual Morpheus Kubernetes Clusters (MKS)
:Morpheus Worker: - Morpheus Worker/Gateway packages updated to v5.4.3. Note: Worker/Gateway v5.4.3 required for Morpheus v5.4.3 Appliances.
:OpenStack: - A Project selection is no longer required when integrating OpenStack Clouds. You can scope the Cloud to a single Project or leave the Project field empty to scope the Cloud to all Projects
:Provisioning: - Default CentOS 8 system Layouts have been disabled. Customers can still add their own CentOS 8 Layouts and continue to use an existing CentOS 8 Layouts they have added
:ServiceNow: - Catalog Items exposed to ServiceNow can now be mapped to a specified SN catalog of the user's choosing
:UI: - Additional details will now appear in an Instance History tab, including startups, shutdowns, resizes and reconfigure details
      - Dark mode theme added. Themes are selected on the User Settings page and are not usable in whitelabeled appliances
      - Display styling for Tags and Labels has been updated to make them more visible on Instance, VM, and server detail pages
      - Performance and monitoring widgets added to the Cluster detail page
      - The node name has been added to the title bar for console sessions to make it clear which node or machine is being accessed
      - WLE count now displayed on license page for all license types
:vCloud Director: - Support for integration with vCD 9 has ended with |morpheus| 5.4.3


Fixes
=====

:API & CLI: - Added warning that NSX-V does not support static routes when users attempt to add one via ``network-static-routes add`` commands issued to |morpheus| CLI
             - Adding rules to pre-existing security groups now works properly through |morpheus| CLI
             - Cleanup work has been done on the Add Clusters flow for |morpheus| CLI to remove duplication of some prompts and make the flow easier for the user
             - Creating ``containerTemplate`` type Tasks through |morpheus| CLI now works properly
             - Fixed an issue that could prevent provisioning of Apps from App Blueprints in a Tenant account from |morpheus| API or CLI
             - Fixed an issue that prevented creation or configuration of Expiration with internal approval configuration through |morpheus| API and CLI
             - Fixed an issue with Cloud filtering when provisioning Kubernetes clusters through |morpheus| CLI. Previously unsupported Clouds could be selected and provisioning would fail
             - Folder selection is now mandatory when "cloning to image" through |morpheus| API and CLI. Previously if a folder was not selected, the process could fail if the user did not have correct permissions on the root folder
             - Improvements made to Instance Type filtering when adding Instances via |morpheus| CLI. Previously Instance Types could potentially appear which were improper for the Group and Cloud selection which would cause failures
             - It's now possible to create Service Plans through |morpheus| API and CLI using a code value that was previously used (and the associated plan subsequently deleted)
             - Network Name and Network Display Name attributes for networks can now both be set through |morpheus| API and CLI as is possible through |morpheus| UI
             - Password-type Input values are now masked when querying an Instance over |morpheus| API and CLI and reviewing the ``customOptions`` map
             - Resizing Instances with Plans allowing custom memory and CPU counts now works correctly through |morpheus| API and CLI
             - SCVMM Instance creation via |morpheus| API no longer hangs and appears to fail when a volume list is not given in the posted payload
             - Setting custom options (Inputs) on an Instance via |morpheus| API is now more tolerant of different payload formats
             - The user's preferred default Persona can now be set via |morpheus| API and CLI as users could already do in |morpheus| UI User Settings
             - Updating ``service-plans`` via |morpheus| CLI now works properly and does not return JSON parse errors
             - Uploading logo icon images for Service Catalog Items via |morpheus| API is now working properly
             - When creating a new Instance via |morpheus| API (POST /api/instances) and specifying multiple copies, the returned array now includes the Instance map for all Instances rather than just one
:Agent: - |morpheus| Windows Agents updated to v1.8.0, fixes Windows Bare-Metal Servers displaying incorrect core count :superscript:`5.2.15`
:Amazon: - Amazon cloud integrations with no VPCs can now be created by selecting "All VPCs" rather than selecting any specific VPC
          - Fixed an issue that caused all Plans in Amazon Clouds to be deactivated if the credentials stored with the integration were no longer good. Now, Plans remain and error messages are surfaced in the logs indicating that credentials must be updated
          - Fixed an issue that could cause the Route53 Zone Records list page for a single AWS integration to show Zone Records for other AWS accounts integrated with |morpheus|
:Ansible: - Added support for multiple Ansible Git URL formats to prevent failure due to parsing issues
           - Ansible integrations can now successfully be made in Library > Integrations. Previously they would only successfully create from the global integrations section (Administration > Integrations)
           - Corrected view inconsistencies that were sometimes present when comparing the same Ansible integration in the Automation Integrations section (Library > Integrations) compared with the global integrations section (Administration > Integrations)
           - Fixed an issue that caused "Master" to show as default branch on an Ansible integration even if another default branch was selected
           - Fixed an issue that could cause the known hosts file not to be cleaned up when Instances are deleted under specific conditions. When a machine is later provisioned with the same IP address, problems could the arise
           - Fixed an issue where Workflows containing Ansible Tasks would run successfully against Instances but not servers
           - The Ansible repo name is now shown from the detail page of an Ansible Task rather than its database ID
           - |morpheus| will now add collections provided in requirements.yml
:Azure: - Fixed an issue that caused some marketplace images not to be available (such as when creating a new Virtual Image) during a Cloud sync
         - Fixed an issue that could cause load balancers to be left behind when Apps were deleted
         - Fixed an issue that could cause multi-node Azure load balancers to be added with only a single node under certain conditions
         - Fixed an issue that could prevent Instance OS and health data to not be correctly tracked when provisioning Azure Windows Instances from ARM templates
         - Fixed an issue that prevented provisioning of default DBaaS Instance Types under certain region and resource group configurations
         - Fixed bug that prevented scale factor of > 1 to be added to the same backend pool
         - |morpheus| now supports multiple address spaces in Azure networks as was already possible through the Azure web console
:Backups: - Fixed an issue that prevented restoring Instances from backups of Instances which were converted into managed Instances in GCP, Azure, OpenStack and UpCloud Clouds
           - The Backup Button now correctly displays the Add Backup modal when an Instance is viewed from the Inventory section of the Service Catalog Persona
:Blueprints: - Corrected an issue that could cause disk sizes to be represented incorrectly on an App Blueprint (though they would be correct after provisioning Apps from the Blueprint)
:Commvault: - Fixed an issue that could cause all backup servers to be shown to the user regardless of their Role permissions related to backups
:Github: - Github integrations can now be deleted even if Spec Templates have been created from an associated respository
:Google Cloud Platform: - Fixed a view issue that would create duplicate server entries in a Subtenant if GCP Instances were shared from the Primary Tenant
                  - Improved sync process for GKE control plane versions
:Huawei Cloud: - Fixed an issue that could prevent provisioning from user-provided Huawei images
                - Fixed an issue that left image references in |morpheus| after the image was deleted from the Huawei cloud console
:Inputs: - Fixed an issue that could allow the user to enter an invalid selection in a Typeahead field which would often lead to provisioning failures
:Instances: - Fixed an issue when cloning CentOS Instances which could cause the user to connect to a console for the original Instance if they used that feature too quickly after a clone
:NSX-T: - Deleted NSX-T certificates are now successfully deleted from the NSX console as well
:NSX: - Fixed missing DNS and Gateway fields when creating NSX-T static networks :superscript:`5.2.15`
:Network: - Users with "Infrastructure: Network" Role permission set to Group can now create new Network integrations successfully
:OpenStack: - Fixed a display issue that caused the CIDR for SFS File Share Access Rules to be displayed incorrectly (though they were set properly in the underlying cloud)
             - Fixed an issue that caused Windows Server 2019 images to be detected as Linux images which would fail to provision when invalid Linux commands were being used in the background
             - Fixed an issue that could prevent successful resizing of SFS shares for OpenStack Clouds
             - Fixed an issue that would cause the total storage value shown in UI not to change after successfully reconfiguring the Instance to increase storage
             - OpenStack Cloud resource pools are now automatically assigned to a Subtenant when a Cloud is assigned to prevent assigned Clouds from being inaccessible to Subtenant users
             - Security Groups are no longer required for Instances in OpenStack Clouds (including Huawei and OTC) as is the case in the cloud console. The Instances will be inaccessible until a Security Group is applied
             - When an OpenStack Cloud is integrated in the Primary Tenant and shared with Subtenants, permissions to Octavia Service are shared with the Subtenant as well
:Policies: - Inputs which are exported as Tags can now be used to satisfy Tag Policies at provision time
            - Primary Tenant users can now scope Policies against specific Subtenant users, Clouds, and Groups when the Policy is scoped to a specific Tenant
:Scaling: - Fixed an issue that could cause Windows servers not to scale when threshold conditions are met
:Security: - |morpheus| version information is no longer returned with unauthenticated calls to /api/ping
:ServiceNow: - Fixed an issue causing duplication of catalog scripts during sync
              - Fixed an issue that prevented custom attributes from being mapped properly to ServiceNow CI items
              - Values like IP addresses and CIDR notation can now be passed to ServiceNow via Inputs on exposed Catalog Items and they will be parsed correctly without specifically quoting them like a string ("10.0.1.1/32")
:Tags: - Tags with leading spaces are no longer duplicated with each Cloud sync
:Terraform: - Improvements made to smooth the process of provisioning Azure and GCP-based Terraform Instances
             - |morpheus| now validates whether an Apply State command can be run against an Instance and will not run it if not supported
:UI: - Fixed a UI rendering issue for Service Catalog in Safari browsers
      - Fixed an issue where network details weren't immediately updated in the UI view after saving new changes (though the changes were made on the underlying network)
      - Fixed minor display issues for Inputs represented on the Edit Instance modal
      - Instance expiration banners no longer show an incomplete message in situations where the Instance has expired but a Delayed Removal policy prevents the deletion
      - The Group name now appears correctly on the review tab of the Add Bare Metal wizard
      - The Virtual Images List Page (Library > Virtual Images) now defaults to listing user-created virtual images at the top of the list above the system default images
      - When viewing the Usage page (Operations > Costing > Usage) the menu is no longer highlighted as if you're looking at the Activity page
:Users: - Fixed an issue that prevented Subtenant users from impersonating other users in their Tenant
:VMware: - Corrected an issue where Virtual Images created via clone to image processes would not have EDIT and DELETE buttons on their detail pages and would be deleted following the next cloud sync
          - Fixed an issue that could cause Snapshots not to be removed for an Instance when the Instance was deleted or when the Snapshot was deleted individually
          - Fixed an issue that could cause networks to remain associated with VMware clusters even after the association was removed in VMware and a |morpheus| Cloud sync had taken place
          - When reconfiguring a server or Instance, the IP address and mode fields are now read-only to reflect the fact that these values cannot be updated with a reconfigure anyway
:Virtual Images: - The source image hyperlink is no longer present and is replaced with a static text image name when the user does not have permission to view the target Virtual Image
:Workflows: - Added additional validation step to ensure valid JSON is entered for Workflows which have "Allow Custom Config" enabled which lets the user enter an additional JSON map of values at execution time
             - Operational Workflows can now be successfully run against non VM-backed Instances (XaaS, Workflow-based)
:vCloud Director: - Fixed an issue that caused reconfigure actions to fail for vCD Instances
                  - Fixed an issue that could cause DHCP to be set to "on" when vCD networks without DHCP were synced in
                  - Fixed an issue with creating and managing NSX router objects with vCD Clouds


Appliance & Agent Updates
=========================

:Appliance: - Java: Updated jdk to v11.0.14
            - MySQL: Embedded MySQL updated to v5.7.37 :superscript:`5.2.15`
            - Tomcat: Updated to v9.0.58
:Agent: - Added FIPS compliant el8 |morpheus| Agent node & vm-node packages. Compatible with RHEL 8, CentOS 8, and Oracle Linux 8
        - Agent Node & VM Node Packages: Java: Updated jdk to v11.0.14
        - |morpheus| Windows Agents updated to v1.8.0, fixes Windows Bare-Metal Servers displaying incorrect core count :superscript:`5.2.15`

.. ..
