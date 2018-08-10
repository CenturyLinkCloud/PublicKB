{{{
  "title": "Run custom script upon failover for Linux PG",
  "date": "07-17-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to configure custom scripts to run upon failover for Linux Protection Groups.

### Requirements
1. Initial Replication is complete for the Protection Group and checkpoints are available for Failover.
2. Custom script execution is only supported in in-band modes, so as not to interfere with the configuration of a production system. Therefore it is supported for CLC and Manual sites as DR destinations, and not for Azure or AWS. 

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available. This article assumes that Test Failover has been done successfully.

### Run custom script upon failover for Linux PG
Users may not choose to perform Network Isolation in case of an actual Failover event.

1. SSH to the Linux server on production.

2. Custom scripts can be executed if dropped into the following folder: **/opt/datagardens/startup/etcRemote/scripts.d/**

3. Scripts need to be marked executable (chmod +x) in order to be run, and will be run as part of the system startup (after mounting local fileystems and initializing network interfaces).

**Note:** There is no restriction as to the source format, binary executables will likewise run. Executables placed into the scripts.d folder will be run in alphabetical order. Hence an ordering of scripts can be enforced by prefixing the script name with a number, e.g. 01_, 02_, .....
