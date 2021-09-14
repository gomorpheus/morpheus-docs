Cloud Profiles
--------------

Role Permissions
^^^^^^^^^^^^^^^^

Access to **Profiles** tab is determined by the following role permissions:

Role: Feature Access: ``Admin: Profiles`` 
  - None: Cannot access Profiles tab or create/view//edit/delete profiles
  - Read: Can access Profiles tab, can view profiles, cannot create/edit/delete profiles
  - Full: Can access Profiles tab, can create/view/edit/delete profiles
  
Create a Profile
^^^^^^^^^^^^^^^^

#. Navigate to ``/infrastructure/clouds/`` and select a Cloud
#. Select the ``Profiles`` tab 
#. Select :guilabel:`+ ADD PROFILE`
#. Select Profile Type 

    - Terraform Profiles allow created cloud associated tfvars secrets, allowing tf apps and specs to be provisioned across multiple clouds that required different tfvars.
    - Key/Value Profiles expand provisioning, automation, billing and reporting capabilities by allowing dynamic custom object specific metadata in provisioning and automation mappings using ``<%=cloud.profile.key%>``
    
#. Populate Profile fields 
#. Select :guilabel:`SAVE CHANGES` 


