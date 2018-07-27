{{{
  "title": "Add and Claim Storage on Production SRN in a Manual Site",
  "date": "02-06-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach storage on a single SRN in CenturyLink Private Cloud on VMware Cloud Foundation. After the SRN has been registered with the SafeHaven Console, the next step is to attach storage to it before creating Protection Groups.

**NOTE**: For ease of management and troubleshooting it is recommended that the user creates one Storage Pool per Protection Group.

### Requirements
1. Access to the Production SRN in CenturyLink Private Cloud on VMware Cloud Foundation.
2. Access to the SafeHaven Cluster

### Assumptions
This article assumes that the user has already registered the SRN within the SafeHaven Console and wants to add storage to the SRN before creating Protection Groups.

### Add storage to the Production SRN in CenturyLink Private Cloud on VMware Cloud Foundation

1. Login to DCC portal. Confirm the Storage requirements for the Production Server (in this case Windows). Click the production VM, and go to **Hardware** tab to see the total provisioned storage. Based on the Production Server O.S. Type and [Storage Requirements](../SafeHaven 5 CLC to AWS/Determine Storage Requirements.md), calculate the amount of storage that needs to be added.

2. Click the **SRN** you want to add storage to, and go to **Hardware** tab.  

3. Click **Add**. Enter the amount of storage. click **Ok**

4. This successfully adds a hard disk to the SRN.

### Add storage to the Production SRN in Hyper-V

1. Right click the SRN VM, and click **Settings**.
2. Click on **SCSI Controller** on the left, select **Hard Drive** and click **Add**.
3. Select **Virtual hard disk**, and click **New**.
4. At the first page of the wizard, click **Next**.
5. For **disk format**, select **VHDX**. Click **Next**.
6. Select **Fixed size** for best IO performance.
7. Enter a **Name** and the **Location** where the disk will be stored. Click **Next**.
8. Enter the **Size** of the disk. Please refer to [Storage Requirements KB article](../SafeHaven 5 CLC to AWS/Determine Storage Requirements.md) to calculate the amount of storage needed on the SRN. Click **Next**.
9. Click **Finish**.

**NOTE**: There is no need to allocate storage for the SRN on AWS. Depending on the size of your Protection Group, SafeHaven will automatically create the EBS volumes to meet the requirements.

### Claim storage pool on Production SRN
1. Once the storage has been attached to the SRN, the next step is to login to the **SafeHaven Console**.
2. Go to the Navigation Tree and select the Production SRN. In the **Properties Panel** select **Claim Storage Pool**.
**NOTE**: If you don't see a device listed click on **Rescan** in order to force a rescan of the SCSI bus on the SRN.

3. If this is the first storage device you are claiming, then select the Storage Device you want to claim and select **Create a New Storage Pool for the Device**. Fill in the **Storage Pool Name** and click **Claim**.

4. Depending on the protection group architecture, the user can claim another disk following a similar procedure and can either **Create a new Storage Pool** or **Add to an existing Storage Pool**.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/RauSUvUXaQE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</p>

For **Windows** Protection Group, **Next Step** is to [Create Windows Protection Group, Install LRA and Start Replication](../SafeHaven 5 CLC to AWS/Create-Windows-Protection-Group-Install-LRA-and-Start-Replication.md)

For **Linux** Protection Group, **Next Step** is to [Create Linux Protection Group](Create-Linux-PG-Production-manual.md)
