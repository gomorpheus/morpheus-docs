**Cloud Configuration**

NAME
  Name of the Cloud in |morpheus|
CODE
  Unique code used for api/cli, automation and policies.
LOCATION
  Description field for adding notes on the cloud, such as location.
VISIBILITY
  For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
TENANT
  If Visibility is set to Private, select the Tenant the Cloud resources will assigned to.
ENABLED
  When disabled, automatic Cloud sync is paused and the Cloud will not be selectable for provisioning.
AUTOMATICALLY POWER ON VMS
  When enabled, |morpheus| will maintain the expected power state of managed VMs. |morpheus| will power on any managed VMs in the Cloud that have been shut down for unknown reasons (not powered off by |morpheus|) to ensure availability of services.

  .. note:: When "AUTOMATICALLY POWER ON VMS" is enabled, the power state of managed VMs should be maintained in |morpheus|. This setting is not applicable to discovered/unmanaged resources.
