{{{
  "title": "Configuring the recovery server in a Linux PG",
  "date": "05-09-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to configuring the recovery server in a Linux PG.

### Requirements
Access to the recovery server.

### Assumption
This article assumes that:

1. A SafeHaven cluster has been created successfully.
2. Linux PG initial sync is completed and there are clean 0 sized checkpoint(s) for Test Failover

### Configure the recovery server
A recovery server boots off of disks of the DR SRN when a test failover/ failover operation is issued. 
1. Right click on the Linux PG, select **Test Failover** from the drop-down menu
2. Select the desired checkpoint and click on next
3. Once **Test Failover** and **Power on** are completed, click on next.
4. Confirm the right PG is selected and click on **Next**
5. SSH into the Recovery Linux Server.
6. Download the Linux Onboarding scripts. The Download URL can be found under the **Download Links** section in [SafeHaven 5.0.0 Release Notes](../SafeHaven 5 General/SafeHaven5.0.0-Release-Notes.md)
   ```
   wget SafeHaven_Linux_Onboarding_Download_URL
   ```
7. Extract the downloaded file.
   ```
   tar xvfz file_name
   ```  
   **Note:** the above file name can be different.
8. Run the replication script : makestub.sh  
   ```
   cd safehaven_linux_onboarding_scripts
   ```  
   ```
   ./makestub.sh -d
   ```
 **Note**: The above script will download some packages required for the replication.
   - **Please enter the iSCSI Target Server IP Address at this site:**  
     Please put the Local iSCSI IP Address of the Recovery SRN in CenturyLink Cloud Prouction Datacenter here.
9. Shut down the Recovery server.
    ```
    shutdown -h now
    ```
10. Go back to SafeHaven Console Test Failover wizard, check both **MakeStub tool complete** and **Reboot & verify complete** boxes, then click on **Finish**.
11. Click on **Delete and Finish** button to exit the wizard, Wait till the job to complete.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/kJI63oXwmrg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</p>
