{{{
  "title": "Create Linux Protection Group with Production site in Lumen Private Cloud on VMware Cloud Foundation",
  "date": "02-06-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach a RAW disk to Production SRN in Lumen Private Cloud on VMware Cloud Foundation and create a Linux Protection Group.

### Requirements
Access to the Production SRN in Lumen Private Cloud on VMware Cloud Foundation and permissions to add raw disks to it.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Both production and recovery SRNs have been registered and peered


### Attach and Claim RAW Disks on Production SRN in DCCF.
1. Login to DCC portal. Confirm the Storage requirements for the Production Server (in this case Windows). Click the production VM, and go to **Hardware** tab to see the total provisioned storage. Based on the Production Server O.S. Type and [Storage Requirements](../SafeHaven 5 CLC to AWS/Determine Storage Requirements.md), calculate the amount of storage that needs to be added.

2. Click the **SRN** you want to add storage to, and go to **Hardware** tab.  

Add two raw disks
**First RAW disk**: Add a single **raw disk** amounting to "100% of the total used storage(full copy of data)" on Production Linux Server.
For example, if the VM that needs to be protected has 3 disks of size 1GB, 2GB and 14GB, then add a 17GB raw disk to the production SRN.

**Second RAW disk**: Add a second **raw disk** for checkpoints retention. The minimum size of this raw disk should be 5% of the disk added in step 4.
For example, if you added a 17GB disk in step 1, then please add a second raw disk of roughly 1GB.

3. Click **Add**, and enter the size of the disk. Add one more disk using the same method.

4. Click **Ok**. This successfully adds 2 hard disks to the SRN

**NOTE**: For **Production SRN in Hyper-V**, please add same storage as above, and then follow the steps below.

**NOTE**: There is no need to allocate storage for the SRN on AWS, depending on the size of your Protection Group SafeHaven will automatically create the EBS volumes to meet the requirements.

5. Once the storage has been attached to the SRN, the next step is to login to the **SafeHaven Console**.
6. Go to the Navigation Tree and select the Production SRN. In the **Properties Panel** select **Claim Storage Pool**.  

   **NOTE**: If you don't see a device listed click on **Rescan** in order to force a rescan of the SCSI bus on the SRN.  
   **NOTE**: Do not claim the First RAW disk added in **Step 4** above. Select the Second RAW disk added for Checkpoint retention in **Step 5** above. Select the Storage Device you want to claim, and select **Create a New Storage Pool for the Device**. Fill in the **Storage Pool Name**, and click **Claim**.

### Create a Linux Protection Group
1. Right click on the **Production SRN** and click **Create Protection Group**.

   **NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.

3. Enter the **Server Name**, **IP address**, and select **Linux** in OS type.
   Click **Add**. Click **Next**

   **NOTE**: Only one Linux server can be selected per Protection Group.

4. Choose a name for the Protection Group. Check the **Edit** box.  
   Expand the VM to edit disk layout. You can select an existing disk and change its size to match the production server.   
   If the production VM has more than 1 disks, click **add disk** to add more disks.  
   Click **Next**  

   **Note**: Make sure that disk layout matches the production VM.

5. Select a **RAW/Hard disk**. Please select the First RAW disk that we added in previous section's step 3.

7. Once the correct **Checkpoint Pool** is selected, click **Next**.

8. Please read the acknowledgement, and check the box.

9. Verify the Protection Group summary, and click **Create**.

**Next Step** is to [Install Scripts and Start Replication for Linux Protection Group](../SafeHaven 5 CLC to AWS/Install Scripts and Start Replication for Linux Protection Group.md)
