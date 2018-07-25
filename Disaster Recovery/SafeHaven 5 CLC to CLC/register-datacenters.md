{{{
  "title": "Register Datacenters within a SafeHaven Console",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
Register Datacenters within the SafeHaven Console for CenturyLink Cloud and Amazon Cloud site types.

### Requirements
1. SafeHaven Cluster already installed and user needs to have access to it.
2. CMS and SRNs to have proper network connectivity as per SAHA5.0 Networking guide.

### Assumptions
SafeHaven Cluster has already been installed with proper network connectivity between CMS-SRN and SRN-SRN.

### Register CenturyLink Cloud Datacenter
Each CenturyLink Cloud Parent or Sub Account is treated as a separate Datacenter within a SafeHaven Cluster.

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left, and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name**, and select **CenturyLink Cloud** as the **Data Center Type**. Click **Register**.
3. Click on the Data Center you registered and under the **Properties** Panel. Click on **Change Credentials**.
4. Enter your **CenturyLink Portal Username** and **Password** for CenturyLink Cloud administration. Click **Next**.
5. Select your **parent account** or **sub-account** as well as the CenturyLink Data Center **Location**. Click **Finish**.

**Properties Panel** shows the CenturyLink Cloud information.
