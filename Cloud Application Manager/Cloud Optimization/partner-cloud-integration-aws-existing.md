{{{
  "title": "Partner Cloud: Getting Started With An Existing AWS Customer Account",
  "date": "03-31-18",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}


### Overview

[Cloud Application Manager's](https://www.ctl.io/cloud-application-manager/) Cloud Optimization gives users the ability to benefit from CenturyLink's partnerships with other cloud providers. CenturyLink assumes the billing for these accounts and takes responsibility for platform support. Users may also benefit from Security hardening and cost Optimization. This document is about using Cloud Optimization with existing Amazon Web Services accounts.

### Audience

To migrate an existing, AWS account, Customers must gain approval from AWS. Please contact your CenturyLink representative for more details.

For Amazon Web Services, we are currently limited to serving billable customers who are not resellers (or customers of resellers) with offices within the United States. Also, the associated CenturyLink Cloud account cannot be a demo account or internal for CenturyLink employees. If you need special considerations for setting up an account, please email [cloudintegration@ctl.io](mailto:cloudintegration@ctl.io).

### Prerequisites

* Approval from Amazon Web Services in the form of an agreement.

* Access to Cloud Application Manager.

* The user must be an Administrator of the organization in Cloud Application Manager.

* A working knowledge of how to use [Cloud Application Manager providers](../Core Concepts/providers.md).

* An understanding of the features and benefits of [Partner Cloud Integration](partner-cloud-integration.md)

* For each CenturyLink Cloud account integrated with Amazon Web Services, both CenturyLink's AWS Terms and Conditions for the relevant territory must be accepted. These will be presented to any user attempting to create a new "Amazon Web Services" provider in Cloud Application Manager.

### Important Information

Charges for [AWS usage](partner-cloud-integration-consolidated-billing.md) will appear on invoices from CenturyLink.

![Amazon Web Services Provider](../../images/cloud-application-manager/CINT_AWS_Provider_Options.png)

Cloud Application Manager Provider Option | Description | Related Links
--- | --- | ---
 Use an existing AWS customer account | This is not an Optimized account and customer pays Amazon for usage. | [Click here](../Deploying Anywhere/using-your-aws-account.md)
   Migrate my account to CenturyLink for consolidated billing and Platform Support | **This is a Cloud Optimized option.** Provided Amazon has approved agreement, this allows an existing customer account to move under CenturyLink's care. | This page
  Create a new AWS account for consolidated billing and Platform Support | **This is a Cloud Optimized option.** Initiates the new account creation process, enabling the customer to immediately enter CenturyLink's care without prior approval from AWS. | [Click Here](partner-cloud-integration-aws-new.md)

Most Amazon Web Services offering are available through CenturyLink.

**Considerations**


* **Data changes** Optimized accounts have access to use Cloud Application Manager's [Analytics](../Analytics/CloudApplicationManagerAnalyticsUI.md) and [Monitoring](../Monitoring/CTLCloudMonitoringUI.md) tools for usage details that would have been provided by AWS Billing Services such as Cost Explorer and to offer our customers visibility into the status of their environment.
* **Historical Usage Data** Such as that had been used by AWS Cost Explorer - will be lost when accounts migrate under a new Master Payer. CenturyLink recommends Customers download all necessary usage data to a safe repository prior to completing the following steps.
* **Data Access** Customers will not be given access to consolidated data within the CenturyLink-owned Master Payers. Optimized accounts have access to use Cloud Application Manager's [Analytics](../Analytics/CloudApplicationManagerAnalyticsUI.md) tool for usage details.
* **Tagging Changes.** The quantity of unique [Cost Allocation tag keys](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) available to Customers, such as those used for AWS Cost Explorer, are limited. Customers can have (hypothetically) an unlimited quantity of unique Cost Allocation tag values. If you have concerns, please contact your sales representative or submit a support ticket prior to migration to discuss your Cost Allocation tagging requirements.
* **Reserved Instances**
  * Purchased prior to transferring to CenturyLink must always stay with the account at which they were purchased.  If the Customer purchased Reserved Instances from a Master Payer they own, they can still use them.
  * Customers may contact CenturyLink if they wish to have their Reserved Instance limit increased.
* **Master Payers.** AWS will not allow existing, customer-owned Master Payers to remain as Master Payers when accounts are moved to CenturyLink billing. If they are to move, it must transition in as a linked account:
  * [unlink all their member from their Master Payer](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html),
  * [delete their organization in the master](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_delete.html),
  * complete the steps below for all their accounts.
  * Any Reserved Instances held at the once-master-now-linked account still may be  shared with other, customer-owned linked accounts.


### Steps

The following steps will walk through how to set up a Cloud Application Manager provider that has been designed to transfer an existing Amazon Web Services Customer account into the scope of CenturyLink's responsibility.

1. Log into Cloud Application Manager.
2. Select the Providers tab
3. Select New
4. Select "Amazon Web Services"

  ![Amazon Web Servies Provider](../../images/cloud-application-manager/CINT_New_AWS_Provider.1.png)

5. Provide a name for the provider that identifies it for your purposes

6. Select the "Migrate my account to CenturyLink for consolidated billing and Platform Support" option. (If the user cannot see this option, they are not an organization Administrator.)

  ![Migrate AWS Account](../../images/cloud-application-manager/CINT_Existing_AWS_Provider.2.png)

7. Enter the AWS Account ID

8. Determine what level of permissions you will be providing to CenturyLink. Enter one of the [recommended ARNs](partner-cloud-integration-connect-aws.md) into the Account Role ARN field. The actions to follow correspond with the what permissions you provided when you selected the associated ARN. Once you have completed that, return to this document and continue.

9. Accept the Terms and Conditions

10. Accept the invitation. An invitation will be sent to the account from CenturyLink. AWS notifies the root user of the account in two different ways: an email sent to the email address of the root user, and an invitation within the "My Organization" feature of the Customer account. To a accept the invitation, follow these steps afer logging into the account with your root user:

  * Navigate to "My Organization"

![Navigate to My Organization](../../images/cloud-application-manager/CINT_AWS_Invitation1.png)

  * Click Invitations.

![Click Invitations](../../images/cloud-application-manager/CINT_AWS_Invitation2.png)

  * Check that the invite is from a CenturyLink account and accept it.

![Check the invite](../../images/cloud-application-manager/CINT_AWS_Invitation3.png)

  * Confirm joining the organization.

![Confirm joining](../../images/cloud-application-manager/CINT_AWS_Invitation4.png)

11. Ensure Enterprise Support.  Standard customers with accounts moving under CenturyLink's care will be required to change their accounts' Support plans. A root user must sign into the account with root account credentials (email address and password) to change a support plan. The cost of the support plan does not appear on your consolidated, CenturyLink bill, but it is required so that CenturyLink may meet our Service Level Objectives and use our automated tools. In addition, Amazon Web Services requires it so that proper prioritization is given to any platform-level issues that may need to be addressed.

  Standard Customers must select Enterprise Support.

  * Navigate to support.


  ![Navigate to Support Center](../../images/cloud-application-manager/CINT_AWS_SupportPlan_Change1.png)

  * Navigate to Support Center


  ![Navigate to Support Center](../../images/cloud-application-manager/CINT_AWS_SupportPlan_Change2.png)

After your account becomes a member of the CenturyLink-owned AWS organization, consolidated billing will occur immediately. If you selected Full Hardening for your account, you may need to wait a while for our automation to run because it performs a scheduled check for any new, member organizations which have given the appropriate access.


### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
