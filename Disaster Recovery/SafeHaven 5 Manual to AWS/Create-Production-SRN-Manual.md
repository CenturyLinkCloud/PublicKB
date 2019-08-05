{{{
  "title": "Create Production SRN in a Manual Site",
  "date": "03-14-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to deploy a SafeHaven Replication Node(SRN) in a Manual Production Site.
SRN resides in both production and DR datacenters and work in pairs. A single SafeHaven Cluster can have upto 64 SRN's registered.

### Requirements
Login access to the Manual Production Site.

### Assumptions
This article assumes that the user has login access to the Manual Production Site.

### Create Production SRN - If production site is CenturyLink Private Cloud on VMware Cloud Foundation
1. Login to the **CenturyLink Private Cloud on VMware Cloud Foundation** portal with your credentials.  
2. Upload the **SafeHaven OVA** (from the latest Release notes) to the CenturyLink Private Cloud on VMware Cloud Foundation portal. Once that is complete click on **Catalog**, then **SafeHaven**.  
3. Right-Click on **SafeHavenApplianceOVA** and select **Add to My Cloud**  
4. Enter a name for the VM, and click **Next**.  
5. Under **Configure Resources** tab, enter the **Virtual Machine** name, **Computer Name** (Can be same as VM name).  
   Click **Next**.
6. Under **Network Mapping**, keep the default configuration, and click **Next**.
7. Click **Next**, and go to **Custom Properties** page.  
	Enter **2 Virtual CPUs** and **4 GB RAM**. Click **Next**.
8. You may choose to power on the VM at the end of deployment. Click **FInish**.


### Create Production SRN - If production site is Hyper-V
1. Right click the Hyper-V host, and click on **New** > **Virtual Machine**
2. Enter the **Name** of the SRN VM. Click **Next**.
3. Select **Generation 1**, and click **Next**.
4. Enter **4092** MB in **Startup Memory**. Click **Next**
5. Under Connection, select an  existing virtual switch. If you don't have any existing switch, then select **New Virtual Switch**. Click **Next**.
6. Select **Use an existing virtual hard disk**.  
	Click **Browse** to select the SafeHaven Appliance Virtual Hard disk. It can be downloaded from [SafeHaven 5.0.0 Release Notes](../SafeHaven 5 General/SafeHaven5.0.0-Release-Notes.md)
	Click **Next**
7. Click **Finish**

**Note**: The SRN VM has been deployed. Next step is to edit some VM settings.

8. Right click the VM, and click **Settings**
9. Click on **Processor**, and increase the **number of virtual processors** to 2
10. Right click the VM, and click **Start**.
11. Right click the VM, and click **connect**.

**Note**: Please assign a static IP address to the VM.
You have now completed the deployment of SRN in a Manual Site.

**Next Step** is to [Create CMS in AWS](../SafeHaven 5 CLC to AWS/Create CMS in AWS.md)
