{{{
  "title": "Configure Checkpoints",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to Configure Checkpoints for a Protection Group.

### Requirements
1. Access to the SafeHaven Console (GUI).
2. Initial replication has been completed for the Protection Group.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has been completed for the Protection Group.

### Enable periodic Checkpoints
Before enabling the periodic checkpoints please make sure that the replication is complete.

1. Click the protection group and navigate to the **Properties** tab.
2. Click on **Configure Checkpoints** under **Checkpoints** section.
3. Check the box in front of **Enable Periodic Checkpoints** and enter the **Checkpoint Interval** based on the RTO/RPO requirements.
4. Check the box in front of **Enable Scheduled Checkpoints**. These checkpoints will be VSS checkpoints for Windows on a best-effort basis.
5. Put the number of scheduled checkpoints, as well as total number of checkpoints/AMI's that need to be retained per protected server.
6. Click **Finish**
7. Wait for a few checkpoints to show up in the **Checkpoint History** tab before proceeding with any recovery operation like Test-Failover or Failover.

**Note**: The procedure is same for VMWare/Manual sites as source datacenters.

**Next Step** is to [Configure Email Alerts](Configure Email Alerts.md).

**NOTE**: **At this point the user MUST setup SafeHaven email alerts to receive regular cluster email reports as well as reports incase there is an outage in the Production datacenter. This is an absolutely critical piece for a complete DR solution.**
