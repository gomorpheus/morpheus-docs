Installing on Linux
---------------------------------------

The |morpheus| CLI is a ruby based CLI that provides a lot of functionality out of the box and is rapidly growing in coverage to be able to perform every task that can be performed in the |morpheus| UI. It is also a great way to get started in exploring the |morpheus| API and understanding some of the data model aspects.

Installation
^^^^^^^^^^^^^^^
A Prerequisite to running the CLI is to have ruby 2.0.0+ installed (2.3.0 recommended). Once the ruby runtime is installed simply use rubygems to install the CLI

  .. code-block::

      gem install morpheus-cli

Once the gem is installed all cli commands can be run on the shell via morpheus.

Setup
^^^^^^^^
The first thing that needs to be done after installing the cli is pointing the cli to the appliance. The CLI can be pointed at many appliances and uses the RESTful OAUTH public developer apis to perform tasks. To set this up simply add a remote appliance with the morpheus remote add command.

  .. code-block::

      morpheus remote add myappliance https://applianceUrl
      morpheus remote use myappliance
      morpheus login

There are several commands available when dealing with configuration of remote appliances. To see what commands are available just type

  .. code-block::

      morpheus remote
