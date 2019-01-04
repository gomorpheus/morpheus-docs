vCloud Director
---------------


Overview
^^^^^^^^^

VMware vCloud Director (vCD) is deployment, automation and management software for virtual infrastructure resources in multi-tenant cloud environments.

Features
^^^^^^^^^
* IP Pool allocated IPs sync
* Virtual Machine sync includes undeployed VMs
* IP Pools sync
* “Add User” option during provisioning
* Custom Plans Support
* Docker Host support
* Reconfigure
* Support for VCD v9
* Support for v9.x





Configuration
^^^^^^^^^^^^^

Add vCD Cloud From `Infrastructure -> Clouds`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ ADD`
#. Select **VCLOUD DIRECTOR** from the Clouds list
#. Select :guilabel:`NEXT`
#. Populate the following:

   Name
    Name of the Cloud in |morpheus|
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   API URL
     vCloud Director API Url
      Example: ``https://org.vcd.company.com``
   USERNAME
     vCD Organization Administrator User

     NOTE:: User must have an Organizational Administrator Role in the selected Origination for successful provisioning

   PASSWORD
     vCD Organization Administrator User password
   ORGANIZATION
    Select Organization. Dropdown populates upon successful authorization.
   VDC
    Select VDC. Dropdown populates upon successful authorization.
   Inventory Existing Instances
    If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

   NOTE: Multiple Organizations/VDC's can be added by creating additional Clouds in |morpheus|.

   .. include:: /integration_guides/Clouds/advanced_options.rst

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`


Add vCD Cloud From `Infrastructure -> Groups`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to ``Infrastructure -> Groups``
#. Select a Group
#. Select the `CLOUDS` tab
#. Scroll down to **VCLOUD DIRECTOR** and select :guilabel:`+ ADD`
#. Populate the following:

   Name
    Name of the Cloud in |morpheus|
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   API URL
    vCloud Director API Url
     Example: ``https://org.vcd.company.com``
   USERNAME
    vCD Organization Administrator User

    NOTE:: User must have an Organizational Administrator Role in the selected Origination for successful provisioning

   PASSWORD
    vCD Organization Administrator User password
   ORGANIZATION
    Select Organization. Dropdown populates upon successful authorization.
   VDC
    Select VDC. Dropdown populates upon successful authorization.
   Inventory Existing Instances
    If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

    NOTE: Multiple Organizations/VDC's can be added by creating additional Clouds in |morpheus|.

    .. include:: /integration_guides/Clouds/advanced_options.rst


#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`

.. include:: /integration_guides/Clouds/vCloudDirector/creatingvcloud.rst
​
