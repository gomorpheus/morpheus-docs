Catalog
=======

The Catalog presents a simplified self-service view where users can select and deploy Instances, Blueprints or Workflows with pre-defined configuration in just a few clicks and without presenting an overwhelming list of options. Selections are presented as tiles and users can add items to a cart as if shopping on an eCommerce website. For users who tend to provision regularly from a small selection of Instance Types and configurations, the catalog is an easier option compared with the much more detailed and option-rich Instance provisioning wizard.

Configuring Catalog Item Access
-------------------------------

Within the Catalog, users are presented with selections based on their User Role. Additionally, Catalog Item access can be set on the Tenant Role to restrict certain items from all users in the Tenant. By default, User Roles have no access to any catalog items. Thus, administrators will need to enable access to some Catalog Items in order for users to make use of this view.

Configuring Global Access:

- **Full:** Gives access to all Catalog Items
- **Custom:** Gives access to individually-selected items from the list below
- **None:** No access is given to any Catalog Items

.. TIP:: When giving Custom access, be sure to set access on some of the individual catalog items to Full in order to reveal those items to the Role group.

Catalog
-------

The catalog shows the complete list of pre-defined catalog items available to the user for provisioning. Catalog items are not created here, however. For more on creating catalog items, see the Catalog Items tab in the |morpheus| Library section (Library > Blueprints > Catalog Items).

.. thumbnail:: /images/personas/4scCatalog.png

Placing Orders
--------------

From the Catalog page, select the tile for your chosen item to see any custom options that may need to be set prior to provisioning.

.. thumbnail:: /images/personas/7catalogOrder.png

Once the item is in the cart, make any additional selections to complete the order. Once finished, proceed to the cart by clicking on the cart icon at the top of the application window. Click "Review Order". When reviewing your order, each selected item is listed along with its estimated cost. The total estimated cost for the entire order is also computed.

.. thumbnail:: /images/personas/8catalogCart.png

Once :guilabel:`PLACE ORDER` is clicked, the provisioning process will begin and the user is redirected back to the catalog page. Any new orders can be viewed in Inventory and additional details can be accessed through the Inventory item detail page.

.. include:: inventory.rst
