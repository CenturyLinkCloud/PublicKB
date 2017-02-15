{{{
  "title": "Partner Cloud: Getting Started With A New Azure Customer Account",
  "date": "12-28-16",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}


### Overview

[Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) offers the Cloud Integration feature, giving users the ability to benefit from CenturyLink's partnerships with other cloud providers. CenturyLink integrates the billing and assumes responsibility for Azure support. This document is specific to Azure.

### Audience

All of our customers are invited to use Cloud Integration via Cloud Application Manager.

For Azure, we are currently limited to serving billable customers who are not resellers (or customers of resellers) with offices within the United States. Also, the associated CenturyLink Cloud account cannot be a demo account or internal for CenturyLink employees. If you need special considerations for setting up an account, please email [cloudintegration@ctl.io](mailto:cloudintegration@ctl.io).

### Prerequisites

* Access to Cloud Application Manager.

* Credentials for a [CenturyLink Cloud Account Administrator](../Accounts & Users/user-permissions.md). If you do not have access to CenturyLink Cloud, please contact your CenturyLink representative or sign up for an account [here](https://www.ctl.io/free-trial/). 

* A working knowledge of how to use [Cloud Application Manager providers](https://elasticbox.com/documentation/core-concepts/providers/).

* An understanding of the features and benefits of [Partner Cloud Integration](./partner-cloud-integration.md)

* For each CenturyLink Cloud account integrated with Azure, both CenturyLink's and Microsoft's Terms and Conditions must be accepted. These will be presented to any user attempting to create a new "Azure Resource Manager" provider in Cloud Application Manager.


### Important Information

CenturyLink bills Azure usage against a specific CenturyLink Cloud account monthly. Only an Administrator of your CenturyLink Cloud account should be able to approve this usage. Getting access to CenturyLink Cloud is easy and free. You do not have to use CenturyLink Cloud for anything other than the Account Administrator credentials.

Your charges in Azure will appear as a CenturyLink Public Cloud line item, labeled as "**Integrated Azure Services Usage**".

If you have an existing, Azure customer account for which you would like CenturyLink to assume support and billing responsibility, please contact your CenturyLink representative to discuss.

CenturyLink will manage Azure permissions for our customers to ensure we can support all resources provisioned there. The [Azure permissions can be viewed here](./partner-cloud-integration-azure-permissions.md) to determine what Azure products and services are offered, currently. If there are other resources you would like to allow CenturyLink to support, please email [CloudIntegration-feedback@ctl.io](mailto:cloudintegration@ctl.io) or submit a [service request](./partner-cloud-integration-azure-support.md).


### Steps

The following steps will walk through how to set up a new Cloud Application Manager provider that has been designed to create an Azure Customer account within the scope of CenturyLink's responsibility.

1. Log into Cloud Application Manager.
2. Select the Providers tab
3. Select New
4. Select "Azure Resource Manager"

  ![Azure Resource Manager Provider](../images/cloud-application-manager/CINT_New_ARM1.png)

5. Select the "Create a new Azure customer account" option

  ![Create New Azure Account](../images/cloud-application-manager/CINT_New_ARM2.png)

6. Provide a name for the provider that identifies it for your purposes
7. Click the "Connect a CLC Account" button and provide your CenturyLink Cloud Account Administrator credentials

  ![Create New Azure Account](../images/cloud-application-manager/CINT_New_ARM3.png)

8. From the drop-down menu, select the CenturyLink Cloud account you would like to bill against.
9. Accept the Terms and Conditions

Please expect at least a two-minute wait while our automated process performs the following:

* Provides Microsoft your account details
* Creates an Azure Customer account on your behalf
* Creates a Microsoft Azure Subscription for that Customer account
* Associates your Azure Customer account with your CenturyLink Cloud account
* Grants Cloud Application Manager the appropriate permissions to work on your behalf
