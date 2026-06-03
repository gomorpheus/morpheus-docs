Uninstall Morpheus Agent
=========================

Linux Agents
------------

You can use the following to uninstall the Linux agent (contains commands for both rpm and deb agents):

.. code-block:: bash

   sudo rm /etc/apt/sources.list.d/morpheus.list
   sudo morpheus-node-ctl kill
   sudo apt-get -y purge morpheus-node
   sudo apt-get -y purge morpheus-vm-node
   sudo yum -y remove morpheus-node
   sudo yum -y remove morpheus-vm-node
   sudo yum clean all
   sudo systemctl stop morpheus-node-runsvdir
   sudo rm -f /etc/systemd/system/morpheus-node-runsvdir.service
   sudo systemctl daemon-reload
   sudo rm -rf /var/run/morpheus-node
   sudo rm -rf /opt/morpheus-node
   sudo rm -rf /etc/morpheus
   sudo rm -rf /var/log/morpheus-node
   sudo pkill runsv
   sudo pkill runsvdir
   sudo pkill morphd
   sudo usermod -l morpheus-old morpheus-node

Windows Agents
--------------

.. code-block:: powershell

   $app = Get-WmiObject -Class Win32_Product -Filter "Name = 'Morpheus Windows Agent'"
   $app.Uninstall()
