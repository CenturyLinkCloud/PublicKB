{{{
  "title": "Master Article - CLC(Production) to AWS(DR) SafeHaven Setup",
  "date": "12-27-2017",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for CLC(Production) to AWS(DR) use case.

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information]

2. [Determine Storage Requirements]

3. [Setup AWS for SafeHaven-5 using CloudFormation]

4. [Create Production SRN in CenturyLink Cloud]

5. [Create CMS in AWS]

6. [Create DR SRN in AWS]

7. [Create SafeHaven Cluster and Login to SafeHaven Console]

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
    
14.  [Test Failover to AWS]
 
15.  [Failover to AWS]

