Wiki
====

The Morpheus Wiki is a tenant wide, RBAC controlled, audit-able Wiki that allows easy UI, API and CLI access to information, notes, config or any other data needed to be referenced or shared with others. Wiki pages encompass individual Clouds, Groups, Servers, Instances, Clusters, and other pages can be manually created. Wiki pages from resources are accessible from ``Operations - Wiki`` or in within individual resource detail pages in the Wiki tab.

- Main Wiki section is at ``Operations - Wiki``
- Wiki tabs are on Clouds, Groups, Instances, Hosts, VM's, Bare Metal, and Clusters.
- Additional Wiki Pages and Categories can be created from ``Operations - Wiki``.
- When a Wiki tab is populated, a Page is automatically added and accessible to ``Operations - Wiki``.
- Wiki's are per Tenant. There is no multi-tenant access to Wikis.
- The Wiki is accessible from the UI, CLI and API.
- RBAC controlled via the Operations: Wiki User and Tenant Role permission (None, Read and Full).
- Page updates contain Updated by User and Date stamps.
- Wiki pages can be searched from ``/operations/wiki`` or navigated from ``/operations/wiki-page/page-index``.

.. NOTE:: The Wiki replaces Notes. Notes are automatically migrated to corresponding Wiki pages when upgrading |morpheus| to 4.0.
