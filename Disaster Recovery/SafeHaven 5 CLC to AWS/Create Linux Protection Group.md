{{{
  "title": "Create Linux Protection Group",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach a RAW disk to Production SRN in CenturyLink Cloud and create a Linux Protection Group.

### Requirements
Access to the Production SRN in CenturyLink Cloud and permissions to add raw disks to it.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Both production and recovery SRNs have been registered and peered

### Attach and Claim RAW Disks on Production SRN in CenturyLink Cloud
1. Login to CLC Control portal https://control.ctl.io, select **Servers** under the **Infrastructure** tab. Confirm the Storage requirements for the Production Server (in this case Linux). Based on the Production Server O.S. Type and [Storage Requirements](Determine Storage Requirements.md), calculate the amount of storage that needs to be added.

2. In the Navigation Tree, select the **SRN** you want to add storage to, then scroll down on the main data panel and select **edit storage**.
3. Select **add storage** and then in the drop-down menu select **raw disk**.  
   **NOTE**: **DO NOT** select a **partitoned** disk.

4. First RAW disk: Add a single **raw disk** amounting to "100% of the total used storage(full copy of data)" on Production Linux Server.
For example, if the VM that needs to be protected has 3 disks of size 1GB, 2GB and 14GB, then add a 17GB raw disk to the production SRN.

5. Second RAW disk: Add a second **raw disk** for checkpoints retention. The minimum size of this raw disk should be 5% of the disk added in step 4.
For example, if you added a 17GB disk in step 1, then please add a second raw disk of roughly 1GB.

6. Add required storage and **apply**. Wait for the job to complete.  
**NOTE**: There is no need to allocate storage for the SRN on AWS, depending on the size of your Protection Group SafeHaven will automatically create the EBS volumes to meet the requirements.

7. Once the storage has been attached to the SRN, the next step is to login to the **SafeHaven Console**.
8. Go to the Navigation Tree and select the Production SRN. In the **Properties Panel** select **Claim Storage Pool**.  

   **NOTE**: If you don't see a device listed click on **Rescan** in order to force a rescan of the SCSI bus on the SRN.  
   **NOTE**: Do not claim the First RAW disk added in **Step 4** above. Select the Second RAW disk added for Checkpoint retention in **Step 5** above. Select the Storage Device you want to claim, and select **Create a New Storage Pool for the Device**. Fill in the **Storage Pool Name**, and click **Claim**.

### Create a Linux Protection Group
1. Right click on the **Production SRN** and click **Create Protection Group**.

   **NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.

3. **Select the servers** from the production data center that you want to include in the Protection Group.

   **NOTE**: Only one Linux server can be selected per Protection Group.

4. Choose a name for the Protection Group, and click **Next**.

5. Select a **RAW/Hard disk**. Please select the First RAW disk that we added in previous section's step 4.

7. Once the correct **Checkpoint Pool** is selected, click **Next**.

8. Please read the acknowledgement, and check the box.

9. Verify the Protection Group summary, and click **Create**.

**Next Step** is to [Install Scripts and Start Replication for Linux Protection Group](Install Scripts and Start Replication for Linux Protection Group.md)
