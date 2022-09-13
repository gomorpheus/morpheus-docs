Upgrading Overview
^^^^^^^^^^^^^^^^^^

.. important::

   Known issue with embedded Elasticsearch upgrade: When upgrading to v5.4.8, v5.4.9 or v5.5.1, there is a potential issue with embedded Elasticsearch clustering on rolling upgrades and existing data migration for all embedded Elasticsearch architechtures. Refer to the :ref:`Release Notes` for additional informaiton.

|morpheus| Packages
...................

|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_


Upgrade Requirements
....................

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and VM node packages from the package-repo when appliance free space is needed.

  .. important:: BACKUP YOUR DATABASE before the upgrade! You can use the `appliance backup job in Morpheus <https://docs.morpheusdata.com/en/latest/getting_started/guides/backup_restore.html#create-a-backup-job>`_, then `rollback and restore your appliance <https://docs.morpheusdata.com/en/latest/getting_started/guides/backup_restore.html#restoring-an-appliance-from-backup>`_ if needed. Make sure you download the backup before you do the upgrade!

* For firewall/proxy/acl considerations, the domain for Appliance, Supplemental and Agent packages was changed recently to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com. Please update ACL's to allow access to https://downloads.morpheusdata.com when necessary.

.. include:: /release_notes/compatibility.rst
