{{{
  "title": "Cloud Application Manager Analytics AWS Configuration",
  "date": "12-13-2017",
  "author": "Benjamin Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This process details steps one would perform to manually configure AWS accounts for Cloud Application Manager Analytics functionality. These steps are not typically necessary. Automation will deliver these steps when Managed Services Anywhere, Optimization, or Bring-Your-Own Cloud Analytics are enabled.

The following process automates the configuration of your AWS account for Cloud Application Manager Analytics functionality by using native AWS CloudFormation functionality. You can inspect the code snippet [here](https://s3.us-east-2.amazonaws.com/ctl-cloudoptimization/CTLCloudOptimizationIAMPolicy.template.json).

If you prefer to set-up your environment manually, you can find those setup instructions [here](CloudApplicationManagerAnalyticsAWSSetup-Manual.md).  

### Audience

Customers responsible for AWS Accounts which have been approved by Amazon Web Services to perform a transfer into CenturyLink's care. (New, Optimized accounts are automatically enrolled with Analytics.)

### Prerequisites

* The customer must already have an AWS account that has been specifically mentioned in the AWS account transfer process. (Only approved accounts are authorized for this process.)
* The customer must have reviewed the process for transferring an [existing Amazon Web Services account](../Cloud Optimization/partner-cloud-integration-aws-existing.md)
* It is recommended the user or role performing these steps have full IAM permissions for both CloudFormation and IAM policies and Roles.

#### CenturyLink Cloud Optimization Configuration Steps:

1. Open the CloudFormation template found [here](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=CTL-CloudOptimization-IAM-Stack&templateURL=https%3A%2F%2Fs3.us-east-2.amazonaws.com%2Fctl-cloudoptimization%2FCTLCloudOptimizationIAMPolicy.template.json).
2. Login to the targeted AWS account, if not already.
3. Click “Next.”
4. Enter the External ID: (As provided by your on-boarding representative).
5. Click “Next.”
6. (Optional): Set any Options.
7. Click “Next.”
8. Check “I Acknowledge that AWS CloudFormation might create IAM resources.”
9. Click “Create.”

##### When Stack Creation Is Complete
1. Go to the “Outputs” tab.
2. Copy the “CTLCloudOptimizationRoleARN” Key’s Value (i.e., AWS ARN).
3. Send ARN to your on-boarding representative or into the Account Role ARN field of the AWS provider.

  ![Account Role ARN](../../images/cloud-application-manager/CINT_AWS_AccountRoleARN.1.png)
