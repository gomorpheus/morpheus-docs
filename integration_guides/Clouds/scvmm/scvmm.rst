SCVMM
-----

Requirements
------------

- Access to SCVMM host on port 5985 for Agent installation
- |morpheus| Agent installation (installed on the target SCVMM host via port 5985 and WinRM)
- User with administrator privileges


Agent Requirement
-----------------

SCVMM and Hyper-V integrations utilize the |morpheus| Agent for communication with the |morpheus| appliance, making the |morpheus| Agent required. This also means SCVMM and Hyper-V Clouds can only point to one |morpheus| Appliance at any given time. If another |morpheus| Appliance adds an SCVMM or Hyper-V Cloud thats is already managed by another |morpheus| Appliance, the |morpheus| Agent appliance_url will be updated to point to the new |morpheus| appliance_url, and the previous |morpheus| Appliance will no longer be able to communicate with the SCVMM Cloud or Hyper-V Cloud until the Agent configuration is updated to point to the previous appliance again.

.. NOTE:: |morpheus| only supports integration with standalone SCVMM installations and not high-availability cluster installation at this time.

Add a SCVMM Cloud
^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clouds``
#. Select :guilabel:`+ CREATE CLOUD`, select SCVMM, and then click :guilabel:`Next`.
#. Enter the following into the Create Cloud modal:

.. NOTE::  You will need to open port 5985 in order for |morpheus| to communicate to SCVMM. You will also want to make sure SCVMM has WinRM enabled.

NAME
  Name of the Cloud in |morpheus|
CODE
  An optional short code used for API and variables
LOCATION
  Description field for adding Cloud locations
VISIBILITY
  For setting Cloud permissions in a multi-tenant environment, this field is not applicable in single-Tenant environments
ENABLED
  When checked, makes the configured Cloud available for use in |morpheus|
AUTOMATICALLY POWER ON VMS
  When checked, provisioned VMs will automatically be powered on
SCVMM HOST
  IP address or URL of SCVMM host server
USERNAME
  SCVMM Username, for example: svc.scvmm
PASSWORD
  SCVMM user Password
CLOUD
  To scope the SCVMM Integration to a single Cloud, select it from the Cloud dropdown, which populates after establishing communication and authorization over port 5985 using the supplied username and password. To scope to all Clouds, leave the dropdown selection as ``Select Cloud``
HOST GROUP
  To scope the SCVMM Integration to a single host group, select a host group from the dropdown list. To scope to all host groups, select ``All Hosts``
CLUSTER
 To scope the SCVMM Integration to a single cluster, select a cluster from the dropdown list. To scope to all host groups, select ``All``
WORKING PATH
  Path for |morpheus| to write to, for example ``c:\cloud``
DISK PATH
  Path for Virtual Disks, for example ``c:\virtualdisks``
HIDE HOST SELECTION FROM USERS
  Prevents host selection from appearing in provisioning wizards
INVENTORY EXISTING INSTANCES
  Enable for |morpheus| to automatically discover existing VMs in the scoped resources
ENABLE HYPERVISOR CONSOLE
  Enable to use VNC Hypervisor Console for |morpheus| console connection as opposed to the default SSH and RDP console connection methods. Requires resolution of all Hyper-V host names and access over port 443 from the |morpheus| appliance to Hyper-V hosts.

.. include:: /integration_guides/Clouds/advanced_options.rst

After clicking :guilabel:`NEXT`, the new Cloud can be added to a Group or configured with additional advanced options.
