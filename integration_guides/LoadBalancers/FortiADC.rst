FortiADC
--------

Add FortiADC Load Balancer
^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a FortiADC Load Balancer Integration:

#. Navigate to :menuselection:`Infrastructure --> Load Balancers`
#. Select :guilabel:`+ ADD`
#. Select **FortiADC** from the drop-down list. The NEW LOAD BALANCER panel opens.
#. Configure the following:

   GROUP
     From the drop-down list, select the group for the load balancer.
   CLOUD
     From the drop-down list, select the cloud that hosts the load balancer.
   NAME
     Enter the load balancer name.
   DESCRIPTION
     Identifying information displayed on the load balancer list page.
   API URL
     Enter the URL of the FortiADC API. For example, ``http://10.30.21.55``.
   API PORT
     Enter the FortiADC API port. For example, ``80``
   USERNAME
     Enter FortiADC service account username.
   PASSWORD
     Enter FortiADC service account password.
   VIRTUAL NAME
     Enter the naming pattern for new FortiADC Virtual Servers. If blank, defaults to ``morph_lb_${loadBalancer.id}``.
   SERVICE NAME
     Enter the naming pattern for new FortiADC Services. If blank, defaults to ``morph_service_${container.id}``.
   SERVER NAME
     Enter the naming pattern for new FortiADC Servers. If blank, defaults to ``morph_server_${server.id}``.

#. Click :guilabel:`SAVE CHANGES`.
