.. _Code:

Code
====

.. note:: In v5.3.2+, ``provisioning/deployments`` is moved to ``provisioning/code``.

|ProCod| contains the Repositories, Deployments and Code Integrations sections.

.. toggle-header:: :header: Required Role Permissions **Click to Expand/Hide**

    Access and capabilities for the **Code** section is determined by the following role permissions:

    Role: Feature Access: ``Infrastructure: Groups``
      - None: Cannot access Provisioning: Code section
      - Read or Full: Can access Provisioning: Code section

    Role: Feature Access: ``Provisioning: Code Repositories``
      - None: Cannot access Provisioning: Code Repositories
      - List Files: Can browse repo folder and file names, select branch, refresh Repositories. Cannot access/view file contents.
      - Read or Full: Can browse repo folder and file names, select branch, refresh Repositories and access/view file contents.

    Role: Feature Access: ``Provisioning: Code Deployments``
      - None: Cannot access Provisioning: Code Deployments.
      - Read: Can view Code Deployments. Cannot create, delete or edit Code Deployments.
      - Full: Can create, delete and edit Code Deployments.

    Role: Feature Access: ``Provisioning: Code Integrations``
      - None: Cannot access Provisioning: Code Integrations.
      - Read: Can view Code Integrations. Cannot create, delete or edit Code Integrations.
      - Full: Can create, delete and edit Code Integrations

|

.. duplicated
  .. tabs::

     .. tab:: Repositories

        .. include:: repositories.rst

     .. tab:: Deployments

        .. include:: deployments.rst

     .. tab:: Code Integrations

       .. include:: integrations.rst

.. include:: repositories.rst
.. include:: deployments.rst
.. include:: integrations.rst
