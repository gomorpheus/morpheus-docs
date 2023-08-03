Tenancy
-------

|morpheus| appliances may be multi-tenanted, that is, they may contain multiple isolated environments known as Tenants. Successfully building a multi-Tenanted |morpheus| environment requires creating and pulling together multiple constructs. This guide aims to describe the pieces needed to create functioning Tenants with Users, identity integrations, Roles, Groups, and whitelabeling. We will also share a Cloud and Library item from the |mastertenant| which is provisionable from the new Subtenant.

On installation, a single Tenant is created. This Tenant is often referred to as the |mastertenant| and has some special properties that additional created Tenants (known as Subtenants) do not have. Tenants manage their own workloads, may have their own custom whitelabeling, and also have their own users and integrations. The |mastertenant| may (or may not) share down integrations, Library items, Roles, and more but Subtenants are fully isolated from each other.

.. include:: ../../administration/tenants/tenants.rst
  :start-after: .. begin_tenants_bulleted_list
  :end-before: .. end_tenants_bulleted_list

Tenant Roles
^^^^^^^^^^^^

Before even creating the Tenant, we need to understand what a Tenant Role is and ensure that a Tenant Role with correct rights permissions exists. Tenant Roles set the maximum feature permissions levels for any User in the Subtenant and also give (or revoke) access to Clouds, Library items, Tasks, Workflows, and other things integrated or created in and shared from the |mastertenant|. Only |mastertenant| administrators have the ability to create Tenant Roles.

.. NOTE:: User Roles within the Tenant may be created with lesser permissions than the Tenant Role allows but we will discuss User Roles further in a later section.

In a new environment, the only Tenant Role will be the included "Tenant Admin" Role but this Role is not editable. It's advisable to create your own Tenant Roles so they may be edited as needed. To get started, we can create a new Tenant Role and copy from the pre-existing "Tenant Admin" Role.

#. Navigate to |AdmRol|
#. Click :guilabel:`+ CREATE ROLE`
#. Set a NAME, TYPE (Tenant Role), and COPY FROM ROLE (Tenant Admin)
#. Click :guilabel:`SAVE CHANGES`

..image:: /images/administration/tenants/addTenantRole.png
  :width: 50%

Once created, click into the new Role and edit feature permissions if you wish. Remember the Tenant Role is setting the maximum available Role permissions for each feature that Users within the Tenant can have. We'll worry about scoping resources to the Subtenant (such as Clouds) in a later section.

With a Tenant Role created, we can move on to creating the Tenant itself.

Create a Tenant
^^^^^^^^^^^^^^^

We'll now create a Tenant and apply the Tenant Role we've just created.

#. Navigate to |AdmTen|
#. Click :guilabel:`CREATE TENANT`
#. Name your Tenant and set the Tenant Role in the BASE ROLE field
#. Click :guilabel:`SAVE CHANGES`

The NAME and BASE ROLE are the most important settings and the only two required. See the Tenants section of |morpheus| documentation to learn more about other settings which may be applied when adding or editing Tenants.

..image:: /images/administration/tenants/addTenant.png
  :width: 50%

With the Tenant created, the rest of the guide will pertain to configuring the new Tenant and demonstrating how to provision new workloads using resources shared down from the |mastertenant|.

Users and User Roles
^^^^^^^^^^^^^^^^^^^^

In the prior steps we've created a new Tenant and associated our created Tenant Role with it. If you click into the new Tenant you'll notice that there are currently no users so the new Tenant is still unusable. We could go ahead and create a new User but if this is a new |morpheus| environment, the new Tenant will not have any User Roles to apply to the new User we wish to create.

To remedy this problem, we can add a "Multi-Tenant User Role" from the |mastertenant|. This is essentially a Role Template from which a Role is created and seeded down to each Tenant. Only |mastertenant| administrators can create Multi-Tenant User Roles. After creation, edits can be made and permission changes will be filtered down to the child Role that exists within each Subtenant. However, it's important to know that should the child Role ever be edited in the Subtenant, the link back to the Multi-Tenant User Role will be broken and it will become like any other User Role created in the Subtenant. To prevent this situation, |mastertenant| administrators can set a "MULTITENANT LOCKED" option to restrict such edits in the Subtenant.

