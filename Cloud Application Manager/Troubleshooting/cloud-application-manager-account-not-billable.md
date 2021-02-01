{{{
"title": "Error When Alias is Not Billable",
"date": "02-20-2017",
"author": "Ben Swoboda",
"attachments": [],
"contentIsHTML": false
}}}

<iframe width="560" height="315" src="https://player.vimeo.com/video/204243772" frameborder="0" allowfullscreen></iframe>

### Introduction

Lumen Cloud does not currently sell Azure through [Cloud Application Manager](https://www.ctl.io/cloud-application-manager) to the following types of accounts:
* Resellers
* Internal accounts
* Demo accounts
* Sub-accounts of those categories listed above

### Non-Billable Accounts

The following error will appear if the Lumen Cloud account alias you provide is a reseller, internal, demo or sub-account, and is therefore designated "not billable."

![Cloud Application Manager Error: Account Not Billable](../../images/cloud-application-manager-billable2.png)

Here's how you might arrive at this error message. After you log into Cloud Application Manager, click the **Provider** tab on the top toolbar.

![Cloud Application Manager Create New Provider](../../images/cloud-application-manager-error3.png)

Then click **New Provider** on the left navigation bar.

Select **Microsoft Azure** to build a customer account in the current Microsoft Azure. Note: this is the new Azure, not the classic Azure. The dialog box that appears will enable you to create a new Azure customer account. Add a name for the account and select the **Create a new Azure Subscription** option.

![Cloud Application Manager New Provider Details](../../images/cloud-application-manager-error4.png)

### The Exception Message

If the Lumen Cloud billing account is the wrong account type, the following error message will appear, indicating we're not permitted to offer the product to you.

"Thank you for your interest in integrated Azure. Our apologies, but we are not able to provide this functionality for your account. Please submit a support request if you would like us to review your situation in further detail."

If you send us a support request we will review your case.

![Cloud Application Manager Error: Account Not Billable](../../images/cloud-application-manager-billable2.png)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
