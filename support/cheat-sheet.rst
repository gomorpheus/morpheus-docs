.. |title| replace:: Cheat Sheet

|title|
=======

    So, you want to be able to contribute to the docs but don't know the syntax?  This cheat sheet will not go over all the
    details of `markdown <https://www.markdownguide.org/>`_ and `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.
    However, this cheat sheet will provide many of the common componenets used in the documents, as well as a recommendation for formatting to
    keep the pages consistent.  Consistency is especially important if you include a page inside another, as the headings/titles and other items may not sync
    up.

.. |heading| replace:: Headings

|heading|
---------

    All headings should have characters under it that are **at least** as long as the heading text, this will be seen in the examples below.  You can use many
    different types of special characters under the heading text, they don't have specific meanings, just what order they come in.  It is best to
    analyze the document you are editing to follow the same format, incase it has been created differently.  However, staying consistent is the goal.

    The general order is as follows:

    .. code-block:: text

        =
        -
        ^
        `
        .

Title Heading
^^^^^^^^^^^^^

    It is recommended that pages have the following headings for the very top of the page.  There should only be one title heading on the page, which will
    will be displayed at the top of the page and in the table of contents on the left.

    .. code-block:: text

        Replace Title Heading Here
        ==========================

    An example of the title heading can be seen on this page at the very top, with the text of |title|
    

Section Heading
^^^^^^^^^^^^^^^

    .. code-block:: text

        Replace Section Heading Here
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    An example can be seen on this section heading, with the text of |heading|

.. |sub| replace:: Sub Heading 

|sub|
^^^^^

    .. code-block:: text

        Replace Sub Heading Here
        ````````````````````````

    An example can be seen on this sub heading, with the text of |sub|


Simple Formatting
-----------------

Bold
^^^^

    .. code-block:: text

        Some of **this** text is **bold**.

    Output:

        Some of **this** text is **bold**.

Italics
^^^^^^^

    .. code-block:: text

        Some of *this* text is *italicized*.

    Output:

        Some of *this* text is *italicized*.

Code
^^^^

    .. code-block:: text

        Modify the ``/etc/hosts`` file.

    Output:

        Modify the ``/etc/hosts`` file.

Links
-----

Link Internally
^^^^^^^^^^^^^^^

    Pages can be linked to internally, without the need to provide an absolute path.  The following can be added to a page (usually at the top),
    which will be available from any page when rendered.  The following example directive can have spaces in the name, as seen below.  In the case
    of the example, replace "Replace This Name" with an appropriate name for the page.

        .. code-block:: text

            .. _Replace This Name:

    This is an example that will be used below:

        .. code-block:: text

            .. _Percona TLS RHEL8:

    Once a page has had the above entry added, you can reference that page inside of another as a link.

        .. code-block:: text

            :ref:`Percona TLS RHEL8`

    Output:

        :ref:`Percona TLS RHEL8`

Link Externally
^^^^^^^^^^^^^^^

    Linking externally can be performed using Sphinx format:

        .. code-block:: text

            `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

    Output:

        `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

    Just pasting the link only:

        .. code-block:: text

            https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

    Output:

        https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Substitutions
-------------

    There are cases where you'd like to use the same data multiple times but if you need to change it later on, you need to change it in multiple locations.
    This can be tedious as the documents grow, to find all the locations it might be used, such as a path like ``Administration > Settings > Provisioning``.  What
    if the UI changes, now it need to be updated on all the documentation.

    **Substitutions** helps in this regard.  Consider it similar to variables, where you can use them again in places, and ensure the consistency but also the
    changes globally, when needed.

        .. code-block:: text

            .. |mypath| replace:: Administration > Settings

            Navigate to |mypath| > Appliance to change settings for the appliance.
            
            Navigate to |mypath| > Provisioning to change settings for provisioning.


    Output:

        .. |mypath| replace:: Administration > Settings

        Navigate to |mypath| > Appliance to change settings for the appliance.
        
        Navigate to |mypath| > Provisioning to change settings for provisioning.

    .. note::
        Many of these are already available in the `conf.py` file in this project, as well as the public docs.

    .. note::
        It is the practice in the public docs, as well as this project, to not use "Morpheus" but to use the `|morpheus|` substitution.  This keeps it clean, should the
        name ever change.

Blocks
------

    There are different types of blocks that can be used to catch a users eye or format the text correct.  Here are some examples that can be used:

Callouts
^^^^^^^^

    .. code-block:: text

        .. tip::
            Always look both ways before crossing the road.
    
        .. warning::
            Heavy traffic ahead.

        .. important::
            Watch out for that car!

    Output:

        .. tip::
            Always look both ways before crossing the road.
    
        .. warning::
            Heavy traffic ahead.

        .. important::
            Watch out for that car!

