.. _provisioning_settings:

Provisioning Settings
=====================

Overview
--------

Provisioning Settings (:menuselection:`Administration --> Settings --> Provisioning`) configure global defaults and behaviors for the |morpheus| provisioning engine. These settings control the provisioning wizard experience, default configurations, naming behavior, and infrastructure-as-code settings.

.. NOTE:: These settings apply appliance-wide (Master Tenant scope) or per-Tenant (Account scope) depending on the specific setting.

Role Permissions
----------------

- **Administration: Provisioning Settings** with ``Full`` access is required to modify provisioning settings

General Settings
----------------

Allow Cloud Selection
  When enabled, the Cloud selection dropdown is displayed in the provisioning wizard. When disabled, the default Cloud is used automatically.

Allow Host Selection
  When enabled, the Host selection dropdown is shown during provisioning. When disabled, host selection is handled automatically by |morpheus| placement logic.

Require Environment Selection
  When enabled, users must select an Environment (e.g., Development, Staging, Production) during provisioning. Environments are configured in |ProEnv|.

Show Pricing
  Controls visibility of pricing estimates in the provisioning wizard and on Instance/Host detail pages.

Hide Datastore Stats On Selection
  When enabled, datastore utilization statistics and size information are hidden in provisioning and app wizards.

Cross-Tenant Naming Policies
  When enabled, the ``sequence`` value in naming policies applies globally across all Tenants rather than per-Tenant. This prevents naming collisions in shared infrastructure.

Reuse Naming Sequence Numbers
  When enabled, sequence numbers are recycled when Instances are removed. When disabled, |morpheus| tracks all issued sequence numbers and always uses the next available number, preventing name reuse.

Deployment Archive Store
  Sets the default Storage Provider for storing deployment archives. Storage Providers are configured in Infrastructure > Storage.

Cloud-Init Settings
-------------------

|morpheus| can inject global users during provisioning. This requires Cloud-Init (Linux), Cloudbase-Init (Windows), or VMware Tools on the provisioned images.

Linux
^^^^^

- **USERNAME:** Default user added to Linux Instances during provisioning
- **PASSWORD:** Password for the Linux user
- **KEYPAIR:** SSH key pair added for the Linux user (select from Infrastructure > Trust > Key Pairs)

.. NOTE:: Either a password, key pair, or both can be configured. Key pairs are managed in Infrastructure > Trust.

Windows Settings
^^^^^^^^^^^^^^^^

- **ADMINISTRATOR PASSWORD:** Default password set for the Windows Administrator account during provisioning

PXE Boot Settings
^^^^^^^^^^^^^^^^^

- **DEFAULT ROOT PASSWORD:** Password set for root during PXE boot provisioning

App Blueprint Settings
-----------------------

Sets the default Blueprint Type selected when creating new Apps:

- Morpheus
- ARM Template
- CloudFormation
- Terraform
- Kubernetes Spec
- Helm Chart

Terraform Settings
------------------

Terraform Runtime
  Selects the default Terraform runtime version for new deployments. Available versions depend on the |morpheus| appliance version.

Terraform Log Level
  Sets the verbosity of Terraform execution logs:

  - **Default:** Standard output
  - **Debug:** Detailed debug logging
  - **Trace:** Maximum verbosity (warning: produces large output)

Ordering and Display
---------------------

|morpheus| allows configuration of which provisioning features are visible in the navigation:

Enable Instances
  Show/hide the Instances section in Provisioning navigation.

Enable Apps
  Show/hide the Apps section in Provisioning navigation.

Enable Catalog
  Show/hide the Self-Service Catalog section.

These toggles allow administrators to tailor the |morpheus| experience to their organization's provisioning workflow — for example, hiding direct Instance provisioning in favor of catalog-based self-service.

Saving Settings
---------------

After modifying any provisioning settings:

#. Click :guilabel:`SAVE` at the bottom of the settings page
#. A confirmation message indicates successful save

Settings take effect immediately for subsequent provisioning operations. Existing Instances are not affected by settings changes.

API
---

Provisioning settings can be managed via the API:

.. code-block:: bash

  # Get provisioning settings
  curl "$MORPHEUS_API_URL/api/provisioning-settings" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN"

  # Update provisioning settings
  curl -X PUT "$MORPHEUS_API_URL/api/provisioning-settings" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "provisioningSettings": {
        "allowZoneSelection": true,
        "requireEnvironments": false,
        "showPricing": true,
        "reusePlatformSequence": false
      }
    }'
