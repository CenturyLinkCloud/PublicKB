{{{
  "title": "Test failover on Azure",
  "date": "06-20-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article describes how to perform Test Failover to Azure from a Protection Group level. Test Failovers can be performed multiple times by the user to verify data integrity as well as for their annual DR tests.



### Requirements
1. Access to the SafeHaven console (GUI).
2. Initial Replication is complete for the Protection Group and checkpoints are available for Test Failover.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available.

### Network isolation
While the Test Failover command is in effect, instances of the Protection Group will be active in both the primary and secondary data centers. To avoid inadvertent client redirection to the secondary data center, a strategy for network isolation must be in place before the Test Failover command is issued. On Azure this can be accomplished by selecting a VNet that is isolated from the production environment or by using Network Security Groups that have proper rules to block the traffic. In case of native domain controller setup in the DR Network, user my need to shutdown the DR domain controller in Azure for test purposes.

### Test-Failover
1. Right-click on the Protection Group in the Navigation Tree and click **Test Failover** from the drop-down menu. This launches the Test Failover wizard.

2. **Choose the desired checkpoint** by selecting the Server's disk checkpoints(s) from the Checkpoint History table. Select Multiple checkpoints if required per Protected Server. Click **Next**

3. Under the Production Server Name, click on the Selected Checkpoint. Click **Next**, this will open up a Configuration Detail section on the right side of the window.

4. Select the **Resource Group, VM Size-Type, Virtual Network, Network Security group, Subnet and IP Address(or select DHCP)** for each of the disk checkpoints selected on the previous step. Click Launch.
**NOTE:** Please select a Virtual Network with Isolated Network. Running a test failover instance in a non-isolated environment can adversely affect the production environment.

5. The instance(s) will be created and the wizard will display the Instance Name, state, the instance ID, and IP.  

6. Login to the Azure Virtual Machine using the Production Server credentials (local/cached/domain credentials) and confirm all the data is intact as well as applications are behaving as expected.  

**Note**: After the instance is deployed you can optionally delete it from the wizard by selecting the instance row and clicking on the Delete button or Click on Close to end the Wizard.  

7. If you click on Close to end the wizard, the Test failover instance will still continue to run.

8. Go to the Azure portal and verify the newly deployed instance.

9. To remove the Test Failover instance, right click the protection group and click **Manage Instances**. Select the Instance you want to terminate and click **Delete**. This will shutdown and terminate the Azure Virtual Machine.
