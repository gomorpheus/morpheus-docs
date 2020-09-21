.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading to |morpheus|

|morpheus| UI Updates
=====================

Highlights
----------

New Features
------------

- Amazon: Processing of costing (CUR) reports for detailed invoice costing now occurs when the cloud integration COSTING value is set to "Costing" or "Costing and Reservations". Previously report processing only took place if the cloud integration was configured to get "Costing and Reservations"
- Amazon: ROI (return on investment) figure displayed in Reservation Recommendations and Savings Plan Recommendations tables on Amazon Cloud detail pages. This is the length of time required to make back the original investment when reserving instances or purchasing a savings plan
- Amazon:
- Clouds: Canonical BMaaS Cloud integration type added
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

- Reports: Many report types now allow filtering to include or exclude resources based on multiple tags rather than just one

- .. toggle-header:: :header: Reports: **Automated Generation of Custom Reports**

     - Click :guilabel:`SCHEDULE` in the row for the report type you wish to run
     - After completing required fields to configure the report, select any default or custom execution schedule from the "SCHEDULE" dropdown list to set the interval. Reports can also be scheduled to be run once at a specific date and time
     - In the future, automated runs will appear for viewing or exporting in the list of reports

     .. image:: /images/releases/500/scheduleReport.png

- .. toggle-header:: :header: Reports: **Reports UI and feature set overhauled**

     - New report types added
     - Landing page for Reports now lists report types with buttons to run a selected report type now or schedule one on a recurring basis
     - Clicking into a report type lists all viewable runs of that report type, one-off runs can be executed, schedules for that report type can be viewed or deleted
     - See Reports section of |morpheus| docs for complete feature guides

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

Fixes
-----

|morpheus| API Updates
======================

API Enhancements
----------------

API Fixes
---------

|morpheus| CLI Updates
======================

CLI Enhancements
----------------

CLI Fixes
---------
