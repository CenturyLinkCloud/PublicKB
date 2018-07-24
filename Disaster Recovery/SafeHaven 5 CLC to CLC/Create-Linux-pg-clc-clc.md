{{{
  "title": "Create Linux Protection Group",
  "date": "12-27-2017",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a Linux Protection Group when the source site and recovery site are in CLC

### Requirements
Access to the SRNs in CenturyLink Cloud and permissions to add raw disks to it.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Both production and recovery SRNs have been registered and peered
3. Storage on both SRNs is added and claimed.


### Create a Linux Protection Group
1. Right click on the **Production SRN** and click **Create Protection Group**.

   **NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.

3. **Select the servers** from the production data center that you want to include in the Protection Group.

   **NOTE**: Only one Linux server can be selected per Protection Group.

4. Choose a name for the Protection Group, and click **Next**.

7. Once the correct **Primary Pool** and **Checkpoint Pool** are both selected in Production and recovery data center, click **Next**.

8. Please read the acknowledgement, and check the box.

9. Verify the Protection Group summary, and click **Create**.

