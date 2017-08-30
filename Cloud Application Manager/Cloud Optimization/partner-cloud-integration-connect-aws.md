{{{
  "title": "Partner Cloud Integration: Connecting Existing AWS Accounts for Optimization",
  "date": "8-17-2016",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Existing Accounts which are transferred into CenturyLink's care (a result of an approved Share-Shift agreement with AWS) have some options about what level of security they wish to bring to their account and corresponding level of access they wish to bring to CenturyLink. A basic overview of the options are:

1. Consolidated billing only
2. Everything in #1 plus Cost Optimization
3. Everything in #2 plus full account security hardening and CenturyLink operational access

### Audience

Customers responsible for AWS Accounts which have been approved by Amazon Web Services to perform a Share-Shift into CenturyLink's care.

### Prerequisites

* The customer must already have an AWS account that has been specifically mentioned on the AWS Share-Shift. (Only approved accounts are authorized for this process.)
* The customer must have reviewed the process for transferring an [existing Amazon Web Services account](./partner-cloud-integration-aws-existing.md)


### Important Information

When creating a new, AWS Provider in Cloud Application Manager, a user who selects "Migrate my account to CenturyLink for consolidated billing and Platform Support" has several options. The only option available for new accounts is Full Hardening. In the end, you are really determining which Account Role ARN, if any, you will be placing into the highlighted field, below.

![Account Role ARN](../../images/cloud-application-manager/CINT_AWS_AccountRoleARN.1.png)

Below is a table that will help you determine what permissions you wish to provide to CenturyLink. Below the table are steps to provide the level of access you have decided upon.

  Cloud Optimization Option | Benefits | IAM Permissions given to CenturyLink | Automated changes |
  --- | --- | --- | ---
  Consolidated billing only | [AWS Charges on a CenturyLink Invoice](./partner-cloud-integration-consolidated-billing.md); Discounts on EC2 Usage for Standard Customers | None | The account becomes a member of an organization, owned by CenturyLink. This results in consolidated billing. Please see review this page's [Considerations](./partner-cloud-integration-aws-existing.md) section.
  Cost Optimization | All the benefits listed above, plus [Analytics](./cloudapplicationmanageranalyticsui.md) | Read-Only | All the automated changes above, plus creates a role with a read-only policy and supplies the ARN back to CenturyLink's Analytics tool so that data regarding usage may be retrieved from the account.
  Full Hardening | All the benefits listed above, plus AWS-recommendations within the account for security, compliance, and support. | Admin | All the automated changes above for the purpose of [support](). Creates IAM Policies and Roles for CenturyLink Operations Staff to give them access to your account. Configures a secure password policy. Sets up an S3 audit bucket for CloudTrail and activates CloudTrail on that bucket, auditing all buckets in the linked account. Sets up the AWS Config service for regular compliance monitoring. Performs the steps [here](https://www.ctl.io/knowledge-base/cloud-application-manager/deploying-anywhere/using-your-aws-account/), providing standard permissions to Cloud Application Manager and syncs the provider.


### Steps

**Consolidated Billing Only**
1. Provide your AWS Account ID in the required field. You do not need to provide the Account Role ARN.

  The status of the Cloud Application Manager provider will not change because it will not synchronize. Please return to [existing Amazon Web Services account](./partner-cloud-integration-aws-existing.md) and continue with the remaining steps.

**Cost Optimization**
1. Provide your AWS Account ID in the required field.
2. Open the CloudFormation template found [here](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=CTL-CloudOptimization-IAM-Stack&templateURL=https%3A%2F%2Fs3.us-east-2.amazonaws.com%2Fctl-cloudoptimization%2FCTLCloudOptimizationIAMPolicy.template.json).
3. Login to the targeted AWS account, if not already.
4. Click “Next.”
5. Enter the External ID: (As listed by Cloud Optimization).
6. Click “Next.”
7. (Optional): Set any Options.
8. Click “Next.”
9. Check “I Acknowledge that AWS CloudFormation might create IAM resources.”
10. Click “Create.”
11. When Stack Creation Is Complete go to the “Outputs” tab.
13. Copy the “CTLCloudOptimizationRoleARN” Key’s Value (i.e., AWS ARN).
14. Paste the ARN into the Account Role ARN field of the AWS provider.

  The status of the Cloud Application Manager provider will not change because it will not synchronize. Please return to [existing Amazon Web Services account](./partner-cloud-integration-aws-existing.md) and continue with the remaining steps.

**Full Hardening**
1. Provide your AWS Account ID in the required field.
2. Log into your AWS Account
3. Navigate to IAM and Create Your Own Policy with the following Data:

  - Policy Name: CTLDeveloperPolicy

  - Description: Provides necessary access to AWS services and resources so that compliance-related services may be activated and other IAM policies and roles may be set up for CenturyLink Operational Staff.

  - Policy Document:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

4. Navigate to IAM and Create a New  Role with the following Data:
  - Role for Cross Account access
  - Provide access "between AWS accounts you own,"
  - Provide access to 589942003651. MFA not required.
  - Attach the CTLDeveloperPolicy
  - Role Name: CTLDeveloperRole
  - Description: Provides necessary access to AWS services and resources so that compliance-related services may be activated and other IAM policies and roles may be set up for CenturyLink Operational Staff.

5. When the role is created, click into it and copy the Role ARN.
6. Paste the ARN into the Account Role ARN field of the AWS provider.

  The status of the Cloud Application Manager provider will eventually change to "online: because it will should synchronize. Please return to [existing Amazon Web Services account](./partner-cloud-integration-aws-existing.md) and continue with the remaining steps.
