{{{
  "title": "Partner Cloud: Getting Started With Azure Customer",
  "date": "01-16-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Starting in late January 2017, ElasticBox offers the Cloud Integration feature, giving users the ability to benefit from CenturyLink's partnerships with other cloud providers. CenturyLink takes integrates the billing  and assumes responsibility for support. This document is specific to our partner relationship with Azure and describes how you begin using Azure, provided by CenturyLink.

### Audience

All of our customers are invited to use Cloud Integration though ElasticBox

For Azure, we are currently limited to serving customers who are not resellers (or customers or resellers) with offices within the United States.

### Prerequisites

Access to ElasticBox.

Credentials for a [CenturyLink Cloud Account Administrator](../Accounts-&-Users/user-permissions.md). If you do not have access to CenturyLink Cloud, please contact your CenturyLink representative. (More on that, below.)

A working Knowledge how to use [ElasticBox providers](https://elasticbox.com/documentation/core-concepts/providers/).

An understanding of the features and benefits of [Partner Cloud Integration](../elasticbox/partner-cloud-integration.md)

For each CLC account hoping to integrate with Azure, both CenturyLink's and Microsoft's Terms and Conditions must be accepted. These will be presented to any user attempting to create a new "Azure Resource Manager" provider in ElasticBox.


### Important Information

We will bill monthly usage of Azure resources against a CenturyLink Cloud account you choose when setting up the account. Only a CenturyLink Cloud account administrator will be able to set up the new Azure customer account and select the CLC Account to bill against. Getting access to CenturyLink Cloud is very easy and free. You do not have to use CenturyLink cloud for anything other than the Account Administrator credentials. Please contact your CenturyLink representative for more details and to gain CenturyLink Cloud access.

Your aggregated charges in Azure will appear as a single CenturyLink Public Cloud line item, labeled as "Integrated Azure Services Usage." If you would like more detail, please submit a support request.

Currently, we will only create new Azure customer accounts. If you have an existing, Azure customer account for which you would like CenturyLink to assume support and billing responsibility, please contact your CenturyLink representative to discuss.

CenturyLink will manage Azure permissions for our customers to ensure we can support all resources provisioned there. Please review the [Azure permissions](../elasticbox/partner-cloud-integration-azure-permissions.md) to determine what Azure products and services are offered, currently. If there are other products or services you would like to allow CenturyLink to support, please email CloudIntegration-feedback@ctl.io or submit a service request.


### Steps

To set up a new ElasticBox provider designed to create a CenturyLink-supported Azure Customer account, please follow these steps:

1. Log into ElasticBox.
2. Select the Providers tab
3. Select New
4. Select "Azure Resource Manager"
5. Select the "Create a new Azure customer account" option
6. Provide a name for the provider that identifies it for your purposes.
7. Click the "Connect a CLC Account" button and provide your CenturyLink Cloud Account Administrator credentials
8. From the drop-down menu, select the CenturyLink Cloud account against which you would like to bill.
9. Accept the Terms and Conditions

Please expect at least a two-minute wait while our automated process performs the following:

* Provides Microsoft your account details
* Creates an Azure Customer account on your behalf
* Creates a Microsoft Azure Subscription for that Customer account
* Associates your Azure Customer account with your CenturyLink Cloud account
* Grants ElasticBox the appropriate permissions to work on your behalf
