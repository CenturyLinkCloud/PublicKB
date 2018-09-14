{{{
  "title": "Managed OS Default Linux Monitoring Policy",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This document details the default policy used to monitor supported Linux servers as part of our [Managed OS Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/) offering. 


Managed Linux Default Monitoring Policy

| Type 	| Duration (minutes)   	| Interval (minutes)   	| Details |
|---	|---	|---	|---	|
| CPU Metrics	| 1   	| 1   	| - |
| Disk Metrics	| 1    	| 1   	| -  |
| Memory Metrics	| 1    	| 1   	| -|
| Disk	| 1    	| 1   	| -|
| Memory	| 3    	| 1   	| -|
| Load Average	| 5    	| 1   	| -|
| Process	| 1    	| 1   	| crond|
| Process	| 1    	| 1   	| ntpd|
| Process	| 1    	| 1   	| rsyslog|
| Swap	| 1    	| 1   	| -|
| uptime	| 1    	| 1   	| -|
| File Check	| 1    	| 1   	| /var/log/messages: Event Log Daemon|
| File Check	| 1    	| 1   	| /var/log/messages: IO Error|
| File Check	| 1    	| 1   	| /var/log/messages: run fsck|
| File Check	| 1    	| 1   	| /var/log/messages: out of memory|
