Github
------

Integrate your Github account with |morpheus| and have access to all your public and private repositories within the platform. Use your existing code and any future code to build automation Tasks and Workflows, onboard Spec Templates for Terraform and Kubernetes to build App configurations, and more. Each time code from your repositories is invoked, |morpheus| will pull the current live version (depending on configuration) so any recent changes to the code are used.

Generating an Access Token
^^^^^^^^^^^^^^^^^^^^^^^^^^

As of August 13, 2021, due to policy changes on the Github platform, |morpheus| requires an access token to authenticate with Github. Password authentication is no longer possible. To create a new access token:

#. Log in to Github
#. Click on your account profile avatar in the upper-right portion of the window
#. Click Settings
#. From the left nav, click on Developer Settings
#. Once again from the left nav, click Personal access tokens
#. Click Generate new token
#. Give the new token at least access to everything in the "repo" scope
#. Click Generate token
#. Copy the access token and save it for the next step when the integration is created

.. TIP:: We recommend using a long-lived token, Github even includes the option to have no expiration on your tokens. Should the token expire, any |morpheus| automation, App Blueprints, and Terraform or Kubernetes Spec Templates which are based on code contained in your repositories will no longer work. This could lead to failed provisioning and time spent troubleshooting to isolate the issue until the Github integration is refreshed with a new access token.

Creating an Integration
^^^^^^^^^^^^^^^^^^^^^^^

New Github integrations are created either in the global integrations section (|AdmInt|) or in the code integrations section (|ProCodInt|). You will need a Github access token to complete this step, see the prior section for instructions on obtaining a Github access code.

#. Navigate to the global integrations section (|AdmInt|) or the code integrations section (|ProCodInt|)
#. Click :guilabel:`+ADD`
#. Click Github
#. Configure the following:

    - **NAME:** A friendly name for the Github integration in |morpheus|
    - **ENABLED:** When marked, this Github integration is active and any code repositories are available for building |morpheus| automation and other constructs within the platform
    - **USERNAME:** The username for your Github account
    - **PASSWORD:** This is a legacy field, new integrations do not need to use this field
    - **ACCESS TOKEN:** Enter a valid Github access token, see the prior section for instructions on obtaining an access token
    - **KEY PAIR:** (Optional) Select a stored SSH keypair for Github SSH authentication
    - **ENABLE GIT REPOSITORY CACHING:** When unmarked, |morpheus| retrives code fresh from the repository each time it's invoked. When marked, |morpheus| will use a cached version of the code if it's less than five minutes old. In general, this should be left unmarked unless you are experiencing performance issues related to very large amounts of code being invoked many times during a deployment

#. Click :guilabel:`SAVE CHANGES`

.. NOTE:: In certain cases, it can take several seconds for the integration process to complete and the ADD INTEGRATION modal to be dismissed.

Viewing an Integrated Github Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When authentication is successful, click into the new Github integration from the list of available integrations. The Organizations tab will list each organization the Github account is associated with. The Repositories tab lists all public and private repositories which are associated with the account. We can also click in to each repository to view its files and folders, as well as create specific types of automation or Spec Templates from the files directly in this view.
