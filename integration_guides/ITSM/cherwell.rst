Cherwell
---------

Add Cherwell Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Administration -> Integrations``
#. Select ``+ NEW INTEGRATION``
#. Select ``Cherwell`` from the dropdown.
#. Add the following:

    NAME
     Name of the Integration in Morpheus.
    ENABLE
     Leave checked to enable the Integration.
    HOST
     Url of the Cherwell Instance
    USER
     Enter in username
    PASSWORD
     Above Cherwell user's password
    CLIENT KEY
     Provide your Cherwell client key
    CREATED BY USER
     This is the full name of a user in the Cherwell system. When a new change management record is created in the Cherwell system, this user will be added to the record as the user that created it.
    START DAYS FROM NOW
     Number of days from now to set proposed start date
    END DAYS FROM NOW
     Number of days from now to set proposed end date
    CUSTOM MAPPING
     This is an optional json object that allows the custom setting of the Cherwell fields on the Change Request object.

     .. note:: The keys in the map correspond to the name of the field on the Change Request in Cherwell that you would like to set (see https://bertram.d.pr/1Ziuhy for a reference).  In addition, the value in the map corresponds to the value you wish to use.  Within the value, Morpheus variables may be used.  Here is an example for setting the Description is:

       .. code-block::

          {
          "Description":"Created from Morpheus by ${instance.createdByUsername} in ${zone.name}"
          }


#. Save Changes
