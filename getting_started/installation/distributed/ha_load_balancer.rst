Load Balancer Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For configurations with 2 or more Applications Nodes, a load balancer is recommended to ensure high availability (HA) from disruptions and upgrades. Below are the guidelines to configuring a load balancer for |morpheus| but each configuration may differ based on the organization's requirements.

Requirements
````````````

* WebSockets enabled
* Load Balance 443 (optionally redirect 80 to 443)
  * SSL Termination (Offload), Bridging, and Passthrough are supported
* Round-Robin or least connection distribution
* Persistence/sticky sessions configured
* HTTPS monitor ``https://ip_address/ping`` body for ``MORPHEUS PING`` or status of 200, for node operational health

Example configurations
``````````````````````

Below are a few examples of configuring load balancers to meet the needs of a HA configuration.  The examples assume SSL bridging will be used, which means an SSL (TLS) certificate is presented by the load balancer to clients and the load balancer will communicate with the backend nodes via a different (possibly same) certificate.
This configuration is recommended because the |morpheus| application nodes will create self-signed certificates and the load balancer will present a valid certificate to end users.  Aditionally, all communication will eb encrypted.
This reduces the overhead of maintaining the certificates on the |morpheus| application nodes, as the load balancer can ignore invaild certs on the application nodes.
However, the certificates on the |morpheus| application nodes are not required to be self-signed, they can be replaced with other trusted certificates following the `SSL Certificates <https://docs.morpheusdata.com/en/latest/getting_started/additional/morpheusSslCerts.html>`_ documentation.

.. TIP:: The list below is not meant to be a complete list for all load balancers.  The provided examples are common deployments that can be used for reference.  The settings mentioned in the examples list the primary settings that may need to be configured, other settings are based on the organization's needs requirements own configuration.

- .. toggle-header:: :header: **F5 BIG-IP**

  Monitor
  ```````

    - **Type:** HTTPS
    - **Send String:** GET /ping
    - **Receive String:** MORPHEUS PING

  Pool
  ````

    - **Health Monitor:** Select monitor created in the ``Monitor`` section
    - **Load Balancing Method:** Least Connections (member) is recommended (alternatively Round Robin)
    - **Node Service Port:** 443/HTTPS
      
  Virtual Server
  ``````````````

    - **Type:** Standard
    - **Service Port:** 443/HTTPS
    - **Protocol:** TCP
    - **Protocol Profile (Client):** tcp
    - **Protocol Profile (Server):** tcp
    - **HTTP Profile (Client):** http
    - **HTTP Profile (Server):** http
    - **SSL Profile (Client):** clientssl (or preferred profile with a trusted certificate)
    - **SSL Profile (Server):** serverssl
    - **Source Address Translation:** Auto Map
    - **Default Persistence Profile:** <Organization's preference> (hash, source_addr, and cookie are popular)

- .. toggle-header:: :header: **AWS Application Load Balancer (ALB)**

  Target Group
  ````````````

    - **Target Type:** Instances
    - **Protocol/Port:** HTTPS/443
    - **Health Check Protocol:** HTTPS
    - **Health check path:** /ping
    - **Load balancing algorithm:** Least Outstanding Requests is recommended (alternatively Round Robin)
    - **Stickiness Type:** Load balancer generated cookie

  Load Balancer
  `````````````

    - **Network Mappings:** It is recommended to sele
    - **Security Group:** Allow HTTPS/443 Inbound and Outbound
    - **Listener:** HTTPS:443 to the target group created in the ``Target Group`` section
    - **Security Policy:** ELBSecurityPolicy-2016-08