Importing HPE ProLiant Bare Metal Servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

About this task
```````````````

Perform the following procedure to import HPE ProLiant Bare Metal Servers into |morpheus|.

Procedure
`````````

#. Navigate to :menuselection:`Infrastructure --> Compute`, then select the **Bare Metal** tab.
#. Click the :guilabel:`+ ADD` button and select **HPE Bare Metal Import**.
#. Select the target HPE BMaaS Cloud from the drop-down list.
#. Configure the import settings:

   - **iLO IP Range** - Specify the iLO IP address range to scan for HPE ProLiant servers
   - **Credentials** - Provide the iLO credentials for server discovery

#. Click :guilabel:`Import` to begin the server discovery process.

After successful import, the discovered HPE ProLiant servers appear in the Bare Metal tab and are available for provisioning through |morpheus|.
