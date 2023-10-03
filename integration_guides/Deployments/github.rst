Github
------

Integrate your Github account with |morpheus| and have access to all your public and private repositories within the platform. Use your existing code and any future code to build automation Tasks and Workflows, onboard Spec Templates for Terraform and Kubernetes to build App configurations, and more. Integrated Github repositories also populate the Code list page (|ProCod|) where repositories can be browsed and individual files can be viewed. Repositories can be configured as `import and export <https://docs.morpheusdata.com/en/latest/provisioning/code/code.html?highlight=import#import-and-export>`_ targets from Code detail pages as well. Each time code from your repositories is invoked in Tasks, Workflows, Spec Templates, and more, |morpheus| will pull the current live version (depending on configuration) so any recent changes to the code are used.

Generating a Personal Access Token (Classic)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of August 13, 2021, due to policy changes on the Github platform, |morpheus| requires an access token to authenticate with Github. Password authentication is no longer possible. |morpheus| accepts both classic personal access tokens and fine-grained tokens (described in the next section). To create a new access token:

#. Log in to Github
#. Click on your account profile avatar in the upper-right portion of the window
#. Click Settings
#. From the left nav, click on Developer Settings
#. Once again from the left nav, click Personal access tokens
#. Click "Tokens (classic)"
#. Click Generate new token
#. Click "Generate new token (classic)"
#. Give the new token at least access to everything in the "repo" scope
#. Click Generate token
#. Copy the access token and save it for the next step when the integration is created

.. TIP:: We recommend using a long-lived token, Github even includes the option to have no expiration on your tokens (for classic personal access tokens only, not fine-grained tokens). Should the token expire, any |morpheus| automation, App Blueprints, and Terraform or Kubernetes Spec Templates which are based on code contained in your repositories will no longer work. This could lead to failed provisioning and time spent troubleshooting to isolate the issue until the Github integration is refreshed with a new access token.

Generating a Fine-Grained Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of August 13, 2021, due to policy changes on the Github platform, |morpheus| requires an access token to authenticate with Github. Password authentication is no longer possible. |morpheus| accepts both classic personal access tokens and fine-grained tokens. To create a new fine-grained access token:

#. Log in to Github
#. Click on your account profile avatar in the upper-right portion of the window
#. Click Settings
#. From the left nav, click on Developer Settings
#. Once again from the left nav, click Personal access tokens
#. Click "Fine-grained tokens"
#. Click Generate new token
#. Give the token access to all repositories unless you will only need to work with specific repositories within |morpheus|
#. Click Generate token
#. Copy the access token and save it for the next step when the integration is created

.. TIP:: Fine-grained tokens can be created with an expiration date of up to one year. Should the token expire, any |morpheus| automation, App Blueprints, and Terraform or Kubernetes Spec Templates which are based on code contained in your repositories will no longer work. This could lead to failed provisioning and time spent troubleshooting to isolate the issue until the Github integration is refreshed with a new access token.

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
    - **PASSWORD:** Copy your access token here rather than in the "ACCESS TOKEN" field. See the "Important" box below for additional details
    - **ACCESS TOKEN:** Do not use this field. See the "Important" box below for additional details
    - **KEY PAIR:** (Optional) Select a stored SSH keypair for Github SSH authentication
    - **ENABLE GIT REPOSITORY CACHING:** When unmarked, |morpheus| retrieves code fresh from the repository each time it's invoked. When marked, |morpheus| will use a cached version of the code if it's less than five minutes old. In general, this should be left unmarked unless you are experiencing performance issues related to very large amounts of code being invoked many times during a deployment

#. Click :guilabel:`SAVE CHANGES`

.. IMPORTANT:: Your access token should be pasted into the PASSWORD field and not the ACCESS TOKEN field. If the ACCESS TOKEN field is used, the repository will create successfully and many features will work. However, in Code detail pages (|ProCod| > Selected code detail page), you will not be able to browse files in private Github repositories unless the access token is pasted into the PASSWORD field. New Github integrations should be created by pasting the access token in the PASSWORD field and the ACCESS TOKEN field should be ignored.

.. NOTE:: In certain cases, it can take several seconds for the integration process to complete and the ADD INTEGRATION modal to be dismissed.

Viewing an Integrated Github Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When authentication is successful, click into the new Github integration from the list of available integrations. The Organizations tab will list each organization the Github account is associated with. The Repositories tab lists all public and private repositories which are associated with the account. We can also click in to each repository to view its files and folders, as well as create specific types of automation or Spec Templates from the files directly in this view.

.. image:: /images/integrations_guides/github/github.png
