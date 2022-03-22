.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate|

**5.4.4-3 contains a critical SAML security fix as well as NSX-T, provisioning wizard and windows domain join automation updates.**

.. IMPORTANT:: The morpheus-ui logging configuration file has changed from logback.groovy to logback.xml in v5.4.4 (/opt/morpheus/conf/logback.xml). The logback.groovy file from previous versions can be removed, and any updates to logback.groovy will not result in any logging configuration changes.
:Deprecation Notice: The Venafi and AppDynamics integrations are deprecated in v5.4.4 and will be removed in v5.4.5. AppDynamic will return as a plugin at a later date.


.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - API docs site improvements made to speed slow load times
             - Added CRUD actions for creating credential sets matching UI functionality in |InfTruCre|
             - Catalog items can now be associated with a secondary logo which is displayed when |morpheus| dark mode theme is activated
             - Issuing DELETE requests to the ``service-plans`` API now fully deletes the Plan. Previously, the closest you could get to delete functionality was to update the Plan to be inactive.
             - Mute monitoring command is now ``mute`` rather than ``quarantine`` to match newer verbiage in |morpheus| UI. Related commands have been updated to use "mute" verbiage as well
             - Power Schedules can now be incremented in single minute blocks, previously they were incremented in 15 minute blocks
             - Scale down AKS, MKS, GKE, and EKS Kubernetes clusters by removing workers through |morpheus| API and CLI
             - Some API endpoints have moved to reflect the menu changes made in Morpheus UI. See Morpheus API docs for details on changes
             - ``GET`` response payloads from newer API endpoints no longer include ``success:true`` which makes the response more consistent with older endpoints
:Bluecat: - Bluecat DNS Integration added. Bluecat can now be added as a DNS Integration, in addition to the existing Bluecat IPAM integration.
:Credentials: - Adding Amazon and Azure Clouds now supports use of stored credential sets in addition to VMware Clouds which previously supported them
               - Improved handling for scenarios when an external credential store is offline and users are attempting to view or save credentials to it
               - When editing an existing credential, the location (stored internally or in an integrated external store) is now displayed
:Kubernetes: - MKS Kubernetes v1.22 layouts added for Digital Ocean, Google, SCVMM and vCloud Director Cloud types.
              - MKS Kubernetes v1.22 layouts added for Digital Ocean, Google, SCVMM, vCloud Director and Xen Cloud types.
              - Users can scale down MKS (|morpheus| Kubernetes Service) clusters by deleting worker nodes when needed
:Morpheus: - Grails framework updated to Grails 5
:Nutanix: - Added support for UEFI boot option
:Plugins: - Improvements made to IPAM custom plugin development tools
:Policies: - Added "Network" scope to Max VM policies which will limit the number of VMs which can be connected to a specific network
            - Added new Policy type for Max Load Balancer Pools
:Power Schedules: - Power Schedules can now be set down to single minute granularity, previously they were incremented in 15 minute blocks
:Security: - CVE-2020-28052 Upgrade bouncycastle to 1.67
            - CVE-2021-29425 Update common-io to 2.7
            - CVE-2021-29425 Upgrade commons-io 2.7.0
            - CVE-2021-32769 : Upgrade micronaut to at least 2.5.9
            - CVE-2021-33813 Upgrade jdom to 2.0.6.1
            - CVE-2021-35517 Upgrade commons-compress to 1.21
            - CVE-2021-36373 Upgrade Ant to 1.9.16 either 1.10.11
            - CVE-2021-37714 Upgrade jsoup to 1.14.2
            - CVE-2021-41269 Upgrade cron-utils 9.1.6
            - CVE-2021-41767 Upgrade guacamole-common to 1.4.0
            - CVE-2021-42392 Upgrade H2 to 2:2.0.206
            - CVE-2021-42550 Upgrade logback-classic to 1.2.8
            - CVE-2022-21700 Upgrade micronaut-core to 1.4.0
            - Upgrade spring-security-web-5.1.13.RELEASE.jar to version 1.26
:UI: - Adding the ``forceAccountId`` parameter to a URL, along with the appropriate Tenant ID, will now redirect the user to the login page for the correct Tenant if they don't currently have a login session
      - Further tweaks made to dark mode theme to improve visibility and overall look of some elements
:VMware: - VMware Clouds can now be configured to inventory existing instances from a specific resource pool scope


Fixes
=====

:API & CLI: - Fixed an issue related to paging large lists of objects, such as Instances, in |morpheus| API and CLI
             - Fixed an issue that prevented Instance tags from being updated via |morpheus| API or CLI
             - Fixed an issue that prevented provisioning using Azure Marketplace images via |morpheus| API if the ``marketplaceOffer`` value in the config map contained hyphens or no spaces in the offer name
             - Users can no longer attempt to resize the root volume for Azure VMs through |morpheus| API or CLI which is not supported and caused problems
             - ``networks`` API is updated to handle an array of Tenants for setting Tenant permissions on the Network
:AVI: - Fixed issue related to managing pools for AVI load balancers
:Azure: - Fixed an issue that could cause the Azure Availability Zone to come unset when changing other configurations on an Azure App Blueprint
         - UI error is now surfaced when Azure Marketplace terms haven't been accepted and a failure occurs as a result. Previously it would just silently fail
:BIND DNS: - Improvements made to BIND DNS integration to smooth the initial integration creation experience
:Blueprints: - Fixed an issue that could cause configured resource pools on App Blueprints not to be saved correctly
              - Visibility settings for power schedules on App Blueprints are now honored properly. Previously even if the power schedule was hidden it would be shown as visible but locked
              - When the virtual image behind a Layout in an App Blueprint changes, storage controller information is now updated accordingly
