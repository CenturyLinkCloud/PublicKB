{{{
  "title": "Register Azure Datacenters within a SafeHaven Console",
  "date": "06-14-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
Register Datacenters within the SafeHaven Console for Azure Cloud.

### Requirements
1. SafeHaven Cluster already installed and user has access to it.
2. CMS and SRNs to have proper network connectivity as per SAHA5.0.1 Networking guide.

### Assumptions
1. SafeHaven Cluster has already been installed with proper network connectivity between CMS-SRN and SRN-SRN.
2. A Service Principal on Azure for programatic access has been created.

### Register Azure Region
Each Azure Region is treated as a separate Datacenter within a SafeHaven Cluster.

1. Within the **SafeHaven Console**, right-click on the **Administrator@Cluster** in the Navigation Tree on the left and select **Register Data Center** from the drop-down menu.
2. Enter **Data Center Name** and select **Microsoft Azure** as the **Data Center Type**. Click **Next**.
3. Enter your **Azure Subscription ID**,  **Active Directory Tenant ID**, **Client Id** and **Client Secret** with the values obtained on previous KB [CreateServicePrincipalAzure] (CreateServicePrincipalAzure.md) using **subscription id**, **tenant**, **appId** and **password** respectively. Next, select your Recovery **Region** and Click **Next**.
5. Click **Add Site**.
6. The credentials will be validated by the SafeHaven console before declaring the operation successful.
