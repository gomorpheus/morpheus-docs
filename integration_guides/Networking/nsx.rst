NSX
---

Add NSX Integration
^^^^^^^^^^^^^^^^^^^

#. Navigate to `INFRASTRUCTURE -> NETWORK`
#. Select the  `SERVICES` tab
#. Select Select :guilabel:`+ ADD` -> VMWare NSX
#. Enter the following:

   NAME
    Name for the NSX Integration in |morpheus|
   API HOST
    URL of NSX Manager
   USERNAME
    NSX Manager Admin Username
   PASSWORD
    NSX Manager Admin password
   VMWARE CLOUD
    Select the existing VMware cloud associated with this NSX integration.

#. Select :guilabel:`ADD NETWORK INTEGRATION`

Once the NSX Integration is added |morpheus| will sync in existing Transport Zones, Logical Switches, and Edge Gateways. New Transport Zones, Logical Switches, and Edge Gateways can be now be created.

Create NSX Transport Zone
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `INFRASTRUCTURE -> NETWORK`
#. Select the  `SERVICES` tab
#. Select the name of NSX Integration
#. Select the `TRANSPORT ZONES` tab
#. Select :guilabel:`+ CREATE NSX TRANSPORT ZONE`

   NAME
    Name of Transport Zone
   DESCRIPTION
    Description for the Transport Zone
   CLUSTER
    Select the Cluster the Transport Zone will be provisioned to

Create NSX Logical Switch and Edge Gateway
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. IMPORTANT:: Prior to creating a Logical Switch and Edge Gateway, associated External VMware Networks must be configured in |morpheus|. Navigate to `INFRASTRUCTURE -> NETWORK` and edit any Distributed Switch Groups that will be used and populate the Gateway, DNS and CIDR

#. Navigate to `INFRASTRUCTURE -> NETWORK`
#. Select the  `SERVICES` tab
#. Select the name of NSX Integration
#. Select the `LOGICAL SWITCHES` tab
#. Select :guilabel:`+ CREATE NSX LOGICAL SWITCH`
#. Populate the following for the Logical Switch and Edge Gateway Configurations:

   Logical Switch Configuration:

   NAME
    Name of the Logical Switch
   DESCRIPTION
    d
   TRANSPORT ZONE
    Select an existing Transport Zone
   CIDR
    Add the CIDR for the Logical Switch. Example: 10.30.28.0/24
   TENANT NAME
    Enter Tenant name for the Logical Switch (Optional)
   Edge Gateway Configuration:

   HOSTNAME
    Enter Hostname of the Edge Gateway
   SIZE
    Select Size of the Edge Gateway
   EXTERNAL NETWORK
    Select the External Network for the Edge Gateway.

    .. IMPORTANT:: The Gateway, DNS and CIDR must be populated on an external network for it to be selectable when creating an Edge Gateway.

   IP ADDRESS
    Populate IP address to be assigned to the Edge Gateway
   DATA STORE
    Select the Datastore for the Gateway
   RESOURCE POOL
    Select the Resource Pool for the Gateway
   FOLDER
    Select a Folder for the Edge Gateway (optional)
   USERNAME
    Enter a Username for the Edge Gateway
   PASSWORD
    Enter a Password for the Edge Gateway

    .. NOTE:: Password length must be at-least 12 characters and at-max 255 characters. It must contain mix of alphabets with both upper case and lower case, numbers and at-least one special character. Password must not contain username as substring. Character must not consecutively repeat 3 or more times.

#. Select :guilabel:`+ CREATE`
