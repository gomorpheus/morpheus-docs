How to un-manage an Instance/VM/Host
====================================

Description
-----------

A managed VM (and associated Instance) needs to be unmanaged and returned to Discovered type.

Solution
--------

Delete the record from the ``Infrastructure > Compute`` (! not from Provisioning - Instances) selection with the following configuration in the Delete modal:

- ``Remove Infrastructure`` UNCHECKED
- ``Remove Associated Instances`` Must be checked if the server has an associated Instance, as deleting the VM but not the Instance would result in an abandoned Instance thus not allowed.
- ``Force Delete`` UNCHECKED

The most important items to be aware of when "un-managing" an Instance/VM/Host are:

#. The "Remove from Infrastructure" flag when deleting a VM or Host in |morpheus| determines if the actual VM is deleted from the target Infrastructure.

   - Checking "Remove Infrastructure" means you WANT TO DELETE THE ACTUAL VM. Typing "DELETE" in the confirmation field is required when "Remove From Infrastructure" is enabled.
   - Unchecking "Remove Infrastructure" means you only want to delete the record in |morpheus| but leave the actual VM untouched.

#. Deleting an Instance will always remove Infrastructure.

   .. IMPORTANT:: REPEAT: Deleting an Instance from the ``Provisioning`` section will always remove the VM aka Infrastructure.

#. After removing the record from |morpheus|, the VM must be in a Cloud with Inventory enabled to automatically be re-discovered.

Process
-------

Steps to delete a managed VM from |morpheus| and, when necessary, remove the associated Instance:

#. Navigate to the VM (not Instance) detail page at ``Infrastructure > Compute - VMs``

   .. NOTE:: VM's inside an Instance can be navigated to inside the Instance Details page by selecting the VM in the ``VM's`` seciton on the Instance Details page.

#. Select :guilabel:`DELETE`

#. Configure the DELETE HOST modal with the following settings:

   .. image:: /images/delete_host_modal.png
   
   - ``Remove Infrastructure`` UNCHECKED
   - ``Remove Associated Instances`` Must be checked if the server has an associated Instance, as deleting the VM but not the Instance would result in an abandoned Instance thus not allowed.
   - ``Force Delete`` UNCHECKED

   .. IMPORTANT:: If you have to type DELETE that means the ``Remove Infrastructure`` flag is selected and you are confirming deletion of the actual VM. Ensure ``Remove Infrastructure`` is UNCHECKED when you want to leave the VM intact!

#. Select :guilabel:`DELETE`

#. The VM and associated Insatnce will be removed from |morpheus| but the actual VM will remain.

#. Wait up to 5 min or click :guilabel:`REFRESH` on the associated Clouds details page to force a cloud sync.

   .. NOTE:: ``Inventory`` must be enabled on the associated cloud for the VM to automatically be re-discovered by |morpheus|.

#. The VM is now back in |morpheus| as discovered/unmanaged. To managed and create a new Instance from the VM, select :guilabel:`ACTIONS` : Convert To Managed.
