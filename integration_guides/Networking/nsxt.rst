NSX-T
-----

Overview
^^^^^^^^

VMware NSX-T offers network virtualization allowing for creation and management of software-based virtual networks in an efficient and programmatic way. |morpheus| offers a full-featured integration with NSX-T, exposing its networking abstractions in the following sections of the |morpheus| NSX-T integration:

- SUMMARY
- TRANSPORT ZONES
- SEGMENTS
- FIREWALL
- TIER-1 GATEWAYS
- TIER-0 GATEWAYS

This guide goes through the process of integrating an existing NSX-T installation with |morpheus| and working with the associated objects synced in with the integration. For more on installing NSX-T and an overview of its concepts, please review the `NSX-T overview documentation <https://docs.vmware.com/en/VMware-NSX-T-Data-Center/2.0/com.vmware.nsxt.install.doc/GUID-10B1A61D-4DF2-481E-A93E-C694726393F9.html>`_ provided by VMware.

Add NSX-T Integration to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select Select :guilabel:`+ ADD` > VMWare NSX-T
#. Enter the following:

   - **NAME:** Name for the NSX Integration in |morpheus|
   - **API HOST:** URL of the NSX Manager (ex. https://x.x.x.x/api)
   - **USERNAME:** NSX Manager Admin Username
   - **PASSWORD:** NSX Manager Admin password
   - **VMWARE CLOUD:** Select the existing VMware cloud associated with this NSX integration

#. Select :guilabel:`ADD NETWORK INTEGRATION`

Once the NSX Integration is added |morpheus| will sync in existing Transport Zones, Segments, firewall groups and rules, and Gateways. We can also manage these synced items from within |morpheus| UI, including the ability to create, edit, and delete them.

Summary View
^^^^^^^^^^^^

The SUMMARY tab contains the default view when accessing an NSX-T integration. From the summary view we can see the health status of the NSX-T server, and details about interfaces and group status.

Transport Zones
^^^^^^^^^^^^^^^

Access Transport Zones by navigating to Infrastructure > Networks > Integrations > (Your NSX-T Integration) > Transport Zones tab. We can delete Transport Zones by clicking on the trash can icon to the far right of each list item. The default view lists each Transport Zone and provides the following information about them:

- **NAME:** The given name for the Transport Zone
- **DESCRIPTION:** A given description value (if available)
- **TRAFFIC TYPE:** "Overlay" or "VLAN"
- **N-VDS NAME:** The name of the NSX-managed virtual distributed switch
- **STATUS:** An icon indicating the current status of the Transport Zone
- **HOST MEMBERSHIP CRITERIA:** "Standard" or "Enhanced Datapath"

Creating NSX-T Transport Zones
``````````````````````````````

#. Navigate to `Infrastructure > Network`
#. Select the  `Integrations` tab
#. Select the name of NSX-T integration
#. Select the `Transport Zones` tab
#. Select :guilabel:`+ CREATE NSX-T TRANSPORT ZONE`
#. After completing the required fields and any desired optional fields, click :guilabel:`+ CREATE`

Segments
^^^^^^^^

Access Segments by navigating to Infrastructure > Networks > Integrations > (Your NSX-T Integration) > Segments tab. We can delete Segments by clicking on the trash can icon to the far right of each list item or edit them by clicking on the pencil icon. The default view lists each Segment and provides the following information about them:

- **STATUS:** An icon indicating the current status of the Transport Zone
- **NAME:** The given name for the Segment
- **TRAFFIC TYPE:** "Overlay" or "VLAN"
- **N-VDS NAME:** The name of the NSX-managed virtual distributed switch
- **STATUS:** An icon indicating the current status of the Transport Zone
- **HOST MEMBERSHIP CRITERIA:** "Standard" or "Enhanced Datapath"

Creating NSX-T Segments
```````````````````````

#. Navigate to `Infrastructure > Network`
#. Select the  `Integrations` tab
#. Select the name of NSX-T integration
#. Select the `Segments` tab
#. Select :guilabel:`+ CREATE NSX-T SEGMENT`
#. Complete the fields in the CREATE NETWORK modal
#. Click :guilabel:`SAVE CHANGES`

.. NOTE:: NSX-T Segments can be scoped to specific Groups and Tenants when creating or editing the Segment.

Firewall
^^^^^^^^

Access firewalls by navigating to Infrastructure > Networks > Integrations > (Your NSX-T Integration) > Firewall tab. We can delete firewall groups by clicking on the trash can item at the end of each row. Additionally each group can be expanded (when applicable) to reveal the firewall rules within the group. Individual rules can be edited or deleted by clicking on pencil or trash can icon at the end of the row. The default view lists each Segment and provides the following information about them:

- **NAME:** The name of the rule or group within |morpheus|
- **CATEGORY:** "Ethernet", "Emergency", "Infrastructure", "Environment", or "Application"
- **ENABLED:** Applies only to rules, the rule is enabled when the check mark is present
- **POLICY:** Applies only to rules, "Allow", "Drop", or "Reject"
- **DIRECTION:** Applies only to rules, "In", "Out", or "In-Out"
- **SOURCE:** Applies only to rules, "Any", by default
- **DESTINATION:** Applies only to rules, "Any", by default
- **APPLICATION:** Applies only to rules, "Any", by default

Creating NSX-T Firewall Groups
``````````````````````````````

#. Navigate to `Infrastructure > Network`
#. Select the  `Integrations` tab
#. Select the name of NSX-T integration
#. Select the `Firewall` tab
#. Select :guilabel:`ACTIONS`
#. Select :guilabel:`Create Group`
#. Complete the fields in the CREATE GROUP modal:

   - **NAME:** The name of the rule or group within |morpheus|
   - **DESCRIPTION:** An optional description value for the group
   - **CATEGORY:** "Ethernet", "Emergency", "Infrastructure", "Environment", or "Application"

#. Click :guilabel:`SAVE CHANGES`

Creating NSX-T Firewall Rules
`````````````````````````````

#. Navigate to `Infrastructure > Network`
#. Select the  `Integrations` tab
#. Select the name of NSX-T integration
#. Select the `Firewall` tab
#. Select :guilabel:`ACTIONS`
#. Select :guilabel:`Create Rule`
#. Complete the fields in the CREATE RULE modal:

   - **NAME:** The name of the rule or group within |morpheus|
   - **DESCRIPTION:** An optional description value for the rules
   - **ENABLED:** Rule is enforced when checked
   - **DIRECTION:** "In", "Out", or "In-Out"
   - **SOURCES:** "Any", by default
   - **DESTINATIONS:** "Any", by default
   - **SERVICES:** "Any", by default
   - **PROFILES:** "Any", by default
   - **SCOPES:** "Any", by default
   - **POLICY:** "Allow", "Drop", or "Reject"

#. Click :guilabel:`+ CREATE`

Tier-1 Gateways
^^^^^^^^^^^^^^^

Access Tier-1 Gateways by navigating to Infrastructure > Networks > Integrations > (Your NSX-T Integration) > Tier-1 Gateways tab. We can edit a Gateway by clicking the pencil icon in each row or delete the Gateway by clicking on the trash can icon. The default page for Tier-1 Gateways displays the following information on each:

- **STATUS:** An icon indicating the status of each gateway
- **NAME:** The given name of the gateway
- **DESCRIPTION:** An optional description value for the gateway

Creating Tier-1 Gateways
````````````````````````

#. Navigate to `Infrastructure > Network`
#. Select the  `Integrations` tab
#. Select the name of NSX-T integration
#. Select the `Tier-1 Gateways` tab
#. Select :guilabel:`+ CREATE NSX-T TIER-1 GATEWAY`
#. Complete the fields in the ADD NETWORK ROUTER modal:

   - **GROUP:** If desired, scope the Tier-1 Gateway to a |morpheus| Group
   - **NAME:** The name of the Tier-1 Gateway within |morpheus|
   - **ENABLED:** Tier-1 Gateway is available for use when checked
   - **TIER-0 Gateway:** Select an existing and enabled Tier-0 Gateway
   - **EDGE CLUSTER:** Select an existing Edge Cluster

#. Make selections as needed in the "Route Advertisement" section
#. Click :guilabel:`ADD NETWORK ROUTER`

Tier-0 Gateways
^^^^^^^^^^^^^^^

Access Tier-0 Gateways by navigating to Infrastructure > Networks > Integrations > (Your NSX-T Integration) > Tier-0 Gateways tab. We can edit a Gateway by clicking the pencil icon in each row or delete the Gateway by clicking on the trash can icon. The default page for Tier-0 Gateways displays the following information on each:

- **STATUS:** An icon indicating the status of each gateway
- **NAME:** The given name of the gateway
- **DESCRIPTION:** An optional description value for the gateway

Creating Tier-0 Gateways
````````````````````````

#. Navigate to `Infrastructure > Network`
#. Select the  `Integrations` tab
#. Select the name of NSX-T integration
#. Select the `Tier-0 Gateways` tab
#. Select :guilabel:`+ CREATE NSX-T TIER-0 GATEWAY`
#. Complete the fields in the ADD NETWORK ROUTER modal:

   - **GROUP:** If desired, scope the Tier-0 Gateway to a |morpheus| Group
   - **NAME:** The name of the Tier-0 Gateway within |morpheus|
   - **ENABLED:** Tier-1 Gateway is available for use when checked
   - **HA MODE:** "Active Active" or "Active Standby"
   - **EDGE CLUSTER:** Select an existing Edge Cluster

#. Make selections as needed in the routing and BGP sections
#. Click :guilabel:`ADD NETWORK ROUTER`
