{{{
  "title": " Add and Claim Storage on SRNs in CenturyLink Cloud",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach storage on a SRN in CenturyLink Cloud. After the SRN has been registered with the SafeHaven Console, the next step is to attach storage to it before creating Protection Groups.

**NOTE**: For ease of management and troubleshooting it is recommended that the user creates one Storage Pool per Protection Group.

### Requirements
1. Access to the SRNs in CenturyLink Cloud portal
2. Access to the SafeHaven Cluster

### Assumptions
This article assumes that the user has already registered the SRNs within the SafeHaven Console and wants to add storage to the SRNs before creating Protection Groups.

### Add storage to the Production SRN in CenturyLink Cloud
1. Login to CLC Control portal https://control.ctl.io, select **Servers** under the **Infrastructure** tab. Confirm the Storage requirements for the Production Server (in this case Windows). Based on the Production Server O.S. Type and [Storage Requirements](Determine Storage Requirements.md), calculate the amount of storage that needs to be added.

2. In the Navigation Tree, select the **SRN** you want to add storage to, then scroll down on the main data panel and select **edit storage**.
3. Select **add storage** and then in the drop-down menu select **raw disk**.
   **NOTE**: **DO NOT** select a **partitoned** disk.

4. Add required storage and **apply**. Wait for the job to complete.

### Claim storage pool for CenturyLink Cloud Production SRN
1. Once the storage has been attached to the SRNs, the next step is to login to the **SafeHaven Console**.
2. Go to the Navigation Tree and select the Production SRN. In the **Properties Panel** select **Claim Storage Pool**.
**NOTE**: If you don't see a device listed click on **Rescan** in order to force a rescan of the SCSI bus on the SRN.

3. If this is the first storage device you are claiming, then select the Storage Device you want to claim and select **Create a New Storage Pool for the Device**. Fill in the **Storage Pool Name** and click **Claim**.

4. Depending on the protection group architecture, the user can claim another disk following a similar procedure and can either **Create a new Storage Pool** or **Add to an existing Storage Pool**.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/CjH_Pts0tuk" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>

For **Windows** Protection Group, **Next Step** is to [Create Windows Protection Group, Install LRA and Start Replication](Create-Windows-Protection-Group-Install-LRA-and-Start-Replication.md)

For **Linux** Protection Group, **Next Step** is to [Create Linux Protection Group](Create Linux Protection Group.md)
