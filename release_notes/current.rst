.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

New Features
------------

Appliance Compatibility: Ubuntu 20.04 appliance installation is now supported

- .. toggle-header:: :header: **Multi-year Budgets with Custom Fiscal Years**

    - Budgets based on a yearly interval can now start on a month other than January
    - Multi-year budgets, up to three years, are now supported

- NSX-T: Priority field exposed for Firewall rules
- NSX-V: Create and manage SNAT rules from the NAT tab of the Edge Gateway detail page of an NSX-V network integration"
- Prices: Instances in a suspended state no longer incur prices set to be incurred "While Running" just as stopped Instances do not incur them
- Tags: Morpheus `naming variables <https://docs.morpheusdata.com/en/latest/troubleshooting/Variables_Examples.html?highlight=naming%20policy#pre-provision-vars>`_ can be used as tag values for Instances and VMs/servers at provision time
- Virtual Images: A “FIPS Compliant Image?” checkbox has been added to the Add/Edit Virtual Image modal. When checked, Morpheus will install the FIPS-compliant Agent package

Fixes
-----



API & CLI Enhancements
----------------------

- Dashboard: dashboard command added to give a high level overview of Morpheus activities such as aggregate Instance usage data, monitoring alerts, backup event alerts, recent user activity, and more

- .. toggle-header:: :header: **Invoice Tagging and Tenant Data Filtering Improvements**

    - Invoice tags can now be updated, added and removed through API/CLI
    - Lists of invoices can be filtered by tags (API only, for now)
    - Subtenant users now only see prices (not costs) for Instances provisioned to Clouds owned by the Master Tenant and assigned to the Subtenant when calling the Invoices API
