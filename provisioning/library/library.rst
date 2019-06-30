Library
=======

Overview
--------

The Library section is used to add virtual images as custom instances to the provisioning catalog. The Library Section is composed of:

* Instance Types
* Layouts
* Node Types
* Option Types
* Option Lists
* File Templates
* Scripts

Uploaded or synced images from the virtual images section are added to nodes, a node or multiple nodes are added to layouts, and layouts are added to Instance Types. Scripts and File Templates can be attached to nodes, with phased execution options for scripts.

.. tabs::

   .. tab:: Instance Types

       Instance Types
       --------------

       Adding an Instance Type creates a new Library Item category. Multiple layouts can be added to an instance type, and these layout can have different nodes attached. The instance wizard will present the layout options compatible with the selected cloud. If cloud selection is turned off, all layouts will be presented for all cloud types accessible by the user.

       Name
         Name of the Instance Type in the Provisioning Library
       Code
         Useful shortcode for provisioning naming schemes and export reference.
       Description
         The description of the Instance Type shown in the Provisioning Library. (255 characters max)
       Category
         For filtering in Instance sections and Provisioning Wizard

         * Web
         * SQL
         * NoSLQ
         * Apps
         * Network
         * Messaging
         * Cache
         * OS
         * Cloud
         * Utility

       Icon
         Suggested Dimensions: 150 x 51
       Visibility
         * Private- Only accessibly by assigned Accounts/Tenants
         * Public- accessible by all Accounts/Tenants
       Environment Prefix
         Used for exportable environment variables when tying instance types together environment Variables in app contexts. If not specified a name will be generated
       Enable Scaling (Horizontal)
         Enables load balancer assignment and auto-scaling features
       Supports Deployments
         Enables deployment features (Requires a data volume be configured on each version. Files will be copied into this location)

       Upon saving, this Instance Type will be available in the Provisioning Catalog, per user role access. However we still need to add layouts to the Instance Type, and prior to creating a layout, we will add a node type.

   .. tab:: Layouts

        Layouts
        -------

        .. image::

        - Layouts are attached to Instance types. A Layout can only be attached to a single Instance Type and a single Technology Type.

        - An Instance Type can have one or many Layouts attached to it, allowing for a single Instance Type to work with any Technology Type.

        - Node Types are added to Layouts. A Layout can have one or many node types attached to it. Node types can be shared across Layouts of matching Technology Types.

        .. important:: Once an Instance Type is defined on a Layout and saved, the Instance Type setting on the Layout cannot be changed.

        Layout List view
        ^^^^^^^^^^^^^^^^

        The Layout list view shows all available Instances Types including Name, Version, associated Instance Type and description.

        - The Technology Filter will filter the displayed layouts by selected Technology.
        - The Instance Type Filter will filter the displayed Layout by associated Instance Type.
        - Layout Names link to the Layouts associated Layout Detail page.
        - Instance Types link to the Layouts associated Layout Detail page.
        - The pencil icon open the Edit Layout modal
        - The Trash Can icon deletes the Layout.

          .. note:: A Layout that is in use cannot be deleted.

        - Select :guilabel:`+ ADD` to add a new Layout. Layouts can also be created form an Instance Types detail page.

        Layout Detail View
        ^^^^^^^^^^^^^^^^^^

        The Layout Detail view shows details on the Layout and all associated Node Types.

        - Select a Layout Name from the Layout list page or Instance Type Detail page to get to a Layout Detail page.


        Layout Configuration Options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Instance Type
          Select the Instance Type to add the new Layout to. Custom Instance Types must already be created and one layout cannot be added to multiple instance types, or change Instance Types after creation.

          .. NOTE:: Layouts cannot be added to System Instance Types.

        Name
          The name the layout will present as in the Configuration Options dropdown in the provisioning wizard
        Version
          The version number or name for the Layout. Layouts in an Instance Type with the same version will all show under the Configuration Options dropdown when that version in selected while provisioning.
        Description
          Description of the layout, viewable on the Layout list tab.
        Technology
          Technology determines which cloud this layout will be available for, and which Node Types can be added to it.
        Minimum Memory
          Defines the Minimum amount of Memory required for this Layout. Only Service Plans that meet the defined Minimum Memory value will be available during Provisioning when this Layout is selected, and custom memory values must meet this minimum. 0 equals no Minimum Memory requirement. This Minimum Memory value will override any Virtual Image Minimum Memory requirements.
        Workflow
          Select a Workflow to automatically run and be attached to associated Instances using this Layout. If a Workflow is defined, it is not presented in the Provisioning Wizard and is not user configurable.
        Supports Convert to Managed
          Enabled to allow users to select this layout when converting a Discovered workload to managed.
        Enable Scaling (Horizontal)
          Enables Instances with this layout to use Scaling features
        Environment Variables
          Custom evars to be added to the instance when provisioned.
        Option Types
          Search for and then select one or multiple Option Types to add to Layout. Option Type input fields (except for Hidden Option Types) will appear in Provisioning, App, Blueprint, and Cloning wizards when this layout is selected.
        Nodes
          Single or multiple nodes can be added to a Layout by searching for and selecting the node(s). An example of a layout with multiple nodes is the Hyper-V MySQL Master/Slave layout pictured below (note this is the Layout detail screen after the layout has been created.)

   .. tab:: Node Types

       Node Types
       ----------

       Node Types are the link between Images and Layouts.

       Node Type Configuration Options
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

       The following fields are for all node technology types:

       Name
         Name of the Node Type in |morpheus|
       Short Name
         The short name is a lowercase name with no spaces used for display in your container list.
       Version
         Version for the Node Type. Examples: 7.5, 2012 R2, latest
       Technology
         Select associated Technology. This will filter the available configuration Options, Images and which Layouts the Node Type can be added to.
       Environment Variables
         Add pre-set evars to the Node Type. Click OPTIONS for additional evar config options.

       The Options fields will change depending on the Technology option selected.

       For VM provisioning technology options, select an image from the VM Image dropdown, which is populated from the Virtual Images Section and will include images uploaded into |morpheus|, and synced images from added clouds.

       .. NOTE:: Amazon and Azure Marketplace Images can be added in the Virtual Images section for use as node types in custom library items.

       For Docker, type in the name and version of the Docker Image and select the integrated registry.

       Expose Ports
         To open port on the node, select "Add Port" and enter the name and port to expose. The Load Balancer http, https or tcp setting is required when attaching to Load Balancers.

         Defining an Exposed port will also create a hyperlink(s) on the container location (ip) in the VM or Container section of the associated Instance Detail page.

       Scripts
         Search for and select one or multiple scripts to be executed when the Node Type is provisioned.

       File Templates
         Search for and select one or multiple File Templates to be written when the Node Type is provisioned.

       Example port configuration:

       .. image:: /images/provisioning/library/node_ports.png

       VMware Extra Options
       ````````````````````

       When VMware Technology Type is selected, EXTRA OPTIONS will be available in the VMware VM Options section. These allow defining Advance vmx-file parameters during provisioning.

       Some Example include:

       .. code-block:: bash

         tools.setinfo.sizeLimit : 1048576
         vmci0.unrestricted : FALSE
         isolation.tools.diskWiper.disable : TRUE

       .. NOTE:: Not all parameters can be set using extra config parameters. A sample reference list can be found at http://www.sanbarrow.com/vmx/vmx-advanced.html#vmx

       .. IMPORTANT:: Use caution when setting Extra Options. Malformed config files can break provisioning. Issues related to the Extra Options defined by the user are the users responsibility to troubleshoot.

   .. tab:: Option Types

       Option Types
       ------------

       Option Types are custom input fields that can be added to Instance Types and Layouts and used in Instance, App and Cloning wizards. The resulting value is available in the Instance config map as <%=customOptions.fieldName%>, and the filedName and value can also be exported as metadata.

       .. image:: /images/provisioning/library/OptionType.png


       .. image:: /images/provisioning/library/variable.png

   .. tab:: Option Lists

       Option Lists
       ------------

       Option Lists allow you to give the user more choices during provisioning to then be passed to scripts and/or automation.  Option Lists, however, are pre-defined insofar as they are not free-form. They can either be manually entered CSV or JSON or they can be dynamically compiled from REST calls via GET or POST requests.

       .. NOTE:: JSON entries must be formatted like the following example: ``[{"name":"Test","value":1},{"name":"Testing","value":2}]``

       .. image:: /images/provisioning/library/optionlist.png

       .. image:: /images/provisioning/library/OptionListREST.png


   .. tab:: File Templates

      File Templates
      --------------

      File Templates are for generating config files, such as my.cnf, elasticsearch.yml, morpheus.rb etc, or any text file. With full config map variable support, Template Files are dynamically generated during a workflow phase or ad hoc via Instance Actions.

      File Templates can also be exposed on Instances in the Settings Tab. Ensure the Instance Type supports settings, and Category is defined in Advance Options on the Library Template config.

      .. note:: |morpheus| variables are supported in Library Templates using ``<%= variable.var %>`` format

      Examples:

      HA Proxy Config (haproxy.cfg)

      - FILE NAME: haproxy.cfg
      - FILE PATH: /config/haproxy.cfg
      - PHASE: Pre Provision
      - TEMPLATE:
      - SETTING NAME: haproxyConfig
      - SETTING CATEGORY: haproxy

      .. code-block:: bash

        #!/bin/bash

        global
         maxconn 256
         log /dev/log local0 warning
         log-tag <%=logTag%>

        defaults
         mode http
         timeout connect 5000ms
         timeout client 50000ms
         timeout server 50000ms
         log global

        frontend http-in
         bind *:<%=container.externalPort%>
         default_backend servers

        backend servers
         # server server1 127.0.0.1:80 maxconn 32


      mysql config (mysqld.cnf)

      - FILE NAME: mysqld.cnf
      - FILE PATH: /config/mysqld.cnf
      - PHASE: Pre Provision

      .. code-block:: bash

         #!/bin/bash

         [mysqld]
         pid-file= /var/run/mysqld/mysqld.pid
         socket= /var/run/mysqld/mysqld.sock
         datadir= /var/lib/mysql
         # Disabling symbolic-links is recommended to prevent assorted security risks
         symbolic-links=0
         explicit_defaults_for_timestamp = 1



   .. tab:: Scripts

       Scripts
       -------

       Scripts are bash and powershell scripts that can be attached to node types to always execute at the set phase when that node type is provisioned, added to Workflows as Library Script Tasks, and/or execute ad-hoc on Instances.

       Creating Scripts
       ^^^^^^^^^^^^^^^^

       #. Navigate to ``Provisioning -> Library -> Scripts``
       #. Select :guilabel:`+ ADD`
       #. Enter the Following:

          NAME
            Name of the Script in |morpheus|
          SCRIPT TYPE
            - Bash
            - Powershell
          PHASE
            Select which phase the Script will execute when attached to a Node Type. When a script is attached to a Node Type, it will execute according to the set Phase:

            Start Service
              Any time the Instance action ``Start Service`` is executed.
            Stop Service
              Any time the Instance action ``Stop Service`` is executed.
            Pre-Provision
              Containers
                Script will execute agains the container host before the container is provisioned
              Virtual Machines
                Script will execute before any Provision phase scripts or Tasks
            Provision
                Script will execute once per new Instance node during the Provision Phase. Provisioning will not be considered complete until all scripts and tasks in the Provisioning Phase are completed.

                .. NOTE:: Any Script or Task set to Provision Phase will be included in the total Provision Time and impact success/warn/failure Provision status. Aka your VM could be up and running but if your Script is in the Provision phase and fails, provisioning will be marked as a failure.

              Post-Provision
                  Script will execute once per new Instance node after the Provision phase is completed. Scripts and Tasks in the Post-Provision phase will show Execution Status and History, but are not considered part of the Provision and do not impact Provisioning Status.
              Pre-Deploy
                  Script will execute on Target Instance any time a Deployment is ran against the Instance. The script will run prior to the Deployment file(s) being written.
              Deploy
                  Script will execute on Target Instance any time a Deployment is ran against the Instance. The script will run after the Deployment file(s) are written.
              Reconfigure
                  Script will execute on Target Instance anytime a Reconfigure is executed against the Instance.
              Teardown
                  Script will execute on Target Instance upon Instance deletion. Script will execute against Target Instance prior to the deletion/removal of resources.

          SCRIPT
            Enter bash or powershell script.

            .. note:: |morpheus| variables are supported in Library Scripts using ``<%= variable.var %>`` format 

          RUN AS USER
            By default script are execute as ``morpheus-node``. To execute as another User, populate ``RUN AS USER`` and ensure proper user permissions & group access.
          SUDO
            Flag ``SUDO`` if sudo is required to execute the Script


       To attach scripts and templates that have been added to the Library to a node type, start typing the name and then select the script(s) and/or template(s).

       * Multiple scripts and templates can be added to a node type
       * Scripts and Templates can be added/shared among multiple node types
       * The Execution Phase can be set for scripts in the Scripts section.
       * Search will populate Scripts or Templates containing the characters entered anywhere in their name, not just the first letter(s) of the name.
