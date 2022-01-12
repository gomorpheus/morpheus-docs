.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: This release includes improvements to Amazon AWS price sync. After upgrading, it's recommended that you manually perform one "Daily" refresh of one of your Amazon Clouds to ensure availability of Amazon pricing data. To manually refresh a Cloud, navigate to Infrastructure > Clouds > (Selected Amazon Cloud) and select "Daily" from the REFRESH dropdown menu. If this is not done, |morpheus| may not show Amazon pricing information in the provisioning wizard until the following day after an automatic Daily refresh would have taken place.

.. IMPORTANT:: Support has been removed for exposing Instance Types and App Blueprints to the ServiceNow catalog via |morpheus| integration. This is because more advanced configurations of Instances and App Blueprints, in addition to Workflows, can be exposed utilizing Catalog Items. Following upgrade, Instance Types and App Blueprints which were previously exposed will be disabled from the ServiceNow catalog. Any important configurations will need to be replaced with Service Catalog Items. See our `ServiceNow integration guide <https://docs.morpheusdata.com/en/5.4.2/integration_guides/ITSM/ServiceNow.html#adding-to-servicenow-catalog>`_ for instructions on how to expose |morpheus| Catalog Items to ServiceNow.

.. NOTE:: v5.4.2-2 fixes 5.4.2-1 js event target issue with instance lists and modals. 

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version.

.. .. include:: highlights.rst

New Features
============

:API & CLI: - NSX-T load balancers can now be created and managed from |morpheus| API and CLI :superscript:`5.2.14`
             - Option to expose |morpheus| Instance Types and Blueprints to ServiceNow via |morpheus| API and CLI has been removed which matches the change made to |morpheus| UI
:Backups: - UI wizard is now displayed when restoring from Backup, including option to restore to new Instance or restore to the existing Instance. This can be done from the Backups tab on the Instance detail page or the Backup detail page
:Inputs: - Inputs (previously Option Types) have two additional attributes, one which displays the Input when editing an Instance and a second which allows displayed Inputs to be updated when editing the Instance
:Library: - Create Layouts and Instance Types representing XaaS constructs with no specific VM or container type behind it. Pricing and Workflow phases can be utilized as with other Instance Types. Added new technology type of "Workflow" for Layouts to support this
:ServiceNow: - Instances and Blueprints can no longer be exposed to ServiceNow for provisioning from the ServiceNow. Instead, |morpheus| Catalog Items (which can be built from existing Instance Type and Blueprints) are the only construct which can now be exposed
:UI: - Improved UI on the Instance History tab, including ability to see raw history output, and timeline of executed Tasks, along with the success of each Task


Fixes
=====

:API & CLI: - Fixed an issue that caused vCD Instance resizing to fail when executed via |morpheus| API and CLI
             - Fixed an issue that could cause errors to be thrown when the user enters "?" to see all available options while stepping through CLI wizards
             - Fixed an issue that could cause virtual image adding to fail via |morpheus| CLI
             - Network mode settings now work properly when configured for OpenStack Clouds through |morpheus| API and CLI
:Alibaba Cloud: - Fixed an issue that caused all available plans to appear for every Alibaba Cloud region whether they were truly offered for the selected region or not
                 - Fixed an issue that caused incorrect storage options to appear for some Alibaba Cloud regions
:Amazon: - Added more detailed validation for AWS security group names to ensure users are only submitting valid names
          - Fixed an issue causing pricing data not to be synced in for some AWS plans
:Ansible: - Checkboxes are now evaluating consistently where in the past they wouldn't consistently evaluate as Off/On, True/False, null, etc.
           - Fixed an issue causing Ansible Tasks to hang or fail when run against servers whereas the same Tasks would run fine against the Instance
