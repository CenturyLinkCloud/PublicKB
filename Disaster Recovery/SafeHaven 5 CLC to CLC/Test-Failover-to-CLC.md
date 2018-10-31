{{{
  "title": "Test Failover to CLC",
  "date": "05-01-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article describes how to perform Test Failover to CenturyLink Cloud from a Protection Group level. Test Failovers can be performed multiple times by the user to verify data integrity as well as for their annual DR tests.


### Requirements
1. Access to the SafeHaven console (GUI).
2. Initial Replication is complete for the Protection Group and checkpoints are available for Test Failover.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available.

### Network isolation (Recommended)
While the Test Failover command is in effect, instances of the Protection Group will be active in both the primary and secondary data centers. To avoid inadvertent client redirection to the secondary data center, a strategy for network isolation must be in place before the Test Failover command is issued.  

**For Network Isolation in Linux**  
run : echo 'disabled' >> /opt/datagardens/startup/etcRemote/REMOTE_GATEWAY.  

**For Network Isolation in Windows**  
You can select the network isolation option during Test Failover from within the wizard.  

### Test-Failover
1. Right click the protection group, and click **create manual checkpoint**.  

2. Right-click on the Protection Group in the Navigation Tree and click **Test-Failover** from the drop-down menu. This launches the Test Failover wizard.

3. Clicking on the checkpoint then Choose the desired checkpoint from the Checkpoint History table. Select Multiple checkpoints/AMI's if required per Protected Server. Click **Next**. Make sure that **Network Isolation** is checked.

4. Wait till **Test Failover** and **Power On** complete, click on **Cancel** to close the wizard. If you click on **Finish**, the Test failover clone will be deleted.

5. You can go to the **Active iSCSI Sessions** tab to monitor the booting procedure, once the RDP port is open, you can log in to the recovery server to verify the data consistency.

6. To remove the Test Failover instance, right-click the protection group and click **Delete Failover Clone**. This will shut down the recovery server and delete the Test Failover clone.

7. Restore the files that were edited for Network Isolation.

The procedure is same for CLC/VMWare/Manual sites as source datacenters.

**Note** : If the Network of Recovery Server is isolated, please use a jump server from within the DR vlan to access the recovery server.  
