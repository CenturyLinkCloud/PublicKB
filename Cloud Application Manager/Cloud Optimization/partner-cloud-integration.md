{{{
  "title": "Partner Cloud Integration",
  "date": "8-17-2016",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Partner Cloud Integration allows an Cloud Application Manager user to leverage CenturyLink’s partnerships with third-party cloud providers to easily manage a multi-cloud strategy.

We have integrated with Microsoft Azure and Amazon Web Services.

### Audience

All of our customers are invited to use Cloud Application Manager's Cloud Integration capabilities.

For Azure, we are currently limited to serving customers who are not resellers (or customers or resellers) with offices within the United States and the United Kingdom.
For Amazon Web Services we are currently limited to serving customers who are not resellers (or customers or resellers) with offices within the United States.

### Prerequisites

Access to Cloud Application Manager.

Credentials for a [CenturyLink Cloud Account Administrator](../../Accounts & Users/user-permissions.md)

A working Knowledge how to use [Cloud Application Manager providers](../Core Concepts/providers.md).

For each CLC account hoping to integrate with Azure, both CenturyLink's and vendor-specific and region-specific Terms and Conditions must be accepted. These will be presented to any user attempting to select any of the following options for Microsoft Azure or Amazon Web Services providers in Cloud Application Manager.



### Important Information





Current features of Partner Cloud Integration include:
* **Mapping New Azure Customer Accounts with CLC Account:** For each CLC account meeting the requirements (above), a new Azure Customer account will be created and a relationship between the CLC and Azure accounts will be persisted.
* **Integrated Billing:** All charges within the partner account will be shown as a single, CenturyLink Cloud 1.0 line item on the invoice for the account. I will represent aggregated totals.
* **Month-To-Date Totals:** Accumulated usage in partner clouds will be available via API.
* **Estimated Totals:** Estimated month-end usage for partner clouds will be available via API.
* **Access to Azure's Control Portal:** If you would like to log into portal.azure.com, you will need a user. Please submit a request for user creation via a ticket. You may also simply continue to use Cloud Application Manager to manipulate Azure resources.
* **Partner List Pricing:** Our pricing is consistent with whatever price our partners sell products.
* **Support:** CenturyLink takes on responsibility for platform-level support with Azure resources related to IaaS: Virtual Machines, Storage, Network, and Resource Groups.



**Standard Support Details:**

Please see our Knowledge Base article detailing [Azure platform-level support](partner-cloud-integration-azure-support.md).

For additional details on support responsibilities for our partners and their SLAs we support, please see the table below.

**Additional Support and Management:**
* The true strength of Cloud Integration is that it opens to door for trained, CenturyLink resources to do work for you on your behalf, in Azure. If you are interested in contracting with CenturyLink to provide design, implementation, or ongoing, additional support, request an engagement with your sales representative.

**Partner Pricing Details:**
* **Azure:** Pricing available to CenturyLink customers is shown [here](https://www.ctl.io/pricing), with some variability as Microsoft changes pricing daily. Available products are also listed [here](partner-cloud-integration-azure-capabilities.md). If your organization has agreements with Microsoft which differ from what is shown, please submit a ticket for review. We are constantly working to increase the scope of what is offered through Azure and it is likely we have plans to offer what you require.

**Availability**
* **General:**

  Cloud Integration is currently not available for resellers. Our automation prevents offering this service to resellers or customers of resellers. If you would like us to review your particular use case, please submit a support ticket with your contact details so we can discuss your scenario.

* **Azure:**

  All Microsoft products made available by Microsoft to Cloud Partners via Azure are part of our offering.

  We are currently able to offer this service only to offices inside the United States. Our automation prevents offering this service to CLC accounts which have billing addresses outsides the US. Please submit a support ticket if you feel your situation requires additional review.

  To get started with Azure, please review [Partner Cloud: Getting Started With Azure Customer](partner-cloud-integration-azure-new.md)

**Partner Responsibility:**

  Partner | Cloud | Responsibility | Details
--- | --- | --- | ---
CenturyLink  | Azure |   **Azure platform-level support:** https://portal.azure.com users; Account Sign-up and Set-up; Knowledge Base and FAQs; Service availability; Billing; Subscription management; Basic Technical Support; Configuration review; Azure Control Portal; Partner cloud month-to-date totals; Partner cloud estimates; Terms and Agreements; Estimates for Month-To-Date and month-end usage | Available through Cloud Application Manager. Terms and Conditions contained therein. The easiest way to create a support ticket is through the ticketing functionality of Cloud Application Manager.
CenturyLink | Azure | ** Managed OS. ** For the moment, this in-depth level of support for Windows and RedHat OS-es are not available in Azure. The objective of this services is to provide Remote Administration, Monitoring, ticketing specific to the resources, and Patching for the OS. | Not yet available in Azure
CenturyLink IT Service Management | Azure | **Per agreement.** Design and delivery. Potentially including application architecture, consulting services, solution design, configuration, installation and migration.| Contact your account representative.
CenturyLink Service Management | Azure | **Per agreement** For run-state environments following design and deliver. Potentially including Account Management, Technical Account management, governance, and application management. | Contact your account representative.
Microsoft | Azure | **Infrastructure** Troubleshoot and provide technical guidance for customer issues escalated through CenturyLink including undocumented scenarios and service impacting events.  | [Microsoft SLA](http://www.microsoftvolumelicensing.com/DocumentSearch.aspx?Mode=3&DocumentTypeId=37)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
