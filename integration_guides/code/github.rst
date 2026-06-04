.. _github_integration:

GitHub Integration
==================

Overview
--------

|morpheus| provides dedicated GitHub integration that extends the base Git capabilities with GitHub-specific features including organization browsing, repository discovery, and GitHub API integration for enhanced code management workflows.

GitHub integrations allow |morpheus| to:

- Browse GitHub organizations and their repositories
- Pull Task scripts, templates, and configurations from GitHub repos
- Leverage GitHub authentication (personal access tokens, OAuth)
- Discover and sync repository contents with branch/tag support

Adding a GitHub Integration
----------------------------

To add a GitHub integration:

#. Navigate to |ProCodInt| (Provisioning > Code > Integrations)
#. Click :guilabel:`+ ADD`
#. Select **GitHub** as the integration type
#. Complete the configuration:

   - **NAME:** Descriptive name for the integration
   - **ENABLED:** Toggle to enable/disable
   - **GITHUB API URL:** API endpoint URL

     - GitHub.com: ``https://api.github.com`` (default)
     - GitHub Enterprise: ``https://github.yourcompany.com/api/v3``

   - **ACCESS TOKEN:** GitHub Personal Access Token with appropriate scopes
   - **ORGANIZATION:** (Optional) Default organization to browse

#. Click :guilabel:`SAVE`

GitHub Personal Access Token
-----------------------------

A Personal Access Token (PAT) is required for authentication. Generate one in GitHub:

#. Navigate to GitHub Settings > Developer Settings > Personal Access Tokens
#. Click **Generate new token**
#. Required scopes:

   - ``repo`` — Full control of private repositories (or ``public_repo`` for public only)
   - ``read:org`` — Read organization membership (for org browsing)

#. Copy the generated token and paste it into the |morpheus| integration configuration

.. NOTE:: For GitHub Enterprise, ensure the token is authorized for the target organization if SSO is enabled.

Browsing Organizations
-----------------------

With a GitHub integration configured:

#. Navigate to |ProCodRep| (Provisioning > Code > Repositories)
#. The integration shows available organizations
#. Select an organization to list its repositories
#. Select a repository to browse its contents

Repository features:

- Browse file trees across branches and tags
- View file contents with syntax highlighting
- Switch between branches using the branch selector
- Search repositories by name

Using GitHub Repositories
--------------------------

GitHub repositories integrate with |morpheus| automation:

**Tasks:**

- Source scripts from GitHub repositories
- Specify repository, file path, and branch/tag
- Scripts are pulled fresh on each execution

**Spec Templates:**

- Store Terraform, Kubernetes, Helm, and other IaC templates in GitHub
- Reference specific files and branches
- Changes in GitHub are automatically reflected

**Blueprints:**

- Terraform blueprints can reference GitHub repos for ``.tf`` files
- Multiple environments via branch-based configuration
- Support for Terraform modules in subdirectories

**Deployments:**

- Application code from GitHub repos can be deployed to Instances
- Supports branch/tag selection for deployment versioning

GitHub Enterprise Support
--------------------------

|morpheus| supports GitHub Enterprise Server installations:

- Custom API URL pointing to your GHE instance
- Same authentication and browsing capabilities as GitHub.com
- SSL certificate verification (ensure GHE certificate is trusted by |morpheus| appliance)

To configure for GitHub Enterprise:

#. Set the **GITHUB API URL** to your GHE API endpoint (e.g., ``https://github.corp.com/api/v3``)
#. Ensure network connectivity between |morpheus| and the GHE server
#. If using a self-signed certificate, add the CA certificate to the |morpheus| trust store

Webhook Integration
--------------------

GitHub webhooks can be configured to notify |morpheus| of repository changes:

- Push events trigger repository synchronization
- Enables near-real-time updates for Task scripts and templates
- Webhook URL format: ``https://<morpheus-url>/api/code/webhooks/github``

Differences from Generic Git
------------------------------

The GitHub-specific integration provides additional capabilities over the generic Git integration:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Feature
     - Generic Git
     - GitHub
   * - Repository browsing
     - Single repo
     - Org-level discovery
   * - Authentication
     - User/pass, SSH, token
     - PAT, OAuth, GitHub App
   * - Organization browsing
     - No
     - Yes
   * - Webhook support
     - No
     - Yes
   * - API integration
     - Git protocol only
     - GitHub REST API

Removing a GitHub Integration
------------------------------

#. Navigate to |ProCodInt|
#. Click the trash icon on the GitHub integration row
#. Confirm deletion

.. WARNING:: Removing a GitHub integration will break any Tasks, Templates, or Blueprints sourcing content from its repositories. Migrate references before removal.
