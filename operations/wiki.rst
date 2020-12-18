.. _wiki:

Wiki
====

The Morpheus Wiki is a tenant-wide, RBAC-controlled, auditable Wiki that allows easy UI, API and CLI access to information, notes, configurations or any other data needed to be referenced or shared with others. Wiki pages can be created directly from the Wiki tab of the detail page for various resource types, including Clouds, Groups, Servers, Instances, Clusters, and Self-Service Persona Catalog Items. Wiki pages created this way are automatically categorized under the appropriate resource type. Additional Wiki pages and custom categories can be created when viewing the whole Wiki at ``Operations > Wiki``. Here you will also see the complete Wiki, including pages created on various object detail pages which are categorized appropriately.

Highlights
----------

- Main Wiki section is at ``Operations > Wiki``
- Wiki tabs are on Clouds, Groups, Instances, Hosts, VMs, Bare Metal, and Clusters detail pages
- Additional Wiki Pages and Categories can be created from ``Operations > Wiki``
- When a Wiki tab is populated, a Page is automatically added and accessible at ``Operations > Wiki``
- One Wiki is created per Tenant. There is no multi-tenant access to Wikis
- The Wiki is accessible from the UI, CLI and API.
- Wiki access is RBAC-controlled via the Operations: Wiki permission in User and Tenant Roles (None, Read and Full)
- Page updates are stamped with the "Last Updated By" user and the time the edit was made
- Wiki pages can be searched from ``/operations/wiki`` or navigated from ``/operations/wiki-page/page-index``
- All wiki pages are encrypted using AES 256-bit encryption
- Wiki pages use Flexmark for Markdown. Annotate your Wiki pages with headers, text styling, code blocks, hyperlinks, and more as needed
- Create a new page with title "Home" to replace the default Wiki landing page that ships with |morpheus|

.. NOTE:: The Wiki replaces Notes. Notes are automatically migrated to corresponding Wiki pages when upgrading |morpheus| to 4.0.0+.

The Wiki service ties into assets throughout the environment. Create pages for Instances, hosts, groups, clouds, and even clusters directly on their detail pages. Or, just create general notes pages in the centralized Wiki section in Markdown format.

Creating your first page is as simple as clicking the :guilabel:`Create Page` button. Write down some content, give the page a title, and click :guilabel:`SAVE`. The wiki will also keep track of who last edited a page and when. The beauty of this wiki is that its clean and easy to write down notes related to various parts of your application deployment or infrastructure without going to an external tool.

All wiki pages are encrypted using AES-256 bit encryption. Though we don't advise storing passwords in a wiki document (services like Cypher are for that), role-based access control also can properly restrict access to content related to Instances or hosts the user may not have access to.

To get started, simply create a page with the title Home. When that page is created, it will become the new default page for the Wiki and visible by all the users that have access to this section.
