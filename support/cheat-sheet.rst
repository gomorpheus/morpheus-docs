.. |title| replace:: replacement Cheet Sheet

|title|
=======

    So, you want to be able to contribute to the docs but don't know the syntax?  This cheat sheet will not go over all the
    details of `markdown <https://www.markdownguide.org/>`_ and `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.
    However, this cheat sheet will provide many of the common componenets used in the documents, as well as a recommendation for formatting to
    keep the pages consistent.  Consistency is especially important if you include a page inside another, as the headings/titles and other items may not sync
    up.

.. |heading| replace:: Headings

|section|
---------

    All headings should have characters under it that are as long as the heading text.  This will be seen in the examples below.  You can use many
    different types of special characters under the heading text, they don't have specific meanings, just what order they come in.  It is best to
    analyze the document you are editing to follow the same format, incase it has been created differently.  However, staying consistent is the goal.

    The general order is as follows:

    ::

        =
        -
        ^
        `
        .

Title Heading
^^^^^^^^^^^^^

    It is recommended that pages have the following headings for the very top of the page.  There should only be one title heading on the page, which will
    will be displayed at the top of the page and in the table of contents on the left.

    ::

        Replace Title Heading Here
        ==========================

    An example of the title heading can be seen on this page at the very top, with the text of **|title|**
    

Section Heading
^^^^^^^^^^^^^^^

    ::

        Replace Section Heading Here
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    An example can be seen on this section heading, with the text of **|heading|**

.. |sub| replace:: Sub Heading 

|sub|
^^^^^

    ::

        Replace Sub Heading Here
        ````````````````````````

    An example can be seen on this sub heading, with the text of **|sub|**


Simple Formatting
-----------------

Bold
^^^^

    ::

        Some of **this** text is **bold**.

    Output:

    Some of **this** text is **bold**.

Italics
^^^^^^^

    ::

        Some of *this* text is *italicized*.

    Output:

    Some of *this* text is *italicized*.

Code
^^^^

    ::

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

    ::

        .. _Replace This Name:

    This is an example that will be used below:

    ::

        .. _Percona TLS RHEL8:

    Once a page has had the above entry added, you can reference that page inside of another as a link.

    ::

        :ref:`Percona TLS RHEL8`

    Output:

    :ref:`Percona TLS RHEL8`

Link Externally
^^^^^^^^^^^^^^^

    Linking externally can be performed using Sphinx format:

    ::

        `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

    Output:

    `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

    The markdown format:

    ::

        [Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

    Output:

    [Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

    Just pasting the link only:

    ::

        https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

    Output:

    https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Substitutions
-------------

    There are cases where you'd like to use the same data multiple times but if you need to change it later on, you need to change it in multiple locations.
    This can be tedious as the documents grow, to find all the locations it might be used, such as a path like `Administration > Settings > Provisioning`.  What
    if the UI changes, now it need to be updated on all the documentation.

    **Substitutions** helps in this regard.  Consider it similar to variables, where you can use them again in placed, and ensure the consistency but also the
    changes globally, when needed.

    ::

        .. |mypath| replace:: Administration > Settings

        Navigate to `|mypath| > Appliance` to change settings for the appliance.
        
        Navigate to `|mypath| > Provisioning` to change settings for provisioning.


    Output:

    .. |mypath| replace:: Administration > Settings

    Navigate to `|mypath| > Appliance` to change settings for the appliance.
    
    Navigate to `|mypath| > Provisioning` to change settings for provisioning.

Blocks
------

    There are different types of blocks that can be used to catch a users eye or format the text correct.  Here are some examples that can be used:

Callouts
^^^^^^^^

    ::

        .. tip::
            Always look both ways before crossing the road.
    
        .. warning::
            Heavy traffic ahead.

        .. important::
            Watch out for that car!

Code Blocks
^^^^^^^^^^^
    
    Code blocks can be different languages that can be used, such as: 
    
    - ruby
    - bash
    - pwsh
    - ini
    - etc

    More language short names can be found here:  https://pygments.org/docs/lexers/#pygments.lexers.ruby.RubyLexer

    ::

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

    ::

        .. tabs::

            .. code-tab:: pwsh

                Write-Host "Hello world!"

            .. code-tab:: bash

                echo "Hello world!"

        .. tabs::

            .. code-tab:: pwsh

                Get-Content -Path C:\\Windows\\System32\\drivers\\etc\\hosts

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

            Get-Content -Path C:\\Windows\\System32\\drivers\\etc\\hosts

        .. code-tab:: bash

            echo /etc/hosts

Includes
--------

    Many times, you want to reuse documents, so they can be embedded in other documents.  This allows you to modify a single,
    document but the changes will be seen by all other documents that include it.

    Include paths are relative to the document that you use the include directive.  Examples below will demonstrate.

Include Page
^^^^^^^^^^^^

    Include a page in the same folder:

    ::

        .. include:: file.txt

    Include a page in a different (relative) folder:

Relative
````````
    
    ::

        .. include:: ./installation/app/3-node-ha/assumptions.rst

Literal
```````

    ::

        .. include:: /installation/app/3-node-ha/assumptions.rst

    The examples for relative and literal are very similar, as this document resides in the root.  Here is an example output
    using relative but it would be the same for both:

    **==========START OF INCLUDE==========**

    .. include:: ./installation/app/3-node-ha/assumptions.rst

    **==========END OF INCLUDE==========**

Other interesting items