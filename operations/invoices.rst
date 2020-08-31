Invoices
--------

|morpheus| invoices offer highly-granular costing data through invoices. Invoice views are highly customizable, allowing for nearly unlimited combinations of output columns and filtering. Invoices are based on monthly periods and allow you to slice costs in a highly granular way, as well as predict final monthly costs before the end of the period. As with other |morpheus| UI pages that support advanced table customization, these views can be saved to provide easy access to costing views specific to varying business needs. By default, the invoice list page will show the last three months' invoices across all clouds and invoice types but the list can be modified to target differing time periods or resource groupings. Read on in this section to discover the meaning of various invoice types and how this tool can be used to create targeted costing views.

Invoice List Page
^^^^^^^^^^^^^^^^^

The invoices list page shows high-level aggregate data on a group of invoices and allows you to locate a specific invoice for a deeper look. By default, invoices from the last three months across all clouds and types are shown here. Depending on settings, this page can automatically refresh itself so the list of displayed invoices and the aggregate information on them is up to date.

Aggregated Invoice Data
```````````````````````

The following aggregate totals are displayed for all invoices picked up by set filters:

- **Periods:** The total number of months in the period determined by your start and end date filters. If no start and end dates are set, a three month period will be shown. If a one-month period is selected, the name of that month (ex. Aug 2020) is shown
- **Total Invoices:** The total number of invoices captured by current filters
- **MTD Cost:** The combined month-to-date cost for all invoices captured by current filters
- **Total Cost:** The expected total month-end cost for all invoices captured by current filters

Creating Views
^^^^^^^^^^^^^^

Invoice list views are highly-customizable allowing for virtually limitless combinations of output columns and filtering. A common set of output columns is provided in a default view but users can add and remove columns from a large list of data points and even save multiple views for easy access to different data sets. Any of your stored views can be set as the default to be displayed each time the invoices list page is active.

To create a new invoices view:

#. Click the gear icon (:guilabel:`⚙`)
#. Click on a column from the "Columns" list to add or remove an output field
#. Repeat steps one and two above as many times as needed to complete the desired view
#. Click the gear icon (:guilabel:`⚙`) once more
#. Click "+ add view"
#. Provide a name and a description value for your new view
#. If desired, mark the box to set the new view as your default view so it appears automatically each time the invoices list page is accessed
#. Click :guilabel:`SAVE`

Available Output Columns
````````````````````````

When creating an invoices view, there are many output columns available to select. Consult the list below for more details on each of the available columns:

- Invoice ID: The unique ID in |moprheus| for the invoice
- Type: The invoice type; Cloud, Container, Group, Server, Instance, Resource, User, or Volume
- Ref ID: An ID for the reference object the invoice is tied to (server, instance, cloud, etc.). Reference IDs are reused across invoice types so invoices referring to identical Ref IDs may not necessarily refer to the same reference object
- Reference: 
- Cloud ID
- Cloud
- Instance ID
- Instance
- Server ID
- Server
- Cluster ID
- Cluster
- Plan ID
- Plan
- Group ID
- Group
- User ID
- User
- Tenant ID
- Tenant
- Period
- Interval
- Start Date
- End Date
- Ref Start
- Ref End
- Compute Cost
- Storage Cost
- Network Cost
- Extra Cost
- MTD Cost
- Total Cost
- Metered Storage Cost
- Metered Network Cost
- Metered Extra Cost
- Metered MTD Cost
- Metered Total Cost
- Compute Price
- Storage Price
- Network Price
- Extra Price
- MTD Price
- Total Price
- Metered Storage Price
- Metered Network Price
- Metered Extra Price
- Metered MTD Price
- Metered Total Price
- Active
- Date Created
- Last Updated

Invoice Types
^^^^^^^^^^^^^

Invoice Detail Page
^^^^^^^^^^^^^^^^^^^

Summary
```````

History
```````

Line Items
``````````
