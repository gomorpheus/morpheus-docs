Deleting Instances
==================

It is important to know the difference between deleting an Instance from the Provisioning section, and deleting a VM from the Infrastructure section.

.. IMPORTANT:: Deleting an Instance a with Virtual Machines in it will always try to delete the actual Virtual Machines.

Instances are managed resources that may have one or multiple Virtual Machines associated. Since the VMs in the Instance are managed by |morpheus|, deleting an Instance with a Virtual Machines in it will always try to delete the actual Virtual Machines.

There are scenarios where deleting, or attempting to delete the associated Virtual Machines is not desired:

- The Instance needs to be deleted, but the actual Virtual Machines need to remain.
- The actual Virtual Machines have already been deleted outside of |morpheus|, so only the orphaned records in |morpheus| need to be removed.

Deleting an Instance without deleting Infrastructure
----------------------------------------------------

It is not possible to delete an Instance from the Provisioning section without removing the associated Infrastructure/VMs. However, this can be accomplished from the Infrastructure section by deselecting "Remove Infrastructure" when deleting the VM:

1. Navigate to the Virtual Machine record by clicking on the VM name in the Virtual Machines section of the Instance detail page or by navigating to ``Infrastructure > Compute > Virtual Machines`` and selecting the VM.

.. TIP: The global search bar makes it easy to find resources in any section.

2. Click "DELETE"

3. In the delete confirmation modal:

   - Uncheck "Remove Infrastructure"
   - Check "Remove Associated Instances"

   .. image:: /images/provisioning/deleteOnlyInstance.png

   .. IMPORTANT:: Ensure "Remove Infrastructure" is NOT checked if you do not want to delete the actual Virtual Machine.

4. Select DELETE

This will delete the Virtual Machine record as well as the Instance record but leave the Infrastructure/VM in place. If the VM is in a Cloud that is being inventoried, it will sync back into |morpheus| after the next Cloud refresh. You can disable automatic Cloud inventory by editing the Cloud (Infrastructure > Clouds > selected Cloud > EDIT button) and turning off this feature.


Deleting an Instance/VM that does not exist anymore
----------------------------------------------------

Deleting a managed resource outside of |morpheus| is not recommended as it will leave stranded record in |morpheus| and cause deleting the records in |morpheus| to get stuck on delete when |morpheus| tries to remove infrastructure that is no longer there.

To select an Instance and/or VM record in |morpheus| for a Virtual Machine that no longer exists:

1. Navigate to the Virtual Machine record by clicking on the VM's name in the Virtual Machines section in the Instances details section, or by navigating to `Infrastructure -> Compute - Virtual Machines` and selecting the VM.

.. TIP: Global Search makes it easy to find resources in any section.

2. Click "DELETE"

3. In the delete confirmation modal:

   - Uncheck "Remove Infrastructure"
   - Check "Remove Associated Instances"

   .. image:: /images/provisioning/deleteOnlyInstance.png

   .. IMPORTANT:: Ensure "Remove Infrastructure" is NOT checked. If it is checked, |morpheus| will try to delete the actual VM, and since it is not there anymore, the delete will not complete successfully since |morpheus| will not be able to verify successful deletion of the Infrastructure.

4. Select DELETE

The key point is when deleting an Instance, or when selecting "Remove Infrastructure" when deleting a VM record, |morpheus| will always try to remove the Infrastructure. If the Infrastructure/VM no longer exists, or you do not want to remove it, simply delete from the Infrastructure section and uncheck "Remove Infrastructure".

.. NOTE:: When deleting a managed VM, if that VM is the only VM inside the associated Instance, the Associated Instance must also be removed. Additionally, when removing Instances, even if the infrastructure is not removed, some related teardown tasks are still performed. These can include removing IP addresses or IPAM integration entries, deletion of Active Directory objects, and any Teardown-phase Workflow Tasks. This is done to prevent orphaned records in the |morpheus| database and any associated integrations. Please consider how these processes could affect your infrastructure and take any needed actions to prevent issues.
