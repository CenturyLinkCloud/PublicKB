{{{
  "title": "Expand Disk under a Protection Group",
  "date": "08-22-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to expand the disks under a VM in a protection group is a source VMs disk has been expanded

### Requirements
1. Access to the SafeHaven console (GUI).
2. Access to Centurylink portal
3. SafeHaven version 4.0.2 or above are required

### Expand disk on the DR SRN
This step explains how to expand disk on the DR SRN to accomodate the expanded storage on source VM
1. Login to SafeHaven console.
2. Click on the Protection group where the source VMs disk has been resized.
3. Under the properties panel, note down the **Data volume Storage Pool** under **Peer** side.
4. Click on the SRN where the PG resides under DR datacenter.
5. In properties panel, note down the disks corresponding to the Claimed Storage Pool for the resized source VM. This will appear like /dev/sdd, or /dev/sde,etc
6. Login to Centurylink Cloud Portal : https://control.ctl.io/
7. Under infrastructure, go to the DR SRN for the resized source VM under the DR Datacenter.
8. On the right hand side, click on edit storage. Expand the disk in CLC from step 5 according to the image below 
   ![disk mapping](../../images/SH5.0/byoip/diskformat.png)
