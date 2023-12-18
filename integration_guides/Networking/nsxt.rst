NSX-T
-----

Overview
^^^^^^^^

VMware NSX-T offers network virtualization allowing for creation and management of software-based virtual networks in an efficient and programmatic way. |morpheus| offers a full-featured integration with NSX-T, including Project scoping for NSX-T 4+ integrations. |morpheus| will ingest and expose its networking abstractions in the following sections of the |morpheus| NSX-T integration:

- SUMMARY
- TRANSPORT ZONES
- DHCP
- SEGMENTS
- FIREWALL
- TIER-1 GATEWAYS
- TIER-0 GATEWAYS
- EDGE CLUSTERS
- GROUPS

This guide goes through the process of integrating an existing NSX-T installation with |morpheus| and working with the associated objects synced in with the integration. For more on installing NSX-T and an overview of its concepts, please review the `NSX-T overview documentation <https://docs.vmware.com/en/VMware-NSX-T-Data-Center/2.0/com.vmware.nsxt.install.doc/GUID-10B1A61D-4DF2-481E-A93E-C694726393F9.html>`_ provided by VMware.

NSX-T Projects
^^^^^^^^^^^^^^

Projects in NSX-T are analogous to tenants in other products and are a part of NSX-T version 4+. Projects allow for the isolation of networking abstractions into individual tenants within a single NSX-T appliance. If your organization is already utilizing NSX-T Projects, you are probably very familiar with their concept and execution but others can find high-level details about them `here <https://docs.vmware.com/en/VMware-NSX/4.1/administration/GUID-52180BC5-A1AB-4BC2-B1CE-666292505317.html>`_.

|morpheus| supports a full-featured integration with NSX-T, including the ability to scope the |morpheus| integration to a specific Project the service user can access. Using Project-scoped integrations allows multiple NSX-T integrations to be made to the same NSX-T appliance and ensures |morpheus| users are siloed to only the NSX-T Projects they can access.

Add NSX-T Integration to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select Select :guilabel:`+ ADD` > VMWare NSX
#. Enter the following:

   - **NAME:** Name for the NSX Integration in |morpheus|
   - **VISIBILITY:** Public (available to all |morpheus| Tenants) or Private (available only to the current Tenant). This option is shown only in the |morpheus| |mastertenant|
   - **API HOST:** URL of the NSX Manager (ex. https://x.x.x.x/api)
   - **CREDENTIALS:** A pre-stored credential set can be used to create this integration. If "Local Credentials" is selected, USERNAME and PASSWORD fields are presented and must be filled
   - **USERNAME:** NSX service account username. Prior to NSX version 4, this is likely an admin account with access to all networking constructs. In NSX version 4 and higher, this could be an admin for access to default space constructs or it could be a Project-specific user depending on the access needs of the integration being created
   - **PASSWORD:** The password for the NSX service account entered above
   - **PROJECT:** As soon as an API HOST and credentials are provided, |morpheus| will attempt to authenticate with the NSX-T appliance. When authentication is successful and a NSX-T 4+ appliance is detected, a PROJECT field will appear and the dropdown will be pre-populated with Projects accessible to the service user account
   - **VMWARE CLOUD:** Select the existing VMware cloud associated with this NSX integration

#. Select :guilabel:`ADD NETWORK INTEGRATION`

Once the NSX Integration is added |morpheus| will sync in existing Transport Zones, DHCP servers and relays, Segments, firewall groups and rules, Gateways, Edge Clusters, and Groups. We can manage these synced items from within |morpheus| UI, including the ability to create, edit, and delete them.

.. NOTE:: The available tabs on the integration detail page will be dependent on the Project selected when the integration was created. Just like in NSX-T, the default view (and thus integrations scoped to the default Project) will have access to all constructs whereas individual Projects will not. Integrations scoped to individual Projects can view the DHCP, Segments, Firewall, Tier-1 Gateways, and Groups tabs but not the other tabs described here. These limitations are identical to those in the NSX-T console UI. More information on NSX-T Projects is available `here <https://docs.vmware.com/en/VMware-NSX/4.1/administration/GUID-52180BC5-A1AB-4BC2-B1CE-666292505317.html>`_.

Summary View
^^^^^^^^^^^^

The SUMMARY tab contains the default view when accessing an NSX-T integration. From the summary view we can see the status of the NSX-T server, and details about interfaces and group status.

Transport Zones
^^^^^^^^^^^^^^^

Access Transport Zones by selecting the Transport Zones tab. The default view of the Transport Zones tab lists Transport zones and presents some detail about them such as name, traffic type, status, and more. The integration allows for creation of new Transport Zones, editing and deleting.

.. images:: /images/integration_guides/networking/nsx/nsxt/tz.png

DHCP
^^^^

DHCP servers and relays are displayed on the DHCP tab. View information such as names and server addresses. The integration allows for creation of new servers and relays, editing and deleting.

.. images:: /images/integration_guides/networking/nsx/nsxt/dhcp.png

Segments
^^^^^^^^

Access Segments by from the Segments tab. The summary view includes high-level information such as status, name, network name and CIDR. The integration allows for creating, editing and deleting NSX-T Segments

.. images:: /images/integration_guides/networking/nsx/nsxt/segments.png

Firewall
^^^^^^^^

Firewall Groups and Rules are accessible from the Firewall tab. From the summary view, Groups can be expanded to view Rules within. From the ACTIONS menu, create new Groups by selecting "Create Group". When a Group has been expanded, the "Create Rule" selection within the ACTIONS menu will also be accessible and a new rule can be created within the selcted Group. The integration allows for viewing, creating, editing and deleting Firewall Groups and Rules.

.. images:: /images/integration_guides/networking/nsx/nsxt/firewall.png

Tier-0 Gateways
^^^^^^^^^^^^^^^

Access Tier-0 Gateways from the Tier-0 Gateways tab. The integration allows creating, editing and deleting Tier-0 Gateways.

.. images:: /images/integration_guides/networking/nsx/nsxt/t0.png

Tier-1 Gateways
^^^^^^^^^^^^^^^

Access Tier-1 Gateways from the Tier-1 Gateways tab. The integration allows creating, editing and deleting Tier-1 Gateways.

.. images:: /images/integration_guides/networking/nsx/nsxt/t1.png

Edge Clusters
^^^^^^^^^^^^^

View Edge Clusters from the Edge Clusters tab. The default view lists each Edge Cluster with name, member type, cluster profile, and more. The integration allows viewing and limited editing of Edge Clusters.

.. images:: /images/integration_guides/networking/nsx/nsxt/edgeclusters.png

Groups
^^^^^^

NSX-T Groups are viewed from the Groups tab. The default view lists each Group alone with member details. The |morpheus| NSX-T integration allows for creating, editing and deleting Groups.

.. images:: /images/integration_guides/networking/nsx/nsxt/groups.png
