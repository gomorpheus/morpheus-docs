Single Node Appliance Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When upgrading from 3.6.x to |morphver|, the following services will be automatically upgraded on Single Node (all-in-one) Appliances:

- MySQL upgrade to v5.7
- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v7.4

Debian / Ubuntu
```````````````
To upgrade Morpheus running on Ubuntu/Debian, download new deb package, stop the morpheus-ui, install the new deb package, then reconfigure.

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance_x.x.x-x.amd64.deb
  sudo morpheus-ctl stop
  sudo dpkg -i morpheus-appliance_x.x.x-1.amd64.deb
  sudo morpheus-ctl reconfigure

.. note:: In 4.x services will be stopped during package installation and started during the reconfigure process.

CentOS / RHEL
`````````````

To upgrade Morpheus running on CentOS/RHEL, download and install the new rpm package, stop the morpheus-ui, reconfigure and then start the morpheus-ui:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl stop
  sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl reconfigure

.. note:: In 4.x services will be stopped during package installation and started during the reconfigure process.
