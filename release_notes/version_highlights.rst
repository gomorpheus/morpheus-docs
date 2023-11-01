**************************************
|morpheus| |morphAnnualVer| Highlights
**************************************

This section includes feature change and key enhancement highlights for all standard (non-LTS) releases within |morpheus| version 6.

6.0.0
=====

:Dashboard: - The main |morpheus| Dashboard landing page (|OpeDas|) has been completely redesigned
:Instances: - Instance detail pages now include a Resources tab which shows VMs, containers, Apps, and other constructs which may be associated with the Instance. Previously this information was on the main detail page, not inside its own tab
            - The Instance detail page header has been redesigned to move more of the most important information to the top of the page
            - The Instance detail page headers has been redesigned to move more of the most important information to the top of the page
            - The Instance detail page now includes a costing tab. This tab pulls and aggregates Instance and host invoices, pricing history charts, pricing trends, and lists associated metered prices
            - The Instances detail page now includes a Summary tab which holds information that was previously in the Info section of the page and was always present (regardless of which subtab the user was looking at)
            - The Instances detail page now includes a monitoring tab which holds memory, storage, CPU, disk I/O and network stats. This information can be shown over a maximum of 90 days depending on your appliance stats retainment setting
:Policies: - Many Policy types can now be scoped to Service Plans
:Workflows: - Nested Workflows have been added. Create modular Workflow pieces to build out larger Workflows
            - Retry failed Workflows from the point where the first Task failed

6.0.1
=====

:Labels: - Run Tasks, Operational Workflows, or Jobs against a group of Workloads (Instances or servers) with a commomn Label
:Kubernetes: - Added Kubernetes 1.26 support
:Oracle Cloud: - Added two-way tag sync for Oracle Cloud workloads, similar to tag sync capability with other public Clouds
:Policies: - Added Workflow execution approval Policies. When Operational Workflows are executed
:Workflows: - Added Workflow stop capability, such as if you realize a long-running Task will fail and do not wish to wait out the expected failure

6.1.0
=====

:Forms: - Added a Form builder tool to aid in creating robust order Forms for Catalog Items

6.1.1
=====

:Amazon: - Added ability to scope Amazon AWS Clouds to all regions
:Instances: - Both the Name and Display Name property for Instances can now be edited. Previously, only the Display Name could be edited

6.1.2
=====

:Forms: - Added Text Array input type for Forms which allows the user to enter a list of values separated by a delimiter. Once entered, the values are parsed out and may be individually deleted prior to submitting the form
        - Added new ability to filter available Cloud types on Forms. Select a Cloud type from the LIMIT TO CLOUD TYPE dropdown or select FILTER FROM RESOURCE. The option to filter from resource reads the Cloud type from the Catalog Item Instance config

6.2.0
=====

:Import/Export: - Configure code repositories (ex. integrated Github repositories) as import and export targets. Export |morpheus| items as code into repositories and import them into other |morpheus| appliances.
:Workflows: - When running Workflows on-demand against an Instance, users can now select a specific phase of Tasks to be run if a Provisioning Workflow is selected

6.2.1
=====

:Forms: - Additional quality of life features added for Forms
:XaaS: - When Teardown-phase Tasks fail following an attempt to delete an XaaS Instance, the remaining Tasks are stopped which prevents the deletion from taking place. This allows users to correct the failing Tasks and ensure the object is deleted gracefully. Non-XaaS Instances already supported this.

6.2.2
=====

:Catalog: - Added support for saving Catalog items without first passing a check for valid JSON in the config
:Inputs: - Added “REMOVE NO SELECTION” attribute for Select List-based Inputs. This defaults the Input to the first selection in the list rather than to an empty selection
:Layouts: - Added Display Order property for Layouts. Layouts are listed in high-to-low order based on the Display Order in the Layouts dropdown of the provisioning wizard

6.2.3
=====

:Identity Sources: - SAML SSO identity sources using HTTP-POST binding are now working as expected when integrated with |morpheus| Tenants
:Kubernetes: - Updated default Kubernetes Cluster Layouts to version 1.28
