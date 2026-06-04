.. _catalog_item_types:

Catalog Item Types
==================

Overview
--------

Catalog Item Types define the items available in the |morpheus| Self-Service Catalog. Each catalog item type specifies what gets provisioned or executed when a user orders from the catalog, including the configuration, form fields, branding, and access controls.

Catalog Item Types are managed in |TooCat| (Tools > Self-Service > Catalog Items) or through the Library Blueprints section, depending on the navigation configuration.

The Self-Service Catalog provides a simplified ordering experience for end users who don't need access to the full provisioning wizard.

Role Permissions
----------------

- **Tools: Catalog** — ``None``, ``Read``, or ``Full``

  - **None:** Cannot access Catalog Item Types management
  - **Read:** Can view catalog items
  - **Full:** Can create, edit, and delete catalog items

Catalog Item Reference Types
-----------------------------

Each Catalog Item Type has a reference type that determines what it provisions:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Reference Type
     - Description
   * - **Instance**
     - Provisions an Instance from a configured Instance Type with predefined settings
   * - **Blueprint**
     - Deploys a multi-tier application from an App Blueprint (Morpheus, Terraform, ARM, CloudFormation, Kubernetes, Helm)
   * - **Workflow**
     - Executes an Operational Workflow (no provisioning, just automation)

Creating a Catalog Item Type
-----------------------------

#. Navigate to |TooCat|
#. Click :guilabel:`+ ADD`
#. Select the item type (Instance, Blueprint, or Workflow)
#. Complete the configuration:

   **General Settings:**

   - **NAME:** Display name shown in the catalog (must be unique per tenant)
   - **CODE:** Unique code identifier for API reference
   - **DESCRIPTION:** Description shown to catalog users
   - **CATEGORY:** Optional category for organizing items in the catalog
   - **ENABLED:** Toggle availability in the catalog
   - **FEATURED:** Mark to highlight in the catalog (displayed prominently)
   - **VISIBILITY:** ``Public`` (all tenants) or ``Private`` (owner tenant only)
   - **LABELS:** Organizational labels

   **Branding:**

   - **LOGO:** Upload a custom icon/logo (PNG, JPEG, SVG)
   - **DARK LOGO:** Logo variant for dark mode display

   **Configuration (varies by type):**

   *Instance Type:*

   - Full Instance provisioning configuration in JSON format including Instance Type, layout, plan, network, volumes, and options

   *Blueprint:*

   - App Blueprint selection and configuration
   - App Spec in JSON/YAML format

   *Workflow:*

   - Select the Operational Workflow to execute
   - Configure default input values

   **Form Configuration:**

   - **FORM TYPE:** Option Types (individual fields) or Option Type Form (reusable form)
   - **OPTION TYPES:** Select or create form fields presented to the user at order time
   - **FORM:** Select a pre-built Option Type Form

   **Content:**

   - **CONTENT:** Rich text content (markdown/HTML) displayed on the catalog item detail page. Use for documentation, instructions, or SLA information.

   **Access Control:**

   - Role-based visibility controls which roles can see and order the item

#. Click :guilabel:`SAVE`

Instance Type Configuration
----------------------------

For Instance-type catalog items, the configuration JSON defines the complete provisioning specification:

.. code-block:: JSON

  {
    "instance": {
      "type": "nginx",
      "cloud": {"id": 1},
      "layout": {"id": 105},
      "plan": {"id": 10}
    },
    "config": {
      "resourcePool": {"id": 5},
      "network": {"id": 3}
    },
    "volumes": [
      {"rootVolume": true, "size": 50}
    ]
  }

Users ordering this item see only the form fields you've configured — the underlying provisioning details are hidden.

Blueprint Configuration
------------------------

For Blueprint-type catalog items, reference an existing App Blueprint:

- Select the Blueprint from the configuration
- Optionally lock specific configuration values
- Users can fill in only the fields exposed through the form

Workflow Configuration
-----------------------

For Workflow-type catalog items:

- Select an Operational Workflow
- Configure which inputs are presented to the user
- The workflow executes when the item is ordered

Form Fields (Option Types)
----------------------------

Option Types define the form fields shown to catalog users at order time:

- **Text:** Free-text input
- **Number:** Numeric input
- **Select List:** Dropdown from a static or dynamic list
- **Checkbox:** Boolean toggle
- **Password:** Masked input
- **Text Area:** Multi-line text
- **Hidden:** Value passed without user input
- **Typeahead:** Search-as-you-type selection

Form fields can be sourced from Option Type Lists for dynamic data (e.g., available environments, networks, resource pools).

Quantity Support
----------------

- **ALLOW QUANTITY:** When enabled, users can order multiple copies in a single request
- **MAX QUANTITY:** Maximum number of copies per order (leave empty for unlimited)
- **DISABLE AUTO PRICE:** When enabled, pricing is not automatically calculated for quantity changes

Managing Catalog Item Types
----------------------------

Editing
^^^^^^^

#. Navigate to |TooCat|
#. Click the item name or the pencil icon
#. Modify settings as needed
#. Click :guilabel:`SAVE`

Deleting
^^^^^^^^

#. Navigate to |TooCat|
#. Click the trash icon on the item row
#. Confirm deletion

.. NOTE:: Deleting a Catalog Item Type does not affect previously-provisioned resources from that item. It only removes the item from the catalog for future orders.

Multi-Tenant Considerations
-----------------------------

- **Public** items created in the Master Tenant are visible to all tenants
- **Private** items are only visible to the creating tenant
- Sub-tenant users can only create Private catalog items
- Role-based access further restricts which users within a tenant can see specific items

Layout Providers (Plugin)
--------------------------

Plugin-based layout providers can extend the catalog item presentation with custom rendering. Installed plugins that implement ``AbstractCatalogItemLayoutProvider`` appear as layout options during catalog item creation.

API
---

Catalog Item Types can be managed via the |morpheus| API:

.. code-block:: bash

  # List catalog item types
  curl "$MORPHEUS_API_URL/api/catalog-item-types" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN"

  # Create a catalog item type
  curl -X POST "$MORPHEUS_API_URL/api/catalog-item-types" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "catalogItemType": {
        "name": "Web Server",
        "description": "Standard Nginx web server",
        "type": "instance",
        "visibility": "public",
        "enabled": true,
        "config": "{\"instance\":{\"type\":\"nginx\"}}"
      }
    }'
