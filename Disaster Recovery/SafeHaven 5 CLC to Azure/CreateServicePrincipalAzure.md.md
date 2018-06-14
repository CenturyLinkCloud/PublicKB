{{{
  "title": "Create Storage Account in Azure",
  "date": "06-14-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a Service Principal in order to allow SafeHaven programatic access to Azure cloud. 

### Requirements
1. User must have an Azure account and permissions to login to the Azure portal.

### Assumptions
1. It is assumed here that the user has an Azure account, an active subscription and the right level of permissions at the subscription level. 

### Create a Service Principal in Azure
1. Go to the Azure portal https://portal.azure.com 
2. Identify your **Subscription id** by going to **Subscriptions** service on the **Favorites** list or search for the service at the top of the page next to the arrow glass.
3. Every subscription has a name as well, identify the one under SafeHaven resources will be created and billed and write down the Subscription Id.
4. Launch the **Cloud Shell** on the portal by clicking on the **>_** symbol on the top left of the screen. This will open a new section at the bottom of the screen where you can type commands using the Azure cli, if this is the first time you use  **Cloud Shell** please select _Bash_ for your environment.
5. Modify the following command adding your **Subscription id**. For instance if your subscription is 99999999-9999-9999-9999-999999999999 paste this command on the shell and type enter:
    ```bash
    az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/99999999-9999-9999-9999-999999999999"
    ```
6. The output of the command should be something like this:
    ```bash
    Retrying role assignment creation: 1/36
    {
        "appId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
        "displayName": "azure-cli-2018-XX-XX-XX-XX-XX",
        "name": "http://azure-cli-2018-XX-XX-XX-XX-XX",
        "password": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
        "tenant": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
    }
    ```
    This indicates the successful creation of a Service Principal with _Contributor_ level access to the specified subscription. 
    
7. Write down the values of **appId**, **password** and **tenant** along with the **subscription id** which will be needed on the next phase for the Azure site registration on SafeHaven.  
8. Click on the **>_** symbol on the top left of the screen to close **Cloud Shell**