Code Blocks
^^^^^^^^^^^
    
    Code blocks have different languages that can be used, such as: 
    
    - ruby
    - bash
    - pwsh
    - ini
    - etc

    More language short names can be found here:  https://pygments.org/docs/lexers/#pygments.lexers.ruby.RubyLexer

        .. code-block:: text

            .. code-block:: ruby

                appliance_url 'https://morpheus.localdomain'
                elasticsearch['es_hosts'] = {'192.168.104.01' => 9200, '192.168.104.02' => 9200, '192.168.104.03' => 9200}
                elasticsearch['node_name'] = '192.168.104.01'
                elasticsearch['host'] = '0.0.0.0'
                rabbitmq['host'] = '0.0.0.0'
                rabbitmq['nodename'] = 'rabbit@node01'
                mysql['enable'] = false
                mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
                mysql['morpheus_db'] = 'morpheus'
                mysql['morpheus_db_user'] = 'morpheusDbUser'
                mysql['morpheus_password'] = 'morpheusDbUserPassword'

    Output:

        .. code-block:: ruby

            appliance_url 'https://morpheus.localdomain'
            elasticsearch['es_hosts'] = {'192.168.104.01' => 9200, '192.168.104.02' => 9200, '192.168.104.03' => 9200}
            elasticsearch['node_name'] = '192.168.104.01'
            elasticsearch['host'] = '0.0.0.0'
            rabbitmq['host'] = '0.0.0.0'
            rabbitmq['nodename'] = 'rabbit@node01'
            mysql['enable'] = false
            mysql['host'] = {'192.168.101.01' => 3306, '192.168.101.02' => 3306, '192.168.101.03' => 3306}
            mysql['morpheus_db'] = 'morpheus'
            mysql['morpheus_db_user'] = 'morpheusDbUser'
            mysql['morpheus_password'] = 'morpheusDbUserPassword'

    ``sphinx-tabs`` is included in this project, so some more advanced items are available.  More info can be found here:  https://sphinx-tabs.readthedocs.io/en/latest/

        .. code-block:: text

            .. tabs::

                .. code-tab:: pwsh

                    Write-Host "Hello world!"

                .. code-tab:: bash

                    echo "Hello world!"

            .. tabs::

                .. code-tab:: pwsh

                    Get-Content -Path C:\Windows\System32\drivers\etc\hosts

                .. code-tab:: bash

                    echo /etc/hosts

    Output:

        .. tabs::

            .. code-tab:: pwsh

                Write-Host "Hello world!"

            .. code-tab:: bash

                echo "Hello world!"

        .. tabs::

            .. code-tab:: pwsh

                Get-Content -Path C:\Windows\System32\drivers\etc\hosts

            .. code-tab:: bash

                echo /etc/hosts

Includes
--------

    Many times, you want to reuse documents, so they can be embedded in other documents.  This allows you to modify a single,
    document but the changes will be seen by all other documents that include it.

    Include paths are relative to the document that you use the include directive.  Examples below will demonstrate.

    This is the contents of the document used in the example:

        .. toggle-header::
            :header: **Click to expand**
                
            .. literalinclude:: ./cheat-sheet-inc.rst

    Additional documentation:  https://docutils.sourceforge.io/docs/ref/rst/directives.html#include

    .. important::
        Reminder that if you are using headings, ensure they align appropriately, or your text may not format correctly for them

