{{{
  "title": "Migrate to AWS",
  "date": "04-06-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article describes how to migrate a VM to AWS on a protection group level.

### Requirements
1. Access to the SafeHaven console (GUI).
2. Initial Replication is complete for the Protection Group.
3. Make sure that the Migration is performed during a **down time** because it will require shutting down of the Production/source server. It can take a few hours to take an AWS snapshot and perform migration, depending on gthe size of the VM.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully, and initial replication has completed.

### Migrate

1. Right click the protection group that needs to be migrated, and click **Migrate**.
2. Select an option for **Power operation** on the production server.  
  * **Automatically powered off the servers on the production site** - This will power off the source/ production server.  
  * **I have already powered off the servers on the production site** - Select this option if you have already powered off the source/production server manually and don't want the process to be repeated through SafeHaven.

  **Note** - It is strongly recommended to shut down the production server, so the we do not end up with 2 instances of the same server in different states.

3. Check the box in front of "**I understand**", if you accept the condition above it, that is, **there will be a few hours downtime during migration**  
  Click Next.

4. **Configure Instances** : Here we will configure settings of a migration instance. Select an server under **Server(s)** column
  a. Select the **instance type**
  b. Select the **VPC** . This is the VPC that will be assigned to the migrated instance in AWS.  
  c. Select a **Security Group**.  
  d. Select a **Subnet**.  
  e. Enter a Static IP under **IP Address**, or select **Use DHCP** for a DHCP IP address.    
  Click **Migrate**.   

  **Note** : It may take a few hours for the migration to complete.
 5. Once the migration progress starts, you can close the wizard. wait for migration to finish.

 6. When the migration is complete, a **Migrate Protection Group** job will appear as **Completed** in the job panel at the bottom of SafeHaven console.

 7. Once the job is **Completed**, right click the protection group and click **Manage Instances**.  
  You will be able to see the IP address of **running** migrated instance.

 8. Login to AWS Console, and go to the running instances. Search for **"Migration"** to find the migrated instance.

 9. Log into the Migrated Instance, and verify all the files.

 10. Once the migrated instance is verified, go back to Safehaven Console, right click the migrated protection group and click **Delete Protection Group**.    
 Make sure that **All coressponding Instances in AWS** option is **unchecked**.  
 You can check **All coressponding AMI's and Snapshots in AWS** option if you wish to get rid of the AMIs and Snapshots related to the protection Group being deleted.

  This successfully migrates a Protection Group to AWS Cloud.

#### Email Notification
If you set up email notification already, after the migration job is completed, you will receive an email notifying your migration is either successful or failed.
