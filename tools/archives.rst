Archives
========

Overview
--------

Archives provides a way to store your files and make them available for download by your scripts and Users. Archives are organized by buckets and can be tied to any existing Bucket or File Share that may be currently integrated (for more on integrating new storage targets, see storage documentation). Thus, storage buckets in public clouds, on networked storage, or even on the appliance itself may be used to host files.

Archives List Page
------------------

To view or create Archives, navigate to |TooArc|. At the Archives list page is a list of all currently-configured Archives. From the list view, the following details about each Archive are shown:

- **NAME:** The name for the Archive in |morpheus|
- **BUCKET:** The integrated bucket or file share where files in this Archive are stored
- **# Files:** The number of files in the Archive
- **SIZE:** The total size of all files in the Archive
- **TENANTS:** When Archive visibility is set to Private, only the Tenants listed here have access to the Archive
- **VISIBILITY:** Public or Private, public Archives are available in all Tenants
- **PUBLIC URL:** Indicates whether |morpheus| is automatically generating a public download URL for files in this Archive
- **ACTIONS:** Within the ACTIONS menu users may download a ZIP folder containing all files in the Archive, edit the Archive, or remove it

.. rst-class:: hidden
  .. image:: /images/tools/archives/archivelist.png

Adding an Archive
-----------------

To add a new Archive, click :guilabel:`+ ADD` from the Archives list page. Configure the following:

- **NAME:** A friendly name for the Archive in |morpheus|
- **DESCRIPTION:** An optional description for the Archive
- **BUCKET:** Select an existing bucket or file share to store files in for this Archive. To integrate a new bucket or file share to use for an Archive, navigate to |InfSto|
- **VISIBILITY:** Public or Private, public Archives are available in all Tenants
- **TENANTS:** When Archive visibility is set to Private, only the Tenants selected will have access to the Archive
- **PUBLIC URL:** When marked, |morpheus| will create a public download URL for all files in the Archive

.. WARNING:: Be sure that no sensitive data will be stored in the Archive if it will be configured to generate public URLs. Anyone with the public URL will be able to download the file without authentication.

Once done, click :guilabel:`SAVE CHANGES`

Archive Detail Page
-------------------

The Archive detail contains information about the Archive configuration as well as a list of files currently stored in the Archive. The Archive detail is accessed by navigating to the Archives list page (|TooArc|) and selecting an existing Archive. As on the Archives List Page, users can download a ZIP folder containing all files in the Archive and edit the Archive from the ACTIONS menu.

To delete the Archive, click :guilabel:`DELETE`. New files are added by clicking :guilabel:`+ ADD`. When adding a new file, users may browse the file system on the local computer to select a file.

From the files list, download or delete individual files by clicking on the appropriate selection from the ACTIONS menu.

.. rst-class:: hidden
  .. image:: /images/tools/archives/archivedetail.png

File Detail Page
----------------

The File Detail Page contains details about the file itself as well as private and public (if available) URLs. In the lower section are three tabs. The Links tab contains any download links which have been generated (both active and expired). The History tab contains historical information about the file including creation and deletion of download links and download events. The scripts tab contains a guide for getting started using Archive-stored files in scripts.

.. rst-class:: hidden
  .. image:: /images/tools/archives/filedetail.png
