Load Balancers
==============

``Infrastructure -> Load Balancers``

Overview
--------

|morpheus| can provision VM or Container HaProxy Load Balancers, Amazon Elastic and Application Load Balancers, Azure Load Balancers, and integrates with several external Load Balancers, including F5, A10, Citrix, and AVI.

Once created or integrated, Load Balancers are available as an option to be added during provision time or post-provisioning.

Once a Load Balancer is added to an instance, you can manually scale or configure auto-scaling based on thresholds or schedules, and burst across clouds with cloud priority.

.. NOTE:: HaProxy VM Load Balancer option, Load Balancer detail pages, Balance Mode, Sticky Mode and Shared VIP address option are available in |morpheus| 2.11.3+.

.. image Load_Balancers___|morpheus| .png

In the Load Balancers page there are two sections:

Load Balancers
  View or edit existing Load Balancers, add new Load Balancers.
Virtual Servers
  View and link to Instances that are attached to load balancers.

Load Balancers
--------------
The Load Balancers tab list currently available Load Balancers, which you can select, edit or delete, and is where you can create new or integrate with external Load Balancers.

Add a new Load Balancer
.......................

Select + LOAD BALANCER, chose an option, and fill in the required information:

A10 (aXAPI v3)
  * API Host
  * API Port
  * Username
  * Password
  * Internal IP
  * Public IP
  * VIP Address
  * VIP Port

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
  * Managment URL

F5 LineRate
  * API Host
  * API Port
  * Username
  * Password
  * Internal IP
  * Public IP
  * VIP Address
  * VIP Port

HaProxy Container (Internal, will create a HaProxy container, must have available docker host to provision to)
  * Group
  * Cloud
  * Name
  * Description
  * Plan
    * Select the size of HaProxy container to be provisioned

//HAProxy VM (Internal, will provision a HaProxy VM into selected cloud)
//Group
//Cloud
//Name
//Description
//Plan- Select size of HaProxy VM to be provisioned

Upon saving your new Load Balancer will be added to the Load Balancers list and available in the Load Balancer dropdown in the Provisioning Wizard Automation Section for Instance Types that have scaling enabled.

Load Balancer Detail Pages
..........................

In the main Load Balancer page, select an existing Load Balancer to go to that Load Balancers Details Page, which lists Stats, Settings, Actions and Virtual Servers for that load balancer.

Virtual Servers
---------------
