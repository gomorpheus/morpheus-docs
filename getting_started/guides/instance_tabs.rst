Getting Started with Custom Instance Tabs
-----------------------------------------

The |morpheus| plugin architecture is a library which allows users to extend functionality in several categories, including new Cloud providers, Task types, UI views, custom reports, and more. In this guide, we will take a look at developing a custom DataDog tab for Instance detail pages and adding it to |morpheus| UI. Complete developer documentation including the full API documentation and links to Github repositories containing complete code examples are available in the `Developer Portal <https://developer.morpheusdata.com/>`_.

Custom plugin development requires programming experience but this guide is designed to break down the required steps into a digestible process that users can quickly run with. |morpheus| plugins are written in Java or Groovy, our example here will be written in Groovy. Support for additional languages is planned but not yet available at the time of this writing. If you're not an experienced Java or Groovy developer, it may help to clone an `example code repository <https://github.com/gomorpheus/morpheus-plugin-core/tree/master/samples/morpheus-reports-plugin>`_ which we link to in our developer portal. An additional example, which this guide is based on, is `here <https://github.com/martezr/morpheus-datadog-instance-tab-plugin>`_. You can read the example code and tweak it to suit your needs using the guidance in this document.

Before you begin, ensure you have the following installed in your development environment:

- Gradle 6.5 or later
- Java 8 or 11
- A DataDog account

Planning the Plugin
^^^^^^^^^^^^^^^^^^^

In this example, I'll create a custom UI tab for Instance detail pages that shows related data from the DataDog monitoring solution. The tab will include two selectable sections, the first being an overview with basic information about the Instance and the second showing system information collected by DataDog. We'll also create a default page which will show in this tab for Instance which do not have the DataDog agent installed.

Understanding the DataDog API
`````````````````````````````

Knowing what we want to do, we need to identify the API calls needed to gather the data we want for our plugin. The `DataDog API Documentation <https://docs.datadoghq.com/api/latest/>`_ lays out the supported API calls and the response payloads you can expect. Additionally, the DataDog REST API requires an API key as well as an application key to authenticate calls to its REST API. The process for generating the keys can also be found in `DataDog API documentation <https://docs.datadoghq.com/account_management/api-app-keys/#api-keys>`_.

When making API calls, we'll use a function from the |morpheus| plugin library which simplifies the process for making HTTP requests to external APIs. You'll see an example use of that function later in this guide.

Developing the Plugin
^^^^^^^^^^^^^^^^^^^^^

The first thing we'll do is create a new directory to house the project. You’ll ultimately end up with a file structure typical of Java or Groovy projects, looking something like this:

.. code-block::

  ./
  .gitignore
  build.gradle
  src/main/groovy/
  src/main/resources/renderer/hbs/
  src/test/groovy/
  src/assets/images/
  src/assets/javascript/
  src/assets/stylesheets/

Configure the .gitignore file to ignore the build/ directory which will appear after performing the first build. Project packages live within src/main/groovy and contain source files ending in .groovy. View resources are stored in the src/main/resources subfolder and vary depending on the view renderer of choice. Static assets, like icons or custom javascript, live within the src/assets folder.

Updating the build.gradle File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The build.gradle file contains information used during the build of the plugin. The example included in the expandable section below is sufficient for most use cases with a few updates detailed in the table below.

.. toggle-header:: :header: **build.gradle**

  .. code-block::

    plugins {
        id "com.bertramlabs.asset-pipeline" version "3.3.2"
        id "com.github.johnrengelman.plugin-shadow" version "2.0.3"
    }

    apply plugin: 'java'
    apply plugin: 'groovy'
    apply plugin: 'maven-publish'

    group = 'com.morpheusdata'
    version = '0.0.2'

    sourceCompatibility = '1.8'
    targetCompatibility = '1.8'

    ext.isReleaseVersion = !version.endsWith("SNAPSHOT")

    repositories {
        mavenCentral()
    }

    dependencies {
        compileOnly 'com.morpheusdata:morpheus-plugin-api:0.12.0'
        compileOnly 'org.codehaus.groovy:groovy-all:2.5.6'
        compileOnly 'io.reactivex.rxjava2:rxjava:2.2.0'
        compileOnly "org.slf4j:slf4j-api:1.7.26"
        compileOnly "org.slf4j:slf4j-parent:1.7.26"
    }

    jar {
        manifest {
            attributes(
    	    'Plugin-Class': 'com.morpheusdata.tab.DataDogTabPlugin',
                'Plugin-Version': archiveVersion.get() // Get version defined in gradle
            )
        }
    }

    tasks.assemble.dependsOn tasks.shadowJar


