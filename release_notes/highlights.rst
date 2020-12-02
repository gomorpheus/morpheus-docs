|morphver| Highlights
=====================

Service Catalog Persona Improvements
------------------------------------

The |morpheus| version 5.0.0 beta introduced Personas, which are a new approach for optimizing and simplifying self-service for targeted audiences. The first Persona to ship is `Service Catalog <https://docs.morpheusdata.com/en/5.2.0/personas/personas.html#service-catalog-persona>`_, which sees additional improvements in the 5.2.0 LTS release.

- Make |morpheus| Operational Workflows available for order from the Service Catalog and run them against selected targets
- With added API/CLI support, work with Personas, create and manage Catalog Items, and make selections from the catalog through |morpheus| API and CLI tools
- Inventory list view now includes much greater detail about each inventory item
- Categorize items items under selected headers for enhanced discoverability as the catalog grows
- With the added quantity selector, order additional copies of items in your cart without creating duplicate selections

.. image:: /images/releases/520/catalogWorkflow.png


ServiceNow Integration Improvements
-----------------------------------

|morpheus| 5.2.0 brings improvements to the ServiceNow integration, including upgrades to incident surfacing, integration with service catalog items, and more.

- "|morpheus| Incident” alerts are now more insightful including links to the related Morpheus incident or check, severity information, and other details about the failing check
- Provision Service Catalog Items through the Morpheus ServiceNow plugin
- Added the capability to identify a MID server once on the properties page rather than setting it individually for each call
- Pricing data is now available to the ServiceNow plugin when ordering Service Catalog items. This is made available on the XML as a monthly price, users would have to modify the form UI to surface this information

Hide Blueprint fields
---------------------

Administrators have been able to lock Blueprint fields to restrict editing during App provisioning for a long time. Fields can now be hidden from view completely by toggling the lock/unlock icon to the hidden setting. When users provision Apps based on this Blueprint, they will not see hidden fields at all. This gives administrators additional flexibility to mask unneeded complexity from users.

.. image:: /images/releases/520/blueprint.png
