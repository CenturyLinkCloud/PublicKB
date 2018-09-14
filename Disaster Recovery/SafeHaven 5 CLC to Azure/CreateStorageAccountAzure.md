{{{
  "title": "Create Storage Account in Azure",
  "date": "06-13-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a storage account in order to store unmanaged disks in Azure, as part of the preparation for CMS and DR-SRN deployments. 

### Requirements
1. User must have an Azure account and permissions to create a storage account on a given Subscription.

### Assumptions
1. It is assumed here that the user has an Azure account and an active subscription. 

### Create a Storage Account in Azure
1. Go to the Azure portal https://portal.azure.com 
2. Go to **Storage accounts** service on the **Favorites** list or search for the service at top of the page next to the arrow glass.
3. Click on  the plus sign **Add**.
4. Provide a **Name** to the account. Leave the default _Resource manager_ option for **Deployment model**
5. Under **Account kind** select _Storage (general purpose v1)_. **Note** for more information on storage account types visit  https://docs.microsoft.com/en-us/azure/storage/common/storage-account-options 
6. Select a **Location** for the account. This is important as it will determine the DR Location for other SafeHaven resources like Virtual Machines and Virtual Networks.
7. For **Replication** select _Locally-redundant-storage (LRS)_.
8. Select _Standard_ under **Performance**
9. Leave the default _Disabled_ for **Secure transfer required**
10. Select a **Subscription** for the new storage account.
11. Under **Resource group** select _Create a new_ for  a new SafeHaven deployment or if you have done already select it accordingly from the list after clicking on the _Use existing_ radio button.
12. Click on the Create button to complete the process.
