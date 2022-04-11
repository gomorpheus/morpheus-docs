Security Groups
---------------

``Infrastructure > Network - Security Groups``

Overview
^^^^^^^^

A Security Group acts as a virtual firewall that controls the traffic for one or more Instances. When you launch an instance, you associate one or more Security Groups with the instance. You add rules to each Security Group that allow traffic to or from its associated Instances. You can modify the rules for a Security Group at any time; the new rules are automatically applied to all Instances that are associated with the Security Group.

.. IMPORTANT:: The local firewall setting must be enabled for Security Groups to be applied in the guest firewall (iptables). The local firewall setting can be enabled in |InfClo| > Click the Cloud > Edit > Advanced Options > Local Firewall (On/Off)

.. IMPORTANT:: When then local firewall setting is enabled, Morpheus will automatically set an iptable rule to allow incoming connections on tcp port 22 from the Morpheus Appliance.

.. IMPORTANT:: If the local firewall setting is configured on a cloud that supports Security Groups natively (AWS for example), the local firewall setting is ignored and the guest firewall will not be modified.  Security Groups will be attached to the instance as normal

Add Security Group
^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the `+ Add Security Group` button.
#. From the Security Group Wizard input a name, and description.
#. Save Changes

Add Security Group Rule
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the name of the Security Group you wish to add a rule to.
#. From the Security Group page click the `+ Add Rule` button.
#. From the Rule Wizard select the rule type and input source and depending on the type selected protocol and input a port range.
#. Save Changes

Edit Security Group rule
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the name of the Security Group you wish to edit a rule in.
#. Click the edit icon on the row of the Security Group rule you wish to edit.
#. Modify information as needed.
#. Save Changes

Delete Security Group rule
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the name of the Security Group you wish to delete a rule from.
#. Click the delete icon on the row of the Security Group rule you wish to delete.

Add Cloud Security Group
^^^^^^^^^^^^^^^^^^^^^^^^^

To add Cloud Security Group

#. Navigate to `Infrastructure > Clouds`
#. Click the name of the desired cloud to add a Security Group
#. Click the Networks tab
#. Within the "Security Groups" section, click on a Security Group to edit its rules
#. Alternatively, click :guilabel:`+ ADD SECURITY GROUP` to create a new one

Remove Cloud Security Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Clouds`
#. Click the name of the cloud to remove the Security Group from.
#. Click the Security Groups tab.
#. Click the `Edit Security Groups` button.
#. Click the - (Minus) button of the Security Group from the Added Security Groups list to remove.
#. Save Changes
