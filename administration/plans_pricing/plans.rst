.. _plans:

Plans & Pricing
===============

Overview
--------

Service Plans determine the amount of compute resources available to each Instance. When provisioning new Instances from |morpheus|, a plan is selected which determines the number of CPU cores, amount of memory and the amount of storage available to the associated machines. Additionally, when converting discovered instances in integrated clouds to |morpheus|-managed Instances, the user selects a plan which best fits the instance as it is currently configured. When Instances are reconfigured, a new plan may be selected which redefines the compute resources which should be available to the Instance.

Plans can be as specific or open-ended as the user would like, restricting the user to the resources defined in the plan or allowing the user to increase those amounts at provision time. Price sets are associated with plans, which is how |morpheus| can compute cost values even for Instances running in private, on-prem Clouds.

The Plans & Pricing section is where Plans, Prices Sets and Prices are managed. These concepts are associated with each other in the following way: Prices are added to Prices Sets, and Price Sets are added to Plans. Plans include Service Plans, Load Balancer Price Plans, Virtual Image Prices Plans and Snapshot Price Plans. Price sets can be agnostic and available for any Plan, or specific to a Region Code, Cloud or even a specific Resource Pool. Prices are configured per Price Type and can be added to Price Set configurations that support the Price Type. Master Tenant Prices can apply to all Tenants or be assigned to a single Tenant.

A set of Service Plans are seeded by |morpheus| for private cloud provision types as well as some public clouds. Additional Plans and Prices are synced in for other public clouds when the corresponding cloud types are added to an appliance. Users can create new Service Plans or edit the system-seeded Service Plans for Private Cloud types. Service Plans configurations cannot be created or edited for Public Cloud provision types.

Plans
-----

Plans types include Service Plans and Price Plans. Service Plans determine the memory, storage and cores configuration during provisioning and reconfigure.

Service Plans
^^^^^^^^^^^^^

A set of Service Plans are seeded by |morpheus| for private cloud provision types as well as some public clouds. Additional Plans and Prices are synced in for other public clouds when the corresponding cloud types are added to an appliance. Users can create new Service Plans or edit the system-seeded Service Plans for Private Cloud types. Service Plans configurations cannot be created or edited for Public Cloud provision types.

.. _Service Plan Configuration Options:

Service Plan Configuration
``````````````````````````

.. NOTE:: Not all fields listed below are available for every provision type. After selecting the provision type, the correct fields for that type of Service Plan will be revealed. Not all fields are required to save a valid Service Plan

- **NAME:** The name of the Service Plan in |morpheus|
- **ACTIVE:** Inactive Service Plans are not available for selection during provisioning or reconfigure. New discovered records cannot be associated with deactivated Plans when converting to managed resources. Any resources attached to a Plan will continue to be associated if the Plan is later deactivated
- **CODE:** A unique identifier for use in |morpheus| API and CLI
- **DISPLAY ORDER:** Configures the order in which plans are displayed relative to other plans associated with the same provision type
- **PROVISION TYPE:** Determines the resource Provision Type this Service Plan is available for when provisioning, reconfiguring and converting discovered resources to managed
- **REGION CODE:** (Optional) Limits availability of the Service Plan to Clouds with the specified Region Code
- **STORAGE:** The default storage size of the root volume (in MB or GB)
- **CUSTOMIZE ROOT VOLUME:** Allows the root volume size to be customized during provisioning or reconfigure. Custom Range limits, if set, will apply
- **CUSTOMIZE EXTRA VOLUMES:** Allows the extra volume sizes to be customized during provisioning or reconfigure. Custom Range limits, if set, will apply
- **ADD VOLUMES:** Allows additional volumes to be added during provisioning or reconfigure
- **MEMORY:** The amount of memory included with the plan (in MB or GB)
- **CUSTOM MEMORY:** Allows the amount of memory to be customized during provisioning or reconfigure. Custom Range limits, if set, will apply
- **CORE COUNT:** The number of virtual CPU cores included with the plan
- **CUSTOM CORES:** Allows the number of virtual CPU cores to be customized during provisioning or reconfigure. Custom Range limits, if set, will apply
- **CORES PER SOCKET:** Determines core distribution across sockets. CORES PER SOCKET cannot be larger than CORE COUNT, and CORE COUNT must be divisible by CORES PER SOCKET. For example four CORES with two CORES PER SOCKET means two sockets would have two cores each assigned. Four CORES with one CORE PER SOCKET would have four sockets with one core each assigned, and four CORES with four CORES PER SOCKET would have one socket with four cores assigned
- **TOTAL STORAGE:** When custom storage is enabled for the plan, this sets a minimum and maximum total storage allowed (all disks combined)
- **PER DISK SIZE:** When custom storage is enabled for the plan, this sets the minimum and maximum storage for each disk
- **CUSTOM MEMORY RANGE:** The minimum and maximum allowed amount of memory for the Plan when CUSTOM MEMORY is enabled for the Plan
- **CUSTOM CORES RANGE:** The minimum and maximum allowed amount of virtual CPU cores for the Plan when CUSTOM CORES is enabled for the Plan
- **SOCKETS:** The minimum and maximum allowed sockets range for the Plan when CUSTOM CORES is enabled for the Plan
- **CORES PER SOCKET:** The minimum and maximum allowed cores per socket for the Plan when CUSTOM CORES is enabled for the Plan
- **PRICE SETS:** In the Price Sets tab, associate Price Sets with the Plan. See :ref:`Adding Price Sets to Plans`

