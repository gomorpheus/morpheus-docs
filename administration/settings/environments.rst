Overview
^^^^^^^^

The Environments section is where you create and manage your environment labels, which are available in the `Environment` dropdown during Instance or App provisioning. An Instance's environment label can be changed by editing the Instance.

An Environment is an ``InstanceContextType`` record containing a code, name, description, display order, Tenant, visibility, and active state. Selecting one stores its context on the Instance or App. This supports categorization, display, filtering, automation variables, and naming-policy expressions; it is not itself a placement rule, lifecycle action, or RBAC boundary. Use Groups/Clouds and Policies for placement or lifecycle behavior and Roles/resource permissions for access segmentation. Provisioning Settings can require users to select an Environment, but that requirement does not change what the selected value authorizes.

Creating Environments
`````````````````````

#. Select `+ Create Environment`
#. Populate the following for the New Environment:

   Name
    The friendly name for the environment in |morpheus|
   Code
    Shortcode used for API and CLI
   Description
    Environment description displayed on the Environments list page
   Display Order
    The order in which environments are presented when provisioning, a value of "0" will position the environment at the top of the list
   Visibility
    * *Private*: Available only in the Tenant the environment is created in
    * *Public*: Available for all Tenants. Public is only applicable for environments created in the the Master Tenant.

.. NOTE:: User-created environments can be edited, hidden, or removed from the Actions menu on the environments list page. |morpheus|-default environments can only be hidden from users during provisioning.
