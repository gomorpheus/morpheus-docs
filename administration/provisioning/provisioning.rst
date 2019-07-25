Provisioning Settings
=====================

`Administration -> Provisioning`

Settings
  Configure Global Provisioning, Cloud-init and PXE Boot settings.
Environments
  Create and manage Environment Tags
Licenses
  Add License to apply to Windows Instances during Provisioning.

Settings
--------

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
Deployment Archive Store
  Default Storage Provider for storing Deployment Archives.

  .. NOTE:: Storage Providers can be configured and managed in the `Infrastructure -> Storage` section.

Cloud-Init Settings
-------------------

|morpheus| can add Global users for Linux and Windows at provision time. Cloud-init/Cloudbase-Init or VMware Tools installed on the provisioned Virtual Images is required.

Linux
  * *Username*: Enter User to be added to Linux Instances during provisioning.
  * *Password*: Enter password to be set for the above Linux user.
  * *KeyPair*: Select KeyPair to be added for the above Linux user.

.. NOTE:: Either a Password, KeyPair, or both can be populated for the Linux User. KeyPairs can be added in the `Infrastructure -> Key Pairs` section.

Windows
  * *Administrator Password*: Enter password to be set for the Windows Administrator User during provisioning.

PXE Boot Settings
-----------------

Default Root Password
  Enter the default password to be set for Root during PXE Boots.

.. include:: environments.rst
.. include:: licenses.rst

App Blueprint Settings
----------------------

Determines the Default Blueprint Type selected in new App Wizard

 - Morpheus
 - ARM Template
 - Cloud Formation
 - Terraform
 - Kubernetes Spec
 - Helm Chart
