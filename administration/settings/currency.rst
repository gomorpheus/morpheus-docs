Currency Settings
^^^^^^^^^^^^^^^^^

In |morpheus|, Tenants are separate environments which can be defined as using currencies that are unique from one Tenant to the next. In addition, these currencies may be different from the currency in which Price Sets have been defined. In order to present pricing to Subtenant users in their designated currency, |morpheus| allows for integration with currency conversion services "open exchange rates" and "fixer.io". This article goes through the process of setting up the integration and how it works to determine pricing conversions.

Integrating With a Currency Exchange Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to |AdmSetApp|
#. Under the Currency Settings heading, make a "Currency Provider" selection
#. Enter your "Provider API Key"

The service is now integrated and can be used as described in the next section.

Consuming Currency Exchange in |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currency exchange data is synced from the integrated provider once every 12 hours. When needed, Morpheus will use this cached data to present currency conversions rather than hitting the API directly each time. This limits the total number of API hits and reduces costs.

Exchanged currency values will be shown under conditions similar to the following scenario:

A user is working in a Subtenant configured for Currency B. The user is attempting to provision an instance with pricing sets that have only been defined in Currency A. Morpheus will convert the pricing data from currency A to Currency B for this user (and all users in this Subtenant) since price conversion has been enabled.
