{{{
"title": "Using Microsoft Azure",
"date": "01-20-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using Microsoft Azure

There are two different flavors of Azure and ElasticBox has providers for both. This document is in reference to Classic Azure.

**Name** | **URL of Portal** | **Name of Related ElasticBox Provider** | **KB article**
--- | --- | --- | ---
Classic Azure | https://manage.windowsazure.com | Microsoft Azure | [Using Classic Azure](../ElasticBox/using-azure.md)
Microsoft Azure | https://portal.azure.com | Azure Resource Manager | This document

Each of ElasticBox's Azure Resource Manager Providers gives you the option of setting it up either for an existing or a new Azure Customer Account. Existing accounts are your responsibility and will continue to be billed to you by Azure. New Accounts will automatically be generated on your behalf and the credentials pulled into the Provider via [Cloud Optimization](../ElasticBox/partner-cloud-integration.md), allowing you to hand off platform-level support and billing to CenturyLink.

If you want to learn how to use the New Account feature, please visit [Partner Cloud: Getting Started With a New Azure Customer](../ElasticBox/partner-cloud-integration-azure-new.md). The rest of this article assumes you will be using an existing, Azure Customer Account without any integration with CenturyLink.

If you do have an existing Azure account that you want CenturyLink to manage or support, please contact support@elasticbox.com. Please provide the name and domain of your account. Also, please describe any products, services, or resources within your Customer Account that are not currently shown in this list of [permitted products](./partner-cloud-integration-azure-permissions.md). We likely have already have begun work to enable your products.




### Before You Begin

You need an Microsoft Azure subscription to be able to consume Azure services. Follow these steps to create one.

### Steps

1. Login to the [Azure portal](https://portal.azure.com/) using your Microsoft Account.
2. Create a new Azure application in the Azure Active Directory. <b>Be sure to select "Native" when selecting the application type.</b>
3. Log back in to the Azure portal and go to subscriptions tab, select *Access Control (IAM)* and then select  *+ Add* on the new screen.
4. Select *Contributor* role. (If you do not see the Contributor role, you may need to talk to your administrator.)
5. Search for the application you just created in step 2 and click OK!
6. Return to the "App Registrations" panel in Step 2. Select the app, and select "Keys" in the "Settings" panel. Give the key any name and expiration date, and select "Save." The value of the key will be generated. Copy and keep the value (secret key) as you won't see it anymore once you navigate away.
7. Complete your Azure Resource Manager Provider for an existing account with the information below:
> Subscription ID: The active subscription ID<br>
> Client ID: The Application ID<br>
> Secret: The key value generated in Step 4<br>
> Tenant: Name of Customer URL (everything after @)<br>


Right now, template boxes are the only ones supported for Azure Resource Manager. If you cannot find a specific template that you are looking for in ElasticBox be sure to check out the [Azure github quickstart templates](https://github.com/Azure/azure-quickstart-templates).
