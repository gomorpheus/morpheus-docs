Approvals plugin
````````````````

Integrate Morpheus with your own ITSM solution

Setup
.....
This plugin will enable you to create configuration for several aspects of Approvals within Morpheus.

Integration
...........
A new Integration Type will be created when this plugin is installed.
You are able to customize the ``OptionType`` for the new Integration using the ``ApprovalProvider.integrationOptionTypes`` method.
These ``OptionType`` will be visible when creating the new Integration in the Morpheus UI (|AdmInt|).

Policies
........
Policies (|AdmPol| in the Morpheus UI) define the conditions in which approval is required for provisioning.
Custom ``OptionType`` can be defined for Policy creation by implementing the ``ApprovalProvider.policyOptionTypes`` method.

Create Approval
...............

``ApprovalProvider.createApprovalRequest`` is called after a Provision Request is created.
Here is where you can send the request to your ITSM.
Each ``Request`` will have one or more ``RequestReference`` for each resource associated with the provision request.

.. important:: It is important that you specify an ``externalId`` in the ``RequestResponse`` and each ``RequestReference`` so that Morpheus can track the approval status.

The ``integrationOptionTypes`` you specified are available in the method argument ``Policy.configMap``

.. code-block:: groovy

   String itsmEndpoint = accountIntegration.configMap?.cm?.plugin?."itsm-endpoint"

and the ``policyOptionTypes`` you specified are available in the method argument ``AccountIntegration.configMap``.

.. code-block:: groovy

   String myPolicyConfigValue = policy.configMap?."my-policy-config-option"

Monitor Approval
................
At a regular interval, Morpheus checks for Request approvals. In the ``ApprovalProvider.monitor`` method define your logic for retrieving a list of approval requests in your ITSM solution.

Approval ``RequestReference`` should be returned with one of the following ``ApprovalStatus``:

- ``requesting``
- ``requested``
- ``error``
- ``approved``
- ``rejected``
- ``cancelled``

Integration Logo
................

A custom logo can be used in the Morpheus UI by placing an image at ``src/assets/images/{plugin-code}.png``.
Recommended file size is 180 x 60 px.

-----

|
|
