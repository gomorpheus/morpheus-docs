.. _upgrading:

Upgrading
---------

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed. 

	
.. toctree::
   :maxdepth: 4

   upgrades/overview.rst
   upgrades/single/singlenode.rst
   upgrades/3node/overview.rst
   upgrades/fullha/overview.rst
