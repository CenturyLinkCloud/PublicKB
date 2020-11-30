{{{
  "title": "Create a SafeHaven Cluster",
  "date": "05-08-2017",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview

This article explains how to create a SafeHaven Cluster.

### Requirements

1. Pre-deployed CMS server.
2. Network access to the CMS.

### Assumptions

This article assumes that the user has already deployed the CMS server in Lumen Cloud.

To create CMS please refer to [Deploy CMS and SRN in Lumen Cloud](Deploy-CMS-and-SRN-in-CenturyLink-Cloud.md)

### SafeHaven Cluster Installation

**NOTE**: Please refer to the latest Safehaven Release Notes to download the  latest **GUI Package**

Begin by downloading the latest SafeHaven Console(GUI) from the [GUI Package](https://download.safehaven.ctl.io/SH-4.0.2/SafeHavenConsole-4.0.2.zip) download link under the **Download Links** section of the [SafeHaven 4.0.2 Release Notes](safehaven-4.0.2-release.md).

Launch the Console by clicking on its icon. Select **Create New Cluster**.

![Upgrade](../../images/SH4.0/Cluster/08.png)

Accept the **End User License Agreement** and click **Next**.

![Upgrade](../../images/SH4.0/Cluster/02.png)

Enter the **Customer Name** and the **License key** provided to you by your Lumen Engineer.

![Upgrade](../../images/SH4.0/Cluster/03.png)

Fill in the following fields:
1. CMS hostname in the **Node Name**
2. **Client Access IP** (CMS IP that used to connect to the SafeHaven Console GUI) and **Service Access IP** (CMS IP that is used for communication between CMS and SRN). Typically CMS Private IP address is entered in these fields. You can get this information from the Lumen Control Portal.
3. Set the **Administrator Password** (Password required to login to the SafeHaven Console GUI to manange the SafeHaven)
4. Enter the **CMS root password**. You can get this information from the Lumen Control Portal.
5. Click on **Test Login** to confirm connectivity to the CMS.
6. Copy the **Debian Package for CMS/SRN** link from the **Download Links** section of the [SafeHaven 4.0.2 Release Notes](safehaven-4.0.2-release.md) and enter it in the **SafeHaven 4.0.2 distribution URL** section. Please contact your Lumen Cloud Engineer if you have any questions regarding the latest version of **Debian Package for CMS/SRN**.
7. Do not modify the Service Port (TCP) , Heartbeat Port (UDP) , Installation ID.

Click **Next**

![Upgrade](../../images/SH4.0/Cluster/10.png)

Wait for the SafeHaven software to complete the configuration of the CMS server. When this process is complete, a pop-up window appears to let you know that the installation is successful.

Select **OK** and then **Finish**.

**NOTE**: The CMS will reboot as part of the installation procedure.

### Login to the SafeHaven Console

Login to the **SafeHaven Console** by using the **Client Access IP address** for the CMS. Enter **Administrator** in the **User** field and enter the Administrator **Password** you had set during the cluster installation procedure stated above. Click **Log In**.

![Upgrade](../../images/SH4.0/Cluster/09.png)

**Install** the SSL Certificate (This will require Administrator rights).

![Upgrade](../../images/SH4.0/Cluster/06.png)

The **SafeHaven Cluster** will appear which has now been created and you can start configuring it.

![Upgrade](../../images/SH4.0/Cluster/07.png)
