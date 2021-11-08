vCloud Director
---------------

Configuration
^^^^^^^^^^^^^

Add vCD Cloud From ``Infrastructure > Clouds``
`````````````````````````````````````````````

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ ADD`
#. Select **VCLOUD DIRECTOR** from the Clouds list
#. Select :guilabel:`NEXT`
#. Populate the following:

   .. include:: /integration_guides/Clouds/base_options.rst

   Details
   ```````
   API URL
     vCloud Director API Url
      Example: ``https://org.vcd.company.com``
   USERNAME
     vCD Organization Administrator or System Administrator User

     - User must have an Organizational Administrator or System Administrator Role
     - Username must be in the format of <name>@<org>
     - When using a user with the System Administrator role, ensure this user has permission set correctly, such as to view objects created by the organization administrator if needed. Otherwise, things like catalogs and vApps created by the Organization Administrator might not be visible to |morpheus|

   PASSWORD
    Password for the user indicated above
   ORGANIZATION
    Select Organization. Dropdown populates upon successful authorization.
   VDC
    Select VDC. Dropdown populates upon successful authorization.
   API VERSION
    Example. ``31.0`` Note: Full version required. ``31`` would not be valid, must be xx.x (vCD API versions are strings)
   CATALOG
    Optionally select a vCD catalog to store |morpheus| artifacts or use the default "morpheus_auto" catalog
   Inventory Existing Instances
    If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

   .. NOTE: Multiple Organizations/VDC's can be added by creating additional Clouds in |morpheus|. Additionally, websockets need to be enabled on your load balancer when vCD has been deployed in a highly available configuration. The hypervisor console services use websockets. To enable websockets on your load balancer, please consult your load balancer documentation.

   .. include:: /integration_guides/Clouds/advanced_options.rst

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`

.. include:: /integration_guides/Clouds/vCloudDirector/creatingvcloud.rst
​