New Multi-Tenant User Roles are created in |AdmRol|:

#. Click :guilabel:`+ CREATE ROLE`
#. Provide a NAME, TYPE (User Role), COPY FROM ROLE (if desired)
#. Mark the boxes to set MULTITENANT ROLE and MULTITENANT LOCKED
#. Click :guilabel:`SAVE CHANGES`

After saving the Role, it will appear in the |mastertenant| and will also be seeded down to the Tenant we've already created since it is a Multi-Tenant User Role. We've also locked the Role so that Subtenant users cannot edit it and thus unlink it from future permissions edits made in the |mastertenant|. Keep in mind that no matter what permissions we set, Users in the Subtenant will not be able to exceed permissions set on the Tenant Role as discussed in a prior section. If desired, you can click into this User Role now and edit its permissions to suit your needs.

..image:: /images/administration/tenants/addUserRole.png
  :width: 50%

At this point we're ready to add a User which will make the Tenant usable. We can create one in the new Tenant by navigating to the Tenant list page (|AdmTen|) and selecting the Tenant. There are a number of configurations to make when creating a user but when selecting the User's Role you should see the previously-created Multi-Tenant User Role.

..image:: /images/administration/tenants/addUser.png
  :width: 50%

After saving the new User, we can make the first test of the new Tenant by impersonating the User and entering the Tenant. In the list of Users on the Tenant detail page, click the gear (|gear|) icon at the end of the User's row and select "Impersonate." You should end up inside the new Tenant operating as the new user. This can be confirmed by making note of the updated name given in the upper-right portion of the application window. To quit impersonating, click on the name and select "Quit Impersonating."

At this point we've created a User manually but it's important to point out that |morpheus| can also use an existing identity integration, such as Microsoft Active Directory, to manage User creation and Role assignment. Expand the section below to see an example use case or continue on if you'd prefer to administer your Users directly in |morpheus|. The complete integration guide elsewhere in |morpheus| docs also includes common Active Directory troubleshooting steps should those be needed.

- .. toggle-header:: :header: **Microsoft Active Directory Example**

    .. include:: ../../integration_guides/IdentityManagement/active_directory.rst
      :start-after: .. begin_active_directory
      :end-before: .. end_active_directory

Whitelabeling
^^^^^^^^^^^^^

|morpheus| allows each Tenant to be customized with its own look and feel through whitelabeling features. Your organization can replace the stock |morpheus| logo and color scheme with your own logos and colors. Whitelabel settings are held in |AdmSetWhi| and are mostly self-explanatory. Upload logos and set custom hexadecimal colors in each field. When done, be sure to set the "Enable Whitelabel" configuration and click :guilabel:`SAVE` all the way at the bottom of the page. If needed, review a more detailed explanation of each `whitelabel setting <https://docs.morpheusdata.com/en/latest/administration/settings/settings.html#whitelabel>`_ in |morpheus| documentation.

..image:: /images/administration/tenants/whitelabelSettings.png

Scoping Clouds to Tenants
^^^^^^^^^^^^^^^^^^^^^^^^^

With the Tenant now created and seeded with a User and Roles, we're ready to look at how to set up useful provisioning resources. Of course, Tenants are complete (yet isolated) |morpheus| environments which can create their own Cloud integrations or utilize integrations with other third party technologies (assuming they haven't been restricted from doing so by the Tenant Role). However, |mastertenant| administrators may also choose to share integrations created in the |mastertenant| down to Subtenant users.

