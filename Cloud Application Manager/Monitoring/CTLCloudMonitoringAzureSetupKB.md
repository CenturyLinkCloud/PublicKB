{{{
  "title": "Cloud Application Manager Azure Native Monitoring Configuration",
  "date": "03-20-2018",
  "author": "Jason Oldham",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
The below process details the steps to manual configure your Azure account for CenturyLink's Azure Native Monitoring functionality.

#### Create CenturyLink Cloud Monitoring IAM Policy
* Access the Azure dashboard [here](https://portal.azure.com/)
* Click "Virtual machines" in the left-hand navigation and select your managed appliance VM
* Click Configuration and select Yes for Managed service identity, and click Save.
* Click Subscriptions in the left-hand navigation and click the subscription you want to apply your IAM policy to 
* Click Access control (IAM) and then click add
* Select the role from the dropdown
* Assign access to – Virtual Machine
* Select your subscription from the dropdown
* Select the Resource Group you want
* Select the management appliance VM
* Click save at the bottom

##### Contact Operations for Monitoring Policy Configuration
* Contact operations [here](http://managedservices.ctl.io) to request addition of Azure native monitoring checks to supplement existing monitoring coverage for the Managed OS offering.
