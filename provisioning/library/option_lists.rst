Option Lists
------------

Option Lists allow you to give the user more choices during provisioning to then be passed to scripts and/or automation.  Option Lists, however, are pre-defined insofar as they are not free-form. They can be manually entered CSV or JSON, they can be dynamically compiled from REST calls via GET or POST requests, or populated by LDAP queries.

.. image:: /images/provisioning/library/newOptionList.png
   :align: center
   :scale: 90%

Generic Option List Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^

The displayed fields in the create/edit Option List modal depend on the TYPE value selected.

  NAME
    Name of the Option List
  DESCRIPTION
    Description of the Option List for reference in Option List list view
  TYPE
    - **REST:** REST API call to populate Option List
    - **Manual:** Manually entered dataset, CSV or JSON
    - **Morpheus API:** Call to internal |morpheus| API to populate the Option List
    - **LDAP:** Searches and returns a list of Active Directory objects
  VISIBILITY
    If the account currently signed in is not in the master tenant, visibility will automatically change to private

Manual Option List Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

  DATASET
    Appears only for manual Option Lists. Add your CSV or JSON list to this field

    .. NOTE:: JSON entries must be formatted like the following example: ``[{"name":"Test","value":1},{"name":"Testing","value":2}]``


REST Option List Fields
^^^^^^^^^^^^^^^^^^^^^^^

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

    **Example:**

    .. code-block:: javascript

      for(var x=0;x < data.length; x++) {
        results.push({name: data[x].name,value:data[x].id});
      }

  REQUEST SCRIPT
    Create a JS script to prepare the request. Return a data object as the body for a POST request, and return an array containing properties 'name' and 'value' for a GET request. The input data is provided as 'data' and the result should be put on the global variable 'results'

    **Example:**

    .. code-block:: javascript

      results.push({name: 'userId', value : data.users})