Include Page
^^^^^^^^^^^^

    Include a page in the same folder:

        .. code-block:: text

            .. include:: cheat-sheet-inc.rst

    Relative
    ````````
        
        .. code-block:: text

            .. include:: ./cheat-sheet-inc.rst

    Literal
    ```````

        .. code-block:: text

            .. include:: /support/cheat-sheet-inc.rst

        Here is an example output using relative but it would be the same for both:

            **==========START OF INCLUDE==========**

            .. include:: ./cheat-sheet-inc.rst

            **==========END OF INCLUDE==========**

Include Excerpt
^^^^^^^^^^^^^^^

    In addition to being able to include an entire page, you can include just portions of the page, instead of the entire document.

        .. code-block:: text

            .. include:: ./cheat-sheet-inc.rst
                :start-after: cool-section-start
                :end-before: cool-section-end

    The above includes the first sentence of the document only:

        **==========START OF INCLUDE==========**

        .. include:: ./cheat-sheet-inc.rst
            :start-after: cool-section-start
            :end-before: cool-section-end

        **==========END OF INCLUDE==========**

    In the above example, the file being included contains some extra text, such as:

        .. code-block:: text

            .. cool-section-start

            .. cool-section-end

    The text above is what is used by the include directive to determine what it should include.  You don't have to use both the `:start-after:` and `:end-before:`
    arguments but this ensures just a small portion is captured in this case.  The text above is prepended with `.. ` to make sure the text does not appear in that
    document, if someone was to navigate to it.  The `.. ` is commenting in Sphinx, so it is ignored when rendered.  However, the `.. ` is not required, just a nice
    trick!

Other Interesting Objects
-------------------------

This document is not meant to be comprehensive, but to provide common examples.  See the following examples below, which more details can be searched for in the 
Sphinx documentation.

Tables
^^^^^^

    .. toggle-header::
        :header: **Basic - Click to expand**
                    
        .. code-block:: text

            +---------------+-------------------+------------------+----------------------------------------------+
            | Service       | Source            | Destination      | Port(s)                                      |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | mySQL            | 3306                                         |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | Elasticsearch    | 9200                                         |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | RabbitMQ         | 5672/5671(SSL)                               |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | YUM or APT       | 443                                          |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Elasticsearch | Elasticsearch     | Elasticsearch    | 9300                                         |
            +---------------+-------------------+------------------+----------------------------------------------+
            | mySQL         | mySQL             | mySQL            | 4444,4567,4568                               |
            +---------------+-------------------+------------------+----------------------------------------------+
            | RabbitMQ      | RabbitMQ          | RabbitMQ         | 4369,25672                                   |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Agents        | Managed Instances | Application Node | 443                                          |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Web Interface | Internal Clients  | Application Node | 443                                          |
            +---------------+-------------------+------------------+----------------------------------------------+

        Output:

            +---------------+-------------------+------------------+----------------------------------------------+
            | Service       | Source            | Destination      | Port(s)                                      |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | mySQL            | 3306                                         |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | Elasticsearch    | 9200                                         |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | RabbitMQ         | 5672/5671(SSL)                               |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Morpheus      | Application Node  | YUM or APT       | 443                                          |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Elasticsearch | Elasticsearch     | Elasticsearch    | 9300                                         |
            +---------------+-------------------+------------------+----------------------------------------------+
            | mySQL         | mySQL             | mySQL            | 4444,4567,4568                               |
            +---------------+-------------------+------------------+----------------------------------------------+
            | RabbitMQ      | RabbitMQ          | RabbitMQ         | 4369,25672                                   |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Agents        | Managed Instances | Application Node | 443                                          |
            +---------------+-------------------+------------------+----------------------------------------------+
            | Web Interface | Internal Clients  | Application Node | 443                                          |
            +---------------+-------------------+------------------+----------------------------------------------+

|

    .. toggle-header::
        :header: **Advanced - Click to expand**
                    
        .. code-block:: text

            .. list-table:: **RabbitMQ Port Requirement Details**
                :widths: auto
                :header-rows: 1

                * - Source 
                    - Destination
                    - Port
                    - Protocol
                    - For
                * - Application Tier
                    - Messaging Tier
                    - 5672
                    - TCP
                    - AMQP non-TLS connections
                * - Application Tier
                    - Messaging Tier
                    - 5671
                    - TCP
                    - AMQPS TLS enabled connections
                * - Messaging Tier
                    - Messaging Tier
                    - 25672
                    - TCP
                    - Inter-node and CLI tool communication
                * - Administrator Web Browser
                    - RabbitMQ Server Management
                    - 15672
                    - TCP
                    - Management plugin
                * - Administrator Web Browser
                    - RabbitMQ Server Management
                    - 15671
                    - TCP
                    - Management plugin SSL
                * - Messaging Tier Cluster Node
                    - Messaging Tier Cluster Nodes
                    - 4369
                    - TCP
                    - erlang epmd peer discovery service used by RabbitMQ nodes and CLI tools

        Output:

            .. list-table:: **RabbitMQ Port Requirement Details**
                :widths: auto
                :header-rows: 1

                * - Source 
                    - Destination
                    - Port
                    - Protocol
                    - For
                * - Application Tier
                    - Messaging Tier
                    - 5672
                    - TCP
                    - AMQP non-TLS connections
                * - Application Tier
                    - Messaging Tier
                    - 5671
                    - TCP
                    - AMQPS TLS enabled connections
                * - Messaging Tier
                    - Messaging Tier
                    - 25672
                    - TCP
                    - Inter-node and CLI tool communication
                * - Administrator Web Browser
                    - RabbitMQ Server Management
                    - 15672
                    - TCP
                    - Management plugin
                * - Administrator Web Browser
                    - RabbitMQ Server Management
                    - 15671
                    - TCP
                    - Management plugin SSL
                * - Messaging Tier Cluster Node
                    - Messaging Tier Cluster Nodes
                    - 4369
                    - TCP
                    - erlang epmd peer discovery service used by RabbitMQ nodes and CLI tools

Toggles
^^^^^^^

    .. code-block:: text

        .. toggle-header::
            :header: **Click to expand**

            Some text inside here!

    Output:

        .. toggle-header::
            :header: **Click to expand**

            Some text inside here!

Extra White Space
^^^^^^^^^^^^^^^^^

    If you need extra white space, you can use the pipe ( | ) character.  However, note that it must reside to the far
    lefr of the document to work.

    .. code-block:: text

            I need
        |
        |
        |
        |
            space

    Output:

        I need
|
|
|
|

        space

Images
^^^^^^

    Adding images can be done with relative or absolute paths to the project files.
    
        .. code-block:: text
        
            .. image:: /images/support/troubleshooting/app_guest_cust_hostname_failure.png

        Output:

            .. image:: /images/support/troubleshooting/app_guest_cust_hostname_failure.png

    Additional information:  https://sublime-and-sphinx-guide.readthedocs.io/en/latest/images.html

.. raw:: html

    <iframe width="560" height="315" src="/_static/storageCalculator/index.html" frameborder="0" allowfullscreen></iframe>