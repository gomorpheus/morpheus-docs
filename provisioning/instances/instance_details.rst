Instance Details
----------------

The instance detail page is where you can view and fully manage an instance. To get to an instance detail page, navigate to provisioning,
instances, and click on an instance. Please note instance details and actions differ between instance types and user permissions.

There are several sections within an Instance page that provide useful capabilities to the user.

Summary
  Stats and status information
Deploy
  Track deployment history for instance types that support deployments or manually kick off a deployment (only visible for instance types that support deployments)
Settings
  Some instance types support custom configuration settings (i.e. mysql presents the my.ini)
Network
  Useful for configuring security groups and access to the instance.
Monitoring
  Quick summary of the monitoring system and all checks that were configured to test the state of the instance
Backups
  Quick backup dashboard. Useful for viewing historical backups as well as kicking off new ones.
Logs
  View all aggregated logs from the containers or VM's representing the instance.
Environment
  View the environment variables presented to the instances or exported by the instances via Apps (more on this in the Apps section). Even see Imported environment variables that may be referenced by the running instance.
Scale
  For instances that support load balancing and auto scaling. Easily configure auto scaling thresholds and load balancer settings that pertain to a particular instance. When creating a scale schedule for already-provisioned Instances, a timezone selection is not shown because |morpheus| automatically detects the timezone configuration of the web browser.
Console
  Access the instance or container via a client-less Console supporting SSH, RDP, VNC, and even hypervisor level remote consoles.
