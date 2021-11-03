.. _plans:

Plans & Pricing
===============

Overview
--------

Plans & Pricing is where Plans, Prices Sets and Prices are managed. Prices are added to Prices Sets, and Price Sets are added to Plans. Plans include Service Plans, Load Balancer Price Plans, Virtual Image Prices Plans and Snapshot Price Plans. Price sets can be agnostic and available for any Plan, or specific to a Region Code, Cloud or a specific Resource Pool. Prices are configured per Price Type and can be added to Price Set configurations that support the Price Type. Master Tenant Prices can apply to all Tenants or be assigned to a single Tenant.

A set of Service Plans are seeded by |morpheus| for private cloud provision types as well as some public clouds. Additional Plans and Prices are synced in for other public clouds when the corresponding cloud types are added to an appliance. Users can create new Service Plans or edit the system seeded Service Plans for Private Cloud types. Service Plans configurations cannot be created or edited for Public Cloud provision types.

Plans
-----

Plans types include Service Plans and Price Plans. Service Plans determine the memory, storage and cores configuration during provisioning and reconfigure.

Service Plans
^^^^^^^^^^^^^

A set of Service Plans are seeded by |morpheus| for private cloud provision types as well as some public clouds. Additional Plans and Prices are synced in for other public clouds when the corresponding cloud types are added to an appliance. Users can create new Service Plans or edit the system-seeded Service Plans for Private Cloud types. Service Plans configurations cannot be created or edited for Public Cloud provision types.

.. _Service Plan Configuration Options:

Service Plan Configuration
``````````````````````````

:NAME: The name of the Service Plan in |morpheus|
:ACTIVE: Inactive Service Plans are not available for selection during provisioning or reconfigure, and new discovered records will not be associated with deactivated Plans. Resources attached to active Plans will continue to be associated if the Plan is deactivated
:CODE: A unique identifier for use in |morpheus| API and CLI
:DISPLAY ORDER: Configures the order in which plans are displayed relative to other plans associated with the same provision type
:PROVISION TYPE: Determines the resource Provision Type the Service Plan is available for when provisioning, reconfigures and discovery association.
:REGION CODE: (optional) Limits availability of the Service Plan to Clouds with the specified Region Code
:STORAGE: The default value of the Root volume (in MB or GB)
- :CUSTOMIZE ROOT VOLUME: Allows the Root Volume size value to be customized during provisioning or reconfigure. Custom Range limits apply.
- :CUSTOMIZE EXTRA VOLUMES: Allows the size of additional Volumes to be customized during provisioning or reconfigure. Custom Range limits apply.
- :ADD VOLUMES: Allows additional volumes to be added during provisioning or reconfigure.
       
:MEMORY: The amount of memory included with the plan (in MB or GB), when the CUSTOM MEMORY box is marked users can select a memory amount within the custom range configured below
   - :CUSTOM MEMORY: Allows the Memory value to be customized during provisioning or reconfigure. Custom Range limits apply.
:CORE COUNT: The number of virtual CPU cores associated with the plan, when the CUSTOM CORES box is marked users can select a number of cores within the custom range configured below
   - :CUSTOM CORES: Allows the CORE COUNT value to be customized during provisioning or reconfigure. Custom Range limits apply.
:CORES PER SOCKET: Determines core distribution across sockets. CORES PER SOCKET cannot be larger than CORE COUNT, and CORE COUNT must be divisible by CORES PER SOCKET. For example 4 CORES with 2 CORES PER SOCKET means 2 sockets would have 2 cores each assigned. 4 CORES with 1 CORE PER SOCKET would have 4 sockets with 1 core each assigned, and 4 CORES with 4 CORES PER SOCKET would have 1 socket with 4 cores assigned.
:CUSTOM RANGES: 
- :STORAGE: Min and Max allowed values allowed when **CUSTOMIZE ROOT VOLUME** or **CUSTOMIZE EXTRA VOLUMES** is enabled. Units inherited from the Plans **STORAGE: GB/MB** setting.
- :MEMORY: Min and Max allowed values allowed when **CUSTOM MEMORY** is enabled. Units inherited from the Plans **MEMORY GB/MB** setting.
- :CORES: Min and Max allowed values allowed when **CUSTOM CORES** is enabled.

:PRICE SETS: In the Price Sets tab, associate Price Sets with the Plan. See :ref:`Adding Price Sets to Plans`

.. TIP:: Custom Range storage and memory values units (GB/MB) are inherited from the :STORAGE:: and :MEMORY:: GB/MB settings in the same Plan. For example, if :STORAGE: is configured for for 40 GB, a custom range for Storage would also be in GB.

