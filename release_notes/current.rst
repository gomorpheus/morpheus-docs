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

- .. toggle-header:: :header: Reports: **Reports UI overhauled**

     - New report types added
     - Landing page for Reports now lists report types with buttons to run a selected report type now or schedule one on a recurring basis
     - Clicking into a report type lists all viewable runs of that report type, one-off runs can be executed, schedules for that report type can be viewed or deleted
     - See Reports section of |morpheus| docs

- Reports: Many report types now allow filtering to include or exclude resources based on multiple tags rather than just one

- .. toggle-header:: :header: Reports: **Automated Generation of Custom Reports**

     - Click :guilabel:`SCHEDULE` in the row for the report type you wish to run
     - After completing required fields to configure the report, select any default or custom execution schedule from the "SCHEDULE" dropdown list to set the interval
     - In the future, automated runs will appear for viewing or exporting in the list of reports

     .. image:: /images/releases/500/scheduleReport.png

- .. toggle-header:: :header: Roles: **Changes to User Role Permissions**

     - Permission added for Alarms (Operations: Alarms), previously this permission was dictated by Operations: Health
     - Operations: Health permission relabeled as Admin: Health

- .. toggle-header:: :header: UI: **Reorganization of UI Menu**

     - Health section moved from Operations menu to Administration menu
     - Alarms tab moved from Health to Activity (Operations > Activity)
     - Budgets section moved to a tab in Costing (Operations > Costing) rather than having its own top-level menu selection in the Operations menu
     - Usage tab moved from Activity (Operations > Activity) to Costing (Operations > Costing)
     - Settings (Administration > Settings) now holds settings tabs for Monitoring, Backups, Logs, Provisioning, Environments and Software Licenses rather than keeping them in distinct sections under the Administration menu

- .. toggle-header:: :header: UI: **Expansion of Advanced Lists Tables**

     **Advanced Lists tables added to:**

      - Load balancers list page at Infrastructure > Load Balancers
      - Clusters lis page at Infrastructure > Clusters

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
