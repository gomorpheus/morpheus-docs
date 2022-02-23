BIND DNS
--------

|morpheus| offers the capability to integrate directly with BIND DNS to automatically create DNS entries for Instances when they are provisioned to a configured Cloud or Group.

Integrating BIND with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BIND integrations can be added in the global integrations section (|AdmInt|) and, once added (assuming they are not disabled), will be available to set as the DNS provider for Clouds or Groups as needed.

#. Navigate to |AdmInt|
#. Click :guilabel:`+ NEW INTEGRATION` and select "Bind DNS"
#. Configure the following:

  - **NAME:** A friendly name for the BIND integration in |morpheus|
  - **HOST:** The IP address or resolvable host name for the BIND server
  - **USERNAME:** SSH username for a machine account on the BIND server
  - **PASSWORD:** Password for the user listed in the previous field (not required if using an SSH key)
  - **PUBLIC KEY:** Public SSH key to connect to the BIND server (not required if password provided in the prior field)
  - **TSIG KEY:** Enter TSIG key if required based on your configuration
  - **RNDC KEY:** Enter RNDC key if required based on your configuration
  - **RNDC PORT:** Enter the configured RNDC port

#. Click :guilabel:`SAVE CHANGES`

If successful, a new BIND DNS entry will appear in the list alongside other integrated technologies. A green checkmark will appear next to the integration entry when |morpheus| is successfully in contact with the BIND server.

Configuring BIND DNS with Clouds and Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When adding or editing Clouds and Groups, open the Advanced Options section to associate a DNS integration with the Cloud or Group.

**Setting DNS on Groups**

#. Navigate to |InfGro| and select an existing Group (this can also be done when creating a new Group)
#. Click :guilabel:`EDIT`
#. Expand the Advanced Options Section
#. Select the BIND integration from the DNS SERVICE dropdown
#. Click :guilabel:`SAVE CHANGES`

**Setting DNS on Clouds**

#. Navigate to |InfClo| and select an existing Cloud (this can also be done when creating a new Cloud)
#. Click :guilabel:`EDIT`
#. Expand the Advanced Options Section
#. Select the BIND integration from the DNS INTEGRATION dropdown
#. Click :guilabel:`SAVE CHANGES`
