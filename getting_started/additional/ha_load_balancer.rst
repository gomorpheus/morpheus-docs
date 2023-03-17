Load Balancer Configuration
---------------------------

For configurations with 2 or more Applications Nodes, a load balancer is recommended to ensure high availability (HA) from disruptions and upgrades. Below are the guidelines to configuring a load balancer for |morpheus| but each configuration may differ based on the organization's requirements.

Requirements
^^^^^^^^^^^^

* WebSockets enabled
* Load Balance 443 (optionally redirect 80 to 443)
  
  * SSL Termination (Offload), Bridging, and Passthrough are supported
  
* Round-Robin or least connection distribution
.. * Persistence/sticky sessions configured
* HTTPS monitor ``https://ip_address/ping`` body for ``MORPHEUS PING`` or status of 200, for node operational health

Example configurations
^^^^^^^^^^^^^^^^^^^^^^

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

  **Example** ``/etc/haproxy/haproxy.cfg`` **configuration file**

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

.. toggle-header:: :header: **Azure Application Gateway**

  In this example, it is assumed **End-To-End TLS Encryption** is being used, which means the Application Gateway will present a certificate
  to the clients and the backend nodes will present the **same** certificate.

  If a setting is not mentioned, it is assumed that the default can be maintained.

  **General Settings**

    - **Tier:** Standard V2
    - **Capacity type:** **Autoscale** or **Manual** are both supported
    - **HTTPS2:** Disabled

  **Frontend Configuration**

    - **Type:** Set **Public** if |morpheus| should be accessilbe externally, otherwise choose **Private**
    - **Public IP Address:** Associate a previously create public IP or create a new one

  **Listener**

    - **Frontend IP:** Choose the IP created from the Frontend Configuration above
    - **Protocol:** HTTPS
    - **Port:** 443
    - **Certificate:**
      - Upload the public certificate in **PFX** format
      - This certificate should match the one presented by the backend nodes
      - The certificate should include the entire chain, including the private key
    - **Listener type:** Basic
    - **Error page URL:** No
  
  **Backend Settings**

    - **Backend protocol:** HTTPS
    - **Backend port:** 443
    - **Use well known CA certificate:**
      - If set to **Yes**, the certificate does not need to be uploaded in the settings.  This must be a well known certificate provided by a
        well known certificate authority, not an internally generated certificate
      - If set to **No**, ensure the certificate that is present on the backend nodes is uploaded to the Application Gateway.
         Note that the certificate should include the entire chain (CA, Intermediates, Certificate)
    - **Cookie-based affinity:** Disable
    - **Connection draining:** Enable
    - **Override with new host name:** No
    - **Use Custom probe:** No (one will be created next and will be assoicated during that configuration)
  
  **Health Probe**

    - **Protocol:** HTTPS
    - **Host:** Enter the host that is configured on the |morpheus| application nodes.  This same host that will be used on the Application Gateway
      Example:  morpheus.mydomain.com
    - **Pick host name from backend settings:** No
    - **Pick port from backend settings:** Yes
    - **Path:** /ping
    - **Use probe matching conditions:** Yes
    - **HTTP response status code match:** 200-399
    - **Backend settings:** Choose the backend settings created above
  
  **Backend Pool**

    - The **Target Type** can either be **Virtual Machine** or **IP address or FQDN**
    - If |morpheus| is hosted in Azure, **Virtual Machine** will likely be the choice
    - If |morpheus| is hosted on-premise or outside of Azure, the **IP address or FQDN** can be used but the
      load balancer will need to able to communicate with the target

  **Important Items**

    - Ensure the backend virtual machines allow port 443 from the load balancer, otherwise a **502 error** may be seen
    - If using a wildcard certificate, you **must** use a custom health probe, as mentioned above, otherwise you may see the following error message:
      `The Common Name (CN) of the backend server certificate does not match the host header entered in the health probe configuration (v2 SKU) or the FQDN in the backend pool (v1 SKU). Verify if the hostname matches with the CN of the backend server certificate.`
      More info:
      https://techcommunity.microsoft.com/t5/fasttrack-for-azure/walkthrough-configuring-end-to-end-tls-with-application-gateway/ba-p/3269132
    - As mentioned above, ensure the complete chain for the certificate is presented by |morpheus|, otherwise you may see the following error message:
      `The root certificate of the server certificate used by the backend does not match the trusted root certificate added to the application gateway. Ensure that you add the correct root certificate to whitelist the backend`
      More info:
      https://learn.microsoft.com/en-us/answers/questions/150524/the-root-certificate-of-the-server-certificate-use
    - Configuring the certificate on the |morpheus| nodes
      More info:
      https://docs.morpheusdata.com/en/latest/getting_started/additional/morpheusSslCerts.html
    - Additional reading:
      https://learn.microsoft.com/en-us/azure/application-gateway/certificates-for-backend-authentication
      https://learn.microsoft.com/en-us/azure/application-gateway/end-to-end-ssl-portal
      https://learn.microsoft.com/en-us/azure/application-gateway/ssl-overview

|