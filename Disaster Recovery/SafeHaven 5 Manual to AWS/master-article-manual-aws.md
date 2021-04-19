{{{
  "title": "Master Article - Manual Site(Production) to AWS(DR) SafeHaven Setup",
  "date": "03-21-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Article Overview
This article explains how to setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for Manual Site (Lumen Private Cloud on VMware Cloud Foundation and Hyper-V) to AWS(DR) use case. To read more about a manual site click [here](Introduction to Manual Site.md)

### Prerequisites
* **Network and Ports requirements** - There are certain ports which need to be allowed in between the Production and DR vlans for SafeHaven to work. Please click [**here for Safehaven 5 Network and Ports requirements**](../SafeHaven 5 General/SafeHaven-5.0-Network and Port Requirements.md)

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information](../SafeHaven 5 CLC to AWS/Gather Production Server Information.md)

2. [Determine Storage Requirements](../SafeHaven 5 CLC to AWS/Determine Storage Requirements.md)

3. [Setup AWS for SafeHaven-5 using CloudFormation](../SafeHaven 5 General/Setup AWS for SafeHaven-5 using CloudFormation.md)

4. [Create Production SRN in a Manual Site](Create-Production-SRN-Manual.md)

5. [Create CMS in AWS](../SafeHaven 5 CLC to AWS/Create CMS in AWS.md)

6. [Create DR SRN in AWS](../SafeHaven 5 CLC to AWS/Create DR SRN in AWS.md)

7. [Create SafeHaven Cluster and Login to SafeHaven Console](../SafeHaven 5 CLC to AWS/Create SafeHaven Cluster and Login to SafeHaven Console.md)

8. [Register Datacenters within SafeHaven Console](Register-manual-SafeHaven-Console.md)

9. [Register SRN within SafeHaven Console](../SafeHaven 5 CLC to AWS/Register SRN within SafeHaven Console.md)

10. [Add SRN Peer](../SafeHaven 5 CLC to AWS/Add SRN Peer.md)

11. [Add and Claim Storage on Production SRN in a Manual Site](Add-Claim-Storage-ProdSRN-manual.md)

12. [Create Windows Protection Group,Install LRA and Start Replication](Create-Windows-PG-manual.md)

    a. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)

    b. [Check Replication Status](../SafeHaven 5 CLC to AWS/Check Replication Status.md)

    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](../SafeHaven 5 CLC to AWS/Create Manual Checkpoint.md)

13. [Create Linux Protection Group](Create-Linux-PG-Production-manual.md)

    a. [Install Scripts and Start Replication for Linux Protection Group](../SafeHaven 5 CLC to AWS/Install Scripts and Start Replication for Linux Protection Group.md)

    b. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)

    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](../SafeHaven 5 CLC to AWS/Create Manual Checkpoint.md)

14.  [Configure Email Alerts](../SafeHaven 5 CLC to AWS/Configure Email Alerts.md)

15.  [Test Failover to AWS](../SafeHaven 5 CLC to AWS/Test Failover to AWS.md)

16.  [Failover to AWS](../SafeHaven 5 CLC to AWS/Failover to AWS.md)

17.  [AWS Statistics](../SafeHaven 5 CLC to AWS/AWS Statistics.md)
