.. _storage:

Storage
=======

.. NOTE:: In v3.5.2 STORAGE PROVIDERS has been split out into BUCKETS and FILE SHARES sections.

Overview
--------

`Infrastructure -> Storage` is for adding and managing Storage Buckets, File Shares, Volumes, Data Stores and Storage Servers for use with other Services in |morpheus|.

Role Requirements
^^^^^^^^^^^^^^^^^

There are two Role permissions for the `Infrastructure -> Storage` section: `Infrastructure: Storage` and `Infrastructure: Storage Browser`. `Infrastructure: Storage` give Full, Read or No access to the `Infrastructure -> Storage` sections, while `Infrastructure: Storage Browser` is specific to `Buckets` and `Files Shares`. Full `Infrastructure: Storage Browser` permissions allows `Buckets` and `Files Shares` to be browsed and files and folders to be added, downloaded and deleted from the `Buckets` and `Files Shares`. Read `Infrastructure: Storage Browser` permissions allows `Buckets` and `Files Shares` to be browsed only.

Default Storage
^^^^^^^^^^^^^^^

The default Storage path for Virtual Images, Backups, Deployment Archives, Archive Service, and Archived Snapshots is `var/opt/morpheus/morpheus-ui/`. Its is recommended to add Storage Buckets and File Shares for these targets in the `Infrastructure -> Storage` section to avoid running out of disk space on the |morpheus| Appliance.

.. include:: buckets.rst
.. include:: file_shares.rst
.. include:: volumes.rst
.. include:: data_stores.rst
.. include:: servers.rst
