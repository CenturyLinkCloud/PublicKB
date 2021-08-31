{{{
  "title": "Partner Cloud: Getting Started With A New Google Customer Account",
  "date": "04-20-21",
  "author": "Hannah Becker",
  "attachments": [],
  "contentIsHTML": false
}}}


### Overview

[Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) offers the Cloud Integration feature, giving users the ability to benefit from Lumen's partnerships with other cloud providers. Lumen integrates the billing and assumes responsibility for Google support. This document is specific to GCP.


### Audience

For Google Cloud Platform, see our [Service Guide](https://www.ctl.io/legal/cloud-application-manager/supplemental-terms/) for a current list of countries we support. Also, this offering is not for Lumen employees. If you need special considerations for setting up an account, please email request@centurylink.com.

### Prerequisites

* Access to Cloud Application Manager.

* The user must be an Administrator of the organization in Cloud Application Manager.

* You will need to create a [google cloud identity](../Getting Started/setup-cloud-identity-for-gcp.md) using your email.

* A working knowledge of how to use [Cloud Application Manager providers](../Core Concepts/providers.md).

* An understanding of the features and benefits of [Partner Cloud Integration](partner-cloud-integration.md)

* For each Lumen Cloud account integrated with GCP, both Lumen's and Google's Terms and Conditions must be accepted. These will be presented to any user attempting to create a new "Google Compute" provider in Cloud Application Manager. See our [Service Guide](https://www.ctl.io/legal/cloud-application-manager/supplemental-terms/) for a current list of countries we support.

### Important Information

Charges for [Google usage](partner-cloud-integration-consolidated-billing.md) will appear on invoices from Lumen.

### Steps

The following steps will walk through how to set up a new Cloud Application Manager provider that has been designed to do one of the following:
* Create a new Google Customer account.  
* If the CAM organization already has a Google Customer with at least one subscription, create another Azure subscription.

Subscriptions created in the manners above fall within the scope of Lumen's responsibility.

1. Log into Cloud Application Manager.
2. Select the Providers tab
3. Select New
4. In the Provider drop-down, select "Google Compute"
5. Write a name for the provider.
6. Select the "Create a new GCP account with Centurylink Cloud Optimization" option. (If the user cannot see this option, they are not an organization Administrator.)
7. Accept the Terms and Conditions
Please expect at least a few hours before we are able to process your request.
8. Click the "Google Console" button to access your GCP account.

### Contacting Cloud Application Manager Support

If you are experiencing an issue with [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/), please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
