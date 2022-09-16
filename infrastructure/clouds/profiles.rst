Cloud Profiles
--------------

Role Permissions
^^^^^^^^^^^^^^^^

.. begin_cloud_profiles

Access to **Profiles** tab of Cloud Detail Pages is determined by the following role permissions:

Role: Feature Access: ``Admin: Profiles``
  - None: Cannot access Profiles tab or create/view/edit/delete profiles
  - Read: Can access Profiles tab, can view profiles, cannot create/edit/delete profiles
  - Full: Can access Profiles tab, can create/view/edit/delete profiles

Terraform Profiles
^^^^^^^^^^^^^^^^^^

- Terraform Profiles allow creation of Cloud-associated tfvars secrets, allowing tf apps and specs to be provisioned across multiple clouds that required different tfvars.
- Target Cloud Terraform Profiles are automatically mapped to tf apps/specs during provisioning, no manual scoping is required.
- Terraform Profiles are encrypted in Cypher and creating a profile creates a Cypher entry with key `tfvars/profile/cloud/$cloudCode/variables``
- Terraform Profiles can be edited after creation
- Terraform Profiles are limited to one per Cloud, once one is created for the Cloud the option to create a Terraform Profile is no longer present. Edit the existing Terraform Profile to make changes at that point

Create a Terraform Profile
``````````````````````````

#. Navigate to |InfClo| and select a Cloud
#. Select the "Profiles" tab
#. Select :guilabel:`+ ADD PROFILE`
#. Select Terraform Profile Type
#. Enter tfvars in the `Terraform Profile Variables` field

   - example Terraform Profile Variables

     .. code-block:: bash

        access_key="****acccessKey****"
        secret_key="********secretKey**********"
        region="us-west-1"


#. Select :guilabel:`SAVE CHANGES`

Now, when provisioning a Terraform Instance or App to the Cloud the profile was created in, the tfvars in the profile become available to Terraform. It is not necessary to manually tie this tfvars files to your App Blueprint, these tfvars will automatically be available to Terraform whenever you provision an App to this cloud.

.. end_cloud_profiles

Key/Value Store Profiles
^^^^^^^^^^^^^^^^^^^^^^^^

- Key/Value Profiles (Key/Value Store) expand provisioning, automation, billing and reporting capabilities by allowing dynamic custom object specific metadata in provisioning and automation mappings
- Key/Value Profile entries are available using ``<%=cloud.profile.key%>``
- Terraform Profiles are limited to one Profile per Cloud, however multiple key/value pairs can be added to a single profile

Create a Key/Value Profile
``````````````````````````
#. Navigate to ``/infrastructure/clouds/`` and select a Cloud
#. Select the ``Profiles`` tab
#. Select :guilabel:`+ ADD PROFILE`
#. Select Key/Value Profile Type
#. Enter key/value entries, selecting + to add additional entries
#. Select :guilabel:`SAVE CHANGES`
