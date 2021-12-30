Security Groups
---------------

``Infrastructure > Network - Security Groups``

Overview
^^^^^^^^

A security group acts as a virtual firewall that controls the traffic for one or more Instances. When you launch an instance, you associate one or more security groups with the instance. You add rules to each security group that allow traffic to or from its associated Instances. You can modify the rules for a security group at any time; the new rules are automatically applied to all Instances that are associated with the security group.

.. IMPORTANT:: The Host Level Firewall must be enabled for Security Groups to be applied. The Host Level Firewall can be enabled in |AdmSetPro| > Host Level Firewall Enable/Disable

.. IMPORTANT:: When local firewall management is enabled, Morpheus will automatically set an IP table rule to allow incoming connections on tcp port 22 from the Morpheus Appliance.

Add Security Group
^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the `+ Add Security Group` button.
#. From the Security Group Wizard input a name, and description.
#. Save Changes

Add Security Group Rule
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the name of the security group you wish to add a rule to.
#. From the security group page click the `+ Add Rule` button.
#. From the Rule Wizard select the rule type and input source and depending on the type selected protocol and input a port range.
#. Save Changes

Edit security group rule
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the name of the security group you wish to edit a rule in.
#. Click the edit icon on the row of the security group rule you wish to edit.
#. Modify information as needed.
#. Save Changes

Delete security group rule
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Network - Security Groups`
#. Click the name of the security group you wish to delete a rule from.
#. Click the delete icon on the row of the security group rule you wish to delete.

Add Cloud Security Group
^^^^^^^^^^^^^^^^^^^^^^^^^

To add Cloud security group

#. Navigate to `Infrastructure > Clouds`
#. Click the name of the desired cloud to add a security group
#. Click the Networks tab
#. Within the "Security Groups" section, click on a security group to edit its rules
#. Alternatively, click :guilabel:`+ ADD SECURITY GROUP` to create a new one

Remove Cloud Security Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure > Clouds`
#. Click the name of the cloud to remove the Security Group from.
#. Click the Security Groups tab.
#. Click the `Edit Security Groups` button.
#. Click the - (Minus) button of the Security Group from the Added Security groups list to remove.
#. Save Changes
