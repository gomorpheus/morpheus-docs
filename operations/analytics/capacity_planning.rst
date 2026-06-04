Capacity Planning Analytics
============================

.. tier-note:: Advanced, Enterprise
   :exclude: Essentials

   Analytics dashboards are an Advanced+ feature.

Overview
--------

The Capacity Planning Analytics dashboard projects future infrastructure resource needs based on current utilization trends. It displays memory, storage, and CPU capacity charts with trend projections, helping administrators anticipate when additional capacity will be needed and which hosts are approaching saturation.

Navigate to |OpAna| and select **Capacity Planning** from the analytics type list.

Filters
-------

TENANT
  Filter capacity data to a specific Tenant (multi-tenant environments only).

CLOUD
  Filter capacity data to a specific Cloud integration. The Cloud dropdown is dependent on the selected Tenant filter.

Dashboard Output
----------------

Projection Charts
^^^^^^^^^^^^^^^^^

The dashboard renders three area charts showing historical and projected capacity:

**Memory Capacity**

Displays historical memory utilization across filtered hosts with a trend projection. The chart shows:

- Historical memory consumption over time
- Projected memory demand based on growth trends
- Available memory capacity threshold

**Storage Capacity**

Displays historical storage utilization with trend projections:

- Historical storage consumption over time
- Projected storage demand
- Available storage capacity threshold

**CPU Capacity**

Displays historical CPU utilization with trend projections:

- Historical CPU consumption over time
- Projected CPU demand
- Available CPU capacity threshold

Host Server List
^^^^^^^^^^^^^^^^

Below the projection charts, a table lists individual hosts matching the current filters:

- **Power** — The current power state of the host
- **OS** — The host operating system
- **Name** — The host name
- **Type** — The host/hypervisor type
- **Cloud** — The Cloud integration the host belongs to
- **Price** — The monthly cost associated with the host
- **Utilization** — The current utilization percentage for the selected metric (Memory, CPU, or Overall)

The utilization column type can be toggled between RAM, CPU, and Overall (peak) utilization.

Interpreting Projections
------------------------

- **Crossing threshold lines** in the projection charts indicate when capacity is expected to be exhausted at current growth rates
- **Flattening trends** suggest workload growth has stabilized and current capacity may be sufficient
- **Hosts with high utilization** in the server list are candidates for resource expansion or workload redistribution

Prerequisites
-------------

- At least one Cloud integration must be configured with compute hosts
- **Stats collection** must be enabled on managed hosts for accurate utilization data
- Historical data of at least 30 days provides more accurate projections

.. TIP:: Use Capacity Planning in conjunction with the Guidance engine (|OpGui|) to both anticipate future needs and receive automated recommendations for current right-sizing opportunities.
