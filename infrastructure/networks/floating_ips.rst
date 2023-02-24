Floating IPs
------------

Overview
^^^^^^^^

|morpheus| supports sync and management of floating IP addresses for OpenStack, Huawei, and OTC Clouds. When these Clouds are integrated and floating IPs are present, |morpheus| will automatically sync them in. Once synced, floating IPs are viewable from their own list page (|InfNetFlo|) and related options are presented during provisioning, teardown, and from Instance detail pages.

.. NOTE:: The Floating IPs tab is present only when supported Clouds are integrated and floating IPs are available. Additional Cloud support is planned for the future.

Floating IPs List Page
^^^^^^^^^^^^^^^^^^^^^^

All Floating IPs known to |morpheus| can be viewed on the Floating IPs List Page (|InfNetFlo|). From the Floating IPs list page we can see the following:

- **IP ADDRESS**: The address for the floating IP synced from a supported Cloud
- **CLOUD**: The Cloud integration the floating IP was synced from
- **STATUS**: "Free" when the floating IP is available and "Assigned" when the floating IP is currently assigned to a workload
- **VM**: For assigned floating IPs, the VM which currently has the floating IP attached

Free floating IPs will have a gear icon (|gear|) at the end of the row. Click the gear icon and select "Release Floating IP" to release from within the source cloud and remove the entry from the Floating IPs list.

.. image:: /images/infrastructure/network/floatIpList.png

Working with Floating IPs
^^^^^^^^^^^^^^^^^^^^^^^^^

When provisioning to supported Clouds, |morpheus| will give the option to attach a floating IP at provision time. From the CONFIGURE tab of the provisioning wizard for supported Clouds, select the desired floating IP.

.. image:: /images/infrastructure/network/floatIpSet.png

During Instance teardown, |morpheus| gives the option to release the floating IP.

.. image:: /images/infrastructure/network/floatIpDelete.png

..
  Attach and Detach Floating IPs from Instances
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