Create Service Plan
```````````````````

|morpheus| offers a few distinct types of service plans, each with different data fields to track and valid price types which can be associated. Price Sets can be added to the plan at the time it's created so often it makes sense to create the Prices and associate them with Price Sets before creating the plan. Additional instructions for creating Prices and Price Sets are in the next section. With the Price Sets ready, continue with the instructions below to create Price Plans of various types.

#. Navigate to `Administration > Plans & Pricing` (``/admin/service-plans``)
#. Click the :guilabel:`+ ADD` dropdown and select a Price Plan type
#. Configure details on the Service Plan on the General tab, the data tracked will depend on the Plan type selected.
#. On the Price Sets tab, associate all relevant Price Sets with the Plan. See :ref:`Service Plan Configuration Options`
#. Click :guilabel:`SAVE CHANGES`

.. _Adding Price Sets to Plans:

Add Price Set(s) to Plan
````````````````````````

#. Select a Price Unit to list available Price Sets within that Price Unit. Available Price Sets are filtered to show only those which are relevant for the Plan type you've selected
#. Select a Price Set from the list and click :guilabel:`+ ADD`
#. Add additional Price Sets if desired (multiple Price Sets can be associated with a Plan)
#. Added Price sets can be remove from a Plan by clicking the |trash| icon
#. Once all Price Sets have been added, select :guilabel:`SAVE CHANGES`

   .. tip:: :guilabel:`+ADD` must be selected after selecting a Price Set or it will not be added to a Plan

Service Plan Permissions
````````````````````````

Group and Tenant Access permissions determine availability of a Service Plan.

- Group Access determines what Groups the Service Plan will be available in for Provisioning and Reconfigure.
- Group Access settings only apply to the Tenant they are configured in, as Groups are not multi-tenant.
- For multi-tenant environments, the |master tenant| can set Tenant Permissions to determine if the Service Plan is available to all Tenants (public visibility) or assign the Service Plan to one or multiple Tenants.

Removing Plans
``````````````

Plans can be removed by selecting **ACTIONS: ▼** on a Plan and then selecting :Remove: from the Actions menu. Removing a Plan makes it no longer visible, however it does not hard delete the Plan as the record must remain for existing associations usage and price tracking. Synced Plans should be deactivated rather than removed.

|

Load Balancer Price Plans
^^^^^^^^^^^^^^^^^^^^^^^^^

Load Balancer Price Plans configure pricing for Load Balancers and Load Balancer Virtual Servers.

Load Balancer Price Plan Configuration:

:NAME: The name of the Load Balancer Price Plan in |morpheus|
:ACTIVE: When Active, Prices in Price Sets added to the Price Plan will apply to associated resources per Price and Price Set configuration.
:CODE:: A unique identifier for use in |morpheus| API and CLI
:LOAD BALANCER TYPE: Select from the available Load Balancer Types to associate the Price Plan with
:PRICE SETS: In the Price Sets tab, associate Price Sets with the Plan. See :ref:`Adding Price Sets to Plans`

Virtual Image Price Plans
^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual Image Price Plans configure pricing for Virtual Images. Pricing is associated per Price and Price Set configurations, but in general applies to Images with location records in the Price Plans specified :CLOUD TYPE:. Virtual Image Prices Plans are for setting pricing for Virtual Image storage, not for adding pricing to resources that use
Virtual Images associated with Virtual Image Price Plans. Virtual Image Price Plans do not apply to uploaded Virtual Images that have not been copied to a location in the specified :CLOUD TYPE: yet.

Virtual Image Price Plan Configuration:

:NAME: The name of the Virtual Image Price Plan in |morpheus|
:ACTIVE: When Active, Prices in Price Sets added to the Price Plan will apply to associated resources per Price and Price Set configuration.
:CODE:: A unique identifier for use in |morpheus| API and CLI
:CLOUD TYPE: Virtual Image Pricing applies to Virtual Images with location records in the specified **CLOUD TYPE**.
:PRICE SETS: In the Price Sets tab, associate Price Sets with the Plan. See :ref:`Adding Price Sets to Plans`

Snapshot Price Plans
^^^^^^^^^^^^^^^^^^^^

Snapshot Price Plan Configuration:

:NAME: The name of the Snapshot Price Plan in |morpheus|
:ACTIVE: When Active, Prices in Price Sets added to the Price Plan will apply to associated resources per Price and Price Set configuration.
:CODE:: A unique identifier for use in |morpheus| API and CLI
:CLOUD TYPE: Snapshot Pricing applies to Snapshots that exist in the specified **CLOUD TYPE**.
:PRICE SETS: In the Price Sets tab, associate Price Sets with the Plan. See :ref:`Adding Price Sets to Plans`

.. include:: prices.rst

.. |trash| unicode:: 0x0001F5D1 .. TRASH ICON

.. |downarrow| unicode:: ▼ .. DOWN ARROW


..
  https://apidocs.morpheusdata.com/#service-plans
