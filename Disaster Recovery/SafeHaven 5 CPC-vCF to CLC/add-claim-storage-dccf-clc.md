{{{
  "title": "Add and Claim Storage to SRNs: CPC-vCF to CLC",
  "date": "05-03-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to add and claim storage to the SRNs in the production and DR side.
### Requirements
Access to the Production SRN in CenturyLink Cloud and permissions to add raw disks to it.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Both production and recovery SRNs have been registered and peered

### Add and claim Storage on SRNs.
**Adding Storage to the Production SRN in Centurylink Private Cloud**
1. Login to CPC-vCF console.
2. Click on the production SRN VM.
3. Go to **Hardware** tab
4. Under **Hard Disks**, click on **+Add** to add a new hard disk.
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
   
   
**Adding Storage to the DR SRN in CLC**
1. Login to Centurylink Cloud Portal.
2. Click on the DR-SRN.
3. Click on **Edit Storage**.
4. Click on **Add storage**. Then select **raw disk**.
5. The disk size should be **125% of total provisioned storage**, and **6GB per Protection group** for Failback Test Failover.    
    For example, If Production VMs disk size is 16 GB, add a 26 GB(20 + 6) disk to the Production SRN.

**Claim Storage in SafeHaven Console**
1. Login to the SafeHaven Console.
2. click on Production SRN.
3. On the right side, click **Claim Storage**.
4. Select the recently added disk, then select **Create a new Storage Pool for the Device**
5. Enter a **Storage Pool Name**, and click **Claim**.
6. Click on the DR SRN, and repeat steps 3 to 5.
