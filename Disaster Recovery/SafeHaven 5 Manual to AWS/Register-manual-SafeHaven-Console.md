
{{{
  "title": "Register a Manual Site within a SafeHaven Console",
  "date": "03-21-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to register a manual data center within SafeHaven Console.

### Requirements
1. SafeHaven Cluster already installed and user needs to have access to it.
2. CMS and SRNs to have proper network connectivity as per SAHA5.0 Networking guide.

### Assumptions
1. User has login access to the SafeHaven Console.

### Register a Manual Site

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left, and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name**, and select **Manual** as the **Data Center Type**. Click **Register**.

### Register AWS Region
Each AWS Region is treated as a separate Datacenter within a SafeHaven Cluster.

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name** and select **Amazon Web Services** as the **Data Center Type**. Click **Register**.
3. Now click on the Data Center you registered and under the **Properties** Panel click on **Change Credentials**.
4. Enter your **Access Key ID** and **Security Key** for Amazon Cloud administration. Next, select your Recovery **Region** and Click **Next**.
5. Click **Finish**.

**Properties Panel** shows the Amazon Cloud information.

**Next Step** is to [Register SRN within SafeHaven Console](../SafeHaven 5 CLC to AWS/Register SRN within SafeHaven Console.md)
