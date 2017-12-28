{{{
  "title": "Modify WAN Replication Rate and check Replication Status",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

## Article Overview
This article explains how to:

1. Edit WAN Replication Rate for a Protection Group
2. Check replication status for Windows protection groups from SafeHaven Console and LRA Tools

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has been started on the Windows Production Servers.

### Edit WAN Replication Rate for a Protection Group
1. Log in to the SafeHaven Console
2. Click on a protection group, and navigate to the **Properties** tab.
**WAN  Replication Rate** is located under **Replication Monitor **. By default it is limited to 2048 KB/sec.

3. To allow the Protection Group to use maximum available bandwidth, click **Edit** in front of 2048.
Check the box in front of **Maximum Available Bandwidth**. Click **Ok**

### Check Replication Progress
1. RDP to the Windows server you are protecting. Open a command prompt with admin priviledges, and change the directory to C:\Program Files\SafeHaven\tools
```
cd C:\Program Files\SafeHaven\tools
```
2. Execute the following command:
```
C:\Program Files\SafeHaven\tools>DgSyncEx.exe
```
3. Check the status of the synchronization by running the list command
```
DgSyncEx>list
```
###Video Tutorial
<iframe width="560" height="315" src="https://www.youtube.com/embed/D6hQViavsWg" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>

**Next Step** is to [Configure Checkpoints](Configure Checkpoints.md)