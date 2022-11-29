Data Encryption
---------------

By default, Morpheus encrypts sensitive data in the Database using AES encryption mode with GCM. Passwords and other strings in |morpheus| Appliance configuration files such as ``morpheus-secrets.json`` and ``morpheus.rb`` are in plain text as they are only accessible by root.

Passwords and other strings in |morpheus| Appliance configuration files can be set to an encrypted string using the |morpheus| crypto utility to generate ENC strings and then using ``ENC(string)`` as the value in the configuration file.

Additionally a custom Encryption Key Suffix can be set in the morpheus.rb configuration file. This suffix will be combined with a system string to generate a SHA-256 hash, which is used to generate the AES encryption key.

Generate ENC Strings for morpheus-secrets.json
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System generated passwords are set in ``/etc/morpheus/morpheus-secrets.json``. These entries can be updated to ENC strings with the following steps:

#. On the |morpheus| appliance, run ``morpheus-ctl get-crypto-string migrate`` which will output ENC() strings for the passwords in morpheus-secrets.json
#. Update the desired password strings in the ``morpheus-secrets.json`` config file with the matching ENC() string.
#. Save ``morpheus-secrets.json``
#. Run ``morpheus-ctl reconfigure``

Generate ENC Strings for custom morpheus.rb entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENC() strings can be generated for sensitive data set in morpheus.rb, such as the password to an external service.

To generate ENC(0) strings for morpheus.rb entries:

#. On the |morpheus| appliance, run ``morpheus-ctl get-crypto-string string $clear_text '$suffix'`` which will output strings for the passwords in morpheus-secrets.json

   - Replace ``$clear_text`` with the string to be encrypted
   - If a suffix is defined in morpheus.rb (as described in the next section), replace ``$suffix`` with your suffix.

   .. note:: It is advisable to disable bash history logging by running ``unset HISTFILE`` before running the morphesu-ctl get-crypto-string command and then ``set HISTFILE=$HOME/.bash_history`` to reenable.

#. Update the desired password strings in the ``morpheus.rb`` config file with the matching string output, using ``ENC($output)`` format

      - Example: ``mysql['morpheus_password'] = 'ENC($ZI5DnaO0quhxKe$kDFD+U2ZeJUuYiNC$F1+czPNyo+3lAdq7V0gcrWwHnkINYqr13cUGrDVyog==)'``

#. Save ``morpheus.rb``
#. Run ``morpheus-ctl reconfigure``

Encrypted Key Suffix
^^^^^^^^^^^^^^^^^^^^

A custom Encryption Key Suffix can be set in the morpheus.rb configuration file. This suffix will be combined with a system string to generate a SHA-256 Hash, which is used in the generation of the system AES encryption key.

.. danger:: Setting a custom Encryption Key Suffix affects all data encrypted by |morpheus|, including database and cypher data. Encryption Key Suffix is required in the event data needs to be migrated or recovered. Once the Encryption Key Suffix is set, data cannot be recovered without it. Store any Encryption Key Suffix externally where it can be referenced for future scenarios.

.. important:: The Encryption Key Suffix cannot be changed or removed after being set. Changing or removing an existing Encryption Key Suffix will prevent data access. If an existing suffix is altered in the morpheus.rb file, it must be restore to its original value.

#. Add ``app['encrypted_key_suffix'] = 'key'`` to ``/etc/morpheus/morpheus.rb``, replacing ``$suffix`` with your suffix.

   .. danger:: Once an Encryption Key Suffix is set and applied via reconfigure, it cannot be altered or removed and data cannot be migrated or recovered without it.

#. Run ``morpheus-ctl reconfigure``

   - Reconfigure will generate a new encryption key using the suffix and set (ENC) values for the service password in application.yml
