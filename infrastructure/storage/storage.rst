.. _storage:

Storage
=======

.. NOTE:: In v3.5.2 STORAGE PROVIDERS has been split out into BUCKETS and FILE SHARES sections.

Overview
--------

`Infrastructure > Storage` is for adding and managing Storage Buckets, File Shares, Volumes, Data Stores and Storage Servers for use with other Services in |morpheus|.

Role Requirements
^^^^^^^^^^^^^^^^^

There are two Role permissions for the `Infrastructure > Storage` section: `Infrastructure: Storage` and `Infrastructure: Storage Browser`. `Infrastructure: Storage` gives Full, Read, or No access to the `Infrastructure > Storage` sections. `Infrastructure: Storage Browser` controls file access for Buckets, File Shares, and supported HVM file-based Data Stores. Full `Infrastructure: Storage Browser` permission allows upload and deletion when the user also has Full access to the corresponding storage resource. Read permission allows browsing and download when the user also has at least Read access to that resource.

Default Storage
^^^^^^^^^^^^^^^

The default Storage path for Virtual Images, Backups, Deployment Archives, Archive Service, and Archived Snapshots is `var/opt/morpheus/morpheus-ui/`. Its is recommended to add Storage Buckets and File Shares for these targets in the `Infrastructure > Storage` section to avoid running out of disk space on the |morpheus| Appliance.

.. include:: buckets.rst
.. include:: file_shares.rst
.. include:: share_access.rst
.. include:: volumes.rst
.. include:: data_stores.rst
.. include:: servers.rst
.. include:: storage_hosts.rst
.. include:: snapshots.rst
