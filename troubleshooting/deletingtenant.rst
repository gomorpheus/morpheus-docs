Unable to Delete Tenant
========================

Problem
  When trying to delete a tenant, a message stating ``managed resources must be removed`` or other errors occur and the tenant is not deleted. The tenant may be stuck in a deleting status or return to OK status after delete attempt.

Cause
  All managed resources must be removed from a tenant in order for that tenant to be deleted. This includes instances and their underlying managed VM's

Solution
  #. Login or impersonate an Admin user inside the tenant
  #. Navigate to Infrastructure > Hosts
  #. Under Hosts and VM's, delete any managed resources

     - Uncheck ``remove infrastructure`` when deleting a VM to only remove it from |morpheus| but not from the underlying hypervisor/cloud
     - You must check ``remove associated instances`` if the VM has an associated instance
     - If the VM no longer exists but there is still a record in |morpheus|, uncheck ``remove infrastructure`` and check ``force delete``

     .. WARNING:: Managed resources can also be removed by deleting instances, but be aware this will delete VM's associated with the instance from the underlying hypervisor/cloud

  #. Once all managed resources are removed from the tenant, the tenant can then be deleted
  #. In certain situations other components may prevent a tenant from being deleted. If you have removed all managed resources from a tenant and the tenant still cannot be deleted, please contact |morpheus| support
