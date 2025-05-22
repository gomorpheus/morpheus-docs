Provisioning Settings
^^^^^^^^^^^^^^^^^^^^^

Allow Cloud Selection
  Displays or hides Cloud Selection dropdown in Provisioning wizard.
Allow Host Selection
  Displays or hides Host Selection dropdown in Provisioning wizard.
Require Environment Selection
  Forces users to select and Environment during provisioning
Show Pricing
  Displays or hides Pricing in Provisioning wizard and Instance and Host detail pages.
Hide Datastore Stats On Selection
  Hides Datastore utilization and size stats in provisioning and app wizards
Cross-Tenant Naming Policies
  Enable for the ``sequence`` value in naming policies to apply across tenants
Reuse Naming Sequence Numbers
  When selected, sequence numbers can be reused when Instances are removed. Deselect this option and |morpheus| will track issued sequence numbers and use the next available number each time.
Deployment Archive Store
  Default Storage Provider for storing Deployment Archives.

  .. NOTE:: Storage Providers can be configured and managed in the `Infrastructure > Storage` section.

Cloud-Init Settings
^^^^^^^^^^^^^^^^^^^

|morpheus| can add global users for Linux and Windows at provision time. Cloud-init/Cloudbase-Init or VMware Tools installed on the provisioned virtual images is required.

Linux
  * **Username:** Enter User to be added to Linux Instances during provisioning.
  * **Password:** Enter password to be set for the above Linux user.
  * **KeyPair:** Select KeyPair to be added for the above Linux user.

.. NOTE:: Either a password, keypair, or both can be populated for the Linux user. Keypairs can be added in the `Infrastructure > Keys & Certs` section.

Windows Settings
^^^^^^^^^^^^^^^^

  * **Administrator Password:** Enter password to be set for the Windows Administrator User during provisioning.

PXE Boot Settings
^^^^^^^^^^^^^^^^^

Default Root Password
  Enter the default password to be set for Root during PXE Boots.

App Blueprint Settings
^^^^^^^^^^^^^^^^^^^^^^

Determines the Default Blueprint Type selected in new App Wizard

 - Morpheus
 - ARM Template
 - CloudFormation
 - Terraform
 - Kubernetes Spec
 - Helm Chart

Terraform Settings
^^^^^^^^^^^^^^^^^^

  * **Terraform Runtime:** Select "auto" or "manual". When selecting "auto", |morpheus| will automatically download and use the Terraform version indicated in the VERSION field on the Spec Templates that make up a Terraform Instance type or Blueprint (only up to v1.5.5). When selecting "manual", |morpheus| will use the version of Terraform `installed on your appliance <https://docs.morpheusdata.com/en/latest/integration_guides/Automation/terraform.html?#terraform-installation>`_.
