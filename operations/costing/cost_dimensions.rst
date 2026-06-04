Cost Dimensions
===============

Overview
--------

|morpheus| syncs cost allocation data from cloud providers that support native cost categorization. This data is stored on invoice line items and can be used to filter and group costs in the Time Series Cost report.

Three cost dimensions are available:

- **Cost Project** — maps to the "Project" cost category from the cloud provider
- **Cost Team** — maps to the "Team" cost category from the cloud provider
- **Cost Environment** — maps to the "Environment" cost category from the cloud provider

These dimensions are populated automatically during costing sync. There is no manual configuration of dimension values within |morpheus|—they are derived entirely from cost category data provided by the cloud.

Supported Cloud Providers
-------------------------

**Amazon Web Services (AWS)**

AWS Cost Categories named "Project", "Team", and "Environment" are synced into the corresponding |morpheus| cost dimensions during the costing sync process. To use cost dimensions with AWS:

#. Configure Cost Categories in the AWS Billing console with category names ``Project``, ``Team``, and/or ``Environment``
#. Define rules within each Cost Category to assign cost values (e.g., based on tags, accounts, or services)
#. Enable costing sync in |morpheus| (Infrastructure > Clouds > Edit > set **COSTING** to "Sync Costing")

Once synced, the dimension values appear as filter and Group By options in costing reports.

.. NOTE:: Only AWS is currently supported for cost dimension sync. Other cloud providers do not populate these fields.

Using Cost Dimensions in Reports
---------------------------------

Cost dimensions are available as **Group By** options in the Time Series Cost report. To use them:

#. Navigate to |OpRep|
#. Run a Time Series Cost report
#. Select **Cost Project**, **Cost Team**, or **Cost Environment** from the **Group By** dropdown
#. Optionally use the corresponding filter to limit results to specific dimension values

The full list of Group By options available in the Time Series Cost report:

- Service
- Region
- Cloud
- Plan
- Usage Type
- Cost Project
- Cost Team
- Cost Environment
- Item Action
- Availability Zone
- Platform
- Purchase Option
- Tenancy
- Database Engine
- Billing Entity
- Seller
- Item Type
- Tag (requires specifying a tag name)

Invoice line items that have no value for a cost dimension are grouped under "Undefined" when filtering or grouping by that dimension.