.. list-table::
   :widths: auto
   :header-rows: 1

   * - Name
     - Description
     - Example
   * - group
     - The group of the project or an identifier of who owns the plugins. This is typically a domain that is associated with the individual developer or organization.
     - com.morpheusdata
   * - version
     - The version of the plugin which will appear in the Morpheus UI
     - 0.0.2
   * - dependencies
     - The plugin utilizes a number of dependencies for functionality and the morpheus-plugin-api dependency is the one of particular interest to us. The available release versions can be found on `Maven Central <https://search.maven.org/artifact/com.morpheusdata/morpheus-plugin-api>`_ where the releases are hosted. **Versions of the dependency align with specified versions of the Morpheus platform.**
     - com.morpheusdata:morpheus-plugin-api:0.12.0
   * - plugin-class
     - The name of the plugin class (group.packageName.className). In the example this also aligns with the folder structure of com/morpheusdata/tab/DataDogTabPlugin.groovy
     - com.morpheusdata.tab.DataDogTabPlugin

Plugin Settings
^^^^^^^^^^^^^^^

The plugin should support runtime configuration to allow administrators to update the configuration of the plugin without the need to rebuild it. The 5.4.1 release of the |morpheus| platform added support for plugin settings which enable the plugin to support runtime configuration.

In our example we want to expose a few runtime configuration settings such as the API credentials and conditions for when the tab should be visible. The table below details the settings that the plugin supports.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Name
     - Description
   * - DataDog API Key
     - The API key used for authenticating to the DataDog REST API
   * - DataDog Application Key
     - The application key used for authenticating to the DataDog REST API
   * - Environment Visibility
     - The setting to define which Morpheus environments that a workload belongs to for the tab to be visible
   * - Group Visibility
     - The setting to define which Morpheus groups that a workload belongs to for the tab to be visible

Defining Plugin Settings
````````````````````````

The plugin settings are defined in the `plugin definition <https://github.com/martezr/morpheus-datadog-instance-tab-plugin/blob/main/src/main/groovy/com/morpheusdata/tab/DataDogTabPlugin.groovy>`_ file as inputs similar to inputs used in other areas of the |morpheus| platform. One item of note is the ``fieldName`` which is used as the reference for when retrieving the value specified from within the code.

.. code-block::

  this.settings << new OptionType(
          name: 'API Key',
          code: 'datadog-plugin-api-key',
          fieldName: 'ddApiKey',
          displayOrder: 0,
          fieldLabel: 'API Key',
          helpText: 'The DataDog API key',
          required: true,
          inputType: OptionType.InputType.PASSWORD
  )

Retrieving Plugin Settings
``````````````````````````

The plugin settings enable administrators to update the runtime configuration of the plugin and so we need to reference them in our code. The settings are accessible by retrieving them and parsing the JSON payload.

.. code-block::

  def settings = morpheus.getSettings(plugin)
  def settingsOutput = ""
  settings.subscribe(
          { outData ->
          settingsOutput = outData
  },
  { error ->
          println error.printStackTrace()
  }
  )
  JsonSlurper slurper = new JsonSlurper()
  def settingsJson = slurper.parseText(settingsOutput)

In our example, the value of the settings will be available using dot notation (i.e. settingsJson.settingFieldName). This is where fieldName value of the plugin settings is referenced.

Query the DataDog API
^^^^^^^^^^^^^^^^^^^^^

Now that we've got the response payload we'll use the JsonSlurper library to parse the JSON.

.. code-block::

  JsonSlurper slurper = new JsonSlurper()
  def json = slurper.parseText(results.content)

