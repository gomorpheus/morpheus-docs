Data Encryption
---------------

By default, Morpheus encrypts sensitive data passwords and other strings in |morpheus| Appliance configuration files such as ``morpheus-secrets.json`` and ``morpheus.rb`` are in plain text as they are only accessible by root. Passwords can be set to an encrypted string using the |morpheus| crypto service to generate ENC strings and then using ``ENC(string)`` as the value in the configuration file.

Encrypted Key Suffix 
^^^^^^^^^^^^^^^^^^^^

A custom encryption key suffix can be added for use when generating ENC strings. 

#. Add ``app['encrypted_key_suffix'] = '$suffix'`` to ``/etc/morpheus/morpheus.rb``, replacing ``$suffix`` with your suffix. 
#. Run ``morpheus-ctl reconfigure 


Generate ENC Strings for morpheus-secrets.json
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System generated passwords are set in ``morpheus-secrets.json``. These entries can be updated to ENC strings with the following steps:

#. One the |morpheus| appliance, run ``morpheus-ctl get-crypto-string migrate`` which will 
