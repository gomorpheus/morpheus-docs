Git
---

Git Repository integrations allow integration of public or private Git repositories in Github, GitLab or other services. Use your existing code and any future code to build automation Tasks and Workflows, onboard Spec Templates for Terraform and Kubernetes to build App configurations, and more. Each time code from your repositories is invoked, |morpheus| will pull the current live version (depending on configuration) so any recent changes to the code are used.

Creating an Integration
^^^^^^^^^^^^^^^^^^^^^^^

New Git integrations are created either in the global integrations section (|AdmInt|) or in the code integrations section (|ProCodInt|). You will need an access code for authentication with private repositories, public repositories can be integrated simply with a URL.

#. Navigate to the global integrations section (|AdmInt|) or the code integrations section (|ProCodInt|)
#. Click :guilabel:`+ADD`
#. Click Git repository
#. Configure the following:

    - **NAME:** A friendly name for the Git repository integration in |morpheus|
    - **ENABLED:** When marked, code in this repository will be available for creating automation or other |morpheus| constructs
    - **DEFAULT BRANCH:** The default repository branch from which code should be sourced
    - **USERNAME:** For private repositories, enter an account name (such as a Github username)
    - **PASSWORD:** For Github and GitLab, password authentication is no longer supported **but access tokens should go in this field.**
    - **ACCESS TOKEN:** Currently an unused field, access tokens should go in the Password field
    - **KEY PAIR:**  (Optional) Select a stored SSH keypair for Github SSH authentication
    - **ENABLE GIT REPOSITORY CACHING:** When unmarked, |morpheus| retrieves code fresh from the repository each time it's invoked. When marked, |morpheus| will use a cached version of the code if it's less than five minutes old. In general, this should be left unmarked unless you are experiencing performance issues related to very large amounts of code being invoked many times during a deployment

#. Click :guilabel:`SAVE CHANGES`
