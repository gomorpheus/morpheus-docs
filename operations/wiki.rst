.. _wiki:

Wiki
====

The Morpheus Wiki is a tenant-wide, RBAC-controlled, auditable Wiki that allows easy UI, API and CLI access to information, notes, configurations or any other data needed to be referenced or shared with others. Wiki pages can be created directly from the Wiki tab of the detail page for various resource types, including Clouds, Groups, Servers, Instances, Clusters, and Self-Service Persona Catalog Items. Wiki pages created this way are automatically categorized under the appropriate resource type. Additional Wiki pages and custom categories can be created when viewing the whole Wiki at ``Operations > Wiki``. Here you will also see the complete Wiki, including pages created on various object detail pages which are categorized appropriately.

.. image:: /images/operations/wikihome.jpg

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

Creating Wikis
--------------

The Wiki service ties into assets throughout the environment. Create pages for Instances, hosts, groups, Clouds, and even clusters directly on their detail pages (see the Wiki tab). Users may also just create general notes pages in the centralized Wiki section (|OpeWik|)in Markdown format.

Creating your first page is as simple as clicking the :guilabel:`Create Page` button from the Wiki home page (|OpeWik|). Write down some content, give the page a title, and click :guilabel:`SAVE`. The Wiki will also keep track of who last edited a page and when. The beauty of this Wiki is that it's clean and easy to write down notes related to various parts of your application deployment or infrastructure without going to an external tool. Many |morpheus| constructs, such as Instances, hosts, and more, also have their own Wiki page. Navigate to the detail page for the selected construct, open the Wiki tab, and click :guilabel:`EDIT` to add content.

.. IMPORTANT:: All wiki pages are encrypted using AES-256 bit encryption. Though we don't advise storing passwords in a Wiki document (services like Cypher are for that), role-based access control also can properly restrict access to content related to Instances or hosts which the user may not have access to.

.. image:: /images/operations/wikidetail.png

Hosting Images
--------------

It's possible to add images to your Wiki pages and images can be sourced from the Internet, a Cloud storage bucket (like an AWS S3 Bucket), or even from files stored to the |morpheus| appliance's local file system. Within your Wiki page markdown, add your image using the following syntax:

.. code-block:: markdown

  ![my alt text](https://myimage.com/image.jpg)

The text within the square brackets [] sets the HTML "alt" description for the image and the URL within parentheses () is the "src" URL for the image. The |morpheus| `Archives <https://docs.morpheusdata.com/en/latest/tools/archives.html>`_ feature is a great resource for hosting images for use in Wiki. Archives can target cloud storage buckets or even file shares on the |morpheus| appliance local storage. |morpheus| generates an access URL for each file stored in Archives, simply target this URL in your markdown to show an image stored in |morpheus| Archives within your Wiki pages.
