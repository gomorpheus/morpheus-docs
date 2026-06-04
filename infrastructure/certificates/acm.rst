.. _acm_certificates:

Amazon Certificate Manager (ACM)
=================================

Overview
--------

|morpheus| integrates with Amazon Certificate Manager (ACM) to manage SSL/TLS certificates for AWS resources. This integration allows |morpheus| to provision and manage certificates within AWS, leveraging ACM's automatic renewal and validation capabilities.

ACM certificates managed through |morpheus| can be used with AWS services including:

- Elastic Load Balancers (ALB, NLB, CLB)
- Amazon CloudFront distributions
- Amazon API Gateway endpoints
- AWS Elastic Beanstalk environments

Prerequisites
-------------

- An active AWS Cloud integration in |morpheus|
- IAM permissions for the ACM service:

  - ``acm:RequestCertificate``
  - ``acm:DescribeCertificate``
  - ``acm:ListCertificates``
  - ``acm:DeleteCertificate``
  - ``acm:ImportCertificate``
  - ``acm:GetCertificate``

- For DNS validation: Route 53 permissions or access to the domain's DNS

Configuration
-------------

ACM integration is available automatically when an AWS Cloud is configured in |morpheus|. No additional integration setup is required beyond the AWS Cloud configuration.

Requesting ACM Certificates
----------------------------

To request a new certificate through ACM:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD`
#. Select the ACM certificate type
#. Complete the request fields:

   - **NAME:** A name for the certificate in |morpheus|
   - **AWS CLOUD:** Select the AWS Cloud integration
   - **REGION:** AWS region for the certificate
   - **DOMAIN NAME:** Primary domain for the certificate (e.g., ``example.com``)
   - **ADDITIONAL NAMES:** Subject Alternative Names (SANs) for additional domains
   - **VALIDATION METHOD:** DNS Validation (recommended) or Email Validation

#. Click :guilabel:`REQUEST`

|morpheus| submits the certificate request to ACM. The certificate status will show as "Pending Validation" until domain ownership is verified.

Domain Validation
-----------------

DNS Validation (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ACM provides a CNAME record that must be added to your domain's DNS:

- If the domain is managed in Route 53 through |morpheus|, validation can be completed automatically
- For external DNS, add the provided CNAME record to your DNS zone
- DNS validation records can remain in place for automatic renewal

Email Validation
^^^^^^^^^^^^^^^^^

ACM sends validation emails to domain contacts:

- ``admin@example.com``
- ``administrator@example.com``
- ``hostmaster@example.com``
- ``postmaster@example.com``
- ``webmaster@example.com``

Follow the link in the validation email to approve the certificate request.

Importing Existing Certificates to ACM
----------------------------------------

To import a third-party certificate into ACM through |morpheus|:

#. Navigate to |InfTruCer|
#. Click :guilabel:`+ ADD`
#. Select ACM Import type
#. Provide:

   - **CERTIFICATE BODY:** PEM-encoded certificate
   - **PRIVATE KEY:** PEM-encoded private key
   - **CERTIFICATE CHAIN:** PEM-encoded intermediate certificates

#. Click :guilabel:`IMPORT`

.. NOTE:: Imported certificates are not automatically renewed by ACM. Only certificates requested through ACM receive automatic renewal.

Certificate Renewal
-------------------

Certificates requested through ACM are automatically renewed by AWS:

- ACM begins renewal 60 days before expiration
- DNS-validated certificates renew automatically if the CNAME record is still in place
- Email-validated certificates require re-approval via email
- |morpheus| syncs the renewed certificate data automatically

Certificate Synchronization
----------------------------

|morpheus| synchronizes ACM certificate inventory from AWS:

- Certificates created directly in the AWS Console appear in |morpheus| after sync
- Certificate status (Issued, Pending, Expired, Revoked) is kept current
- Association with AWS resources (ELBs, CloudFront) is tracked

Deleting ACM Certificates
--------------------------

To delete an ACM certificate:

#. Navigate to |InfTruCer|
#. Select the ACM certificate
#. Click :guilabel:`DELETE` from the Actions menu
#. Confirm deletion

.. WARNING:: ACM certificates cannot be deleted while in use by AWS services (load balancers, CloudFront, etc.). Remove the certificate association from all services before deletion.
