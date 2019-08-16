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
- All wiki pages are encrypted using AES-256 bit encryption.

.. NOTE:: The Wiki replaces Notes. Notes are automatically migrated to corresponding Wiki pages when upgrading |morpheus| to 4.0.

The Wiki service ties into assets throughout the environment. Create pages for Instances, hosts, groups, clouds, and even clusters directly on their detail pages. Or, just create general notes pages in the centralized Wiki section in Markdown format.

Creating your first page is as simple as clicking the Create Page button. Write down some content, give the page a title, and click the save button. The wiki will also keep track of who last edited a page and when. The beauty of this wiki is its clean and easy to write down notes related to various parts of your application deployment or infrastructure without going to an external tool.

All wiki pages are encrypted using AES-256 bit encryption. Though we don't advise storing passwords in a wiki document (theres services like Cypher for that), role based access control also can properly restrict access to content related to instances or hosts the user may not have access to.

To get started, simply create a page with the title Home. When that page is created, it will become the new default page for the Wiki and visible by all the users that have access to this section.
