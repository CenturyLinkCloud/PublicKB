{{{
  "title": "Create Linux Protection Group with Production site in vCenter",
  "date": "01-16-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach a RAW disk to Production SRN in Lumen Cloud and create a Linux Protection Group.

### Requirements
Access to the Production SRN in Lumen Cloud and permissions to add raw disks to it.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Both production and recovery SRNs have been registered and peered

### Attach and Claim RAW Disks on Production SRN in VMWare vCenter.
1. Login to your vcenter, right click the production server and click on **Edit Settings**. Confirm the Storage requirements for the Production Server (in this case Linux) by taking all the hard disks into account. Based on the Production Server O.S. Type and [Storage Requirements](../SafeHaven 5 CLC to AWS/Determine Storage Requirements.md), calculate the amount of storage that needs to be added.

2. In the Navigation Tree, right click the **SRN** you want to add storage to, and click **Edit Settings**.

Add two raw disks
**First RAW disk**: Add a single **raw disk** amounting to "100% of the total used storage(full copy of data)" on Production Linux Server.
For example, if the VM that needs to be protected has 3 disks of size 1GB, 2GB and 14GB, then add a 17GB raw disk to the production SRN.

**Second RAW disk**: Add a second **raw disk** for checkpoints retention. The minimum size of this raw disk should be 5% of the disk added in step 4.
For example, if you added a 17GB disk in step 1, then please add a second raw disk of roughly 1GB.

3. Click **Add**, and select **Hard Disk**. click **Next**

4. Select **Create a new virtual disk**, and click Next

5. Enter the **disk size**, select **Thick Provision Lazy Zeroed**, then select **Store with the virtual machine**. Click **Next**.

6. Keep the default **Virtual Device Node**, that is SCSI(0:1). Click **Next**.

7. Click **Finish**. Repeat steps 3 to 7 to add a second disk.

8. Click **Ok** on the main edit settings window. This successfully adds 2 hard disks to the SRN

**NOTE**: There is no need to allocate storage for the SRN on AWS, depending on the size of your Protection Group SafeHaven will automatically create the EBS volumes to meet the requirements.

9. Once the storage has been attached to the SRN, the next step is to login to the **SafeHaven Console**.
10. Go to the Navigation Tree and select the Production SRN. In the **Properties Panel** select **Claim Storage Pool**.  

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

**Next Step** is to [Install Scripts and Start Replication for Linux Protection Group](../SafeHaven 5 CLC to AWS/Install Scripts and Start Replication for Linux Protection Group.md)
