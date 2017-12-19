{{{
  "title": "Managed OS Default Windows Monitoring Policy",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This document details the default policy used to monitor supported Windows servers as part of our [Managed OS Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/) offering. 


Managed Windows Default Monitoring Policy

| Type 	| Duration (minutes)   	| Interval (minutes)   	| Details |
| ---	| ---	| ---	| ---	|
| CPU Metrics	| 5   	| 1   	| - |
| Disk Metrics	| 5    	| 1   	| - |
| Memory Metrics	| -    	| 1   	| - |
| Comitted Memory	| 3    	| 1   	| - |
| Disk	| 5    	| 1   	| - |
| Event Log | 1    	| 1   	| System: 8198 WARNING Security-SPP |
| Event Log | 1    	| 1   	| System: 8198 ERROR Security-SPP |
| Event Log | 1    	| 1   	| System: 8198 UnexpectedShutdown |
| Event Log | 1    	| 1   	| System: 1074 USER32 |
| Event Log | 1    	| 1   	| System: 4198 WARNING TCPIP |
| Event Log | 1    	| 1   	| System: 4199 ERROR TCPIP |
| Event Log | 1    	| 1   	| System: 4199 Warning TCPIP |
| Event Log | 1    	| 1   	| System: 4198 ERROR TCPIP |
| Process Queue Length | 5    	| 1   	| Windows CPU Load Check |
| uptime	| 1    	| 1   	| - |
