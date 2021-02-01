{{{
  "title": "Failover to AWS",
  "date": "12-27-2017",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to initiate Failover to AWS using SafeHaven incase of a disaster scenario where Production Datacenter is unavaiable and users lose access to the Production Server.

### Requirements
1. Access to the SafeHaven console (GUI).
2. Initial Replication is complete for the Protection Group and checkpoints are available for Failover.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available. This article assumes that Test Failover has been done successfully.

**NOTE**: It is strongly recommended that users must peform a Test Failover before doing an actual Failover even incase of a disaster scenario to verify the integrity of data in the recovery datacenter as a first step. Refer to [Test Failover to AWS](Test Failover to AWS.md) for more information.

### Failover to AWS
Users may not choose to perform Network Isolation incase of an actual Failover event.

1. To initiate Failover, right-click on the appropriate Protection Group in the Navigation Tree and click **Failover** from the drop-down menu. The Failover wizard appears.

2. In most cases, you will want to Failover to the most recent checkpoint, however, by clicking in the Checkpoint column you can pick an earlier checkpoint as appropriate. Choose the desired checkpoint by selecting the AMI(s) from the Checkpoint History table. You may select multiple checkpoints if needed Select **Next**.

3. Under the Production Server Name, click on the **Selected Checkpoint**. This will open up a **Configuration Detail** section on the right side of the window.

4. Select the **Instance type, VPC, Security group, Subnet and IP Address(or select DHCP)** for each of the AMI(s) selected on the previous step. Click **Launch**.

5. The instance(s) will be created and the wizard will display the **Instance Name, state, the instance ID, and IP**. Login to the EC2 Instance using the Production Server credentials (local/cached/domain credentials) and confirm all the data is intact as well as applications are behaving as expected.  
   **NOTE:** **Do not click on the Delete button as it will terminate the Failed over Instance and this may impact business continuity incase of a disaster scenario.**

6. Click on **Close** to end the wizard. The Failover instance will still continue to run.

7. Go to the AWS console and verify the newly deployed instance.

**NOTE: The failed over EC2 Instance in AWS is now the production server and users can verify business continuity and take time to stabilize applications and working of their AWS environment. Email Lumen Team at help@ctl.io if SafeHaven assistance is required incase of a Failover event.**
The procedure is same for CLC/VMWare/Manual sites as source datacenters.
