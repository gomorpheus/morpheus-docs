Open Telekom Cloud
------------------


Add an Open Telekom Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````

IDENTITY API URL

DOMAIN ID
  This pertains to the Openstack V3 API and should be ignored when using V2. This is the Domain ID (Not to be confused with Domain Name). The Domain ID can be found via the CLI by typing openstack domain list.

PROJECT

USERNAME

PASSWORD

OS VERSION

IMAGE FORMAT

Image Store
  Set an OBS bucket as a permanent store location for |morpheus| virtual images. Users are limited to uploading images of 2GB or less in size if an OBS bucket is not specified here

LB TYPE
  Inventory Existing Instances
  Enable Hypervisor Console

.. NOTE:: Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment.

Advanced Options

Provisioning Command
