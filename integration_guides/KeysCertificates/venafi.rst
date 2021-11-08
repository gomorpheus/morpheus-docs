Venafi
------

Overview
^^^^^^^^

Morpheus integrates with Venafi to sync and request SSL certificates

Add Venafi
^^^^^^^^^^

#. Navigate to |AdmInt|
#. Select :guilabel:`+ NEW INTEGRATION`
#. Enter in the following:

    * Name
    * Venafi Host
    * Username
    * Password

#. Click :guilabel:`SAVE CHANGES`

Link Venafi To Cloud
^^^^^^^^^^^^^^^^^^^^

To add Venafi as the `Trust Provider` for a cloud

#. Navigate to ``Infrastructure > Clouds``
#. Select Cloud
#. Select :guilabel:`EDIT`
#. Under `Advanced Options` select the Venafi integration from the `TRUST PROVIDER` dropdown
#. Select :guilabel:`SAVE CHANGE`
