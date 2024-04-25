.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Identity Sources: - Added an optional configuration to Active Directory Identity Sources which allows users to log in with a UPN credential for subdomain access rather than just a username :superscript:`7.0.1`
:Kubernetes: - Disabled built-in MKS HA Cluster Layouts with the intention to explore the feasibility of adding them back with load balancing


Fixes
=====

:API & CLI: - Billing API responses now can include start and end times down to the millisecond by including the ``&includeMS=True`` parameter :superscript:`7.0.1`
             - Fixed updates to NSX-T network ``displayName`` properties also updating the network name value following the next sync :superscript:`7.0.1`
:Automation Execute Schedules: - Fixed Daylight Saving adjustments for Execution Schedules :superscript:`7.0.1`
:Azure: - Fixed successful reconfigures leaving workloads in a "resizing" status under specific conditions :superscript:`7.0.1`
:Catalog: - After updating the number of disks, the order review page now shows the updated number rather than displaying the original ordered number :superscript:`7.0.1`
           - For Catalog Item Blueprints, the Layouts field selections are now given in alphabetical order and the pre-set value prior to any user selection now reads "default" rather than "select" :superscript:`7.0.1`
:Code: - When browsing folders in integrated Git repositories, folders in non-default branches can now be expanded to view files :superscript:`7.0.1`
:Costing: - Fixed costs shown on Instance detail pages within Subtenants showing costs in USD rather than the configured Tenant currency :superscript:`7.0.0 `
:Currency: - Improved currency conversion logic in specific scenarios to ensure greater accuracy :superscript:`7.0.1`
:Github: - Clicking the Location link from the Organizations tab of a Github integration detail page now leads to a better formatted page :superscript:`7.0.1`
:Inputs: - Default Input values on Inputs set due to "Remove No Selection" configuration are now shown on detail page as expected when configured to show there :superscript:`7.0.1`
          - Fixed regex verification for text-type Inputs not being checked under specific conditions when the Input was Visibility-dependent on another Input :superscript:`7.0.1`
          - Number-type Inputs now work properly when the spinner controls are used to increment the value :superscript:`7.0.1`
          - When a required Input defaults to a "false" value sourced from a manual Option List, it will no longer fail the required validation without the user toggling the values :superscript:`7.0.1`
:Instances: - Fixed Layout and Version fields not appearing on "Convert to Instance" modal (for converting servers to managed Instances) :superscript:`7.0.0 `
:Jobs: - Jobs (|ProJob|) that have more than 25 "Context Instance" targets will now show them all when editing the Job later :superscript:`7.0.1`
        - Workflow Jobs containing dependent fields now property update to using the new values if edited after the initial save :superscript:`7.0.1`
:Kubernetes: - Adding workers to Kubernetes clusters with custom memory ranges defined on the Plan no longer fails with error :superscript:`7.0.1`
              - We now properly show the number of master nodes present on external (brownfield) Kubernetes clusters when there are multiple masters :superscript:`7.0.1`
:Layouts: - Sorting the Layouts list page by the version column now sorts the Layouts in a logical ascending or descending order :superscript:`7.0.1`
:NSX-T: - Fixed creation of pools for NSX Advanced Load Balancers which previously failed with error :superscript:`7.0.1`
         - Fixed network resources being visible in other Subtenants when NSX-T integrations created in one Subtenant were scoped to a public Cloud integrated from the |mastertenant| :superscript:`7.0.0 `
         - Services shared across projects are now available while creating NAT Rules for integration scoped to a specific project :superscript:`7.0.1`
:Network: - Fixed large CIDR ranges slowing down loading of network detail pages :superscript:`7.0.1`
:Nutanix Prism Central: - Fixed errors that prevented deleting Prism Central Clouds :superscript:`7.0.1`
                  - When Nutanix Prism Central Clouds are deleted, synced Virtual Images are also deleted to prevent duplicate images if the Cloud is re-added later :superscript:`7.0.1`
:Option Lists: - Option Lists can now use Input values in request and translation scripts when their associated Input is hidden :superscript:`7.0.1`
:Route 53: - Fixed Route53 integration being limited to returning only the first 100 routes :superscript:`7.0.1`
:Security: - A list of installed plugins is no longer visible when visiting ``<applianceUrl>/plugins`` without a logged in session :superscript:`7.0.1`
            - Fixed an issue that could potentially allow users to run Tasks against workloads in different Tenants by manipulating POST requests :superscript:`7.0.1`
            - HTML injection is no longer possible via the "Label" field when adding links (|AdmSetWhi|) to the global support menu :superscript:`7.0.1`
:VMware: - Cloning vCenter VMs from |morpheus| no longer fails under specific scenarios where the VM was built from a synced template which was later removed from inventory in vCenter :superscript:`7.0.1`
          - Fixed issues related to snapshot reverting when disks had been added after the snapshot was taken :superscript:`7.0.1`
          - Fixed scenarios where address information did not sync due to MAC addresses not matching due to letter casing :superscript:`7.0.1`
          - Fixed successful reconfigures leaving workloads in a "pending" status under certain conditions :superscript:`7.0.1`
          - When Resource Pools are nested, |morpheus| now shows all of the child Resource Pools properly when many are present :superscript:`7.0.1`

Appliance & Agent Updates
=========================

:Appliance: - Embedded MySQL updated to v8.0.36 :superscript:`7.0.1`
            - Java updated to v11.0.22 :superscript:`7.0.1`
            - Standard Appliance OpenSSL version updated to v1.1.1w :superscript:`7.0.1`
:Agent Packages:  - Agent updated to v2.6.0
                  - Node and VM Node Packages Java updated to v11.0.22 :superscript:`7.0.1`
                  - Node and VM Node Packages Java updated to v3.2.23 :superscript:`7.0.1`
