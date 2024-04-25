.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|
- 7.0.1-2 Apr 22 2024

7.0.1-2 Updates
===============

:catalog: -  Fixed a 7.0.1-1 regression with Form Variables not appearing on the right side when using Input form types
          -  Fixed a 7.0.1-1 regression with incorrectly locked fields when editing a catalog item
          - Fixed a 7.0.1-1 regression with the option to enable/disable auto injection of Form Variables

New Features
============

:Clusters: - Added SSH validation to the Add Clusters Wizard. When entering host IP addresses, |morpheus| will validate that it has SSH access to that IP address
            - Removed option to provision KVM and KVM/Docker cluster types. KVM is still supported through onboarding pre-configured brownfield hosts and consuming them as provisioning targets
:DigitalOcean: - Added support for scoping DigitalOcean Clouds to specific VPCs as well as support for discovering existing Droplets and onboarding them as discovered servers
:Identity Sources: - Added an optional configuration to Active Directory Identity Sources which allows users to log in with a UPN credential for subdomain access rather than just a username :superscript:`6.2.9`



Fixes
=====

:API & CLI: - Billing API responses now can include start and end times down to the millisecond by including the ``&includeMS=True`` parameter :superscript:`6.2.9`
             - Fixed an issue adding NSX-T integrations scoped to individual Projects at the |morpheus| subtenant level
             - Fixed updates to NSX-T network ``displayName`` properties also updating the network name value following the next sync :superscript:`6.2.9`
:Automation Execute Schedules: - Fixed Daylight Saving adjustments for Execution Schedules :superscript:`6.2.9`
:Azure: - Fixed successful reconfigures leaving workloads in a "resizing" status under specific conditions :superscript:`6.2.9`
:Catalog: - After updating the number of disks, the order review page now shows the updated number rather than displaying the original ordered number :superscript:`6.2.9`
           - For Catalog Item Blueprints, the Layouts field selections are now given in alphabetical order and the pre-set value prior to any user selection now reads "default" rather than "select" :superscript:`6.2.9`
:Code: - When browsing folders in integrated Git repositories, folders in non-default branches can now be expanded to view files :superscript:`6.2.9`
:Currency: - Improved currency conversion logic in specific scenarios to ensure greater accuracy :superscript:`6.2.9`
:Github: - Clicking the Location link from the Organizations tab of a Github integration detail page now leads to a better formatted page :superscript:`6.2.9`
:Inputs: - Default Input values on Inputs set due to "Remove No Selection" configuration are now shown on detail page as expected when configured to show there :superscript:`6.2.9`
          - Fixed regex verification for text-type Inputs not being checked under specific conditions when the Input was Visibility-dependent on another Input :superscript:`6.2.9`
          - Number-type Inputs now work properly when the spinner controls are used to increment the value :superscript:`6.2.9`
          - When a required Input defaults to a "false" value sourced from a manual Option List, it will no longer fail the required validation without the user toggling the values :superscript:`6.2.9`
:Jobs: - Jobs (|ProJob|) that have more than 25 "Context Instance" targets will now show them all when editing the Job later :superscript:`6.2.9`
        - Workflow Jobs containing dependent fields now property update to using the new values if edited after the initial save :superscript:`6.2.9`
:KVM: - Fixed VMs restarting unnecessarily when adding new disks or extending the root disk
:Kubernetes: - Adding workers to Kubernetes clusters with custom memory ranges defined on the Plan no longer fails with error :superscript:`6.2.9`
              - We now properly show the number of master nodes present on external (brownfield) Kubernetes clusters when there are multiple masters :superscript:`6.2.9`
:Layouts: - Sorting the Layouts list page by the version column now sorts the Layouts in a logical ascending or descending order :superscript:`6.2.9`
:NSX-T: - Fixed creation of pools for NSX Advanced Load Balancers which previously failed with error :superscript:`6.2.9`
         - Services shared across projects are now available while creating NAT Rules for integration scoped to a specific project :superscript:`6.2.9`
:Network: - Fixed large CIDR ranges slowing down loading of network detail pages :superscript:`6.2.9`
:Nutanix Prism Central: - Fixed errors that prevented deleting Prism Central Clouds :superscript:`6.2.9`
                  - When Nutanix Prism Central Clouds are deleted, synced Virtual Images are also deleted to prevent duplicate images if the Cloud is re-added later :superscript:`6.2.9`
:Option Lists: - Option Lists can now use Input values in request and translation scripts when their associated Input is hidden :superscript:`6.2.9`
:Route 53: - Fixed Route53 integration being limited to returning only the first 100 routes :superscript:`6.2.9`
:Security: - A list of installed plugins is no longer visible when visiting ``<applianceUrl>/plugins`` without a logged in session :superscript:`6.2.9`
            - Fixed an issue that could potentially allow users to run Tasks against workloads in different Tenants by manipulating POST requests :superscript:`6.2.9`
            - HTML injection is no longer possible via the "Label" field when adding links (|AdmSetWhi|) to the global support menu :superscript:`6.2.9`
:VMware: - Cloning vCenter VMs from |morpheus| no longer fails under specific scenarios where the VM was built from a synced template which was later removed from inventory in vCenter :superscript:`6.2.9`
          - Fixed issues related to snapshot reverting when disks had been added after the snapshot was taken :superscript:`6.2.9`
          - Fixed scenarios where address information did not sync due to MAC addresses not matching due to letter casing :superscript:`6.2.9`
          - Fixed successful reconfigures leaving workloads in a "pending" status under certain conditions :superscript:`6.2.9`
          - When Resource Pools are nested, |morpheus| now shows all of the child Resource Pools properly when many are present :superscript:`6.2.9`
:Veeam: - Fixed backup jobs and repositories removed in Veeam not being removed from |morpheus| on sync


Appliance & Agent Updates
=========================

:Appliance: - Embedded MySQL updated to v8.0.36 :superscript:`6.2.9`
            - Java updated to v11.0.22 :superscript:`6.2.9`
            - Standard Appliance OpenSSL version updated to v1.1.1w :superscript:`6.2.9`
:Agent Packages:  - Node and VM Node Packages Java updated to v11.0.22 :superscript:`6.2.9`
:Plugins: - DigitalOcean: Embedded Digital Ocean plugin updated to v1.2.4
