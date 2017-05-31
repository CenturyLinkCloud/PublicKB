{{{
  "title": "Cloud Application Manager AWS Native Monitoring Configuration - Manual",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Introduction
To supplement our [Managed OS Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/) offering in AWS we have released functionality to monitoring a customers servers via CloudWatch to augment our existing OS level monitoring capabilities as an optional feature. 

### Overview
The below process details the steps to manual configure your AWS account for CenturyLink's AWS Native Monitoring functionality.

If you prefer for set-up of your environment to be automated those setup steps can be found [here](CTLCloudMonitoringAWSSetupKB.md).  

#### Create CenturyLink Cloud Optimization IAM Policy
* Access the AWS IAM dashboard [here](https://console.aws.amazon.com/iam)
* Navigate to IAM "Policy"
* Click "Create Policy"
* Select "Create Your Own Policy"
* Name the Policy as "CTLCloudOptimizationPolicy"
* Add the following Description: "Access Policy for CTL's Cloud Optimization Functionality"
* Paste the CenturyLink Cloud Optimization IAM policy listed below (internal link)
* Click "Validate Policy"
* Click "Create Policy"

#### Create CenturyLink Cloud Optimization IAM Role
* Navigate to IAM "Roles"
* Click "Create New Role"
* Click "Role for Cross-account access"
* Select "Provide access between your AWS account and 3rd party AWS account"
* Add Account ID as: "540339316802"
* Add External ID as : [as provided by Cloud Optimization]
* Do NOT check "require MFA"
* Click "Next Steps"
* Select "ReadOnlyAccess"
* Click "Next Step"
* Name the Role as "CTLCloudApplicationManagerMonitoring"
* Add the following Description: "CTL's Cloud Application Manager Monitoring Functionality"
* Click "Create Role"

##### Apply ARN Policy to CTL Management Appliance
* Within in AWS navigate to the [EC2 section](http://console.aws.amazon.com/ec2/v2/)
* Right click CTL's Management Appliance, select 'Instance Settings' then 'Attach/Replace IAM role'
* Select 'CTLCloudApplicationManagerMonitoring' from drop down
* Click 'Apply'


##### Contact Operations for Monitoring Policy Configuration
* Contact operations [here](http://managedservices.ctl.io) to request addition of AWS native monitoring checks to supplement existing monitoring coverage for the Managed OS offering.
