{{{
  "title": "Cloud Application Manager AWS Native Monitoring Configuration",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Introduction
To supplement our [Managed OS Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/) offering in AWS we have released functionality to monitoring a customers servers via CloudWatch to augment our existing OS level monitoring capabilities as an optional feature. 

### Overview
The following process automates the configuration of an your AWS account for CenturyLink’s Cloud Application Manager AWS Native Monitoring functionality utilizing AWS CloudFormation functionality. You can inspect the code [here](https://s3.us-east-2.amazonaws.com/ctl-cloudoptimization/CTLCloudMonitoringIAMPolicy.template.json).

If you prefer the manual setup steps can be found [here](CTLCloudMonitoringAWSSetupKB-Manual.md)

#### CenturyLink Cloud Application Manager AWS Native Monitoring Configuration Steps:
* Open [Link](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=CTL-CloudApplicationManagerMonitoring-IAM-Stack&templateURL=https%3A%2F%2Fs3.us-east-2.amazonaws.com%2Fctl-cloudoptimization%2FCTLCloudMonitoringIAMPolicy.template.json)
* Login to targeted AWS account, if not already.
* Click “Next”
* Click “Next” again
* (OPTIONAL): Set Options
* Click “Next”
* Check “I Acknowledge that AWS CloudFormation might create IAM resources”
* Click “Create”
* Validate CloudFormation Template has completed successfully

##### Apply ARN Policy to CTL Management Appliance
* Within in AWS navigate to the [EC2 section](http://console.aws.amazon.com/ec2/v2/)
* Right click CTL's Management Appliance, select 'Instance Settings' then 'Attach/Replace IAM role'
* Select 'CTLCloudApplicationManagerMonitoring' from drop down
* Click 'Apply'


##### Contact Operations for Monitoring Policy Configuration
* Contact operations [here](http://managedservices.ctl.io) to request addition of AWS native monitoring checks to supplement existing monitoring coverage for the Managed OS offering.
