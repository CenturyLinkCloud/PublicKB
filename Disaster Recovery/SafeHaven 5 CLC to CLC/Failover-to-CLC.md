{{{
  "title": "Failover to CLC",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to initiate Failover to CLC using SafeHaven incase of a disaster scenario where Production Datacenter is unavaiable and users lose access to the Production Server.

### Requirements
1. Access to the SafeHaven console (GUI).
2. Initial Replication is complete for the Protection Group and checkpoints are available for Failover.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available. This article assumes that Test Failover has been done successfully.

**NOTE**: It is strongly recommended that users must peform a Test Failover before doing an actual Failover even incase of a disaster scenario to verify the integrity of data in the recovery datacenter as a first step. Refer to [Test Failover to CLC](test-failover-dccf-clc.md) for more information.

### Failover to CLC
Users may not choose to perform Network Isolation incase of an actual Failover event.

1. To initiate Failover, right-click on the appropriate Protection Group in the Navigation Tree and click **Failover** from the drop-down menu. The Failover wizard appears.

2. In most cases, you will want to Failover to the most recent checkpoint, however, by clicking in the Checkpoint column you can pick an earlier checkpoint as appropriate. Choose the desired checkpoint from the Checkpoint History table. Click **Next**.

3. Wait till **Failover** and **Power On** complete, click on **Finish** to close the wizard.

7. You can go to the **Active iSCSI Sessions** tab to monitor the booting procedure, once the RDP port is open, you can log in to the recovery server to verdify the data consistancy.

The procedure is same for VMWare/Manual sites as source datacenters.
