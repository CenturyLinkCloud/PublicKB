{{{
  "title": "Register Datacenters within a SafeHaven Console",
  "date": "12-27-2017",
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
SafeHaven Cluster has already been installed with proper network connectivity between CMS-SRN and SRN-SRN.

### Register CenturyLink Cloud Datacenter
Each CenturyLink Cloud Parent or Sub Account is treated as a separate Datacenter within a SafeHaven Cluster.

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left, and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name**, and select **CenturyLink Cloud** as the **Data Center Type**. Click **Next**.
3. Enter your **CenturyLink Portal Username** and **Password** for CenturyLink Cloud administration. Click **Retreive account information**. Choose Organization and Location. Click **Add Site**.


### Register AWS Region
Each AWS Region is treated as a separate Datacenter within a SafeHaven Cluster.

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name** and select **Amazon Web Services** as the **Data Center Type**. Click **Next**.
3. Enter your **AWS Access Key ID** and **Security Key** for Amazon Cloud administration. Next, select your Recovery  **Region** and click **Retreive account information**. Click **Add Site**.


**Properties Panel** shows the Amazon Cloud information.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/3GLZj9FoFBg" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>

**Next Step** is to [Register SRN within SafeHaven Console](Register SRN within SafeHaven Console.md)
