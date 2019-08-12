SCVMM
-----

Requirements
------------

- Access to SCVMM host on 5985 for Agent Installation
    - The Morpheus Agent is required, and is installed on the target SCVMM host via port 5985/winrm.
- User with Administrator privileges

Agent Requirement
-----------------

SCVMM and Hyper-V Integrations utilize the Morpheus Agent for communications with the Morpheus appliance, making the Morpheus Agent required. This also means SCVMM and Hyper-V Clouds can only point to one Morpheus Appliance at once. If another Morpheus Appliance adds a SCVMM or Hyper-V Cloud thats is already managed by another Morpheus Appliance, the Morpheus Agent appliance_url will be updated to point to the new Morpheus Appliance url, and the previous Morpheus Appliance iwll no longer be able to communicate with the SCVMM cloud or Hyper-V cloud until the agent configuration is updated to point to the previous Appliance again.

Add a SCVMM Cloud
^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ CREATE CLOUD`, select SCVMM, and then click :guilabel:`Next`.
#. Enter the following into the Create Cloud modal:

.. NOTE::  You will need to open is 5985 in order for |morpheus| to communicate to SCVMM. You will also want to make sure SCVMM has WinRM enabled.

Name
  Name of the Cloud in |morpheus|
Location
  Description field for adding notes on the cloud, such as location.
Visibility
  For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
SCVMM HOST
  IP or url of SCVMM host
USERNAME
  SCVMM Username. ex: svc.scvmm
PASSWORD
  SCVMM User Password
CLOUD
  To scope the SCVMM Integration to a single Cloud, select it from the Cloud dropdown, which populates after establishing communication and authorization over 5985 using the supplied username and password above. To scope to all Clouds, leave the srop down as ``Select Cloud``
HOST GROUP
  To scope the SCVVM Integration to a single host group, select a Host group from the drop down list. To scope to all Host Groups, select ``All Hosts``
Cluster
 To scope the SCVVM Integration to a single Cluster, select a Cluster from the drop down list. To scope to all Host Groups, select ``All``
WORKING PATH
  Path for |morpheus| to write to. ex: ``C:\Cloud``
DISK PATH
  Path for Virtual Disks. ex: ``C:\VirtualDisks``
HIDE HOST SELECTION FROM USERS
  Prevents host selection from appearing in provisioning wizards
INVENTORY EXISTING INSTANCES
  Enable to discover exiting VM's in the scoped resources.
ENABLE HYPERVISOR CONSOLE
  Enable to use VNC Hypervisor Console for Morpheus Console conneciton, vs the default SSH and RDP Console Conneciton methods. Requires resolution of all Hyper-V host names and access over port 443 from the Morpheus Appliance to Hyper-V hosts.
.. include:: /integration_guides/Clouds/advanced_options.rst

#. The Cloud can now be added to a Group or configured with additional Advanced options.
