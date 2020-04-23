Option Lists
------------

Option Lists allow you to give the user more choices during provisioning to then be passed to scripts and/or automation.  Option Lists, however, are pre-defined insofar as they are not free-form. They can either be manually entered CSV or JSON or they can be dynamically compiled from REST calls via GET or POST requests.

.. NOTE:: JSON entries must be formatted like the following example: ``[{"name":"Test","value":1},{"name":"Testing","value":2}]``

.. image:: /images/provisioning/library/newOptionList.png
   :align: center

Create Option List
^^^^^^^^^^^^^^^^^^

NAME
 Name of the Option List
DESCRIPTION
 Description of the Option List for reference in Option List list view
TYPE
 - REST
    REST API call to populate Option List
 - Manual
    Manually entered dataset
 - |morpheus| API
    Call to |morpheus| API to populate Option List
VISIBILITY
 If the account currently signed in is not in the master tenant, visibility will automatically change to private
DATASET
 Appears only for manual Option Lists. Add your CSV or JSON list to this field
SOURCE URL
 A REST URL used to fetch list data which is cached in the appliance database
REAL TIME
 When checked, a REST call will be made to update the Option List at the time its presented to the User
IGNORE SSL ERRORS
 Do not fail API query for self-signed or invalid certs on REST call target
SOURCE METHOD
  GET or POST
SOURCE HEADERS
 Custom HTTP Headers to include in the source request
INITIAL DATASET
 Create an initial JSON or CSV dataset to be used as the collection for this option list. It should be a list containing objects with properties 'name' and 'value'
TRANSLATION SCRIPT
 Create a JS script to translate the result data object into an array containing objects with properties 'name' and 'value'. The input data is provided as data and the result should be put on the global variable results.
REQUEST SCRIPT
 Create a JS script to prepare the request. Return a data object as the body for a POST request, and return an array containing properties 'name' and 'value' for a GET request. The input data is provided as 'data' and the result should be put on the global variable 'results'.

.. NOTE:: Option Lists must be set on one or multiple ``Select List`` Option Types. The Option Type is then set on an Instance Type, Layout, Cluster Layout, and/or Operational Workflow for input during provisioning or execution.
