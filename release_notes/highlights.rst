5.0.0 Highlights
================

Introducing Personas
--------------------

5.0.0 introduces Personas, a new approach to streamline, optimize and simplify targeted self-service across disciplines. Our first Persona is Service Catalog, a paradigm shift to self-service that removes the complexity of multi-cloud, multi-format, multi-service offerings and presents a simple RBAC Catalog with one-click ordering of any resource. The new Self Service tool allows Admins to easily create Catalog Items using existing wizards and specs that minimize or even eliminate end-user input. Personas are assigned using existing Roles and users can be give access to multiple Personas with quick access to each Persona added to the global nav.

- Personas further optimize interfaces and processes for target audiences.
- The Service Catalog Persona further simplifies self-service provisioning of any resource with minimum or even zero user input.
- Service Catalog users can add items to their cart and checkout with a few clicks, then access resource in the Service Catalog Dashboard or Inventory section.
- Admins can quickly create Catalog Items using familiar processes and existing configurations, exposing only the options they choose to end users.
- Instances and Blueprints/Apps are supported for Catalog Items in 5.0.0 with additional options coming, including Operational Workflows.
- Personas and Catalog Items utilize existing RBAC permissions and Policies. Users can easily switch between assigned Personas.

.. image:: /images/releases/500/morpheusCatalog500-1.gif

|

Morpheus Plugins
----------------

The Morpheus Core Plugin Library provides a common framework for extending and customizing Morpheus capabilities. This includes providing plugin extensions for adding various integrations such as Cloud Integrations, Service Level Integrations or Providers for things like DNS, IPAM, Config Management, UI Extensions, Etc. The Morpheus Plugin API is a Java based library that currently supports implementing providers of the following types:

- UI Extensions
- Task Types
- IPAM
- DNS
- Approvals
- Cypher Modules

Additional information will be accessible in the Morpheus Developer Portal.

|

Invoices UI
-----------

The new Invoices UI brings the existing powerful Invoices API <https://apidocs.morpheusdata.com/#invoices> to the UI

- View highly-granular costing data through Invoices
- Create and export Invoice views with custom filters and columns
- View Invoice summaries, historical Cost and Price charts, and individual Line Item details

.. image:: /images/releases/500/invoiceList.png

|

Enhanced Reports
----------------

Reporting capabilities have been expanding with a new interface, additional report types, and report scheduling.

- Schedule reports to be run at a specific point in time or on a specific recurring schedule
- Eight new report types added for additional costing and usage breakdowns
- New filtering options added for new and existing reports

.. image:: /images/releases/500/reportsHome.png
