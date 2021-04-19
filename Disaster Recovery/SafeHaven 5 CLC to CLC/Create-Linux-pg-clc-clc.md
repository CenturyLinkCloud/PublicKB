{{{
  "title": "Create Linux Protection Group",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a Linux Protection Group when the source site and recovery site are in CLC

### Requirements
Access to the SRNs in Lumen Cloud and permissions to add raw disks to it.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Both production and recovery SRNs have been registered and peered
3. Storage on both SRNs is added and claimed.


### Create Recovery Server
A recovery server boots off of disks of the DR SRN when a test failover/ failover operation is issued. 
1. Go to Lumen Cloud Portal.
2. Go to the Dr Data center, and create a Group for the recovery server by clickin on **Create** and then selecting **Group**
3. Click on the group, on the right click on **Create** and select **Server**.
   Make sure that correct datacenter and group are selected.  
   Keep the default **Standard** server type.
   Select an **Operating System**. The operating system should be same as the production server.  
   **Note** : It is very important to select the same operating system.  
   Enter an **admin/root password**  
   Give same **CPU** and **memory** as the production server.  
   Select the recovery vlan in **network**.  
   Click **Create server**.
   Enter the **Name** of the server.  
   Provide a **description** for the server.  


### Create a Linux Protection Group
1. Right click on the **Production SRN** and click **Create Protection Group**.

   **NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.

3. **Select the servers** from the production data center that you want to include in the Protection Group.

   **NOTE**: Only one Linux server can be selected per Protection Group.

4. a. **Select** the Recovery server instance from the Recovery Datacenter.  
      Click **Next**.  
   b. Under **Mapping**, click on **select** and select the right recovery instance after clicking on down arrow.  
      Click **Next**.  
    
5. Enter a **Protection Group Name**.
   Click on the VM name. Click **Add Disk** on the right to the VM. 
   Expand the VM to see the disks attached to it.
   Select a disk and click on **Resize Disk** to change the size of the disk.
   Make sure that the disk layout of the VM matches the production VM.
   Click **Next**.
   
6. If you selected **Local Replica**:  
   Under **Production Data Center**, Select a **primary storage pool** and **checkpoint storage pool**. It is completly fine to use the same pool for both primary storage and checkpoint storage.  
   Under **Recovery Data Center**, select **Primary storage pool** and **checkpoints storage pool**. 
   Click **Next**
7. Click **Finish**.

**Note**: It may take a few minutes for the the protection group to be created.


