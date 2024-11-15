Network Groups
--------------

Network Groups are useful for grouping networks during provisioning and scaling or grouping availability subnets together such that during provisioning vm’s within an instance can be round robin provisioned across availability zones.

Adding Network Groups
^^^^^^^^^^^^^^^^^^^^^

1. Navigate to `Infrastructure > Network > Networks Groups`
2. Select :guilabel:`ADD`
3. Enter the following:

   Group info:
     * *Name*: Name of the Network Group in |morpheus|
     * *Description*: Details of the Network Group in |morpheus|
   Networks
     * Search for and select target Networks for the Network Group
     * Search for and select target Subnets for the Network Group
   Group Access
     * Set Group Access for the Network Group. Group access controls which Groups at provision time will have access to this resource. Select "all" (default) to give workloads provisioned to any Group access to this resource. If this resource should be restricted only to workloads provisioned to specific Groups, select all that apply.

2. Select :guilabel:`SAVE CHANGES`
