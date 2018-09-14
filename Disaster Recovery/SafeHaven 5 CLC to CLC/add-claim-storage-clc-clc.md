{{{
  "title": " Add and Claim Storage on SRNs in CenturyLink Cloud",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to attach storage on production site SRN and recovery site SRN in CenturyLink Cloud. After the SRNs have been registered with the SafeHaven Console, the next step is to attach storage to it before creating Protection Groups.

**NOTE**: For ease of management and troubleshooting it is recommended that the user creates one Storage Pool per Protection Group.

### Requirements
1. Access to the SRNs in CenturyLink Cloud portal
2. Access to the SafeHaven Cluster

### Assumptions
This article assumes that the user has already registered the SRNs within the SafeHaven Console and wants to add storage to the SRNs before creating Protection Groups.

### Add and claim Storage on SRNs.
#### Adding Storage to the Production SRN in Centurylink Private Cloud
1. Login to Centurylink Cloud Portal.
2. Click on the PROD-SRN.
3. Click on **Edit Storage**.
4. Click on **Add storage**. Then select **raw disk**.
5. Change the size of the disk :

 If the production/source VM is a **Linux machine**:   
    The disk size should be **125% of total provisioned storage**, and **6GB per Protection group** for Failback Test Failover.    
    For example, If Production VMs disk size is 16 GB, add a 26 GB(20 + 6) disk to the Production SRN.   

   If the production/source VM is a **Windows machine**:  
  **For a local cache based Windows Protection Group(recommended):** 
    The disk size should be **10% of total provisioned storage**   
    For example, If Production VMs disk size is 60 GB, add a 6GB disk to the Production SRN.  

   **For a Replica based Windows Protection Group(recommended):**    
   The disk size should be **125% of total provisioned storage**, and **6GB per Protection group** for Failback Test Failover.
   For example, If Production VMs disk size is 60 GB, add a 81 GB(75+6) disk to the Production SRN.

6. Click on **apply**


#### Adding Storage to the DR SRN in CLC
1. Login to Centurylink Cloud Portal.
2. Click on the DR-SRN.
3. Click on **Edit Storage**.
4. Click on **Add storage**. Then select **raw disk**.
5. The disk size should be **125% of total provisioned storage**, and **6GB per Protection group** for Failback Test Failover.    
    For example, If Production VMs disk size is 16 GB, add a 26 GB(20 + 6) disk to the Production SRN.
6. Click on **apply**
    
#### Claim storage pool for CenturyLink Cloud SRNs
1. Login to the SafeHaven Console.
2. click on Production SRN.
3. On the right side, click **Claim Storage**.
4. Select the recently added disk, then select **Create a new Storage Pool for the Device**
5. Enter a **Storage Pool Name**, and click **Claim**.
6. Click on the DR SRN, and repeat steps 3 to 5.
