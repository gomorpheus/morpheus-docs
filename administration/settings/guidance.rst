Overview
^^^^^^^^

|moprheus| guidance is an important tool that makes recommendations for resource and cost optimization. It analyzes CPU, memory, and storage activities over time to make intelligent recommendations on sizing and power state. These recommendations can free up resources and save organizations significant amounts of money over time. Out of the box, |morpheus| is configured for sensible thresholds used in making these recommendations but they can be edited here if needed.

Power Settings
``````````````

|morpheus| will recommend shutting down a resource if *all* three of the baselines in this section are exceeded.

- **Average CPU (%):** Shutdown will be recommended if the average CPU usage is below this value. Values over 100% are possible as this value factors the number of CPU cores. Default value: 75
- **Maximum CPU (%):** Shutdown will be recommended if the CPU usage never exceeds this value. Values over 100% are possible as this value factors the number of CPU cores. Default value: 500
- **Network Threshold (bytes):** Shutdown will be recommended if the average network bandwidth is below this value. Default value: 2000 bytes/second

CPU Up-size Settings
````````````````````

CPU up-size will be recommended when *both* of the following baselines are exceeded for a resource.

- **Average CPU (%):** CPU up-size is recommended if the average CPU percentage exceeds this value (and other criteria are also met). Default value: 50
- **Maximum CPU (%):** CPU up-size is recommended if the maximum CPU percentage exceeds this value. Default value: 99

Memory Up-size Settings
```````````````````````

- **Minimum Free Memory (%):** Memory up-size will be recommended if free memory dips below this value. Default value: 10

Memory Down-size Settings
`````````````````````````

Memory down-size will be recommended when both of the following thresholds are met for a resource.

- **Average Free Memory (%):** Memory down-size is recommended if the average free memory is above this value. Default value: 60
- **Maximum Free Memory (%):** Memory down-size is recommended if free memory has never dipped below this value. Default value: 30
