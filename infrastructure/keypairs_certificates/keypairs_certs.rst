Trust
=====

The Trust section is where credentials, SSH keypairs, and SSL certificates are stored. In addition, related integrations to outside technologies can be made in this section as well. Integration types include Venafi for SSL certificates and |morpheus| Cypher for externalized credential storage. Continue onto the next section for more on standing up an external Cypher credential store.

Credentials
-----------

The credentials section allows for various credential types to be securely stored and called back when necessary, such as when creating new integrations with Cloud accounts or other outside technologies. Credentials can also be used to populate REST-based Option Lists sourced from data behind an authentication wall, as well as to run automation Tasks on remote targets that require authentication. Credentials can be securely stored internally on the appliance or stored in an external Cypher integration, more information about setting up and integrating with an external Cypher store are in the next section. The following credential pair types are currently supported:

- Access Key and Secret Key
- Client ID and Secret
- Email and Private Key
- Tenant, Username, and Keypair
- Username and API Key
- Username and Keypair
- Username and Password
- Username, Password, and Keypair

To create a new credential set, click :guilabel:`+ ADD` and then select the type of credential set you'd like to store. Complete the following:

- **CREDENTIAL STORE:** Select "Internal" or an integrated external Cypher store (if any). See the next section for instructions on standing up and integrating with an external Cypher store
- **NAME:** A name for the credential set in |morpheus|
- **DESCRIPTION:** An optional description for the credential set
- **ENABLED:** If checked, the credential set will be available for use
- **CREDENTIAL VALUES:** Depending on the credential pair type selected (listed above), the remaining fields will be specific to the chosen type

.. image:: /images/infrastructure/trust/addCredentials.png
  :width: 50%

Finally, click :guilabel:`ADD CREDENTIALS`. Once saved, the credential set will be available for selection where appropriate in |morpheus| UI. In the screenshot below, I'm integrating a new VMware Cloud. In the credentials section, I have the following options: Creating (and using) a new Username and Password credential set (which includes the option to save internally or to an external Cypher store), choosing a previously-stored credential set, or simply entering my credentials locally and not saving them for reuse.

.. image:: /images/infrastructure/trust/useCredentials.png
  :width: 50%

Installing and Integrating an External Cypher Appliance
-------------------------------------------------------

The external Cypher appliance runs on a small separate VM and supports a variety of base OS distributions. Credentials are securely passed to the external appliance and can be retrieved and consumed in specific places within |morpheus| UI. The download URL for the installer can be retrieved from |morpheus| `Hub <https://morpheushub.com/>`_, replace the placeholder URL in the instructions below with the correct URL for the latest version of the Cypher appliance.

Begin by provisioning and updating the VM for the Cypher appliance. Then, download the installer. The following steps go through the installation process on Ubuntu but, as mentioned in the previous paragraph, many popular distributions are supported.

.. code-block:: bash

  # An example URL is shown below, find the URL for the latest version and for the correct distro at |morpheus| Hub
  wget https://downloads.morpheusdata.com/path/to/morpheus-cypher_$version_amd64.deb

Next, install and reconfigure the package.

.. code-block:: bash

  sudo dpkg -i morpheus-cypher_$version_amd64.deb
  sudo morpheus-cypher-ctl reconfigure

After the installation and reconfigure is complete, we need to record the generated API key so we can integrate the external Cypher store with |morpheus| in a later step. We can get this from the logs with the following command:

