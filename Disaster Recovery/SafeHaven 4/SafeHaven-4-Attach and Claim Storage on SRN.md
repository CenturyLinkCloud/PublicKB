
### Add storage to each SRN  

Select Servers under the Infrastructure tab. In the Navigation Tree, select the SRN in the recovery data center, then scroll down on the main data panel and select edit storage.

![Upgrade](../../images/SH4.0/Create%20Nodes/Nodes16.png)

Select add storage and then in the drop-down menu select raw disk.

![Upgrade](../../images/SH4.0/Create%20Nodes/Nodes17.png)

Add enough storage for the aggregate capacity of all VMs to be protected by the SRN, plus 25 to 30% for the checkpoint pool and an additional 5 GB for each VM to be used as temporary storage for Test Failover operations. Select apply.

![Upgrade](../../images/SH4.0/Create%20Nodes/Nodes18.png)

Similarly, add storage to the SRN in the production data center. For Windows Protection Groups, with Local Cache protection type, you should add about 10% of the aggregate capacity of the protected VMs to be used as a disk cache. For Windows and Linux Protection Groups of the Local Replica protection type, you should add enough storage for the aggregate storage capacity of the protected VMs, plus 25 to 30% for the checkpoint pool and an extra 5 GB for each VMs as temporary storage for failback operations. Select apply.
You have now deployed the servers that will become the SRNs and the CMS and have attached the prerequisite storage to the SRNs.
