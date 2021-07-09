Budgets
-------

Budgets provide insight into spending across their designated scope, allowing users to create and plan a budget targeted to their account, clouds, tenants, users, or groups.

Creating A Budget
^^^^^^^^^^^^^^^^^^
  #. Navigate to ``Operations > Costing > Budgets``
  #. Start a new budget by clicking :guilabel:`+ ADD`

      #. **Name**
      #. **Description**
      #. **Scope:** Here you can choose which construct this budget is tied to (Account, Tenant, Cloud, Group, or User)
      #. **Period**: Currently "Year" is the only option
      #. **Year:** Select a year to set budgets for future years. Alternatively, select "custom" to create a multi-year budget or input a custom fiscal year if required by your organization
      #. **Interval:** Choose Month, Quarter, Year then fill in the budgeted amount for that interval

  #. Click :guilabel:`SAVE CHANGES`

.. image:: /images/operations/budgets/createBudget.png
  :width: 50%

Multi-year Budgets
^^^^^^^^^^^^^^^^^^

Some organizations may need to create multi-year budgets or may need to set a fiscal year period. By default, annual budgets are tied to a calendar year (January - December) but |morpheus| offers the flexibility of setting a fiscal year period when needed. When selecting a value from the YEAR dropdown in the add/edit budget modal, select "Custom" rather than one of the discreet years from the list. After selecting Custom, START DATE and END DATE fields allow the user to input any desired fiscal year period. Users can enter a period of up to three years using the start and end date bookends. The entered period must be one, two or three full years, partial years are not permitted.

In the example below, I've created a three-year budget:

.. image:: /images/operations/multiBudget.png
  :width: 50%

Cloud Budgets
^^^^^^^^^^^^^^

If you scope a budget to a Cloud, visit the Cloud summary tab in ``Infrastructure > Clouds > Select Cloud`` to see a cost-to-budget breakdown for that Cloud.

.. image:: /images/operations/budgets/cloudBudget.png

View Budget Summary
^^^^^^^^^^^^^^^^^^^

To view the budget summary, click into the budget to see a breakdown of budgeted amounts against actual costs for the selected interval period. Budgets can be edited or deleted by clicking the pencil or trash can icons, respectively, for each budget.

.. image:: /images/operations/budgets/budgetSummary.png

Budget Analytics
^^^^^^^^^^^^^^^^

In ``Operations > Analytics > Budget Analysis`` select scope (Account, Tenant, Cloud, Group, User) to view the budget analysis. If a budget exists for the selected scope, a cost breakdown against budgeted amounts will be shown.

.. image:: /images/operations/budgets/budgetAnalysis.png