.. TIP:: Custom Range storage and memory values units (GB/MB) are inherited from the :STORAGE:: and :MEMORY:: GB/MB settings in the same Plan. For example, if :STORAGE: is configured for for 40 GB, a custom range for Storage would also be in GB.

Create Service Plan
```````````````````

|morpheus| offers a few distinct types of service plans, each with different data fields to track and valid Price Set types which can be associated. For more on Service Plan configuration, see the preceding section.

Price Sets can be added to the Plan at creation time so often it makes sense to create the Prices and associate them with Price Sets before creating the Plan. Additional instructions for creating Prices and Price Sets are in the next section. With the Price Sets ready, continue with the instructions below to create Price Plans of various types.

#. Navigate to |AdmPla| (``/admin/service-plans``)
#. Click the :guilabel:`+ ADD` dropdown and select the appropriate Plan type
#. Configure details for the Plan on the General tab, the configuration options will depend on the Plan type. See the section above for a detailed description of each configuration option available for Service Plans
#. On the Price Sets tab, associate all relevant Price Sets with the Plan. The desired Price Sets must already exist. If needed, you may save the Plan at this point and come back to associate Price Sets later
#. Click :guilabel:`SAVE CHANGES`

.. _Adding Price Sets to Plans:

Add Price Set(s) to Plan
````````````````````````

#. Select a Price Unit to list available Price Sets which have the selected Price Unit. Available Price Sets are filtered to show only those which are relevant for the Plan type you've selected
#. Select a Price Set from the list and click :guilabel:`+ ADD`
#. Add additional Price Sets if desired (multiple Price Sets can be associated with a Plan)
#. Added Price sets can be removed from a Plan by clicking the |trash| icon
#. Once all Price Sets have been added, select :guilabel:`SAVE CHANGES`

.. tip:: The :guilabel:`+ADD` button must be clicked after selecting a Price Set or it will not be added to a Plan.

Service Plan Permissions
````````````````````````

Group and Tenant Access permissions determine availability of a Service Plan.

- Group Access determines what Groups the Service Plan will be available in for Provisioning and Reconfigure.
- Group Access settings only apply to the Tenant they are configured in, as Groups are not multi-tenant.
- For multi-tenant environments, the |master tenant| can set Tenant Permissions to determine if the Service Plan is available to all Tenants (public visibility) or assign the Service Plan to one or multiple Tenants.

Removing Plans
``````````````

Plans can be removed by navigating to the Service Plans list page (|AdmPlaPla|), opening the ACTIONS menu for a Plan, and then selecting "Remove". Removing a Plan makes it no longer visible, however, it does not hard delete the Plan as the record must remain for any existing associations' usage and price tracking. Synced Plans should be deactivated rather than removed.

|

Load Balancer Price Plans
^^^^^^^^^^^^^^^^^^^^^^^^^

Load Balancer Price Plans configure pricing for Load Balancers and Load Balancer Virtual Servers.

Load Balancer Price Plan Configuration:

- **NAME:** The name of the Load Balancer Price Plan in |morpheus|
- **ACTIVE:** When Active, Prices in Price Sets added to the Price Plan will apply to associated resources as configured
- **CODE:** A unique identifier for use in |morpheus| API and CLI
- **LOAD BALANCER TYPE:** Select the load balancer type the Price Plan should be associated with
- **PRICE SETS:** In the Price Sets tab, associate Price Sets with the Plan. Load Balancer Price Sets may be associated with Load Balancer-type and Load Balancer Virtual Server-type Prices. Fore more, see :ref:`Adding Price Sets to Plans`

Virtual Image Price Plans
^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual Image Price Plans configure pricing for Virtual Images. Pricing is associated per Price and Price Set configurations, but in general applies to Images with location records in the Price Plans specified Cloud type. Virtual Image Price Plans are for setting pricing for Virtual Image storage, not for adding pricing to resources that use Virtual Images associated with Virtual Image Price Plans. Virtual Image Price Plans do not apply to uploaded Virtual Images that have not been copied to a location in the specified Cloud type yet.

Virtual Image Price Plan Configuration:

- **NAME:** The name of the Virtual Image Price Plan in |morpheus|
- **ACTIVE:** When Active, Prices in Price Sets added to the Price Plan will apply to associated resources as configured
- **CODE:** A unique identifier for use in |morpheus| API and CLI
- **CLOUD TYPE:** Virtual Image Pricing applies to Virtual Images with location records in the specified Cloud type
- **PRICE SETS:** In the Price Sets tab, associate Price Sets with the Plan. Virtual Image Price Sets may be associated with Storage-type Prices. Fore more, see :ref:`Adding Price Sets to Plans`

Snapshot Price Plans
^^^^^^^^^^^^^^^^^^^^

Snapshot Price Plan Configuration:

- **NAME:** The name of the Snapshot Price Plan in |morpheus|
- **ACTIVE:** When Active, Prices in Price Sets added to the Price Plan will apply to associated resources as configured
- **CODE:** A unique identifier for use in |morpheus| API and CLI
- **CLOUD TYPE:** Snapshot Pricing applies to Snapshots with location records in the specified Cloud type
- **PRICE SETS:** In the Price Sets tab, associate Price Sets with the Plan. Snapshot Price Sets must have at least one Storage-type Price but may also have Datastore-type Prices. Fore more, see :ref:`Adding Price Sets to Plans`

.. include:: prices.rst

..
  https://apidocs.morpheusdata.com/#service-plans
