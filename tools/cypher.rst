.. _Cypher:

Cypher
======

Overview
--------

Cypher at its core is a secure Key/Value store. But what makes Cypher useful is the ability to securely store or generate credentials to connect to your Instances. Not only are these credentials encrypted but by using Cypher you don't have to burn in connection credentials between Instances into your apps.

Cypher keys can be revoked, either through lease timeouts or manually. So, even if somebody were to gain access to your keys you could revoke access to the keys and generate new ones for your applications.

Keys can have different behaviors depending on the specified mountpoint.

Mountpoints
-----------

password
  Generates a secure password of specified character length in the key pattern (or 15) with symbols, numbers, upper case, and lower case letters (i.e. password/15/mypass generates a 15 character password).
tfvars
  This is a module to store a tfvars file for terraform app blueprints.
secret
  This is the standard secret module that stores a key/value in encrypted form.
uuid
  Returns a new UUID by key name when requested and stores the generated UUID by key name for a given lease timeout period.
key
  Generates a Base 64 encoded AES Key of specified bit length in the key pattern (i.e. key/128/mykey generates a 128-bit key)
vault
  Configures an integration between |morpheus| and a Hashicorp Vault server. See below for additional configuration instructions.

  * Key lease times are entered in seconds and default to 32 days (2764800 s).

    * Quick Time Reference:
    * Day: 86400
    * Week: 604800
    * Month (30 days): 2592000
    * Year: 31536000


Creating Cypher Keys
--------------------

#. Navigate to |TooCyp| and select :guilabel:`+ ADD`
#. Configure one of the following types of Keys:

Password
--------

A Cypher password generates a secure password of specified character length in the key pattern (or 15) with symbols, numbers, upper case, and lower case letters (i.e. password/15/mypass generates a 15 character password).

Key
  Pattern "password/character_length/key"

  Example: password/10/mypassword

Value
  Leave the Value filed blank for a password, as it will be generated.

Lease
  Enter lease time in seconds (ex. 604800 for one week)

Save changes and the password will be generated and available for use.

If your user role has Cypher: Decrypt permissions, a "DECRYPT" button will be available in the Cypher section to view the generated password.

To delete the password key, select `Actions > Remove` and confirm.

tfvars
------

A mountpoint to store tfvars files for Terraform App Blueprints.

Key
  Pattern "tfvars/key"

  Example: tfvars/my-aws-account

Value
  The values for your tfvars file to be encrypted

Lease
  Enter lease time in seconds (ex. 604800 for one week)

Click :guilabel:`SAVE CHANGES` and the stored values will be available for use.

.. NOTE:: You may also see Cloud profiles stored at the tfvars mountpoint. They will have a key pattern like: "tfvars/profile/cloud/$cloudCode/variables". Terraform Cloud profiles are created on the Cloud detail page (|InfClo| > selected Cloud) under the Profiles tab. They allow Terraform apps and specs to be provisioned across multiple Clouds that require differed tfvars. See the `Cloud profiles <https://docs.morpheusdata.com/en/latest/infrastructure/clouds/profiles.html>`_ page for more.

Secret
------

A Cypher secret is the standard secret module that stores a key/value in encrypted form.

Key
  Pattern "secret/key"

  * EXAMPLE: secret/mysecret

Value
  Add the secret value to be encrypted

Lease
  Enter lease time in seconds (ex. 604800 for one week)

Save changes and the secret will be encrypted and available for use.

If your |morpheus| user role has Cypher: Decrypt permissions, a "DECRYPT" button will be available in the Cypher section to view the secret.

To delete the secret, select `Actions > Remove` and confirm.

UUID
----

A Cypher UUID Returns a new UUID by key name when requested and stores the generated UUID by key name for a given lease timeout period.

Key
  Pattern "uuid/key"

  * Example: uuid/myuuid

Value
  Leave the Value filed blank for UUID, as it will be generated.

