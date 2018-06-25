Morpheus Agent
===============

The |morpheus| agent is an important and powerful facet of the |morpheus| platform.  After an initial brownfield discovery users can decided to convert unmanaged vms to managed. **The agent is not required** to by |morpheus| to become a managed instance but it does provide numerous additional benefits when it is utilized. Once a vm is managed it can run workflows, have expiration/shutdown policies and can help reign in environments amongst other things.  The |morpheus| agent is very lightweight and secure.


Key Agent Features
-------------------
* Provides key statics (disc usage, CPU usage)
* Handles log aggregation
* Very secure and does not require credentials to get into box.
* SSH agent can be disabled and still get access to the box.
* Agent can be installed over Cloud Init for internetless situations
*  **The |morpheus| agent is optional**
* Makes a single connect over HTTPs and runs as a service
* Health checks for Linux (not available on windows)
* **No inbound Ports**
