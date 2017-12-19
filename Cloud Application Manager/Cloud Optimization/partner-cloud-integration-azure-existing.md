{{{
  "title": "Partner Cloud: Getting Started With An Existing Azure Customer Account",
  "date": "08-18-17",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}


### Overview

[Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) offers the Cloud Integration feature, giving users the ability to benefit from CenturyLink's partnerships with other cloud providers. CenturyLink integrates the billing and assumes responsibility for Azure support. This document is specific to Azure.

### Audience

All of our customers are invited to use Cloud Optimization via Cloud Application Manager.

For Azure, we are currently limited to serving billable customers who are not resellers (or customers of resellers) with offices within the United States. Also, the associated CenturyLink Cloud account cannot be a demo account or internal for CenturyLink employees. If you need special considerations for setting up an account, please email [cloudintegration@ctl.io](mailto:cloudintegration@ctl.io).

### Prerequisites

* Knowledge who your existing Azure Administrator is

* Access to Cloud Application Manager.

* The user must be an Administrator of the organization in Cloud Application Manager.

* A working knowledge of how to use [Cloud Application Manager providers](../Core Concepts/providers.md).

* An understanding of the features and benefits of [Partner Cloud Integration](partner-cloud-integration.md)

* For each CenturyLink Cloud account integrated with Azure, both CenturyLink's and Microsoft's Terms and Conditions must be accepted. These will be presented to any user attempting to create a new "Azure Resource Manager" provider in Cloud Application Manager.

### Important Information

![Microsoft Azure Provider Options](../../images/cloud-application-manager/CINT_Azure_Provider_Options1.png)

Cloud Application Manager Provider Verbiage | Description | Related Links
--- | --- | ---
Use an existing Azure customer account | This is not an optimized option. Customer pays Amazon for usage. | [Click here](../../Cloud Application Manager/Deploying Anywhere/using-microsoft-azure.md)
Migrate my account to CenturyLink for consolidated billing and Platform Support | **This is a Cloud Optimized option.** This allows an existing customer account to move under CenturyLink's care. | This document
Create a new Azure customer account | **This is a Cloud Optimized option.** Begins the new account creation automation, enabling the customer to immediately enter CenturyLink's care. | [Click Here](partner-cloud-integration-azure-new.md)

Charges for [Azure usage](partner-cloud-integration-consolidated-billing.md) will appear on invoices from CenturyLink.




### Steps

The following steps will walk through how to set up a Cloud Application Manager provider that has been designed to transfer an existing Azure Customer account into the scope of CenturyLink's responsibility.

NOTE: If the customer is already partnered with another provider, they may need to log into portal.office.com and remove the existing partnership. The Azure Admin will need to log in with Azure domain credentials, click "Partner Relationships" and select the existing provider to remove.

  ![Office 365 Administrator](../../images/cloud-application-manager/CINT_Office365Admin.png)

1. Log into Cloud Application Manager.
2. Select the Providers tab
3. Select New
4. In the Provider drop-down, select "Microsoft Azure"

  ![Microsoft Azure Provider](../../images/cloud-application-manager/CINT_New_ARM1.3.png)

5. Provide a name for the provider that identifies it for your purposes

6. Select the "Migrate my account to CenturyLink for consolidated billing and Platform Support" option. (If the user cannot see this option, they are not an organization Administrator.)

  ![Create New Azure Account](../../images/cloud-application-manager/CINT_Existing_ARM1.1.png)

7. Accept the Terms and Conditions

8. The user will receive an email shortly with a link that will need to be clicked by the existing Azure Administrator. Once clicked, they will be directed to an Office 365 sign in page. (Please contact Microsoft if you are not clear who this is.)

  ![Office 365 Administrator](../../images/cloud-application-manager/CINT_Office365_Accept.png)

9. The Azure Admin will need to log in with Azure domain credentials. They will be directed to a page where they must accept Terms and Conditions and authorize CenturyLink.

  ![Office 365 authorize](../../images/cloud-application-manager/CINT_Office365_AuthorizeCSP.png)

10. This is all it takes to move your Azure "Customer" tenant into CenturyLink's care. In some cases, work may need to be done to move your Azure Subscription(s) as well. This may require that your Azure Administrator give Owner access to a CenturyLink-generated user on the Subscription(s). If that is true, CenturyLink representatives will contact you guide you through this Microsoft-approved process.

11. CenturyLink will work with you to enable Cloud Application Manager to work on your behalf.

In the end, the following will have occurred:

* Microsoft will be provided with your account details
* Your Azure Customer account will be migrated under CenturyLink's care
* Your Microsoft Azure Subscription(s) for that Customer account will be migrated under CenturyLink's care
* Moves approved resources under CenturyLink's care for consolidated billing and platform-level support
* Grants Cloud Application Manager the appropriate permissions to work on your behalf

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
