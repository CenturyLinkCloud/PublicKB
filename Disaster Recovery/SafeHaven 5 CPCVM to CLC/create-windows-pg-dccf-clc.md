{{{
  "title": "Create Windows Protection Group, Install LRA and Start Replication- CPCVM to CLC",
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

### Pre-deploy a Recovery Instance(Optional)
It is possible to pre-deploy the recovery instance to speed up the Protection Group Deployment process.
1. Login to Centurylink Cloud Portal https://control.ctl.io/
2. Click on the DR Datacenter.
3. Click on a group where the recovery instance should be deployed.
4. Click on **create**, then select **server**.
5. Deploy a VM using an Ubuntu-14 template that has same NIC and PCI slot number as the production server.
   Please make sure that:
   a. The VM has same CPU and RAM as the source VM.
   b. The recovery vlan is selected to deploy the instance
   
### Create a Windows Protection Group
1. Right click on the **Production SRN** and select **Create Protection Group**.
**NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.  

3. Click **Add a Server**  
   Enter the **Server Name**, **OS Family and OS Version**. 
   Select **LRA** under Mirroring type.
   Enter **IP address**.  
   Enter the **CPU and Memory** so that it matches the production server
   Click **Add**. Click **Next**
   Click **Add** again if more than one VMs are needed in the protection group.

4. Select **Automatically Deploy and Configure New recovery Proxy Servers**. 
    or
   Select **Use pre-deployed proxy recovery server** , if the recovery server has already been deployed
    
   Click **Next**.
    
5. If **Automatic deployment of the new recovery proxy instance** is selected:  
 
    a. Select a **Parent Hardware Group**.    
    b. Enter a **Stub Group Name** if required.  
    c. Select **Linux** as the **OS base for all the Stub machines**  
    d. Enter an **Alias**(maximum 6 characters) for the Recovery Server.  
    e. Select a **Proxy Template**  
**Note** : Make sure that the **Template** you select has the same **NIC and PCI slot number** as the production/source VM.  
    f. Select the **Installed OS on Production Server**.  
    g. In front of **"Connect all the server to"**, select the **DR vlan**. The Recovery instance will be deployed in this particular vlan.  
    h. Enter the **administrator**(or root) password that you want to be set on the Recovery server.  
       Click **Next**.  
    
    **OR**  
      
    If **pre-deployed proxy recovery server** is selected:    
    
    a. **Select** the Recovery server instance from the Recovery Datacenter.  
       Click **Next**.  
    b. Under **Mapping**, click on **select** and select the right recovery instance after clicking on down arrow.  
       Click **Next**.  
    
  6. Enter a **Protection Group Name**.
     Click on the VM name. Click **Add Disk** on the right to the VM. 
     Expand the VM to see the disks attached to it.
     Select a disk and click on **Resize Disk** to change the size of the disk.
     Make sure that the disk layout of the VM matches the production VM.
     Click **Next**.
  
  7. SafeHaven supports two types of protection types. Select a Protection type:
     **Local Replica** : 125% of total production VM's storage on the local SRN and 125% on the DR SRN.
     **Local Cache** : 10% of total production VM's storage on the local SRN and 125% on the DR SRN.   
     Please [click here](../Overview/local-cache-vs-local-replica.md) for more information on difference between local cache and local replica
     
  8. If you selected **Local Replica**:  
     Under **Production Data Center**, Select a **primary storage pool** and **checkpoint storage pool**. It is completly fine to use the same pool for both primary storage and checkpoint storage.  
     Under **Recovery Data Center**, select **Primary storage pool** and **checkpoints storage pool**.  
     
     If you selected **Local Cache**.
     Under **Production Data Center**, Select a **local cache storage pool**
     Under **Recovery Data Center**, select **Primary storage pool** and **checkpoints storage pool**.  It is completly fine to use the same pool for both primary storage and checkpoint storage.  
     Click **Next**
     
   9. Check **Automatically Install Windows LRA** if you want the SafeHaven Agent to be automatically installed on the production/source VM.   
      
      **Note**:  Automatic Installation requires a **reboot of the production server**.  It is advised to use this option only during maintenance window.
   
      Leave the box **unchecked** if automatic installation is not required.  
      Click **Finish**.  
     **Note**: This will Create a Protection group, Deploy a recovery instance and then configure it to boot using iSCSI target from the DR-SRN disk when ever Test-Failover/Failover is performed.  
     **Note**: It may take some time for the PG to be deployed.  
     
   10. If **pre-deployed proxy recovery server** was selected while creating the PG, and the server has not been configured for iscsi boot, then:   
       a. Right click the **Protection group** that was just created.  
       b. Go to **Intallation** > **Install SafeHaven makestub**.  
       c. Verify the Protectiongroup name , and click **Next**.  
       d. Enter the root password of the VM.  
       e. Check all the boxes.  
       f. Click **Next**.
       This will configure the recovery server to boot using iSCSI off the disks of the DR-SRN when a test-failover/failover operation is initiated.
       
       
   
     
     
