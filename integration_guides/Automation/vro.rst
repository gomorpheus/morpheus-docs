vRealize Orchestrator
---------------------

The vRealize Orchestrator (vRO) Integration provided for |morpheus| enables users to easily trigger existing workflows that may already exist in vRealize Orchestrator. Not only can the user trigger these workflows, but they can also be chained easily into non-vRO workflows and process both output and input parameters of a workflow.

Adding the Integration
^^^^^^^^^^^^^^^^^^^^^^

Setting up the vRO integration involves some steps which vary depending on the authentication model being used.

When using OAUTH, the Client ID must be gathered first. This can be found by browsing a file on the actual VRA server using SSH. On the vRA server, run the following command: ``grep -i cafe_cli= /etc/vcac/solution-users.properties | sed -e ‘s/cafe_cli=//’``

Secondly, you will need the username, password, and host API URL. Typically, the API URL is run on port 8283. A sample API URL may look like the following example: `https://vrahost.com:8283/`

Be sure to fill in the tenant token as the domain or tenant ID, for example: `vsphere.local`, with a username of `administrator@vsphere.local`.

.. NOTE:: At times, this can vary depending on how authentication and role assignments for the user have been set up for vRO.

vRA auth uses vRA identity Bearer tokens for API consumption. The only real difference in field requirements when using this authentication mode is that the `Client ID` is no longer needed.

Using vRealize Orchestrator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the first things |morpheus| does when it is tied into a vRO integration is sync all available workflows by category. These workflows become available when creating a new |morpheus| task in |LibAut|. |morpheus| allows a user to map these vRO workflows into the task engine. The task engine allows users to design workflows that chain tasks in order or operate at different phases of a provisioning request. For more information on tasks, please read the Automation documentation.

Creating a task for VRO is simple.

First, go to |LibAut| and create a new task. Choose a task type of `vRealize Orchestrator Workflow`. A dropdown will appear allowing one to first select the active vRO Integration you would like to use. Once that is selected, a list of workflows becomes available.

.. NOTE:: The next part is where things can get a bit tricky. The parameter body (expected in JSON) format can be a bit difficult to track down. One way is to use the Network Chrome inspector when kicking off a sample workflow from the vRO HTML5 client and grabbing the parameter JSON. Another is to query the API yourself and look at the samples from historical run history.

An exmaple payload for the `SSH / Run SSH Command` Workflow would look like this:

.. code-block:: JSON

  {
      "parameters": [
          {
              "name": "hostNameOrIP",
              "type": "string",
              "value": {
                  "string": {
                      "value": "x.x.x.x"
                  }
              }
          },
          {
              "name": "port",
              "type": "number",
              "value": {
                  "number": {
                      "value": 22
                  }
              }
          },
          {
              "name": "cmd",
              "type": "string",
              "value": {
                  "string": {
                      "value": "echo \"Hello <%=instance.name%>\""
                  }
              }
          },
          {
              "name": "encoding",
              "type": "string",
              "value": {
                  "string": {
                      "value": ""
                  }
              }
          },
          {
              "name": "username",
              "type": "string",
              "value": {
                  "string": {
                      "value": "myuser"
                  }
              }
          },
          {
              "name": "passwordAuthentication",
              "type": "boolean",
              "value": {
                  "boolean": {
                      "value": true
                  }
              }
          },
          {
              "name": "password",
              "type": "string",
              "value": {
                  "string": {
                      "value": "password"
                  }
              }
          },
          {
              "name": "path",
              "type": "string",
              "value": {
                  "string": {
                      "value": "\/var\/lib\/vco\/app-server\/conf\/vco_key"
                  }
              }
          },
          {
              "name": "passphrase",
              "type": "string",
              "value": {
                  "string": {
                      "value": ""
                  }
              }
          }
      ]
  }

Note that all |morpheus| variables can be injected into the parameter body. In the above example we inject the instance name into the sample command with `<%=instance.name%>`.

Adding this task to a workflow allows the result parameters to be referenced in subsequent tasks called throughout the workflow. For example, a local script task type could reference the output text of the above ssh command by injecting the following results map: ``echo "results.vro: <%=results.vro.find{it.name == 'outputText'}?.value?.string?.value%>"``

There are very powerful options available for chaining results and injecting variables relevant to the instance being provisioned or even custom inputs from an operational workflow. Please reference the rest of the Automation documentation for examples.
