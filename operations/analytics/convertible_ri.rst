Amazon Convertible RI Analytics
================================

.. tier-note:: Advanced, Enterprise
   :exclude: Essentials

   Analytics dashboards are an Advanced+ feature.

Overview
--------

The Amazon Convertible RI (Reserved Instance) Analytics dashboard helps administrators optimize their AWS Reserved Instance portfolio by identifying underutilized convertible reservations and recommending conversions to better match current workload demands.

Convertible RIs allow you to exchange one reservation for another with different instance attributes (family, OS, tenancy, payment option), making them ideal for dynamic workloads. This dashboard analyzes current RI utilization and suggests conversion opportunities.

Navigate to Operations > Analytics and select **Amazon Convertible RI Analysis** from the analytics type list.

Filters
-------

CLOUD
  Select a specific AWS Cloud integration with costing enabled. Only AWS clouds with costing sync active are available in this dropdown.

Dashboard Output
----------------

Conversion Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When |morpheus| identifies convertible RI capacity that could be better utilized through conversion, a recommendations table is displayed with the following columns:

- **Name** — The current RI type/family that has excess or insufficient capacity
- **Units Needed** — The number of normalized units of capacity required to meet current demand
- **Convert Plan** — The recommended RI type to convert to
- **Convert Units** — The number of normalized units that would be converted

If no conversion source is available for a shortage, the dashboard recommends purchasing new reservations to cover the gap.

Underutilized Items
^^^^^^^^^^^^^^^^^^^

A second table displays convertible RIs that are currently underutilized:

- **Name** — The RI type/family
- **Current Units** — The current normalized unit allocation
- **Units After Conversions** — The projected unit count after recommended conversions are applied

Interpreting Results
--------------------

- **Units Needed > 0** indicates demand exceeds current RI capacity for that type; consider converting excess capacity from other types or purchasing new reservations
- **Units After Conversions < Current Units** indicates that some capacity from this RI type is recommended for conversion to other types with higher demand
- An empty recommendations table indicates the current convertible RI portfolio is optimally aligned with workload demand

Prerequisites
-------------

- An Amazon AWS Cloud integration must be configured (Infrastructure > Clouds)
- **Costing** must be set to "Sync Costing" on the AWS Cloud configuration
- The AWS account must have active Convertible Reserved Instances
- The IAM credentials used for the integration must have ``ce:GetReservationUtilization`` and ``ce:GetReservationCoverage`` permissions

.. NOTE:: RI analytics data is synced from AWS Cost Explorer. There may be up to a 24-hour delay between AWS console data and |morpheus| analytics.
