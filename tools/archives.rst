Archives
========

Overview
--------

Archives provides a way to store your files and make them available for download by your Scripts and Users. Archives are organized by buckets. Each bucket has a unique name that is used to identify it in URLs and Scripts.

.. image:: /images/services/archives.gif

.. [caption="Figure 1: ", title="Archives", alt="Archives"]

Storage Provider
----------------

Archive buckets are assigned a Storage Provider (Object Store). This is where the bucket will write its files. A Storage Provider can be configured to use the local appliance file system (Local), an Amazon S3 bucket, etc.

Every archive bucket generates and uses a random File Path to store its files under. This ensures two different archive buckets will not contend for the same backend storage location.

Permissions
-----------

Visibility
^^^^^^^^^^

Visibility determines whether your files are secure or not.

Private
  This secures your files. Only authorized users of the Owner and Tenants account may view the bucket and download its files. This is the default.
Public
  This makes your files available to the public. Anyone, including anonymous users/scripts can download these files without any authentication.

.. WARNING:: Be careful not to store sensitive files in a Public archive.

Users of the Owner account may fully manage the files in a bucket.

Tenants
^^^^^^^

Users of the Owner account may fully manage the files in a bucket. Users of the Tenant account(s) will have read-only access. The may browse and download files in the bucket.

Both Owner and Tenants must have the Services: Archives permission to access a Private bucket. READ level access allows browsing and downloading files in the bucket.

FULL access allows full management of the bucket and its files. This includes modifying files and links, bucket settings and deleting it.

Files
-----

To add a file to a bucket, click on the bucket name, and then click the + ADD FILE button. Once added, click on the file name to access the links, history and script section for the file.

Links
-----

You can create a Link to download a Private file without any authentication. Links may be configured to expire after a period of time.

Scripts
-------

|morpheus| automatically generates syntax for creating a link to a file in your Scripts. When the Script is generated, it will create a temporary link to download the file and return the URL of that link. This link is made available to the public. It is accessible to any user or script that can reach the appliance. Downloading the file only requires knowing the URL, which includes a secret token parameter. You can specify the number of seconds before the link expires. The default value is 1200 (20 minutes).
