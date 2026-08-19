Data Stores
-----------

Data Stores are logical divisions of underlying storage disk. Organizations may use them to divide and track cloud resources by team or department. When integrating certain Cloud types, |morpheus| will onboard existing data stores and administrators can then make them available to Groups or Tenants as needed. Supported datastore types can also be created directly from |morpheus|. At provision time, when applicable based on Cloud and Layout, users can select the data store they wish to provision to.

Here within the Data Store view in the storage section, users can see a list of data stores for each Cloud. In the row for each Cloud, the storage type, associated Cloud, and permissions information are shown.

Create Data Stores
^^^^^^^^^^^^^^^^^^

The available Data Store types depend on the selected Cloud, configured storage integrations, and supported Cluster type. HVM cluster datastores can be created here or from the HVM Cluster's :guilabel:`Datastores` tab.

#. Navigate to :menuselection:`Infrastructure --> Storage --> Data Stores`.
#. Click :guilabel:`Add`.
#. Enter a :guilabel:`Name` and select the :guilabel:`Type`.
#. Select the :guilabel:`Cloud`.
#. For an HVM cluster datastore, select the :guilabel:`Cluster`. This field requires **Infrastructure: Clusters** permission at the **Full** level and only lists Clusters that support the selected Data Store type.
#. Complete the type-specific fields. For example, an HPE Clustered Datastore requires its shared block device; a Datastore Group requires member datastores and placement settings.
#. Configure :guilabel:`Group Access` and :guilabel:`Tenant Permissions` as needed.
#. Save the Data Store.

HVM supports creating these built-in types from this page:

- **Directory Datastore (Local)**
- **NFS Datastore**
- **HPE Clustered Datastore (Shared LUN)**
- **Datastore Group**

Storage plugins can provide additional types. See :doc:`/infrastructure/clusters/hvm/storage_operations` for HVM prerequisites, shared-storage creation, Datastore Groups, and operational guidance.

For Cloud types that do not expose a creatable datastore type, create the datastore in the target platform and refresh the Cloud integration to synchronize it into |morpheus|.

Datastore Details and Explorer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select a Data Store name to open its detail page. The available tabs include:

- **Summary** — Capacity, free space, type, Cloud, and other datastore metadata
- **Volumes** — Virtual disks stored on the datastore and their associated VM where applicable
- **Virtual Machines** — VMs with one or more volumes on the datastore
- **History** — Recorded datastore configuration and lifecycle events
- **Files** — Datastore Explorer for supported HVM shared file datastores

The :guilabel:`Files` tab is currently available for HVM shared, file-based datastores such as NFS and HPE Clustered Datastores (GFS2). Local, block, LUN-per-vDisk, RBD, and cloud-scoped datastores do not expose the file browser. An online HVM Host with access to the datastore is required.

From :guilabel:`Files`, users can search the current directory, navigate into directories, upload and download files, and delete files or directories. Empty directories cannot be created directly, and files cannot be renamed, moved, copied, or edited in place.

Permissions are cumulative:

- **Infrastructure: Storage** set to **Read** and **Infrastructure: Storage Browser** set to **Read** allow file listing and download.
- Both permissions set to **Full** allow upload and deletion. Cluster-scoped access additionally requires **Infrastructure: Clusters** permission, and write operations require ownership of the datastore.

.. warning::

   Deleting a directory recursively removes its contents. Confirm that no VM disk, image, active process, or required datastore artifact is in the selected path. Upload and delete operations are blocked while the datastore is in maintenance mode; browsing and download remain available.

Manage Permissions
^^^^^^^^^^^^^^^^^^

From this view, users can manage permissions for any data store synced from integrated Clouds. This includes setting which Groups have access to the data store, and which Tenants have access. To edit data store permissions:

- Navigate to Infrastructure > Storage > Data Stores
- Click ACTIONS > Edit
- **Groups:** Select "all" Groups or select specific Groups which should have access to the data store
- **Tenants:** Primary Tenant users can opt to make the data store available to all Tenants (public visibility) or to selected Tenants (private visibility with specific Tenants selected). Subtenant users will only be able to make data stores visible to their own Tenant
- **Active:** When marked, the data store is active and available for provisioning
- **Image Target:** Marks the Data Store as a default image-storage target when its Data Store type supports image targets. If no Bucket, File Share, or capable Data Store is selected as the image target, uploaded images are stored locally on the appliance and available storage may be limited. Only one target should be selected for the intended Tenant scope.
- Click :guilabel:`SAVE CHANGES` 