.. code-block:: bash

  sudo morpheus-cypher-ctl tail

  ==> /var/log/morpheus-cypher/cypher/current <==
  2022-02-02_15:22:27.84848 |  \/  (_) ___ _ __ ___  _ __   __ _ _   _| |_
  2022-02-02_15:22:27.84848 | |\/| | |/ __| '__/ _ \| '_ \ / _` | | | | __|
  2022-02-02_15:22:27.84848 | |  | | | (__| | | (_) | | | | (_| | |_| | |_
  2022-02-02_15:22:27.84848 |_|  |_|_|\___|_|  \___/|_| |_|\__,_|\__,_|\__|
  2022-02-02_15:22:27.84849   Micronaut (v3.2.2)
  2022-02-02_15:22:27.84849
  2022-02-02_15:22:28.09130 15:22:28.087 [main] INFO  i.m.context.env.DefaultEnvironment - Established active environments: [ec2, cloud]
  2022-02-02_15:22:30.15129 15:22:30.151 [main] INFO  c.m.cypher.service.CypherService - Root Data: null
  2022-02-02_15:22:30.83499 15:22:30.834 [main] INFO  c.m.cypher.service.CypherService - Initialized Root Token: c90xxxx00000xxxxxx000000xxxxx000 ... Write this down as it will only display once
  2022-02-02_15:22:32.01282 15:22:32.012 [main] INFO  io.micronaut.runtime.Micronaut - Startup completed in 4749ms. Server Running: http://localhost:8080

.. IMPORTANT:: The API key is only shown once when the appliance is first installed. Securely store this API key for later reference or you will be unable to integrate this Cypher appliance with any other |morpheus| appliances.

This completes the installation process, move to |morpheus| UI to integrate the remote Cypher store with |morpheus|. Cypher integrations are added in |InfTruInt|. Click :guilabel:`+ ADD` and then click Cypher. Configure the following:

- **NAME:** A name for the Cypher integration in |morpheus|
- **ENABLED:** When checked, this Cypher integration is available for storing and retriving credentials
- **API HOST:** The URL where your Cypher appliance can be reached (ex. https://x.x.x.x/)
- **API KEY:** The API Key we retrieved and saved in the previous step

.. image:: /images/infrastructure/trust/addCypherInt.png
  :width: 50%

Click :guilabel:`SAVE CHANGES` to save the new integration. Refer to the "Credentials" section above for details on storing new credential sets using the external appliance and how they can be called back in various places throughout the UI.

Key Pairs
---------

The key pairs section enables the following actions: Add and Delete key pairs. Key pairs are commonly used by |morpheus| for accessing instances via SSH. |morpheus| stores key pairs to simplify administration and access across both private and public clouds.

|morpheus| only accepts key pairs in PEM format (for example, a private key beginning with ``-----BEGIN RSA PRIVATE KEY-----``). If you have a key in another format, such as OpenSSH, convert the key:

.. code-block:: bash

  #No passphrase
  ssh-keygen -m pem -f /path/to/key

  #With passphrase
  ssh-keygen -p -P "old passphrase" -N "new passphrase" -m pem -f path/to/key

Add Key Pair
------------

To Add Key Pair:

#. Navigate to Infrastructure > Keys & Certs
#. On the Key Pairs tab, click :guilabel:`+ ADD`
#. From the Add Key Pair wizard input the following as needed:

   * Name
   * Public Key
   * Private Key
   * Passphrase

   .. NOTE:: Certain features do not require storage of the private key.

Delete Key Pair
---------------

To Delete Key Pair:

#. Navigate to Infrastructure > Keys & Certs
#. On the Key Pairs tab, select the trash can icon at the end of any row
#. Acknowledge that you wish to delete the selected key pair

SSL Certificates
----------------

SSL certificates authenticate the identity of web servers and encrypt the data being transmitted. |morpheus| stores SSL certificates to simplify administration and application of SSL certificates to |morpheus|-managed resources.

Add SSL Certificate
-------------------

#. Navigate to Infrastructure > Keys & Certs
#. On the SSL Certificates tab, click :guilabel:`+ ADD`
#. From the Add SSL Certificate wizard input the following as needed:

   * Name
   * Domain Name
   * Key File
   * Cert File
   * Root Cert

Delete SSL Certificate
----------------------

To Delete SSL Certificate:

#. Navigate to Infrastructure > Keys & Certs
#. On the SSL Certificates tab, select the trash can icon at the end of any row
#. Acknowledge that you wish to delete the selected SSL Certificate

Trust Integrations
------------------

Some organizations may use outside technologies to manage their key and certificates. |morpheus| allows users to integrate with Venafi for trust management. Trust management integrations can be managed from the Integrations tab on the Infrastructure > Keys & Certs page. Additionally, they can be managed in |AdmInt|.

Currently, |morpheus| supports trust integration Venafi. For more detailed information on integrating Venafi with |morpheus|, take a look at our `integration guide <https://docs.morpheusdata.com/en/latest/integration_guides/KeysCertificates/keysandcerts.html>`_.
