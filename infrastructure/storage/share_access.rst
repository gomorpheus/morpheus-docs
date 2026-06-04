Share Access Control
--------------------

Overview
^^^^^^^^

Share Access controls allow administrators to manage host-level access rules for File Shares associated with storage servers. Access rules define which hosts or IP addresses can connect to a file share and what level of access they are granted (e.g., read-only, read/write).

Share Access rules are specific to File Shares that are backed by a Storage Server integration (such as Dell EMC Isilon or other NAS platforms). The available access rule options are determined by the storage server type.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Storage`` role permission at **Full** level is required to create, edit, or delete access rules.
- ``Infrastructure: Storage`` role permission at **Read** level allows viewing access rules only.

Viewing Share Access Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Storage``
#. Select the **FILE SHARES** tab
#. Click the name of the File Share to view its detail page
#. Select the **ACCESS** tab

The Access tab displays all configured access rules for the file share, including the rule name, access level, and associated host or IP address.

Adding an Access Rule
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Storage``
#. Select the **FILE SHARES** tab
#. Click the name of the File Share
#. Select the **ACCESS** tab
#. Click :guilabel:`+ ADD`
#. Fill in the required fields:

   NAME
     A descriptive name for the access rule.
   HOST / IP
     The host name or IP address to grant access to. The available fields depend on the storage server type.
   ACCESS LEVEL
     The level of access to grant to the host. Options depend on the storage provider and may include:

     - **Read Only** — The host can read data from the share but cannot write.
     - **Read/Write** — The host can both read and write data to the share.
     - **Root** — The host has full root-level access (where supported by the provider).

   .. NOTE:: Additional configuration fields may appear depending on the underlying storage server type. These are defined by the provider's share access option types.

#. Click :guilabel:`SAVE CHANGES`

Editing an Access Rule
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the File Share detail page
#. Select the **ACCESS** tab
#. Click the edit icon (pencil) next to the access rule
#. Modify the desired fields
#. Click :guilabel:`SAVE CHANGES`

Deleting an Access Rule
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the File Share detail page
#. Select the **ACCESS** tab
#. Click the delete icon (trash) next to the access rule
#. Confirm the deletion

.. WARNING:: Removing an access rule immediately revokes the host's ability to connect to the file share. Ensure no active workloads depend on the access before removing.
