.. _provisioning_licenses:

Software Licenses
=================

Overview
--------

The Software Licenses section (|AdmSetLic|) enables automated application of license keys to Instances during provisioning. This is primarily used for Windows license management but supports any software requiring key-based activation.

When a license is associated with a Virtual Image, |morpheus| automatically applies the license key to any Instance provisioned using that image, streamlining license management across your infrastructure.

Role Permissions
----------------

- **Administration: Settings** with ``Full`` access is required to manage software licenses

Creating Licenses
-----------------

To create a new software license:

#. Navigate to |AdmSetLic| (Administration > Settings > Software Licenses)
#. Click :guilabel:`+ CREATE LICENSE`
#. Complete the form:

   - **LICENSE TYPE:** Select the license type:

     - Windows

   - **NAME:** A descriptive name for the license in |morpheus|
   - **LICENSE KEY:** The software license key
   - **ORG NAME:** Organization name associated with the license (if applicable)
   - **FULL NAME:** Full name associated with the license (if applicable)
   - **VERSION:** The software version this license applies to
   - **COPIES:** Number of copies/seats available on the license
   - **DESCRIPTION:** Description displayed in the license list for identification
   - **VIRTUAL IMAGES:** Search for and select Virtual Images to associate with this license. When Instances are provisioned from these images, the license is automatically applied.
   - **TENANT PERMISSIONS:** Select one or more Tenants that can use this license. Leave empty for Master Tenant only.

#. Click :guilabel:`SAVE CHANGES`

Provisioning with Licenses
---------------------------

When a Virtual Image is associated with a license, |morpheus| automatically handles license application during provisioning:

- **Instance Type Provisioning:** If an Instance Type's Node Type uses a licensed Virtual Image, the license is applied
- **Generic Cloud Instances:** If a licensed Virtual Image is selected during provisioning (VMware, AWS, Nutanix, OpenStack, etc.), the license is applied
- **Multi-Tenant:** Only Tenants specified in the license's Tenant Permissions can use the license

The license key is injected during the provisioning process, typically through:

- Windows unattend.xml for Windows KMS/MAK keys
- Cloud-init user data for Linux license activation
- Custom automation Tasks triggered during provisioning

License Tracking
----------------

The license list displays:

- **Name:** License name
- **License Type:** Type of license
- **Version:** Software version
- **Copies:** Total available copies
- **Applied:** Number of copies currently in use
- **Virtual Images:** Count of associated images
- **Tenants:** Tenants with access

|morpheus| tracks the number of applied copies against the total available. When all copies are consumed, additional provisioning with that license may be restricted depending on the license type configuration.

Managing Licenses
-----------------

Editing a License
^^^^^^^^^^^^^^^^^

#. Navigate to |AdmSetLic|
#. Click :guilabel:`ACTIONS` on the license row
#. Select :guilabel:`Edit`
#. Modify the editable fields:

   - Name, Version, Copies, Description
   - Virtual Images (add/remove associations)
   - Tenant Permissions

#. Click :guilabel:`SAVE CHANGES`

.. NOTE:: License Type, License Key, Org Name, and Full Name cannot be modified after creation. To change these values, delete and recreate the license.

Deleting a License
^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmSetLic|
#. Click :guilabel:`ACTIONS` on the license row
#. Select :guilabel:`Delete`
#. Confirm deletion

.. NOTE:: Deleting a license does not deactivate software on existing Instances. It only prevents future automatic application during provisioning.

Virtual Image Association
--------------------------

Virtual Images are the link between licenses and provisioning:

- A single Virtual Image can be associated with one license
- A single license can be associated with multiple Virtual Images
- Virtual Images are managed in :menuselection:`Library --> Virtual Images` (Library > Virtual Images)
- Images synced from Clouds are available for license association

To add a Virtual Image to a license:

#. Edit the license
#. In the **VIRTUAL IMAGES** field, search by name
#. Select the image from the results
#. Save the license

API
---

Licenses can be managed via the |morpheus| API:

.. code-block:: bash

  # List licenses
  curl "$MORPHEUS_API_URL/api/provisioning-licenses" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN"

  # Create a license
  curl -X POST "$MORPHEUS_API_URL/api/provisioning-licenses" \
    -H "Authorization: Bearer $MORPHEUS_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "license": {
        "licenseType": "win",
        "name": "Windows Server 2022 Datacenter",
        "licenseKey": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX",
        "licenseVersion": "2022",
        "copies": 50,
        "description": "Datacenter license for production"
      }
    }'
