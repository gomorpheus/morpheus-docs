Routers
-------

Overview
^^^^^^^^

Routers can be viewed, created, and managed from the Routers tab of the Infrastructure > Networks page. |morpheus| supports the creation of the following router types depending on networks that are currently configured:

- Amazon Internet Gateway
- Huawei Router
- Neutron Router
- NSX Edge Gateway
- NSX Edge Logical Router
- NSX Cloud Tier0 Gateway
- NSX Cloud Tier1 Gateway
- NSX Tier0 Gateway
- NSX Tier1 Gateway
- Open Telekom Router
- VM Network (OVS)

Create New Router
^^^^^^^^^^^^^^^^^

#. Navigate to Infrastructure > Networks > Routers tab
#. Click :guilabel:`+ ADD`
#. Select the router type and complete the fields on the resulting modal
#. Once complete, click :guilabel:`ADD NETWORK ROUTER`

Common Fields
`````````````

The first field is **Router Type**. The remaining fields are supplied by that router provider, so a field shown for one type must not be assumed to apply to another. Common provider fields include a router **Name**, enabled state, Cloud or network integration, and integration-specific location or gateway selections.

VM Network (OVS)
````````````````

**VM Network (OVS)** is the UI label for the ``openVSwitch`` type. Despite appearing in the Routers list, it defines an Open vSwitch bridging domain for an HVM cluster; it does not provide gateway, NAT, firewall, DHCP, BGP, or static-routing functions.

.. list-table:: VM Network (OVS) creation fields
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - Name
     - Required display name for the OVS network definition.
   * - Cluster
     - Required HVM cluster on which the OVS bridge or overlay is configured. Only eligible clusters are offered.
   * - Enable Overlay
     - Selects an overlay network across cluster hosts. When clear, configure a bridge and port instead.
   * - OVS Bridge Name
     - Existing bridge on the selected cluster for a non-overlay network. Select the create option to expose **New OVS Bridge Name**.
   * - New OVS Bridge Name
     - Required name when creating a bridge rather than selecting an existing one.
   * - Port Name
     - Required host network interface attached to a newly created non-overlay bridge.
   * - Overlay Net Interface
     - Required cluster interface carrying overlay traffic when **Enable Overlay** is selected.
   * - Overlay Net Port
     - Required UDP overlay port. The current form defaults to ``4789``.
   * - Overlay ID
     - Required overlay network identifier.
   * - CIDR
     - Required overlay address range in CIDR notation.

The OVS type and these fields are HVM-cluster scoped. Other router types expose provider-specific fields and capabilities; compare the form in the running release with the corresponding integration guide before creating or changing them.

Provider-specific Router Fields
```````````````````````````````

The bundled documentation metadata does not establish a release-independent field inventory for the NSX, OpenStack, Open Telekom, and other integration-supplied Router forms. Their visible fields depend on the selected integration, provider inventory, permissions, and product release. The running Create Router form is authoritative for field availability; a field or Router type absent from that form is not documented as supported for that provider. Do not reuse the VM Network (OVS) meanings for another Router type.

Editing Existing Routers
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to Infrastructure > Networks > Routers tab
#. Click on the pencil icon for the appropriate router
#. After editing router fields, click :guilabel:`SAVE`

Deleting Existing Routers
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to Infrastructure > Networks > Routers tab
#. Click on the trash can icon for the appropriate router
#. Acknowledge the pop-up banner ensuring you wish to delete the router
