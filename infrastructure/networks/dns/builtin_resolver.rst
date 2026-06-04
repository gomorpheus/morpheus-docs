.. _builtin_dns_resolver:

Built-in DNS Resolver
=====================

Overview
--------

|morpheus| includes a built-in DNS resolver that provides internal DNS management capabilities without requiring an external DNS server. The built-in resolver supports full DNS record type management and can serve as the primary DNS for |morpheus|-managed infrastructure or as a complementary service alongside external DNS.

The built-in resolver is configured as an internal DNS integration type and supports the complete set of standard DNS record types.

Supported Record Types
-----------------------

The |morpheus| built-in DNS resolver supports the following record types:

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Record Type
     - Description
   * - **A**
     - Maps a hostname to an IPv4 address
   * - **AAAA**
     - Maps a hostname to an IPv6 address
   * - **CNAME**
     - Creates an alias pointing to another hostname
   * - **MX**
     - Specifies mail exchange servers with priority values
   * - **NS**
     - Delegates a DNS zone to authoritative name servers
   * - **PTR**
     - Maps an IP address to a hostname (reverse DNS)
   * - **TXT**
     - Stores arbitrary text data (SPF, DKIM, verification)
   * - **SRV**
     - Specifies service location (host, port, priority, weight)
   * - **SOA**
     - Start of Authority — defines zone parameters (serial, refresh, retry, expire, TTL)
   * - **DNAME**
     - Delegation name — redirects an entire subtree of the domain name tree
   * - **TSIG**
     - Transaction Signature — authenticates DNS updates and zone transfers

Configuring the Built-in Resolver
----------------------------------

To enable and configure the built-in DNS resolver:

#. Navigate to Infrastructure > Network > Services
#. Click :guilabel:`+ ADD`
#. Select **Morpheus DNS** as the provider type
#. Configure:

   - **NAME:** Name for the internal DNS service
   - **DOMAIN:** Default domain suffix for managed records

#. Click :guilabel:`SAVE`

Managing DNS Zones
------------------

Creating a Zone
^^^^^^^^^^^^^^^

#. Navigate to Infrastructure > Network > Domains
#. Click :guilabel:`+ ADD`
#. Configure the zone:

   - **NAME:** Zone name (e.g., ``internal.example.com``)
   - **TYPE:** Forward or Reverse lookup zone
   - **DNS SERVICE:** Select the built-in resolver integration
   - **SOA RECORD:** Automatically created with defaults:

     - **Primary NS:** |morpheus| appliance hostname
     - **Admin Email:** ``admin@<zone-name>``
     - **Serial:** Auto-incremented
     - **Refresh:** 3600 seconds
     - **Retry:** 600 seconds
     - **Expire:** 604800 seconds
     - **Minimum TTL:** 300 seconds

#. Click :guilabel:`SAVE`

Managing Records
^^^^^^^^^^^^^^^^

Adding Records
""""""""""""""

#. Navigate to Infrastructure > Network > Domains
#. Select the target domain
#. Click :guilabel:`+ ADD RECORD`
#. Select the record type and complete the fields:

   **A Record:**

   - **HOSTNAME:** Record name (e.g., ``webserver01``)
   - **IP ADDRESS:** IPv4 address
   - **TTL:** Time to live in seconds (default: 300)

   **MX Record:**

   - **HOSTNAME:** Record name (typically ``@`` for zone apex)
   - **MAIL SERVER:** FQDN of the mail server
   - **PRIORITY:** Numeric priority (lower = higher priority)
   - **TTL:** Time to live

   **NS Record:**

   - **HOSTNAME:** Subdomain being delegated (or ``@`` for zone)
   - **NAME SERVER:** FQDN of the authoritative name server
   - **TTL:** Time to live

   **PTR Record:**

   - **IP ADDRESS:** The IP address (in reverse zone format)
   - **HOSTNAME:** FQDN the IP resolves to
   - **TTL:** Time to live

   **SRV Record:**

   - **SERVICE:** Service name (e.g., ``_sip._tcp``)
   - **TARGET:** FQDN of the service host
   - **PORT:** Service port number
   - **PRIORITY:** Priority value
   - **WEIGHT:** Weight for load balancing between same-priority records
   - **TTL:** Time to live

   **DNAME Record:**

   - **HOSTNAME:** Source subtree name
   - **TARGET:** Destination subtree name
   - **TTL:** Time to live

   **TSIG Record:**

   - **KEY NAME:** TSIG key identifier
   - **ALGORITHM:** HMAC algorithm (hmac-sha256 recommended)
   - **SECRET:** Base64-encoded shared secret

#. Click :guilabel:`SAVE`

Editing and Deleting Records
"""""""""""""""""""""""""""""

- To edit a record, click the pencil icon on the record row
- To delete a record, click the trash icon on the record row

Provisioning Integration
-------------------------

The built-in DNS resolver integrates with the |morpheus| provisioning workflow:

- **Automatic A Record Creation:** When an Instance is provisioned with an IP assignment, an A record is created in the associated domain
- **PTR Record Creation:** If a reverse zone exists for the IP range, a PTR record is automatically created
- **Record Cleanup:** DNS records are automatically removed when Instances are terminated
- **Naming Policy Integration:** DNS records follow configured naming policies for consistent naming

To enable automatic DNS for provisioning:

#. Associate a domain with the built-in resolver in Infrastructure > Network > Domains
#. On the Cloud or Network configuration, select the domain for DNS assignment
#. Configure naming policies as needed (Administration > Provisioning > Settings)

SOA Record Management
---------------------

The SOA record for each zone is automatically managed:

- **Serial Number:** Auto-incremented on each zone change (YYYYMMDDNN format)
- **Refresh Interval:** How often secondary servers check for updates
- **Retry Interval:** How long secondary servers wait before retrying after a failed refresh
- **Expire Time:** How long secondary servers serve data without a successful refresh
- **Minimum TTL:** Default TTL for negative caching (NXDOMAIN responses)

SOA parameters can be edited on the domain detail page.

TSIG Authentication
-------------------

TSIG (Transaction Signature) provides authentication for DNS operations:

- **Zone Transfers:** Authenticate AXFR/IXFR requests between DNS servers
- **Dynamic Updates:** Verify the identity of clients sending DNS updates
- **Algorithm Support:** HMAC-MD5, HMAC-SHA1, HMAC-SHA256, HMAC-SHA384, HMAC-SHA512

To configure TSIG:

#. Create a TSIG key record in the zone
#. Configure both parties (sender and receiver) with the same key name, algorithm, and secret
#. DNS operations between authenticated parties will include TSIG signatures

Limitations
-----------

The built-in DNS resolver is designed for internal use and has the following considerations:

- Not intended as an internet-facing authoritative DNS server
- Zone transfers to external secondary servers require network accessibility
- Query volume should be appropriate for the |morpheus| appliance resources
- For production internet-facing DNS, integrate with dedicated DNS infrastructure (Route 53, PowerDNS, etc.)
