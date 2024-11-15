Data Stores
-----------

Data Stores are logical divisions of underlying storage disk. Organizations may use them to divide and track cloud resources by team or department. When integrating certain Cloud types, |morpheus| will onboard all existing data stores and administrators can then make them available to Groups as needed. At provision time, when applicable based on Cloud and Layout, users can select the datastore they wish to provision to.

Here within the Data Store view in the storage section, users can see a list of data stores for each Cloud. In the row for each Cloud, the storage type, associated Cloud, and permissions information are shown.

Create Data Stores
^^^^^^^^^^^^^^^^^^

To a limited extent, data stores can be created from this view. Currently, data store creation is restricted to VMware data store creation on 3Par volumes. In order to create such a data store you would need to first have an integrated 3Par server. See the section on storage servers for more information on setting up this integration.

.. NOTE:: For all other data store types, create the needed data store within the target Cloud and |morpheus| will automatically sync in the data store on the next Cloud sync. You can force a Cloud sync from the Cloud Detail Page (Infrastructure > Clouds > Selected Cloud > Refresh Menu > Short).

- Navigate to Infrastructure > Storage > Data Stores
- Click :guilabel:`+ADD`
- Enter a Name, select a VMware Cloud, select a 3Par Volume, and select a Host Group
- Manage permissions in the Group Access and Tenant Permissions sections, if needed
- Click :guilabel:`SAVE CHANGES`

Manage Permissions
^^^^^^^^^^^^^^^^^^

From this view, users can manage permissions for any data store synced from integrated Clouds. This includes setting which Groups have access to the data store. To edit data store permissions:

- Navigate to Infrastructure > Storage > Data Stores
- Click ACTIONS > Edit
- **Groups:** Select "all" Groups or select specific Groups which should have access to the data store
- **Active:** When marked, the data store is active and available for provisioning
- Click :guilabel:`SAVE CHANGES`
