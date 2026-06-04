Cost Dimensions
===============

Overview
--------

|morpheus| supports cost allocation through configurable dimensions that allow organizations to attribute cloud spending to specific business units, projects, and environments. These cost dimensions—**Cost Project**, **Cost Team**, and **Cost Environment**—enable chargeback and showback reporting across the platform.

Cost dimensions appear as filter and grouping options in reports (such as the Time Series Cost report), invoices, and analytics dashboards. They allow administrators to slice cost data along organizational boundaries regardless of the underlying cloud infrastructure topology.

Cost Project
------------

Cost Projects represent organizational projects or initiatives to which cloud spending can be attributed. They are useful for:

- Tracking costs associated with specific development efforts or business initiatives
- Enabling project-level chargeback to business stakeholders
- Comparing projected vs. actual spend per project

Cost Projects are typically mapped through tags applied to cloud resources. When resources are tagged with a project identifier, their associated costs roll up into the Cost Project dimension for reporting.

Cost Team
---------

Cost Teams represent organizational teams or departments responsible for cloud spending. Use cases include:

- Departmental chargeback/showback reporting
- Budget allocation per team
- Identifying which teams drive the most cloud consumption

Like Cost Projects, team attribution is typically driven by resource tags or by the |morpheus| Group/Tenant structure.

Cost Environment
-----------------

Cost Environments segment spending by deployment stage or environment type (e.g., Production, Staging, Development, QA). This dimension enables:

- Comparing production vs. non-production spend ratios
- Identifying environments that may be over-provisioned
- Enforcing cost policies per environment tier

Configuration
-------------

Cost dimensions are populated through the following mechanisms:

**Tag-Based Allocation**

Resources tagged with specific key/value pairs are automatically attributed to the corresponding cost dimension. Configure tag keys for each dimension in the costing settings:

- Map a tag key (e.g., ``Project``, ``CostCenter``, ``Team``) to the appropriate cost dimension
- Resources carrying that tag will have their costs attributed accordingly
- Untagged resources appear as "Unallocated" in dimension-based reports

**Cloud-Native Cost Allocation**

For public clouds that support native cost allocation (AWS Cost Categories, Azure Cost Management tags, GCP Labels), |morpheus| syncs these allocations during costing sync and maps them to the internal cost dimension model.

Using Cost Dimensions in Reports
---------------------------------

Cost dimensions are available as **Group By** options in the following reports and views:

- **Time Series Cost Report** — Group monthly costs by Project, Team, or Environment
- **Invoice List** — Filter and sort invoices by cost dimension values
- **Analytics Dashboards** — Slice costing analytics by any configured dimension

To generate a report grouped by cost dimension:

#. Navigate to |OpRep|
#. Click :guilabel:`RUN NOW` next to the desired cost report type
#. Select the appropriate value from the **Group By** dropdown (Cost Project, Cost Team, or Cost Environment)
#. Configure any additional filters and run the report

.. NOTE:: Cost dimensions require costing sync to be enabled on at least one Cloud integration. Navigate to Infrastructure > Clouds > (Cloud) > EDIT and set the **COSTING** field to "Sync Costing" to enable cost data collection.
