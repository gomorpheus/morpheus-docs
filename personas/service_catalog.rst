Service Catalog Persona
=======================

The Service Catalog Persona presents a simplified catalog where users can select and deploy Instances or Blueprints with pre-defined configuration with just a few clicks and without presenting an overwhelming list of options.

Configuring Catalog Item Access
-------------------------------

Within the Service Catalog Persona, users are presented with Catalog Items based on their User Role. Additionally, Catalog Item access can be set on the Tenant Role to restrict certain items from all users in the Tenant. By default, User Roles have no access to any catalog items (and no access to the Service Catalog Persona). When enabling Service Catalog Persona access for User Roles, you will also need to give access to some or all Catalog Items.

Configuring Global Access:

- **Full:** Gives access to all Catalog Items
- **Custom:** Gives access to individually-selected items from the list below
- **None:** No access is given to any Catalog Items

.. TIP:: When giving Custom access, be sure to set access on some of the individual catalog items to Full in order to reveal those items to the Role group.

Dashboard
---------

The default page for the Service Catalog Persona is the Dashboard. The Dashboard shows a selection of featured catalog items, a listing of the last few items the user has ordered, and a selection from the user's inventory.

.. thumbnail:: /images/personas/3scDashboard.png

Catalog
-------

The catalog shows the complete list of pre-defined catalog items available to the user for provisioning. Catalog items are not created in the Service Catalog Persona. For more on creating catalog items, see the `Self Service section <https://docs.morpheusdata.com/en/latest/tools/self-service.html>`_ (Tools > Self Service) of |morpheus| docs.

.. thumbnail:: /images/personas/4scCatalog.png

Inventory
---------

The Inventory Page reveals the complete list of items which have been ordered by the user and provisioned. Users will only see their own items in this section.

.. thumbnail:: /images/personas/5scInventory.png

Inventory Detail
----------------

Access the detail page for an item in your inventory by clicking the View Details link. The page displayed will look very similar to an Instance or App detail page in the Standard Persona. Highly detailed information on the health of the Instance or App are shown here. We can also take actions against Instances such as running Tasks or Workflows, reconfiguring the Instance, controlling the power state, and more.

.. thumbnail:: /images/personas/6scDetail.png

Placing Orders
--------------

From the Catalog page, select the tile for your chosen item to see any custom options that may need to be set prior to provisioning.

.. thumbnail:: /images/personas/7catalogOrder.png

Once the item is in the cart, make any additional selections to complete the order. Once finished, proceed to the cart by clicking on the cart icon at the top of the application window. Click "Review Order". When reviewing your order, each selected item is listed along with its estimated cost. The total estimated cost for the entire order is also computed.

.. thumbnail:: /images/personas/8catalogCart.png

Once :guilabel:`PLACE ORDER` is clicked, the provisioning process will begin and the user is redirected back to the catalog page. Any new orders can be viewed in Inventory and additional details can be accessed through the Inventory item detail page.
