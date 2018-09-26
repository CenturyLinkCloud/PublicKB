{{{
  "title": "Test Failover to AWS",
  "date": "12-27-2017",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article describes how to perform Test Failover to AWS from a Protection Group level. Test Failovers can be performed multiple times by the user to verify data integrity as well as for their annual DR tests.


### Requirements
1. Access to the SafeHaven console (GUI).
2. Initial Replication is complete for the Protection Group and checkpoints are available for Test Failover.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available.

### Network isolation
While the Test Failover command is in effect, instances of the Protection Group will be active in both the primary and secondary data centers. To avoid inadvertent client redirection to the secondary data center, a strategy for network isolation must be in place before the Test Failover command is issued. On AWS this can be accomplished by selecting a VPC that is isolated from the production environment or by using Security Groups that have proper rules to block the traffic. Incase of native domain controller setup in the DR vlan, user my  need to shutdown the DR domain controller in AWS for test purposes.

### Test-Failover

1. Right-click on the Protection Group in the Navigation Tree and click **Test-Failover** from the drop-down menu. This launches the Test Failover wizard.

2. Choose the desired checkpoint by **selecting the AMI(s)** from the Checkpoint History table. Select Multiple checkpoints/AMI's if required per Protected Server. Click **Next**.

3. Under the Production Server Name, click on the **Selected Checkpoint**. This will open up a **Configuration Detail** section on the right side of the window.

4. Select the **Instance type, VPC, Security group, Subnet and IP Address(or select DHCP)** for each of the AMI(s) selected on the previous step. Click **Launch**.  
**NOTE**: Please select a VPC with **Isolated Network.** Running a test failover instance in a non-isolated environment can adversly affect the production environment.

5. The instance(s) will be created and the wizard will display the **Instance Name, state, the instance ID, and IP**. Login to the EC2 Instance using the Production Server credentials (local/cached/domain credentials) and confirm all the data is intact as well as applications are behaving as expected. After the instance is deployed you can optionally delete it from the wizard by selecting the instance row and clicking on the **Delete** button or Click on **Close** to end the Wizard.

6. If you click on **Close** to end the wizard, the Test failover instance will still continue to run.

7. Go to the AWS console and verify the newly deployed instance.

8. To remove the Test Failover instance, right click the protection group and click **Manage Instance**. Select the Instance you want to terminate and click **Terminate**. This will shutdown and terminate the EC2 Instance.

The procedure is same for CLC/VMWare/Manual sites as source datacenters.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/rrBvCAI4HM4" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>

**NOTE:This step completes SafeHaven setup for a Protection Group.**

The user may go through [AWS Statistics](AWS Statistics.md) for information on EBS Volumes(s), AMIs, AWS Snapshots and running AWS Instances(test failover/failover)

In case of an acutal Disaster Recovery event when there is a Production Datacenter outage and the user cannot access Production Servers, as a **Next Step** the user may [Failover to AWS](Failover to AWS.md)  

**NOTE: Failover can be a disruptive operation if not done properly**.