The parsed payload supports accessing the payload values using dot notation. The example below which is been truncated for brevity shows how the payload is accessed and ultimately passed to the html template file.

.. code-block::

  if (json.host_list.size == 0){
          getRenderer().renderTemplate("hbs/instanceNotFoundTab", model)
  } else {
          // Store objects from the response payload
          def baseHost = json.host_list[0]
          def apps = baseHost.apps
          def agentVersion = baseHost.meta.agent_version
          def checks = baseHost.meta.agent_checks.size
          def agentChecks = baseHost.meta.agent_checks

          dataDogPayload.put("id", instance.id)
          dataDogPayload.put("apps", apps)
          dataDogPayload.put("agentVersion", agentVersion)
          dataDogPayload.put("checks", checks)
          dataDogPayload.put("agentChecks", agentChecks)
          // Set the value of the model object to the HashMap object
          model.object = dataDogPayload

          // Render the HTML template located in
          // resources/renderer/hbs/instanceTab.hbs
          getRenderer().renderTemplate("hbs/instanceTab", model)
  }

Managing Tab Visibility
^^^^^^^^^^^^^^^^^^^^^^^

Now that we've got the core functionality of the plugin developed, we want to restrict which Instances the tab is displayed for (i.e. only production, AWS cloud Instances, etc.).

Manage Visibility with |morpheus| RBAC
``````````````````````````````````````

The RBAC permissions associated with a user can be used to determine the visibility of the DataDog plugin tab.

.. code-block::

  def permissionStatus = false
  if(user.permissions["datadog-instance-tab"] == "full"){
      permissionStatus = true
  }

Manage Visibility by Instance Environment Setting
`````````````````````````````````````````````````

The |morpheus| environment that an Instance or virtual machine belongs to can be used to determine the visibility of the DataDog plugin tab.

.. code-block::

  def tabEnvironments = settingsJson.environmentVisibilityField.split(",");
  def visibleEnvironments = []
  for(environment in tabEnvironments){
      visibleEnvironments.add(environment.trim())
  }
  println visibleEnvironments
  def environmentStatus = false
  if (visibleEnvironments.contains("any")){
      environmentStatus = true
  }
  if(visibleEnvironments.contains(config.instance.instanceContext)){
      environmentStatus = true
  }

Manage Visibility By |morpheus| Group
`````````````````````````````````````

The Morpheus group that an instance or virtual machine belongs to can be used to determine the visibility of the DataDog plugin tab.

.. code-block::

  def tabGroups = settingsJson.groupVisibilityField.split(",");
  def visibleGroups = []
  for(group in tabGroups){
      visibleGroups.add(group.trim())
  }
  println visibleGroups
  def groupStatus = false
  if(visibleGroups.contains("any")){
      groupStatus = true
  }
  if(visibleGroups.contains(instance.site.name)){
      groupStatus = true
  }

Build the UI Tab Plugin
^^^^^^^^^^^^^^^^^^^^^^^

With the code written, we'll use gradle to build the JAR which we'll upload to |morpheus| to install the plugin. To do so, change directory into the location of the directory created earlier to hold your custom plugin code.

.. code-block::

  cd path/to/your/directory

Run gradle to build a new version of the plugin.

.. code-block::

  gradle shadowJar

Once the build process has completed, locate the JAR in the build/libs directory.

Install and Configure the UI Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custom plugins are added to |morpheus| through the Plugins tab in the Integrations section of the Morpheus UI.

#. Navigate to |AdmIntPlu| and click CHOOSE FILE
#. Browse for the JAR file and upload it to |morpheus|
#. The new plugin will be added next to any other custom plugins that may have been developed for your appliance
#. Click on the pencil to the right of the plugin to open the configuration modal
#. Enter the API and Application keys used to authenticate to the DataDog REST API
#. Click :guilabel:`SAVE`

Once the plugin has been added to |morpheus|, navigate to an Instance detail page which is running the DataDog agent and meets any visibility requirements you may have established. In the row of tabs, you should now see DataDog. Click on this tab to see the retrieved DataDog details relevant to this Instance.
