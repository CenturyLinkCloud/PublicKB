{{{
  "title": "Master Article - CLC(Production) to CLC(DR) SafeHaven Setup",
  "date": "07-27-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Article Overview
This article explains how to setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for CenturyLink Private Cloud on VMware Cloud Foundation to CLC use case. To read more about a manual site click [here](../SafeHaven 5 Manual to AWS/Introduction to Manual Site.md)

### Prerequisites
* **Network and Ports requirements** - There are certain ports which need to be allowed in between the Production and DR vlans for SafeHaven to work. Please click [**here for Safehaven 5 Network and Ports requirements**](../SafeHaven 5 General/SafeHaven-5.0-Network and Port Requirements.md)

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information](../SafeHaven 5 CLC to AWS/Gather Production Server Information.md)

3. [Create CMS in CLC](create-cms-clc.md)

4. [Create SRNs in CLC](create-srns-clc.md)

5. [Create SafeHaven Cluster and Login to SafeHaven Console](../SafeHaven 5 CLC to AWS/Create SafeHaven Cluster and Login to SafeHaven Console.md)

6. [Register Datacenters within SafeHaven Console](register-datacenters.md)

7. [Register SRN within SafeHaven Console](register-srn-clc-clc.md)

8. [Add SRN Peer](add-srn-peers-clc-clc.md)

9. [Add and Claim Storage on the SRNs](add-claim-storage-clc-clc.md)

10. [Create Windows Protection Group,Install LRA and Start Replication](Create-Windows-pg-Install-LRA-clc-clc.md)

    a. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)

    b. [Check Replication Status](../SafeHaven 5 CLC to AWS/Check Replication Status.md)

    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](Create-manual-checkpoint-clc-clc.md)

11. [Create Linux Protection Group](Create-Linux-pg-clc-clc.md)

    a. [Install Scripts and Start Replication for Linux Protection Group](Install-Scripts-for-Linux-ph-clc-clc.md)

    b. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)

    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](Create-manual-checkpoint-clc-clc.md)

    e. [Configure Recovery Server for a Linux PG](configure-recovery-server-linux-clc-clc.md)

12.  [Configure Email Alerts](../SafeHaven 5 CLC to AWS/Configure Email Alerts.md)

13.  [Test Failover to CLC](Test-Failover-to-CLC.md)

14.  [Failover to CLC](Failover-to-CLC.md)