:Catalog: - Fixed an issue that caused provisioning failures in catalog items if the Layout was set via Inputs in certain ways
:Clusters: - Clouds with "private" visibility and assigned to a Subtenant are now selectable as provisioning targets in the Cluster wizard from the Primary Tenant matching the behavior in Instance and App wizards
            - Improved validation in the Add Cluster wizard to ensure an IP address is entered when a network with static IP is selected
:Datastores: - Fixed an issue that could cause default datastores not to be honored for certain networks or clouds
:Domains: Fixed issue with automated Windows Domain joins :superscript:`5.4.4-2 5.4.4-3`
:Huawei Cloud: - Fixed an issue that could prevent existing projects from being selected when integrating a new Huawei Cloud
:Kubernetes: - Fixed issue with adding External Kubernetes Cluster in AWS requiring plan selection
              - Improved static IP address handling for Kubernetes clusters in the Add Cluster wizard
              - Relabeled title of the modal for adding workers to EKS clusters to reduce confusion
:MaaS: - Fixed an issue that could prevent proper stopping and starting of MaaS machines from the Infrastructure menu
:MicrosoftDNS: - MicrosoftDNS entries are now synced correctly when using an intermediate jump server
:Morpheus Worker: - Fixed issue with image uploads using morpheus worker hitting Socket Buffer limit
:NSX: - Fixed enabling dhcp on existing NSX-T segments :superscript:`5.4.4-3`
      - Fixed NSX-T distributed firewall rule source and destination loading issue :superscript:`5.4.4-3`
      - Fixed NSX-T LB pool creation error :superscript:`5.4.4-3`
      - Fixed dchp range validation on NSX-T segment creation :superscript:`5.4.4-3`
      - Fixed subtenant NSX-T Network selection issue :superscript:`5.4.4-3`
:OpenStack: - Errors are no longer thrown when restoring from an OpenStack backup which has moved from its original storage space
             - Improved OpenStack API detection for scenarios when an OpenStack environment has services on multiple domains and subdomains
:Option Lists: - Fixed an issue that caused keys rather than values to be returned when Option Lists were presented as Typeahead fields in Inputs
:Oracle Cloud: - Fixed an issue that could cause Oracle Cloud Instance clone to fail
:Policies: - Subtenant administrators can now set Policies which are scoped to Clouds shared with the Tenant from the Primary Tenant
            - When a Policy is scoped to multiple Tenants, the full list of Tenants can be viewed from the Policies list page by clicking on the info (i) button
            - When scoping a Policy to a Tenant, previously-selected Clouds or Networks on the Policy are no longer cleared after the Tenant is set unless the Tenant does not have access to the Cloud or Network
:Provisioning: - Fixed permission issue with disk when used does not have access to associated Virtual Image record :superscript:`5.4.4-3`
               - Fixed networks being reloaded when layout is changed in wizard :superscript:`5.4.4-3`
:Reports: - OpenStack Instance now show the correct CPU counts on Instance Inventory Summary Reports
:Roles: - Access to create and manage Snapshots no longer requires "Full" access to Infrastructure: Compute and "Read" access to Backups. Users with "Read" access to Infrastructure: Compute and "None" access to Backups are now able to manage Snapshots
         - Removing Roles from users with API tokens generated no longer throws errors
:Rubrik: - Fixed an issue that could cause 500 errors to be thrown when Rubrik backups were selected from an Instance backup tab
:SCVMM: - Fixed an issue that could cause Linux consoles not to work properly for SCVMM Instances
:Security: - Changes made to login session handling to improve application security
           - SAML: Critical SAML security fix :superscript:`5.4.4-3`
:Security Scans: Fixed permission issue perventing users with security scan role permission from accessing security scans :superscript:`5.4.4-3`
:ServiceNow: - Fixed an issue that could cause provisioning from a ServiceNow integration to fail when naming Policies were in effect
:Terraform: - Fixed an issue caused by applying Terraform state changes when |morpheus| naming policies were in place
             - Fixed data loading issue when clicking "i" button on tf resources
             - Fixed issue with Terraform App provisioning status not completing after Approval policy is approved and resources are created.
             - Fixed issue with applying available updates to terraform modules.
             - Fixed issue with passing options in the morpheus-ui terraform command line
             - Fixed issue with tf provisioning on cloud with existing key/value cloud profiles (not terraform cloud profiles)
             - Fixed issue with wrong app to cloud association potentially assigned when multiple clouds of same type are available in the target group
:UI: - "Location" heading renamed to "Addresses" on the Inventory (Instance Detail) page for provisioned Catalog Items
      - A warning message is now surfaced in the UI to let the User know they cannot delete a Spec Template when it is tied to a Layout. Previously the delete action would silently fail which could cause confusion
      - The History tab on an Instance detail page is no longer empty if the User does not have Monitoring: Logs permissions
:UpCloud: - Fixed an issue that caused provisioning to UpCloud to fail under some circumstances
:VDI Pools: - Fixed an issue that could cause VDI sessions not to display properly for SCVMM-based VDI pools
:VMware: - Fixed an issue that caused VMware Clouds to become stuck and unable to be deleted
          - Fixed an issue that prevented provisioning to VMware Clouds shared with a Subtenant and which had just one cluster-type data store
          - Improvements made in syncing process for |morpheus| Wiki content with VMware notes fields
:Workflows: - Fixed an issue that caused Input values not to be pre-populated when executing one-off Operational Workflows from the Instance detail page under certain conditions


Appliance & Agent Updates
=========================

:Appliance: - morpheus-ui logging configuration file changed from logback.groovy to logback.xml.



.. ..
