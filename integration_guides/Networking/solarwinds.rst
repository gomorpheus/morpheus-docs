SolarWinds IPAM
---------------

Features
^^^^^^^^

- Automate static ip assignment across environments using Solarwinds IPAM
- Network Pool sync. Network Pools can be set on networks in |morpheus| for automated IP allocation and record creation.
- Optional Network Pool allocation and record sync. ``Inventory Existing`` option syncs all individual ip's records and corresponding status. Inventory is not required for provisioning.
- Grid and list displays with IP record overlays and color coding for static, available, reserved and transient status.
- Manual IP Host record creation from Network Pool detail pages.


Adding SolarWinds to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Click :guilabel:`+ ADD`
#. Select `SolarWinds`
#. Enter in the following information

    Name
      Name of the SolarWinds Integration in |morpheus|
    Enabled
      Uncheck to disable sync with the SolarWinds endpoint
    URL
      URL of the SolarWinds server, ex: ``http://10.30.20.10``
    Username
      Username of SolarWinds API User. API and root level propagating read access required, read/write access required for target Networks and Domains.
    Password
      SolarWinds User password

#. Click :guilabel:`SAVE CHANGES`
