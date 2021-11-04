Network Groups
--------------

Network Groups are useful for grouping networks during provisioning and scaling or grouping availability subnets together such that during provisioning vm’s within an instance can be round robin provisioned across availability zones.

Adding Network Groups
^^^^^^^^^^^^^^^^^^^^^

1. Navigate to `Infrastructure -> Network -> Networks Groups`
2. Select :guilabel:`ADD`
3. Enter the following:

   Group info:
     * *Name*: Name of the Network Group in |morpheus|
     * *Description*: Details of the Network Group in |morpheus|
   Networks
     * Search for and select target Networks for the Network Group
     * Search for and select target Subnets for the Network Group
   Group Access
     * Set Group Access and Defaults for the Network Group
   Tenant Permissions
     * Set Tenant Visibility for Network Group

2. Select :guilabel:`SAVE CHANGES`
