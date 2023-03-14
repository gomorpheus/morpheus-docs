Apps
====

Apps allow instances having general relationships to be grouped in a
clean and organized manner. App functionality enables full control of
which instances belong in an app as well setting Firewall and Access
Control List (ACL) rules. Use Apps to structure all necessary components
into a single place. Add checks and groups for web servers, database
nodes, etc.

Creating Apps
-------------

To create and App, click "+ADD APP" on the right side of the main Apps
section in Provisioning.

.. image:: /images/apps/howtocreateapp-ee817.png

Next fill in the Setup tab with your App name, optional description, and
select a resource group:

.. image:: /images/apps/howtocreateapp-7f57d.png

In the LAYOUT tab, you have the option of selecting a Template (created
in the Templates section) or Add Tiers. To use a Template, select a
Template from the dropdown and your app will populate in the layout
section. You can add to, modify, edit your template, or simply click
next of the Template is fully configured:

.. image:: /images/apps/howtocreateapp-680f5.png

To create an app without a Template, start by adding a Tier by clicking "+ ADD TIER". Name the Tier by selecting a pre-populated, recently used, or add a new/custom Tier name:

.. image:: /images/apps/howtocreateapp-07e66.png

For each Tier added, a new Tier container is created, and the Tier is
added to the Tier list:

.. image:: /images/apps/howtocreateapp-8b54f.png

Next click +Add Instance to add a new instance, or select from existing
instances using the Existing tab. Multiple instances can be added to a
single container as well:

.. image:: /images/apps/howtocreateapp-ab55e.png

After adding all instances, click out of the Add Instance pop up to
return to the layout page. Continue to add all Tiers and instances for
your App:

.. image:: /images/apps/howtocreateapp-119c3.png

To configure new or existing instances, hover over the instance name in
the Tier List and click the Settings gear icon. (Instances can also be
fully configured/edited in the Configure tab by clicking next in the
bottom right):

.. image:: /images/apps/howtocreateapp-f3949.png

To link Tiers, hover over a Tier, click the blue circle at the top of a
Tier and drag the arrow over the top of the Tier you would like to link:

.. image:: /images/apps/howtocreateapp-b92f5.png

To remove a Tier or Instance, click the trash icon. Once your App is
built, click Next in the bottom right.

In the Configure tab, you can fully configure your instances if they are
not configured yet, or edit the configurations. If the app was built
with Existing instances, no configuration options are presented:

.. image:: /images/apps/howtocreateapp-5fd9f.png

Once your App is ready, click Complete in the bottom right and your App
will be created, appear in the App section, and if new instances were
used, the instances will be provisioned:

.. image:: /images/apps/howtocreateapp-20fbf.png
