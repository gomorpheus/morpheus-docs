CyberArk Conjur
---------------

|morpheus| supports integration with CyberArk Conjur for stored credential sets as well utilization of Conjur-stored secret values via |morpheus| Cypher service. This works identically to built-in credential storage and built-in Cypher functionality with the exception that your Conjur server is the storage backend rather than the |morpheus| appliance itself. In some cases, this may help to consolidate secret management into one central place or it even may be a requirement to satisfy internal security policies at some organizations.

CyberArk Conjur integration is not included with |morpheus| out of the box. It is developed as an official plugin and may be applied to any |morpheus| appliance that needs it. See the |morpheus| plugin repository website for access to the latest version of the plugin.

Applying the Plugin
^^^^^^^^^^^^^^^^^^^

The latest version of the CyberArk Conjur plugin is available at the |morpheus| `plugin share site <https://share.morpheusdata.com/>`_. Select the pane for the correct plugin and click the :guilabel:`DOWNLOAD` button. The plugin JAR file will be downloaded to the local computer you're working on.

.. image:: /images/integration_guides/conjur/share.png

With the plugin downloaded, head back to |morpheus| to apply the plugin to your appliance. Plugins are added by navigating to |AdmIntPlu| and clicking :guilabel:`ADD`. Drop the plugin JAR file onto the target and click :guilabel:`UPLOAD`. It may take a few moments for the plugin to be applied successfully and for the modal to be dismissed after clicking the upload button.

.. image:: /images/integration_guides/conjur/addPlugin.png

Once the plugin is added, we configure the connection details here. Edit the new Conjur plugin by clicking the pencil (|pencil|) icon from its row in the list. Configure the following fields:

- **NAME:** A friendly name for the new integration to identify it within |morpheus|
- **ENABLED:** Mark the box to make this integration active and available
- **CONJUR API URL:** The full URL for the Conjur server, usually listening on port 8443
- **CONJUR USERNAME:** The Conjur user account you wish to authenticate with. This user should have read, write, and execute access to the variables configured within the Conjur policy
- **CONJUR USERNAME API KEY:** The API key for user entered in the prior field
- **CONJUR ORGANIZATION:** The Conjur account in which the user and variables reside
- **CLEAR SECRET ON DELETION:** When marked, secret values will be cleared when deleted from |morpheus|

.. IMPORTANT:: Variables are predefined by Conjur policies. This integration does not allow users to create variables but does allow you to read and update their values. If the plugin is configured to clear secrets that are deleted from |morpheus|, the variable value is updated with an empty value as there is no concept of fully deleting secrets in the Conjur API. If the plugin is configured not to clear secrets on deletion, the secret object is deleted from |morpheus| without altering it on the Conjur backend.

By applying and configuring the plugin, the appliance now has the Conjur/Cypher integration available. If you don't intend to use the credential store integration, you can stop here and look ahead to the feature demonstration further ahead in this guide. If you do intend to use the credential store integration as well, there's one additional configuration step to take in the next section.

Adding A Conjur Trust Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use Conjur with |morpheus| credentials, we must also add a Conjur-type integration in |InfTruInt|. By applying the plugin in the previous step, we now have the ability to add this type of integration. From the Trust integrations list page, click :guilabel:`+ ADD` and select "Conjur." It's important to note that you ***do not*** need to again configure the API URL and Conjur login credentials as we just did in the previous step. You may configure them here if you wish, such as if you were making multiple integrations with multiple Conjur appliances, but if you're simply integrating with the same appliance and user account, this is unnecessary. Simply give the new Trust integration a friendly name for reference in |morpheus| and indicate the desired mount point for secrets you wish to consume as done in the screenshot below.

.. NOTE:: In many cases, you don't have to configure the connection details when adding a Conjur Trust integration. See the paragraph above.

.. image:: /images/integration_guides/conjur/addTrustInt.png

Conjur and Credential Stores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With configurations completed, we can take a look at how |morpheus| is able to interface with Conjur as a credential store. As mentioned at the beginning of this guide, variables are created by Conjur policies and not by |morpheus|. We can reference existing variables and update the secret values stored within.

As an example, there is a variable named ``BotApp/secretVar`` in the target Conjur appliance. When configuring the Trust integration (in the prior section), the ``BotApp/`` mount point was referenced (see the screenshot in the last section). When creating stored credential sets in |morpheus| against this Conjur credential store, reference the rest of the variable path as the NAME value on the credential set. In this case, the credential set will be named ``secretVar`` to complete the ``BotApp/secretVar`` path as shown in the screenshot below. Be sure to also select Conjur as the CREDENTIAL STORE value rather than the default "Internal."

.. image:: /images/integration_guides/conjur/credentials.png

After saving and going back to the Conjur appliance, the value stored at the referenced variable has been updated. This credential set is also available for use anywhere |morpheus| allows users to utilize them, such as when integrating new Clouds, authenticating REST calls to populate Option Lists, and many other places.

Conjur and Cypher
^^^^^^^^^^^^^^^^^

In addition to stored credential sets, the CyberArk Conjur plugin also enables integration with |morpheus| Cypher. Just as calls can be made to internally-stored secret values with Cypher, Conjur variable endpoints may be referenced to onboard secret strings into automation Tasks.

In the screenshot below, see a simple shell script Task which echoes out a secret value stored in Conjur. As you can see, the ``conjur/`` mount point is referenced along with the rest of the path to the variable which should be accessed. After executing the Task, we can check the execution history and see that the Conjur-stored value is indeed echoed back out.

.. image:: /images/integration_guides/conjur/cypherTask.png

If desired, the value stored in Conjur could also be updated through the |morpheus| Cypher UI. Navigate to |TooCyp| and click :guilabel:`+ ADD`. Note the ``conjur`` mount point is included in the example list of available mount points shown in the modal. By creating a new Cypher entry at the ``conjur`` mount point which references an existing Conjur variable path, the value in Conjur can be overwritten. If you've configured the plugin to clear secrets on deletion, you can also update the stored value with an empty string when you delete the Cypher object in |morpheus|. For our example case, we could update the value in Conjur by creating a Cypher entry at the mount point ``conjur/BotApp/secretVar``.

.. image:: /images/integration_guides/conjur/cypher.png
