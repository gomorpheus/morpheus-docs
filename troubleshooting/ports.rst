Common Ports & Requirements
===========================

The following chart is useful for troubleshooting Agent install, Static IP assignment, Remote Console connectivity, and Image transfers.

.. csv-table:: Common Ports & Requirements
   :header: "Feature", "Method",  "OS", "Source", "Destination", "Port", "Requirement"

   "Agent Communication", "All", "All", "Node", "Appliance", 443, "DNS Resolution from node to appliance url"
   "Agent Install", "All", "Linux", "Node", "Appliance", 80, "Used for appliance yum and apt repos"
   " ", "SSH", "Linux", "Appliance", "Node", 22, "| DNS Resolution from node to appliance url
   | Virtual Images configured
   | SSH Enabled on Virtual Image"
   "","WinRM",Windows,Appliance,Node,5985,"| DNS Resolution from node to appliance url
   | Virtual Images configured
   | WinRM Enabled on Virtual Image(`winrm quickconfig`)"
   " ",Cloud-init,Linux, , , ,"| Cloud-init installed on template/image
   | Cloud-init settings populated in User Settings or in `Admin –> Provisioning`
   | Agent install mode set to Cloud-Init in Cloud Settings"
   " ",Cloudbase-init,Windows, , , ,"| Cloudbase-init installed on template/image
   | Cloud-init settings populated in User Settings or in `Admin –> Provisioning`
   | Agent install mode set to Cloud-Init in Cloud Settings"
   " ",VMtools,All, , , ,"| VMtools installed on template
   | Cloud-init settings populated in Morpheus user settings or in `Administration –> Provisioning` when using Static IP’s
   | Existing User credentials entered on Virtual Image when using DHCP
   | RPC mode set to VMtools in VMware cloud settings."
   "Static IP Assignment/IP Pools",Cloud-Init,All, , , ,"| Network configured in Morpheus (Gateway, Primary and Secondary DNS, CIDR populated, DHCP disabled)
   | Cloud-init/Cloudbase-init installed on template/image
   | Cloud-init settings populated in Morpheus user settings or in `Administration –> Provisioning`"
   " ", "VMware Tools",All, , , ,"| Network configured in Morpheus (Gateway, Primary and Secondary DNS, CIDR populated, DHCP disabled)
   | VMtools installed on Template/Virtual Image"
   Remote Console,SSH,Linux,Applaince,Node,22,"| ssh enabled on node
   | user/password set on VM or Host in Morpheus "
   " ",RDP,WIdnows,Appliance,Node,3389,"| RDP Enabled on node
   | user/password set on VM or Host in Morpheus"
   " ",Hypervisor Console,All,Appliance,ESXi Host,5900-6000+,"| GBB server opened on all ESXii host firewalls
   | *Port range req's vary per env
   | ESXi host names resolvable by morpheus appliance"
   "Morpheus Catalog Image Download", ,All,Amazon S3,Appliance,443,"Available space at ``/var/opt/morpheus/``"
   "Image Transfer",Stream,All,Appliance,Datastore,443,"Hypervisor Host Names resolvable by Morpheus Appliance"


---
