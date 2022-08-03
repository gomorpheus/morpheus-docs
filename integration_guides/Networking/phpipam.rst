phpIPAM
-------

Configuration
^^^^^^^^^^^^^^

#. Within phpIPAM dashboard, enable api in Administration > phpIPAM settings > feature settings.  Toggle API switch to ``on`` and save.
#. Go to Admin > API > create API key.
#. Create unique App ID.
#. Enable ``read/write/admin`` access under **App Permissions**.
#.  Under **App Security** select ``SSL with User Token``.

Add phpIPAM integration to |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select :guilabel:`+ ADD` > IPAM > phpIPAM
#. Enter the following:

   * Name
   * URL
      Add ``/api/`` to end of URL ex. ``http://10.30.20.196/api/``
   * App ID
      From phpIPAM API Key
   * Username
   * Password
   * Enable or Disable SSL SNI Verification
   * Enter Network Filter

#. Select :guilabel:`SAVE IPAM INTEGRATION`
