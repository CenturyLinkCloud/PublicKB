{{{
  "title": "Master Article - CLC(Production) to AWS(DR) SafeHaven Setup",
  "date": "12-27-2017",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Article Overview
This article explains how to setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for CLC(Production) to AWS(DR) use case.

### Prequisites
1. **CLC to AWS Site-to-site VPN** - Please make sure that a VPN exists between the CLC and AWS accounts. Please click [**here for the clc to aws site-to-site VPN KB article**] (../SafeHaven 5 General/aws-clc-site-to-site.md).

2. **Network and Ports requirements** - There are certain ports which need to be allowed in between the Production and DR vlans for SafeHaven to work. Please click [**here for Safehaven 5 Network and Ports requirements**](../SafeHaven 5 General/SafeHaven-5.0-Network and Port Requirements.md)

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information](Gather Production Server Information.md)

2. [Determine Storage Requirements](Determine Storage Requirements.md)

3. [Setup AWS for SafeHaven-5 using CloudFormation](../SafeHaven 5 General/Setup AWS for SafeHaven-5 using CloudFormation.md)

4. [Create Production SRN in CenturyLink Cloud](Create Production SRN in CenturyLink Cloud.md)

5. [Create CMS in AWS](Create CMS in AWS.md)

6. [Create DR SRN in AWS](Create DR SRN in AWS.md)

7. [Create SafeHaven Cluster and Login to SafeHaven Console](Create SafeHaven Cluster and Login to SafeHaven Console.md)

8. [Register Datacenters within SafeHaven Console](Register Datacenters within a SafeHaven Console.md)

9. [Register SRN within SafeHaven Console](Register SRN within SafeHaven Console.md)

10. [Add SRN Peer](Add SRN Peer.md)

11. [Add and Claim Storage on Production SRN in CenturyLink Cloud](Add and Claim Storage on Production SRN in CenturyLink Cloud.md)

12. [Create Windows Protection Group,Install LRA and Start Replication](Create-Windows-Protection-Group-Install-LRA-and-Start-Replication.md)

    a. [Modify WAN Replication Rate](Modify WAN Replication Rate.md)
    
    b. [Check Replication Status](Check Replication Status.md)

    c. [Configure Checkpoints](Configure Checkpoints.md)

    d. [Create Manual Checkpoint](Create Manual Checkpoint.md)

13. [Create Linux Protection Group](Create Linux Protection Group.md)
	
    a. [Install Scripts and Start Replication for Linux Protection Group](Install Scripts and Start Replication for Linux Protection Group.md)
    
    b. [Modify WAN Replication Rate](Modify WAN Replication Rate.md)
    
    c. [Configure Checkpoints](Configure Checkpoints.md)

    d. [Create Manual Checkpoint](Create Manual Checkpoint.md)  

14.  [Configure Email Alerts](Configure Email Alerts.md)
    
15.  [Test Failover to AWS](Test Failover to AWS.md)
 
16.  [Failover to AWS](Failover to AWS.md)

17. [AWS Statistics](AWS Statistics.md)
