Tenant Usage Report
===================

The Tenant Usage Report is designed to give summary usage details for all Tenants or a single selected Tenant within the |morpheus| environment.

Stats
-----

- **Hosts:** The total number of managed and unmanaged Hosts and VMs associated with all selected Tenants
- **Instances:** The total number of managed Instances associated with the selected Tenant
- **Peak Compute:** The highest compute utilization for a single host associated with all Tenants regardless of the compute utilization for any other host
- **Total Memory:** The total memory allocated to all hosts associated with the Tenant
- **Total Storage:** The total storage allocated to all hosts associated with the Tenant

Utilization
-----------

- **Average Utilization:** Displays the average memory or storage utilization percentage, whichever is higher
- **Peak Utilization:** Displays the maximum memory or storage utilization percentage, whichever is higher

Tenants
-------

This report can be run against either one or all Tenants in the |morpheus| environment. When run against a single Tenant, much of this information is duplicated from the aggregate data area above. When run against all Tenants, see a breakdown per Tenant in this area compared with the aggregate data for all Tenants above.

- **Hosts:** The total number of managed and unmanaged hosts and VMs associated with the indicated Tenant
- **Instances:** The total number of managed Instances associated with the indicated Tenant
- **Utilization:** Displays the average memory or storage utilization percentage for the Tenant, whichever is higher
- **Peak Compute:** The highest compute utilization for a single host associated with the indicated Tenant regardless of the compute utilization for any other host
- **Average Memory:** The average memory use percentage for all hosts associated with the Tenant
- **Average Storage:** The average storage use percentage for all hosts associated with the Tenant

.. image:: /images/operations/reports/report_types/tenantUsage.png
