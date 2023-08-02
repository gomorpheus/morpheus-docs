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

IMAGE - CREATE ROLE
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

IMAGE - CREATE TENANT
  :width: 50%

With the Tenant created, the rest of the guide will pertain to configuring the new Tenant and demonstrating how to provision new workloads using resources shared down from the |mastertenant|.

Users and User Roles
^^^^^^^^^^^^^^^^^^^^

In the prior steps we've created a new Tenant and associated our created Tenant Role with it. If you click into the new Tenant you'll notice that there are currently no users so the new Tenant is still unusable. We could go ahead and create a new User but if this is a new |morpheus| environment, the new Tenant will not have any User Roles to apply to the new User we wish to create.

To remedy this problem, we can add a "Multi-Tenant User Role" from the |mastertenant|. This is essentially a Role Template from which a Role is created and seeded down to each Tenant. Only |mastertenant| administrators can create Multi-Tenant User Roles. After creation, edits can be made and permission changes will be filtered down to the child Role that exists within each Subtenant. However, it's important to know that should the child Role ever be edited in the Subtenant, the link back to the Multi-Tenant User Role will be broken and it will become like any other User Role created in the Subtenant. To prevent this situation, |mastertenant| administrators can set a "MULTITENANT LOCKED" option to restrict such edits in the Subtenant.











Multitenant User Roles, Role locking, Identity Sources
Editing users, including from master
Impersonating


Whitelabeling
^^^^^^^^^^^^^


Scoping Clouds to Tenants
^^^^^^^^^^^^^^^^^^^^^^^^^

Integrating directly in the Tenant as well as sharing from master (ex. sharing specific Resource Pools)
Same for networks, security groups


Groups
^^^^^^

Discussion of Groups and adding Cloud which has been shared with Tenant


Provisioning Test
^^^^^^^^^^^^^^^^^

Provision built-in Instance Type and note that only shared resources are available (cloud resource pool, network, SG)
