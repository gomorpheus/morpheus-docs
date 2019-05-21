.. _ruby-prerequisite:


Ruby Installation
------------------

Step 1 – Installing Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First of all, we need to install all required packages for ruby installation on our system using the following command.

.. code-block:: text

    yum install gcc-c++ patch readline readline-devel zlib zlib-devel libyaml-devel libffi-devel openssl-devel make bzip2 autoconf automake libtool bison iconv-devel sqlite-devel

Step 2 – Install RVM
^^^^^^^^^^^^^^^^^^^^^

Install the latest stable version of RVM on your system using the following command. This command will automatically download all required files and install on your system.

.. code-block:: text

    curl -sSL https://rvm.io/mpapis.asc | gpg --import -
    curl -L get.rvm.io | bash -s stable

Also, run below command to load the RVM environment.

.. code-block:: text

    source /etc/profile.d/rvm.sh
    rvm reload

Step 3 – Verify Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now use the following command to verify all dependencies are properly installed. This will install any missing dependencies on your system.

.. code-block:: text

    rvm requirements run
    Checking requirements for centos.
    Requirements installation successful.

Step 4 – Install Ruby 2.5
^^^^^^^^^^^^^^^^^^^^^^^^^

After completing setup of RVM environment lets install Ruby language using the following command. Change Ruby version to below command you need to install.

.. code-block:: text

    rvm install 2.5
    [Sample Output]

    Searching for binary rubies, this might take some time.
    No binary rubies available for: centos/7/x86_64/ruby-2.5.1.
    Continuing with compilation. Please read 'rvm help mount' to get more information on binary rubies.
    Checking requirements for centos.
    Requirements installation successful.
    Installing Ruby from source to: /usr/local/rvm/rubies/ruby-2.5.1, this may take a while depending on your cpu(s)...
    ruby-2.5.1 - #downloading ruby-2.5.1, this may take a while depending on your connection...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 13.3M  100 13.3M    0     0   866k      0  0:00:15  0:00:15 --:--:--  823k
    ruby-2.5.1 - #extracting ruby-2.5.1 to /usr/local/rvm/src/ruby-2.5.1.....
    ruby-2.5.1 - #configuring..................................................................
    ruby-2.5.1 - #post-configuration..
    ruby-2.5.1 - #compiling....................................................................
    ruby-2.5.1 - #installing.............................
    ruby-2.5.1 - #making binaries executable..
    ruby-2.5.1 - #downloading rubygems-2.7.7
    ruby-2.5.1 - #extracting rubygems-2.7.7.....................................................
    ruby-2.5.1 - #removing old rubygems........
    ruby-2.5.1 - #installing rubygems-2.7.7................................
    ruby-2.5.1 - #gemset created /usr/local/rvm/gems/ruby-2.5.1@global
    ruby-2.5.1 - #importing gemset /usr/local/rvm/gemsets/global.gems...................................................
    ruby-2.5.1 - #generating global wrappers.......
    ruby-2.5.1 - #gemset created /usr/local/rvm/gems/ruby-2.5.1
    ruby-2.5.1 - #importing gemsetfile /usr/local/rvm/gemsets/default.gems evaluated to empty gem list
    ruby-2.5.1 - #generating default wrappers.......
    ruby-2.5.1 - #adjusting #shebangs for (gem irb erb ri rdoc testrb rake).
    Install of ruby-2.5.1 - #complete
    Ruby was built without documentation, to build it run: rvm docs generate-ri

Step 5 – Setup Default Ruby Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First of all, check the currently installed ruby versions on your system. So that we can find which version is using currently by the system and which is set to default.

.. code-block:: text

    rvm list
    ruby-2.3.5 [ x86_64 ]
       ruby-2.4.2 [ x86_64 ]
    * ruby-2.4.4 [ x86_64 ]
    => ruby-2.5.1 [ x86_64 ]
    # => - current
    # =* - current && default
    #  * - default

After that use rvm command to set up the default ruby version to be used by applications.

.. code-block:: text

    rvm use 2.5 --default
    Using /usr/local/rvm/gems/ruby-2.5.1

Step 6 – Verify Active Ruby Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using following command you can check the current ruby version is used.

.. code-block:: text

    ruby --version
    ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-linux]

Step 7 – Install Morpheus CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

    gem install morpheus-cli
