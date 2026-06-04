.. _lb_policies:

Load Balancer Policies and Rules
---------------------------------

Overview
^^^^^^^^

Load Balancer Policies define traffic management rules that control how requests are routed, redirected, or modified by the load balancer. Policies contain one or more rules, and each rule can match on specific conditions (such as URI path, hostname, or header values) and perform actions (such as forwarding to a pool, redirecting, or rewriting).

Policy management is available for load balancer types that support policy-based routing (such as F5 BIG-IP and NSX-T).

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Load Balancers`` role permission at **Full** level is required to create, edit, or delete policies and rules.
- ``Infrastructure: Load Balancers`` role permission at **Read** level allows viewing policies and rules only.

Viewing Policies
^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Load Balancers``
#. Click the name of a Load Balancer to view its detail page
#. Select the **POLICIES** tab

The Policies tab lists all policies configured for the load balancer, including:

- **Name** — Policy name
- **Description** — Policy description
- **Rules** — Number of rules defined within the policy

Creating a Policy
^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Load Balancers``
#. Click the name of a Load Balancer
#. Select the **POLICIES** tab
#. Click :guilabel:`+ ADD`
#. Configure the policy fields:

   NAME
     A descriptive name for the policy.
   DESCRIPTION
     Optional description of the policy's purpose.

   .. NOTE:: Additional fields are displayed based on the load balancer type. These are defined by the provider's policy option types.

#. Click :guilabel:`SAVE CHANGES`

Deleting a Policy
^^^^^^^^^^^^^^^^^

#. Navigate to the Load Balancer detail page
#. Select the **POLICIES** tab
#. Click the delete icon next to the policy
#. Confirm the deletion

.. WARNING:: Deleting a policy that is currently assigned to a virtual server may disrupt traffic routing. Ensure no active virtual servers reference the policy before removing it.

Policy Rules
^^^^^^^^^^^^

Each policy contains one or more rules that define match conditions and actions. Rules are evaluated in order and the first matching rule's action is applied.

Viewing Rules
`````````````

#. Navigate to the Load Balancer detail page
#. Select the **POLICIES** tab
#. Click the name of a policy to expand its rules list

Creating a Rule
```````````````

#. Navigate to the Policy detail view
#. Click :guilabel:`+ ADD RULE`
#. Configure the rule fields:

   NAME
     A descriptive name for the rule.
   MATCH CONDITIONS
     Define the criteria that must be met for the rule to apply. Conditions vary by load balancer type and may include:

     - **URI Path** — Match on request URI path (e.g., ``/api/*``)
     - **Hostname** — Match on the Host header value
     - **HTTP Method** — Match on GET, POST, PUT, etc.
     - **Header** — Match on a specific HTTP header value
     - **Source IP** — Match on client source IP address or range

   ACTIONS
     Define what happens when the rule matches:

     - **Forward to Pool** — Send traffic to a specific backend pool
     - **Redirect** — Return an HTTP redirect response
     - **Reject** — Return a rejection response
     - **Rewrite** — Modify the request URI or headers before forwarding

   .. NOTE:: Available match conditions and actions depend on the load balancer type and are defined by the provider's policy rule option types.

#. Click :guilabel:`SAVE CHANGES`

Deleting a Rule
```````````````

#. Navigate to the Policy detail view
#. Click the delete icon next to the rule
#. Confirm the deletion

Using Policies with Virtual Servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating or editing a Virtual Server, policies can be selected from the **POLICIES** field. The available policies are filtered to those belonging to the same load balancer. Policies are evaluated in the order they are assigned to the virtual server.
