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

LB TYPE
  Inventory Existing Instances
  Enable Hypervisor Console

.. NOTE:: Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment.

Advanced Options

Provisioning Command

..
  OpenStack Scalable File Service (SFS)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  The |morpheus| integration with Openstack Cloud includes the capability to work with Openstack Scalable File Service (SFS). SFS is shared file storage hosted on Openstack Cloud. By integrating |morpheus| with Openstack you can discover, create, manage, and delete SFS servers, as well as view and work with the file shares and files contained therein.

  SFS Server Discovery and Management
  ```````````````````````````````````

  On integrating Openstack Cloud with |morpheus|, SFS servers and file shares are discovered automatically after a short time. The server(s) can be viewed in Infrastructure > Storage > Servers. By viewing the server detail page and clicking :guilabel:`EDIT`, the storage server can be scoped as needed. Administrators can choose to scope to other Openstack Cloud integrations (if more than one relevant integration currently exists), select from synced availability zones, and scope the storage server to specific Tenants if desired.

  Additionally, Openstack SFS servers can be created from the storage server list page (Infrastructure > Storage > Servers) directly in |morpheus|. Click :guilabel:`+ADD` to begin and set the storage server type value to "Openstack SFS". Just like with existing synced SFS servers, those created from |morpheus| can be scoped as needed.

  .. image:: /images/integration_guides/clouds/openstack/addSfs.png
    :width: 50%

  SFS File Share Discovery and Management
  ```````````````````````````````````````

  Discovered file shares will appear among other file shares synced with |morpheus| in Infrastructure > Storage > File Shares. Depending on the number of cloud integrations in your |morpheus| appliance and the number of cloud integrations available to your user account, this list may be quite large. Using the search bar on this page, we can narrow down the list to only file shares whose names match the search terms.

  We can drill into individual file shares by clicking on the hyperlinked name in the list of all integrated file shares. From the file share detail page, a list of files will appear on the files tab. Begin the process of adding a new file by clicking :guilabel:`+ADD`. The Access tab on the file shares detail page allows users to view and manage ACL rules.

  .. NOTE:: "Failed to load files from storage provider" is present when the |morpheus| appliance doesn't have access to the file share.

  New Openstack SFS file shares can also be created directly in |morpheus|. From the file shares list page, get started by clicking :guilabel:`+ADD`. Select the type "Openstack SFS Share". Set the storage service field to a pre-existing Openstack SFS server. Setting a friendly name for the file share in |morpheus| and selecting from synced availability zones is required.
