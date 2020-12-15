.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: This list includes improvements that were initially provided in version 4.2.5. Those feature items are marked with :superscript:`+`.

.. Small Update, omitting highlights this time
  .. include:: highlights.rst

All New Features
================

- .. toggle-header:: :header: **Azure Cloud Integration Enhancements**

    - Azure Marketplace images now synced by region rather than by Cloud:superscript:`+`
    - Azure pricing now synced by region and currency rather than Cloud:superscript:`+`
    - Azure VM sizes (Service Plans) now synced by region rather than Cloud:superscript:`+`

- .. toggle-header:: :header: **Budget Enhancements**

    - Budgets based on a yearly interval can now start on a month other than January
    - Multi-year budgets, up to three years, are now supported

- NSX-V: Create and manage SNAT rules from the NAT tab of the Edge Gateway detail page of an NSX-V network integration
- Option Types: Custom help block text can now be displayed with any Option Type
- Security Scanning: Windows support added for SCAP security scans:superscript:`+`
- ServiceNow: Plugin version 3.0 now available on the ServiceNow store, see `integration guide <https://morpheusdata.com/wp-content/uploads/content/ServiceNow-Cloud-Management-Morpheus-CMP-1.pdf>`_ for new features and complete use instructions
- Tags: |morpheus| `naming variables <https://docs.morpheusdata.com/en/latest/troubleshooting/Variables_Examples.html?highlight=naming%20policy#pre-provision-vars>`_ can be used as tag values for
Instances and VMs/servers at provision time
- Tenants: Account Name, Account Number and Customer Number values tracked on the Tenant are now resolveable from naming variables: ``${accountName}``, ``${accoountNumber}``, and ``${customerNumber}``

- .. toggle-header:: :header: **UI and Usability Improvements**

    - Tokens in forgot/reset password email now expire after seven days:superscript:`+`
    - Network REF UUID now appears on the Network tab of the server detail page for bare metal hosts

- Virtual Images: A "FIPS Compliant Image?" checkbox has been added to the Add/Edit Virtual Image modal. When checked, |morpheus| will install the FIPS-compliant Agent package

|morpheus| API & CLI Improvements
=================================

- Dashboard: ``dashboard`` command added to give a high level overview of |morpheus| activities such as aggregate Instance usage data, monitoring alerts, backup event alerts, recent user activity, and more
- Hosts: Added ability to tag servers (hosts). These are automatically updated when Instance tags are updated but useful for tagging discovered servers (currently API only):superscript:`+`
- Instances: Passing ``masked=true`` flag for tags masks the value of the tag:superscript:`+`

- .. toggle-header:: :header: **Invoices Improvements**

    - Invoice tags can now be updated, added and removed through API/CLI
    - Lists of invoices can be filtered by tags (API only, for now)
    - Subtenant users now only see prices (not costs) for Instances provisioned to Clouds owned by the Master Tenant and assigned to the Subtenant when calling the Invoices API

- Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``, previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags``:superscript:`+`
- Snapshots: Create and view snapshots:superscript:`+`

- .. toggle-header:: :header: **Virtual Images**

    - Associated ``volumes`` are returned with ``maxStorage`` viewable for each:superscript:`+`
    - Added ability to tag Virtual Images (currently API only):superscript:`+`

Fixes
=====



.. NOTE:: :superscript:`+` indicates items also released in v4.2.5

.. new do not remove

  Appliance Updates
  =================

  .. not sure if we should have separate appliance/installer updates, adding here for now

  - Support added for Installing |morpheus| on Ubuntu 20.04
  - Java: Openjdk-jre updated to 8u275
  - Appliance Logs: Default log rotation added for Nginx and Tomcat logs //add paths & files
  - Installer: ``iptables_bach`` setup bash script moved from /tmp to /opt/morpheus/embedded/bin and renamed to iptables_morpheus.rules. Resolves reconfigure issue for systems with ``noexec`` set on ``/tmp``.

  Agent/Node Package Updates
  ==========================

  .. same

  - Java: openjdk and openjdk-jre updated to 8u275
  - Node and VM Node package versions updates to 3.1.11
  .. add agent package version vars/list to compatibility?
