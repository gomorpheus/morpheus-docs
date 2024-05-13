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
      #. **Period:** Currently "Year" is the only option
      #. **Year:** Select a year to set budgets for future years. Alternatively, select "custom" to create a multi-year budget or input a custom fiscal year if required by your organization
      #. **Forecast Model:** Optionally apply a forecast model to the Budget. When applied, forecasted amounts for each budget interval will be computed and graphical trend lines will be shown based on the model computation
      #. **Interval:** Choose Month, Quarter, Year then fill in the budgeted amount for that interval (for quarter and year interval Budgets the entered amount is evenly split across the months in the given interval)

  #. Click :guilabel:`SAVE CHANGES`

.. image:: /images/operations/budgets/createBudget.png
  :width: 50%

Multi-year Budgets
^^^^^^^^^^^^^^^^^^

Some organizations may need to create multi-year budgets or may need to set a fiscal year period. By default, annual budgets are tied to a calendar year (January - December) but |morpheus| offers the flexibility of setting a fiscal year period when needed. When selecting a value from the YEAR dropdown in the add/edit budget modal, select "Custom" rather than one of the discreet years from the list. After selecting Custom, START DATE and END DATE fields allow the user to input any desired fiscal year period. Users can enter a period of up to three years using the start and end date bookends. The entered period must be one, two or three full years, partial years are not permitted.

In the example below, I've created a three-year budget:

.. image:: /images/operations/multiBudget.png
  :width: 50%

Budget Monitoring
^^^^^^^^^^^^^^^^^

As the year (or years) goes on, existing Budgets can be reviewed to compare actual spend against the budgeted amount. To access the Budget detail, navigate to |OpeCosBud| and select the desired Budget. The reported actual amount for a given month will be the same as the total cost reported for the month on the Invoice with the same scoping (for the current month, projected cost is used). Depending on the Cloud type, this figure can be pulled from a public clouds live costing API (such as with AWS, Azure, or GCP Clouds) or from the |morpheus| in-built cost metering for private clouds (like VMware).

Example Budget, Cloud-scoped:

.. image:: /images/operations/budget.png

Example Cloud Invoice for the same month:

.. image:: /images/operations/invoice.png

Cloud Budgets
^^^^^^^^^^^^^^

If you scope a budget to a Cloud, visit the Cloud summary tab in ``Infrastructure > Clouds > Select Cloud`` to see a cost-to-budget breakdown for that Cloud.

.. image:: /images/operations/budgets/cloudBudget.png

Budget Analytics
^^^^^^^^^^^^^^^^

In ``Operations > Analytics > Budget Analysis`` select scope (Account, Tenant, Cloud, Group, User) to view the budget analysis. If a budget exists for the selected scope, a cost breakdown against budgeted amounts will be shown.

.. image:: /images/operations/budgets/budgetAnalysis.png
