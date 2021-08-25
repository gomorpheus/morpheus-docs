.. # define a hard line break for HTML
.. |br| raw:: html

   <br />

Invoices
--------

|morpheus| offers highly-granular costing data through invoices. Invoice views are highly customizable, allowing for nearly unlimited combinations of output columns and filtering. Invoices are based on monthly periods and allow you to slice costs in a highly granular way, as well as predict final monthly costs before the end of the period. As with other |morpheus| UI pages that support advanced table customization, these views can be saved to provide easy access to costing views specific to varying business needs. By default, the invoice list page will show the last three months' invoices across all clouds and invoice types but the list can be modified to target differing time periods or resource groupings. Read on in this section to discover the meaning of various invoice types and how this tool can be used to create targeted costing views.

Invoices for Public vs On-Prem Clouds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| supports live cost syncing for many public clouds, including all of the most commonly-used public clouds like Amazon AWS, Microsoft Azure, and Google Cloud Platform. For these clouds, costing sync is enabled through the COSTING field on the Add/Edit Cloud modal (Infrastructure > Clouds > selected Cloud > EDIT button). When live costs are synced from public clouds, invoices will be generated for this activity including month-to-date costs, projected monthly totals, historical cost data, and a lot more which is discussed in the following sections.

Additionally, |morpheus| has implemented a costing service for on-prem clouds to closely mirror the live costing experience through a public cloud. As with public clouds, this costing service is enabled for on-prem clouds through the COSTING field on the Add/Edit Cloud modal (Infrastructure > Clouds > selected Cloud > EDIT button). Change the setting to "Sync Costing" and save the changes to the cloud integration. From this point, costs will be aggregated into invoices for on-prem clouds in the same way as public clouds including complete line item listings, current costs for the month, month-end projections, and much more as discussed in the next sections.

Invoice List Page
^^^^^^^^^^^^^^^^^

The invoices list page shows high-level aggregate data on a group of invoices and allows you to locate a specific invoice for a deeper look. By default, invoices from the last three months across all clouds and types are shown here. Depending on settings, this page can automatically refresh itself so the list of displayed invoices and the aggregate information on them is up to date.

.. image:: /images/operations/invoices/1listInvoices.png

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
#. Click on one or more columns from the "Columns" list to add or remove an output field
#. Click "+ add view"
#. Provide a name and a description value for your new view
#. If desired, mark the box to set the new view as your default view so it appears automatically each time the invoices list page is accessed
#. Click :guilabel:`SAVE`

.. image:: /images/operations/invoices/2createViews.png

Available Output Columns
````````````````````````

When creating an invoices view, there are many output columns available to select. Consult the list below for more details on each of the available columns:

.. toggle-header:: :header: Available Output Columns: **Expand for Complete List**

  - **Invoice ID:** The unique ID in |morpheus| for the invoice
  - **Type:** The invoice type; Cloud, Container, Group, Server, Instance, Resource, User, or Volume
  - **Ref ID:** An ID for the reference object tied to the invoice (server, instance, cloud, etc.). Reference IDs are reused across invoice types so invoices referring to identical Ref IDs may not necessarily refer to the same reference object
  - **Reference:** The name of the reference object (server, cloud, user, group, etc.) tied to the invoice
  - **Cloud ID:** The internal ID for a Cloud integration in |morpheus|. This field will be blank unless the invoice references a Cloud
  - **Cloud:** The name for a Cloud integration in |morpheus|. This field will be blank unless the invoice references a Cloud
  - **Instance ID:** The internal ID for an Instance in |morpheus|. This field will be blank unless the invoice references an Instance
  - **Instance:** The name for an Instance in |morpheus|. This field will be blank unless the invoice references an Instance
  - **Server ID:** The internal ID for a server in |morpheus|. This field will be blank unless the invoice references a server
  - **Server:** The name for a server in |morpheus|. This field will be blank unless the invoice references a server
  - **Cluster ID:** The internal ID for a cluster in |morpheus|. This field will be blank unless the invoice references a cluster
  - **Cluster:** The name for a cluster in |morpheus|. This field will be blank unless the invoice references a cluster
  - **Plan ID:** The internal ID for a service plan in |morpheus|. This field will be populated only for invoices that reference an object which would be associated with a service plan (server, Instance, container, etc.).
  - **Plan:** The name for a service plan in |morpheus|. This field will be populated only for invoices that reference an object which would be associated with a service plan (server, Instance, container, etc.).
  - **Group ID:** The internal ID for a Group in |morpheus|. This field will be blank unless the invoice references a Group
  - **Group:** The name for a Group in |morpheus|. This field will be blank unless the invoice references a Group
  - **User ID:** The internal ID for a User in |morpheus|. This field will be blank unless the invoice references a User.
  - **User:** The name for a User in |morpheus|. This field will be blank unless the invoice references a User.
  - **Tenant ID:** The internal ID for the |morpheus| Tenant which owns the reference object
  - **Tenant:** The name of the |morpheus| Tenant which owns the reference object
  - **Period:** The monthly period during which the invoice was generated
  - **Interval:** The length of the invoice billing period, currently all invoices are generated at a one-month interval
  - **Start Date:** The start date and time for the invoice period, typically the first of the month at midnight
  - **End Date:** The end date and time for the invoice period, typically the last day of the month at midnight
  - **Ref Start:** The date and time the reference object is created or the start of the invoicing period if the reference object existed prior to the start of the invoicing period
  - **Ref End:** The date and time the reference object is decommissioned or the end of the invoicing period if the reference object still existed at the end of the period
  - **Compute Cost:** The actual compute costs for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Storage Cost:** The actual storage costs for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Network Cost:** The actual network costs for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Extra Cost:** The actual additional costs for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **MTD Cost:** The actual month-to-date costs for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Total Cost:** The actual total costs for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Metered Compute Cost:** Compute costs determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Storage Cost:** Storage costs determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Network Cost:** Network costs determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Extra Cost:** Additional costs determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered MTD Cost:** Month-to-date costs determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Total Cost:** Total costs determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Compute Price:** The actual compute price (cost plus markup) for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Storage Price:** The actual storage price (cost plus markup) for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Network Price::** The actual network price (cost plus markup) for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Extra Price:** The actual additional price (cost plus markup) for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **MTD Price:** The actual month-to-date price (cost plus markup) for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Total Price:** The actual total price (cost plus markup) for the invoice (from public cloud costing API when available or from an on-prem cloud with "Sync Costing" enabled)
  - **Metered Compute Price:** Compute price (cost plus markup) determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Storage Price:** Storage price (cost plus markup) determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Network Price:** Network price (cost plus markup) determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Extra Price:** Additional price (cost plus markup) determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered MTD Price:** Month-to-date price (cost plus markup) determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Metered Total Price:** Total price (cost plus markup) determined by |morpheus| usage and pricing data (when live pricing data is not available, such as with an on-prem cloud without "Sync Costing" enabled)
  - **Active:** Indicates whether or not the reference object is currently existing and active
  - **Date Created:** The date and time the invoice is created
  - **Last Updated:** The date and time the invoice was last updated

|br|

Invoice Types
^^^^^^^^^^^^^

Invoices can reference any of the |morpheus| workload element types or resource reference types in the list below. Some invoice types are broader and may account for resource costs calculated in other narrower invoice types. For instance, a container-type invoice returns costs for a single node of an Instance while an Instance-type invoice for the same period may be including costs for that same single node. The invoices list view can be filtered to show just one type or all types. Complete descriptions of each invoice type are included below:

- Cloud: In |morpheus|, a Cloud is any connection into a public cloud, private cloud, hybrid cloud, or bare metal server
- Container: A single node of a service, in other words, a single node of a |morpheus| Instance. This could be a virtual machine or Docker container which is part of a |morpheus|-managed Instance
- Group: In |morpheus|, Groups define which resources a user has access to through their role. Clouds are added to Groups and users access Clouds to which their roles give access
- Server: A server refers to any individual host, virtual machine, or bare metal server that is inventoried or managed by |morpheus|. This can include servers which are parts of |morpheus|-managed Instances or inventoried servers from integrated Clouds
- Instance: A set of containers or virtual machines which correlate to a single horizontally-scalable entity. This could be a single VM or it could be many VMs operating as a service
- Resource: Resource-type invoices are generated when |morpheus| cannot determine that the referenced costs belong to any of the other resource reference types in this list
- User: User-type invoices aggregate the costs of resources owned by a specific |morpheus| user during the invoicing period
- Volume: When possible, costs will be tied to known volumes and a volume-type invoice is generated as a result

Invoice Detail Page
^^^^^^^^^^^^^^^^^^^

Summary
```````

The summary tab of the invoice detail page displays a great deal of reference information about the resource identified by the invoice. This will vary depending on the type of resource. In addition, total and projected costs are displayed along with cost breakdowns for compute, storage, network, and other categories. Month-to-date totals and final month projections are given.

.. image:: /images/operations/invoices/3invoiceSummary.png

History
```````

The history tab displays the costs and prices for the associated resource over time. This tab is especially valuable for resources that have existed through at least a few invoicing periods to show changes over time. In addition, cost breakdowns for compute, storage, network, and other categories are shown for each invoicing period. These costs can be displayed visually through graphs.

.. image:: /images/operations/invoices/4invoiceHistory.png

Line Items
``````````

For supported resource types, |morpheus| includes a tab to display all costing line items. This provides the user with a complete list of line items that make up the costing totals on the invoice.

.. image:: /images/operations/invoices/5invoiceLineItem.png
