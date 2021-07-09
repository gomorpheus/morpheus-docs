.. _Repositories:

Repositories
============

The ``/provisioning/code`` **Repositories** section contains the repositories integrated with |morpheus| allowing users to browse repositories folders and files and view file contents from any branch, trigger a refresh, and create tasks, scripts and templates directly from the repos. 

- Browse integrated repositories 
- View repo files
- Switch branches
- Trigger repo refresh
- Filter by Integration, Organization or Text search
- Create Custom Views
- Create Tasks from repo files
- Create Spec Templates from repo files
  
Role Permissions
----------------

Access and capabilities for the **Repositories** section is determined by the following role permissions:

Feature Access: ``Infrastructure: Groups`` 
  - None: Cannot access Provisioning: Code section
  - Read or Full: Can access Provisioning: Code section

Feature Access: ``Provisioning: Code Repositories``
  - None: Cannot access Provisioning: Code Repositories
  - List Files: Can browse repo folder and file names, select branch, refresh Repositories. Cannot access/view file contents.
  - Read or Full: Can browse repo folder and file names, select branch, refresh Repositories and access/view file contents.
  
Feature Access: ``Provisioning: Tasks``
  - None: Cannot create Tasks from repo files in Repository browser
  - Read or Full: Can create Tasks from repo files in Repository browser
  
  Feature Access: ``Provisioning: Library``
    - None: Cannot create Spec Templates from repo files in Repository browser
    - Read or Full: Can create Spec Templates from repo files in Repository browser
    
