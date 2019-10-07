{{{
  "title": "Modify WAN Replication Rate",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to Edit WAN Replication Rate for a Protection Group.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has been started on the Windows Production Servers.

### Edit WAN Replication Rate for a Protection Group
1. Log in to the SafeHaven Console
2. Click on a protection group, and navigate to the **Properties** tab.
**WAN  Replication Rate** is located under **Replication Monitor**. By default it is limited to 2048 KB/sec.

3. To allow the Protection Group to use maximum available bandwidth, click **Edit** in front of 2048.
Check the box in front of **Maximum Available Bandwidth**. Click **Ok**

**Note**: The procedure is same for CLC/VMWare/Manual sites as source datacenters.

**Next Step** is to [Check Replication Status](Check Replication Status.md)