Lease
  Enter lease time in seconds (ex. 604800 for one week)

Save changes and the UUID will be generate and available for use.

If your user role has Cypher: Decrypt permissions, a "DECRYPT" button will be available in the Cypher section to view the generate UUID.

To delete the UUID, select `Actions > Remove` and confirm.

Key
---

A Cypher Key generates a Base 64 encoded AES Key of specified bit length in the key pattern (i.e. key/128/mykey generates a 128-bit key).

Key
  Pattern "key/bit_length/key"

  * Example: key/256/mykey

Value
  Leave the Value filed blank for key, as it will be generated.

Lease
  Enter lease time in seconds (ex. 604800 for one week)

Save changes and the AES Key will be generate and available for use.

If your user role has Cypher: Decrypt permissions, a "DECRYPT" button will be available in the Cypher section to view the generate AES Key.

To delete the UUID, select `Actions > Remove` and confirm.

Vault
-----

Use this mountpoint to store Cypher secrets in a Hashicorp Vault server backend rather than |morpheus|. Additionally, you can call secrets stored in Vault from this Cypher mountpoint even if they are only saved there and not listed in the |morpheus| Cypher UI. This requires installation and configuration of the Hashicorp Vault plugin. See the YouTube video embedded in this section for more information on adding the plugin, configuration, and a demonstration of its capabilities.

.. NOTE:: It's recommended that you use a long-lived token as attempts to call Vault-stored values into Tasks will stop working if the token is no longer good. In such a case you'd have to obtain a new token, delete the Cypher entry with the old token, and create a new one to restore functionality once again. Using a long-lived token will prevent the need to do this often.

Key
  Pattern "vault/<engineMount>/<secretPath>/data/<key>" (ex. vault/KV2/secret/data/morpheus/lab)

Value
  Enter your key/value pair here in valid JSON (ex. {"hello": "world"} )

Lease
  Enter lease time in seconds (ex. 604800 for one week)

Click :guilabel:`SAVE CHANGES`. The example BASH script below onboards the value stored in Vault from the secret/data/morpheus/lab mountpoint:

.. code-block:: bash

  from_vault="<%= cypher.read('vault/KV2/secret/data/morpheus/lab') %>"

  echo $from_vault

.. rst-class:: hidden
  .. raw:: html

      <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
          <iframe src="//www.youtube.com/embed/9OSXXJi15Rw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
      </div>

  |

Editing Cypher Keys
-------------------

Cypher key types which accept user-entered values (not generated values) are editable. To edit, click the "ACTIONS" button at the end of the row for the appropriate Cypher key and then click "Edit." Edit the values and click :guilabel:`SAVE CHANGES`.

Using Cypher Keys in Scripts
----------------------------

To use a Cypher key in a script, use the following syntax:

``<%=cypher.read('var_name')%>``

Example: ``PASSWORD=<%=cypher.read('secret/myuserpassword')%>``

Cypher also includes an option to read a value from the ``password/*`` mountpoint or create one if it doesn't already exist. Use the following syntax:

``<%=cypher.readPassword('var_name')%>``

Example: ``PASSWORD=<%=cypher.readPassword('myuserpassword')%>```

It should be noted that when Cypher keys are created using the ``readPassword`` function, the subsequent reads can only come from the same user. If another |morpheus| user attempts to run the automation script containing the ``readPassword`` call, the secret value will not be read and it's very likely the script will fail. For Tasks that need to be run by multiple users, use a pre-existing Cypher key and reference it back in the script using ``read`` rather than ``readPassword``.

.. rst-class:: hidden
  .. NOTE:: You can reference the original owner of a workflow so that keys can be used in a subtenant.  Example ``PASSWORD=<%=cypher.read('secret/myuserpassword')%>`` could be changed to ``PASSWORD=<%=cypher.read('secret/myuserpassword',true)%>`` within a library or a workflow and the true means OWNER true.  This will keep that key in the master tenants cypher store.
