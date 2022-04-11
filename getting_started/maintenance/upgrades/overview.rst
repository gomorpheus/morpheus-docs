Upgrading Overview
^^^^^^^^^^^^^^^^^^

|morpheus| Packages
...................

|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_


Upgrade Requirements
....................

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and VM node packages from the package-repo when appliance free space is needed.

  .. important:: BACKUP YOUR DATABASE before the upgrade! You can use the `appliance backup job in Morpheus <https://docs.morpheusdata.com/en/latest/getting_started/guides/backup_restore.html#create-a-backup-job>`_, then `rollback and restore your appliance <https://docs.morpheusdata.com/en/latest/getting_started/guides/backup_restore.html#restoring-an-appliance-from-backup>`_ if needed. Make sure you download the backup before you do the upgrade!

* For firewall/proxy/acl considerations, the domain for Appliance, Supplemental and Agent packages was changed recently to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com. Please update ACL's to allow access to https://downloads.morpheusdata.com when necessary.

.. include:: /release_notes/compatibility.rst
