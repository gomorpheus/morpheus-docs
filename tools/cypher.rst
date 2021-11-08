.. _Cypher:

Cypher
======

Overview
--------

Cypher at its core is a secure Key/Value store. But what makes cypher useful is the ability to securely store or generate credentials to connect to your instances. Not only are these credentials encrypted but by using a cypher you don't have to burn in connection credentials between instances into your apps.

Cypher keys can be revoked, either through lease timeouts or manually. So even if somebody were to gain access to your keys you could revoke access to the keys and generate new ones for your applications.

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

  * Key lease times are entered in seconds and default to 32 days (2764800 s).

    * Quick Time Reference:
    * Day: 86400
    * Week: 604800
    * Month (30 days): 2592000
    * Year: 31536000


Creating Cypher Keys
--------------------

#. Navigate to Services - Cypher and select "+ ADD KEY"
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

Using Cypher Keys in Scripts
----------------------------

To use a cypher Key in a script, use the following syntax:

``<%=cypher.read('var_name')%>``

Example: ``PASSWORD=<%=cypher.read('secret/myuserpassword')%>``

.. NOTE:: You can reference the original owner of a workflow so that keys can be used in a subtenant.  Example ``PASSWORD=<%=cypher.read('secret/myuserpassword')%>`` could be changed to ``PASSWORD=<%=cypher.read('secret/myuserpassword',true)%>`` within a library or a workflow and the true means OWNER true.  This will keep that key in the master tenants cypher store.
