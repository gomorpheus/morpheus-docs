Option Lists
------------

Option Lists allow you to give the user more choices during provisioning to then be passed to scripts and/or automation.  Option Lists, however, are pre-defined insofar as they are not free-form. They can be manually entered CSV or JSON, they can be dynamically compiled from REST calls via GET or POST requests, or populated by LDAP queries.

.. NOTE:: JSON entries must be formatted like the following example: ``[{"name":"Test","value":1},{"name":"Testing","value":2}]``

.. image:: /images/provisioning/library/newOptionList.png
   :align: center

Option List Fields
^^^^^^^^^^^^^^^^^^

The displayed fields in the create/edit Option List modal depend on the TYPE value selected.

NAME
 Name of the Option List
DESCRIPTION
 Description of the Option List for reference in Option List list view
TYPE
 - **REST:** REST API call to populate Option List
 - **Manual:** Manually entered dataset, CSV or JSON
 - **|morpheus| API:** Call to |morpheus| API to populate the Option List
 - **LDAP:** Searches and returns a list of Active Directory objects
VISIBILITY
 If the account currently signed in is not in the master tenant, visibility will automatically change to private

**For manual Option Lists:**

DATASET
 Appears only for manual Option Lists. Add your CSV or JSON list to this field

**For Option Lists populated by a REST call:**

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
 Create a JS script to translate the result data object into an array containing objects with properties 'name' and 'value'. The input data is provided as 'data' and the result should be put on the global variable 'results'.
REQUEST SCRIPT
 Create a JS script to prepare the request. Return a data object as the body for a POST request, and return an array containing properties 'name' and 'value' for a GET request. The input data is provided as 'data' and the result should be put on the global variable 'results'

 **For Option Lists populated by an LDAP query:**

 LDAP URL
  The URL pointing to the LDAP server
 USERNAME
  The fully qualified username (with @ suffix syntax) for the binding account
 PASSWORD
  The password for the above account
 LDAP Query
   The LDAP query to pull the appropriate objects. See the next section for an example use case
 TRANSLATION SCRIPT
   Create a JS script to translate the result data object into an array containing objects with properties 'name' and 'value'. The input data is provided as 'data' and the result should be put on the global variable 'results'.

.. NOTE:: Option Lists are set on one or multiple ``Select List`` or ``Typeahead`` Option Types. The Option Type is then set on an Instance Type, Layout, Cluster Layout, and/or Operational Workflow for input during provisioning or execution.

Creating an Option List Based on an LDAP Query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Morpheus version 4.2.1 and higher, Option Lists can be populated from LDAP queries. This gives users the ability to search Active Directory, capture objects, and present them as custom options where needed.

It's recommended that you connect LDAP-type Option Lists to Typeahead-type Option Types as the list of returned selections can be very large. This also allows you to select multiple options from the list, presuming you've allowed for that when creating the Option Type.

Populating LDAP-type Option Lists requires knowledge of LDAP query syntax. This guide provides one example and there are many publicly-available resources for help writing additional queries.

1. Create a new Option List (Provisioning > Library > Option Lists > ADD)

2. Enter a name for the new LDAP Option List

3. Change the Type value to LDAP and the relevant fields will appear as shown in the screenshot:

4. Enter the LDAP URL in the following format (an example is also shown as a placeholder in the UI form field):

.. code-block:: bash

  ldap[s]://<hostname>:<port>/<base_dn>

5. Enter the fully qualified username with @ suffix syntax, such as: `user@ad.mycompany.com`

6. Enter the account password

7. Enter your LDAP query. You can even inject variables into your query structure to query based on the value the user has entered into the typeahead field as shown in the example below:

.. code-block:: bash

  (&(objectClass=user)(cn=<%=phrase%>*))

8. Finally, enter a translation script which will convert the returned LDAP object into a list of name:value pairs you can work with in Morpheus. The example script below shows the user DisplayName and sets the value to the SAMAccountName:

.. code-block:: bash

  for(var x=0;x < data.length ; x++) {

    var row = data[x];
    var a = {};

      if(row.displayName != null) {
      a['name'] = row.displayName;

    } else {

      a['name'] = row.sAMAccountName;

    }

    a['value'] = row.sAMAccountName;
    results.push;

  }

9. Click SAVE CHANGES

.. image:: /images/provisioning/library/ldap_option_list.png
  :width: 80%
