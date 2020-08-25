Appliance Settings
^^^^^^^^^^^^^^^^^^

Host Level Firewall Enabled
  Enables or Disables the host level firewall. This must be Enabled to use |morpheus| Security Groups.
Appliance URL
  The default URL used for Agent install and Agent functionality. All Instances and Hosts must be able to resolve and reach this URL over 443 for successful agent install and communication.

.. NOTE:: Alternate Appliance URLs can be configured per Cloud in the `Edit Cloud -> Advanced Options` section.

Internal Appliance URL (PXE)
  For PXE-Boot your appliance needs to be routable directly with minimal NAT masquerading. This allows one to override the default appliance url endpoint for use by the PXE Server. If this is unset, the default appliance url will be used instead.
API Allowed Origins
  Specifies which origins are allowed to access the |morpheus| API.
Enable SSL Verification of Agent (Communications)
  Enabling SSL Verification of Agent Communications requires a valid Certificate be installed on the Appliance.
Disable SSH Password Authentication
  Only allow ssh login using SSH keys. When true, SSH Password Authentication will not be enabled for VM's and Hosts provisioned after the setting is enabled.
