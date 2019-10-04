{{{
  "title": "Create Production SRN in vCenter",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to deploy a SafeHaven Replication Node(SRN) in VMWare vCenter.
SRN resides in both production and DR datacenters and work in pairs. A single SafeHaven Cluster can have upto 64 SRN's registered. This article explains how to deploy SRN in VMWare Production Datacenter.

### Requirements
1. Login access to the VMWare vCenter
2. Internet access on the Production SRN once it is deployed.

### Assumptions
This article assumes that the user has login access to Vcenter

### Create Production SRN in Vcenter.

1. Login to your Vcenter with your credentials.

2. Select the Resource pool under a host where the production SRN is to be deployed.

3. Click on **File**, then click on **Depoy OVF Template**

4. Download the SafeHaven Appliance OVA. The download link can be found under Download Links Section in [SafeHaven 5.0 Release Notes](../SafeHaven 5 General/SafeHaven5.0.0-Release-Notes.md)

5. Click on **Browse** and select the SafeHaveAppliance OVA file. Click **Next**

6. Verify the OVF template details :
Make sure that Product is **SafeHavenAppliance**, version is **5.0.x.x**, and Vendor is **CenturyLink Inc.**  
Click **Next**.

7. Enter the name fo the VM(e.g. SRN-PR), and select the Inventory Location. Click **Next**.

8. Select **Thick provision Lazy Zeroed** as the disk format. Click **Next**.

9. Select a Network for the VM. Click **Next**.

10. Enter the Network information of the VM: IP address, Netmask, Gateway and DNS server. Click **Next**

11. Verify all the properties of the VM. You may choose for the VM to automatically **power on the after deployment** by checking the box in fron of it. Click **Finish**.

**NOTE:** This will deploy an SRN in the vCenter. The deployment can take some time to complete. Once the deployment complete, the user can click on the VM and go to the **Summary** tab to verify all the proterties of the VM

**Next Step** is to [Create CMS in AWS](../SafeHaven 5 CLC to AWS/Create CMS in AWS.md)
