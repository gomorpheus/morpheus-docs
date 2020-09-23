Instance Tabs
^^^^^^^^^^^^^

Customize the UI for your Instances by providing your own tabs.

Setup
`````
Create a new class that extends ``com.morpheusdata.core.AbstractInstanceTabProvider``. When the Morpheus UI builds the Instance UI it calls the ``renderTemplate`` method. Below is a simple example binding the Instance object to the template model.

.. code-block:: groovy

   @Override
   HTMLResponse renderTemplate(Instance instance) {
     ViewModel<String> model = new ViewModel<String>()
     model.object = instance
     getRenderer().renderTemplate("hbs/instanceTab", model)
   }


.. tip:: Use ``MorpheusContext.buildInstanceConfig`` to get more details about your Instance. See ``com.morpheusdata.model.TaskConfig``

Handlebars <https://github.com/jknack/handlebars.java> is the default provided template engine. To override this default, implement the ``com.morpheusdata.core.InstanceTabProvider`` interface and then write your own ``getRenderer()`` method.


Templating
``````````
See the Views <https://github.com/gomorpheus/morpheus-plugin-core/blob/master/morpheus-plugin-docs/src/docs/asciidoc/Views.adoc> section and the documentation for your templating engine for specific syntax.


Security Policies
`````````````````

User Permissions
................
Before a template is rendered in the UI, the ``InstanceTabProvider.show`` method is called to determine if the current user can view the custom Instance Tab. For example, you may wish to check that the current ``User`` has been granted the custom permission defined by your plugin.

.. code-block:: groovy

   @Override
   Boolean show(Instance instance, User user, Account account) {
     def show = true
     plugin.permissions.each { Permission permission ->
       if(user.permissions[permission.code] != permission.availableAccessTypes.last().toString()){
         show = false
       }
     }
     return show
   }


Content Security Policy
.......................
If your custom UI needs to include external resources such as scripts, stylesheets, or frames, you will need to customize the Morpheus ``Content-Security-Policy`` Header to allow those elements to be loaded in the browser.

.. code-block:: groovy

   @Override
   TabContentSecurityPolicy getContentSecurityPolicy() {
     def csp = new TabContentSecurityPolicy()
     csp.scriptSrc = '*.jsdelivr.net'
     csp.frameSrc = '*.digitalocean.com'
     csp.imgSrc = '*.wikimedia.org'
     csp.styleSrc = 'https: *.bootstrapcdn.com'
     csp
   }
