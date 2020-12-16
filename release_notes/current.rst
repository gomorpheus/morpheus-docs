.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

New Features
------------

- .. toggle-header:: :header: **Budget Enhancements**

    - Budgets based on a yearly interval can now start on a month other than January
    - Multi-year budgets, up to three years, are now supported

- NSX-V: Create and manage SNAT rules from the NAT tab of the Edge Gateway detail page of an NSX-V network integration
- Tags: Morpheus `naming variables <https://docs.morpheusdata.com/en/latest/troubleshooting/Variables_Examples.html?highlight=naming%20policy#pre-provision-vars>`_ can be used as tag values for Instances and VMs/servers at provision time
- Virtual Images: A “FIPS Compliant Image?” checkbox has been added to the Add/Edit Virtual Image modal. When checked, Morpheus will install the FIPS-compliant Agent package

Fixes
-----



API & CLI Enhancements
----------------------

- Dashboard: dashboard command added to give a high level overview of Morpheus activities such as aggregate Instance usage data, monitoring alerts, backup event alerts, recent user activity, and more

- .. toggle-header:: :header: **Invoices Improvements**

    - Invoice tags can now be updated, added and removed through API/CLI
    - Lists of invoices can be filtered by tags (API only, for now)
    - Subtenant users now only see prices (not costs) for Instances provisioned to Clouds owned by the Master Tenant and assigned to the Subtenant when calling the Invoices API
