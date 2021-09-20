Reports
=======

Overview
--------

|morpheus| offers 28 different report types which are designed to slice up costing and usage across Clouds, Tenants, and more. Reports can be run on-demand as needed or can be scheduled to run on certain intervals to be viewed at a later time. The list of available report types can be viewed at Operations > Reports.

.. image:: /images/operations/reports/1reportList.png

Report Types
------------

**ACCOUNT INVENTORY**

  - Tenant Inventory Summary

**CLOUD USAGE**

  - Cloud Usage
  - Cloud Usage App Summary
  - Cloud Usage Instance Type Summary
  - `Tenant Usage <https://docs.morpheusdata.com/en/latest/operations/report_types/tenant_usage.html>`_

**CLOUD COST**

  - Amazon Reservation Coverage
  - Amazon Reservation Utilization
  - Amazon Savings Inventory Summary
  - Amazon Savings Plan Coverage
  - Amazon Savings Plan Utilization
  - Application Cost
  - Cloud Cost
  - Group Cost
  - Instance Cost
  - Invoice Details
  - Tenant Cost
  - Time Series Cost

**INFRASTRUCTURE INVENTORY**

  - Cloud Inventory Summary
  - Container Host Inventory Summary
  - Group Inventory Summary
  - Guidance
  - Hypervisor Inventory Summary
  - Migration Planning
  - Tenant Resource Allocation

**PROVISIONING INVENTORY**

  - Instance Inventory Summary
  - Software Inventory
  - Software Inventory By Server
  - Virtual Machine Inventory Summary
  - Workload Summary

By clicking into a report type, users can see any previous runs and active report schedules. New on-demand runs and new schedules of the selected report type can be created, edited, or deleted from here. The next few sections go into creating, editing, scheduling, viewing, and deleting reports in greater detail.

Create Reports
--------------

To create a new report, navigate to the report type list page (Operations > Reports). Click :guilabel:`RUN NOW` to the right of the specific report type to bring up the wizard to run that particular report. The required and optional fields to run the selected report type will appear, for example, the configuration panel for the Instance Cost report is shown below:

.. image:: /images/operations/reports/2reportExample.png
  :width: 50%

In this case, we can choose to scope the report by start and end dates, Groups, Clouds, Tenants, and can specific include or omit Instances based on tags. Once the report is run, it will be visible in the list of Instance Cost reports and all reports until deleted.

Schedule Reports
----------------

In addition to running on-demand reports, |morpheus| also allows reports to be scheduled. This allows you to save report configuration and have access to refreshed information on the schedule you need.

The process of scheduling a report is nearly identical to running on on-demand. From the report type list page (Operations > Reports) click :guilabel:`SCHEDULE` to the right of the report type you wish to schedule. The required and optional fields to schedule the selected report type will appear, for example, the configuration panel for the Instance Cost report is shown below:

.. image:: /images/operations/reports/3scheduleExample.png
  :width: 50%

In this case, we can choose to scope the report by start and end dates, Groups, Clouds, Tenants, and can specific include or omit Instances based on tags. Additionally, we select the time schedule on which this report should automatically run.

.. NOTE:: |morpheus| includes three schedules by default: Date and Time (run once at the specified time), Daily at Midnight, and Weekly on Sunday at Midnight. Any other listed scheduling periods are user-configured execution schedules (Provisioning > Automation > Execute Scheduling). Create a new execution schedule if none of the existing schedules work for your reporting needs.

Viewing Results
---------------

A list of all report runs is viewable on the Results tab of the report types list page (Operations > Reports). To view the report itself, click on the hyperlinked report filters. Only reports that are ready for viewing will have an active hyperlink on their filters. In addition to report filters, the run date, report type, creating user, and run status are shown. Click on any of these headers to filter the report list by that column in either ascending or descending order. Any report can be deleted by clicking on the trash can icon at the end of its row.

.. image:: /images/operations/reports/4resultsList.png

Viewing Schedules
-----------------

A list of all scheduled report runs can be viewed in the Scheduled tab of the report types list page (Operations > Reports). The friendly name of the report schedule is displayed along with the report type, last run time, next run time, and success status of the previous run. Schedules can be edited or deleted by clicking on the pencil or trash can icon, respectively. We can also view the most recent run of a given schedule (if it was successful) by clicking on the hyperlinked "last run" value.
