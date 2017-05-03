
{{{
  "title": "SafeHaven-4-Deploy SRN in VMware (Private or On-premise DataCenter)",
  "date": "05-01-2016",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

## Article Overview
This article explains how to deploy the SafeHaven Replication Node(SRN) in VMware (Private or On-premise DataCenter).

### Requirements

Login access to the production vCenter envirionment 

### Assumptions

This article assumes that the user has login access to the CenturyLink Cloud Portal. Begin by logging into the Control Portal at https://control.ctl.io 

![vmwareSRN](../../images/SH4.0/VMware_SRN/01.png)

### Deploy the SafeHaven Repliation Node(SRN) in VMwera

Login to the **VMware Data Center** with your credentials and select the appropriate **Host** and the appropriate **Resource Pool** to deploy the SRN. Click on **File**, choose **Deploy OVF Template...** from the drop-down menu.

Put https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova in **Deploy from a URL** blank and click on **next**.

![vmwareSRN](../../images/SH4.0/VMware_SRN/02.png)

Also you can find this URL in **Download Links** section in the [SafeHaven 4.0.1 Release Notes](safehaven-4.0.1-release.md).

![vmwareSRN](../../images/SH4.0/VMware_SRN/03.png)

Confirm the information of the OVF Template and click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/04.png)

Accept the End user license aggreement and click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/05.png)

 Provide a **Name** and **Inventory Location** for the SRN. Click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/06.png)

Choose a storage device for SRN deployment, click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/07.png)

Leave the default Disk Format and click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/08.png)

Confirm the Networking Mapping and click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/09.png)

Provide a **Networking Properties** for the SRN. Click on **Next**

![vmwareSRN](../../images/SH4.0/VMware_SRN/10.png)

Confirm the Deployment settings and click on **Finish** to start the deployment.

![vmwareSRN](../../images/SH4.0/VMware_SRN/11.png)

