Configuring Tenants and Resources for Multi-Tenancy
---------------------------------------------------

A very common scenario for Managed Service Providers is the need to provide access to resources on a customer by customer basis. Several administrative features are available in |morpheus| to ensure customer resources are properly scoped and isolated. With its built multi-tenancy capabilities and white label support, managed service providers have a wide range of capabilities when it comes to managing customer Tenants and users.

Tenants
^^^^^^^

There are essentially two types of Tenants in |morpheus|

* Master Tenant
* Sub Tenants

During the initial setup of a |morpheus| Appliance, the Master Tenant is created. All Tenants created in addition to this Master Tenant are sub-Tenants. There can only be one Master Tenant, and sub-Tenants cannot become the Master Tenant. The delineation between the Master Tenant and sub-Tenants is important to understand for properly scoping resources across Tenants.

Creating Tenants
````````````````

The Master Tenant is created during the initial appliance setup. Additional sub-Tenants can be created in the `Administration -> Tenants` section.

The Tenants page displays a list of all Tenants. This page enables users to: Create, Edit, and Delete Tenants. The list of Tenants displays the Tenant Name, Role, Total Instances, Total Users, Status (active or inactive) and the Created Date. Click the Tenant Name to drill into the Tenant View where you can edit or delete the Tenant, as well as create, edit and delete users belonging to the Tenant.

.. NOTE:: At least one Tenant in addition to the Master Tenant is required to scope resources across Tenants.

To create a new sub-Tenant

#. Select the Administration link in the navigation bar.
#. Select the Tenants link in the sub navigation bar.
#. Click the :guilabel:`+Create Tenant` button.
#. From the New Tenant wizard input
   * Name (Required)
   * Description
   * Base Role
   * Currency (for pricing)

The Base Role defines a role set from which all roles created within the Tenant will inherit.

.. NOTE:: In prior versions, we could set Limits when creating a Subtenant. These could restrict the amount of storage, memory, and CPUs that can be collectively provisioned by all users in the Tenant. In more recent versions, this functionality has been rolled into Policies (|AdmPol|). When creating a Policy, we are able to specify a Tenant to which the Policy should apply.

Click the :guilabel:`Save Changes` button.

.. image:: /images/advanced/tenant/createtenant.png
	:width: 80%
	:alt: The Create Tenant dialog box is shown
	:align: center

Viewing Tenants
```````````````````

To View an individual Tenant page, select the Tenant name from the main Tenants section.

.. image:: /images/advanced/tenant/viewtenant.png

From inside the Tenant view, we can edit or delete the Tenant, as well as click into any of the Tenant's users.

Tenant Users
`````````````

To create a new user within the Tenant:

Click the :guilabel:`CREATE USER` button, then from the New User wizard input the fields below:

* First Name
* Last Name
* Username
* Email
* Role
* Password
* Confirm Password

Click :guilabel:`Save Changes`.

.. NOTE:: Users are specific to each Tenant. Users created in the Master Tenant or other sub-Tenants will only have access to the Tenant they are created in.

Impersonate Tenant User
```````````````````````

|morpheus| allows admin users in the Master Tenant to impersonate any user in the Subtenants to see the application as if they are that user. To impersonate a user, you must be logged in as a user with the "Impersonate User" feature enabled in the assigned role.

From inside a Tenant detail page (containing the list of that Tenant's users), and in the specific user's ACTIONS drop down, select "Impersonate".

.. image:: /images/advanced/configuring_multi_tenancy-9583a.png

This will log you in as that user in their respective Tenant. To log out of the impersonate users Tenant, select the username in the header, and then select "Quit Impersonating"

.. image:: /images/advanced/configuring_multi_tenancy-d229b.png

Resources
^^^^^^^^^
In the Master Tenant, resources can be configured with private or public visibility:

* Private Visibility: Only available to the assigned Tenant.
* Public Visibility (option available in Master Tenant only): Available across all Tenants

Resources in the Master Tenant can also be assigned directly to Subtenants. When a resource is assigned to a Subtenant, it is only available for that Subtenant, and its visibility is automatically set to private. Public visibility is not an option for any resource assigned to or created in a Subtenant.

From the Master Tenant, the following resources can be configured for public visibility across all Tenants, or assigned to individual sub-Tenants

* Clouds
* Hosts
* Virtual Machines
* Networks
* Datastores
* Resource Pools
* Folders
* Virtual Images
* Library Instance Types
* Pricing
* Policies
* Workflows
* Roles

.. NOTE:: Virtual Image Blueprints can be made available to multiple select Tenants when set to private.

Cloud Visibility & Assignment
``````````````````````````````

To set the visibility of a Cloud to Public (shared across all Tenants) or Private (only available to the assigned Tenant):

#. Navigate to Infrastructure > Clouds
#. Select either the pencil/edit icon on the end of the cloud row, or click the name of the cloud and select "Edit" in the cloud page.
#. From the "Visibility" drop down, select either "Public" or "Private"
#. Select :guilabel:`Save Changes` in the footer of the Edit Cloud modal.

.. image:: /images/advanced/configuring_multi_tenancy-349e2.png

When a cloud is set to Public visibility, it is available to be added to Subtenants. All Subtenants created after a Master Tenant cloud is set to public will automatically have clouds with public visibility added, and a group will be created for each available cloud matching the cloud name in the new Subtenant(s).

For Tenants created prior to a Master Tenant cloud being set to public visibility, the Subtenant will have the option to add that cloud but it will not automatically be added.

While the cloud will be available for Subtenants, the resources available in that cloud to the Subtenant(s) depends on the visibility or assignment of the individual resources.

.. NOTE:: A Subtenant user must have sufficient role permissions and cloud access to add publicly available clouds. Master Tenant clouds settings cannot be edited from Subtenants.

Assign a Cloud to an Tenant
```````````````````````````

