{{{
  "title": "Install Scripts and Start Replication for Linux Protection Group",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to Install Scripts and Start Replication for a Linux Protection Group.

### Requirements
SSH access to the Production Linux Server.

### Assumption
This article assumes that a Linux Protection group has been successfully created.

### Install Scripts and Start Replication for Linux Protection Group
1. SSH into the Production Linux Server.

2. Download the Linux Onboarding scripts. The Download URL can be found under the **Download Links** section in [SafeHaven 5.1 Release Notes](../SafeHaven 5 General/SafeHaven5.1.2-Release-Notes.md)
   ```
   wget SafeHaven_Linux_Onboarding_Download_URL
   ```
3. Extract the downloaded file.
   ```
   tar xvfz file_name
   ```  
   **Note:** the above file name can be different.

4. Run the replication script : rsync2iscsi.sh  
   ```
   cd safehaven_linux_onboarding_scripts
   ```  
   ```
   ./rsync2iscsi.sh -d
   ```
   **Note**: The above script will download some packages required for the replication.

   - **What is your remote hypervisor type ?[xen/vmware]**  
     Please put **xen** if the DR site is AWS.
   - **Please enter the iSCSI Target Server IP Address at this site:**  
     Please put the Local iSCSI IP Address of the Production SRN in CenturyLink Cloud Prouction Datacenter here.
   - **Select the target IQN of your protection group**  
     Put the number corresponding to the correct protection group. This question will not be asked if there is just one protection group.  
**Note**: Now the rsync replication of files will start automatically. The replication can take a while depending at the size of the server. Once the replication is done, hit <enter> to end the screen session.  

5. Once the replication completes, the user can type **crontab -l** to see the hourly Rsync job that is running in the background. User can modify the cronjob interval as well as exclude certain files/folders from Rsync replication.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/0x9CRRQkZ0I" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>

**Next Step** is to [Modify WAN Replication Rate](Modify WAN Replication Rate.md)
