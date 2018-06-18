
{{{
  "title": "Register sites within a SafeHaven Console - CPC-vCF to CLC",
  "date": "04-30-2018",
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

### Register a Manual Site (CenturyLink Private Cloud on VMware Cloud Foundation/DCC-core/Hyper-V)

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left, and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name**, and select **Manual** as the **Data Center Type**. Click **Register**.

### Register a CLC site

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name** and select **CenturyLink Cloud** as the **Data Center Type**. Click **Register**.
3. Now click on the Data Center you registered and under the **Properties** Panel click on **Change Credentials**.
4. Enter the **username** and **password** of your Centurylink Portal account. Click **Next**.
5. Select an **Account** and **location**(Datacenter). Click **Finish**.

If you click on each datacenter, the **Properties** panel will show the information specific to that datacenter.

**Next Step** is to [Register SRN within SafeHaven Console](../SafeHaven 5 CLC to AWS/Register SRN within SafeHaven Console.md)
