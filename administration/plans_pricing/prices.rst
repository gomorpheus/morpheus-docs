Pricing
---------


Price Sets
^^^^^^^^^^^

Price sets combine Prices and then attach to Plans. Prices must be created prior to creating Price Sets, but it is recommended to review the Price Set Type options prior to creating Prices.

Price Unit
  Select the Price Unit to use for the Price Set.

  -  Minute
  -  Hour
  -  Day
  -  Month
  -  Year
  -  Two Year
  -  Three Year
  -  Four Year
  -  Five Year

  .. NOTE:: Only Prices configured with matching Price Units can be used in a Price Set.
  .. NOTE:: Month is equivalent to 30 days by default. For AWS, month is 30.5 days. For Azure, month is 30.4 days.

Types
  Price Set Types determine what prices the Set is composed of.

  .. NOTE:: Make note of the Price set options below before creating Prices.

Everything
  'Everything' price sets require 1 or more 'Everything' price types and may include 'Platform' or 'Software' price types.

Compute + Storage
  'Compute + Storage' price sets require at least one of each 'Memory  CPU' and 'Disk Only' price types and may include 'Platform' or 'Software' price types.

Component
  'Component' price sets require at least one of each 'Memory', 'Cores', 'CPU', and 'Storage' price types and may include 'Platform' or 'Software' price types.

Prices
  Search for and select Prices to be added to the Price Set. One of each Price Type required for the Price Set Type selected must be added for the Price Set to save.

Price Types
^^^^^^^^^^^^

- Everything

  - One price for all resources Memory, CPU, RAM, and Disks

- Memory + CPU
- Memory Only
- Cores Only
- Disk Only
- Platform
- Software

Price Units
^^^^^^^^^^^^
-  Minute
-  Hour
-  Day
-  Month
-  Year
-  Two Year
-  Three Year
-  Four Year
-  Five Year

Currency
^^^^^^^^^

-  AUD
-  CHF
-  DKK
-  EUR
-  GBP
-  IDR
-  ILS
-  MAD
-  NOK
-  NZD
-  ROL
-  SEK
-  TRL
-  USD
-  XAF
-  XCD
-  XOF
-  XPF
-  ZAR (South African Rand)

Cost
^^^^^

The base cost of the resource(s). The Price will match the Cost unless a
Price Adjustment is added.

Price Adjustment
^^^^^^^^^^^^^^^^^

None
  Default, no markup added and Price will match Cost
Fixed Markup
  A fixed amount added to the Cost. Price will equal Cost + Markup.
Percentage Markup
  Adds a percentage markup to Cost. Price equals `Cost + (Cost x Markup %)`
Custom Price
  Sets a Price independent from the Cost. If the Cost changes, a Custom Price will not.