:Automation: - Task and Workflow output is now displayed in greater detail on History and Execution Tabs throughout the UI to improve aid in error identification
:Backups: - Fixed an issue that prevented restoration from backup for brownfield Instances converted to managed Instances under certain conditions
:Billing: - Fixed an issue that caused SCVMM controller nodes to appear as a discovered server in usage records
:Catalog: - Removed the "copies" concept from Service Catalog items as it was only intended to be part of traditional Instance provisioning
:Chef: - Fixed an issue that could cause Chef integrations not to work correctly during provisioning of Windows boxes
:DNS: - Fixed an issue that could cause an error message to be surfaced when creating zone records (though the record was successfully saved)
:Identity Sources: - Fixed an issue causing the failed login attempt count not to reset after the user successfully logged in under certain conditions. This could lead to users being locked out or disabled
                  - ``IssueInstant`` parameter added to logout payload for SAML identity sources to prevent errors in certain scenarios
:Kubernetes: - Fixed an issue causing vCD Kubernetes cluster provisioning to fail when triggered via |morpheus| CLI
:Logs: - Fixed an issue that could cause incorrect formatting in exported log files
:NSX-T: - Fixed an issue preventing Subtenant users from creating load balancer virtual servers using load balancer SSL profiles they've just created :superscript:`5.2.14`
         - Fixed an issue that prevented Subtenant users from adding routers to shared NSX-T networks under certain conditions
         - Improvements made to smooth the process of creating Tier-0 routers for NSX-T :superscript:`5.2.14`
         - Setting NSX-T distributed firewall rules by IP address now works correctly :superscript:`5.2.14`
:OpenStack: - Project and Cloud visibility is now aligned for Project-scoped OpenStack Clouds to prevent confusion in certain cases
:Oracle Cloud: - Fixed an issue that caused the "Install Agent?" option to become unchecked at times on Virtual Images added for Oracle Cloud
:Plans & Pricing: - Fixed an issue that caused pricing information not to appear in Service Catalog when a Price Set was scoped to a specific Resource Pool
:Security: - MySQL usernames and passwords are no longer exposed in the History output when provisioning MySQL Instances or Apps
:Terraform: - Fixed an issue that could cause Terraform Plan to run a different version of Terraform than that which is specified in the Blueprint
:UI: - Fixed an issue related to integrated backup server pagination
     - Fixed js event target issue with instance lists and modals that caused some areas in instance list and modals to not be clickable (Found in 5.4.2-1, fixed in 5.4.2-2)
      - On the Groups List page (Infrastructure > Groups), the Instances field now shows "0" when there are no Instances associated with a Group rather than an empty space
      - Tags set via Inputs are now shown on the Instance detail page for Instances provisioned through Service Catalog as they are for Instances provisioned through the provisioning wizard
:VMware: - Fixed an issue causing networks to no longer be visible if VMware clusters were renamed
          - Fixed an issue related to plan filtering when provisioning Instance Types using templates synced via VMware Content Library
:Veeam: - Fixed an issue that could cause Veeam backup creation to hang when created from the Backups area of the UI (not during provisioning)
         - Fixed an issues that prevented the removal of Veeam backups under certain conditions
         - Fixed jobs deleted in Veeam not being removed on Veeam sync
         - Fixed unable to delete a veeam backup in morpheus if the backup has already been deleted in veeam


Appliance & Agent Updates
=========================

:Appliance: - Embedded Elasticsearch Log4j updated to v2.17 (CVE-2021-45105).  :superscript:`5.2.14`
             - Embedded Elasticsearch jackson-databind updated to 2.13.1 (CVE-2020-25649) :superscript:`5.2.14`
             - Embedded Elasticsearch jackson-dataformat-cbor updated to 2.13.1 (CVE-2020-28491) :superscript:`5.2.14`

:Agent: - Linux Agent version updated to v2.2.2 :superscript:`5.2.14`
        - Log4j removed from Linux Agent, replaced with Slf4j :superscript:`5.2.14`

:Node Packages: - Node and VM Node Package versions updated to v3.2.4 :superscript:`5.2.14`
                - Java jdk & jre updated to 11.0.13+8 :superscript:`5.2.14`

.. ..
