{{{
  "title": "Partner Cloud Integration: Usage Estimates for Optimized Accounts",
  "date": "01-17-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Use this API operation when you want to get the estimates of month-to-date and end-of-month charges for the Azure account for which CenturyLink provides platform-level support.

### Audience

All of our customers are invited to use Cloud Optimization via Cloud Application Manager.

### Prerequisites

* Knowledge of Cloud Application Manager's [partner cloud integration](partner-cloud-integration.md) feature.

* An existing [Optimized Provider created by Cloud Application Manager](partner-cloud-integration.md).

### Important Information

The estimates provided are based on the best information we have from our partner. It is possible for the estimate to be different than the total presented on a customer's invoice.


 **Month-To-Date:** In dollars, what CenturyLink estimates you would be billed if the month ended today. The month-to-date amount is based on information CenturyLink gets from Azure and is not intended to be 100% accurate.


 **End-of-month Estimate:** In dollars, what CenturyLink estimates you would be billed at the end of the month. The month-end estimation formula is prorated, based on the number of days in the month and the number of days remaining in the month. The formula assumes any recent spikes will be continued for the remainder of the month. As the month progresses, the estimate should get more and more accurate.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
