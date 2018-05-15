{{{
  "title": "Master Article - DCCF(Production) to DCC-F(DR) - SafeHaven Setup",
  "date": "05-09-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Article Overview
This article explains how to setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for DCC-F to DCC-F use case. To read more about a manual site click [here](../SafeHaven 5 Manual to AWS/Introduction to Manual Site.md)

### Prerequisites
* **Network and Ports requirements** - There are certain ports which need to be allowed in between the Production and DR vlans for SafeHaven to work. Please click [**here for Safehaven 5 Network and Ports requirements**](../SafeHaven 5 General/SafeHaven-5.0-Network and Port Requirements.md)

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information](../SafeHaven 5 CLC to AWS/Gather Production Server Information.md)

2. [Create Production SRN in DCCF](../SafeHaven 5 Manual to AWS/Create-Production-SRN-Manual.md)

3. [Create CMS in CLC](../SafeHaven 5 Manual to AWS/Create-Production-SRN-Manual.md)  
   
4. [Create DR SRN in CLC](../SafeHaven 5 Manual to AWS/Create-Production-SRN-Manual.md)

5. [Create SafeHaven Cluster and Login to SafeHaven Console](../SafeHaven 5 CLC to AWS/Create SafeHaven Cluster and Login to SafeHaven Console.md)

6. [Register Datacenters within SafeHaven Console]

7. [Register SRN within SafeHaven Console](../SafeHaven 5 CLC to AWS/Register SRN within SafeHaven Console.md)

8. [Add SRN Peer](../SafeHaven 5 CLC to AWS/Add SRN Peer.md)

9. [Add and Claim Storage on the SRNs]

10. [Create Windows Protection Group,Install LRA and Start Replication]

    a. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)
    
    b. [Check Replication Status](../SafeHaven 5 CLC to AWS/Check Replication Status.md)
    
    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](../SafeHaven 5 CLC to AWS/Create Manual Checkpoint.md)

11. [Create Linux Protection Group]
	
    a. [Install Scripts and Start Replication for Linux Protection Group](../SafeHaven 5 CLC to AWS/Install Scripts and Start Replication for Linux Protection Group.md)
    
    b. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)
    
    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](../SafeHaven 5 CLC to AWS/Create Manual Checkpoint.md) 
    
    e. [Configure Recovery Servrer]()

12.  [Configure Email Alerts](../SafeHaven 5 CLC to AWS/Configure Email Alerts.md)
    
13.  [Test Failover to CLC]
 
14.  [Failover to CLC]

