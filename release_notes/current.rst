.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

|morphver| Highlights
=====================


All New Features
----------------

- Amazon AWS Cloud Integration: Hong Kong region (ap-east-1) support added

- .. toggle-header:: :header: **NSX-T Integration Improvements**

    - Scope NSX-T routers to Groups and assign visibility permissions for Tenants
    - Set Tenant visibility permissions for Transport Zones
    - Added Edge Cluster inventorying from NSX-T integrations
    - Set Tenant visibility permissions for Edge Clusters
    - Tenants can view NAT rules for T-0 and T-1 routers they have been given access
    - Create and manage NAT rules for T-0 and T-1 routers
    - T-1 Interfaces tab renamed to Services Interfaces for clarity
    - Added role-based access permissions for all tabs on T-0 and T-1 routers

- Networks: Set Tenant visibility permissions for IP pools

- .. toggle-header:: :header: **Role Permission Changes**

    - Added access permissions for NSX-T T-0 and T-1 router tabs

- Security Scanning: Windows support added for SCAP security scans

Fixes
-----

- Instances: Passing ``masked=true`` flag for tags masks the value of the tag
- Metadata: Metadata tags now referred to as ``tags`` and labels now referred to as ``labels``, previously metadata tags were referred to as ``metadata`` and labels were referred to as ``tags``
- Virtual Images: Associated ``volumes`` are returned with ``maxStorage`` viewable for each

API & CLI Enhancements
----------------------
