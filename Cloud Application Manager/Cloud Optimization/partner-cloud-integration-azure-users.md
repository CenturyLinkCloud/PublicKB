{{{
  "title": "Partner Cloud Integration: Obtaining Users to Portal.Azure.Com",
  "date": "07-20-2018",
  "author": "Kevin Quaintance",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Cloud Application Manager is a powerful tool for addressing many customers' needs. Regardless, a user may still want to log into portal.azure.com  occasionally to modify resources there.

### Audience

All of our customers are invited to use Cloud Optimization via Cloud Application Manager.
### Prerequisites

Knowledge of Cloud Application Manager's [partner cloud integration](partner-cloud-integration.md) feature.

An existing [Microsoft Azure Provider created by Cloud Application Manager](partner-cloud-integration-azure-new.md).

### Important Information

To obtain an Azure user account, please navigate to https://portal.azure.com/. If you automatically sign into a portal without being asked for your credentials, that can be confusing. You are likely already logged into another Microsoft account. Sign out of the account, navigate back to https://portal.azure.com/.  At this point you will see an option to create a new account.  Once your account is created, contact your Azure admin to add your access permissions.

**ADMIN Accounts**
For each CAM Customer, administrators of the first, Optimized Azure Subscription will receive Admin credentials and login URL. This can be obtained through the Edit screen of the Optimized, Azure provider. The admin user will receive the Owner role for that first subscription and *all future subscriptions created via Cloud Application Manager*.   If that Cloud Application Manager user also launches other Azure providers, their existing Azure user will also get the Owner role on the new subscriptions. A new Azure user will not be created.

![Admin Credentials](../../images/Admin-Creds.png) 

### Contacting Cloud Application Manager Support

If you are experiencing an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/), please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md) or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
