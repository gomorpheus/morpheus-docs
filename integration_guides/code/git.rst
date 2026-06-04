.. _git_integration:

Git Repository Integration
==========================

Overview
--------

|morpheus| integrates with Git repositories (both self-hosted and cloud-hosted) to provide version-controlled source management for automation scripts, Terraform configurations, ARM templates, Kubernetes specs, and application deployment code.

Git integrations are configured in |ProCodInt| (Provisioning > Code > Integrations) and enable |morpheus| to pull Task scripts, Spec Templates, and other configuration content directly from repositories.

Adding a Git Integration
-------------------------

To add a generic Git repository integration:

#. Navigate to |ProCodInt|
#. Click :guilabel:`+ ADD`
#. Select **Git Repository** as the integration type
#. Complete the configuration:

   - **NAME:** Descriptive name for the integration
   - **ENABLED:** Toggle to enable/disable
   - **REPOSITORY URL:** The Git clone URL (HTTPS or SSH)

     - HTTPS: ``https://git.example.com/org/repo.git``
     - SSH: ``git@git.example.com:org/repo.git``

   - **DEFAULT BRANCH:** The default branch to use (e.g., ``main``, ``master``)
   - **AUTHENTICATION:**

     - **Username/Password:** For HTTPS repositories with basic auth
     - **Access Token:** For HTTPS with token-based authentication
     - **SSH Key:** Select a key pair from Infrastructure > Trust > Key Pairs for SSH access
     - **Credential:** Select a stored credential set

#. Click :guilabel:`SAVE`

|morpheus| validates connectivity and clones the repository metadata.

Repository Browsing
-------------------

Once integrated, repository contents can be browsed directly in |morpheus|:

#. Navigate to |ProCodRep| (Provisioning > Code > Repositories)
#. Select the repository
#. Browse the file tree, switch branches, and view file contents

.. NOTE:: File browsing requires the **Provisioning: Code Repositories** role permission set to "Read" or "Full".

Using Git Repositories with Tasks
-----------------------------------

Tasks can source their scripts from Git repositories:

#. When creating or editing a Task, set **SOURCE** to "Repository"
#. Select the Git integration from the **REPOSITORY** dropdown
#. Specify the file path in **WORKING PATH** (e.g., ``scripts/deploy.sh``)
#. Optionally specify a **BRANCH/TAG** (defaults to the integration's default branch)

   - To reference a specific tag: ``refs/tags/v1.0.0``
   - To reference a branch: ``feature/my-branch``

Each time the Task executes, |morpheus| pulls the latest version from the repository, ensuring scripts stay current without manual updates.

Using Git Repositories with Spec Templates
--------------------------------------------

Spec Templates (Library > Templates > Spec Templates) can be sourced from Git:

#. Set the source type to "Repository"
#. Select the repository and specify the file path
#. The template content is pulled from Git at execution time

Using Git Repositories with Blueprints
----------------------------------------

Terraform, ARM, CloudFormation, and Kubernetes blueprints can reference Git repositories for their configuration files. The Git integration provides:

- Version-controlled infrastructure-as-code
- Branch-based environment separation (dev, staging, production)
- Pull request workflows for infrastructure changes

Repository Synchronization
---------------------------

|morpheus| synchronizes repository metadata periodically:

- File tree structure is cached for browsing performance
- Branch and tag lists are refreshed on sync
- Manual refresh can be triggered from the repository detail page

To force a refresh:

#. Navigate to |ProCodRep|
#. Select the repository
#. Click :guilabel:`REFRESH` from the Actions menu

Authentication Methods
-----------------------

+---------------------------+------------------------------------------+
| Method                    | Use Case                                 |
+===========================+==========================================+
| Username/Password         | Basic HTTPS authentication               |
+---------------------------+------------------------------------------+
| Personal Access Token     | GitHub, GitLab, Bitbucket HTTPS access   |
+---------------------------+------------------------------------------+
| SSH Key Pair              | SSH-based Git access                     |
+---------------------------+------------------------------------------+
| Stored Credential         | Reusable credential from Trust section   |
+---------------------------+------------------------------------------+

Removing a Git Integration
---------------------------

#. Navigate to |ProCodInt|
#. Click the trash icon on the integration row
#. Confirm deletion

.. WARNING:: Removing a Git integration will break any Tasks, Spec Templates, or Blueprints that reference it. Update those resources to use a different source before removal.
