Plans & Pricing
===============

Overview
--------

The Plans & Pricing page displays a list of all of your available
service plans. From the service plans page you will be able to Create,
Edit, and Delete service plans, as well as review basic plan details.
The list of plans displayed on this page displays planName, Description,
Instances Layout, Memory, Storage, and Cost, as well as an action column
to edit and delete. A default set of Service Plans are created in
|morpheus| . They provide a means to set predefined tiers on memory,
storage, cores, and cpu. Price tables can also be applied to these so
estimated cost per virtual machine can be tracked as well as pricing for
customers.

Create Service Plan
-------------------

To create service plan

#. Select the Administration link in the navigation bar.
#. Select the Plans & Pricing link in the sub navigation bar.
#. Click the Create Service Plan button.

#. From the New Service Plan wizard, input:

   * Name
   * Code used as a unique identifier in the API and CLI. \*\*
   * Storage size in megabytes.
   * Memory size in megabytes.
   * Cost is internal cost of plan.
   * Price is what the service offering will be priced at.
   * Instance Types that will be associated with this plan.
   * Click the Save Changes button to save.

Edit Service Plan
-----------------

By default, these options are fixed sizes but can be configured for
dynamic sizing. A service plan can be configured to allow a custom user
entry for memory, storage, or cpu. To configure this, simply edit an
existing Service Plan. These all can be easily managed from the
``Admin -> Service Plans`` section.

To edit service plan:

#. Select the Administration link in the navigation bar.
#. Select the Plans & Pricing link in the sub navigation bar.
#. Click the Edit pencil icon on the row of the plan to edit.
#. Edit the following Edit Service Plan.
#. Click the Save Changes button to save.

Delete Service Plan
-------------------

To delete service plan


#. Select the Administration link in the navigation bar.
#. Select the Plans & Pricing link in the sub navigation bar.
#. Click the Delete trashcan icon on the row of the#  plan to delete.
#. Confirm

.. include:: price_sets.rst
.. include:: prices.rst
