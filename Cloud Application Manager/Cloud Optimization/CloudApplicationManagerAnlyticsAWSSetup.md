{{{
  "title": "Cloud Application Manager Analytics AWS Configuration",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
The following process automates the configuration of an your AWS account for Cloud Application Manager Analytics functionality utilizing AWS CloudFormation functionality. You can inspect the code [here](https://s3.us-east-2.amazonaws.com/ctl-cloudoptimization/CTLCloudOptimizationIAMPolicy.template.json)

If you prefer to set-up your environment manually those setup steps can be found [here](CloudApplicationManagerAnalyticsAWSSetup-Manual.md).  

#### CenturyLink Cloud Optimization Configuration Steps:
* Open CloudFormation template [here](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=CTL-CloudOptimization-IAM-Stack&templateURL=https%3A%2F%2Fs3.us-east-2.amazonaws.com%2Fctl-cloudoptimization%2FCTLCloudOptimizationIAMPolicy.template.json)
* Login to targeted AWS account, if not already.
* Click “Next”
* Enter the External ID: [As listed by Cloud Optimization]
* Click “Next”
* (OPTIONAL): Set Options
* Click “Next”
* Check “I Acknowledge that AWS CloudFormation might create IAM resources”
* Click “Create”

##### When Stack Creation has completed
* Go to “Outputs” tab
* Copy “CTLCloudOptimizationRoleARN” Key’s Value (i.e. AWS ARN)
* Paste ARN into the Cloud Optimization Portal or send it to your on-boarding representative
