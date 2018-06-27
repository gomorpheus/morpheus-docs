Installing on Windows
---------------------------------------

The morpheus cli is capable of running on many platforms due to its ruby runtime. This includes windows based platforms. To get started, we must first ensure ruby is running on the windows machine in question. To do this please visit http://rubyinstaller.org/downloads and download at least Ruby version 2.0.0 (2.3.3 recommended).

  .. note:: text
      When installing ruby on windows, make sure the options are selected for adding the ruby binaries to your PATH.

Now that ruby is installed, simply open a PowerShell window and run

    .. code-block:: text
      gem install morpheus-cli --no-ri --no-rdoc

A list of installed dependencies should start sliding by the screen. Once this has completed the CLI setup is complete. Now all that must be done is configuring the cli to point to an appliance for use.

    .. code-block:: text
      morpheus remote add myapp https://applianceUrl
      morpheus remote use myapp
      morpheus login

Credentials are used to acquire an access token which is then stored in the users home directory in a folder called .morpheus. Now all commands provided by the CLI are available for use just as if running in a *nix based environment.
