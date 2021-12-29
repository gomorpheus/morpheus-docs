.. _plans:

Plans & Pricing
===============

Overview
--------

<<<<<<< HEAD
The Plans & Pricing page displays a list of all of your available service plans. From the service plans page you will be able to Create, Edit, and Delete service plans, as well as review basic plan details. The list of plans displayed on this page displays the plan name, description, Instances layout, memory, storage, and cost, as well as an action column to edit and delete. A default set of Service Plans are created in |morpheus|. They provide a means to set predefined tiers on memory, storage, cores, and cpu. Price tables can also be applied to these so estimated cost per virtual machine can be tracked as well as pricing for customers.
=======
Service Plans determine the amount of compute resources available to each Instance. When provisioning new Instances from |morpheus|, a plan is selected which determines the number of CPU cores, amount of memory and the amount of storage available to the associated machines. Additionally, when converting discovered instances in integrated clouds to |morpheus|-managed Instances, the user selects a plan which best fits the instance as it is currently configured. When Instances are reconfigured, a new plan may be selected which redefines the compute resources which should be available to the Instance.

Plans can be as specific or open-ended as the user would like, restricting the user to the resources defined in the plan or allowing the user to increase those amounts at provision time. Price sets are associated with plans, which is how |morpheus| can compute cost values even for Instances running in private, on-prem Clouds.

The Plans & Pricing section is where Plans, Prices Sets and Prices are managed. These concepts are associated with each other in the following way: Prices are added to Prices Sets, and Price Sets are added to Plans. Plans include Service Plans, Load Balancer Price Plans, Virtual Image Prices Plans and Snapshot Price Plans. Price sets can be agnostic and available for any Plan, or specific to a Region Code, Cloud or even a specific Resource Pool. Prices are configured per Price Type and can be added to Price Set configurations that support the Price Type. Master Tenant Prices can apply to all Tenants or be assigned to a single Tenant.

A set of Service Plans are seeded by |morpheus| for private cloud provision types as well as some public clouds. Additional Plans and Prices are synced in for other public clouds when the corresponding cloud types are added to an appliance. Users can create new Service Plans or edit the system-seeded Service Plans for Private Cloud types. Service Plans configurations cannot be created or edited for Public Cloud provision types.

Plans
-----

Plans types include Service Plans and Price Plans. Service Plans determine the memory, storage and cores configuration during provisioning and reconfigure.
>>>>>>> 4cca5b2b... add more detail around plans and plan filtering

Service Plans
-------------

Create Service Plan
^^^^^^^^^^^^^^^^^^^

To create service plan

#. Select the Administration link in the navigation bar.
#. Select the Plans & Pricing link in the sub navigation bar.
#. Click the Create Service Plan button.

#. From the New Service Plan wizard, input:

   * Name
   * Code used as a unique identifier in the API and CLI.
   * Storage size in megabytes.
   * Memory size in megabytes.
   * Cost is internal cost of plan.
   * Price is what the service offering will be priced at.
   * Instance Types that will be associated with this plan.
   * Click the Save Changes button to save.

Edit Service Plan
^^^^^^^^^^^^^^^^^

By default, these options are fixed sizes but can be configured for dynamic sizing. A service plan can be configured to allow a custom user entry for memory, storage, or cpu. To configure this, simply edit an existing Service Plan. These all can be easily managed from the ``Admin -> Service Plans`` section.

To edit service plan:

#. Select the Administration link in the navigation bar.
#. Select the Plans & Pricing link in the sub navigation bar.
#. Click the Edit pencil icon on the row of the plan to edit.
#. Edit the following Edit Service Plan.
#. Click the Save Changes button to save.

Delete Service Plan
^^^^^^^^^^^^^^^^^^^

To delete a service plan

#. Select the Administration link in the navigation bar.
#. Select the Plans & Pricing link in the sub navigation bar.
#. Click the Delete trashcan icon on the row of the plan to delete.
#. Confirm

.. include:: prices.rst