Morpheus API Option List Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  OPTION LIST
    A list of available object types to return
  TRANSLATION SCRIPT
    Create a JS script to translate the result data object into an array containing objects with properties 'name' and 'value'. The input data is provided as 'data' and the result should be put on the global variable 'results'.

    **Example:**

    .. code-block:: javascript

      var i=0;
      results = [];
      for(i; i<data.length; i++) {
        results.push({name: data[i].name, value: data[i].value});
      }

    Translation script inputs:

      **Clouds**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``name: <String>``
      - ``displayName: <String>``
      - ``category: <String>``
      - ``description: <String>``
      - ``apiKey: <String>``
      - ``status: <String>``
      - ``hourlyPrice: <Number>``
      - ``hourlyCost: <Number>``
      - ``instanceType: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``plan:<Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``site:<Object>``

        - ``id: <Number>``
        - ``name: <String>``

      **Environments**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience attribute to avoid requiring translation
      - ``code: <String>``
      - ``name: <String>``

      **Groups**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience attribute to avoid requiring translation
      - ``name: <String>``
      - ``code: <String>``
      - ``uuid: <String>``
      - ``location: <String>``
      - ``datacenterId: <Number>``

      **Instances**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``name: <String>``
      - ``displayName: <String>``
      - ``category: <String>``
      - ``description: <String>``
      - ``apiKey: <String>``
      - ``status: <String>``
      - ``hourlyPrice: <Number>``
      - ``hourlyCost: <Number>``
      - ``instanceType: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``plan: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``site: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      **Instances Wiki**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``name: <String>``
      - ``urlName: <String>``
      - ``category: <String>``
      - ``instanceId: <String>``
      - ``content: <String>``
      - ``contentFormatted: <String>``
      - ``format: <String>``
      - ``createdByUsername: <String>``
      - ``updatedByUsername: <String>``

      **Networks**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``code: <String>``
      - ``category: <String>``
      - ``name: <String>``
      - ``status: <String>``
      - ``cloudId: <Number>``
      - ``groupId: <Number>``
      - ``networkType:<Object>``

        - ``id: <Number>``
        - ``code: <String>``
        - ``name: <String>``

      - ``externalId: <String>``
      - ``externalNetworkType: <String>``
      - ``networkDomain: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``networkPool: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``createdBy: <String>``

      **Plans**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``code: <String>``
      - ``name: <String>``
      - ``storage: <Integer, bytes>``
      - ``memory: <Integer, bytes>``
      - ``cores: <Number>``

      **Resource Pools**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``code: <String>``
      - ``externalId: <String>``
      - ``name: <String>``
      - ``serverGroupId: <Number>``
      - ``status: <String>``
      - ``regionCode: <String>``
      - ``parentPoolId: <Number>``
      - ``type: <String>``

      **Security Groups**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``code: <String>``
      - ``name: <String>``
      - ``externalType: <String>``
      - ``externalId: <String>``
      - ``cloudId: <Number>``
      - ``scopeMode: <String>``
      - ``scopeId: <Number>``

      **Servers**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``name: <String>``
      - ``displayName: <String>``
      - ``description: <String>``
      - ``category: <String>``
      - ``osType: <String>``
      - ``powerState: <String>``
      - ``lastStats: <String>``
      - ``zone: <Object>``

        - ``id: <Number>``
        - ``name: <String>``

      - ``capacityInfo: <Object>``

        - ``maxStorage: <Integer, bytes>``
        - ``maxMemory: <Integer, bytes>``
        - ``maxCores: <Number>``
        - ``usedMemory: <Integer, bytes>``
        - ``usedStorage: <Integer, bytes>``

      - ``computeServerType: <Object>``

        - ``id: <Number>``
        - ``name: <String>``
        - ``nodeType: <String>``
        - ``vmHypervisor: <String>``
        - ``containerHypervisor: <String>``

      **Servers Wiki**

      - ``id: <Number>``
      - ``value: <Number>`` // id, convenience
      - ``name: <String>``
      - ``urlName: <String>``
      - ``category: <String>``
      - ``serverId: <String>``
      - ``content: <String>``
      - ``contentFormatted: <String>``
      - ``format: <String>``
      - ``createdByUsername: <String>``
      - ``updatedByUsername: <String>``

  REQUEST SCRIPT
    The request script is used differently for Morpheus API Option List types. A Morpheus API option list type will use an internal API to return a list of objects instead of performing HTTP(S) requests to the Morpheus API. Due to this approach, the results object will not be used to generate query parameters or a JSON body. The results object will instead be used to contain a map of accepted key:value pairs that can be used to filter, sort and order the list of objects that get returned.

    Below is a list of accepted ``key:value`` pairs for each object type:
      **Generic options available for all object types**

      - ``max: <integer>`` // Maximum number of results to return. Default: 25
      - ``offset: <integer>`` // Offset for returned results. Default: 0
      - ``sort: <string>`` // Field to sort on. Default: 'name'
      - ``order: <string>`` // Order of returned values. Accepted values: 'asc', 'desc'. Default: 'asc'
      **Example:**
      ``results = {max: 5, order : 'desc'}``

      **Networks**

      - ``zoneId``
      - ``siteId``
      - ``planId``
      - ``provisionTypeId: <Number>`` // Id of the provision type (technology), filters to only networks associated with this provision type
      - ``layoutId: <Number>`` // Id of an Instance Layout, ignored if provisionTypeId is supplied, otherwise used to look up the provision type
      - ``poolId: <Number>`` // Id of a network pool, filters to only networks within the specified network pool

      **Plans**

      - ``zoneId``
      - ``siteId``
      - ``layoutId``
      - ``provisionTypeId: <Number>`` // Id of the provision type (technology), filters to only plans associated with this provision type

      **Resource Pools**

      - ``zoneId``
      - ``siteId``
      - ``planId``
      - ``layoutId: <Number>`` // Id of an Instance Layout, used to get the associated provision type and filter to that provision type

      **Security Groups**

      - ``zoneId`` // required
      - ``poolId``

      **Clouds**

      - ``zoneId : <integer>``  // Database ID of cloud to return
      - ``tenantId : <integer>`` // Database ID of tenant where clouds are added. Filters to only clouds added within the specified tenant. Only available in Master Tenant
      - ``zoneTypeId : <integer>`` // Database ID of cloud type. Filters to only clouds with the specified cloud type
      - ``siteId : <integer>`` // Database ID of group. Filters to only clouds within the specified group
      - ``tagName : <string>`` // Filters to clouds with servers with tags containing the tagName
      - ``tagValue : <mixed>`` // Requires tagName. Filters to clouds with servers that have tags containing the tagName and specified tagValue
      - ``phrase : <string>`` // Fuzzy matches phrase on cloud name and description
      **Example:**
      ``results = {tenantId: 1, siteId: 1, tagName: "morpheus"}``

      **Instances**

       - ``appsId : <integer>`` // Database ID of app to filter by. Returns instances linked to the app
       - ``tenantId : <integer>`` // Database ID of tenant where instances are located. Filters to only instances within the specified tenant. Only available in Master Tenant
       - ``serverId : <integer>`` // Database ID of server. Filters to the instance that contains the specified server 
       - ``tagName : <string>`` // Filters to instances with tags containing the tagName
       - ``tagValue : <mixed>`` // Requires tagName. Filters to instances with tags containing the tagName and specified tagValue
       - ``phrase : <string>`` // Fuzzy matches phrase on instance name and description
       **Example:**
       ``results = {tenantId:1, phrase: "ha"}``

      **Groups**

      - ``tenantId : <integer>`` // Database ID of tenant where groups are located. Filters to only groups added within the specified tenant. Only available in Master Tenant
      - ``zoneTypeId : <integer>`` Database ID of cloud type. Filters to only groups that contain clouds with the specified cloud type
      - ``zoneId : <integer>``  // Database ID of cloud. Filters to only groups that contain the cloud with the specified ID
      - ``siteId : <integer>`` // Database ID of group to return
      - ``phrase : <string>`` // Fuzzy matches phrase on group name and location.

      **Servers**

      - ``tenantId : <integer>`` // Database ID of tenant where servers are located. Filters to only servers within the specified tenant. Only available in Master Tenant
      - ``serverId : <integer>`` // Database ID of server. Filters to the server specified by the ID
      - ``siteZoneId : <integer>`` // Database ID of cloud. Filters to servers contained within the specified cloud
      - ``serverType : <string>`` // Type of server. Accepted values: 'host', 'baremetal', 'vm'
      - ``siteId : <integer>`` // Database ID of group. Filters to only servers contained within clouds that are added in the specified group
      - ``tagName : <string>`` // Filters to servers with tags containing the tagName
      - ``tagValue : <mixed>`` // Requires tagName. Filters to servers with tags containing the tagName and specified tagValue
      - ``phrase : <string>`` // Fuzzy matches phrase on server name and description.
      **Example:**
      ``results = {max: 50, siteZoneId : 3}``

      **instance-wiki:**
      Contains same options for Instances Morpheus API type.
        - ``phrase : <string>`` // Fuzzy matches phrase on wiki name, urlName and content

      **server-wiki:**
      Contains same options for Servers Morpheus API type.
        - ``phrase : <string>`` // Fuzzy matches phrase on wiki name, urlName and content

LDAP Option List Fields
^^^^^^^^^^^^^^^^^^^^^^^

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

.. code-block:: javascript

  for(var x=0;x < data.length ; x++) {

    var row = data[x];
    var a = {};

    if(row.displayName != null) {
      a['name'] = row.displayName;

    } else {

      a['name'] = row.sAMAccountName;

    }

    a['value'] = row.sAMAccountName;
    results.push(a);

  }

9. Click SAVE CHANGES

.. image:: /images/provisioning/library/ldap_option_list.png
  :scale: 40%
