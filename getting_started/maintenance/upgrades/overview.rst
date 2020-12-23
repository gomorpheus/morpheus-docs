Upgrading Overview
^^^^^^^^^^^^^^^^^^

|morpheus| Packages
^^^^^^^^^^^^^^^^^^^
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 
    

Upgrade Requirements
^^^^^^^^^^^^^^^^^^^^

* Only appliances running Morpheus |minUpgradeVer| or higher can upgrade to |morphver|

  .. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* For firewall/proxy/acl considerations, the domain for Appliance, Supplemental and Agent packages was changed recently to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com. Please update ACL's to allow access to https://downloads.morpheusdata.com when necessary. 

Refer to :ref:`compatibility` for externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

