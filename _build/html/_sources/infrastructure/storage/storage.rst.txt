Storage
-------

Overview
^^^^^^^^

The default Storage path for Virtual Images, Backups, Deployment Archives, Archive Server, and Archived Snapshots is `var/opt/morpheus`. Additional Storage providers can be added and mapped for these targets in the `Infrastructure -> Storage` section. Adding Storage providers are also required for scenarios like AWS migrations.

=== Supported Storage Provider Types

* Local
* NFSv3
* CIFS (Samba Windows File Sharing)
* Amazon S3
* Azure
* Rackspace CDN
* OpenStack Swift

=== To View Storage:

. Select the Infrastructure link in the navigation bar.
. Select the Storage link in the sub navigation bar.

=== Add Storage Provider

To Add Storage Provider:

. Select the Infrastructure link in the navigation bar.
. Select the Storage link in the sub navigation bar.
. Click the Add Storage Provider button.
. From the New Storage Provider Wizard input the following:
Name::  Name of the storage provider.
Provider Type:: Select from:
* Local Storage
** Storage Path
* NFSv3
** Host
** Export Folder
* CIFS (Samba Windows File Sharing)
** Host
** Username
** Password
** Share Path
* Amazon S3
** Access Key
** Secret Key
** Bucket Name
** Endpoint URL (Optional endpoint URL if pointing to an object store other than amazon that mimics the Amazon S3 APIs.)
* Azure
** Storage Account
** Storage Key
** Share Name
* Rackspace CDN
** Username
** API Key
** Region
** Bucket Name
* OpenStack Swift
** Username
** API Key
** Region
** Bucket Name
** Identity URL
Targets::
* Default Backup Target
** Update existing backups
* Archive Snapshots
* Default Deployment Archive Target
* Default Virtual Image Store

. Click the Save Changes button to save.

=== Edit Storage Provider

To Edit Storage Provider:

. Select the Infrastructure link in the navigation bar.
. Select the Storage link in the sub navigation bar.
. Click the Edit pencil icon on row of the Storage Provider to edit.
. Edit required information.
. Click the Save Changes button to save.


=== Delete Storage Provider

To Delete Storage Provider:

. Select the Infrastructure link in the navigation bar.
. Select the Storage link in the sub navigation bar.
. Click the Delete icon on row of the Storage Provider to delete.
