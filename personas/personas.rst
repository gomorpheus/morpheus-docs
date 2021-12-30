Personas
========

Personas are alternate views in |morpheus| UI. A user's access to the various Personas is controlled by Role permissions. At present, there are three Persona types: Standard, Service Catalog, and Virtual Desktop. The Standard Persona is the typical default view. The Service Catalog Persona is a simplified view where users are presented with pre-configured Instance types, Blueprints, and Workflows to choose from based on their Role. The Virtual Desktop Persona allows administrators to grant user access to remote workstations and applications.

The rest of this section goes through the use of the Service Catalog Persona and Virtual Desktop Persona in greater detail, including how administrators can curate catalog item and virtual desktop selections for their users.

.. toctree::
      :glob:

      *

Configuring Persona Access
--------------------------

Access to Personas is controlled by a user's Role. Additionally, Persona access can be configured on the Tenant Role to set maximum Persona access for any user in the Tenant. By default, new Roles and Roles that existed prior to the creation of Personas will only have access to the Standard Persona. If desired, new Roles can be configured to have access to one or both Personas and existing Roles can be edited in the same way.

.. TIP:: It's recommended to set access to all Personas to "None" if you intend not to use Personas at all. Under this configuration, |morpheus| gives access only to the Standard Persona and hides the Persona selection menu from the user. New Roles and Roles that existed prior to creation of the Personas feature are pre-configured in this way.

Edit Persona access on a Role with the following steps:

#. Navigate to |AdmRol|
#. Select the desired Role to edit
#. Go to the Personas tab
#. Allow access to one or both Personas as needed, changes are saved automatically

.. image:: /images/personas/1rolePerms2.png

Accessing Alternate Personas
----------------------------

Switch Personas by clicking on your name in the upper-right corner of the application window. If your Role gives you access to any additional Personas, they will be listed here.

.. image:: /images/personas/2switchPersona2.png
  :width: 50%
