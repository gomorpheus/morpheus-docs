Scripts
========================================

ISCIS Discovery and MultiPathing Specific Target
^^^^^^^^

.. code-block:: bash

    eths=("eth1" "eth2")
    portals=("192.168.3.40" "192.168.9.40")
    target="iqn.2005-10.org.freenas.ctl:lun1"
     
    for i in {0..1}; do
      iscsiadm -m iface -I iface$i -o new -n iface.net_ifacename -v ${eths[$i]}
      iscsiadm -m discovery -t st -p ${portals[$i]} -I iface$i
      iscsiadm -m node -p ${portals[$i]} --login -I iface$i
      sudo iscsiadm -m node -T $target -p ${portals[$i]} -I iface$i --op update -n node.startup -v automatic
    done

ISCIS Discovery and MultiPathing all Targets
^^^^^^^^     
.. code-block:: bash

    eths=("eth1" "eth2")
    portals=("192.168.3.40" "192.168.9.40")
     
    for i in {0..1}; do
      iscsiadm -m iface -I iface$i -o new -n iface.net_ifacename -v ${eths[$i]}
      iscsiadm -m discovery -t st -p ${portals[$i]} -I iface$i
      iscsiadm -m node -p ${portals[$i]} --login -I iface$i
      sudo iscsiadm -m node -p ${portals[$i]} -I iface$i --op update -n node.startup -v automatic
    done