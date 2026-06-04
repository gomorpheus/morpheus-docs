Time Series Cost Report
=======================

The Time Series Cost report visualizes cloud spending over time, breaking down costs by month and allowing administrators to identify spending trends, anomalies, and seasonal patterns across their infrastructure. The report renders a column chart displaying usage over time alongside a detailed cost table.

Configuration
-------------

To run a Time Series Cost report, navigate to Operations > Reports and click :guilabel:`RUN NOW` next to **Time Series Cost**. The following configuration options are available:

START MONTH
  The beginning of the reporting period. Select the month/year from which to start tracking costs.

END MONTH
  The end of the reporting period. Select the final month/year to include in the report.

GROUP BY
  Optionally group cost data by a specific dimension. Available Group By options include:

  - **Service** — Group costs by cloud service type (e.g., Compute, Storage, Database)
  - **Region** — Group costs by cloud region
  - **Plan** — Group costs by service plan
  - **Usage Type** — Group costs by the type of usage (e.g., on-demand, reserved, spot)
  - **Cost Project** — Group costs by project allocation tag
  - **Cost Team** — Group costs by team allocation tag
  - **Cost Environment** — Group costs by environment allocation tag

CLOUD
  Filter the report to a specific Cloud integration or leave blank for all Clouds.

GROUP
  Filter the report to a specific Group.

TENANT
  Filter the report to a specific Tenant (multi-tenant environments only).

TAGS
  Include or exclude resources based on tag key/value pairs.

Report Output
-------------

**Chart**

The report generates a column chart displaying monthly costs over the selected time period. When a Group By dimension is selected, each category is rendered as a separate series in the chart with a color-coded legend.

**Cost Table**

Below the chart, a detailed table displays:

- **Period columns** — One column per month in the selected range showing the cost for that period
- **Group By column** — When grouping is applied, the first column identifies the grouping dimension value (e.g., the region name, service type, or team name)
- **Total** — The aggregate cost across all periods for each row

All monetary values are displayed in the Tenant's configured currency.

Scheduling
----------

To schedule this report for periodic generation, click :guilabel:`SCHEDULE` next to **Time Series Cost** on the report types list. In addition to the configuration fields above, provide:

SCHEDULE
  The run frequency (e.g., Daily, Weekly, Monthly).

.. NOTE:: Scheduled reports retain their configuration and generate fresh results on each run. Results are available in the report history for the Time Series Cost report type.

Use Cases
---------

- **Trend analysis:** Identify month-over-month spending increases across the organization
- **Chargeback/showback:** Group by Cost Team or Cost Project to attribute spending to business units
- **Regional optimization:** Group by Region to discover geographic cost imbalances
- **Service profiling:** Group by Service to understand which cloud services drive the most cost
