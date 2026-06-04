Invoice Details
===============

The Invoice Details view provides granular cost breakdowns for individual invoices with advanced grouping and tag-based filtering capabilities. From the invoice list (|OpCos| > Invoices), click into any invoice to access its detailed line item view.

Accessing Invoice Details
-------------------------

#. Navigate to |OpCos| > **Invoices**
#. Click on any invoice row to open the detail view

The detail view displays the invoice reference object (Cloud, Instance, Server, etc.), the billing period, and all associated line items.

Group By
--------

Invoice details support grouping line items by various dimensions to organize cost data for analysis:

- **None** — Display all line items in a flat list
- **Usage Type** — Group line items by their usage category (Compute, Storage, Network, etc.)
- **Usage Category** — Group by high-level cost category
- **Item** — Group by the individual resource or service item
- **Region** — Group line items by the cloud region where usage occurred
- **Availability Zone** — Group by specific availability zone
- **Tag** — Group by tag key/value combinations applied to the resources

Tag Grouping
^^^^^^^^^^^^

When **Tag** grouping is selected, line items are organized by their tag values. This enables:

- Viewing costs broken down by any tag applied to cloud resources
- Identifying cost attribution at a tag-granularity level
- Comparing tagged vs. untagged spend within a single invoice

To use tag grouping:

#. Open an invoice detail view
#. Select **Tag** from the Group By dropdown
#. Optionally filter to a specific tag key

Line items without the selected tag appear in an "Untagged" group.

Line Item Details
-----------------

Each line item in the invoice displays:

- **Item** — The specific service or resource generating the cost
- **Usage Type** — The category of usage (e.g., BoxUsage, DataTransfer, Requests)
- **Usage Category** — High-level cost category
- **Usage** — The quantity of usage consumed
- **Rate** — The per-unit rate applied
- **Cost** — The total cost for this line item
- **Region** — The cloud region (if applicable)
- **Availability Zone** — The specific AZ (if applicable)
- **Start/End Date** — The time period for the line item
- **Tags** — Any tags associated with the resource

Filtering
---------

The invoice detail view supports filtering to narrow the displayed line items:

- **Search** — Free-text search across line item descriptions
- **Usage Type** — Filter to a specific usage type
- **Date Range** — Filter line items by their effective dates

Exporting
---------

Invoice details can be exported for external analysis:

- Click :guilabel:`EXPORT` to download the invoice detail data as CSV
- Exported data includes all visible columns and respects current filters and grouping

.. NOTE:: Invoice details are available for all invoice types (Cloud, Instance, Server, Group, User, Volume, Container, Resource). The level of detail varies based on what cost data is available from the cloud provider.
