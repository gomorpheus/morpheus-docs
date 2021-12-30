Backups
=======

In the `Backups > Backups` section, currently configured Backups can be viewed and managed, and new Instance, Host and Provider backups be configured.

.. NOTE:: Role permissions for Backups determine which backups will be accessible per user.

Manage an existing Backup
-------------------------

#. Select the Backups link in the navigation bar.
#. Select the Backups link in the sub navigation bar.
#. Select the name of the Backup to view the Backups detail page.


Create Instance Backup
----------------------

To create instance backup

#. Select the Backups link in the navigation bar.
#. Select the Backups link in the sub navigation bar.
#. Click the Add Backup button.
#. From the Create Backup Wizard select the radio button Instance, then click Next.
#. Input the following:

   Name
    Name of the backup job being created.
   Instance
    Select an instance to backup from the dropdown.

#. Click Next.
#. Depending on the instance type selected in the previous step, enter additional details such as:

   - Database Name
   - Username
   - Password
   - Container
   - etc..

#. Click the Next button.
#. Schedule the backup Days, Time, Storage Provider & Retention Count.
#. Click Complete to save.

.. NOTE:: On VMware Cloud types, |morpheus| will merge and consolidate the snapshots held against a VM before exporting the OVF to the storage location or share. This is so |morpheus| has a full and consistent copy of the VM state.

..
  Create Server Backup
  --------------------

  To create a server backup:

  #. Select the Backups link in the navigation bar.
  #. Select the Backups link in the sub navigation bar.
  #. Click Add Backup.
  #. From the Create Backup Wizard select the radio button Server, then click Next.
  #. Input the following:

     - Name of the backup job being created
     - Server
     - Type of backup you wish to create.

       - File
       - Directory
       - Mongo
       - MySQL
       - Postgres

  #. Click Next. Different options are presented based upon the type of backup being created.

     - File/Directory - input path for the backup.
     - Mongo/MySQL/Postgres - input 'Database IP Address/URL', 'Database Port', 'Database Username', 'Database Password', 'Database Name', and the option to select 'All Databases'.

  #. Click Next.
  #. Schedule the backup Days, Time, Storage Provider & Retention Count.
  #. Click Complete to save.
