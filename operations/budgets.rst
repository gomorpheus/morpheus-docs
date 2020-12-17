Budgets
-------

Budgets provide insight into spending across entire accounts, allowing users to create and plan a budget scoped to their account, clouds, tenants, users, or groups.

Creating A Budget
^^^^^^^^^^^^^^^^^^
  #. Navigate to ``Operations > Costing > Budgets``
  #. Create a new budget and enter in the following:

      #. **Name**
      #. **Description**
      #. **Scope:** Here you can choose which construct this budget is tied to (Account, Tenant, Cloud, Group, or User)
      #. **Period**
      #. **Year:** Select a year to set budgets for future years or "custom" to create a multi-year budget or input a custom fiscal year as required by your organization
      #. **Interval:** Choose Month, Quarter, Year then fill in the budget for that interval

  #. :guilabel:`SAVE CHANGES`

.. image:: /images/operations/create_budget.png

Multi-year Budgets
^^^^^^^^^^^^^^^^^^

Some organizations may need to create multi-year budgets or may need to set a fiscal year period. By default, annual budgets are tied to a calendar year (January - December) but |morpheus| offers the flexibility of setting a fiscal year period when needed. When selecting a value from the YEAR dropdown in the add/edit budget modal, select "Custom" rather than one of the discreet years from the list. After selecting Custom, START DATE and END DATE fields allow the user to input any desired fiscal year period. Users can enter a period of up to three years using the start and end date bookends. The entered period must be one, two or three full years, partial years are not permitted.

In the example below, I've created a three-year budget:

.. image:: /images/operations/multiBudget.png
  :width: 50%

Cloud Budgets
^^^^^^^^^^^^^^

If you scope a budget to a cloud visit the cloud summary page in ``Infrastructure > Clouds > Select Cloud > Summary`` for a detailed breakdown of the costing

.. image:: /images/operations/cloud_budget.png

View Budget Summary
^^^^^^^^^^^^^^^^^^^

To view the budget summary, click into the budget to see the actual vs budgeted spend for the interval selected.

To edit the budget just select :guilabel:`EDIT`

.. image:: /images/operations/budget_summary.png

Budget Analytics
^^^^^^^^^^^^^^^^

In ``Operations > Analytics > Budget Analysis`` select scope (Account, Tenant, Cloud, Group, User) to view the budget analysis.

.. image:: /images/operations/budget_analysis.png
