Load Balancer Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For configurations with 2 or more Applications Nodes, a load balancer is recommended to ensure high availability (HA) from disruptions and upgrades. Below are the guidelines to configuring a load balancer for |morpheus| but each configuration may differ based on the organization's requirements.

Requirements
````````````

* WebSockets enabled
* Load Balance 443 (optionally redirect 80 to 443)
  
  * SSL Termination (Offload), Bridging, and Passthrough are supported
  
* Round-Robin or least connection distribution
.. * Persistence/sticky sessions configured
* HTTPS monitor ``https://ip_address/ping`` body for ``MORPHEUS PING`` or status of 200, for node operational health

Example configurations
``````````````````````

Below are a few examples of configuring load balancers to meet the needs of a HA configuration.  The examples assume SSL bridging will be used, which means an SSL (TLS) certificate is presented by the load balancer to clients and the load balancer will communicate with the backend nodes via a different (possibly same) certificate.
This configuration is recommended because the |morpheus| application nodes will create self-signed certificates and the load balancer will present a valid certificate to end users.  Additionally, all communication will be encrypted.
This reduces the overhead of maintaining the certificates on the |morpheus| application nodes, as the load balancer can ignore invaild certs on the application nodes.
However, the certificates on the |morpheus| application nodes are not required to be self-signed, they can be replaced with other trusted certificates following the `SSL Certificates <https://docs.morpheusdata.com/en/latest/getting_started/additional/morpheusSslCerts.html>`_ documentation.

.. TIP:: The list below is not meant to be a complete list for all load balancers.  The provided examples are common deployments that can be used for reference.  The settings mentioned in the examples list the primary settings that may need to be configured, other settings are based on the organization's needs requirements and own configuration.

.. toggle-header:: :header: **F5 BIG-IP**

  **Monitor**

    - **Type:** HTTPS
    - **Send String:** GET /ping
    - **Receive String:** MORPHEUS PING

  **Pool**

    - **Health Monitor:** Select monitor created in the **Monitor** section
    - **Load Balancing Method:** Least Connections (member) is recommended (alternatively Round Robin)
    - **Node Service Port:** 443/HTTPS
    
  **Virtual Server**

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
  ..  - **Default Persistence Profile:** <Organization's preference> (hash, source_addr, and cookie are popular)

.. toggle-header:: :header: **AWS Application Load Balancer (ALB)**

  **Target Group**

    - **Target Type:** Instances
    - **Protocol/Port:** HTTPS/443
    - **Health Check Protocol:** HTTPS
    - **Health check path:** /ping
    - **Load balancing algorithm:** Least Outstanding Requests is recommended (alternatively Round Robin)
  ..  - **Stickiness Type:** Load balancer generated cookie

  **Load Balancer**

    - **Security Group:** Allow HTTPS/443 Inbound and Outbound
    - **Listener:** HTTPS:443 to the target group created in the **Target Group** section
    - **Security Policy:** ELBSecurityPolicy-2016-08

.. toggle-header:: :header: **HAProxy**

  **Example configuration file**

  .. code-block:: bash

    #---------------------------------------------------------------------
    # Example configuration for a possible web application.  See the
    # full configuration options online.
    #
    #   https://www.haproxy.org/download/1.8/doc/configuration.txt
    #
    #---------------------------------------------------------------------

    #---------------------------------------------------------------------
    # Global settings
    #---------------------------------------------------------------------
    global
        log         127.0.0.1:514 local2
        chroot      /var/lib/haproxy
        pidfile     /var/run/haproxy.pid
        maxconn     4000
        user        haproxy
        group       haproxy
        daemon

        # turn on stats unix socket
        stats socket /var/lib/haproxy/stats

        # utilize system-wide crypto-policies
        ssl-default-bind-ciphers PROFILE=SYSTEM
        ssl-default-server-ciphers PROFILE=SYSTEM

    defaults
        mode                    http
        log                     global
        option                  httplog
        option                  dontlognull
        option http-server-close
        option forwardfor       except 127.0.0.0/8
        option                  redispatch
        retries                 3
        timeout http-request    10s
        timeout queue           1m
        timeout connect         10s
        timeout client          1m
        timeout server          1m
        timeout http-keep-alive 10s
        timeout check           10s
        maxconn                 3000

    frontend main
        mode http
        bind *:443 ssl crt /etc/haproxy/ssl/combined_crt_key.pem
        default_backend             mybackend

    backend mybackend
        mode http
        option      httpchk
        http-check  send meth GET uri /ping
        http-check  expect string MORPHEUS\ PING
        balance     leastconn
        server      app1 192.168.101.1:443 check ssl verify none
        server      app2 192.168.101.2:443 check ssl verify none
        server      app3 192.168.101.3:443 check ssl verify none  

|