{{{
  "title": " Add and Claim Storage on Production SRN in VMWare",
  "date": "01-11-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach storage on a single SRN in VMWare. After the SRN has been registered with the SafeHaven Console, the next step is to attach storage to it before creating Protection Groups.

**NOTE**: For ease of management and troubleshooting it is recommended that the user creates one Storage Pool per Protection Group.

### Requirements
1. Access to the Production SRN in VMWare
2. Access to the SafeHaven Cluster

### Assumptions
This article assumes that the user has already registered the SRN within the SafeHaven Console and wants to add storage to the SRN before creating Protection Groups.

### Add storage to the Production SRN in Lumen Cloud
1. Login to VMWare Vcenter. Confirm the Storage requirements for the Production Server (in this case Windows). Right click the VM, and click **Edit Settings** to see the total provisioned storage. Based on the Production Server O.S. Type and [Storage Requirements](../SafeHaven 5 CLC to AWS/Determine Storage Requirements.md), calculate the amount of storage that needs to be added.

2. In the Navigation Tree, right click the **SRN** you want to add storage to, and click **Edit Settings**.
3. Click **Add**, and select **Hard Disk**. click **Next**

4. Select **Create a new virtual disk**, and click Next

5. Enter the **disk size**, select **Thick Provision Lazy Zeroed**, then select **Store with the virtual machine**. Click **Next**.

6. Keep the default **Virtual Device Node**, that is SCSI(0:1). Click **Next**.

7. Click **Finish**, then click **Ok** on the main edit settings window. This successfully adds a hard disk to the SRN..


**NOTE**: There is no need to allocate storage for the SRN on AWS. Depending on the size of your Protection Group, SafeHaven will automatically create the EBS volumes to meet the requirements.

### Claim storage pool for Lumen Cloud Production SRN
1. Once the storage has been attached to the SRN, the next step is to login to the **SafeHaven Console**.
2. Go to the Navigation Tree and select the Production SRN. In the **Properties Panel** select **Claim Storage Pool**.
**NOTE**: If you don't see a device listed click on **Rescan** in order to force a rescan of the SCSI bus on the SRN.

3. If this is the first storage device you are claiming, then select the Storage Device you want to claim and select **Create a New Storage Pool for the Device**. Fill in the **Storage Pool Name** and click **Claim**.

4. Depending on the protection group architecture, the user can claim another disk following a similar procedure and can either **Create a new Storage Pool** or **Add to an existing Storage Pool**.

For **Windows** Protection Group, **Next Step** is to [Create Windows Protection Group, Install LRA and Start Replication](../SafeHaven 5 CLC to AWS/Create-Windows-Protection-Group-Install-LRA-and-Start-Replication.md)

For **Linux** Protection Group, **Next Step** is to [Create Linux Protection Group](../SafeHaven 5 CLC to AWS/Create Linux Protection Group.md)
