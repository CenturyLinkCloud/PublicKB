{{{
  "title": "Create Windows Protection Group, Install LRA and Start Replication- DCCF to CLC",
  "date": "04-30-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create Windows Protection Group and protect a Windows server Automatically as well as Manually.

### Requirements
1. To protect a Windows server using SafeHaven, we need to install a Local Replication Agent (LRA) on the production server. In order to complete the LRA installation, a **Reboot** of the production server is required. **Please schedule a downtime window for LRA installation.**

2. For Ansible LRA installation to work, make sure TCP 445 port Inbound is open on the production server by running the following command via Windows Commandline (run as administrator):
```
New-NetFirewallRule -DisplayName "psexec tcp 445" -Name "psexec tcp 445" -Profile Any -LocalPort 445 -Protocol TCP
```
### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully
2. Both production and recovery SRNs have been registered and peered
3. Proper storage has been attached and claimed on the production SRN

### Prepare a Recovery Server Template
A Recovery Server template is 

### Create a Windows Protection Group
1. Right click on the **Production SRN** and select **Create Protection Group**.
**NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.  

3. Enter the **Server Name**, **IP address**, and select **Windows** in OS type.
   Click **Add**. Click **Next**
   Click **Add** again if more than one VMs are needed in the protection group.

4. Enter a name for the Protection Group. Check the **Edit** box.  
   Expand the VM to edit disk layout. You can select an existing disk and change its size to match the production server.   
   If the production VM has more than 1 disks, click **add disk** to add more disks.  
   Click **Next**  
   
   **Note**: Make sure that disk layout matches the production VM.
