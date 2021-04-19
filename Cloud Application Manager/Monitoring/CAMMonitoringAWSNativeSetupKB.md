{{{
  "title": "Cloud Application Manager AWS Native Monitoring Configuration",
  "date": "03-20-2018",
  "author": "Jason Oldham",
  "attachments": [],
  "contentIsHTML": false
}}}

### Introduction
To supplement our [Managed OS Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/) offering we offer functionality to monitor native AWS Services via CloudWatch to augment our existing OS level monitoring capabilities as an optional feature. 

### Overview
The below process details the steps to configure your AWS account for Lumen's AWS Native Monitoring functionality.

#### Create Lumen Cloud Monitoring IAM Role
* Navigate to IAM 'Roles'
* Click 'Create Role'
* Select 'EC2' for the services
* Click 'Next'
* Select 'ReadOnlyAccess'
* Click 'Next'
* Name the Role as "CTLCloudApplicationManagerMonitoring"
* Add the following Description: "CTL's Cloud Application Manager Monitoring Functionality"
* Click 'Create Role'

##### Apply ARN Policy to CTL Management Appliance
* Within AWS navigate to the [EC2 section](http://console.aws.amazon.com/ec2/v2/)
* Right click CTL's Management Appliance, select 'Instance Settings' then 'Attach/Replace IAM role'
* Select 'CTLCloudApplicationManagerMonitoring' from drop down
* Click 'Apply'

##### Contact Operations for Monitoring Policy Configuration
* Contact our operations team [here](http://managedservices.ctl.io) to request the configuration of AWS native monitoring checks in your enviorment to supplement existing monitoring coverage for the Managed OS offering.
