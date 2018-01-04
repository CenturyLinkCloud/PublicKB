{{{
  "title": "SafeHaven-4 Monitor Windows IO Statistics",
  "date": "02-22-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}
### Article Overview
For SafeHaven-4.0.1 and later released, there is a built-in monitoring tool shipped with the Windows SafeHaven agent. This document shows how to enable this tool to get statistics of the Windows disk IOs for a given period of time. It is a useful tool to have in order to determine the sufficient amount of WAN replication bandwidth for a given a workload, particularly for those busy servers that may be having problem meeting the recovery point objective (RPO). 

###  Disk Monitoring

By default, the monitoring is turned off.  To turn it on, simply run the ```DgSyncEx``` command with Administrator privileges 
* first select the disk that needs to be monitored
```
DgSyncEx> select disk 0
```
* then  enable statistics monitoring
```
DgSyncEx> set stats on
```
* then the ```stats``` command would report on the IO statistics from enabling monitoring to current time, for example,

```
DgSyncEx>stats

DgReportDiskUsageStats: Disk usage statistics for Disk #0:

"Collect disk usage statistics" is ON.

Start time: 13132276047620385 microseconds (13132276047620 miliseconds)
End time  : 13132276074343870 microseconds (13132276074343 miliseconds)
Difference: 26723485 microseconds (26723 miliseconds)

READ STATS:
  Count      : 86
  Sum        : 1129984 Bytes (1 MB)
  Average    : 0.04 MB/s

WRITE STATS:
  Count 512  : 18
  Count x512 : 49
  Count 4096 : 97
  Count x4096: 103
  Count All  : 152
  Sum 512    : 19470848 Bytes (18 MB)
  Sum 4096   : 515072 Bytes (0 MB)
  Sum All    : 19985920 Bytes (19 MB)
  Average    : 0.73 MB/s

FAILED WRITE STATS:
  Count      : 0
  Sum        : 0 Bytes (0 MB)

SYNC STATS:
  Count      : 0
  Sum        : 0 Bytes (0 MB)
  Average    : 0.00 MB/s

FAILED SYNC STATS:
  Count      : 0
  Sum        : 0 Bytes (0 MB)

DgSyncEx>
```

There is very little performance impact by turning on the monitoring feature. In order to turn it off, you can run
```
DgSyncEx> set stats off
```
