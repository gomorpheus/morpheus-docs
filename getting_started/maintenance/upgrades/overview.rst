Upgrading Overview
^^^^^^^^^^^^^^^^^^

|morpheus| Packages
...................

|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 
    

Upgrade Requirements
....................

.. warning:: |morpheus| |morphver| contain new node and vm node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed. 

  .. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* For firewall/proxy/acl considerations, the domain for Appliance, Supplemental and Agent packages was changed recently to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com. Please update ACL's to allow access to https://downloads.morpheusdata.com when necessary. 

.. include:: /release_notes/compatibility.rst

