{{{
  "title": "Partner Cloud Integration: Maintaining Users on the AWS portal",
  "date": "09-19-2018",
  "author": "Kevin Quaintance",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Cloud Application Manager is a powerful tool for addressing many customers' needs. Regardless, a user may still want to log into console.aws.amazon.com from occasionally to modify resources there.

### Audience

All of our customers are invited to use Cloud Integration via Cloud Application Manager.

### Prerequisites

Knowledge of Cloud Application Manager's [partner cloud integration](partner-cloud-integration.md) feature.

An optimized Amazon AWS account. [Click here for more information](partner-cloud-integration.md).

### Important Information

To obtain a user, please submit a support request via the following method:

* Email incident@CenturyLink.com

Our operations staff will confirm your identity according to protocol.
Within the request, please provide the list of users who require Access and a secure, quick method for CenturyLink to provide temporary passwords. We will deliver the credentials only to the person who made the request.

Once you have the user, navigate to https://console.aws.amazon.com/. If you automatically sign into a portal without being asked for your credentials, that can be confusing. You are likely already logged into another AWS account. Sign out of the account, navigate back to https://console.aws.amazon.com/, and try again.


### Contacting Cloud Application Manager Support

If you are experiencing an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/), please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md) or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
