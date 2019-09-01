{{{
  "title": "Register vCenter and AWS Datacenter within a SafeHaven Console",
  "date": "01-12-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
Register Datacenters within the SafeHaven Console for CenturyLink Cloud and Amazon Cloud site types.

### Requirements
1. SafeHaven Cluster already installed and user needs to have access to it.
2. CMS and SRNs to have proper network connectivity as per SAHA5.0 Networking guide.

### Assumptions
1. User has login access to the SafeHaven Console.
2. The machine which is running SafeHaven Console has reachability to user's vCenter environment.

### Register VMWare vCenter

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left, and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name**, and select **vCenter** as the **Data Center Type**. Click **Register**.
3. Click on the Data Center you registered and under the **Properties** Panel. Click **Register**.
4. Enter a **vCenter Identifier**. This can be any name for the vCenter. Enter the **IP Address**, **User Name** and **Password** for the datacenter. Make sure that username has permissions to perform power operations on the VMs within the vCenter. Click **Register**.

**Properties Panel** shows the vCenter information.

### Register AWS Region
Each AWS Region is treated as a separate Datacenter within a SafeHaven Cluster.

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name** and select **Amazon Web Services** as the **Data Center Type**. Click **Register**.
3. Now click on the Data Center you registered and under the **Properties** Panel click on **Change Credentials**.
4. Enter your **Access Key ID** and **Security Key** for Amazon Cloud administration. Next, select your Recovery **Region** and Click **Next**.
5. Click **Finish**.

**Properties Panel** shows the Amazon Cloud information.

**Next Step** is to [Register SRN within SafeHaven Console](../SafeHaven 5 CLC to AWS/Register SRN within SafeHaven Console.md)
