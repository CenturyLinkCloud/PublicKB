{{{
  "title": "Create Windows Protection Group, Install LRA and Start Replication",
  "date": "12-27-2017",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create Windows Protection Group and protect a Windows server Automatically as well as Manually.

### Requirements
1. To protect a Windows server using SafeHaven, we need to install a Local Replication Agent (LRA) on the production server. In order to complete the LRA installation, a **Reboot** of the production server is required. **Please schedule a downtime window for LRA installation.**

2. For Ansible LRA installation to work, make sure TCP 445 port Inbound is open on the production server by running the following command via Windows Commandline (run as administrator):
```
New-NetFirewallRule -DisplayName "psexec tcp 445" -Name "psexec tcp 445" -Profile Any -LocalPort 445 -Protocol TCP
```
### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully
2. Both production and recovery SRNs have been registered and peered
3. Proper storage has been attached and claimed on the production SRN

### Create a Windows Protection Group
1. Right click on the **Production SRN** and select **Create Protection Group**.
**NOTE**: Always start the Protection Group creation from the Production SRN.

2. Select the **Recovery SRN**, and click **Start Wizard**.  

3. **Select the servers** from the production datacenter that you want to include in the Protection Group.  Remember that it is perfectly acceptable to select just one server for inclusion in the Protection Group. Click **Next**.  
**NOTE**: VSS Checkpoints are not available if you select multiple Windows to create a single Protection Group.

4. Choose a name for the Protection Group and click **Next**.

5. Next, the SafeHaven software provides a suitable default size for the Disk Cache. You can modify this should you choose.  

6. Select the **storage pool** for cache. Click Next.  
   **NOTE**: By default the Cache size is "10% of the total provisioned storage" for the Windows server(s) you are protecting.

7. A summary panel appears. You may navigate back and change configurations for the Protection Group if you like. Please check the acknowledgement box and click **Create**  

**NOTE**: LRA stands for Local Replication Agent which is the kernel level driver that Lumen provides to replicate Windows Production Servers. There are two methods by which LRA can be installed and initial replication can be started. User must select one of the two methods stated below.  

Method 1. Automatic/Ansible LRA installation and Automatically Start Initial Replication   
OR  
Method 2. Manual LRA Installation and Manually Start Initial Replication

### METHOD 1
#### Automatic/Ansible LRA installation and Automatically Start Initial Replication
1. Once the Protection Group is created and its status is **Running** on the Properties tab, right click on it and click **Install Local Replication Agent**.
2. First select the VM you need to install LRA on, then click **Next**.
3. Next you will need to provide the credentials for each protected VM, and acknowledge that you understand that :  
    a. Each selected virtual server will automatically reboot during the process.  
    b. Powershell version 3 will be installed along with the LRA in each selected VM.  
    **NOTE**: Before clicking the Finish button , please be aware that auto installation of LRA will automatically trigger a reboot of the production server **right away**. **This reboot cannot be scheduled if you choose to install the LRA using automation/ansible.**  
    Click **Next**

4. Once it says **Completed** under **Install LRA**, click **Next**. Next, click **Finish** to end the wizard.

**The initial replication of the production windows server is started automatically as part of the installation process.**

**NOTE**: Follow the steps below incase the user prefers to install the LRA and start the replication manually.

### METHOD 2
#### Manual LRA installation
1. After the protection group is created, log into each of the Windows production server within the protection group.

2. Download the latest compatible SafeHaven LRA software from the **Windows Downloads - Driver Installer** link which can be found under the **Download Links** of [SafeHaven 5.0.0 Release Notes](../SafeHaven 5 General/SafeHaven5.0.0-Release-Notes.md).  
   **NOTE:** Please make sure the LRA agent is compatible with the SafeHaven release version you are using. For example: A SafeHaven LRA version 4.0.4 is NOT compatible with SafeHaven release version 5.  
   **NOTE**: The VM requires a reboot at the end of the LRA installlation.

3. Launch the LRA installer, select the default **Express Installation**, and click **Next**.

4. To install the LRA, you must reboot the Windows production VM. Click **Restart Now**.

   **NOTE**: Reboot of the production server can be scheduled for a later time.

#### Manually Start Initial Replication
1. After reboot, click on **Start**, find and launch the SafeHaven **Manager.exe**.

2. Select the default options on the first screen of the wizard (all boxes checked) and click **Next**.

3. Verify the NIC type and PCI slot number. Click **Next**

4. Enter the **Local iSCSI IP address of Production SRN** in front of **Target Portal IP Address** and click **Discover**. Select the appropriate ISCSI target to connect from the ISCSI target list.  
   Click **Connect**, then select **Next**.

5. A new window appears which provides the mapping from source(VMDK on production server) to destination disk(ISCSI on the SRN) along with the recommended Sync Rate, accept the default option and click **Next**.  
   **NOTE**: Please make sure each production virtual disk you want to protect is mapped to a corresponding iSCSI target destination disk. **The size of the source and destination disk must match**.

6. Select **Obtain IP via DHCP** under IP Address Setting, then click **Next**.

7. Click **Finish** to end the wizard.

The initial replication of the production windows VM will start now. Close the command prompt window if required.

Once the Protection Group is created successfully, **Next** step is to [Modify WAN Replication Rate](Modify WAN Replication Rate.md) and [check replication status](Check Replication Status.md)
