Personas
========

Personas are alternate views in |morpheus| UI. A user's access to certain Personas is controlled by Role permissions. At present, there are two Persona types: Standard and Service Catalog. The Standard Persona is the typical default view. The Service Catalog Persona is a simplified view where users are presented with pre-configured Instance types and Blueprints to choose from based on their Role. The rest of this section goes through the use of the Service Catalog Persona and how administrators can curate the selection their users see in this area.

Configuring Persona Access
--------------------------

Access to Personas is controlled by a user's Role. Additionally, Persona access can be configured on the Tenant Role to set maximum Persona access for any user in the Tenant. By default, new Roles and Roles that existed prior to the creation of Personas will only have access to the Standard Persona. If desired, new Roles can be configured to have access to one or both Personas and existing Roles can be edited in the same way.

.. TIP:: It's recommended to set access to both Personas to "None" if you intend not to use Personas at all. Under this configuration, |morpheus| gives access only to the Standard Persona and hides the Persona selection menu from the user. New Roles and Roles that existed prior to creation of the Personas feature are pre-configured in this way.

Edit Persona access on a Role with the following steps:

#. Navigate to ``Administration > Roles``
#. Select the desired Role to edit
#. Go to the Personas tab
#. Allow access to one or both Personas as needed, changes are saved automatically

.. image:: /images/personas/1rolePerms.png

Configuring Catalog Item Access
-------------------------------

Within the Service Catalog Persona, users are presented with Catalog Items based on their User Role. Additionally, Catalog Item access can be set on the Tenant Role to restrict certain items from all users in the Tenant. By default, User Roles have no access to any catalog items (and no access to the Service Catalog Persona). When enabling Service Catalog Persona access for User Roles, you will also need to give access to some or all Catalog Items.

Configuring Global Access:

- **Full:** Gives access to all Catalog Items
- **Custom:** Gives access to individually-selected items from the list below
- **None:** No access is given to any Catalog Items

.. TIP:: When giving Custom access, be sure to set access on some of the individual catalog items to Full in order to reveal those items to the Role group.

Accessing Alternate Personas
----------------------------

Switch Personas by clicking on your name in the upper-right corner of the application window. If your Role gives you access to any additional Personas, they will be listed here.

.. image:: /images/personas/2switchPersona.png

.. include:: service_catalog.rst
