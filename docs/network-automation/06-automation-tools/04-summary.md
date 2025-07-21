# Summary

All of the described tools have their advantages and use cases. I would recommend starting with more high-level tools such as NAPALM, Ansible, or Nornir.

```
// This query retrieves time-series data for in/out utilization
// for interfaces with "GWAN" in their description across all devices.

let devices = `analytics:Devices/*`
let timeSeriesData = newDict()

for deviceId, deviceData in devices {
    let interfaces = `analytics:Devices/${deviceId}/versioned-data/interfaces/interface/*`

    for interfaceName, interfaceData in interfaces {
        if interfaceData["description"] is defined && regex(interfaceData["description"], "GWAN") {
            let inUtilPath = `analytics:Devices/${deviceId}/interface/${interfaceName}/utilization/inUtilization`
            let outUtilPath = `analytics:Devices/${deviceId}/interface/${interfaceName}/utilization/outUtilization`

            // Fetch time-series for a given duration (e.g., last 1 hour)
            // You can make this duration dynamic with a dashboard input.
            let inUtilTs = inUtilPath[1h] | field("util")
            let outUtilTs = outUtilPath[1h] | field("util")

            // Add the time series data to the result dictionary,
            // using a descriptive key for each series.
            timeSeriesData[deviceData["hostname"] + " " + interfaceName + " In Utilization"] = inUtilTs
            timeSeriesData[deviceData["hostname"] + " " + interfaceName + " Out Utilization"] = outUtilTs
        }
    }
}

timeSeriesData
```
``
