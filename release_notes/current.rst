.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Morpheus 5.0.0 is a Beta Release and should not be installed in Production environments. Review :ref:`compatibility` before installing or upgrading |morpheus|

5.0.0 Highlights
================

Introducing Personas
--------------------

5.0.0 introduces Personas, a new approach to streamline, optimize and simplify targeted self-service across disciplines. Our first Persona is Service Catalog, a paradigm shift to self-service that removes the complexity of multi-cloud, multi-format, multi-service offerings and presents a simple RBAC Catalog with one-click ordering of any resource. The new Self Service tool allows Admins to easily create Catalog Items using existing wizards and specs that minimize or even eliminate end-user input. Personas are assigned using existing Roles and users can be give access to multiple Personas with quick access to each Persona added to the global nav. 

- Personas further optimize interfaces and processes for target audiences.
- The Service Catalog Persona further simplifies self-service provisioning of any resource with minimum or even zero user input.
- Service Catalog users can add items to their cart and checkout with a few clicks, then access resource in the Service Catalog Dashboard or Inventory section. 
- Admins can quickly create Catalog Items using familiar processes and existing configurations, exposing only the options they choose to end users.
- Instances and Blueprints/Apps are supported for Catalog Items in 5.0.0 with additional options coming, including Operational Workflows.
- Personas and Catalog Items utilize existing RBAC permissions and Policies. Users can easily switch between assigned Personas.

.. image:: /images/releases/500/morpheusCatalog500-1.gif

|

Morpheus Plugins
----------------

The Morpheus Core Plugin Library provides a common framework for extending and customizing Morpheus capabilities. This includes providing plugin extensions for adding various integrations such as Cloud Integrations, Service Level Integrations or Providers for things like DNS, IPAM, Config Management, UI Extensions, Etc. The Morpheus Plugin API is a Java based library that currently supports implementing providers of the following types:

- UI Extensions
- Task Types
- IPAM
- DNS
- Approvals
- Cypher Modules

Additional information will be accessible in the Morpheus Developer Portal.

|

Invoices UI
-----------

The new Invoices UI brings the existing powerful Invoices API <https://apidocs.morpheusdata.com/#invoices> to the UI

- View highly-granular costing data through Invoices
- Create and export Invoice views with custom filters and columns
- View Invoice summaries, historical Cost and Price charts, and individual Line Item details

.. image:: /images/releases/500/invoiceList.png

|

Enhanced Reports
----------------

Reporting capabilities have been expanding with a new interface, additional report types, and report scheduling. 

- Schedule reports to be run at a specific point in time or on a specific recurring schedule
- Eight new report types added for additional costing and usage breakdowns
- New filtering options added for new and existing reports

.. image:: /images/releases/500/reportsHome.png


All New Features
----------------

- Amazon: Processing of costing (CUR) reports for detailed invoice costing now occurs when the cloud integration COSTING value is set to "Costing" or "Costing and Reservations". Previously report processing only took place if the cloud integration was configured to get "Costing and Reservations"
- Amazon: ROI (return on investment) figure displayed in Reservation Recommendations and Savings Plan Recommendations tables on Amazon Cloud detail pages. This is the length of time required to make back the original investment when reserving instances or purchasing a savings plan
- Amazon: Routes on AWS routers are now editable (Infrastructure > Network > Selected AWS Network > Routing tab > Pencil icon) in addition to viewing, creating and deleting which could be done previously
- Clouds: Canonical BMaaS Cloud integration added
- Core: Major optimizations for Cloud synchronization resulting in faster sync times 
- Guidance: Recommendations can now be made based on 30, 60, or 90 day periods

- .. toggle-header:: :header: Invoices: **Highly-granular costing data surfaced into UI**

     - Added list view showing high-level detail about groups of Invoices (Operations > Costing > Invoices)
     - Invoice list page results can be filtered and customized with desired output columns
     - Click into an Invoice from the list page to see a detail page for the Invoice

- Java: Ugpraded to version 8u265 for VM node packages
- Networks: vCloud Director-managed IP Pools from privately-assigned Clouds are now shown on the Subtenant's IP Pools page (Infrastructure > Networks > IP Pools)

- .. toggle-header:: :header: Personas: **Service Catalog Persona Added**

     - Simplified Service Catalog Persona created for easy provisioning of curated Instance and Blueprint configurations
     - Add items to a cart and "check out" to begin the provisioning process
     - Users can make configuration selections when ordering based on Option Types defined for the catalog item
     - Service Catalog Dashboard displays recent orders, featured catalog items, and an abbreviated list of inventory items
     - Inventory list view for user-owned Instances and Apps
     - View details on user-owned Instances and Apps
     - Control catalog selection and access to specific personas through Role permissions
     - Catalog items with invalid configuration cannot be ordered and friendly error messages are surfaced to aid troubleshooting

- Plugins: Add custom plugins to |morpheus| by uploading them in Administration > Integrations > Plugins. See documentation on the plugin architecture SDK for details on getting started with plugin development

