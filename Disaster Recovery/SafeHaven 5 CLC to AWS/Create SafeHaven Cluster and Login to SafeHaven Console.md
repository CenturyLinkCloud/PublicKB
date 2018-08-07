{{{
  "title": "Create a SafeHaven Cluster and Login to SafeHaven Console",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to deploy a SafeHaven Cluster. Once the cluster is deployed, a user can log in to SafeHaven Console to access their SafeHaven Environment and start the DR setup.

### Requirements
1. Please ensure that the SafeHaven CMS server is already created in AWS and it is reachable from the PC/machine on which the user will use to launch the SafeHaven Console to create/login to the SafeHaven Cluster.
2. TCP and UDP Ports 20080 and 20081 must be opened on your security group/Network ACL on AWS.
3. CMS server has internet access.

### Assumptions
1. CMS server has been created in AWS Recovery Datacenter.
2. The CMS server is reachable from the PC/machine you are running the SafeHaven Console on.
3. The CMS server has internet access.

### Most Recent SafeHaven Release Updates
Please ensure that you are using the most recent SafeHaven release update to create a new cluster. Please refer to [Most Recent SafeHaven Release Updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md) for information on what's most recent.

### Download the SafeHaven Console Application
Download the **GUI Package** from the **Download Links** section of the most recent SafeHaven release notes. In this case, it is [SafeHaven 5.0 Release Notes](../SafeHaven 5 General/SafeHaven5.0.0-Release-Notes.md). Once the file is downloaded, extract it, and run **safehaven-console.exe**.


### Create a New SafeHaven Cluster
1. Launch the **safehaven-console.exe**.
2. Click on **Create new cluster**.
3. Enter the **Organization Name** and the **License key** provided to you by your CenturyLink Resource. Click **Next**.
4. Fill in the following fields:  

   a. Enter **CMS Hostname**.

   b. **CMS Access IP** (used to connect to the SafeHaven Console GUI) and **CMS Service IP** (used for communication between CMS 		and SRN's). Typically the CMS Private IP address is entered in these fields although they can differ in some cases. You can 	get this information from the CMS Server deployed in the recovery datacenter which is AWS in this case.

   c. Set the **Administrator Password** (Password required to login to the SafeHaven Console GUI to manage the DR environment and 	initiate recovery operations).  

   d. Enter the **CMS root password**. You can get this information from the CMS Server deployed in the recovery datacenter which 		is AWS in this case.

    **NOTE**: Best practice is to use different passwords for Administrator and root user.

   e. Click on **Validate CMS Access** to confirm connectivity to the CMS.

   f. Copy the **Debian Package for CMS/SRN** link from the **Download Links** section of the most recent SafeHaven release notes.
   In this case, it is  [SafeHaven 5.0 Release Notes](../SafeHaven 5 General/SafeHaven5.0.0-Release-Notes.md) and enter it in the **SafeHaven distribution URL** field.

   **NOTE**:Please contact your CenturyLink Cloud Resource if you have any questions regarding the latest version of **Debian 
   Package for CMS/SRN**. Do not modify the Service Port (TCP), Heartbeat Port (UDP), Installation ID.

5. Click **Next**
6. A warning message will appear.
"By clicking continue, a fresh cluster will be installed. Previous configuration will be replaced. Are you sure to continue ?" Click on **Continue**.

7. Wait for the SafeHaven software to complete the configuration of the CMS server. When this process is complete, a pop-up window appears to let you know that the configuration was successful.
8. Click **OK** and then **Finish**.

	**NOTE**: The CMS will reboot as part of the installation procedure.

### Login to the SafeHaven Console
1. Login to the **SafeHaven Console** by using the **Client Access IP address** for the CMS.
2. Enter **Administrator** in the **User** field and enter the Administrator **Password** you had set during the cluster installation procedure stated above.
3. Click **Log In**.
2. **Install** the SSL Certificate (This will require Administrator rights).
3. The **SafeHaven Cluster** will appear and you can start configuring it.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/f3EZhkA39ak" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>

**Next Step** is to [Register Datacenters within a SafeHaven Console.md](Register Datacenters within a SafeHaven Console.md)