Many constructs in |morpheus| have a "Visibility" attribute when viewed from the |mastertenant|. This attribute controls whether the construct is "Private" (in other words reserved for a selected Tenant) or Public (available to all Tenants). In our example, we're going to expose an Amazon AWS Cloud integrated in the |mastertenant| down to our newly-created Subtenant. To set the Cloud visibility, use the following steps:

#. Navigate to the Clouds list page (|InfClo|)
#. Edit the Cloud by clicking the pencil icon (|pencil|) in its row
#. Toggle the VISIBILITY attribute to "Public"
#. Click :guilabel:`SAVE CHANGES`

..image:: /images/administration/tenants/editCloud.png
  :width: 50%

The Cloud is now exposed to the Subtenant but we also need to expose a Resource Pool (A VPC, in Amazon parlance) for Subtenant users to provision into. We do this from the Cloud detail page (|InfClo|) > Click on selected Cloud.

#. Select the Resources subtab
#. Click ACTIONS next to the selected Resource Pool (VPC)
#. Click Edit
#. Expand the "Tenant Permissions" section
#. Set Visibility to Public (alternatively, you could keep the Private visibility and add the new Tenant in the next field)
#. Click :guilabel:`SAVE CHANGES`

..image:: /images/administration/tenants/addResourcePool.png

Repeat the same process for Networks and Security Groups, both of which are contained in the Networks subtab of the Cloud detail page.

Groups
^^^^^^

The last thing to take a look at before Library items and provisioning are Groups. Groups define which resources a User can access. Group access is defined by the User Role and many resources have a Group access component which allows administrators to control User access to things like Clouds, Networks, Datastores, Resource Pools, Folders and more.

Groups exist solely within the Tenant that creates them, they cannot be shared down from |mastertenant| to Subtenants. In order to create a Group for our new Tenant, impersonate the User we've created in previous steps. Once working in the Tenant, use the following steps:

#. Navigate to |InfGro|
#. Click :guilabel:`+ CREATE`
#. Set a NAME for the Group and click :guilabel:`SAVE CHANGES`

We'll now add the shared Cloud to the Group:

#. Click on the name of the Group to access the Group detail page
#. Click on the Clouds tab
#. Click :guilabel:`+ ADD`
#. Use the typeahead field to select the shared Cloud
#. Click :guilabel:`SAVE CHANGES`

..image:: /images/administration/tenants/addCloudToGroup.png
  :width: 50%

At this point the basic configuration steps are complete and we will attempt a provisioning test using built-in Instance Types which are preinstalled with |morpheus|.

Provisioning Test
^^^^^^^^^^^^^^^^^

At this point, you can conduct a test by attempting to provision one of the basic Instance Types shipped with |morpheus| for demonstration purposes. To test, we'll provision a basic Ubuntu box to our AWS Cloud.

#. Navigate to |ProIns|
#. Click :guilabel:`+ ADD`
#. Select the Ubuntu Instance Type
#. Click :guilabel:`NEXT`
#. Select the Group and Cloud noting that only resources shared with the Subtenant are selectable
#. Name the Instance
#. Click :guilabel:`NEXT`
#. On the CONFIGURE tab, select a Resource Pool, Network, and Security Group once again noting that only resources shared with the Subtenant are selectable
#. Click :guilabel:`NEXT`
#. Click :guilabel:`NEXT` once again
#. Click :guilabel:`COMPLETE`

..image:: /images/administration/tenants/createInstance.png

After a minute or two, the Instance should be fully provisioned.

Exposing Custom Instance Types to Subtenants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|mastertenant| administrators can also share custom Library items down to Subtenants. Do do this, navigate to |LibBlu| and select an Instance Type. Click the pencil (|pencil|) icon in the row for the selected Instance Type to edit it. As we've done before, update the VISIBILITY setting to Public. In addition, ensure the User Role for the Subtenant User grants access to the selected Instance Type. Once configurations have been made, conduct a similar test to the previous section. When you attempt to provision a new Instance, the new Instance Type should be selectable and the User should be able to provision the custom Instance Type in the same was as the default Instance Type was provisioned in the previous step.
