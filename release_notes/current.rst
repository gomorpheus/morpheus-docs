.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - NSX-T load balancers can now be created and managed from |morpheus| API and CLI :superscript:`5.4.2`


Fixes
=====

:NSX-T: - Fixed an issue preventing Subtenant users from creating load balancer virtual servers using load balancer SSL profiles they've just created :superscript:`5.4.2`
         - Improvements made to smooth the process of creating Tier-0 routers for NSX-T :superscript:`5.4.2`
         - Setting NSX-T distributed firewall rules by IP address now works correctly :superscript:`5.4.2`


Appliance & Agent Updates
=========================

:Appliance: - Embedded Elasticsearch Log4j updated to v2.17 (CVE-2021-45105).  :superscript:`5.4.2`
             - Embedded Elasticsearch jackson-databind updated to 2.13.1 (CVE-2020-25649) :superscript:`5.4.2`
             - Embedded Elasticsearch jackson-dataformat-cbor updated to 2.13.1 (CVE-2020-28491) :superscript:`5.4.2`
:Agent: - Linux Agent version updated to v2.2.2 :superscript:`5.4.2`
        - Log4j removed from Linux Agent, replaced with Slf4j :superscript:`5.4.2`
:Node Packages: - Node and VM Node Package versions updated to v3.2.4 :superscript:`5.4.2`
                - Java jdk & jre updated to 11.0.13+8 :superscript:`5.4.2`

.. ..