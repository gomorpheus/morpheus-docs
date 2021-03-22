.. _plans:

Plans & Pricing
===============

Overview
--------

The Plans & Pricing page displays a list of all of your available service plans. Plans provide a means to set predefined tiers on memory, storage, cores, and CPU. From the service plans page you will be able to create, edit and delete service plans, as well as review basic plan details. Plans are listed along with the type, associated clouds and region codes, and number of associated price sets. A default set of Service Plans are included with |morpheus| but most users will want to create their own as well. Price tables can also be applied to these plans so estimated costs per virtual machine, load balancer, snapshot, and more can be tracked. Customer price conversions can also be configured.

Service Plans
-------------

Create Service Plan
^^^^^^^^^^^^^^^^^^^

|morpheus| offers a few distinct types of service plans, each with different data fields to track and valid price types which can be associated. Price Sets can be added to the plan at the time it's created so often it makes sense to create the Prices and associate them with Price Sets before creating the plan. Additional instructions for creating Prices and Price Sets are in the next section. With the Price Sets ready, continue with the instructions below to create Price Plans of various types.

#. Navigate to Administration > Plans & Pricing
#. Click the :guilabel:`+ ADD` dropdown and select a Price Plan type
#. Configure details on the Service Plan on the General tab, the data tracked will depend on the Plan type selected
#. On the Price Sets tab, associate all relevant Price Sets with the Plan. Available Price Sets are automatically filtered to show only those which are relevant for the Plan type you've selected
#. Click :guilabel:`SAVE CHANGES`

Edit Service Plan
^^^^^^^^^^^^^^^^^

By default, these options are fixed sizes but can be configured for dynamic sizing. A service plan can be configured to allow a custom user entry for memory, storage, or cpu. To configure this, simply edit an existing Service Plan. These all can be easily managed from the ``Admin -> Service Plans`` section.

To edit service plan:

#. Select the Administration link in the navigation bar
#. Select the Plans & Pricing link in the sub navigation bar
#. Click the ACTIONS dropdown in the row for the Price Plan you wish to edit
#. Click EDIT
#. After making changes, click the :guilabel:`SAVE CHANGES` button to save

Delete Service Plan
^^^^^^^^^^^^^^^^^^^

To delete a service plan

#. Select the Administration link in the navigation bar
#. Select the Plans & Pricing link in the sub navigation bar
#. Click the ACTIONS dropdown in the row for the Price Plan you wish to delete
#. Click REMOVE
#. When the warning pop-up appears, confirm that you wish to delete the Plan

.. include:: prices.rst
