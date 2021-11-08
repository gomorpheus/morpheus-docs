Git
---

Authentication
^^^^^^^^^^^^^^

Add a private Github or Git repository. Authentication can be handled by supplying any one of the following:

- Username and password

- Access token

- Key pair

.. image:: /images/integration_guides/deployments/addgitintegration.png
  :width: 80%
  :alt: The add github integration modal
  :align: center

.. NOTE:: Git and Github integrations can be authenticated over HTTPS with a username and password or with an access token. They are authenticated over SSH by providing a key pair. In previous versions of |morpheus|, Git (not Github) integrations could only be authenticated over SSH.

Key pairs are stored in Morpheus and selected from a dropdown menu when needed. To add a key pair to Morpheus:

#. Generate an SSH key pair, or use an existing SSH key pair.
#. Navigate to ``Infrastructure > Keys & Certs``
#. Select :guilabel:`+ ADD`
#. Enter both the Public and Private keys
#. Click :guilabel:`SAVE CHANGES`
