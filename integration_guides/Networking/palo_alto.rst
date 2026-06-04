.. _palo_alto_integration:

Palo Alto Networks
------------------

Overview
^^^^^^^^

|morpheus| integrates with Palo Alto Networks next-generation firewalls and Panorama management platforms to provide centralized security policy management alongside cloud provisioning workflows. The integration allows |morpheus| to apply security policies, manage firewall rules, and enforce zone-based segmentation as part of automated infrastructure deployment.

Key capabilities of the Palo Alto Networks integration include:

- Security policy and rule management
- Zone-based firewall configuration
- Address group and service group management
- Panorama device group support
- Security profile assignment during provisioning
- Commit workflow for staged policy changes

Prerequisites
^^^^^^^^^^^^^

Before configuring the Palo Alto integration in |morpheus|, ensure the following:

- A Palo Alto Networks firewall or Panorama appliance is accessible from the |morpheus| appliance over HTTPS (port 443)
- An API-capable administrative user account exists on the Palo Alto device
- API access is enabled on the management interface
- (Panorama) The desired device groups and templates are configured

Add Palo Alto Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Click :guilabel:`+ ADD`
#. Select ``Security`` > ``Palo Alto``
#. Complete the following fields:

   :NAME: A name for the Palo Alto integration in |morpheus|
   :URL: The management URL of the Palo Alto firewall or Panorama (e.g., ``https://192.168.1.1``)
   :USERNAME: API-capable admin username
   :PASSWORD: Password for the admin account

#. Click :guilabel:`ADD NETWORK INTEGRATION`

Once added, |morpheus| will connect to the Palo Alto appliance and sync existing security configuration including zones, address objects, address groups, services, security rules, and NAT rules.

Configure Cloud Security Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make the Palo Alto integration available during provisioning:

#. Navigate to ``Infrastructure > Clouds``
#. Select and edit the target Cloud
#. Expand the **Advanced Options** section
#. Select the Palo Alto integration in the ``SECURITY SERVER`` dropdown
#. Click :guilabel:`SAVE CHANGES`

Managing Security Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^

After the integration is established, security policies can be managed from the integration detail view:

Firewall Rules
``````````````

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the Palo Alto integration
#. Click the **Firewall** tab
#. From here, create, edit, or delete security rules

When creating rules, the following fields are available:

:Name: Rule name (required)
:Description: Optional rule description
:Enabled: Toggle rule enforcement
:Priority: Rule priority/order
:Source Zone: Source security zone
:Destination Zone: Destination security zone
:Source Address: Source address or address group
:Destination Address: Destination address or address group
:Service: Service or service group
:Action: Allow, Deny, Drop, or Reset

Commit Workflow
```````````````

Palo Alto Networks uses a commit-based configuration model. Changes made through |morpheus| are staged as candidate configuration and must be committed to take effect:

#. Make desired changes to security rules, groups, or policies
#. Review pending changes
#. Click :guilabel:`COMMIT` to apply changes to the running configuration
#. Alternatively, click :guilabel:`DISCARD` to abandon pending changes

.. IMPORTANT:: Uncommitted changes exist only in the candidate configuration. They do not affect traffic until committed. Multiple changes can be batched into a single commit operation.

Security Groups for Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a Cloud has a Palo Alto security server configured, security groups become available during instance provisioning:

#. During instance provisioning, in the **Configure** section
#. Expand **Security** options
#. Select the desired security group or policy to apply to the instance
#. The security policy will be applied as part of the provisioning workflow

.. NOTE:: The specific security options available during provisioning depend on the Palo Alto configuration and the address objects/groups defined on the appliance.

Troubleshooting
^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Issue
     - Resolution
   * - Integration fails to connect
     - Verify the URL is reachable from the |morpheus| appliance. Check that HTTPS/443 is open and the SSL certificate is valid or the appliance trusts the CA.
   * - Sync shows no objects
     - Verify the API user has sufficient permissions to read security configuration. On Panorama, ensure the correct device group is targeted.
   * - Commit fails
     - Check the Palo Alto system logs for validation errors. Commits can fail due to conflicting rules or missing referenced objects.
   * - Rules not taking effect
     - Ensure changes have been committed. Check rule ordering and ensure the rule is enabled.
