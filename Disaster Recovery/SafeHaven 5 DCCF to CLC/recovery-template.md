{{{
  "title": "Prepare a Recovery Server Template",
  "date": "04-30-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
* A **Recovery Server** is the server that runs the image of the production server at the time of a disaster, when a user clicks the test-failover/failover button.  
* **Matching NIC and PCI Slot**: For Windows Production Server, if the DR-Site is CLC/DCC/VMWare, the **NIC and PCI slots** of the Recovery VM should be exactly same as that of the Production Server. This is a requirement for iSCSI boot on the DR Side.  
**Note** : Matching NIC/PCI is not needed for a Linux Production VM.
* For ease of deployment, it is highly recommended to have a Recovery instance template in advance before creating a protection group. It is mostly benefitial when there are multiple production VMs similar PCI slots
**Note** : If the production server's NIC and PCI slots are VMXNET3 and 160, respectively , then a template is not required because Centurylink Cloud's default Ubuntu 14 template can be used to deploy a recovery instance.

This article explains how to create a template for recovery server in CLC.

### Find out NIC and PCI of the Production Server.
1. Log into the Windows Production VM.
2. Go to **Device Manager**.
3. Expand **Network Adapters**.
4. Right click the Network Adapter, and click **Properties**.
5. Take a note of the **NIC Type** and **PCI slot number**.  
![NIC-PCI](../../images/SH5.0/NIC-PCI.png)
