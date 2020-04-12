|morpheus| |morphver| Documentation
===================================

.. note:: Please review all :ref:`Release Notes` in depth before upgrading. |morpheus| Releases, well frequent, are never small. 
	
.. important:: 4.2.0 brings all of the new features and enhancements from the 4.1 Feature Branch to a LTS branch. Future versions of 4.2 will add additional capabilities, fixes, performance improvements and security enhancements to the existing feature set of 4.2.0, while net new Feature and changes to the platform will be added to the upcoming 4.3 Feature branch.

.. important:: Please be aware of the default security enhancements added to v4.1.2+ and assess potential impacts to your env, including agent installation and front end load balancers.  Starting in v4.1.2 (not new but worth mentioning again), the default |morphues| Nginx config removes support for incoming ``TLS v1.0 and v1.1`` connections. Please update source config to be compatible. If necessary, |morphues| can be configured to support older TLS versions via :ref:`morpheus.rb` config. 

.. important:: |morphver| requires Elasticsearch v7.x. Please refer to :ref:`upgrading` and `Elasticsearch Upgrade Documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ before installing or upgrading to |morphver| if your Appliance's Elasticsearch is external. As of 4.2.0, Ubuntu 14.04 is no longer supported, you must be running Ubuntu 16.04+.

.. important:: v3.6.0 or later required to upgrade to |morphver|. Upgrading from v3.6.x to v4.2.0+ contains upgrades to MySQL, RabbitMQ, and Elasticsearch. Please refer to Upgrade Requirements before upgrading. When upgrading from v3.6.x to v4.x, a database backup is recommended due to MySQL version upgrade.

.. note:: It is recommend to upgrade existing VM and Host Agents after upgrading to |morphver| for Automation tasks with large task outputs/results when executing over |morpheus| Agent Command Bus.

.. toctree::
   :maxdepth: 2
   :caption: Morpheus UI

   getting_started/getting_started
   provisioning/provisioning
   infrastructure/infrastructure
   administration/administration
   monitoring/monitoring
   logs/logs
   backups/backups
   operations/operations
   tools/tools
   integration_guides/integration_guides
   troubleshooting/troubleshooting

.. toctree::
   :maxdepth: 1
   :caption: Morpheus CLI

   CLI Documentation <https://github.com/gomorpheus/morpheus-cli/wiki>

.. toctree::
   :maxdepth: 1
   :caption: Morpheus API

   API Documentation <http://bertramdev.github.io/morpheus-apidoc/#introduction>

.. toctree::
   :maxdepth: 1
   :caption: Release Notes

   release_notes/current.rst
   release_notes/compatibility.rst
   release_notes/previousReleases.rst

.. toctree::
   :maxdepth: 1
   :caption: Resource Center

   Resource Center <https://www.morpheusdata.com/resource-center>
