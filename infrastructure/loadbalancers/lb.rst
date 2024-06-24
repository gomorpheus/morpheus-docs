Load Balancers
==============

``Infrastructure > Load Balancers``

Overview
--------

|morpheus| can provision VM or Container HaProxy Load Balancers, Amazon Elastic and Application Load Balancers, Azure Load Balancers, and integrates with several external Load Balancers, including F5, Citrix, and AVI.

Once created or integrated, Load Balancers are available as an option to be added during provision time or post-provisioning.

Once a Load Balancer is added to an instance, you can manually scale or configure auto-scaling based on thresholds or schedules, and burst across clouds with cloud priority.

.. image Load_Balancers___|morpheus| .png

In the Load Balancers page there are two sections:

Load Balancers
  View or edit existing Load Balancers, add new Load Balancers.
Virtual Servers
  View and link to Instances that are attached to load balancers.

**Group and Tenant Access**

Load balancers can be configured to provide specific Group and Tenant access, if desired. **Group Access** controls which Groups at provision time will have access to the load balancer resource. Only workloads being provisioned to the selected Groups would have visibility to the load balancer. Workloads provisioned to other Groups would not see the load balancer as an available selection. **Tenant Permissions** control which Tenants may see the load balancer. Public visibility allows access to the load balancer for users in all Tenants (subject to additional RBAC controls) while Private visibility allows access only for selected Tenants. Select all that may apply.

Load Balancers
--------------

The Load Balancers tab list currently available Load Balancers, which you can select, edit or delete, and is where you can create new or integrate with external Load Balancers.

Add a new Load Balancer
^^^^^^^^^^^^^^^^^^^^^^^

Select + LOAD BALANCER, chose an option, and fill in the required information:

Amazon ALB
  * Scheme
  * Internal
  * Internet-Facing
  * Amazon Subnets (Select + to add additional)
    * Specify the subnets to enable for your load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones to increase the availability of your load balancer.

  * Amazon Security Groups (Select + to add additional)

AVI
  * API Host
  * API Port
  * Username
  * Password
  * Internal IP
  * Public IP
  * VIP Address
  * VIP Port

Azure Load Balancer
  * Cloud
  * Resource Group
    * Populated from cloud selection

Citrix NetScaler
  * API Host
  * API Port
  * Username
  * Password

F5 BigIP (v11.4+)
  * API Host
  * API Port
  * Username
  * Password
  * Management URL

FortiADC
 * API HOST
 * API PORT
 * USERNAME
 * PASSWORD
 * INTERFACE (synced on auth)

HaProxy Container (Internal, will create a HaProxy container, must have available docker host to provision to)
  * Group
  * Cloud
  * Name
  * Description
  * Plan
    * Select the size of HaProxy container to be provisioned

NSX-T Load Balancer
  * NSX-T
  * Name
  * Description
  * Enabled
  * Admin State
  * Size
  * Tier-1 Gateways
  * Log Level

    .. HAProxy VM (Internal, will provision a HaProxy VM into selected cloud)
    .. Group
    .. Cloud
    .. Name
    .. Description
    .. Plan- Select size of HaProxy VM to be provisioned

Upon saving your new Load Balancer will be added to the Load Balancers list and available in the Load Balancer dropdown in the Provisioning Wizard Automation Section for Instance Types that have scaling enabled.

Load Balancer Detail Pages
``````````````````````````

In the main Load Balancer page, select an existing Load Balancer to go to that Load Balancers Details Page, which lists Stats, Settings, Actions and Virtual Servers for that load balancer.

Orchestrating Load Balancers
----------------------------

A large part of application orchestration and automation involves tying various web services and backend services into different load balancer configurations. If the automation tool is unable to communicate or integrate with this aspect of your infrastructure, a lot of gaps will be created in the full orchestrated flow of application deployment. This is why Morpheus provides deep integration with load balancers and explicit definitions with catalog items as to how they are connected to provisioned instances. Some of the functionality includes:

* Public Cloud Load Balancer Support
* Private Cloud Load Balancer Support
* Port Type definitions (Profiles like HTTP/HTTPS or UDP)
* SSL Certificate Management and SSL Certificate Upload
* SSL Passthrough or Forced Redirect

Not only does Morpheus have an ability to provision HAProxy based load balancer containers for easy consumption in development environments, but also has direct tie ins with several Load Balancer Types:

* F5 BigIP
* Netscaler
* NSX Advanced Load Balancer
* Amazon ELB
* Amazon ALB
* Azure Load Balancer
* Fortinet
* Openstack Octavia
* HA Proxy
* NSX-T

Morpheus exposes configuration options during provisioning of an Instance relevant and common to each supported LB Integration. In some cases, Morpheus also provides direct management and sync support for VIP configurations on the various Load Balancers (such as F5, and NSX Advanced Load Balancer), However in a day to day orchestrated workflow this would not be the ideal means by which a user should consume load balancer services.

By tying the Load Balancer associations into the provisioning of instances and the definition of the instance catalog item, the lifecycle of the VIP can more easily be maintained throughout the lifecycle of whatever application may be deployed.

Setting up an Instance for Load Balancer Consumption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several of the provided Morpheus instance types are ready to go with load balancer orchestration out of the box (Apache, Nginx, Tomcat, Node.js, etc). It is also fairly easy to extend existing generic instance types during provisioning to be tied to load balancers or to set up said catalog items in advanced for such functionality.

When creating a custom Instance Type (in |Lib|), one can define a list of exposed ports that the node type within the instance exposes.  When defining these exposed ports it prompts for a Name, Port Number, and LB Type. The LB Type is what enables load-balancer functionality. This can either be HTTP,HTTPS, or TCP. This specification helps build the correct profile for the VIP as well as setup the appropriate types of Health Monitors within the target load balancer integration.

Now, when a user consumes this custom instance type (either through single instance provisioning or full application blueprint provisioning), a section appears in the Automation phase of provisioning. Each port that is defined that exposes a load-balancer gets a dropdown to choose which load balancer integration attach to the exposed port and various prompts become available.

These prompts control features ranging from target VIP Address to selecting an SSL Certificate to be applied to the VIP. These SSL Certificates will even go so far as to create SSL Profiles in integrations for things like an F5 automatically for the application.

Once the instance is provisioned, as part of the final phase, the load balancer configuration will be applied and maintained on the instance. This association can be manipulated after the fact via the "Scale" tab found on the Instance Detail page.

Another benefit to associating load-balancers this way is that the pool members are automatically maintained during scaling events, either via auto-scaling thresholds or manual node additions / removals.

.. include:: /infrastructure/loadbalancers/f5.rst
.. include:: /infrastructure/loadbalancers/netscaler.rst
