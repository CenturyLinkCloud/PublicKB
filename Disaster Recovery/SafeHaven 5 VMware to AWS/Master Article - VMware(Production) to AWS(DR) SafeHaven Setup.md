{{{
  "title": "Master Article - CLC(Production) to AWS(DR) SafeHaven Setup",
  "date": "12-27-2017",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for VMware(Production) to AWS(DR) use case.

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information](../CLC to AWS/Gather Production Server Information.md)

2. [Determine Storage Requirements](../CLC to AWS/Determine Storage Requirements.md)

3. [Setup AWS for SafeHaven-5 using CloudFormation](../../General/Setup AWS for SafeHaven-5 using CloudFormation.md)

4. [Create Production SRN in VMware]

5. [Create CMS in AWS]

6. [Create DR SRN in AWS]

7. [Create SafeHaven Cluster and Login to SafeHaven Console](../CLC to AWS/Create SafeHaven Cluster and Login to SafeHaven Console.md)

8. [Register Datacenters within SafeHaven Console]

9. [Register SRN within SafeHaven Console]

10. [Add SRN Peer]

11. [Add and Claim Storage on Production SRN in CenturyLink Cloud]

12. [Create Windows Protection Group,Install LRA and Start Replication]

    a. [Modify WAN Replication Rate and Check Replication Status]

    b. [Configure Checkpoints]

    c. [Create Manual Checkpoint]

13. [Create Linux Protection Group]
	
    a. [Install Scripts and Start Replication for Linux Protection Group]
    
    b. [Modify WAN Replication Rate]
    
    c. [Configure Checkpoints]

    d. [Create Manual Checkpoint]

14.  [Configure Email Alerts](../CLC to AWS/Configure Email Alerts.md)
    
15.  [Test Failover to AWS]
 
16.  [Failover to AWS]

17. [AWS Statistics]
