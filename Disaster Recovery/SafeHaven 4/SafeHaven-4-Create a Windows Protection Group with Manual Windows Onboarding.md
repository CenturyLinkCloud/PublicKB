
{{{
  "title": "SafeHaven-4: Install the Local Replication Agent (LRA) on windows servers and start initial replication",
  "date": "04-24-2016",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}
## Article Overview
This article explains how to install windows agent(LRA) on a windows production server using two methods:
- Auto-Installation using ansible from the SafeHaven console
- Manually

### Assumption
This article assumes that a Windows protection group (Local Cache or Local Replica) has already been created successfully. 

### Requirement
To protect a Windows server using SafeHaven, we need to install a Local Replication Agent (LRA) on the production server. In order to complete the LRA installation, a REBOOT of the production server is required.

### Auto Installation (using ansible)

Right click on the Windows protection group and then click on "Installation". Then click on "Install Local Replication Agent" from the drop-down menu.

![Auto Installation](../../images/SH4.0/LRA_0.png)

Enter the production server login credentials for each server that requires LRA installation.

![Auto Installation](../../images/SH4.0/LRA_9.png)
**NOTE**: Before clicking the Finish button , please be aware that auto installation of LRA will automatically trigger a reboot of the production server right away. This reboot cannot be scheduled if you choose to install the LRA using automation/ansible. 



Wait for the job to show up as complete in the progress panel of the SafeHaven console.

Once the job is complete , the initial replication of the production windows VM will start automatically.


### Manual Installation (without ansible)

Log into each of the Windows production VMs within the protection group.

Download the latest compatible SafeHaven LRA software from the Windows Downloads - Driver Installer link (https://download.safehaven.ctl.io/SH-4.0.1/safehaven_windows_driver-4.0.1.exe) under the Download Links section of the SafeHaven 4.0.1 release notes : https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4/safehaven-4.0.1-release/

NOTE: Please make sure the LRA agent is compatible with the SafeHaven release version you are using. For example: A SafeHaven LRA version 3 is NOT compatible with SafeHaven release version 4.0.1

Launch the LRA installer, select the default Express Installation and accept the license agreement by clicking on "I accept the License Agreement", select "Next".

![install LRA1](../../images/SH4.0/LRA_1.png)

To install the LRA, you must reboot the Windows production VM. 

![install LRA1](../../images/SH4.0/LRA_13.png)

**NOTE**: Reboot of the production server can be scheduled for a later time if required.  

After reboot, click on "Start", find and launch the SafeHaven LRA manager

![install LRA1](../../images/SH4.0/LRA_11.png)

Select the default options on the first screen of the wizard (all boxes checked) and select "Next"

![install LRA1](../../images/SH4.0/LRA_2.png)

Enter the Local ISCSI IP address of production SRN and select Discover, select the appropriate ISCSI target to connect from the ISCSI target list, select "Connect", a pop up window appears to let you know that the communication service between the production machine and the SRN has been configured successfully, select "OK" then select "Next".

![install LRA1](../../images/SH4.0/LRA_3.png)

A new window appears which provides the mapping from source(VMDK on production server) to destination disk(ISCSI on the SRN) along with the recommanded Sync Rate, accept the default option and select "Next".

**NOTE**: Please make sure each production VMDK disk you want to protect is mapped to a corresponding ISCSI target destination disk. The size of the source and destination disk has to match.

![install LRA1](../../images/SH4.0/LRA_4.png)

Now enter IP information for the corresponding proxy recovery server in the DR datacenter, select "Next".

![install LRA1](../../images/SH4.0/LRA_5.png)

Click "Finish" to end the wizard.

![install LRA1](../../images/SH4.0/LRA_6.png)

The initial replication of the production windows VM will start now.

### Procedure to check 


To confirm the successful installation, launch "Tools" within the protected VM

![install LRA1](../../images/SH4.0/LRA_7.png) 

Issue a command to lauch the local replication manager
```sh
$ DgSyncEx.exe
```

Type `List`, check if "Driver status" is "NO ERROR", The active physical disk devices is correct, finally confirm the sync is enabled and the synchronization is progressing correctly.

![install LRA1](../../images/SH4.0/LRA_8.png) 