.. IMPORTANT:: When assigning a Cloud to a Tenant, all resources for that Cloud will only be available to the assigned Tenant. If a cloud is created in the Master Tenant and assigned to a sub-Tenant, it will no longer be available for use by the Master Tenant or any other sub-Tenants, although it can be assigned back to the Master Tenant, or to another sub-Tenant.

It may be preferable for service providers to share or assign their cloud resources, such as specific hosts, networks, resources pools and datastores, across sub-Tenants, rather than an entire cloud.

**To assign a cloud from the Master Tenant to a Sub-Tenant**

#. Navigate to Infrastructure, Clouds
#. Select either the pencil/edit icon on the end of the cloud row, or click the name of the cloud and select "Edit" in the cloud page.
#. From the "Tenant" drop down, select the Tenant to assign the cloud to. The visibility will automatically be set to "Private" when a cloud is assigned to a sub-Tenant.
#. Select :guilabel:`Save Changes` in the footer of the Edit Cloud modal.

.. image:: /images/advanced/configuring_multi_tenancy-c907d.png

When a cloud is assigned to a sub-Tenant, or assigned to the Master Tenant with private visibility, that cloud and all of its resources are only available to the assigned Tenant. The Master Tenant still maintains control and visibility, and can edit the cloud settings or re-assign the cloud.

Individual Resource Visibility & Assignment
````````````````````````````````````````````

Similar to clouds, individual resources from the Master Tenant can be set to public and available to sub-Tenants, or assigned to sub-Tenants.

By default, any host, virtual machine, bare metal server, network, resource pool, datastore or blueprint added, created or inventoried by an Tenant is assigned to that Tenant. If these resources are in the Master Tenant, they can be assigned to sub Tenants. Assigning one of these resources will make it unavailable to the Master Tenant, but it will still be visible and editable by the Master Tenant. This allows Master Tenant resources to be isolated for use by sub-Tenants while still under the control of the Master Tenant.

Resources assigned to sub-Tenants from the Master Tenant will be visible and available for use by that sub-Tenant, however they cannot be edited or re-assigned by the sub-tenant.

**Set the Visibility of a Host, Virtual Machine or Bare metal Server to Public or Private**

#. From the Master Tenant, navigate to Infrastructure, Hosts
#. Select either the Hosts, Virtual Machines or Bare Metal tab
#. Click the name of the resource
#. Select :guilabel:`Edit` in the resource page to bring up the config modal
#. From the "Visibility" drop down, select either "Public" or "Private"
#. Select :guilabel:`Save Changes`

.. image:: /images/advanced/configuring_multi_tenancy-d738d.png

Assigning a Host, Virtual Machine, or Bare Metal server to an Tenant

#. From the Master Tenant, navigate to Infrastructure, Hosts
#. Select either the Hosts, Virtual Machines or Bare Metal tab
#. Click the name of the resource
#. From the "Actions" dropdown in the the resource page, select Assign Tenant
#. In the Assign Tenant modal, select the Tenant to assign the resource to.
#. Select :guilabel:`Execute` in the modal

.. image:: /images/advanced/configuring_multi_tenancy-3c39f.png

The resource will now be assigned and available for use by the assigned Tenant. If assigned to a sub-Tenant, the Master Tenant will maintain visibility and control.

**Set the Visibility of a Network to Public or Private**

#. From the Master Tenant, navigate to Infrastructure, Network
#. Select either the pencil/edit icon in the network row, or click the name of the network and select "Edit" in the network page.
#. From the "Visibility" drop down, select either "Public" or "Private"
#. Select :guilabel:`Save Changes` in the modal

.. image:: /images/advanced/configuring_multi_tenancy-bc333.png

**Assign a Network to an Tenant**

#. From the Master Tenant, navigate to Infrastructure, Network
#. Select either the pencil/edit icon in the network row, or click the name of the network and select "Edit" in the network page.
#. From the "Tenant" drop down, select an Tenant to assign the network to.
#. Select :guilabel:`Save Changes` in the lower the modal

.. image:: /images/advanced/configuring_multi_tenancy-9f15c.png

The Network will now be assigned and available for use by the assigned Tenant. If assigned to a sub-Tenant, the Master Tenant will maintain visibility and control.

Set the Visibility or assign a datastore to an Tenant

#. From the Master Tenant, navigate to Infrastructure, Storage
#. Select the "Data Stores" tab
#. Select Edit from the "Actions" dropdown in the datastores row
#. From the "Visibility" drop down, select either "Public" or "Private"
#. From the "Tenant" drop down, select the Tenant to assign the datastore to.

   .. NOTE:: If assigned to a sub-tenant, the visibility will be automatically set to private.

#. Select :guilabel:`Save Changes` in the modal

.. image:: /images/advanced/configuring_multi_tenancy-1e978.png

**Set the Visibility or assign a Virtual Image to an Tenant**

#. From the Master Tenant, navigate to Provisioning, Virtual Images
#. Select Edit from the "Actions" dropdown in the Virtual Images row
#. From the "Visibility" drop down, select either "Public" or "Private". Public will share the
#. From the "Tenant" field, start typing the name of the Tenant to assign the Virtual Image to. Matching Tenants will populate, then select the Tenant to add.

   .. NOTE:: Virtual Images can be set to Private, but accessible to more that one Tenant

#. Repeat step 4 for all Tenants requiring access to the virtual image.
.. To remove access for an Tenant, click the "x" next to the Tenant name
#. Select :guilabel:`Save Changes` in the modal

.. image:: /images/advanced/configuring_multi_tenancy-d9abe.png

The Virtual Image will now be available for use by the assigned Tenants.