- .. toggle-header:: :header: Reports: **Reports UI and feature set overhauled**

     - New report types added
     - Landing page for Reports now lists report types with buttons to run a selected report type now or schedule one on a recurring basis
     - Clicking into a report type lists all viewable runs of that report type, one-off runs can be executed, schedules for that report type can be viewed or deleted
     - See Reports section of |morpheus| docs for complete feature guides
     - Many report types now allow filtering to include or exclude resources based on multiple tags rather than just one

- .. toggle-header:: :header: Reports: **New report types added**

     Several new report types are added, note that the Amazon costing reports listed below are not shown for users that don't have an Amazon cloud integration exposed to them:

     - Guidance
     - Migration Planning
     - Time Series Cost
     - Amazon Reservation Coverage
     - Amazon Reservation Utilization
     - Amazon Savings Inventory Summary
     - Amazon Savings Plan Coverage
     - Amazon Savings Plan Utilization

- .. toggle-header:: :header: Reports: **Automated Generation of Custom Reports**

     - Click :guilabel:`SCHEDULE` in the row for the report type you wish to run
     - After completing required fields to configure the report, select any default or custom execution schedule from the "SCHEDULE" dropdown list to set the interval. Reports can also be scheduled to be run once at a specific date and time
     - In the future, automated runs will appear for viewing or exporting in the list of reports

     .. image:: /images/releases/500/scheduleReport.png

- .. toggle-header:: :header: Roles: **Changes to User Role Permissions**

     - Permission added for Alarms (Operations: Alarms), previously this permission was dictated by Operations: Health
     - Operations: Health permission relabeled as Admin: Health
     - Permission added to grant access to global guidance thresholds (Admin: Guidance Settings)
     - Permission added for integration of custom plugins

- .. toggle-header:: :header: Self Service: **Catalog Item Builder Added**

     - Self Service section added at Tools > Self Service
     - Configure Instances or Blueprints which will appear as selections when viewing the Service Catalog Persona
     - Control access to the builder through Role permissions and Tenant visibility
     - Select Option Types from the |morpheus| Library for user-selected configuration on provisioning

- Settings: Cloud refresh interval is now user-configurable, the settings can be changed in Administration > Settings > Appliance

- .. toggle-header:: :header: UI: **Reorganization of UI Menu**

     - Health section moved from Operations menu to Administration menu
     - Alarms tab moved from Health to Activity (Operations > Activity)
     - Budgets section moved to a tab in Costing (Operations > Costing) rather than having its own top-level menu selection in the Operations menu
     - Usage tab moved from Activity (Operations > Activity) to Costing (Operations > Costing)
     - Settings (Administration > Settings) now holds settings tabs for Monitoring, Backups, Logs, Provisioning, Environments and Software Licenses rather than keeping them in distinct sections under the Administration menu

- UI: The User Detail page (Administration > Users > Selected User) now includes tabs for viewing Persona and Catalog Item access specific to the user
- UI: The Instance Detail page now has a maximum number of tabbed sections with an overflow element to handle any additional tabs

- .. toggle-header:: :header: UI: **Expansion of Advanced Lists Tables**

     **Advanced Lists tables added to:**

     - Load balancers list page at Infrastructure > Load Balancers
     - Clusters list page at Infrastructure > Clusters

- vCloud Director: Create and delete Snapshots in a vCD Cloud

- .. toggle-header:: :header: Veeam: **Backup Jobs can now be deleted**

     - Backup Jobs are deleted from the :guilabel:`ACTIONS` menu on the Backup Jobs list page (Backups > Jobs)
     - Delete action existed previously but, due to Veeam API limitations, |morpheus| could only disable the job

- Windows: Windows VMs will now auto-expand their root storage partitions to fill drive space, previously this was done manually

Fixes
-----

- Azure: Fixed AKS Cluster Deployment Failure when Azure Cloud is scoped to single Resource Group
- Azure: Fixed issue with deleting a Resource Group created from an ARM App when an Azure Cloud is scoped to a single Resource Group.
- Azure: Fixed provisioning issue when specifying mixed managed disk types
- Azure: Fixed user provided disk labels being overwritten with external_id names
- Budgets: Fixed current years actuals displaying in future years budgets
- CLI: Added more specific error when specified cores exceed policy allowance.
- CLI: Fixed issue with blueprint creation via cli using yaml or json file
- ElasticSearch: Added auto-reconnect or rebuilding of client on runtime exception 
- NSX-T: Fixed issue with NSX-T IP Pool creation
- Reconfigure: Fixed issue where field values were not being updated to default values when selecting plans with customizable inputs.
- SCVMM: Fixed issue where selected SCVMM Cloud was not being passed in SCVMM VM config 
- SCVVM: Fixed Instance reconfigure startup memory and fixed memory allocation
- VCD: Fixed Image Sync not working for Catalogs with spaces in the Catalog name
