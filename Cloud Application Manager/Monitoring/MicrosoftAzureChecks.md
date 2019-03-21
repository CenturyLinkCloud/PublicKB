{{{
  "title": "Microsoft Azure Checks",
  "date": "03-20-2019",
  "author": "Mindy Daugherty",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


**In this article:**
[Overview](#overview)
[Prerequisites](#prerequisites)
[Navigation](#navigation)
[Configure Policy] (#configurepolicy)


### Overview
Cloud Application Manager Monitoring features Microsoft Azure checks.  These checks will provide base-level infrastructure metrics and logs for Azure services.


![AzureCheckCatalog](../../images/AzureCheckCatalog.TIFF)

#### Prerequisites 
User must have access to Cloud Application Manager Monitoring Site, the workspace where the monitoring assets are configured, and should be at the organization level scope to access Settings.

User must also have access to the organization’s Azure account in order to obtain necessary information for the setup of an Azure check. 


#### Navigation 

The Policies tab, located in the left-hand navigation pane, provides a list of available policies as well as checks currently setup for your organization.


![NavigationPolicies](../../images/NavigationPolicies.TIFF)

#### Configure Policy

You can select a current policy or add a new policy in order to configure the setup. 

**Adding a New Policy:**
To create a new policy, click the **New** button on the top left side of the screen and follow the prompts to complete the **Creating Policy** screen. You will be required to enter a name for the policy as well as entering a description, define the Scope and Workspace, include any filters, and add any additional labels. You will also have the option to enable the policy now or unselect and enable at a later time. Click **Save Policy**.


![CreatingPolicy](../../images/CreatingPolicy.TIFF)

Once you have saved the policy, you will now be able to edit the policy and add a check. Click **Add** on the top right corner to continue on to select the check from the Check Catalog.

![AzureMetricTest](../../images/AzureMetricTest.TIFF)


On the Check Catalog screen, select the catalog from left-hand side menu then select the check or metric from the associated list and click **Configure**.

![AzureMetricCheckConfig](../../images/AzureMetricCheckConfig.TIFF)


To add a specific metric check for Azure, select **Azure Metric Check** and follow the prompts to configure the check. 

![AzureMetricCheckANNO](../../images/AzureMetricCheckANNO.TIFF)


Click **Show More** to view additional fields. For additional information about each field, click into the box for a descriptive tool tip.  

Once complete, click **Save Check** then follow the instructions below for the Azure piece of the setup. 

Log into the Azure portal (portal.azure.com) and navigate to ** All resources**.

![AzureNavigationANNO](../../images/AzureNavigationANNO.TIFF)


After selecting the resource, click on **Properties** under Settings.

![AzurePropertySettings](../../images/AzurePropertySettings.TIFF)


Next, locate the resource ID and click the blue icon on the right to copy the resource ID.

![AzureResourceID](../../images/AzureResourceID.TIFF)

Lastly, return to the Cloud Application Manager Monitoring site to edit the Azure Policy and paste the resource ID into the **Resource ID** field. Review the page for any additional fields that need to be completed such as Critical over and/or Warning over.

Click **Save Check** to complete the process. 

![AzureResourceFieldANNO](../../images/AzureResourceFieldANNO.TIFF)

After the check has been saved, it will then appear in the list of available Policies.
![AzureCheckCompleteANNO](../../images/AzureCheckCompleteANNO.TIFF)

