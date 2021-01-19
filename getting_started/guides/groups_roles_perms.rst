Configuring Access with Clouds, Groups, and Roles
=================================================

As you get started, it's vital to understand constructs such as Clouds and Groups as they are implemented in |morpheus|. Deploying an effective strategy for dividing organizational resources and people groups under these constructs will ensure all parties have convenient access to the resources they need. Currently-existing strategies for splitting resources and controlling costs continue to be honored and your teams have access only to resources allocated to their department.

This guide discusses the constructs of Clouds, Groups, Roles and Policies while also presenting an example use case for allocating resources and distributing access under these umbrellas. We'll end up with a permissions structure represented by the diagram below and step through each part of the implementation process.

.. image:: /images/integration_guides/perms_guide/0permsDiagram.png

Clouds
------

Clouds have broad meaning in |morpheus| and can be integrations into public clouds, private clouds, or bare metal servers. You can read more about Clouds in |morpheus| Docs `here <https://docs.morpheusdata.com/en/latest/infrastructure/clouds/clouds.html>_`.

In our example case, the organization has an Azure account and three separate departmental projects consolidated under separate resource groups. The |morpheus| integration with Azure public cloud allows users to scope the Cloud to one specific resource group, if desired. We will do so in this case because it will allow us to restrict our users to the appropriate Azure resource groups in a later step. In the screenshot below, note how I am scoping the |morpheus| Azure Cloud to a specific resource group when adding or editing the Cloud. This process will be repeated two additional times to create the three |morpheus| Clouds we need. Complete details on integrating |morpheus| with Azure public cloud are `here <https://docs.morpheusdata.com/en/latest/integration_guides/Clouds/azure/azure.html>_` in |morpheus| Docs.

.. image:: /images/integration_guides/perms_guide/1configCloud.png
:width: 50%

Groups
------

`Groups <https://docs.morpheusdata.com/en/latest/infrastructure/groups/groups.html>_ in |morpheus| allow administrators to determine which Clouds their users have access to. Part of defining a Role, which we'll see in the next section, is selecting which Groups are associated with the Role. One or multiple Clouds are added to each Group and passed to users through their assigned Roles.

When creating a Cloud, it must be added to a Group. Additionally, Clouds can be added to a Group at any time from the Clouds tab on the Group detail page (Infrastructure > Groups > Specific Group). In the example case diagrammed above, one Cloud (Azure cloud scoped to a specific resource group) is associated with each Group but often Groups will contain many Clouds. In the screenshot below, I am adding an Azure Cloud to a Group that is currently empty.

.. image:: /images/integration_guides/perms_guide/2addCloudToGroup.png

Roles
-----

|morpheus| Roles determine user access to many things, including application features, Groups, configured Instance Types, configured Blueprints, Personas, and Catalog Item configurations for the Service Catalog Persona. It's important to note that a user can have multiple Roles and will take the most permissive rights across all of these Roles. In many cases, this greatly simplifies Role configuration for administrators as it prevents the need to create highly-specific individual Roles that can suit every case. To illustrate this for our example case here, I will create a set of Roles to handle Group access for my users and another set of Roles to give access to the correct feature permissions.

For this example case, I'll start by creating one Role for each of the three Groups we created in the previous step. By default, a new Role will have all feature permissions set to "None" as shown below meaning we can skip directly to the Group Access tab.

.. image:: /images/integration_guides/perms_guide/3roleFeatureAccess.png

On the Group Access tab, I will toggle the Global Access setting to Custom and give access only to one Group as shown in the next image. By doing this for each of our Groups created in the last section, we can easily control Group access for each user by applying one or more of our Group Roles to their user which we will do in the next section.

.. image:: /images/integration_guides/perms_guide/4roleGroupAccess.png

In addition to Roles for handling Group access, we need additional Role sets which will control our feature access. For example, we might have highly permissive feature access for administrators and more restrictive ones for developers or other users who have specific responsibilities requiring access to just a few specific areas of the UI.

Users
-----

With the groundwork laid in the previous steps, we can easily configure permissions for any user accounts we might add to |morpheus|. In the screenshot below, I'm adding a user account for a developer at my organization. I've applied one Role to handle correct Group access for this user and I've applied the "Developer" role to give only the feature access needed for this user to carry out his or her responsibilities.

.. image:: /images/integration_guides/perms_guide/5newUser.png
:width: 50%

Policies
--------

One final consideration for this example case is policy application. |morpheus| enables administrators to place fine-grained governance scoped to specific users, Roles, Groups, Clouds, Tenants, or globally. You can read more about policies in |morpheus| docs `here <https://docs.morpheusdata.com/en/latest/administration/policies/policies.html>_` but we will also create some that apply to the example case discussed in this guide.

Policies are created from the Administration menu in the Policies section. In the screenshot below, I've created a new policy and chosen to scope it to a Group. In this case, I'm creating a maximum VMs policy but there are many other types which are listed in our documentation linked above.

.. image:: /images/integration_guides/perms_guide/6policies.png
:width: 50%
