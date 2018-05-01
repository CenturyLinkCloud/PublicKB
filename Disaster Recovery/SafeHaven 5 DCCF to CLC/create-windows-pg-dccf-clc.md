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

### Create a Recovery Server Template
A Recovery Server template can make Protection group deployment easier if there are multiple production servers with same NIC and PCI slot. Please[ click here](recovery-template.md) for a KB article to create a recovery server template. 

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
   
 5. Select **Automatically Deploy and Configure New recovery Proxy Servers**. Click **Next**.
 
 6. Select a **Parent Hardware Group**.    
    Enter a **Stub Group Name** if required.  
    Select **Linux** as the **OS base for all the Stub machines**  
    Enter an **Alias**(maximum 6 characters) for the Recovery Server.  
    Select a **Proxy Template**  
**Note** : Make sure that the **Template** you select has the same **NIC and PCI slot number** as the production/source VM.  
    
    Select the **Installed OS on Production Server**.  
    In front of **"Connect all the server to"**, select the **DR vlan**. The Recovery instance will be deployed in this particular vlan.   
    Enter the **administrator**(or root) password that you want to be set on the Recovery server.  
    Click **Next**.
    
  7. Enter a **Protection Group Name**.
     Click on the VM name. Click **Add Disk** on the right to the VM. 
     Expand the VM to see the disks attached to it.
     Select a disk and click on **Resize Disk** to change the size of the disk.
     Make sure that the disk layout of the VM matches the production VM.
     Click **Next**.
  
  8. Select a Protection type:
     **Local Replica** : 125% of total production VM's storage on the local SRN and 125% on the DR SRN.
     **Local Cache** : 10% of total production VM's storage on the local SRN and 125% on the DR SRN.   
     Please [click here](../Overview/local-cache-vs-local-replica.md)More information on difference between local cache and local replica
     
  9. If you selected **Local Replica**:  
     Under **Production Data Center**, Select a **primary storage pool** and **checkpoint storage pool**. It is completly fine to use the same pool for both primary storage and checkpoint storage.  
     Under **Recovery Data Center**, select **Primary storage pool** and **checkpoints storage pool**.  
     
     If you selected **Local Cache**.
     
     
