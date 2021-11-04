ESXi
----

The ESXi Cloud type enables managing and provisioning to ESXi hosts, even without the ESXi API enabled.

.. IMPORTANT:: The VMware ESXi integration is for adding a single ESXi / vSphere Hypervisor host. If you have vCenter please use the VMWare vCenter cloud type for full vSphere integraiton features.

To get started with VMware ESXi, simply add a VMware ESXi Cloud in either the ``Infrastructure -> Clouds or Infrastructure -> Groups`` section.

#. Select ``+ Create Cloud`` Button
#. Select ESXi from the Add Cloud modal
#. Select NEXT
#. Provide the following information.

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

   * ESXi Host name or IP address
   * Username ( This is normally root )
   * Password

.. NOTE:: If you receive the message "Error! Invalid cloud config" Please ensure you have ssh enabled on the ESXi host.

.. include:: /integration_guides/Clouds/advanced_options.rst

.. IMPORTANT:: ESXi provisioning require a vmx file, which is not included in an OVF/OVA export from vCenter. A proper vmx file must be included when adding a vmdk/ovf/ova image to Virtual Images in Morpheus for successful provisioning.
