{{{
  "title": "Master Article - CLC(Production) to Microsoft Azure(DR) SafeHaven Setup",
  "date": "06-19-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Article Overview
This article explains how to setup SafeHaven at a high level and use SafeHaven for recovery with all the KB article links in order for CLC(Production) to Microsoft Azure(DR) use case.

### Prequisites
1. **CLC to Azure site-to-site VPN** - Please make sure that a VPN exists between the CLC and Azure accounts.

2. **Network and Ports requirements** - There are certain ports which need to be allowed in between the Production and DR vlans for SafeHaven to work. Please click [**here for Safehaven 5 Network and Ports requirements**](../SafeHaven 5 General/SafeHaven-5.0-Network and Port Requirements.md)

### SafeHaven Setup and Recovery Workflow

1. [Gather Production Server Information](../SafeHaven 5 CLC to AWS/Gather Production Server Information.md)

2. [Create Production SRN in CLC](../SafeHaven 5 CLC to AWS/Create Production SRN in CenturyLink Cloud.md)

3. [Create CMS in Azure](CreateCMSAzure.md)

4. [Create DR SRN in Azure](CreateDRSRNAzure.md)

5. [Create SafeHaven Cluster and Login to SafeHaven Console](../SafeHaven 5 CLC to AWS/Create SafeHaven Cluster and Login to SafeHaven Console.md)

6. [Register Datacenters within SafeHaven Console](SiteRegistrationAzure.md)

7. [Register SRN within SafeHaven Console](../SafeHaven 5 CLC to AWS/Register SRN within SafeHaven Console.md)

8. [Add SRN Peer](../SafeHaven 5 CLC to AWS/Add SRN Peer.md)

9. [Add and Claim Storage on the SRNs](../SafeHaven 5 CLC to AWS/Add and Claim Storage on Production SRN in CenturyLink Cloud.md)

10. [Create Windows Protection Group,Install LRA and Start Replication](SafeHaven 5 CLC to AWS/Create-Windows-Protection-Group-Install-LRA-and-Start-Replication.md)

    a. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)

    b. [Check Replication Status](../SafeHaven 5 CLC to AWS/Check Replication Status.md)

    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](../SafeHaven 5 CLC to AWS/Create Manual Checkpoint.md)

11. [Create Linux Protection Group](../SafeHaven 5 CLC to AWS/Create Linux Protection Group.md)

    a. [Install Scripts and Start Replication for Linux Protection Group](../SafeHaven 5 CLC to AWS/Install Scripts and Start Replication for Linux Protection Group.md)

    b. [Modify WAN Replication Rate](../SafeHaven 5 CLC to AWS/Modify WAN Replication Rate.md)

    c. [Configure Checkpoints](../SafeHaven 5 CLC to AWS/Configure Checkpoints.md)

    d. [Create Manual Checkpoint](../SafeHaven 5 CLC to AWS/Create Manual Checkpoint.md)

12.  [Configure Email Alerts](../SafeHaven 5 CLC to AWS/Configure Email Alerts.md)

