{{{
  "title": "Partner Cloud: Requirements for Dedicated Edition",
  "date": "02-20-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Azure Cloud Integration is available for Cloud Application Manager Dedicated Edition as well as the Cloud Edition. There are special connectivity requirements that must be considered.

### Audience

Users of the Cloud Application Manager Dedicated Edition

### Prerequisites

Knowledge of how to get started with  [new cloud-optimized Azure](partner-cloud-integration-azure-new.md),  [new cloud-optimized AWS](partner-cloud-integration-aws-new.md), [existing cloud-optimized Azure](partner-cloud-integration-azure-existing.md) or [existing cloud-optimized AWS](partner-cloud-integration-aws-existing.md)

### Important Information

The Data Center Addition will need to have outbound port 443 for the following:

* https://api.ctl.io
* https://cloudintegration.ctl.io

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
